"""Insert printed-page markers into the SGA 5 or SGA 6 TeX (diplomatic and corrected layers), in the SGA 7 format
    %%%%%%%%%%  scan idx N  |  folio F  %%%%%%%%%%
on a line of its own just before the first word of printed page F (a line break inside a paragraph is a space in TeX,
and the comment line adds nothing to the output).

The page starts are found by aligning the words of the scan's own OCR text (SGA 5: the page-aligned DjVu OCR of the
same scan; SGA 6: the text layer of the Internet Archive PDF) with the words of the TeX: accent-free words of four or
more letters, lower case, in order. Pages whose start cannot be placed are listed; the checkers report any marker
that is off ("kind": "marker").

usage: python -I insert_markers.py VOL [--apply]      (VOL = 5 or 6)
"""
import difflib
import json
import pathlib
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import MARK, VOLS, W, files  # noqa: E402

vol = sys.argv[1]
apply = "--apply" in sys.argv
v = VOLS[vol]
DJVUTXT = r"C:\Program Files (x86)\DjVuLibre\djvutxt.exe"
FIRST, LAST = {"5": (1, 484), "6": (1, 700)}[vol]
ocr_dir = W / f"ocr_{vol}"
ocr_dir.mkdir(exist_ok=True)


def ocr_page(folio):
    p = ocr_dir / f"page_{folio:03d}.txt"
    if not p.exists():
        filepage = v["idx_of"](folio) + 1
        if vol == "5":
            r = subprocess.run([DJVUTXT, f"--page={filepage}", str(v["scan"].with_suffix(".djvu"))],
                               capture_output=True)
        else:
            r = subprocess.run(["pdftotext", "-enc", "UTF-8", "-f", str(filepage), "-l", str(filepage), str(v["scan"]),
                                "-"], capture_output=True)
        p.write_bytes(r.stdout)
    return p.read_text(encoding="utf-8", errors="replace")


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)).lower()


WORD = re.compile(r"[A-Za-z]{4,}")


def ocr_body(folio):
    """The page's OCR lines without the running head (page number, exposé number: up to three short lines)."""
    body = [ln for ln in ocr_page(folio).splitlines() if ln.strip()]
    for _ in range(3):
        if body and len(re.sub(r"\s", "", body[0])) <= 15:
            body = body[1:]
    return body


def ocr_words(folio):
    return [w.lower() for w in WORD.findall(" ".join(ocr_body(folio)))]


BODY_START = {"5": None, "6": r"\\section\*\{Exposé 0\}"}


def safe_split(t, k):
    """Move a split position k back so that the marker line does not fall inside inline mathematics or inside a
    braced argument that starts on the same line (\\emph{..., \\underline{..., \\textbf{...)."""
    for _ in range(6):
        ls = t.rfind("\n", 0, k) + 1
        seg = t[ls:k]
        dollars = [m.start() for m in re.finditer(r"(?<!\\)\$", seg)]
        if len(dollars) % 2 == 1:
            k = ls + dollars[-1]
            continue
        depth, opens = 0, []
        i = 0
        while i < len(seg):
            c = seg[i]
            if c == "\\":
                i += 2
                continue
            if c == "{":
                opens.append(i)
            elif c == "}" and opens:
                opens.pop()
            i += 1
        if opens:
            p = opens[0]
            m = re.search(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})*\s*$", seg[:p])
            k = ls + (m.start() if m else p)
            continue
        break
    return k


def tex_tokens(t):
    """(word, offset) for the accent-free words of 4+ letters of the TeX, outside comments and control words."""
    out = []
    for line_m in re.finditer(r"[^\n]*\n?", t):
        line = line_m.group(0)
        cut = re.search(r"(?<!\\)%", line)
        body = line[:cut.start()] if cut else line
        for m in re.finditer(r"\\[A-Za-z]+|[^\W\d_]+", body):
            if m.group(0).startswith("\\"):
                continue
            w = fold(m.group(0))
            if len(w) >= 4 and w.isascii() and w.isalpha():
                out.append((w, line_m.start() + m.start()))
    return out


def place(t):
    """folio -> character offset in t where the page begins (or None)."""
    toks = tex_tokens(t)
    if BODY_START[vol]:
        b0 = re.search(BODY_START[vol], t).start()
        toks = [(w, o) for w, o in toks if o >= b0]
    tw = [w for w, _ in toks]
    seq, owner = [], []
    for f in range(FIRST, LAST + 1):
        ws = ocr_words(f)
        seq += ws
        owner += [f] * len(ws)
    sm = difflib.SequenceMatcher(None, seq, tw, autojunk=False)
    amap = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            amap[a + k] = b + k
    starts = {}
    first_idx = {}
    for i, f in enumerate(owner):
        first_idx.setdefault(f, i)
    for f in range(FIRST, LAST + 1):
        if f not in first_idx:
            starts[f] = None
            continue
        i0 = first_idx[f]
        # the first OCR word of the page that is aligned, within the page's first 25 words
        j = next((i for i in range(i0, min(i0 + 25, len(owner))) if owner[i] == f and i in amap), None)
        if j is None:
            starts[f] = None
            continue
        k = amap[j] - (j - i0)  # back up over the page's leading words that did not align
        k = max(k, 0)
        starts[f] = toks[k][1]
    return starts


def insert(t, starts):
    out, pos, done, prev = [], 0, [], -1
    for f in sorted(s for s in starts if starts[s] is not None):
        k = safe_split(t, starts[f])
        if k <= prev:  # out of order: leave for the checkers
            continue
        line = f"%%%%%%%%%%  scan idx {v['idx_of'](f)}  |  folio {f}  %%%%%%%%%%"
        # put the marker at the start of the line if the page starts there, otherwise break the line
        ls = t.rfind("\n", 0, k) + 1
        if t[ls:k].strip() == "":
            out.append(t[pos:ls] + line + "\n")
            pos = ls
        else:
            out.append(t[pos:k].rstrip(" ") + "\n" + line + "\n")
            pos = k
        prev = k
        done.append(f)
    out.append(t[pos:])
    return "".join(out), done


report = {}
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        if MARK.search(t):
            print(f.name, edition, "already has markers")
            continue
        starts = place(t)
        new, done = insert(t, starts)
        missing = [p for p in range(FIRST, LAST + 1) if p not in done]
        report[edition] = dict(placed=len(done), missing=missing)
        print(edition, f.name, "placed", len(done), "of", LAST - FIRST + 1, "| not placed:", missing[:40],
              "..." if len(missing) > 40 else "")
        if apply:
            f.write_text(new, encoding="utf-8", newline="")
(W / f"MARKERS_{vol}.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
