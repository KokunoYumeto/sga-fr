"""Page table of the SGA 4 API pass: where every printed page of SGA 4 lies in the TeX and in the scans.

The edition marks the start of each printed page with \\pageoriginale (a counter, set per exposé with
\\setcounter{pageoriginal}{N}, continued from the previous file of the same tome otherwise). Two facts make the counter
alone unreliable: Springer counts blank versos that are not in the scans and carry no marker (pp. 218 and 264 of Tome 1,
so the counter runs one page behind in Exposé II and two in Exposé III), and the marker stands after the page's first
word or two, or after a heading or display that opens the page, so the TeX alone cannot tell whether the block of
non-prose lines just before a marker ends the previous page or opens the next. The scans' own OCR (text layer,
ocr/<scan>.json; never shown to the models) settles both where it can:

- scan page of a TeX page: the folio numbers at the foot of the scan pages give a first guess; the guess is moved to
  the scan page within three pages whose first lines hold the words of the marker line (a drift is carried on to the
  following pages). The page's folio is the Springer number of that scan page (foot number, or its neighbours').
- page start: if the marker line's words open the scan page (nothing above them but the running head), the block
  before the marker ends the previous page; if other lines stand above them, the block opens this page; otherwise the
  block goes to both pages and the page's first comment line says so;
- the marker line is shared by both pages when two or more words precede the marker, unless the OCR shows all of
  them at the top of the new page.

Each page's TeX is cut at whole lines; the overlaps are named in its comment line. Writes PAGES.json (one record per
printed page with TeX) and PAGES_DIAG.json (doubtful placements, scan pages with text but no TeX page, gaps).

usage: python -I build_pages.py
"""
import difflib
import json
import pathlib
import re
import sys
import unicodedata
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parent
DIP = W / "sga4" / "diplomatic"
OCR = HERE / "ocr"

TOMES = {
    "1": {"lnm": 269, "files": ["01", "02", "03", "04"], "scan": "t1",
          "scan_path": r"C:\Users\user\Documents\sga4_scans_20261110\rochester_artin-SGA4-1.pdf",
          "scan_name": "rochester_artin-SGA4-1.pdf"},
    "2": {"lnm": 270, "files": ["05", "05bis", "06", "07", "08"], "scan": "t2",
          "scan_path": r"C:\Users\user\Downloads\artin-SGA4-2.pdf", "scan_name": "artin-SGA4-2.pdf"},
    "3": {"lnm": 305, "files": ["09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"], "scan": "t3",
          "scan_path": r"C:\Users\user\Documents\Papors\OS\Théorie des topos et cohomologie étale des schemas  [SGA 4] ( etc.).pdf",
          "scan_name": "Théorie des topos et cohomologie étale des schemas  [SGA 4] ( etc.).pdf",
          "witness": "w3", "witness_path": r"C:\Users\user\Downloads\Number4.pdf", "witness_name": "Number4.pdf",
          "witness_covers": [250, 587]},
}
EXPOSE = {"01": "I", "02": "II", "03": "III", "04": "IV", "05": "V", "05bis": "Vbis", "06": "VI", "07": "VII",
          "08": "VIII", "09": "IX", "10": "X", "11": "XI", "12": "XII", "13": "XIII", "14": "XIV", "15": "XV",
          "16": "XVI", "17": "XVII", "18": "XVIII", "19": "XIX"}

MARK = re.compile(r"\\pageoriginaled?(?![A-Za-z])")
SETC = re.compile(r"\\setcounter\{pageoriginal\}\{(\d+)\}")
OPEN_DISPLAY = re.compile(r"\\begin\{(equation|align|eqnarray|gather|multline|displaymath|tikzcd|CD|xy)\*?\}")
CLOSE_DISPLAY = re.compile(r"\\end\{(equation|align|eqnarray|gather|multline|displaymath|tikzcd|CD|xy)\*?\}")
OPENER = re.compile(r"\s*(\\(section|subsection|subsubsection|paragraph|chapter|begin|end|etiquette|label|item|"
                    r"smallskip|medskip|bigskip|noindent|par\b|newpage|clearpage|renewcommand|newcommand|setcounter|"
                    r"addtocounter|def\b|let\b|vspace|vskip|hfill)|%|\\\]|\\\[|\$\$)")
STOP = set("pour dans avec sont donc tout toute tous toutes cette alors comme etre mais plus elle elles nous vous "
           "leur leurs dont tel telle ceci cela ainsi aussi encore bien ont qui que les des une est par sur pas "
           "son ses aux ces cet entre sous meme memes autre autres deux the and".split())


# ---------------------------------------------------------------- text normalisation

def fold(s):
    """Lower case, accents stripped, letters only (other characters become spaces)."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]+", " ", s.lower())


def tex_plain(s):
    """A TeX line as running text: comments, math, environment names, labels and command names removed."""
    s = re.sub(r"(?<!\\)%.*", " ", s)
    s = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", " ", s)
    s = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?", " ", s)
    s = re.sub(r"\\(etiquette|label|hyperref|eqhyperref|hyperrefext|ref|cite|eqref)(?![A-Za-z])(\[[^\]]*\])*"
               r"(\{[^}]*\})?", " ", s)
    s = re.sub(r"\\[A-Za-z]+\*?", " ", s)
    return s


def tex_words(s):
    """Words of running text in a TeX line (three letters or more)."""
    return [w for w in fold(tex_plain(s)).split() if len(w) >= 3]


def alnum(s):
    """Letters and digits only, accents stripped, lower case (for comparing the first words of a page)."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


HEADING = re.compile(r"^\s*(\\(section|subsection|subsubsection|paragraph)\*?\{.*\}|\\begin\{[^}]*\}(\{[^}]*\})?|"
                     r"\\item(\[[^\]]*\])?|\\etiquette\[[^\]]*\]\{[^}]*\}|\\label\{[^}]*\}|\s)+")


def prefix_chunks(before):
    """What precedes the marker on its line, without a heading command that opens the line: whitespace chunks."""
    m = HEADING.match(before)
    rest = before[m.end():] if m else before
    rest = re.sub(r"\\(hyperref|eqhyperref|hyperrefext|ref|cite|eqref)(\[[^\]]*\])*", " ", rest)
    rest = re.sub(r"\\[A-Za-z]+\*?", " ", rest).replace("{", " ").replace("}", " ")
    return rest.split()


def ocr_tokens(s):
    return [w for w in fold(s).split() if len(w) >= 3]


def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


def tok_match(t, cands):
    """Fuzzy: an OCR token equals a TeX word up to OCR noise (accents read as ~ or other letters)."""
    for c in cands:
        if t == c or (len(t) >= 4 and len(c) >= 4 and similar(t, c) >= 0.75):
            return True
    return False


# ---------------------------------------------------------------- TeX side

def scan_file(fn):
    """Lines, markers (line index, column), display flags, prose flags, content range of one exposé file."""
    text = (DIP / fn / f"{fn}.tex").read_text(encoding="utf-8")
    lines = text.split("\n")
    markers, setc = [], None
    disp = [False] * len(lines)
    in_dd = in_env = False
    for i, l in enumerate(lines):
        code = re.sub(r"(?<!\\)%.*", "", l)
        m = SETC.search(code)
        if m and setc is None:
            setc = (i, int(m.group(1)))
        for mm in MARK.finditer(l):  # a marker inside a commented-out printed passage still starts a printed page
            markers.append([i, mm.start()])
        was = in_dd or in_env
        n_dd = code.count("$$")
        if OPEN_DISPLAY.search(code) or "\\[" in code:
            in_env = True
        if n_dd % 2 == 1:
            in_dd = not in_dd
        disp[i] = was or in_dd or in_env or n_dd > 0
        if CLOSE_DISPLAY.search(code) or "\\]" in code:
            in_env = False
            disp[i] = True
    start = next(i for i, l in enumerate(lines) if l.startswith("\\chapter"))
    ends = [i for i, l in enumerate(lines) if l.strip().startswith("\\ifx\\danslelivre")]
    end = ends[-1] - 1 if ends and ends[-1] > markers[-1][0] else len(lines) - 1
    # running text: a line outside displays with at least one word that is not a heading or environment line
    # (an \item line with words counts as running text); blank, comment, display and heading lines do not
    prose, printing = [], []
    for i, l in enumerate(lines):
        item = re.match(r"^\s*\\item(\[[^\]]*\])?", l)
        body = l[item.end():] if item else l
        words = re.findall(r"[a-z]+", fold(tex_plain(body)))
        inline_math = "$" in re.sub(r"(?<!\\)%.*", "", body) and not disp[i]
        closer = re.match(r"^\s*\\end\{", l) and not disp[i]
        if disp[i] or not l.strip() or l.lstrip().startswith("%"):
            prose.append(False)
        elif item:
            prose.append(bool(words) or inline_math)
        elif closer:
            prose.append(False)  # \end{...}: prints nothing; a display above it is part of the block
        elif OPENER.match(l):
            prose.append(False)
        else:
            prose.append(bool(words) or inline_math)
        printing.append(bool(disp[i] and re.sub(r"(?<!\\)%.*", "", l).strip()) or bool(words) or inline_math)
    return {"fn": fn, "lines": lines, "markers": markers, "setc": setc, "disp": disp, "prose": prose,
            "printing": printing, "start": start, "end": end}


# ---------------------------------------------------------------- OCR side

def ocr_pages(name):
    return json.loads((OCR / f"{name}.json").read_text(encoding="utf-8"))


def foot_number(page_text):
    lines = [l.strip() for l in page_text.splitlines() if l.strip()]
    for l in reversed(lines[-2:]):
        t = l.replace("O", "0").replace("o", "0").replace("I", "1").replace("l", "1").replace(" ", "")
        if re.fullmatch(r"\d{1,3}", t):
            return int(t)
    return None


def body_lines(page_text):
    """OCR lines without the running head (first line, when short) and the folio line."""
    lines = [l.strip() for l in page_text.splitlines() if l.strip()]
    if lines and foot_number("\n".join(lines[-1:])) is not None:
        lines = lines[:-1]
    if lines and (len(ocr_tokens(lines[0])) <= 1 or re.match(r"^[-\s]*[\dIlO]{1,3}\s*-?\s*[IVXlx! ]*\.?$", lines[0])):
        lines = lines[1:]
    return lines


def foot_map(texts):
    """PDF index -> Springer folio, from the foot numbers that agree with their neighbours; others by offset."""
    raw = {i: foot_number(t) for i, t in enumerate(texts)}
    good = {}
    idx = [i for i in raw if raw[i] is not None]
    for k, i in enumerate(idx):
        off = i - raw[i]
        near = [j - raw[j] for j in idx[max(0, k - 3):k + 4] if j != i]
        if sum(1 for o in near if abs(o - off) <= 1) >= min(2, len(near)):
            good[i] = raw[i]
    out = {}
    gi = sorted(good)
    for i in range(len(texts)):
        if i in good:
            out[i] = (good[i], "foot")
            continue
        lo = max((g for g in gi if g < i), default=None)
        hi = min((g for g in gi if g > i), default=None)
        if lo is not None and hi is not None and lo - good[lo] == hi - good[hi]:
            out[i] = (i - (lo - good[lo]), "interpolated")
        elif lo is not None and hi is not None:
            out[i] = (None, "between offsets %d and %d" % (lo - good[lo], hi - good[hi]))
        elif lo is not None:
            out[i] = (i - (lo - good[lo]), "extrapolated")
        elif hi is not None:
            out[i] = (i - (hi - good[hi]), "extrapolated")
    return out


def top_score(body, words):
    """How well the page's first OCR lines match the TeX words that open it: (matched among the first 6 content
    words of the TeX, OCR line of the first match)."""
    content = [w for w in words if len(w) >= 4 and w not in STOP][:6] or words[:3]
    best_line, hits = None, 0
    toks = []
    for k, l in enumerate(body[:3]):
        toks.append((k, ocr_tokens(l)))
    for w in content:
        for k, t in toks:
            if tok_match(w, t):
                hits += 1
                best_line = k if best_line is None else min(best_line, k)
                break
    return hits, best_line, len(content)


def first_ocr_hit(body, words, look=8):
    """Index of the first OCR body line (among the first `look`) holding >= 2 of the given words (or 1 if only 1)."""
    need = 1 if len(words) < 2 else 2
    for k, l in enumerate(body[:look]):
        toks = ocr_tokens(l)
        if sum(1 for w in words if tok_match(w, toks)) >= need:
            return k
    return None


def build():
    pages, diag = [], []
    for tome, tv in TOMES.items():
        texts = ocr_pages(tv["scan"])
        bodies = [body_lines(t) for t in texts]
        fm = foot_map(texts)
        folio_to_pdf = {}
        for i, (f, how) in fm.items():
            if f is not None and f not in folio_to_pdf:
                folio_to_pdf[f] = i
        wtexts = ocr_pages(tv["witness"]) if tv.get("witness") else None
        wfm = foot_map(wtexts) if wtexts else {}
        w_folio_to_pdf = {}
        for i, (f, how) in wfm.items():
            if f is not None and f not in w_folio_to_pdf:
                w_folio_to_pdf[f] = i
        counter = 0
        used_pdf = []
        for fn in tv["files"]:
            F = scan_file(fn)
            lines, prose, mk = F["lines"], F["prose"], F["markers"]
            n = len(mk)
            if F["setc"] is not None:
                counter = F["setc"][1]
            info = []
            for k in range(n):
                counter += 1
                L, col = mk[k]
                lo_limit = (mk[k - 1][0] + 1) if k else F["start"]
                b0 = L
                while b0 - 1 >= lo_limit and not prose[b0 - 1] and L - (b0 - 1) <= 30:
                    b0 -= 1
                block = [w for i in range(b0, L) for w in tex_words(lines[i])] if k else []
                prefix = tex_words(lines[L][:col])
                after = tex_words(lines[L][col:])
                j = L + 1
                while len(after) < 12 and j <= F["end"]:
                    after += tex_words(lines[j])
                    j += 1
                info.append({"k": k, "L": L, "col": col, "prefix": prefix, "after": after, "block": block,
                             "counter": counter, "words": block + prefix + after if k else after})
            # offset of the scan against the counter (blank versos counted by Springer without a marker, a marker
            # lost): a Viterbi path over offsets -4..4, scoring each page by how many of its opening TeX words stand
            # in the first three OCR lines of the scan page, with a penalty of 5 for each change of offset
            D = range(-4, 5)
            em = []
            for it in info:
                row = {}
                for d in D:
                    i = folio_to_pdf.get(it["counter"] + d)
                    if i is None:
                        row[d] = -1.0
                        continue
                    h, line, m = top_score(bodies[i], it["words"])
                    row[d] = float(h) if line is not None and line <= 2 else 0.0
                em.append(row)
            score = {d: em[0][d] - 0.5 * abs(d) for d in D}
            back = []
            for k in range(1, n):
                new, bk = {}, {}
                for d in D:
                    prev = max(D, key=lambda e: score[e] - (0 if e == d else 5.0))
                    new[d] = score[prev] - (0 if prev == d else 5.0) + em[k][d]
                    bk[d] = prev
                score = new
                back.append(bk)
            d = max(D, key=lambda e: (score[e], -abs(e)))
            path = [d]
            for bk in reversed(back):
                d = bk[d]
                path.append(d)
            path.reverse()
            for it, delta in zip(info, path):
                pdf = folio_to_pdf.get(it["counter"] + delta)
                hits, line, m = top_score(bodies[pdf], it["words"]) if pdf is not None else (0, None, 0)
                it.update(pdf=pdf, folio=fm[pdf][0] if pdf is not None else None, top_hits=hits, top_line=line,
                          top_m=m, delta=delta)
                used_pdf.append(pdf)
            changes = [(info[k]["counter"], path[k]) for k in range(n) if k == 0 or path[k] != path[k - 1]]
            print(f"tome {tome} {fn}: offsets (counter, offset) {changes}")
            # boundaries. The block before a marker line (lines between the last running text and the marker line)
            # has a display part D = [b0, h0) and a heading part H = [h0, L) (headings, statement labels,
            # \begin lines, blank lines after the last display line). Each part is placed on this page ("this"), on
            # the previous one ("prev") or on both ("both", named in the comment lines of both pages).
            for k in range(n):
                it = info[k]
                L, col = it["L"], it["col"]
                if k == 0:
                    it.update(a=F["start"], z_prev=None, label="first page of the exposé", shared=False,
                              both_this=[], both_prev=[])
                    continue
                lo_limit = mk[k - 1][0] + 1
                b0 = L
                while b0 - 1 >= lo_limit and not prose[b0 - 1] and L - (b0 - 1) <= 30:
                    b0 -= 1
                h0 = L
                while h0 - 1 >= b0 and not F["disp"][h0 - 1]:
                    h0 -= 1
                while h0 < L and not lines[h0].strip():  # blank lines right after a display go with the display
                    h0 += 1
                body = bodies[it["pdf"]] if it["pdf"] is not None else []
                pbody = bodies[info[k - 1]["pdf"]] if info[k - 1]["pdf"] is not None else []
                first_words = (it["prefix"] + it["after"])[:3]
                hit = first_ocr_hit(body, first_words) if first_words else None
                # heading part: where do its words stand? (a part that prints nothing goes with this page)
                hw = [w for i in range(h0, L) for w in tex_words(lines[i])][:4]
                H = None if h0 == L or not any(F["printing"][i] for i in range(h0, L)) else "both"
                if hw:
                    need = (len(hw) + 1) // 2
                    in_top = sum(1 for w in hw if tok_match(w, ocr_tokens(" ".join(body[:2])))) >= need
                    in_bottom = sum(1 for w in hw if tok_match(w, ocr_tokens(" ".join(pbody[-2:])))) >= need
                    H = "this" if in_top and not in_bottom else "prev" if in_bottom and not in_top else "both"
                # display part: the last running words before the block, and where they stand on the previous page
                tail = []
                j = b0 - 1
                while j >= lo_limit and len(tail) < 3:
                    tail = tex_words(lines[j]) + tail
                    j -= 1
                tail = tail[-3:]
                prev_end = None
                for back_i, l in enumerate(reversed(pbody[-4:])):
                    if tail and sum(1 for w in tail if tok_match(w, ocr_tokens(l))) >= min(2, len(tail)):
                        prev_end = back_i
                        break
                Dp = None
                if b0 < h0 and any(F["printing"][i] for i in range(b0, h0)):
                    Dp = "both"
                    if H == "prev":
                        Dp = "prev"
                    elif hit == 0 and not hw and prev_end is not None and prev_end >= 1:
                        trailing = pbody[len(pbody) - prev_end:]
                        if all(len([w for w in ocr_tokens(x) if len(w) >= 4]) <= 3 for x in trailing):
                            Dp = "prev"
                    elif prev_end == 0 and ((hit is not None and hit >= 1) or H == "this"):
                        Dp = "this"
                shared = False
                if H != "this":
                    chunks = prefix_chunks(lines[L][:col])
                    if len(chunks) >= 2:
                        pre = alnum(" ".join(chunks))
                        first = alnum(body[0]) if body else ""
                        shared = not (pre and similar(first[:len(pre)], pre) >= 0.75)
                # this page starts at ...
                if Dp in ("this", "both"):
                    a = b0
                elif H in ("this", "both") or (H is None and h0 < L):
                    a = h0
                else:
                    a = L
                # ... and the previous page ends at
                if H in ("prev", "both"):
                    z_prev = L if shared else L - 1
                elif Dp in ("prev", "both"):
                    z_prev = h0 - 1
                else:
                    z_prev = b0 - 1
                if shared:
                    z_prev = max(z_prev, L)
                both = []
                if Dp == "both":
                    both.append((b0, h0 - 1))
                if H == "both":
                    both.append((h0, L - 1))
                label = ("no block" if b0 == L else
                         "display %s, heading %s" % (Dp or "-", H or ("-" if h0 == L else "blank")))
                it.update(a=a, z_prev=z_prev, label=label, shared=shared, both=both, first_hit=hit,
                          prev_end=prev_end)
            for k in range(n):
                it = info[k]
                a = it["a"]
                z = info[k + 1]["z_prev"] if k + 1 < n else F["end"]
                while z > a and not lines[z].strip():
                    z -= 1
                folio = it["folio"]
                nxt = info[k + 1]["folio"] if k + 1 < n else None
                prv = info[k - 1]["folio"] if k else None
                notes, overlaps = [], []
                for x, y in it.get("both", []):
                    notes.append(f"lines {x + 1}-{y + 1}, before this page's \\pageoriginale, may end p. {prv} "
                                 f"instead of opening this page")
                    overlaps.append({"where": "start", "kind": "block", "lines": [x + 1, y + 1], "other": prv})
                if k > 0 and it["shared"]:
                    notes.append(f"its line {it['L'] + 1} may also hold the last words of p. {prv} (this page begins "
                                 f"one or two words before the page marker)")
                    overlaps.append({"where": "start", "kind": "shared", "lines": [it["L"] + 1, it["L"] + 1],
                                     "other": prv})
                if k + 1 < n:
                    nb = info[k + 1]
                    for x, y in nb.get("both", []):
                        notes.append(f"lines {x + 1}-{y + 1}, before the \\pageoriginale of p. {nxt}, may open p. "
                                     f"{nxt} instead of ending this page")
                        overlaps.append({"where": "end", "kind": "block", "lines": [x + 1, y + 1], "other": nxt})
                    if nb["shared"]:
                        notes.append(f"its last line, {nb['L'] + 1}, also holds the first words of p. {nxt} (from "
                                     f"the word or two before the page marker on)")
                        overlaps.append({"where": "end", "kind": "shared", "lines": [nb["L"] + 1, nb["L"] + 1],
                                         "other": nxt})
                it["decision"] = it["label"]
                rec = {"tome": tome, "lnm": tv["lnm"], "file": fn, "expose": EXPOSE[fn],
                       "tex": f"sga4/diplomatic/{fn}/{fn}.tex", "folio": folio, "counter": it["counter"],
                       "lines": [a + 1, z + 1], "marker_line": it["L"] + 1,
                       "start_decision": it["decision"], "shared_start": it["shared"], "notes": notes,
                       "overlaps": overlaps,
                       "scan": tv["scan_name"], "scan_path": tv["scan_path"],
                       "pdf_page": it["pdf"] + 1 if it["pdf"] is not None else None,
                       "pdf_how": fm[it["pdf"]][1] if it["pdf"] is not None else None,
                       "ocr_top": {"hits": it["top_hits"], "of": it["top_m"], "line": it["top_line"]}}
                if wtexts and folio is not None and tv["witness_covers"][0] <= folio <= tv["witness_covers"][1]:
                    wi = w_folio_to_pdf.get(folio)
                    if wi is not None:
                        wh = top_score(body_lines(wtexts[wi]), it["prefix"] + it["after"] if k else it["after"])
                        rec.update(witness=tv["witness_name"], witness_path=tv["witness_path"],
                                   witness_pdf_page=wi + 1, witness_how=wfm[wi][1],
                                   witness_ocr_top={"hits": wh[0], "of": wh[2], "line": wh[1]})
                weak = it["top_hits"] < min(2, it["top_m"]) or it["top_line"] is None or it["top_line"] > 2
                if weak or folio is None:
                    diag.append({"why": "first words not found at the top of the scan page", "tome": tome, "file": fn,
                                 "folio": folio, "pdf_page": rec["pdf_page"], "marker_line": rec["marker_line"],
                                 "words": (it["prefix"] + it["after"])[:6],
                                 "ocr_top": " | ".join(bodies[it["pdf"]][:2])[:160] if it["pdf"] is not None else ""})
                pages.append(rec)
        # scan pages between the first and the last used page that no TeX page took
        used = sorted(set(p for p in used_pdf if p is not None))
        dup = [p for p, c in Counter(used_pdf).items() if p is not None and c > 1]
        for p in dup:
            diag.append({"why": "two TeX pages on one scan page", "tome": tome, "pdf_page": p + 1, "folio": fm[p][0]})
        for i in range(used[0], used[-1] + 1):
            if i not in used:
                b = bodies[i]
                diag.append({"why": "scan page without a TeX page", "tome": tome, "pdf_page": i + 1, "folio": fm[i][0],
                             "body_lines": len(b), "ocr_top": " | ".join(b[:2])[:160]})
    return pages, diag


def head_number(page_text):
    """The typescript page number in the running head (first OCR line), or None."""
    lines = [l.strip() for l in page_text.splitlines() if l.strip()]
    if not lines:
        return None
    m = re.match(r"^-?\s*([0-9IlO]{1,3})\s*-?\s+[IVXrxl!|.]+\.?$", lines[0])
    if not m:
        return None
    t = m.group(1).replace("I", "1").replace("l", "1").replace("O", "0")
    return int(t) if t.isdigit() else None


def add_typescript(pages):
    """Typescript page = printed page - c, with c the constant of the exposé that most OCR heads agree on; a page's
    number is given only where its own head confirms it."""
    texts = {t: ocr_pages(TOMES[t]["scan"]) for t in TOMES}
    by_file = {}
    for p in pages:
        by_file.setdefault(p["file"], []).append(p)
    for fn, ps in by_file.items():
        votes = Counter()
        for p in ps:
            h = head_number(texts[p["tome"]][p["pdf_page"] - 1]) if p["pdf_page"] else None
            p["_head"] = h
            if h is not None and p["folio"] is not None:
                votes[p["folio"] - h] += 1
        c = votes.most_common(1)[0][0] if votes else None
        for p in ps:
            ok = c is not None and p["_head"] is not None and p["folio"] - p["_head"] == c
            p["typescript"] = f"{p['expose']}-{p['folio'] - c}" if ok else None
            del p["_head"]


if __name__ == "__main__":
    pages, diag = build()
    add_typescript(pages)
    print("typescript numbers confirmed:", sum(1 for p in pages if p["typescript"]), "of", len(pages))
    (HERE / "PAGES.json").write_text(json.dumps(pages, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "PAGES_DIAG.json").write_text(json.dumps(diag, ensure_ascii=False, indent=1), encoding="utf-8")
    print("pages", len(pages), "by tome", Counter(p["tome"] for p in pages))
    print("start decisions", Counter(p["start_decision"] for p in pages))
    print("shared starts", sum(p["shared_start"] for p in pages), "| pdf how", Counter(p["pdf_how"] for p in pages))
    print("folio = counter:", sum(p["folio"] == p["counter"] for p in pages), "differs:",
          Counter((p["file"], p["folio"] - p["counter"]) for p in pages if p["folio"] is not None and p["folio"] != p["counter"]))
    print("diag", Counter(d["why"] for d in diag))
