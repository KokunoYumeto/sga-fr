"""Writes run_6/findings_351_355.json (SGA 6, folios 351-355) and checks every fix against its page_NNN.tex.
In the LaTeX strings below, the character U+23CE stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b351_355"
OUT = RUN / "findings_351_355.json"
NL = "\u23ce"


def L(s):
    return s.replace(NL, "\n")


def fix(old, new):
    return {"old": L(old), "new": L(new)}


M351 = "%%%%%%%%%%  scan idx 364  |  folio 351  %%%%%%%%%%"
M352 = "%%%%%%%%%%  scan idx 365  |  folio 352  %%%%%%%%%%"
M353 = "%%%%%%%%%%  scan idx 366  |  folio 353  %%%%%%%%%%"

F = []


def add(page, where, scan, tex, kind, conf, fx, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fx}
    if corrected is not None:
        d["corrected"] = L(corrected)
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 351
add(351, "start of page (folio-351 marker)",
    "p. 351 begins 'où A est l'anneau K[X_1,...,X_n], filtré par le poids'; p. 350 ends '... il suffit de faire la "
    "démonstration dans le cas' (both scans)",
    "'où \\(A\\) est l'%' ends the last line of page_350.tex, above the folio-351 marker; page_351.tex begins 'anneau'",
    "marker", "high", None,
    "The folio-351 marker stands four words late. Page 351 really begins at 'où \\(A\\) est l'anneau'. Exact fix in "
    "main.tex (both layers, once each): replace 'dans le cas où \\(A\\) est l'%\\n" + M351 + "\\nanneau' by "
    "'dans le cas\\n" + M351 + "\\noù \\(A\\) est l'anneau' (the line end after 'cas' keeps the space; the % is no "
    "longer needed). Equivalent: python -I move_marker.py 6 351 'où \\(A\\) est' --before (leaves 'l'%' and "
    "'anneau' joined by the comment as now). Both simulated in memory on both layers of the live main.tex with "
    "crops_351_355/sim_markers.py (one match each; same text after the move). The checker of p. 350 may report the "
    "same boundary: apply once.")

add(351, "after 'et pour l'élément (n,1+X_1+...+X_n).'",
    "'On plonge A dans A' = K[T_1,...,T_n] ...' begins a new, indented paragraph (both scans)",
    "...+X_n)\\). On plonge (same paragraph)", "other", "high",
    fix(r"X_n)\). On plonge", r"X_n)\).⏎⏎On plonge"),
    "Missing paragraph break.")

add(351, "first display, end: '= Σ_{i=1}^n (1,1+T_i)'",
    "no full stop after (1,1+T_i) (both scans)", r"\sum_{i=1}^n(1,1+T_i).", "punctuation", "high",
    fix(r"\sum_{i=1}^n(1,1+T_i).", r"\sum_{i=1}^n(1,1+T_i)"),
    "Full stop added by the transcription at the end of a display.")

add(351, "display 'λ^k(x) = 0 pour k > n, et λ^n(x) = ... = (1,1+X_1)', end",
    "no full stop after (1,1+X_1) (both scans)", r"=(1,1+X_1).", "punctuation", "high",
    fix(r"=(1,1+X_1).", r"=(1,1+X_1)"),
    "Full stop added by the transcription at the end of a display.")

add(351, "'Enfin, Σ_{i=1}^n (-1)^iλ^i(x) = λ_{-1}(x) = ... = (-1)^n.∏(0,1+T_i) .'",
    "the formula follows 'Enfin,' in the running line at the left margin, the full stop at the end of the same line "
    "(both scans)",
    r"Enfin, \[ ... \] (a display)", "other", "medium",
    fix(r"Enfin,⏎\[⏎  \sum_{i=1}^n(-1)^i\lambda^i(x)=\lambda_{-1}(x)⏎  =⏎  \prod_{i=1}^n\bigl(1-(1,1+T_i)\bigr)⏎  =⏎"
        r"  (-1)^n.\prod_{i=1}^n(0,1+T_i).⏎\]",
        r"Enfin, \(\sum_{i=1}^n(-1)^i\lambda^i(x)=\lambda_{-1}(x)=\prod_{i=1}^n\bigl(1-(1,1+T_i)\bigr)"
        r"=(-1)^n.\prod_{i=1}^n(0,1+T_i)\)."),
    "The print sets the formula inline after 'Enfin,'; the TeX makes it a display (same kind of fix as pp. 301, "
    "303, 326, 332, 338). The edit keeps the printed lower index i=1 of the sum (misprint entry that follows, fix "
    "null).")

add(351, "'Enfin, Σ (-1)^iλ^i(x) = λ_{-1}(x)': lower index of the sum",
    "Σ with n above and i=1 below (both scans; crops_351_355/p351_enfin.png)",
    r"\sum_{i=1}^n(-1)^i\lambda^i(x)=\lambda_{-1}(x) (printed reading kept)", "misprint_in_print", "high", None,
    "λ_{-1}(x) = Σ_{i≥0}(-1)^iλ^i(x) includes λ^0(x) = 1; with i=1 the left member has augmentation -1 while "
    "λ_{-1}(x) = (0, ...) has augmentation 0, and the relation 6.6.1 iii) being proved (p. 350) reads Σ_{i=0}^n. "
    "The TeX keeps the printed reading; the corrected layer already reads i=0.",
    corrected=r"\sum_{i=0}^n(-1)^i\lambda^i(x)=\lambda_{-1}(x)")

add(351, "'Or, d'après (6.5.3), ∏_{i=1}^n(0,1+T_i) = (0,1+(-1)^{n-1}(n-1)!∏T_i +...)'",
    "the formula follows 'Or, d'après (6.5.3),' in the running line; no comma after the closing parenthesis (both "
    "scans; crops_351_355/p351_or.png)",
    r"Or, d'après (6.5.3), \[ ... \right), \] (a display ending with a comma)", "other", "medium",
    fix(r"Or, d'après (6.5.3),⏎\[⏎  \prod_{i=1}^n(0,1+T_i)⏎  =⏎"
        r"  \left(0,1+(-1)^{n-1}(n-1)!\prod_{i=1}^nT_i+\cdots\right),⏎\]",
        r"Or, d'après (6.5.3), \(\prod_{i=1}^n(0,1+T_i)=\left(0,1+(-1)^{n-1}(n-1)!\prod_{i=1}^nT_i+\cdots\right)\)"),
    "The print sets the formula inline (as 'Enfin,' above) and has no comma after it; the edit does both. If the "
    "display is kept, drop only the added comma: '\\cdots\\right),' -> '\\cdots\\right)' (unique on the page).")

add(351, "'soit : λ_{-1}(x) = (0,1 - (n-1)!X_n +...) .'",
    "the formula follows 'soit :' in the running line, then the full stop (both scans)",
    r"soit : \[ \lambda_{-1}(x)=(0,1-(n-1)!X_n+\cdots). \] (a display)", "other", "medium",
    fix(r"soit :⏎\[⏎  \lambda_{-1}(x)=(0,1-(n-1)!X_n+\cdots).⏎\]",
        r"soit : \(\lambda_{-1}(x)=(0,1-(n-1)!X_n+\cdots)\)."),
    "Inline in the print, display in the TeX (as the two entries above). Independent of them (the 'old' strings do "
    "not overlap).")

add(351, "proof of Lemme 6.6.3: 'γ^i(0,φ) = (0,1+Q''_{i,1}+...+Q''_{i,j}+..) les Q''_{i,j} étant'",
    "no comma between the closing parenthesis and 'les' (both scans; crops_351_355/p351_gamma.png)",
    r"+\cdots)\), les", "punctuation", "high",
    fix(r"+\cdots)\), les", r"+\cdots)\) les"),
    "Comma added by the transcription.")

add(351, "statements of pp. 351-355: Corollaire 6.6.2, Lemme 6.6.3 (p. 351); Corollaires 6.6.4, 6.6.5, 6.6.7 "
         "(p. 352); Proposition 6.8 (p. 353); Proposition 6.9 (p. 354); Proposition 6.10 (p. 355)",
    "underlined word groups: 6.6.2 'La relation', 'est vraie pour tout élément', 'd'augmentation'; 6.6.3 'Pour tout', "
    "'est un', 'idéal de' (λ- plain); 6.6.4 'Soit', 'l'homomorphisme d'augmentation de', 'alors', 'pour tout', "
    "'on a'; 6.6.5 'Avec les notations de'; 6.6.7 'Soit', 'une', 'algèbre graduée de caractéristique nulle', "
    "'à degrés bornés', 'alors les deux filtrations définies sur', 'sont', 'identiques'; 6.8 'La classe de Chern "
    "complétée', 'est', 'un', 'homomorphisme de', 'algèbres augmentées'; 6.9 'Soit', 'une', 'algèbre augmentée', "
    "'alors', and the i and the e of 'i.e.'; 6.10 'Soient', 'un anneau binômial', 'une', 'algèbre augmen-tée', "
    "'un élément de', 'tel que', 'pour', 'et', 'Alors' (both scans)",
    "the eight statements in roman (no \\underline, no \\emph); 'i.e.' plain", "underline", "high", None,
    "Exposé V continues the GLOBAL_ISSUES 82 pattern (as reported for pp. 323, 325, 330, 336-340): not itemized, "
    "for the scripted per-exposé decision; the word groups are listed for that script. Formulas, letters and "
    "numbers inside the statements are plain in the print. The underlined defined term of 6.7 (p. 353) is a "
    "separate entry.")

# ---------------------------------------------------------------- page 352
add(352, "start of page (folio-352 marker)",
    "p. 352 begins '(ChA)_n est un λ-idéal.' and then the indented 'Soit alors x = (n,1+a_1+...)'; p. 351 ends "
    "'... les γ^i(x) appartiennent à (ChA)_n , et' (both scans)",
    "'\\((\\Ch A)_n\\) est un \\(\\lambda\\)-idéal.' ends the last paragraph of page_351.tex, above the folio-352 "
    "marker; page_352.tex begins 'Soit alors'",
    "marker", "high", None,
    "The folio-352 marker stands one sentence late. Page 352 really begins at '\\((\\Ch A)_n\\) est un "
    "\\(\\lambda\\)-idéal.'. Exact fix in main.tex (both layers, once each): replace ' \\((\\Ch A)_n\\) est un "
    "\\(\\lambda\\)-idéal.\\n\\n" + M352 + "\\nSoit alors' by '\\n" + M352 + "\\n\\((\\Ch A)_n\\) est un "
    "\\(\\lambda\\)-idéal.\\n\\nSoit alors' (begins with the space after 'et'). Equivalent: python -I "
    "move_marker.py 6 352 '\\((\\Ch A)_n\\) est un \\(\\lambda\\)-idéal.' --before (the last match before the "
    "marker is the right one; Lemme 6.6.3 has 'idéal de'). Simulated in memory on both layers with "
    "crops_351_355/sim_markers.py: '... appartiennent à \\((\\Ch A)_n\\), et' / marker / '\\((\\Ch A)_n\\) est un "
    "\\(\\lambda\\)-idéal.' / blank / 'Soit alors ...'. Independent of the folio-351 and folio-353 moves.")

add(352, "Corollaire 6.6.4, display 'γ^n(x-ε(x)) = (0,1+(-1)^{n-1}(n-1)!a_n + ... )'",
    "no full stop after the closing parenthesis (both scans; crops_351_355/p352_disp.png)",
    r"(0,1+(-1)^{n-1}(n-1)!a_n+\cdots).", "punctuation", "high",
    fix(r"(-1)^{n-1}(n-1)!a_n+\cdots).", r"(-1)^{n-1}(n-1)!a_n+\cdots)"),
    "Full stop added by the transcription at the end of a display. Independent of the paragraph entry below.")

add(352, "after the display of Corollaire 6.6.4, before 'Par définition'",
    "'Par définition, γ^n(x-ε(x)) = ...' begins a new, indented paragraph (the proof) (both scans)",
    "\\]\\nPar définition (same paragraph as the display)", "other", "high",
    fix(r"\]⏎Par définition", r"\]⏎⏎Par définition"),
    "Missing paragraph break.")

add(352, "'Par définition, γ^n(x-ε(x)) = (-1)^n Σ_{i=0}^n (-1)^iλ(x+n-ε(x))'",
    "λ(x+n-ε(x)) without the superscript i: the only i is the exponent of (-1) (both scans; "
    "crops_351_355/p352_pardef.png)",
    r"(-1)^i\lambda(x+n-\epsilon(x)) (printed reading kept)", "misprint_in_print", "high", None,
    "The definition (1.23) reads γ^n(x) = (-1)^nΣ_{i=0}^n(-1)^iλ^i(x+n); the sum needs λ^i. The TeX keeps the "
    "printed reading; the corrected layer has the same misprint.",
    corrected=r"(-1)^i\lambda^i(x+n-\epsilon(x))")

add(352, "Corollaire 6.6.5, before 'D'après le corollaire précédent'",
    "'D'après le corollaire précédent, γ^n(x-ε(x)) ∈ (ChA)_n. ...' begins a new, indented paragraph after the "
    "statement (both scans)",
    r"\subset(\Ch A)_n\). D'après (the proof runs on in the statement's paragraph)", "other", "high",
    fix(r"\subset(\Ch A)_n\). D'après", r"\subset(\Ch A)_n\).⏎⏎D'après"),
    "Missing paragraph break between statement and proof.")

add(352, "Corollaire 6.6.5, 'Fil_n ChA ⊂ (ChA)_n'",
    "Fil with a lowered n (subscript), as the n of (ChA)_n (both scans)",
    r"\Fil_n\Ch A\subset(\Ch A)_n (printed reading kept)", "misprint_in_print", "low", None,
    "The λ-filtration of 3.10 is Fil^n (superscript) everywhere else (Fil^n A in 3.10, Fil^nChA on p. 353, "
    "Fil^mA, Fil^{m+1}A, Fil^iR on pp. 354-355); the subscript here looks like a typing slip, but it may be the "
    "author's notation: low confidence. The TeX keeps the printed reading; the corrected layer too.",
    corrected=r"\Fil^n\Ch A\subset(\Ch A)_n")

add(352, "proof of Corollaire 6.6.7: 'on a alors : γ^n(x') = (0,1+a_n+...+a'_p), car x' est d'augmentation nulle'",
    "the formula stands at the left margin of the next text line, at ordinary line spacing, and the sentence goes on "
    "in the same line ', car x' est ...' (both scans; crops_351_355/p352_end.png)",
    r"\[ \gamma^n(x')=(0,1+a_n+\cdots+a'_p), \] car ...", "other", "medium",
    fix(r"\[⏎  \gamma^n(x')=(0,1+a_n+\cdots+a'_p),⏎\]⏎car", r"\(\gamma^n(x')=(0,1+a_n+\cdots+a'_p)\), car"),
    "Inline formula made a display (same kind of fix as p. 326 'ou encore γ_t(f(x)) = ...').")

add(352, "last line of the page: 'Par suite,'",
    "comma after 'Par suite' (both scans; crops_351_355/p352_end.png)",
    r"Par suite \(x-\gamma^n(x')\in", "punctuation", "high",
    fix(r"nulle. Par suite", r"nulle. Par suite,"),
    "The comma is dropped in the TeX. Independent of the folio-353 marker move (either order: the move's 'old' "
    "begins at the space after 'suite').")

# ---------------------------------------------------------------- page 353
add(353, "start of page (folio-353 marker)",
    "p. 353 begins 'x - γ^n(x') ∈ (ChA)_{n+1}. En itérant l'opération p-n fois'; p. 352 ends '... car x' est "
    "d'augmentation nulle. Par suite,' (both scans)",
    "'\\(x-\\gamma^n(x')\\in(\\Ch A)_{n+1}\\). En' ends the last line of page_352.tex, above the folio-353 "
    "marker; page_353.tex begins 'itérant'",
    "marker", "high", None,
    "The folio-353 marker stands one sentence late. Page 353 really begins at '\\(x-\\gamma^n(x')\\in(\\Ch "
    "A)_{n+1}\\). En itérant'. Exact fix in main.tex (both layers, once each): replace ' \\(x-\\gamma^n(x')\\in"
    "(\\Ch A)_{n+1}\\). En\\n" + M353 + "\\nitérant' by '\\n" + M353 + "\\n\\(x-\\gamma^n(x')\\in(\\Ch "
    "A)_{n+1}\\). En itérant' (begins with the space after 'suite', so it works before or after the p. 352 comma "
    "entry). Equivalent: python -I move_marker.py 6 353 \"\\(x-\\gamma^n(x')\\in\" --before. Simulated in memory "
    "on both layers with crops_351_355/sim_markers.py: '... nulle. Par suite' / marker / '\\(x-\\gamma^n(x')\\in"
    "(\\Ch A)_{n+1}\\). En itérant l'opération ...'.")

add(353, "6.7, 'on appelle classe de Chern totale de x'",
    "the underline runs on over 'de' at the start of the next line: 'classe de Chern totale de' (both scans; "
    "crops_351_355/p353_de.png)",
    r"\emph{classe de Chern totale} de \(x\)", "underline", "high",
    fix(r"\emph{classe de Chern totale} de", r"\emph{classe de Chern totale de}"),
    "Underline extent; the file writes this underline with \\emph.")

add(353, "(6.7.1), end: 'c(x) = 1 + c^1(x) + ...'",
    "the three dots of the series end the formula; no full stop (both scans; crops_351_355/p353_671.png)",
    r"c(x)=1+c^1(x)+\cdots .", "punctuation", "high",
    fix(r"c(x)=1+c^1(x)+\cdots .", r"c(x)=1+c^1(x)+\cdots"),
    "Full stop added by the transcription at the end of a display.")

add(353, "Proposition 6.8, 'La classe de Chern complétée c : A → Ch(GrA), est'",
    "plain c, no tilde (both scans; crops_351_355/p353_prop.png); the tilde stands in (6.7.2) and in 'on appelle "
    "c̃(x) la classe de Chern complétée' just above",
    r"\(c:A\longrightarrow\Ch(\Gr A)\) (printed reading kept)", "misprint_in_print", "medium", None,
    "The complete Chern class with values in Ch(Gr A) is c̃ (6.7.2); c takes values in 1+Gr^+ (6.7.1). The hand-"
    "added tilde is missing. The TeX keeps the printed reading; the corrected layer already reads \\widetilde c.",
    corrected=r"\(\widetilde c:A\longrightarrow\Ch(\Gr A)\)")

add(353, "display 'γ_t(xy-ε(xy)) = ...', end of the second line",
    "'... .(γ_t(x-ε(x))∇γ_t(y-ε(y)))' with no comma; the page ends there (both scans; "
    "crops_351_355/p353_dispend.png)",
    r"\nabla\gamma_t(y-\epsilon(y))\bigr),", "punctuation", "high",
    fix(r"\nabla\gamma_t(y-\epsilon(y))\bigr),", r"\nabla\gamma_t(y-\epsilon(y))\bigr)"),
    "Comma added by the transcription at the end of a display.")

# ---------------------------------------------------------------- page 354
add(354, "after 'd'où le résultat d'après (6.1.2) en passant au quotient.'",
    "'Si a ∈ K, c̃(a) = (a,1), ...' begins a new, indented paragraph (both scans)",
    "au quotient. Si (same paragraph)", "other", "high",
    fix(r"au quotient. Si", r"au quotient.⏎⏎Si"),
    "Missing paragraph break.")

add(354, "diagram, bottom arrow ChA → Ĝ_g(ChA)",
    "label γt above the bottom arrow, as on the top arrow (both scans; crops_351_355/p354_diag.png)",
    "\\arrow[r,\"\\gamma_t\"'] (the ' sets the label below the arrow)", "formula", "medium",
    fix("\\arrow[r,\"\\gamma_t\"']", "\\arrow[r,\"\\gamma_t\"]"),
    "Label on the wrong side of the arrow (as reported on pp. 41, 59, 74); the other three labels stand as printed "
    "(c̃ left, Ĝ_g(c̃) right, γt above the top arrow).")

add(354, "diagram, lower right corner 'Ĝ_g(ChA)'",
    "no full stop after the diagram (both scans)",
    r"\widehat G_g(\Ch A).", "punctuation", "high",
    fix(r"\widehat G_g(\Ch A).", r"\widehat G_g(\Ch A)"),
    "Full stop added by the transcription inside the diagram.")

add(354, "after the diagram, before 'Par additivité'",
    "'Par additivité, il suffit ...' begins a new, indented paragraph (both scans)",
    "\\]\\nPar additivité (same paragraph as the diagram)", "other", "high",
    fix(r"\]⏎Par additivité", r"\]⏎⏎Par additivité"),
    "Missing paragraph break.")

add(354, "proof of Proposition 6.9: 'avec a ∈ A ε(x_i) = 0 pour tout i'",
    "no comma after 'a ∈ A' at the end of the line; the next line begins 'ε(x_i) = 0' (both scans; "
    "crops_351_355/p354_avec.png)",
    r"\(a\in A\), \(\epsilon(x_i)=0\) (silently corrected)", "misprint_in_print", "medium",
    fix(r"\(a\in A\), \(\epsilon(x_i)=0\)", r"\(a\in A\) \(\epsilon(x_i)=0\)"),
    "The enumeration 'avec a ∈ A, ε(x_i) = 0 pour tout i, et ...' lacks its comma (cf. the p. 88 entry); the TeX "
    "silently supplies it. The edit restores the printed reading for the diplomatic layer.",
    corrected=r"\(a\in A\), \(\epsilon(x_i)=0\)")

add(354, "display 'c̃(z) = Σ c̃(a).c̃(γ^{i_1}(x_1))...c̃(γ^{i_k}(x_k))', end",
    "no full stop after the formula (both scans; crops_351_355/p354_ctz.png)",
    r"\widetilde c(\gamma^{i_k}(x_k)).", "punctuation", "high",
    fix(r"\widetilde c(\gamma^{i_k}(x_k)).", r"\widetilde c(\gamma^{i_k}(x_k))"),
    "Full stop added by the transcription at the end of a display.")

# ---------------------------------------------------------------- page 355
add(355, "first display 'c̃(γ^{i_j}(x_j)) = (0,1 + (-1)^{i_j-1}(i_j-1)! γ^{i_j}(x_j)+...)', end",
    "no full stop after the formula (both scans; crops_351_355/p355_disp1.png)",
    r"\gamma^{i_j}(x_j)+\cdots\right).", "punctuation", "high",
    fix(r"\gamma^{i_j}(x_j)+\cdots\right).", r"\gamma^{i_j}(x_j)+\cdots\right)"),
    "Full stop added by the transcription at the end of a display.")

add(355, "proof of Proposition 6.10: 'On peut trouver des éléments z_{α,j} R'",
    "'z_{α,j} R': a z, and no ∈ between it and R (both scans; crops_351_355/p355_ztrouver.png)",
    r"\(z_{\alpha,j}\) \(R\) (printed reading kept)", "misprint_in_print", "high", None,
    "The elements are the x_{α,j} of the display that follows (and of ε(x_{α,j}) = 0), elements of R. Two slips in "
    "one place (z for x, the ∈ left out). The TeX keeps the printed reading; the corrected layer already reads "
    "\\(x_{\\alpha,j}\\in R\\).",
    corrected=r"\(x_{\alpha,j}\in R\)")

add(355, "same sentence: 'et a_α ∈ K tels que :'",
    "no comma after K (both scans)",
    r"\(a_\alpha\in K\), tels que", "punctuation", "high",
    fix(r"\(a_\alpha\in K\), tels", r"\(a_\alpha\in K\) tels"),
    "Comma added by the transcription. Independent of the misprint entry above (fix null).")

add(355, "'engendrée par des générateurs N'_o,X_{α,j} soumis aux relations :'",
    "'N'_o,X_{α,j}': a comma between the two generators, no 'et', no comma before 'soumis' (both scans; "
    "crops_351_355/p355_gen.png)",
    r"\(N'_0\) et \(X_{\alpha,j}\), soumis", "word", "high",
    fix(r"\(N'_0\) et \(X_{\alpha,j}\), soumis", r"\(N'_0\), \(X_{\alpha,j}\) soumis"),
    "The TeX writes 'et' for the printed comma and adds a comma after X_{α,j}.")

# ---------------------------------------------------------------- checks
ok = True
texts = {p: (PAGES / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(351, 356)}
work = dict(texts)
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    p = d["page"]
    t = texts[p]
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, p, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", p, repr(fx["old"]))
    n2 = work[p].count(fx["old"])
    if n2 != 1:
        ok = False
        print("SEQUENTIAL COUNT", n2, p, repr(fx["old"]))
    else:
        work[p] = work[p].replace(fx["old"], fx["new"])
    if d["kind"] == "misprint_in_print" and "corrected" not in d:
        ok = False
        print("NO CORRECTED", p)
for d in F:
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in d:
            ok = False
            print("MISSING KEY", k, d["page"], d["where"][:40])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
print("all checks passed" if ok else "CHECK FAILED")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
    # rendered tails after all fixes, for eyeballing
    for p in range(351, 356):
        pass
