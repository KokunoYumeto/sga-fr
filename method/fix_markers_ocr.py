"""Find page markers that stand one TeX line too late, using the scan's OCR, and move them up (both editions).

For each marker of the volume, the OCR of the printed page (ocr_<vol>/page_NNN.txt, header lines skipped) is compared
with the TeX right after the marker and with the TeX line right before it followed by that text. When the page's
opening words match the line before the marker clearly better, the marker belongs before that line: it is moved there
in the diplomatic and in the current edition (only where that edition has the same line before its marker).
usage: python -I fix_markers_ocr.py VOL [--apply] [--pages=A-B] [--show]"""
import difflib
import pathlib
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import MARK, W, files  # noqa: E402

vol = sys.argv[1]
APPLY = "--apply" in sys.argv
SHOW = "--show" in sys.argv
rng = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--pages=")), None)
lo, hi = (int(x) for x in rng.split("-")) if rng else (0, 10 ** 6)


def norm(s):
    s = re.sub(r"%.*", " ", s)
    s = re.sub(r"\\(begin|end)\{[^}]*\}", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^A-Za-z0-9]+", " ", s).lower()
    return re.sub(r"\s+", " ", s).strip()


def ocr_start(n):
    p = W / f"ocr_{vol}" / f"page_{n:03d}.txt"
    if not p.exists():
        return ""
    words = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        x = norm(line)
        if len(re.sub(r"[^a-z]", "", x)) < 6:       # page numbers, running heads, OCR debris
            if not words:
                continue
        words += x.split()
        if len(words) >= 8:
            break
    return " ".join(words[:8])


def score(a, b):
    return difflib.SequenceMatcher(None, a, b[:len(a) + 10]).ratio() if a and b else 0.0


moves = []
for f in files(vol, "diplomatic"):
    t = f.read_text(encoding="utf-8")
    for m in MARK.finditer(t):
        n = int(m.group(2))
        if not lo <= n <= hi:
            continue
        ls = t.rfind("\n", 0, m.start())          # the marker's line starts after ls
        if ls < 0:
            continue
        ps = t.rfind("\n", 0, ls) + 1
        prev = t[ps:ls]
        if not norm(prev):
            continue
        after = t[m.end():m.end() + 400]
        o = ocr_start(n)
        if len(o) < 12:
            continue
        s_after, s_prev = score(o, norm(after)), score(o, norm(prev + " " + after))
        if SHOW:
            print(f"{n}: after {s_after:.2f} prev {s_prev:.2f} | OCR {o[:50]!r} | prev {prev[:50]!r}")
        pw = norm(prev).split()
        # a short fragment before the marker (the aligner split the page's first line after its first words) that the
        # page's OCR begins with
        fragment = (1 <= len(pw) <= 4 and not prev.rstrip().endswith((".", ":", ";", "}", "]", "$"))
                    and difflib.SequenceMatcher(None, " ".join(pw), o[:len(" ".join(pw))]).ratio() >= 0.75
                    and s_prev >= s_after - 0.02)
        if fragment or (s_prev >= 0.6 and s_prev - s_after >= 0.15):
            moves.append((n, prev, s_after, s_prev))

print(f"{vol}: {len(moves)} markers one line too late" + ("" if APPLY else " (dry run)"))
for n, prev, a, p in moves:
    print(f"  {n}: before the line {prev[:70]!r}  (match {a:.2f} -> {p:.2f})")
if APPLY:
    for edition in ("diplomatic", "current"):
        for f in files(vol, edition):
            t = f.read_text(encoding="utf-8")
            done = 0
            for n, prev, _, _ in moves:
                m = next((m for m in MARK.finditer(t) if int(m.group(2)) == n), None)
                if not m:
                    continue
                ls = t.rfind("\n", 0, m.start())
                ps = t.rfind("\n", 0, ls) + 1
                if ls < 0 or norm(t[ps:ls]) != norm(prev):
                    print(f"  {edition} {f.name}: page {n} not moved (the line before its marker differs)")
                    continue
                line_end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
                mark = t[ls + 1:m.end()] if t[ls + 1:m.start()].strip() == "" else m.group(0)
                t = t[:ls + 1] + t[line_end:]                    # take the marker line out
                t = t[:ps] + mark.strip("\n") + "\n" + t[ps:]     # put it before the previous line
                done += 1
            f.write_text(t, encoding="utf-8", newline="")
            print(f"  {edition} {f.name}: {done} moved")
