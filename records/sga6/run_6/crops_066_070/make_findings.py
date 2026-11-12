"""Write findings_066_070.json and check that every fix's old occurs exactly once in its page_NNN.tex.
usage: python -I make_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b066_070"

SHRIEK = ("The print distinguishes the hand-drawn lower shriek i_! from i_* (same page: 'i_* et i* proviennent "
          "par passage au quotient de i_! et i^!'); NOTE_6: report each.")
TODD = ("Handwritten script T of Todd (NOTE_6: \\mathcal T, report each); the print has no check accent on it "
        "(its top loop belongs to the letter).")


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if old is None else {"old": old, "new": new})
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


items = [
    # ---------------- p. 66
    F(66, "start of page",
      "p. 66 begins 'La formule (iv) exprime que i_! ...'; p. 65 ends with the ')' closing the parenthesis after (2.36) (both scans)",
      "'La' is the last line of page_065.tex (under the folio-65 marker); page_066.tex begins 'formule (iv)'",
      "marker", "high", None, None,
      "Page 66 really begins with 'La'. Move the folio-66 marker up one line, above 'La': python -I move_marker.py 6 66 \"La\" --before "
      "(simulated on both layers: ')', the marker, 'La', 'formule (iv)'). Apply once only: p. 65's checker may report the same move, "
      "and a second run would move the marker to an earlier 'La'."),
    F(66, "first sentence, 'exprime que i_! est un homomorphisme d'anneaux'",
      "exprime que i_! (lower shriek, both scans)", r"exprime que $i_*$ est", "symbol", "high",
      r"exprime que $i_*$ est", r"exprime que $i_!$ est", SHRIEK),
    F(66, "formula (v)", "(v) i_!(λ^p(N,x)) = λ^p(i_!(x)) pour p ≥ 1 , (both i with the lower shriek)",
      r"\item $i_*(\lambda^p(N,x))=\lambda^p(i_*(x))$", "symbol", "high",
      r"\item $i_*(\lambda^p(N,x))=\lambda^p(i_*(x))$", r"\item $i_!(\lambda^p(N,x))=\lambda^p(i_!(x))$", SHRIEK),
    F(66, "after (v): 'qui signifie que i_! définit un λ-homomorphisme'", "qui signifie que i_! définit",
      r"qui signifie que $i_*$ définit", "symbol", "high",
      r"qui signifie que $i_*$ définit", r"qui signifie que $i_!$ définit", SHRIEK),
    F(66, "last sentence, 'passage au quotient de i_! et i^!, en notant que i_! décale'",
      "par passage au quotient de i_! et i^!, en notant que i_! décale la filtration (both scans)",
      r"quotient de $i_*$ et $i^!$, en notant que $i_*$ décale", "symbol", "high",
      r"quotient de $i_*$ et $i^!$, en notant que $i_*$ décale", r"quotient de $i_!$ et $i^!$, en notant que $i_!$ décale",
      "The earlier 'que i_* et i* proviennent' of the same sentence is i_* in the print, as in the TeX. " + SHRIEK),
    F(66, "'pourvu qu'on se place dans G(K(Y)) et G(K(X)) et non dans A(Y) et A(X)'",
      "underlined: 'pourvu qu'on se place dans', 'et', 'et non' + 'dans' (line break), 'et'; the four formulas not (both scans)",
      "no underline", "underline", "high",
      r"pourvu qu'on se place dans $G(\underline K(Y))$ et $G(\underline K(X))$ et non dans $A(Y)$ et $A(X)$",
      r"\emph{pourvu qu'on se place dans} $G(\underline K(Y))$ \emph{et} $G(\underline K(X))$ \emph{et non dans} $A(Y)$ \emph{et} $A(X)$",
      "This file writes the typescript's underlined words in running text with \\emph (\\emph{locaux}, p. 69)."),
    F(66, "before 'Dans ces formules, q est la codimension'",
      "'Dans ces formules' starts a new, indented paragraph after (v bis) (both scans)",
      r"\end{enumerate} then 'Dans ces formules' on the next line (no blank line: no new paragraph)", "other", "medium",
      "\\end{enumerate}\nDans ces formules", "\\end{enumerate}\n\nDans ces formules", "Missing paragraph break."),
    F(66, "last line of page_066.tex: 'N.B.' (printed at the top of p. 67)",
      "N.B. typed plain: not underlined, not bold (both scans)", r"\textbf{N.B.}", "font", "medium",
      r"\textbf{N.B.}", "N.B.",
      "Not a label the typescript underlines, so the bold-label convention does not cover it; the TeX itself has a plain "
      "'N.B. L'homomorphisme' on p. 63. Filed under p. 66 because the line stands in page_066.tex: apply before the "
      "folio-67 marker move (see p. 67)."),
    # ---------------- p. 67
    F(67, "start of page",
      "p. 67 begins 'N.B. Toutes les formules \"universelles\" liant i_! et i^!'; p. 66 ends '... de q unités.' (both scans)",
      r"\textbf{N.B.} is the last line of page_066.tex (under the folio-66 marker); page_067.tex begins 'Toutes les formules'",
      "marker", "high", None, None,
      "Page 67 really begins with 'N.B.'. After the p. 66 font fix: python -I move_marker.py 6 67 \"N.B.\" --before; "
      "without that fix use the anchor \"\\textbf{N.B.}\" (both simulated on both layers: 'unités.', blank line, the marker, "
      "'N.B.', 'Toutes les formules'). With the font fix not applied, the anchor \"N.B.\" would put the marker inside the braces."),
    F(67, "N.B., 'liant i_! et i^! (resp. i_* et i*)'", "liant i_! et i^! (resp. i_* et i*)",
      r"liant $i_*$ et $i^!$", "symbol", "high",
      r"liant $i_*$ et $i^!$", r"liant $i_!$ et $i^!$", "The 'resp. i_* et i^*' is right. " + SHRIEK),
    F(67, "display after 'De la formule (v) résulte la formule'", "i_!(γ^p(N,x)) = γ^p(i_!(x)) . (both lower shrieks)",
      r"i_*(\gamma^p(N,x))=\gamma^p(i_*(x))", "symbol", "high",
      r"i_*(\gamma^p(N,x))=\gamma^p(i_*(x))", r"i_!(\gamma^p(N,x))=\gamma^p(i_!(x))", SHRIEK),
    F(67, "display after 'le théorème 2.16 montre que l'on a'", "i_*(G_p(N,x)) = c^p(i_!(x)) .",
      r"i_*(G_p(N,x))=c^p(i_*(x))", "symbol", "high",
      r"c^p(i_*(x))", r"c^p(i_!(x))", "The first i_* (before G_p) is right. " + SHRIEK),
    F(67, "(2.37), left side", "c^{q+j}(i_!(x)) = i_*( ... )^{(j)}", r"c^{q+j}(i_*(x))=i_*\left(", "symbol", "high",
      r"c^{q+j}(i_*(x))", r"c^{q+j}(i_!(x))", "The i_* of the right side is right. " + SHRIEK),
    F(67, "before 'Le deuxième membre de la formule (2.37)'",
      "'Le deuxième membre ...' starts a new, indented paragraph after (2.37) (both scans)",
      r"\end{equation} then 'Le deuxième membre' on the next line (no blank line: no new paragraph)", "other", "medium",
      "\\end{equation}\nLe deuxième membre", "\\end{equation}\n\nLe deuxième membre", "Missing paragraph break."),
    F(67, "(2.38), left side", "ch(c̃(i_!(x))) = i_*(...)", r"\ch(\widetilde c(i_*(x)))", "symbol", "high",
      r"\ch(\widetilde c(i_*(x)))", r"\ch(\widetilde c(i_!(x)))", SHRIEK),
    F(67, "(2.38), right side", "i_*(ch(c̃(x)) 𝒯(Ň)^{-1}): script T of Todd, the check over N (both scans)",
      r"\check{\mathcal C}(N)^{-1}", "symbol", "high",
      r"\check{\mathcal C}(N)^{-1}", r"\mathcal T(\check N)^{-1}",
      "Two differences in one place: \\mathcal C for the Todd T, and the check set on the letter instead of on N "
      "(the print's Ň, as in (1.30), p. 32: \\mathcal C(\\check N)^{-1}). " + TODD),
    # ---------------- p. 68
    F(68, "start of page", "p. 68 begins 'Il suffit d'utiliser (2.37) écrit sous la forme :' (indented; both scans)",
      "'Il' is the last line of page_067.tex (under the folio-67 marker); page_068.tex begins 'suffit d'utiliser'",
      "marker", "high", None, None,
      "Page 68 really begins with 'Il'. Move the folio-68 marker up one line: python -I move_marker.py 6 68 \"Il\" --before "
      "(simulated on both layers: '(1.26).', blank line, the marker, 'Il', 'suffit d'utiliser')."),
    F(68, "(2.37 bis), left side", "c̃(i_!(x)) = 1 + i_*( ... )", r"\widetilde c(i_*(x))=1+i_*", "symbol", "high",
      r"\widetilde c(i_*(x))=1+i_*", r"\widetilde c(i_!(x))=1+i_*", "The second i_* is right. " + SHRIEK),
    F(68, "(2.37 bis), numerator", "c̃(x) * λ_{-1}(c(N)) - 1: no tilde over the c of c(N) (both scans)",
      r"\lambda_{-1}(c(N)) (printed reading kept)", "misprint_in_print", "low", None, None,
      "(2.37 bis) is (2.37) 'écrit sous la forme', and (2.37) has λ_{-1}(c̃(N)): λ_{-1} is taken in the λ-ring of the c̃'s. "
      "Probably a hand-drawn tilde left out. The TeX keeps the printed reading; so does the corrected layer.",
      corrected=r"\lambda_{-1}(\widetilde c(N))"),
    F(68, "(2.38 bis)", "i_*(ch_Y(F) 𝒯(T_{X/Y})^{-1}) : script T of Todd, no check (both scans)",
      r"\check{\mathcal C}(T_{X/Y})^{-1}", "symbol", "high",
      r"\check{\mathcal C}(T_{X/Y})^{-1}", r"\mathcal T(T_{X/Y})^{-1}", TODD),
    F(68, "Remarques: 'le produit de leur différence par N^q est nulle'", "est nulle (both scans)",
      "est nulle (printed reading kept)", "misprint_in_print", "low", None, None,
      "Agreement slip: the subject is 'le produit'. The TeX keeps the printed reading; so does the corrected layer.",
      corrected="est nul"),
    # ---------------- p. 69
    F(69, "section heading", "§ 6. Le théorème de Riemann-Roch (both scans)", r"\section*{6. Le théorème de Riemann--Roch}",
      "missing", "high", r"\section*{6. Le", r"\section*{\S 6. Le",
      "The TeX drops the printed §; same form as \\subsection*{\\S 4. Quelques résultats techniques} (p. 54) and "
      "Chap. II §§ 1-3."),
    F(69, "statement of Riemann-Roch, 'soit f un morphisme propre d'une variété'",
      "'propre' not underlined; 'un morphisme' and 'd'une variété' underlined (both scans)",
      r"\emph{soit \(f\) un morphisme propre d'une variété ...} (propre inside the emphasis)", "underline", "high",
      r"un morphisme propre d'une variété", r"un morphisme} propre \emph{d'une variété",
      "A word the print leaves plain, not a formula or punctuation inside the block (the block decision does not cover it)."),
    F(69, "(2.39), left side", "f_*(ch_Y(x) 𝒯(Y)) : script T of Todd, no check (both scans)",
      r"\,\check{\mathcal C}(Y)\bigr)", "symbol", "high",
      r"\,\check{\mathcal C}(Y)\bigr)", r"\,\mathcal T(Y)\bigr)", TODD),
    F(69, "(2.39), right side", "ch_X(f_*(x)) 𝒯(X) . : script T of Todd, no check (both scans)",
      r"\,\check{\mathcal C}(X).", "symbol", "high",
      r"\,\check{\mathcal C}(X).", r"\,\mathcal T(X).", TODD),
    F(69, "after (2.39): '(Les deux membres sont dans A(X) ⊗ Q et 𝒯(X) = 𝒯(C(T_X)).)'",
      "𝒯(X) = 𝒯(C(T_X)) : script T of Todd twice, no check (both scans)",
      r"\(\check{\mathcal C}(X)=\check{\mathcal C}(C(T_X))\)", "symbol", "high",
      r"\(\check{\mathcal C}(X)=\check{\mathcal C}(C(T_X))\)", r"\(\mathcal T(X)=\mathcal T(C(T_X))\)", TODD),
    F(69, "'et l'on démontre (2.39) pour chacun de ces deux morphismes..'", "morphismes.. (two full stops, both scans)",
      "morphismes.. (printed reading kept)", "misprint_in_print", "high", None, None,
      "Typing slip. The TeX keeps the printed reading; so does the corrected layer.", corrected="morphismes."),
    # ---------------- p. 70
    F(70, "start of page",
      "p. 70 begins 'z ∈ K(X). Alors, la formule de Künneth ...'; p. 69 ends '... avec y ∈ K(P) et' (both scans)",
      r"'\(z\in\underline K(X)\).' ends the last line of page_069.tex (under the folio-69 marker); page_070.tex begins 'Alors,'",
      "marker", "high", None, None,
      "Page 70 really begins with 'z ∈ K(X).'. Split the line at the marker: python -I move_marker.py 6 70 "
      "\"\\(z\\in\\underline K(X)\\)\" --before (simulated on both layers: '... avec \\(y\\in\\underline K(P)\\) et', the marker, "
      "'\\(z\\in\\underline K(X)\\).', 'Alors, la formule' on the next line, same paragraph)."),
    F(70, "(2.40)", "χ(F) = ϰ_r(ch_P(F) 𝒯(P)) : subscript capital P, the space (both scans)",
      r"\varkappa_r\bigl(\ch_p(F)", "formula", "high",
      r"\varkappa_r\bigl(\ch_p(F)", r"\varkappa_r\bigl(\ch_P(F)",
      "Letter shapes measured: the subscripts of ch on this page have the capital P's short bowl and wide foot (as P in "
      "'(P)'), the exponents p of ξ^p and (1-e^{-L})^p the small p's deep bowl; ch_P as γ_P (TeX \\gamma_P)."),
    F(70, "(2.40), Todd class", "𝒯(P) : script T of Todd, no check (both scans)", r"\,\check{\mathcal C}(P)\bigr)",
      "symbol", "high", r"\,\check{\mathcal C}(P)\bigr)", r"\,\mathcal T(P)\bigr)", TODD),
    F(70, "display after 'd'où :'", "C_P(1 - ξ) = [1, 1 - L] , : capital C (height of E and L, not of the c of ch) and subscript capital P (both scans)",
      r"c_p(1-\xi)=[1,1-L],", "formula", "high",
      r"c_p(1-\xi)=[1,1-L]", r"C_P(1-\xi)=[1,1-L]",
      "C is the Chow-valued class: [1, 1 - L] is its pair [rank, total class], as \\Ctil(E)=[rang E, ΣC^i(E)] (2.4)."),
    F(70, "display after 'et par suite'", "ch_P(1 - ξ) = e^{-L} , d'où ch_P(ξ) = 1 - e^{-L} , (subscripts capital P)",
      r"\ch_p(1-\xi)=e^{-L},\qquad\text{d'où}\qquad \ch_p(\xi)=1-e^{-L},", "formula", "high",
      r"\ch_p(1-\xi)=e^{-L},\qquad\text{d'où}\qquad \ch_p(\xi)", r"\ch_P(1-\xi)=e^{-L},\qquad\text{d'où}\qquad \ch_P(\xi)",
      "As (2.40)."),
    F(70, "display after 'et donc'", "ch_P(ξ^p) = (1 - e^{-L})^p . (subscript capital P, exponents small p)",
      r"\ch_p(\xi^p)", "formula", "high", r"\ch_p(\xi^p)", r"\ch_P(\xi^p)", "As (2.40)."),
    F(70, "display after 'on en déduit', left side", "ch_P(F) 𝒯(P) = ... (subscript capital P)",
      r"\ch_p(F)\,\check{\mathcal C}(P)", "formula", "high",
      "\\[\n  \\ch_p(F)", "\\[\n  \\ch_P(F)", "As (2.40)."),
    F(70, "display after 'on en déduit', Todd class", "𝒯(P) : script T of Todd, no check (both scans)",
      r"\,\check{\mathcal C}(P) (end of line)", "symbol", "high",
      "\\,\\check{\\mathcal C}(P)\n", "\\,\\mathcal T(P)\n", TODD),
    F(70, "'Or si p est la dimension de Q dans P'", "Or si p est la dimension de Q dans P , on a ξ^p = γ_P(Q)",
      r"la dimension de \(Q\) dans \(P\) (printed reading kept)", "misprint_in_print", "medium", None, None,
      "ξ is the class of O_V for a hyperplane V, so ξ^p = γ_P(Q) for a linear Q cut out by p hyperplanes: p is the "
      "codimension, and the factor (1-e^{-L})^p of the next display uses it so. The TeX keeps the printed reading; so does "
      "the corrected layer.",
      corrected=r"la codimension de \(Q\) dans \(P\)"),
    F(70, "last line, '(poser q = r + 1 - p)'", "(poser q = r + 1 - p) .", r"(poser \(q=r+1-p\)) (printed reading kept)",
      "misprint_in_print", "medium", None, None,
      "(L/(1-e^{-L}))^{r+1}(1-e^{-L})^p = L^p (L/(1-e^{-L}))^{r+1-p}, so the coefficient of L^r is that of L^{r-p} in "
      "(L/(1-e^{-L}))^{r-p+1}: the stated property applies with q = r - p (q + 1 = r + 1 - p). The TeX keeps the printed "
      "reading; so does the corrected layer.",
      corrected=r"(poser \(q=r-p\))"),
]

# checks: every old occurs exactly once in its page file; no old crosses a marker; olds on one page do not overlap
bad = 0
spans = {}
for x in items:
    if not x["fix"]:
        continue
    page, old = x["page"], x["fix"]["old"]
    t = (B / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    n = t.count(old)
    if n != 1 or "%%%%%%%%%%" in old:
        bad += 1
        print("BAD", page, n, repr(old))
    k = t.find(old)
    spans.setdefault(page, []).append((k, k + len(old), old))
for page, ss in spans.items():
    ss.sort()
    for a, b in zip(ss, ss[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP", page, repr(a[2]), repr(b[2]))
out = RUN / "findings_066_070.json"
out.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for x in items:
    c = counts.setdefault(x["page"], [0, 0])
    c[x["kind"] == "misprint_in_print"] += 1
print("written", out, len(items), "items; bad", bad)
print({p: f"{c[0]}/{c[1]}" for p, c in sorted(counts.items())})
