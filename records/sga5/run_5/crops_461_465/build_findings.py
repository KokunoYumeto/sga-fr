"""Build findings_461_465.json and check that every fix's old occurs exactly once in its page_NNN.tex."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
OUT = RUN / "findings_461_465.json"
NL = chr(10)


def page_file(p):
    for d in RUN.glob("b*_*"):
        f = d / f"page_{p:03d}.tex"
        if f.exists():
            return f
    raise FileNotFoundError(p)


items = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    fix = None
    if old is not None:
        fix = {"old": old.replace("⏎", NL), "new": new.replace("⏎", NL)}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    items.append(d)


# ---------------------------------------------------------------- page 461
add(461, "top of the page",
    "The page begins with the line 'fr̄_X = fr_X x id_ē = image réciproque de fr_X par X̄ ⟶ X ,'; page 460 ends with 'constant. Posons :' (checked on page_460_s4).",
    r"page_461.tex begins at 'image réciproque de $\fr_X$ par ...'; the display \[ \overline{\fr}_X=\fr_X\times\id_{\bar e}, \] is the last thing in page_460.tex, after 'Posons'.",
    "marker", "high", None, None,
    r"The folio-461 marker belongs just before the \[ that opens \overline{\fr}_X=\fr_X\times\id_{\bar e}, (the last three lines of page_460.tex). The '=' this display should end with is the next finding, filed under page 460 because its old is in page_460.tex.")

add(460, "first line of printed p. 461 (its TeX still stands under the folio-460 marker: the last display of page_460.tex)",
    "fr̄_X = fr_X x id_ē = image réciproque de fr_X par X̄ ⟶ X ,",
    r"\overline{\fr}_X=\fr_X\times\id_{\bar e}, \] image réciproque de $\fr_X$ ...",
    "punctuation", "high",
    r"\overline{\fr}_X=\fr_X\times\id_{\bar e},",
    r"\overline{\fr}_X=\fr_X\times\id_{\bar e}=",
    "The print equates the formula with its description ('... x id_ē = image réciproque de ...'); the TeX ends the display with a comma. The line is printed on p. 461; old is in page_460.tex (b456_460) until the marker is moved (finding above). As the next two findings.")

add(461, "second formula line, 'f_X = id_X x fr_ē = automorphisme de X̄ ...'",
    "f_X = id_X x fr_ē = automorphisme de X̄ défini par f (par transport de structure)",
    r"f_X=\id_X\times\fr_{\bar e}, \] automorphisme de $\overline X$ ...",
    "punctuation", "high",
    r"\id_X\times\fr_{\bar e},",
    r"\id_X\times\fr_{\bar e}=",
    "The print has '=' between the formula and its description; the TeX has a comma. (The print's text inside the display line, set as running text in the TeX, is layout and not reported.)")

add(461, "same line, end",
    "défini par f (par transport de structure)   [nothing follows; the next formula line begins]",
    "défini par $f$ par transport de structure, et",
    "punctuation", "high",
    "par $f$ par transport de structure, et",
    "par $f$ (par transport de structure)",
    "The TeX drops the print's parentheses and adds ', et', which the print does not have.")

add(461, "third formula line, 'Fr̄*_{F/X} = ... = image réciproque de ...'",
    "Fr̄*_{F/X} = Fr*_{F/X} ⊗ id_{Λ_ē} = image réciproque de Fr*_{F/X} par X̄ ⟶ X .",
    r"\overline{\Fr}^*_{F/X}=\Fr^*_{F/X}\otimes\id_{\Lambda_{\bar e}}, \] image réciproque de ...",
    "punctuation", "high",
    r"\otimes\id_{\Lambda_{\bar e}},",
    r"\otimes\id_{\Lambda_{\bar e}}=",
    "As the f_X line: '=' in the print, a comma in the TeX.")

add(461, "'On peut écrire :' display, the second fr",
    "fr_X̄ = fr̄_X∘f_X = f_X∘fr_X   (no bar over the second fr; the bar over the first is clear)",
    r"f_X\circ\overline{\fr}_X",
    "misprint_in_print", "medium",
    r"f_X\circ\overline{\fr}_X",
    r"f_X\circ\fr_X",
    "Checked at 5x: no trace of a bar over the fr of f_X∘fr_X, while the bar over fr̄_X∘f_X just before it is plainly typed. The bar is required (fr̄_X and f_X are the two commuting automorphisms of X̄; fr_X lives on X). The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"f_X\circ\overline{\fr}_X")

add(461, "'On peut écrire :' display, between the two formulas",
    "... = f_X∘fr_X  et  Fr*_{F̄/X̄} = Fr̄*_{F/X} .",
    r"f_X\circ\overline{\fr}_X, \qquad \Fr^*_{\overline F/\overline X}=...",
    "word", "high",
    r",⏎\qquad⏎\Fr^*",
    r"\quad\text{et}\quad⏎\Fr^*",
    "The print joins the two formulas with 'et'; the TeX has a comma and \\qquad. Independent of the misprint finding just before (the olds touch but do not overlap).")

add(461, "'Le corollaire de la proposition 3 montre que l'endomorphisme de RΓ_X̄(F̄)'",
    "R Γ_X̄(F̄) défini par le couple   (plain typed R, no double underline; checked on a crop)",
    r"$\RGamma_{\overline X}(\overline F)$ (\RGamma = \mathbb{R}\Gamma)",
    "font", "high",
    r"$\RGamma_{\overline X}(\overline F)$ défini",
    r"$\mathrm{R}\Gamma_{\overline X}(\overline F)$ défini",
    "Only this first RΓ of the page has a plain R; the two later ones (fr_{RΓ_X̄(F̄)} and 'l'automorphisme de RΓ_X̄(F̄)') have the double-underlined R that \\RGamma gives, and stay.")

add(461, "'la correspondance de Frobenius géométrique'",
    "géométrique (underlined)", "géométrique (no markup)",
    "underline", "high",
    "Frobenius géométrique",
    r"Frobenius \emph{géométrique}",
    "Underlined in the print. Exposé XV of the TeX has no underline markup; \\emph as itemized for Exposés III B and V.")

add(461, "'l'opération de Frobenius arithmétique'",
    "arithmétique (underlined)", "arithmétique (no markup)",
    "underline", "high",
    "Frobenius arithmétique",
    r"Frobenius \emph{arithmétique}",
    "Underlined in the print.")

add(461, "heading § 3",
    "§ 3. LA FONCTION L .   (capitals, underlined)",
    r"\subsection*{§ 3. La fonction $L$}",
    "word", "high",
    "La fonction",
    "LA FONCTION",
    "The print sets the § headings of Exposé XV in capitals (also '§ 1. MORPHISME DE FROBENIUS', p. 442, and '§ 2. CORRESPONDANCE DE FROBENIUS.', p. 452); the TeX writes all three in small letters.")

add(461, "heading § 3, end",
    "§ 3. LA FONCTION L .", r"\subsection*{§ 3. La fonction $L$}",
    "punctuation", "high",
    "$L$}",
    "$L$.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")

add(461, "heading n°1",
    "n°1. Définition.   (underlined)", r"\subsubsection*{n\textsuperscript{o} 1. Définition}",
    "punctuation", "high",
    "1. Définition}",
    "1. Définition.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")

# ---------------------------------------------------------------- page 462
add(462, "'l'élément de Frobenius f : λ ⇝ λ^p (λ ∈ F̄_p) ,'",
    "f : λ ⇝ λ^p   (hand-drawn wavy arrow; checked on a crop)",
    r"f: \lambda\longmapsto \lambda^p",
    "symbol", "high",
    r"\lambda\longmapsto \lambda^p",
    r"\lambda\rightsquigarrow \lambda^p",
    "The print draws a wavy arrow, not a maps-to arrow; \\rightsquigarrow (amssymb) is used elsewhere in s5.tex.")

add(462, "'l'image directe g(F) est de même définie par sa fibre'",
    "l'image directe g(F)   (no lower star; checked on a crop)",
    "l'image directe $g(F)$",
    "misprint_in_print", "high",
    None, None,
    "The direct image is g_*(F), as in the rest of the paragraph. The TeX keeps the printed reading; the corrected layer (current/s5.tex) already reads $g_*(F)$.",
    corrected="$g_*(F)$")

add(462, "'sa fibre g_*(F)_ē munie des opérations de π_e'",
    "g_*(F)_ē", "$(g_*F)_{\\bar e}$",
    "formula", "high",
    r"sa fibre $(g_*F)_{\bar e}$",
    r"sa fibre $g_*(F)_{\bar e}$",
    "The print writes g_*(F)_ē (parentheses around F only); the TeX regroups as (g_*F)_ē. Same in the next two findings.")

add(462, "'module induit' formula",
    "g_*(F)_ē ≃ F_x̄ ⊗_{π_x} π_e .", r"(g_*F)_{\bar e}\simeq F_{\bar x}\otimes_{\pi_x}\pi_e.",
    "formula", "high",
    r"(g_*F)_{\bar e}\simeq",
    r"g_*(F)_{\bar e}\simeq",
    "As the previous finding.")

add(462, "display 'L_F(t) = L_{g_*(F)}(t) = ...'",
    "L_F(t) = L_{g_*(F)}(t) = 1/det(1-f^{-1}_{g_*(F)_ē} t) ;",
    r"L_F(t)=L_{g_*F}(t)=1/\det(1-f^{-1}_{(g_*F)_{\bar e}}t);",
    "formula", "high",
    r"L_{g_*F}(t)=1/\det(1-f^{-1}_{(g_*F)_{\bar e}}t)",
    r"L_{g_*(F)}(t)=1/\det(1-f^{-1}_{g_*(F)_{\bar e}}t)",
    "Two places in the display: L_{g_*(F)} and the index g_*(F)_ē, as printed.")

# ---------------------------------------------------------------- page 463
add(463, "top of the page",
    "The page begins with the word 'à' on a line of its own, then the display L_F(t) = 1/det(1-f^{-d}_{F_x̄} t^d) . (page 462 ends with 'cette expression est égale')",
    "page_462.tex ends with 'montre que cette expression est égale à'; page_463.tex begins at the display",
    "marker", "high", None, None,
    "The folio-463 marker belongs between 'égale' and 'à' (last line of page_462.tex).")

add(463, "'l'ensemble des points fermés de X'",
    "fermés (underlined)", "fermés (no markup)",
    "underline", "high",
    "points fermés de",
    r"points \emph{fermés} de",
    "Underlined in the print.")

add(463, "'multipliable dans Ω[[t]] ; explicitons-le en effet'",
    "Ω[[t]] ; explicitons-le en effet,en introduisant",
    r"$\Omega[[t]]$. Explicitons-le en effet,",
    "punctuation", "high",
    r"$\Omega[[t]]$. Explicitons-le",
    r"$\Omega[[t]]$; explicitons-le",
    "The print has a semicolon and a small e; the TeX starts a new sentence.")

add(463, "after the display d(x) = [k(x) : F_p]",
    "d(x) = [k(x) : F_p] (degré de x) ;   avec ces notations",
    "(degré de $x$). Avec ces notations",
    "punctuation", "high",
    "(degré de $x$). Avec ces notations",
    "(degré de $x$); avec ces notations",
    "The print has a semicolon and a small a; the TeX has a full stop and a capital.")

add(463, "display 'Ainsi la fonction L de (X,F) est'",
    "L_F(t) = ∏_{x∈X°} (1/det(1-f^{-d(x)}_{F_x̄} t^{d(x)})   (two opening parentheses, one closing; checked on a crop)",
    r"L_F(t)=\prod_{x\in X^0}1/\det(1-f_{F_{\bar x}}^{-d(x)}t^{d(x)}).",
    "misprint_in_print", "high",
    r"\prod_{x\in X^0}1/\det",
    r"\prod_{x\in X^0}(1/\det",
    "The print opens a parenthesis before 1/det that it never closes. The TeX silently drops it; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"\prod_{x\in X^0}1/\det(1-f_{F_{\bar x}}^{-d(x)}t^{d(x)})")

add(463, "Proposition 1 a)",
    "a) (multiplicativité en F) Soit 0 ⟶ F' ⟶ F ⟶ F'' ⟶ 0",
    r"\item Multiplicativité en $F$. Soit",
    "punctuation", "high",
    r"\item Multiplicativité en $F$.",
    r"\item (multiplicativité en $F$)",
    "The print puts the item's title in parentheses, with a small m and no full stop.")

add(463, "Proposition 1 a), 'Soit'",
    "Soit (underlined)", "Soit (no markup)",
    "underline", "high",
    r"Soit⏎\[",
    r"\emph{Soit}⏎\[",
    "The print underlines the statement's words (Proposition 1 runs on p. 464).")

# ---------------------------------------------------------------- page 464
add(464, "Proposition 1 a), end of the statement (first lines of the page)",
    "une suite exacte de Ω-faisceaux constructibles sur X , alors on a   (underlined: 'une suite exacte de', 'faisceaux constructibles sur', 'alors on a')",
    "no underline markup",
    "underline", "high",
    "une⏎suite exacte de $\\Omega$-faisceaux constructibles sur $X$, alors on a",
    "\\emph{une⏎suite exacte de} $\\Omega$-\\emph{faisceaux constructibles sur} $X$, \\emph{alors on a}",
    "Underlined statement, word group by word group (math not underlined).")

add(464, "Proposition 1 a), formula",
    "L_F = L_{F'}.L_{F''} .   (typed product dot)",
    "L_F=L_{F'}L_{F''}.",
    "symbol", "high",
    "L_{F'}L_{F''}",
    r"L_{F'}\cdot L_{F''}",
    "The TeX drops the print's product dot (a typed full stop, written \\cdot in this file, e.g. p\\cdot 1 on p. 442).")

add(464, "Proposition 1 b), first sentence",
    "Soient Y un sous-schéma fermé de X et U = X-Y l'ouvert complémentaire.   (underlined: 'Soient', 'un sous-schéma fermé de', 'et', 'l'ouvert complémentaire')",
    "no underline markup",
    "underline", "high",
    "Soient $Y$ un sous-schéma fermé de $X$ et $U=X-Y$ l'ouvert complémentaire.",
    r"\emph{Soient} $Y$ \emph{un sous-schéma fermé de} $X$ \emph{et} $U=X-Y$ \emph{l'ouvert complémentaire}.",
    "Underlined statement.")

add(464, "Proposition 1 b), 'Alors on a'",
    "Alors on a (underlined)", "Alors on a",
    "underline", "high",
    "Alors on a",
    r"\emph{Alors on a}",
    "Underlined statement. Independent of the colon and dot findings that follow (the olds do not overlap).")

add(464, "Proposition 1 b), before the formula",
    "Alors on a : L_F = L_{F|U}.L_{F|Y}",
    r"Alors on a \[ L_F=L_{F|U}\,L_{F|Y} \]",
    "punctuation", "high",
    r"⏎\[⏎L_F=L_{F|U}",
    r" :⏎\[⏎L_F=L_{F|U}",
    "The TeX drops the colon after 'on a'.")

add(464, "Proposition 1 b), formula",
    "L_{F|U}.L_{F|Y}   (typed product dot)",
    r"L_{F|U}\,L_{F|Y}",
    "symbol", "high",
    r"\,L_{F|Y}",
    r"\cdot L_{F|Y}",
    "The print has a product dot; the TeX a thin space.")

add(464, "Proposition 1 b), after the formula",
    "pour tout Ω-faisceau constructible F .   (underlined: 'pour tout', 'faisceau', 'constructible')",
    "no underline markup",
    "underline", "high",
    "pour tout $\\Omega$-faisceau constructible $F$.",
    "\\emph{pour tout} $\\Omega$-\\emph{faisceau constructible} $F$.",
    "Underlined statement.")

add(464, "Proposition 1 c)",
    "Soit X ⟶ S un morphisme de schémas de type fini sur F_p , et soit F un Ω-faisceau constructible sur X ; alors   (underlined: 'Soit', 'un morphisme de schémas de type fini sur', 'et soit', 'un', 'faisceau constructible sur', 'alors')",
    "no underline markup",
    "underline", "high",
    "Soit $X\\to S$ un morphisme de schémas de type fini sur $\\mathbb F_p$, et soit $F$ un $\\Omega$-faisceau constructible sur $X$; alors",
    "\\emph{Soit} $X\\to S$ \\emph{un morphisme de schémas de type fini sur} $\\mathbb F_p$, \\emph{et soit} $F$ \\emph{un} $\\Omega$-\\emph{faisceau constructible sur} $X$; \\emph{alors}",
    "Underlined statement.")

add(464, "proof of Proposition 1, last sentence",
    "par un morphisme de préschémas de type fini sur F_p   ('de type fini' underlined)",
    "de type fini (no markup)",
    "underline", "high",
    "préschémas de type fini sur",
    r"préschémas \emph{de type fini} sur",
    "Underlined in the print.")

add(464, "heading n°2",
    "n°2. Enoncé du théorème de rationalité et réduction au cas d'une courbe.   (underlined, final full stop)",
    r"\subsubsection*{n\textsuperscript{o} 2. Énoncé du théorème de rationalité et réduction au cas d'une courbe}",
    "punctuation", "high",
    "au cas d'une courbe}",
    "au cas d'une courbe.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")

add(464, "Théorème, statement",
    "Soient X un schéma de type fini sur F_p , de dimension n , g : X ⟶ e son morphisme structural, et F un Ω-faisceau constructible sur X . On a   (underlined: 'Soient', 'un schéma de type fini sur', 'de dimension', 'son morphisme structural', 'et', 'un', 'faisceau', 'constructible sur', 'On a')",
    "no underline markup",
    "underline", "high",
    "Soient $X$ un schéma de type fini sur $\\mathbb F_p$, de dimension $n$, $g:X\\to e$ son morphisme structural, et $F$ un $\\Omega$-faisceau constructible sur $X$. On a",
    "\\emph{Soient} $X$ \\emph{un schéma de type fini sur} $\\mathbb F_p$, \\emph{de dimension} $n$, $g:X\\to e$ \\emph{son morphisme structural}, \\emph{et} $F$ \\emph{un} $\\Omega$-\\emph{faisceau constructible sur} $X$. \\emph{On a}",
    "Underlined statement.")

add(464, "Théorème, formula (1)",
    "(L_{R^i_! g(F)})^{(-1)^i}   (plain typed R; checked on a crop)",
    r"L_{\R^i_!g(F)} (\R = \mathbb{R})",
    "font", "high",
    r"L_{\R^i_!g(F)}\bigr)",
    r"L_{\mathrm{R}^i_!g(F)}\bigr)",
    "The R of R^i_! is a plain typed R on pp. 464-466 (no double underline); \\R is double-struck.")

add(464, "'Dans cet énoncé les R^i_! g(F)'",
    "R^i_! g(F)   (plain R)", r"$\R^i_!g(F)$",
    "font", "high",
    r"les $\R^i_!g(F)$",
    r"les $\mathrm{R}^i_!g(F)$",
    "As formula (1).")

add(464, "'On pose H^i_!(X̄,F̄) = R^i_! ḡ(F̄) = R^i_! g(F)_ē'",
    "R^i_! ḡ(F̄) = R^i_! g(F)_ē   (both R plain)",
    r"\R^i_!\bar g(\bar F)=\R^i_!g(F)_{\bar e}",
    "font", "high",
    r"\R^i_!\bar g(\bar F)=\R^i_!g(F)_{\bar e}",
    r"\mathrm{R}^i_!\bar g(\bar F)=\mathrm{R}^i_!g(F)_{\bar e}",
    "Two places, as formula (1).")

# ---------------------------------------------------------------- page 465
add(465, "top of the page",
    "The page begins 'X̄ , F̄ et ḡ proviennent de X , F et g ...'; page 464 ends with '(théorème du changement de base), où'",
    r"page_464.tex ends with 'où $\bar X$, $\bar F$ et $\bar g$'; page_465.tex begins at 'proviennent'",
    "marker", "high", None, None,
    r"The folio-465 marker belongs between 'où' and '$\bar X$' (last line of page_464.tex).")

add(465, "first display, 'on a d'après le n°1 :'",
    "L_{R^i_! g(F)}(t) = ...   (plain R; checked on a crop)",
    r"L_{\R^i_!g(F)}(t)",
    "font", "high",
    r"L_{\R^i_!g(F)}(t)",
    r"L_{\mathrm{R}^i_!g(F)}(t)",
    "As on p. 464.")

add(465, "display (P_{F,u})",
    "(P_{F,u}) : L_F = ∏_i (L_{R^i_! u(F)})^{(-1)^i} .   (plain R)",
    r"L_{\R^i_!u(F)}",
    "font", "high",
    r"L_{\R^i_!u(F)}",
    r"L_{\mathrm{R}^i_!u(F)}",
    "As on p. 464.")

add(465, "Lemme 1, statement",
    "Soient u : X ⟶ Y un morphisme de schémas de type fini sur F_p et F un Ω-faisceau constructible. Si (P_{F|X_y,u_y}) est vraie pour tout y ∈ Y° , alors (P_{F,u}) est vraie.   (underlined: 'Soient', 'un morphisme de schémas de type fini sur', 'et', 'un', 'faisceau constructible', 'Si', 'est vraie pour tout', 'alors', 'est vraie')",
    "no underline markup",
    "underline", "high",
    "Soient $u:X\\to Y$ un morphisme de schémas de type fini sur $\\mathbb F_p$ et $F$ un $\\Omega$-faisceau constructible. Si $(P_{F|X_y,u_y})$ est vraie pour tout $y\\in Y^0$, alors $(P_{F,u})$ est vraie.",
    "\\emph{Soient} $u:X\\to Y$ \\emph{un morphisme de schémas de type fini sur} $\\mathbb F_p$ \\emph{et} $F$ \\emph{un} $\\Omega$-\\emph{faisceau constructible}. \\emph{Si} $(P_{F|X_y,u_y})$ \\emph{est vraie pour tout} $y\\in Y^0$, \\emph{alors} $(P_{F,u})$ \\emph{est vraie}.",
    "Underlined statement.")

add(465, "proof of Lemme 1, 'En effet'",
    "En effet   (no comma)", "En effet,",
    "punctuation", "high",
    "En effet,",
    "En effet",
    "The TeX adds a comma.")

add(465, "proof of Lemme 1, second line of the computation",
    "(L_{R^i_! u_y(F|X_y)})^{(-1)^i}   (plain R)",
    r"L_{\R^i_!u_y(F|X_y)}",
    "font", "high",
    r"L_{\R^i_!u_y(F|X_y)}",
    r"L_{\mathrm{R}^i_!u_y(F|X_y)}",
    "As on p. 464.")

add(465, "'or R^i_! u_y(F|X_y) ≃ R^i_! u(F)_y'",
    "R^i_! u_y(F|X_y) ≃ R^i_! u(F)_y   (both R plain)",
    r"\R^i_!u_y(F|X_y)\simeq \R^i_!u(F)_y",
    "font", "high",
    r"\R^i_!u_y(F|X_y)\simeq \R^i_!u(F)_y",
    r"\mathrm{R}^i_!u_y(F|X_y)\simeq \mathrm{R}^i_!u(F)_y",
    "Two places, as on p. 464.")

add(465, "end of the page",
    "The page ends with '(théorème du changement de base), ce qui'; p. 466 begins with 'donne :' (checked on page_466_s1)",
    "page_465.tex ends with '(théorème du changement de base), ce qui donne'",
    "marker", "high", None, None,
    "The folio-466 marker belongs between 'ce qui' and 'donne' (last line of page_465.tex).")

add(465, "last word under the folio-465 marker ('ce qui donne'), printed at the top of p. 466",
    "donne :   (colon, then the display)",
    "ce qui donne",
    "punctuation", "high",
    "ce qui donne",
    "ce qui donne :",
    "The colon is printed at the top of p. 466; the word stands under the folio-465 marker until that marker is moved (finding above).")

# ---------------------------------------------------------------- checks
bad = 0
for x in items:
    fx = x["fix"]
    if not fx:
        continue
    t = page_file(x["page"]).read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        bad += 1
        print("PROBLEM", x["page"], n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO-OP", x["page"], repr(fx["old"]))
    for ch in fx["old"] + fx["new"]:
        if ord(ch) < 32 and ch != NL:
            bad += 1
            print("CONTROL CHAR", x["page"], repr(fx["old"]))
            break
print("findings:", len(items), "problems:", bad)
counts = {}
for x in items:
    k = "mis" if x["kind"] == "misprint_in_print" else "norm"
    counts.setdefault(x["page"], {"norm": 0, "mis": 0})[k] += 1
print(counts)
if not bad:
    OUT.write_text(json.dumps(items, ensure_ascii=False, indent=1) + NL, encoding="utf-8", newline=NL)
    print("written", OUT)
