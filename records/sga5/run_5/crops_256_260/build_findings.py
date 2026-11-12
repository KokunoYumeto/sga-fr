"""Build findings_256_260.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b256_260"
OUT = RUN / "findings_256_260.json"
NL = "\n"

UL_NOTE = ("Exposé VI: the TeX has no underline markup (as Exposé V); \\emph, the exposé's own form "
           "('\\emph{Preuve}') and that of the Exposé V fixes.")

F = []


def add(page, where, scan, tex, kind, confidence, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 256
add(256, "Proposition 1.2.3.1, 'est une équivalence de catégories.'",
    "'équivalence de catégories' underlined (not the full stop)",
    "no underline markup", "underline", "high",
    {"old": r"une équivalence de catégories. Il", "new": r"une \emph{équivalence de catégories}. Il"},
    UL_NOTE)
add(256, "'Soient maintenant Lc(X), Abf(π_1)'",
    "'Lc(X)' typed upright, a category name like 'Abf' beside it",
    r"\(Lc(X)\): the name in math italic", "font", "medium",
    {"old": r"\(Lc(X)\)", "new": r"\(\Lc(X)\)"},
    r"The preamble defines \Lc (\operatorname{Lc}, s5.tex l. 173) but the page writes the name in math italic, "
    r"unlike \Abf and \Ensf beside it.")
add(256, "display 'F_a: Lc(X) → Abf(π_1) ,'",
    "'Lc(X)' upright, as 'Abf'",
    r"F_a:Lc(X): math italic", "font", "medium",
    {"old": r"F_a:Lc(X)", "new": r"F_a:\Lc(X)"},
    "As the previous finding.")

# ---------------- page 257
add(257, "heading 1.2.4",
    "'1.2.4. Z_ℓ -faisceaux constants tordus sur un préschéma connexe.': underlined title ending with a full stop",
    r"\subsubsection*{1.2.4. ... sur un préschéma connexe}: no full stop", "punctuation", "high",
    {"old": r"préschéma connexe}", "new": r"préschéma connexe.}"},
    "Underlined title: the TeX drops the print's final full stop.")
add(257, "'Sa limite projective lim_N (F_n) est naturellement munie'",
    "lim with the arrow under it and index N, then '(F_n)' in parentheses",
    r"\varprojlim_{\mathbb N}F_n", "formula", "high",
    {"old": r"\varprojlim_{\mathbb N}F_n", "new": r"\varprojlim_{\mathbb N}(F_n)"},
    "The parentheses of the print are missing. The print runs the limit into the text (layout, not reported).")
add(257, "display 'G x M → M / (g, m) ↦ g.m'",
    "two stacked lines without punctuation: 'G x M ——> M' over '(g, m) |——> g.m'",
    r"G\times M\longrightarrow M,\qquad (g,m)\longmapsto g\cdot m,", "punctuation", "high",
    {"old": r"M,\qquad (g,m)\longmapsto g\cdot m,", "new": r"M\qquad (g,m)\longmapsto g\cdot m"},
    r"The TeX adds a comma after each line. The stacking is layout (not reported); the print's maps-to arrow has "
    r"its bar, so \longmapsto stands.")
add(257, "'telle que : (i)'",
    "'telle que :' before (i)",
    "telle que (no colon)", "punctuation", "high",
    {"old": "telle que" + NL + r"\[", "new": "telle que:" + NL + r"\["},
    "Colon written without a space, as the file's 'suivante:'.")
add(257, "condition (i), the parenthesis",
    "'(g ∈ G, m et n ∈ M)'",
    r"(g\in G,\ m,n\in M)", "word", "high",
    {"old": r"\ m,n\in", "new": r"\ m\text{ et }n\in"},
    "The print has 'et' where the TeX has a comma. Does not overlap the next edit.")
add(257, "condition (i), end of the display",
    "no punctuation after '(g ∈ G, m et n ∈ M)'; the next line begins 'et (ii)'",
    r"M),", "punctuation", "high",
    {"old": "M)," + NL + r"\]", "new": "M)" + NL + r"\]"},
    "Comma added by the TeX at the end of the display.")
add(257, "condition (ii), the parenthesis",
    "'(g et h ∈ G, m ∈ M) .'",
    r"(g,h\in G,\ m\in M).", "word", "high",
    {"old": r"(g,h\in G", "new": r"(g\text{ et }h\in G"},
    "The print has 'et' where the TeX has a comma.")

# ---------------- page 258
add(258, "top of the page",
    "p. 258 begins 'GL(M/ℓ^{n+1}M). Ces derniers groupes étant finis'; p. 257 ends "
    "'s'identifie à la limite projective des groupes'",
    r"'\(\GL(M/\ell^{n+1}M)\). Ces' ends the last line of page_257.tex, above the folio-258 marker; "
    r"page_258.tex begins 'derniers groupes'", "marker", "high", None,
    r"Page 258 really begins at '\(\GL(M/\ell^{n+1}M)\). Ces'. Exact fix: python -I move_marker.py 5 258 "
    r"'\(\GL(M/\ell^{n+1}M)\). Ces' --before (simulated in memory on both layers: the marker then stands between "
    r"'des groupes ' and '\(\GL(M/\ell^{n+1}M)\). Ces', the line break before 'derniers' stays). Text not moved.")
add(258, "Lemme 1.2.4.2, 'est une équivalence de catégories.'",
    "'équivalence de catégories' underlined (not the full stop)",
    "no underline markup", "underline", "high",
    {"old": r"une équivalence de catégories.", "new": r"une \emph{équivalence de catégories}."},
    "As Proposition 1.2.3.1 on p. 256.")
add(258, "proof of 1.2.4.2, 'Soient maintenant F=(F_n) et G=(G_n)'",
    "'F=(F_n)_{n∈N} et' / 'G=(G_n)_{n∈N}', run into the text",
    r"F=(F_n)_{n\in\mathbb N},\qquad G=(G_n)_{n\in\mathbb N} in a display", "word", "high",
    {"old": r",\qquad G=(G_n)", "new": r"\quad\text{et}\quad G=(G_n)"},
    r"The TeX replaces the print's 'et' by a comma; the display itself is layout (not reported). Same form as the "
    r"file's own 1.3.1 ('\quad\text{et}\quad').")
add(258, "proof of 1.2.4.2, 'deux objets de la catégorie ℓZ-ad(Abf(π_1))'",
    "'ℓ Z-ad(Abf(π_1)),': no parentheses around ℓZ here",
    r"\((\ell\mathbb Z)\text{-}\ad(\Abf(\pi_1))\)", "formula", "high",
    {"old": r"\((\ell\mathbb Z)\text{-}\ad", "new": r"\(\ell\mathbb Z\text{-}\ad"},
    "Elsewhere the print writes (ℓZ)-ad; here it omits the parentheses and the TeX supplies them. A variant of "
    "the notation with the same meaning, not a misprint.")
add(258, "proof of 1.2.4.2, 'et notons pour simplifier Hom_π1(F,G)'",
    "no commas around 'pour simplifier'",
    r"et notons, pour simplifier, \(\Hom", "punctuation", "high",
    {"old": r"notons, pour simplifier, ", "new": r"notons pour simplifier "},
    "Commas added by the TeX.")

MODN_NOTE = (r"The macro \modn is defined as \operatorname{mod} (s5.tex preamble l. 181) and prints 'mod'; "
             r"these three are its only uses in the volume, so redefining it as \operatorname{modn} is the "
             r"alternative to the three edits.")
add(258, "display after 'Ceci dit, on définit de façon évidente un foncteur'",
    "'Z_ℓ-modn(π_1) ,'",
    r"\mathbb Z_\ell\text{-}\modn(\pi_1), which prints 'Z_ℓ-mod(π_1)'", "word", "high",
    {"old": r"\modn(\pi_1),", "new": r"\operatorname{modn}(\pi_1),"},
    MODN_NOTE)
add(258, "'où Z_ℓ-modn(π_1) désigne la catégorie'",
    "'Z_ℓ-modn(π_1)'",
    r"\(\mathbb Z_\ell\text{-}\modn(\pi_1)\), which prints 'Z_ℓ-mod(π_1)'", "word", "high",
    {"old": r"\modn(\pi_1)\) désigne", "new": r"\operatorname{modn}(\pi_1)\) désigne"},
    "As the previous finding.")
add(258, "Lemme 1.2.4.2, display",
    "'Z_ℓ-modn(π_1)'",
    r"\mathbb Z_\ell\text{-}\modn(\pi_1), which prints 'Z_ℓ-mod(π_1)'", "word", "high",
    {"old": r"\modn(\pi_1)" + NL + r"\]", "new": r"\operatorname{modn}(\pi_1)" + NL + r"\]"},
    "As the previous findings.")

# ---------------- page 259
add(259, "'et si u appartient à Hom_o(F,G) on pose'",
    "no comma after 'Hom_o(F,G)'",
    r"\(\Hom_0(F,G)\), on pose", "punctuation", "high",
    {"old": r"\(\Hom_0(F,G)\), on pose", "new": r"\(\Hom_0(F,G)\) on pose"},
    "Comma added by the TeX.")
add(259, "display 's.u = souos^-1 .'",
    "'s.u = souos^{-1} .': the typewriter's letter o for the composition sign, twice",
    r"s\cdot u=sus^{-1}.", "symbol", "high",
    {"old": r"=sus^{-1}", "new": r"=s\circ u\circ s^{-1}"},
    r"The TeX drops both composition signs (the letter o is the typewriter substitute for \circ).")
add(259, "'Il résulte par exemple de (SERRE : Groupes proalgébriques, Prop. 12)'",
    "the author's name typed in capitals: 'SERRE'",
    r"(Serre", "word", "high",
    {"old": r"(Serre", "new": r"(SERRE"},
    "As the capitals restored on p. 1 (GROTHENDIECK, ILLUSIE). Does not overlap the next edit.")
add(259, "'(SERRE : Groupes proalgébriques'",
    "a colon after the name",
    r"Serre, Groupes", "punctuation", "high",
    {"old": r", Groupes proalgébriques", "new": r": Groupes proalgébriques"},
    "Colon written without a space, as elsewhere in the file.")
add(259, "'Les lemmes 1.2.4.1. et 1.2.4.2. permettent'",
    "each number ends with a full stop: '1.2.4.1.' and '1.2.4.2.'",
    r"1.2.4.1 et 1.2.4.2", "punctuation", "high",
    {"old": r"lemmes 1.2.4.1 et 1.2.4.2 permettent", "new": r"lemmes 1.2.4.1. et 1.2.4.2. permettent"},
    "")
add(259, "Proposition 1.2.5, 'localement noethérien connexe X'",
    "'connexe' underlined, the only underline of the statement",
    "no underline markup", "underline", "high",
    {"old": r"noethérien connexe \(X\)", "new": r"noethérien \emph{connexe} \(X\)"},
    UL_NOTE)

# ---------------- page 260
add(260, "Remarque, 'C'est même nécessaire lorsque X est normal.'",
    "'normal' underlined (not the full stop)",
    "no underline markup", "underline", "high",
    {"old": r"est normal.", "new": r"est \emph{normal}."},
    UL_NOTE)
add(260, "Remarque, 'on peut pour le voir se ramener au cas où'",
    "no commas around 'pour le voir'",
    r"on peut, pour le voir, se ramener", "punctuation", "high",
    {"old": r"on peut, pour le voir, se", "new": r"on peut pour le voir se"},
    "Commas added by the TeX.")
add(260, "Remarque, 'En effet (SGA 1 V 8.2) π_1(K) → π_1(X) est surjectif'",
    "no comma after the reference",
    r"(SGA 1 V 8.2), \(\pi_1(K)", "punctuation", "high",
    {"old": r"8.2), \(", "new": r"8.2) \("},
    "Comma added by the TeX.")
add(260, "Proposition 1.2.6 (i), end",
    "'constructible,': a comma",
    r"constructible;", "punctuation", "high",
    {"old": r"faisceau constructible;", "new": r"faisceau constructible,"},
    "")
add(260, "Proposition 1.2.6 (ii), first word",
    "'(ii) Tout ouvert noethérien': capital T",
    r"\item tout ouvert", "word", "high",
    {"old": r"\item tout ouvert", "new": r"\item Tout ouvert"},
    "")
add(260, "Proposition 1.2.6 (ii), end",
    "'constructible,': a comma",
    r"constructible;", "punctuation", "high",
    {"old": r"tordu constructible;", "new": r"tordu constructible,"},
    "")
add(260, "end of page_260.tex: the opening of the proof of 1.2.6",
    "p. 260 ends with (iii) '... F est un Z_ℓ-faisceau constant tordu constructible.'; the proof begins on p. 261",
    r"'\begin{prooftext}[' is the last line of page_260.tex: the folio-261 marker line splits "
    r"'\begin{prooftext}[Preuve]' (page_261.tex begins 'Preuve]')", "marker", "high", None,
    r"Page 261 begins with the proof label. Exact fix: python -I marker_split_word.py 5 261 pull "
    r"'\begin{prooftext}[' (simulated in memory on both layers: the marker line then stands above "
    r"'\begin{prooftext}[Preuve]', rejoined on one line). move_marker.py with this anchor would leave a line break "
    r"inside the brackets. Text not moved.")

# ---------------- order: by place on the page (marker at the top first, at the end last)
def _key(f):
    if f["fix"] is None:
        return (f["page"], -1 if "top" in f["where"] else 10 ** 9)
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    return (f["page"], t.find(f["fix"]["old"]))


F.sort(key=_key)

# ---------------- checks
ok = True
for f in F:
    if f["fix"] is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], n, repr(f["fix"]["old"]))
    if "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False
        print("MARKER IN OLD", f["page"])
# overlaps of edits on the same page
by_page = {}
for f in F:
    if f["fix"] is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    k = t.find(f["fix"]["old"])
    by_page.setdefault(f["page"], []).append((k, k + len(f["fix"]["old"]), f["fix"]["old"]))
for p, spans in by_page.items():
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
# applying all edits in sequence must work
for p in by_page:
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    for f in F:
        if f["page"] == p and f["fix"] is not None:
            assert t.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"])
print("all checks passed" if ok else "CHECKS FAILED")
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print(counts)
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(F))
