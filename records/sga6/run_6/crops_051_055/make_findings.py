"""Write findings_051_055.json (SGA 6 pp. 51-55) and check every fix: each "old" must occur exactly once in its
page_NNN.tex at the point where it is applied (fixes of a page applied in list order, as process_sga.py does).
usage: python -I make_findings.py"""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
OUT = RUN / "findings_051_055.json"

SHRIEK = ("the print writes every direct image on pp. 53-54 (of sheaves and in K) with a hand-drawn exclamation mark "
          "under the letter, f_! (lower shriek), seen in both scans; the TeX has f_* in all 20 places, each given "
          "with its own fix. The TeX itself writes f_! for the print's lower shriek on pp. 69-76.")

F = []

# ---------------- p. 52
F.append(dict(
    page=52, where="'on a f^!(O_Z) = O_{f^{-1}(Z)}' (convention of the appendix)",
    scan="typed capital O, underlined: f^!(O_Z) = O_{f^{-1}(Z)} (both scans); the same underlined typed O on p. 47 "
         "(witness): (2.14) f(E) = g(O_X(E)), 'en notant O_X(E)', 'de la forme O_X(E_i)'",
    tex="$f^!(\\cO_Z)=\\cO_{f^{-1}(Z)}$ (\\cO is \\mathcal O)",
    kind="font", confidence="medium", fix=None,
    note="Convention of the transcription in the appendix, not a page fix: the TeX writes \\cO (\\mathcal O) for the "
         "typescript's underlined typed O, which Exposé 0 writes \\underline O (\\underline O_X, pp. 4-12), as the "
         "appendix itself writes \\underline K, \\underline E, \\underline L. \\cO in the diplomatic main.tex: pp. "
         "45-49, 52, 58, 63, 65 (and p. 84). If the volume follows the print, here: "
         "$f^!(\\underline O_Z)=\\underline O_{f^{-1}(Z)}$."))

# ---------------- p. 53
F.append(dict(
    page=53, where="start of page",
    scan="p. 52 ends with the opening of Proposition 2.8: 'Proposition 2.8. Soit f : X -> Y un morphisme de variétés "
         "non singulières, et soit Z un cycle sur Y. Si Z est partout transversal à f, la formule'; p. 53 begins "
         "'(2.22) est exacte ; si Z est homogène de codimension i ...' (both scans; witness p. 64)",
    tex="the whole statement \\emph{Soit $f:X\\longrightarrow Y$ ... on a~:} stands under the folio-53 marker (the "
        "marker could not split the \\emph argument)",
    kind="marker", confidence="high",
    fix={"old": "la formule (2.22) est exacte", "new": "la formule}\n\\emph{(2.22) est exacte"},
    note="Page 53 really begins with '(2.22) est exacte'. The fix closes the \\emph after 'la formule' and opens a "
         "new one before '(2.22)' (prints the same), so that the marker can stand between the two groups. Then move "
         "the marker: python -I move_marker.py 6 53 \"\\emph{(2.22) est exacte\" (no --before: the anchor follows "
         "the marker's present place). Simulated on both layers: '\\textbf{Proposition 2.8.}', '\\emph{Soit ... la "
         "formule}', the marker, '\\emph{(2.22) est exacte~; ... on a~:}'."))
F.append(dict(
    page=53, where="'le faisceau image directe f_!(F) est algébrique cohérent'",
    scan="f_!(F) (hand-drawn lower shriek, both scans)", tex="$f_*(F)$",
    kind="symbol", confidence="high",
    fix={"old": "image directe $f_*(F)$", "new": "image directe $f_!(F)$"},
    note=SHRIEK[0].upper() + SHRIEK[1:]))
F.append(dict(
    page=53, where="'des faisceaux R^q f_!(F) (cf. [3])'",
    scan="R^qf_!(F) (both scans)", tex="$R^qf_*(F)$",
    kind="symbol", confidence="high",
    fix={"old": "faisceaux $R^qf_*(F)$", "new": "faisceaux $R^qf_!(F)$"},
    note="Lower shriek, as in the first finding of this page."))
F.append(dict(
    page=53, where="'par définition, R^q f_!(F) est le faisceau sur Y'",
    scan="R^qf_!(F) (both scans)", tex="$R^qf_*(F)$",
    kind="symbol", confidence="high",
    fix={"old": "définition, $R^qf_*(F)$", "new": "définition, $R^qf_!(F)$"},
    note="Lower shriek."))
F.append(dict(
    page=53, where="(2.24)",
    scan="R^of_!(F) = f_!(F),  R^qf_!(F) = 0 (both scans)", tex="R^0f_*(F)=f_*(F),\\qquad R^qf_*(F)=0",
    kind="symbol", confidence="high",
    fix={"old": "R^0f_*(F)=f_*(F),\\qquad R^qf_*(F)=0", "new": "R^0f_!(F)=f_!(F),\\qquad R^qf_!(F)=0"},
    note="Lower shriek, three times."))
F.append(dict(
    page=53, where="(2.25)",
    scan="Γ(U,R^qf_!(F)) (both scans)", tex="\\Gamma(U,R^qf_*(F))",
    kind="symbol", confidence="high",
    fix={"old": "\\Gamma(U,R^qf_*(F))", "new": "\\Gamma(U,R^qf_!(F))"},
    note="Lower shriek."))
F.append(dict(
    page=53, where="'noté encore f_! , par la formule'",
    scan="f_! (both scans)", tex="$f_*$",
    kind="symbol", confidence="high",
    fix={"old": "noté encore $f_*$", "new": "noté encore $f_!$"},
    note="Lower shriek."))
F.append(dict(
    page=53, where="(2.26)",
    scan="f_!(γ_X(F)) = Σ_{q≥0} (-1)^q γ_Y(R^qf_!(F)) . (both scans)",
    tex="f_*(\\gamma_X(F))=\\sum_{q\\geq0}(-1)^q\\gamma_Y(R^qf_*(F)).",
    kind="symbol", confidence="high",
    fix={"old": "f_*(\\gamma_X(F))=\\sum_{q\\geq0}(-1)^q\\gamma_Y(R^qf_*(F))",
         "new": "f_!(\\gamma_X(F))=\\sum_{q\\geq0}(-1)^q\\gamma_Y(R^qf_!(F))"},
    note="Lower shriek, twice."))
F.append(dict(
    page=53, where="'La relation (fg) = f_!g_!', right side",
    scan="f_!g_! (both scans)", tex="$(fg)_*=f_*g_*$",
    kind="symbol", confidence="high",
    fix={"old": "$(fg)_*=f_*g_*$", "new": "$(fg)_!=f_!g_!$"},
    note="Lower shriek. This fix also gives (fg) the subscript _! of the correct reading (for the corrected layer); "
         "the misprint fix that follows removes it in the diplomatic layer. Apply this one first."))
F.append(dict(
    page=53, where="'La relation (fg) = f_!g_!', left side",
    scan="(fg) = f_!g_!: no mark under (fg), only the typist's gap before '=' (both scans; f and g have their "
         "hand-drawn marks, and the next line has (fg)^! = g^!f^!)",
    tex="$(fg)_*=f_*g_*$: the subscript of (fg) silently supplied",
    kind="misprint_in_print", confidence="medium",
    fix={"old": "$(fg)_!=", "new": "$(fg)="},
    corrected="(fg)_!=f_!g_!",
    note="The hand-drawn _! of (fg) was never added. Its old is taken from the text after the symbol fix listed just "
         "before (apply in this order)."))

# ---------------- p. 54
F.append(dict(
    page=54, where="start of page",
    scan="p. 53 ends '... est un cas parti-'; p. 54 begins 'culier des relations de transitivité' (both scans; "
         "witness pp. 64-65)",
    tex="'est un cas' ends the last line of page_053.tex; page_054.tex begins 'particulier'",
    kind="marker", confidence="medium", fix=None,
    note="Page 54 really begins with 'culier' (the word is divided at the page break). As at the folio-18 marker "
         "('cet ex%' / marker / 'pos\\'e est'), by hand in both layers replace 'est un cas\\n%%%%%%%%%%  scan idx 67  "
         "|  folio 54  %%%%%%%%%%\\nparticulier' by 'est un cas parti%\\n%%%%%%%%%%  scan idx 67  |  folio 54  "
         "%%%%%%%%%%\\nculier' (the pattern occurs once in each layer; simulated: 'particulier' stays one word)."))
F.append(dict(
    page=54, where="(2.27)",
    scan="f_!(x.f^!(y)) = f_!(x).y (both scans)", tex="f_*(x.f^!(y))=f_*(x).y",
    kind="symbol", confidence="high",
    fix={"old": "f_*(x.f^!(y))=f_*(x).y", "new": "f_!(x.f^!(y))=f_!(x).y"},
    note="Lower shriek, twice: " + SHRIEK))
F.append(dict(
    page=54, where="(2.27), '(x.∈ K(X) , y ∈ K(Y))'",
    scan="(x.∈ K(X) , y ∈ K(Y)): a typed full stop after x (both scans)",
    tex="(x.\\in\\underline K(X),\\ y\\in\\underline K(Y)) (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="(x\\in\\underline K(X),\\ y\\in\\underline K(Y))",
    note="Stray full stop after x (as in the product x.f^!(y) of the same display). The TeX keeps the printed reading."))
F.append(dict(
    page=54, where="'le foncteur F -> f_!(F) est exact'",
    scan="F ---> f_!(F) (both scans)", tex="$F\\longrightarrow f_*(F)$",
    kind="symbol", confidence="high",
    fix={"old": "F\\longrightarrow f_*(F)", "new": "F\\longrightarrow f_!(F)"},
    note="Lower shriek."))
F.append(dict(
    page=54, where="'et que R^qf_!(F) = 0 pour q > 0'",
    scan="R^qf_!(F) = 0 (both scans)", tex="$R^qf_*(F)=0$",
    kind="symbol", confidence="high",
    fix={"old": "$R^qf_*(F)=0$", "new": "$R^qf_!(F)=0$"},
    note="Lower shriek."))
F.append(dict(
    page=54, where="'dans ce cas, on a donc f_!(γ_X(F)) = γ_Y(f_!(F))'",
    scan="f_!(γ_X(F)) = γ_Y(f_!(F)) (both scans)", tex="$f_*(\\gamma_X(F))=\\gamma_Y(f_*(F))$",
    kind="symbol", confidence="high",
    fix={"old": "$f_*(\\gamma_X(F))=\\gamma_Y(f_*(F))$", "new": "$f_!(\\gamma_X(F))=\\gamma_Y(f_!(F))$"},
    note="Lower shriek, twice."))
F.append(dict(
    page=54, where="'si i est l'injection canonique de Y dans X'",
    scan="l'injection canonique de Y dans X (both scans)",
    tex="l'injection canonique de $Y$ dans $X$ (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="l'injection canonique de $X$ dans $Y$",
    note="X is the subspace of Y and (2.28) reads i_!(γ_X(F)) = γ_Y(F), so i goes from X to Y; the print exchanges "
         "the two letters. The TeX keeps the printed reading."))
F.append(dict(
    page=54, where="'... de Y dans X, on a :' before (2.28)",
    scan="'X, on a :' with a colon (both scans)", tex="'dans $X$, on a' with no colon",
    kind="punctuation", confidence="high",
    fix={"old": "dans $X$, on a\n", "new": "dans $X$, on a~:\n"},
    note="The colon before the display is left out."))
F.append(dict(
    page=54, where="(2.28)",
    scan="i_!(γ_X(F)) = γ_Y(F) , (both scans)", tex="i_*(\\gamma_X(F))=\\gamma_Y(F),",
    kind="symbol", confidence="high",
    fix={"old": "i_*(\\gamma_X(F))", "new": "i_!(\\gamma_X(F))"},
    note="Lower shriek."))
F.append(dict(
    page=54, where="section heading '§ 4. Quelques résultats techniques'",
    scan="§ 4. Quelques résultats techniques (both scans)", tex="\\subsection*{4. Quelques résultats techniques}",
    kind="missing", confidence="high",
    fix={"old": "\\subsection*{4. Quelques", "new": "\\subsection*{\\S 4. Quelques"},
    note="The section sign is left out; the TeX has it in the headings of §§ 1-3 of this chapter "
         "(\\subsection*{\\S 3. Généralités fonctorielles sur $\\underline{K}(X)$})."))

# ---------------- p. 55
F.append(dict(
    page=55, where="'d'après la proposition 2.10, γ_{X×k}(D) - p^!(y)) provient'",
    scan="γ_{X×k}(D) - p^!(y)) : two closing parentheses, none opened (both scans)",
    tex="$\\gamma_{X\\times k}(D)-p^!(y))$ (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="\\gamma_{X\\times k}(D)-p^!(y)",
    note="Unbalanced parenthesis of the print, kept by the diplomatic TeX; the corrected layer already reads p^!(y)."))
F.append(dict(
    page=55, where="label of the corollary",
    scan="Corollaire : (colon after the underlined label, both scans)", tex="\\textbf{Corollaire.}",
    kind="punctuation", confidence="high",
    fix={"old": "\\textbf{Corollaire.}", "new": "\\textbf{Corollaire~:}"},
    note="The print has a colon, not a full stop (the TeX has \\textbf{Corollaire~:} for the same form on p. 45)."))
F.append(dict(
    page=55, where="end of page",
    scan="p. 55 ends '... Alors la suite d'homomorphismes naturels :'; p. 56 begins with the display '(2.30) K(Y) "
         "--> K(X) --> K(U) --> 0', then 'est exacte.' (both scans; witness p. 67)",
    tex="page_055.tex ends with \\begin{equation}\\tag{2.30} ... \\end{equation}, which belongs to p. 56",
    kind="marker", confidence="high", fix=None,
    note="Move the folio-56 marker above that display: python -I move_marker.py 6 56 "
         "\"\\begin{equation}\\tag{2.30}\" --before (simulated on both layers: '... homomorphismes naturels~:}', "
         "the marker, \\begin{equation}\\tag{2.30}, ..., '\\emph{est exacte.}'). The display agrees with the print "
         "of p. 56."))

# ---------------- write and check
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
ok = True
texts = {}
for x in F:
    p = x["page"]
    if p not in texts:
        texts[p] = (RUN / "b051_055" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    fx = x.get("fix")
    if not fx:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", p, n, repr(fx["old"]))
        continue
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("TOUCHES MARKER", p, repr(fx["old"]))
    texts[p] = texts[p].replace(fx["old"], fx["new"])
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("all fixes unique in sequence" if ok else "PROBLEMS", {p: tuple(c) for p, c in sorted(counts.items())})
print(len(F), "findings written to", OUT)
