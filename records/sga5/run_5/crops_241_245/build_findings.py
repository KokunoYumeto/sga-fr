"""Build findings_241_245.json and check that every fix's old occurs exactly once in its page_NNN.tex."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
SRC = RUN / "b241_245"
OUT = RUN / "findings_241_245.json"

F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


ST = "Exposé V: the print underlines the statements; \\emph as on pp. 204-230."

# ---------------------------------------------------------------- page 241
add(241, "Corollaire 5.2.5, first word", "'Soit' underlined", "Soit (no underline markup)", "underline", "high",
    r"""Soit
\[""", r"""\emph{Soit}
\[""", ST)

add(241, "Corollaire 5.2.5, 'une suite exacte de Hom(N°,C), avec J^{n+1}Y_n = 0 pour tout n. On suppose que :'",
    "underlined: 'une suite exacte de', Hom (the word only), 'avec', 'pour tout', 'On suppose que'; not (N°,C), the formula, n, the comma, the full stop, the colon",
    "no underline markup; plain \\Hom", "underline", "high",
    r"""une suite exacte de \(\Hom(\mathbb N^\circ,\mathcal C)\), avec \(J^{n+1}Y_n=0\) pour tout \(n\). On suppose que:""",
    r"""\emph{une suite exacte de} \(\uHom(\mathbb N^\circ,\mathcal C)\), \emph{avec} \(J^{n+1}Y_n=0\) \emph{pour tout} \(n\). \emph{On suppose que}:""",
    "\\uHom (\\underline{\\Hom}) as on pp. 205-227.")

add(241, "Corollaire 5.2.5 (i), end of the item",
    "'(resp. artinien et noethérien) ,' ends with a comma; underlined: 'est', 'adique artinien (resp. artinien et noethérien)' (the parentheses inside the underline); not X, AR-J-, the comma",
    "noethérien); (semicolon; no underline markup)", "punctuation", "high",
    r"""\item \(X\) est AR-\(J\)-adique artinien (resp. artinien et noethérien);""",
    r"""\item \(X\) \emph{est} AR-\(J\)-\emph{adique artinien (resp. artinien et noethérien)},""",
    "Semicolon in the TeX for the print's comma. One edit: the punctuation and the statement's underline touch.")

add(241, "Corollaire 5.2.5 (ii)",
    "underlined: 'est', 'adique artinien (resp. noethérien)'; not Z, AR-J-, the full stop",
    "no underline markup", "underline", "high",
    r"""\item \(Z\) est AR-\(J\)-adique artinien (resp. noethérien).""",
    r"""\item \(Z\) \emph{est} AR-\(J\)-\emph{adique artinien (resp. noethérien)}.""", "")

add(241, "Corollaire 5.2.5, last sentence 'Alors Y est AR-J-adique artinien (resp. noethérien) .'",
    "underlined: 'Alors', 'est', 'adique artinien (resp. noethérien)'; not Y, AR-J-, the full stop",
    "no underline markup", "underline", "high",
    r"""Alors \(Y\) est AR-\(J\)-adique artinien (resp. noethérien).""",
    r"""\emph{Alors} \(Y\) \emph{est} AR-\(J\)-\emph{adique artinien (resp. noethérien)}.""", "")

add(241, "heading 5.3", "'5.3. Systèmes projectifs AR-J-adiques noethériens et ∂-foncteurs.' (title underlined, full stop)",
    "\\subsubsection*{5.3. ... -foncteurs} (no full stop)", "punctuation", "high",
    r"""-foncteurs}""", r"""-foncteurs.}""",
    "Underlined title: the print's full stop. The \\delta of this title is the ∂ convention (message), not changed here.")

add(241, "5.3, first sentence 'deux A-catégories abéliennes et F : C -> D'", "abéliennes et F (no comma)",
    "abéliennes, et \\(F", "punctuation", "high",
    r"""abéliennes, et""", r"""abéliennes et""", "The TeX adds a comma.")

add(241, "5.3, display F : Hom(N°,C) -> Hom(N°,D)", "both Hom underlined",
    "\\Hom ... \\Hom", "underline", "high",
    r"""F:\Hom(\mathbb N^\circ,\mathcal C)\longrightarrow\Hom(""",
    r"""F:\uHom(\mathbb N^\circ,\mathcal C)\longrightarrow\uHom(""", "")

add(241, "Proposition 5.3.1, 'Soient C et D deux A-catégories abéliennes et'",
    "underlined: 'Soient', 'et', 'deux', 'catégories abéliennes et'; not C, D, A-",
    "no underline markup", "underline", "high",
    r"""Soient \(\mathcal C\) et \(\mathcal D\) deux \(A\)-catégories abéliennes et
\[""",
    r"""\emph{Soient} \(\mathcal C\) \emph{et} \(\mathcal D\) \emph{deux} \(A\)-\emph{catégories abéliennes et}
\[""", "")

add(241, "Proposition 5.3.1, 'un ∂-foncteur exact' after the display T = (T^i)", "'un' underlined",
    "un (no underline markup)", "underline", "high",
    r"""\]
un \(""", r"""\]
\emph{un} \(""",
    "Kept apart from the next edit so that neither touches the \\delta (∂ convention, message).")

add(241, "Proposition 5.3.1, 'foncteur exact A-linéaire de C dans D . On suppose que :'",
    "underlined: 'foncteur exact', 'linéaire de', 'dans', 'On suppose que'; not ∂-, A-, C, D, the full stop, the colon",
    "no underline markup", "underline", "high",
    r"""-foncteur exact \(A\)-linéaire de \(\mathcal C\) dans \(\mathcal D\). On suppose que:""",
    r"""-\emph{foncteur exact} \(A\)-\emph{linéaire de} \(\mathcal C\) \emph{dans} \(\mathcal D\). \emph{On suppose que}:""", "")

add(241, "Proposition 5.3.1 (i)",
    "'Pour tout objet noethérien M de C annulé par une puissance de J et tout entier n , T^n(M) est noethérien.': no comma after C nor after J; underlined: 'Pour tout objet noethérien', 'de', 'annulé par une puissance de', 'et tout entier', 'est noethérien'",
    "de \\(\\mathcal C\\), annulé par une puissance de \\(J\\), et tout entier (two commas; no underline markup)",
    "punctuation", "high",
    r"""\item Pour tout objet noethérien \(M\) de \(\mathcal C\), annulé par une puissance de \(J\), et tout entier \(n\), \(T^n(M)\) est noethérien.""",
    r"""\item \emph{Pour tout objet noethérien} \(M\) \emph{de} \(\mathcal C\) \emph{annulé par une puissance de} \(J\) \emph{et tout entier} \(n\), \(T^n(M)\) \emph{est noethérien}.""",
    "The TeX adds two commas. One edit with the statement's underline.")

add(241, "Proposition 5.3.1 (ii)",
    "underlined: 'Pour toute', 'algèbre graduée de type fini', 'annulée par', 'et tout', 'module gradué noethérien', 'les', 'modules gradués', 'sont noethériens'; not A-, B, J, (B,C)-, N, (B,D)-, T^n(N)(n ∈ N), the commas, the full stop",
    "no underline markup", "underline", "high",
    r"""\item Pour toute \(A\)-algèbre graduée de type fini \(B\), annulée par \(J\), et tout \((B,\mathcal C)\)-module gradué noethérien \(N\), les \((B,\mathcal D)\)-modules gradués \(T^n(N)\) \((n\in\mathbb N)\) sont noethériens.""",
    r"""\item \emph{Pour toute} \(A\)-\emph{algèbre graduée de type fini} \(B\), \emph{annulée par} \(J\), \emph{et tout} \((B,\mathcal C)\)-\emph{module gradué noethérien} \(N\), \emph{les} \((B,\mathcal D)\)-\emph{modules gradués} \(T^n(N)\) \((n\in\mathbb N)\) \emph{sont noethériens}.""",
    "")

add(241, "Proposition 5.3.1, last sentence 'Alors pour tout objet AR-J-adique noethérien X de Hom(N°,C) , les T^n(X) sont AR-J-adiques noethériens.'",
    "no comma after 'Alors'; underlined: 'Alors pour tout objet', 'adique noethérien', Hom (the word only), 'les', 'sont', 'adiques noethériens'; not AR-J-, X, 'de', (N°,C), T^n(X)",
    "Alors, pour tout objet (comma; no underline markup; plain \\Hom)", "punctuation", "high",
    r"""Alors, pour tout objet AR-\(J\)-adique noethérien \(X\) de \(\Hom(\mathbb N^\circ,\mathcal C)\), les \(T^n(X)\) sont AR-\(J\)-adiques noethériens.""",
    r"""\emph{Alors pour tout objet} AR-\(J\)-\emph{adique noethérien} \(X\) de \(\uHom(\mathbb N^\circ,\mathcal C)\), \emph{les} \(T^n(X)\) \emph{sont} AR-\(J\)-\emph{adiques noethériens}.""",
    "The TeX adds a comma after 'Alors'. One edit with the statement's underline and the underlined Hom.")

# ---------------------------------------------------------------- page 242
add(242, "top of the page",
    "p. 242 begins with 'Preuve : Comme les foncteurs T^n commutent aux translations'; p. 241 ends with 'les T^n(X) sont AR-J-adiques noethériens.'",
    "the folio-242 marker splits the label: '\\begin{prooftext}[' is the last line of page_241.tex, 'Preuve]' the first line of page_242.tex",
    "marker", "high", None, None,
    "Page 242 really begins at '\\begin{prooftext}[' (the line just before the folio-242 marker in both layers). Exact fix: python -I move_marker.py 5 242 '\\begin{prooftext}[' --before (simulated in memory on both layers). Then, on p. 242, replace '\\begin{prooftext}[' + newline + 'Preuve]' by '\\begin{prooftext}[Preuve]': the line break left by the marker insertion puts a space before 'Preuve' (seen in a test compile). Text not moved.")

add(242, "end of the proof of Proposition 5.3.1", "'Le \"lemme d'Artin-Rees\" (4.2.6) permet de conclure.' (in quotation marks)",
    "Le lemme d'Artin-Rees (4.2.6) (no quotation marks)", "punctuation", "high",
    r"""Le lemme d'Artin-Rees""", r"""Le ``lemme d'Artin-Rees''""",
    "The TeX drops the quotation marks; ``...'' is Exposé V's form for the print's straight quotes.")

add(242, "Corollaire 5.3.2, 'Le ∂-foncteur'", "'Le' underlined", "Le (no underline markup)", "underline", "high",
    r"""
Le \(""", r"""
\emph{Le} \(""", "Kept apart from the next edit so that neither touches the \\delta (∂ convention, message).")

add(242, "Corollaire 5.3.2, 'Le ∂-foncteur' before the display", "'foncteur' underlined", "no underline markup",
    "underline", "high",
    r"""-foncteur
\[""", r"""-\emph{foncteur}
\[""", "")

add(242, "Corollaire 5.3.2, display T = (T^i)_{i∈N} : Hom(N°,C) -> Hom(N°,D)", "both Hom underlined",
    "\\Hom ... \\Hom", "underline", "high",
    r"""\Hom(\mathbb N^\circ,\mathcal C)\longrightarrow\Hom(\mathbb N^\circ,\mathcal D)""",
    r"""\uHom(\mathbb N^\circ,\mathcal C)\longrightarrow\uHom(\mathbb N^\circ,\mathcal D)""", "")

add(242, "Corollaire 5.3.2, 'induit un ∂-foncteur'", "'induit un' underlined", "no underline markup",
    "underline", "high",
    r"""induit un \(""", r"""\emph{induit un} \(""", "")

add(242, "Corollaire 5.3.2, 'foncteur exact A-linéaire' before the display E_C -> E_D",
    "underlined: 'foncteur exact', 'linéaire'; not ∂-, A-", "no underline markup", "underline", "high",
    r"""-foncteur exact \(A\)-linéaire
\[""", r"""-\emph{foncteur exact} \(A\)-\emph{linéaire}
\[""", "")

add(242, "Corollaire 5.3.2, 'commutant aux translations, donc par passage au quotient un nouveau'",
    "underlined in one run (through the comma)", "no underline markup", "underline", "high",
    r"""commutant aux translations, donc par passage au quotient un nouveau""",
    r"""\emph{commutant aux translations, donc par passage au quotient un nouveau}""", "")

add(242, "Corollaire 5.3.2, 'foncteur exact A-linéaire, noté encore (T^i)_{i∈N} ,'",
    "underlined: 'foncteur exact', 'linéaire, noté encore' (through the comma); not ∂-, A-, the family, the final comma",
    "no underline markup", "underline", "high",
    r"""-foncteur exact \(A\)-linéaire, noté encore""",
    r"""-\emph{foncteur exact} \(A\)-\emph{linéaire, noté encore}""", "")

# ---------------------------------------------------------------- page 243
add(243, "title of the appendix", "'Appendice : le théorème de SHIH.' (underlined title, full stop)",
    "\\section*{Appendice: le théorème de SHIH} (no full stop)", "punctuation", "high",
    r"""le théorème de SHIH}""", r"""le théorème de SHIH.}""", "Underlined title: the print's full stop.")

add(243, "label 'Terminologie'", "'Terminologie : Soit r_o un entier ...' ('Terminologie' underlined, colon, run into the text)",
    "\\paragraph{Terminologie.} (full stop)", "punctuation", "medium",
    r"""\paragraph{Terminologie.}
Soit""", r"""\emph{Terminologie} : Soit""",
    "As p. 228 (\\paragraph{Exemples.} -> \\emph{Exemples} :). Medium only for the form of the label.")

add(243, "Terminologie, 'pour tout entier r, ≥ r_o ,'", "a clear comma between r and ≥ (crop p243_rcomma.png)",
    "\\(r\\ge r_0\\) (no comma)", "misprint_in_print", "high",
    r"""\(r\ge r_0\)""", r"""\(r,\ge r_0\)""",
    "Stray comma typed after r; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only).",
    corrected=r"""\(r\ge r_0\)""")

add(243, "Terminologie, 'sera appelée dans la suite filtre spectral.'", "'filtre spectral' underlined (defined term), not the full stop",
    "no underline markup", "underline", "high",
    r"""suite filtre spectral.""", r"""suite \emph{filtre spectral}.""", "")

add(243, "heading A.1", "'A.1. Rappels sur les suites spectrales associées aux ∂-foncteurs.' (underlined title, full stop)",
    "\\subsubsection*{A.1. ... -foncteurs} (no full stop)", "punctuation", "high",
    r"""-foncteurs}""", r"""-foncteurs.}""", "Underlined title: the print's full stop.")

add(243, "A.1, 'Pour tout ∂-foncteur exact de C dans une catégorie abélienne D'",
    "'Pour tout ∂ - foncteur exact' / 'de C dans une catégorie abélienne D ,': the functor is not named (crop p243_exact.png)",
    "exact \\(T\\) de", "extra", "high",
    r"""exact \(T\) de""", r"""exact de""",
    "The TeX adds the name T, which the print uses in the display below without introducing it.")

add(243, "A.1, display E(X) : E_1^{pq} = ...", "the name of the spectral sequence is a double-struck E (crop p243_EX.png); the terms E_1^{pq}, E^n are plain",
    "E(X):\\quad (plain E)", "font", "high",
    r"""E(X):\quad""", r"""\mathbb{E}(X):\quad""",
    "The appendix writes the spectral sequence as double-struck E throughout (pp. 243-245), its terms E_r^{pq}, E^n plain.")

# ---------------------------------------------------------------- page 244
add(244, "Fonctorialité, display E(f) : E(X) -> E(Y)", "three double-struck E", "plain E", "font", "high",
    r"""E(f):E(X)\longrightarrow E(Y),""", r"""\mathbb{E}(f):\mathbb{E}(X)\longrightarrow \mathbb{E}(Y),""", "")

add(244, "Fonctorialité, 'u(F^pX) ⊂ F^{p+h}(X) , pour un entier h'", "a comma after the formula",
    "no comma (the formula is set as a display)", "punctuation", "high",
    r"""F^{p+h}(X)
\]""", r"""F^{p+h}(X),
\]""", "The print runs the formula into the text (layout not reported); only the comma is missing.")

add(244, "Fonctorialité, 'E(u) est un endomorphisme'", "double-struck E", "\\(E(u)\\)", "font", "high",
    r"""\(E(u)\)""", r"""\(\mathbb{E}(u)\)""", "")

add(244, "Fonctorialité, 'du filtre spectral associé à E(X)'", "double-struck E", "\\(E(X)\\)", "font", "high",
    r"""associé à \(E(X)\)""", r"""associé à \(\mathbb{E}(X)\)""", "")

add(244, "heading A.2", "'A.2. Cas des systèmes projectifs.' (underlined title, full stop, run into the text)",
    "\\subsubsection*{A.2. Cas des systèmes projectifs} (no full stop)", "punctuation", "high",
    r"""Cas des systèmes projectifs}""", r"""Cas des systèmes projectifs.}""", "Underlined title: the print's full stop.")

add(244, "A.2, display Hom(Z°,C) -> Hom(Z°,D)", "both Hom underlined", "\\Hom ... \\Hom", "underline", "high",
    r"""\Hom(\mathbb Z^\circ,\mathcal C)\longrightarrow \Hom(\mathbb Z^\circ,\mathcal D)""",
    r"""\uHom(\mathbb Z^\circ,\mathcal C)\longrightarrow \uHom(\mathbb Z^\circ,\mathcal D)""", "")

add(244, "A.2, display E(X) = E(X_n)_{n∈Z}", "two double-struck E", "plain E", "font", "high",
    r"""E(X)=E(X_n)_{n\in\mathbb Z},""", r"""\mathbb{E}(X)=\mathbb{E}(X_n)_{n\in\mathbb Z},""", "")

add(244, "A.2, 'où les E(X_n) désignent'", "double-struck E", "\\(E(X_n)\\)", "font", "high",
    r"""où les \(E(X_n)\)""", r"""où les \(\mathbb{E}(X_n)\)""", "")

add(244, "label 'Propriétés de E(X) .'", "double-struck E ('Propriétés de' underlined)", "\\(E(X)\\)", "font", "high",
    r"""Propriétés de \(E(X)\)""", r"""Propriétés de \(\mathbb{E}(X)\)""", "")

add(244, "a), 'dans la suite spectrale E(X) est identique'", "double-struck E", "\\(E(X)\\)", "font", "high",
    r"""spectrale \(E(X)\)""", r"""spectrale \(\mathbb{E}(X)\)""", "The E^n(X) of the same sentence is plain in the print, as in the TeX.")

add(244, "a), 'de système projectif, lorsque X est strict .'", "a comma after 'projectif'",
    "projectif lorsque (no comma)", "punctuation", "high",
    r"""projectif lorsque""", r"""projectif, lorsque""", "")

add(244, "a), 'lorsque X est strict .'", "'strict' underlined, not the full stop", "no underline markup",
    "underline", "high",
    r"""est strict.""", r"""est \emph{strict}.""", "")

add(244, "last line, 'désignant par la lettre F (comme dans A 1 ) la première'",
    "'la première' ends the page; p. 245 begins 'et par la lettre Φ la seconde': the word 'filtration' is not printed (la première ... la seconde refer to the two filtrations of a))",
    "la première filtration et par la", "extra", "high",
    r"""la première filtration""", r"""la première""",
    "The TeX adds 'filtration'. Independent of the folio-245 marker move ('et par la' is not part of this edit).")

# ---------------------------------------------------------------- page 245
add(245, "top of the page",
    "p. 245 begins with 'et par la lettre Φ la seconde, on a pour tout entier α :'; p. 244 ends with '(comme dans A 1 ) la première'",
    "'et par la' ends page_244.tex; the folio-245 marker stands between 'la' and 'lettre'", "marker", "high", None, None,
    "Page 245 really begins at 'et par la' (end of the line before the folio-245 marker, both layers). Exact fix: python -I move_marker.py 5 245 'et par la' --before (simulated in memory on both layers: the marker goes on its own line between 'la première filtration' and 'et par la', no blank line). Text not moved.")

add(245, "display F^pE^n(X)_α = ..., the two cases", "'0 si α ≤ p - 1' and 'Ker (T^n(X_α) -> T^n(X_{p-1})) si α ≥ p-1 .': 'si' before each condition; no commas",
    "0,& \\alpha\\le p-1,\\\\ and ...\\bigr),& \\alpha\\ge p-1. (no 'si'; commas)", "missing", "high",
    r"""0,& \alpha\le p-1,\\
\Ker\bigl(T^n(X_\alpha)\longrightarrow T^n(X_{p-1})\bigr),& \alpha\ge p-1.""",
    r"""0 & \text{si } \alpha\le p-1\\
\Ker\bigl(T^n(X_\alpha)\longrightarrow T^n(X_{p-1})\bigr) & \text{si } \alpha\ge p-1.""",
    "The TeX drops the two 'si' and adds two commas.")

add(245, "a), diagram of the transition morphism after 'le morphisme de transition'",
    "a two-row diagram: E_∞^{pq}(X_β) -> E_∞^{pq}(X_α) above gr^pT^{p+q}(X_β) -> gr^pT^{p+q}(X_α), joined by vertical equal signs (‖) under each term (crop p245_diag.png); no words between the rows; gr has no index T; no comma after the diagram",
    "two displays joined by the words 'qui s'identifie à'; \\gr_T^pT^{p+q}(...) (index T); a comma after the second display",
    "formula", "high",
    r"""\[
E_\infty^{pq}(X_\beta)\longrightarrow E_\infty^{pq}(X_\alpha)
\]
qui s'identifie à
\[
\gr_T^pT^{p+q}(X_\beta)\longrightarrow
\gr_T^pT^{p+q}(X_\alpha),
\]""",
    r"""\[
\begin{tikzcd}
E_\infty^{pq}(X_\beta) \arrow[r] \arrow[d,equal] & E_\infty^{pq}(X_\alpha) \arrow[d,equal]\\
\gr^pT^{p+q}(X_\beta) \arrow[r] & \gr^pT^{p+q}(X_\alpha)
\end{tikzcd}
\]""",
    "The words 'qui s'identifie à' are not in the print (they render its vertical equal signs); the index T of gr is not printed (one T only: gr^p T^{p+q}). \\arrow[d,equal] as at s5.tex folios 178, 201-202. Test-compiled.")

add(245, "a), 'est un monomorphisme, d'après EGA 0_III 13.4.1.3.'", "'monomorphisme' underlined, not the comma",
    "no underline markup", "underline", "high",
    r"""est un monomorphisme""", r"""est un \emph{monomorphisme}""", "")

add(245, "b), the drawing ('cf. le dessin ci-contre')",
    "two vertical lines crossing a horizontal line, no arrowheads on these lines: the left one through the origin, labelled 'o' below left (the typewriter's small o for 0), the right one labelled α below right; a triangle away from the axes, with vertex (p,q) left of the α line: from (p,q) an arrow down labelled 1-r, from its foot an arrow to the right labelled r (crossing the α line), and a plain line from (p,q) to the tip of the r arrow, also crossing the α line (crops p245_fig_top.png, p245_fig_bot.png, p245_fig_o.png)",
    "one vertical axis only, axes with arrowheads; capital O and α both at the origin; the triangle on the axes with the 1-r arrow pointing up from the origin to (p,q) and the hypotenuse drawn as an arrow",
    "formula", "high",
    r"""\draw[->] (-2.0,0) -- (2.2,0);
\draw[->] (0,-1.0) -- (0,1.6);
\node[below left] at (0,0) {$O$};
\node[below] at (0,0) {$\alpha$};
\draw[->] (0,0) -- (0,1.1);
\draw[->] (0,1.1) -- (1.35,0);
\draw[->] (0,0) -- (1.35,0);
\node[above] at (.22,1.1) {$(p,q)$};
\node[left] at (0,0.55) {$1-r$};
\node[above] at (.72,0.08) {$r$};""",
    r"""\draw (-1.27,0) -- (3.81,0);
\draw (0,-0.5) -- (0,2.77);
\draw (1.78,-1.05) -- (1.78,2.5);
\node[below left] at (0,0) {$0$};
\node[below right] at (1.78,0) {$\alpha$};
\draw[->] (1.38,2.22) -- (1.38,1.33);
\draw[->] (1.38,1.33) -- (2.68,1.33);
\draw (1.38,2.22) -- (2.68,1.33);
\node[above] at (1.33,2.22) {$(p,q)$};
\node[left] at (1.38,1.78) {$1-r$};
\node[above] at (2.08,1.33) {$r$};""",
    "Coordinates measured on the scan (1 unit = 100 px at 300 dpi). The origin label is the typewriter's small o; written 0 as the index zeros (o for 0 is handled globally); the TeX's capital O is not the printed letter. Test-compiled.")

add(245, "c), 'on obtient ainsi un filtre spectral ℰ_r^{pq}(X) (p,q ∈ Z ; r ≥ 1) .'",
    "the range in parentheses, with a semicolon: (p,q ∈ Z ; r ≥ 1); no comma before it",
    "\\(\\mathcal E_r^{pq}(X)\\), \\(p,q\\in\\mathbb Z,\\ r\\ge1\\). (commas, no parentheses)", "punctuation", "high",
    r"""\(\mathcal E_r^{pq}(X)\), \(p,q\in\mathbb Z,\ r\ge1\).""",
    r"""\(\mathcal E_r^{pq}(X)\) \((p,q\in\mathbb Z;\ r\ge1)\).""", "")

add(245, "c), last display 'Z_r^{pq}(X) , B_r^{pq}(X) (r < +∞)'",
    "the B is a double-struck B (doubled stem, like the double-struck E of these pages; crop p245_ZB2.png); the Z is a hand-drawn script Z",
    "\\mathcal B_r^{pq}(X)", "font", "medium",
    r"""\mathcal B_r^{pq}(X)""", r"""\mathbb B_r^{pq}(X)""",
    "Medium: the letter is small and partly blotted; its doubled stem matches the typist's double-struck letters, not a script B.")

# ---------------------------------------------------------------- check and write
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    t = (SRC / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"][:80]))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
print(len(F), "findings;", "bad olds:", bad)
for p in range(241, 246):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
