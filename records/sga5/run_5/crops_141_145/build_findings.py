"""Build findings_141_145.json and check every fix: exactly one occurrence in the batch's page_NNN.tex (snapshot) and
in the live page span of both layers; then apply all fixes in order, in memory only, to the live spans."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, pages  # noqa: E402

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
OUT = RUN / "findings_141_145.json"

ENV = ("The III B statement environment (\\renewenvironment{statement} of III B, s5.tex line 4329 at 20:17: "
       "\\textbf{#1.}) appends a full stop the print does not have: with this edit the label renders '{L} -.' until "
       "III B takes Exposé III's environment (\\textbf{#1}), as in the message.")
EMPH = "\\emph is the file's command for the print's underline in Exposé III, whose typescript III B continues"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if fix is None else dict(old=fix[0], new=fix[1]))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 141
add(141, "top of the page: 'i.e. pour tout E ∈ ob D_ctf(X) (resp. D_ctf(Y)) , on a E ⥲ D_XD_XE'",
    "'(resp. D_ctf(Y))': the parenthesis has no 'E ∈ ob'",
    r"(resp. $E\in\ob D_{\ctf}(Y)$)",
    "extra", "high",
    (r"(resp. $E\in\ob D_{\ctf}(Y)$)", r"(resp. $D_{\ctf}(Y)$)"),
    "Printed at the top of p. 141. In the batch's page files this text still stood at the end of page_140.tex; in "
    "the live s5.tex the folio-141 marker has been moved (batch 136-140), so the 'old' is checked against the live "
    "page 141 (once in each layer), not against page_141.tex. The rest of the moved text agrees with the print.")

add(141, "top of the page",
    "p. 141 begins 'D_ctf(X) (resp. D_ctf(Y)) est dualisant, i.e. pour tout E ∈ ob D_ctf(X) ... On écrira parfois "
    "D au'; p. 140 ends '(resp. D_Y = RHom(-,K_Y)) sur'",
    "in the batch's files page_141.tex begins 'lieu de $D_X$, $D_Y$.' and the first lines of p. 141 end "
    "page_140.tex",
    "marker", "high", None,
    "Page 141 really begins at '$D_{\\ctf}(X)$ (resp. $D_{\\ctf}(Y)$) est dualisant'. Already done: the live s5.tex "
    "(20:12) has the folio-141 marker just before that anchor in both layers (move of the batch 136-140 report). "
    "Nothing to do.")

add(141, "'On écrira parfois D au lieu de D_X , D_Y . Notons d'autre part p_i^! le foncteur p_i^*(-)(1)[2] .'",
    "one paragraph: 'Notons d'autre part' follows 'lieu de D_X , D_Y .' in the same line",
    "a blank line before 'Notons d'autre part' (new paragraph)",
    "other", "high",
    ("$D_Y$.\n\nNotons", "$D_Y$. Notons"),
    "Paragraph break added by the TeX.")

add(141, "'On a trivialement K_X ⊗ M ⥲ p_2^!M , L ⊗ K_Y ⥲ p_1^!L , et il découle de (III 2.3) ,'",
    "the two isomorphisms run in the text line that begins 'vialement' ('tri-vialement'), a comma after each; "
    "each ⊗ has a plain typed L standing above it and S as subscript",
    "a display \\[ ... ,\\qquad ... , \\] between 'trivialement' and 'et il découle', the tensors written "
    "\\otimes_S^{\\LL} (bold L set beside the sign)",
    "other", "high",
    ("trivialement\n\\[\nK_X\\otimes_S^{\\LL}M\\xrightarrow{\\sim}p_2^!M,\n\\qquad\n"
     "L\\otimes_S^{\\LL}K_Y\\xrightarrow{\\sim}p_1^!L,\n\\]\net il",
     "trivialement $K_X\\lten_SM\\xrightarrow{\\sim}p_2^!M$, $L\\lten_SK_Y\\xrightarrow{\\sim}p_1^!L$, et il"),
    "Display against inline formula (as the logged fixes of pp. 44, 120-124 and 140). The same edit writes the two "
    "tensors with the file's \\lten (\\overset{\\mathrm L}{\\otimes}), as the next findings: one edit, so that no "
    "two edits overlap.")

TENS = ("p. 141 writes its 14 derived tensors \\otimes_S^{\\LL} / \\otimes^{\\LL} (\\LL = \\mathbf L, set beside "
        "the sign); everywhere else Exposé III B has the file's \\lten = \\overset{\\mathrm L}{\\otimes} (347 times), "
        "which is the print's form. Two of the 14 are in the display edit above.")
add(141, "the Künneth arrows 'DL ⊗_S M ⟶ RHom(p_1^*L,p_2^!M) , L ⊗_S DM ⟶ RHom(p_2^*M,p_1^!L)'",
    "a plain typed L standing above each ⊗, S as subscript", "\\otimes_S^{\\LL} (bold L beside the sign), twice",
    "font", "high",
    ("DL\\otimes_S^{\\LL}M\\longrightarrow \\uRHom(p_1^*L,p_2^!M),\n\\qquad\nL\\otimes_S^{\\LL}DM",
     "DL\\lten_SM\\longrightarrow \\uRHom(p_1^*L,p_2^!M),\n\\qquad\nL\\lten_SDM"),
    TENS)
add(141, "(*) 'Hom(a_1^*L,a_2^!M) ⥲ H^o(X x_S Y , a_*a^!(DL ⊗_S M))'",
    "a plain typed L above the ⊗", "\\otimes_S^{\\LL}", "font", "high",
    ("a_*a^!(DL\\otimes_S^{\\LL}M)", "a_*a^!(DL\\lten_SM)"), "As the Künneth arrows.")
add(141, "(**) 'Hom(b_2^*M,b_1^!L) ⥲ H^o(X x_S Y, b_*b^!(L ⊗_S DM))'",
    "a plain typed L above the ⊗", "\\otimes_S^{\\LL}", "font", "high",
    ("b_*b^!(L\\otimes_S^{\\LL}DM)", "b_*b^!(L\\lten_SDM)"), "As the Künneth arrows.")
add(141, "the pairing '(DL ⊗_S M) ⊗ (L ⊗_S DM) ⟶ K_X ⊗_S K_Y = Λ_{X x_S Y}(2) [4] =dfn K_{X x_S Y} .'",
    "a plain typed L above each of the four ⊗ (the middle one without S)",
    "\\otimes_S^{\\LL} three times, \\otimes^{\\LL} once", "font", "high",
    ("(DL\\otimes_S^{\\LL}M)\\otimes^{\\LL}(L\\otimes_S^{\\LL}DM)\n\\longrightarrow K_X\\otimes_S^{\\LL}K_Y",
     "(DL\\lten_SM)\\lten(L\\lten_SDM)\n\\longrightarrow K_X\\lten_SK_Y"),
    "As the Künneth arrows.")
add(141, "'a_*a^!P ⊗ b_*b^!Q ⟶ c_*c^!(P ⊗ Q) ,' (analogue of III 4.2.3)",
    "a plain typed L above both ⊗", "\\otimes^{\\LL} twice", "font", "high",
    ("a_*a^!P\\otimes^{\\LL} b_*b^!Q\\longrightarrow c_*c^!(P\\otimes^{\\LL}Q)",
     "a_*a^!P\\lten b_*b^!Q\\longrightarrow c_*c^!(P\\lten Q)"),
    "As the Künneth arrows.")
add(141, "'où P = DL ⊗_S M , Q = L ⊗_S DM ,'",
    "a plain typed L above both ⊗", "\\otimes_S^{\\LL} twice", "font", "high",
    ("$P=DL\\otimes_S^{\\LL}M$, $Q=L\\otimes_S^{\\LL}DM$", "$P=DL\\lten_SM$, $Q=L\\lten_SDM$"),
    "As the Künneth arrows; with this one all 14 \\LL tensors of III B are replaced.")

# ---------------------------------------------------------------- p. 142
add(142, "1.1.3, 'A' (resp. B') une S-courbe séparée, a' : A' ⟶ X' x_S Y' , b' : B' ⟶ X' x_S Y' des S-morphismes finis'",
    "the two morphisms run in the text line that begins 'séparée,'; a comma between them, none after",
    "a display \\[ ... ,\\qquad ... \\] between 'séparée,' and 'des $S$-morphismes'",
    "other", "high",
    ("séparée,\n\\[\na':A'\\longrightarrow X'\\times_S Y',\n\\qquad\nb':B'\\longrightarrow X'\\times_S Y'\n\\]\ndes",
     "séparée, $a':A'\\longrightarrow X'\\times_S Y'$, $b':B'\\longrightarrow X'\\times_S Y'$ des"),
    "Display against inline formula (as the same maps of 1.1 on p. 140).")
add(142, "1.1.3, 'L' ∈ ob D_ctf(X') , M' ∈ ob D_ctf(Y') , u' ∈ Hom(a'^*_1L',a'^!_2M') , v' ∈ Hom(b'^*_2M',b'^!_1L') .'",
    "a text line from the left margin, after '... soit quasi-fini en s' (resp. t') ,', ending with a full stop; "
    "'On peut alors considérer' begins the next line",
    "a display \\[ ...,\\quad ...,\\quad ...,\\quad ... . \\]",
    "other", "high",
    ("(resp. $t'$),\n\\[\nL'\\in\\ob D_{\\ctf}(X'),\\quad M'\\in\\ob D_{\\ctf}(Y'),\\quad\n"
     "u'\\in\\Hom(a_1'^*L',a_2'^!M'),\\quad v'\\in\\Hom(b_2'^*M',b_1'^!L').\n\\]\nOn peut",
     "(resp. $t'$), $L'\\in\\ob D_{\\ctf}(X')$, $M'\\in\\ob D_{\\ctf}(Y')$, $u'\\in\\Hom(a_1'^*L',a_2'^!M')$, "
     "$v'\\in\\Hom(b_2'^*M',b_1'^!L')$. On peut"),
    "Display against inline formula; the commas and the final full stop stand as printed.")
add(142, "label of Théorème 1.2",
    "'Théorème 1.2 - Sous les hypothèses ...': 'Théorème' underlined, the number, a typewriter dash, the statement "
    "run in", "\\begin{statement}{Théorème 1.2} (prints 'Théorème 1.2.')",
    "punctuation", "high",
    ("\\begin{statement}{Théorème 1.2}", "\\begin{statement}{Théorème 1.2 -}"),
    "Exposé III's label form (as pp. 93-102). " + ENV.replace("{L}", "Théorème 1.2"))
add(142, "statement of Théorème 1.2",
    "underlined: 'Sous les hypothèses du début de' | 'on suppose de plus que' | 'et' | 'sont en position générale' | "
    "'i.e. que l'intersection des cônes tangents en' | 'aux' + 'images de' (across the line break) | 'et' | 'dans' | "
    "'est réduite à' | 'et que de même' | 'et' | 'sont en position générale' | 'ainsi que' | 'et' | 'Alors on a'; "
    "not underlined: 1.1, A, B, (x,y), X x_S Y, X x {y}, {x} x Y, the commas, the full stop, the colon",
    "no underline", "underline", "high",
    ("Sous les hypothèses du début de 1.1, on suppose de plus que $A$ et $B$ sont en position générale, i.e. que "
     "l'intersection des cônes tangents en $(x,y)$ aux images de $A$ et $B$ dans $X\\times_S Y$ est réduite à $(x,y)$, "
     "et que de même $A$ et $X\\times\\{y\\}$ sont en position générale, ainsi que $\\{x\\}\\times Y$ et $B$. Alors on a",
     "\\emph{Sous les hypothèses du début de} 1.1, \\emph{on suppose de plus que} $A$ \\emph{et} $B$ \\emph{sont en "
     "position générale}, \\emph{i.e. que l'intersection des cônes tangents en} $(x,y)$ \\emph{aux images de} $A$ "
     "\\emph{et} $B$ \\emph{dans} $X\\times_S Y$ \\emph{est réduite à} $(x,y)$, \\emph{et que de même} $A$ \\emph{et} "
     "$X\\times\\{y\\}$ \\emph{sont en position générale}, \\emph{ainsi que} $\\{x\\}\\times Y$ \\emph{et} $B$. "
     "\\emph{Alors on a}"),
    "Underlined statement, as the statements of Exposé III (pp. 79-84); " + EMPH + " (no underline command in III B "
    "yet). Independent of the colon edit below.")
add(142, "end of Théorème 1.2, 'Alors on a :' before (1.2.1)",
    "'Alors on a :' with a colon (not underlined)", "'Alors on a' without colon, then the equation (1.2.1)",
    "punctuation", "high",
    ("\n\\begin{equation}\\tag{1.2.1}", ":\n\\begin{equation}\\tag{1.2.1}"),
    "Colon left out; the 'old' begins after 'Alors on a', so it applies before or after the underline edit.")

# ---------------------------------------------------------------- p. 143
add(143, "'Par la formule de Lefschetz-Verdier (III 4.7), compte tenu de 1.1.3'",
    "Lefschetz-Verdier with a typewriter hyphen", "Lefschetz--Verdier", "punctuation", "high",
    ("Lefschetz--Verdier", "Lefschetz-Verdier"), "En dash added by the TeX (as pp. 138-139).")
add(143, "label of Corollaire 1.3", "'Corollaire 1.3 - Soit F ...': 'Corollaire' underlined, the number, a dash",
    "\\begin{statement}{Corollaire 1.3}", "punctuation", "high",
    ("\\begin{statement}{Corollaire 1.3}", "\\begin{statement}{Corollaire 1.3 -}"),
    "As Théorème 1.2 (p. 142). " + ENV.replace("{L}", "Corollaire 1.3"))
add(143, "statement of Corollaire 1.3, up to 'Alors on a'",
    "underlined: 'Soit' | 'un endomorphisme d'une courbe propre et lisse' | 'tel' + 'que le schéma des points fixes' "
    "(across the line break) | 'soit fini et formé de points où le graphe de' | 'est transverse à la diagonale' | "
    "'Soient' | 'et' | 'Alors on a'; not underlined: F, X/S, X^F, the formulas, the commas and full stops",
    "no underline", "underline", "high",
    ("Soit $F$ un endomorphisme d'une courbe propre et lisse $X/S$ tel que le schéma des points fixes $X^F$ soit fini "
     "et formé de points où le graphe de $F$ est transverse à la diagonale. Soient $L\\in\\ob D_{\\ctf}(X)$, et "
     "$u\\in\\Hom(F^*L,L)$. Alors on a",
     "\\emph{Soit} $F$ \\emph{un endomorphisme d'une courbe propre et lisse} $X/S$ \\emph{tel que le schéma des points "
     "fixes} $X^F$ \\emph{soit fini et formé de points où le graphe de} $F$ \\emph{est transverse à la diagonale}. "
     "\\emph{Soient} $L\\in\\ob D_{\\ctf}(X)$, \\emph{et} $u\\in\\Hom(F^*L,L)$. \\emph{Alors on a}"),
    "As Théorème 1.2; " + EMPH + ".")
add(143, "Corollaire 1.3, after the display: 'où la trace, aux deux membres, est prise au sens de (SGA 6 I 8).'",
    "underlined: 'où la trace' | 'aux deux membres' | 'est prise au sens de'; the commas and (SGA 6 I 8). not",
    "no underline", "underline", "high",
    ("où la trace, aux deux membres, est prise au sens de",
     "\\emph{où la trace}, \\emph{aux deux membres}, \\emph{est prise au sens de}"), "")
add(143, "'1.3 est le résultat d'Artin-Verdier ([6] 4.1)'", "Artin-Verdier with a typewriter hyphen",
    "Artin--Verdier", "punctuation", "high", ("Artin--Verdier", "Artin-Verdier"), "En dash added by the TeX.")
add(143, "label of Corollaire 1.3.1", "'Corollaire 1.3.1 - Avec X et F ...': 'Corollaire' underlined, the number, a dash",
    "\\begin{statement}{Corollaire 1.3.1}", "punctuation", "high",
    ("\\begin{statement}{Corollaire 1.3.1}", "\\begin{statement}{Corollaire 1.3.1 -}"),
    "As Théorème 1.2 (p. 142). " + ENV.replace("{L}", "Corollaire 1.3.1"))
add(143, "statement of Corollaire 1.3.1",
    "underlined: 'Avec' | 'et' | 'comme en' | 'soient' | 'un' | 'faisceau construc-' + 'tible sur' (across the line "
    "break; the hyphen after Q_ℓ is not underlined) | 'et' | 'Alors on a'; not underlined: X, F, 1.3, L, Q_ℓ, "
    "'(ℓ premier ≠ p)', the formulas, the punctuation",
    "no underline", "underline", "high",
    ("Avec $X$ et $F$ comme en 1.3, soient $L$ un $\\mathbb Q_\\ell$-faisceau constructible sur $X$ ($\\ell$ premier "
     "$\\ne p$), et $u\\in\\Hom(F^*L,L)$. Alors on a",
     "\\emph{Avec} $X$ \\emph{et} $F$ \\emph{comme en} 1.3, \\emph{soient} $L$ \\emph{un} $\\mathbb Q_\\ell$-\\emph{"
     "faisceau constructible sur} $X$ ($\\ell$ premier $\\ne p$), \\emph{et} $u\\in\\Hom(F^*L,L)$. \\emph{Alors on a}"),
    "As Théorème 1.2; " + EMPH + ".")
add(143, "display of Corollaire 1.3.1, 'Σ(-1)^i Tr((F,u),H^i(X,L))'",
    "a typed Σ with no index before (-1)^i (only the second sum has 'x ∈ X^F' below it)",
    "\\sum_i(-1)^i", "extra", "high", ("\\sum_i(-1)^i", "\\sum(-1)^i"), "Summation index added by the TeX.")
add(143, "end of the display of Corollaire 1.3.1, after Tr(u_x,L_x)",
    "no punctuation after the display", "\\Tr(u_x,L_x). (full stop)", "punctuation", "high",
    ("\\Tr(u_x,L_x).\n\\]", "\\Tr(u_x,L_x)\n\\]"), "Full stop added at the end of the display.")
add(143, "1.4, '(III 5.1) Du ∈ Hom(a_2^*DM,a_1^!DL) , Dv ∈ Hom(b_1^*DL,b_2^!DM) , et les homomorphismes'",
    "the two formulas run in the text line that ends ', et les homomorphismes'",
    "a display \\[ ... ,\\qquad ... , \\] between '(III~5.1)' and 'et les homomorphismes'",
    "other", "high",
    ("(III~5.1)\n\\[\nDu\\in\\Hom(a_2^*DM,a_1^!DL),\\qquad Dv\\in\\Hom(b_1^*DL,b_2^!DM),\n\\]\net les",
     "(III~5.1) $Du\\in\\Hom(a_2^*DM,a_1^!DL)$, $Dv\\in\\Hom(b_1^*DL,b_2^!DM)$, et les"),
    "Display against inline formula; does not touch the misprint below.")
add(143, "1.4, 'et les homomorphismes (Du)_z ∈ Hom((DM)_y,(DM)_x)'",
    "Hom((DM)_y,(DM)_x), clearly typed", "$(Du)_z\\in\\Hom((DM)_y,(DM)_x)$ (keeps the printed reading)",
    "misprint_in_print", "high", None,
    "Du ∈ Hom(a_2^*DM,a_1^!DL) goes from DM to DL, so (Du)_z goes from (DM)_y to (DL)_x (compare (Dv)_z ∈ "
    "Hom((DL)_x,(DM)_y) in the same line). The diplomatic TeX keeps the printed reading; the corrected layer "
    "already has (DL)_x.",
    corrected="\\Hom((DM)_y,(DL)_x)")

# ---------------------------------------------------------------- p. 144
add(144, "'par la formule de Lefschetz-Verdier (III 4.7) :'", "Lefschetz-Verdier with a typewriter hyphen",
    "Lefschetz--Verdier", "punctuation", "high", ("Lefschetz--Verdier", "Lefschetz-Verdier"),
    "En dash added by the TeX.")
add(144, "label of Corollaire 1.5", "'Corollaire 1.5 - Soient X , Y ...': 'Corollaire' underlined, the number, a dash",
    "\\begin{statement}{Corollaire 1.5}", "punctuation", "high",
    ("\\begin{statement}{Corollaire 1.5}", "\\begin{statement}{Corollaire 1.5 -}"),
    "As Théorème 1.2 (p. 142). " + ENV.replace("{L}", "Corollaire 1.5"))
add(144, "Corollaire 1.5, 'sur S , a : A ⟶ X x_S Y , b : B ⟶ X x_S Y des correspondances'",
    "the two maps run in the text line that ends 'des correspondances où A et B sont'; a comma between them",
    "a display \\[ ... ,\\qquad ... \\] after 'sur $S$,'", "other", "high",
    ("\n\\[\na:A\\longrightarrow X\\times_S Y,\n\\qquad\nb:B\\longrightarrow X\\times_S Y\n\\]\n",
     " $a:A\\longrightarrow X\\times_S Y$, $b:B\\longrightarrow X\\times_S Y$ "),
    "Display against inline formula; the 'old' runs from the line break after 'sur $S$,' to the one before 'des "
    "correspondances', so it does not overlap the underline edits around it.")
add(144, "Corollaire 1.5, 'Soient X , Y des courbes propres et lisses sur S ,'",
    "underlined: 'Soient' | 'des courbes propres et lisses sur'", "no underline", "underline", "high",
    ("Soient $X,Y$ des courbes propres et lisses sur $S$,",
     "\\emph{Soient} $X,Y$ \\emph{des courbes propres et lisses sur} $S$,"),
    "Underlined statement, as Théorème 1.2 (p. 142); " + EMPH + ". Five edits for this statement; they leave "
    "the misprint ({y} x Y) out.")
add(144, "Corollaire 1.5, 'des correspondances où A et B sont des courbes propres sur S ,'",
    "underlined: 'des correspondances où' | 'et' | 'sont' + 'des courbes propres sur' (across the line break)",
    "no underline", "underline", "high",
    ("des correspondances où $A$ et $B$ sont des courbes propres sur $S$,",
     "\\emph{des correspondances où} $A$ \\emph{et} $B$ \\emph{sont des courbes propres sur} $S$,"), "")
add(144, "Corollaire 1.5, from 'On suppose que' to 'chacun des couples' (conditions for z ∈ C_1)",
    "underlined: 'On suppose que' | 'est fini' + 'sur' | 'et de la forme' | 'avec les propriétés suivantes' | 'pour' | "
    "'les morphismes déduits de' | 'par localisation stricte aux images' + 'de' | 'sont finis' | 'et' | 'si' | "
    "'désigne l'image de' | 'dans' | 'chacun' + 'des couples'; not underlined: the formulas, z, the commas, the colon",
    "no underline", "underline", "high",
    ("On suppose que $C=A\\times_{(X\\times_S Y)}B$ est fini sur $S$ et de la forme $C=C_1\\amalg C_2$, avec les "
     "propriétés suivantes: pour $z\\in C_1$, les morphismes déduits de $a_2,b_1$ par localisation stricte aux images "
     "de $z$ sont finis, et, si $(x,y)$ désigne l'image de $z$ dans $X\\times_S Y$, chacun des couples",
     "\\emph{On suppose que} $C=A\\times_{(X\\times_S Y)}B$ \\emph{est fini sur} $S$ \\emph{et de la forme} "
     "$C=C_1\\amalg C_2$, \\emph{avec les propriétés suivantes}: \\emph{pour} $z\\in C_1$, \\emph{les morphismes "
     "déduits de} $a_2,b_1$ \\emph{par localisation stricte aux images de} $z$ \\emph{sont finis}, \\emph{et}, "
     "\\emph{si} $(x,y)$ \\emph{désigne l'image de} $z$ \\emph{dans} $X\\times_S Y$, \\emph{chacun des couples}"), "")
add(144, "Corollaire 1.5, from 'est en position générale en (x,y) ; pour z ∈ C_2' to 'Alors, si'",
    "underlined: 'est en position générale en' | 'pour' | 'les morphismes déduits de' | 'par localisation stricte' + "
    "'aux images de' | 'sont finis' | 'et chacun des couples' | 'est en position générale en' | 'position générale\" "
    "signifiant' (the opening quote not underlined) + 'que l'intersection des cônes tangents en' | 'aux images des "
    "courbes du couple' + 'considéré est réduite à' | 'Alors' | 'si'",
    "no underline", "underline", "high",
    ("est en position générale en $(x,y)$; pour $z\\in C_2$, les morphismes déduits de $a_1,b_2$ par localisation "
     "stricte aux images de $z$ sont finis, et chacun des couples $(A,B)$, $(A,\\{x\\}\\times Y)$, $(B,X\\times\\{y\\})$ "
     "est en position générale en $(x,y)$ (``position générale'' signifiant que l'intersection des cônes tangents en "
     "$(x,y)$ aux images des courbes du couple considéré est réduite à $(x,y)$). Alors, si",
     "\\emph{est en position générale en} $(x,y)$; \\emph{pour} $z\\in C_2$, \\emph{les morphismes déduits de} "
     "$a_1,b_2$ \\emph{par localisation stricte aux images de} $z$ \\emph{sont finis}, \\emph{et chacun des couples} "
     "$(A,B)$, $(A,\\{x\\}\\times Y)$, $(B,X\\times\\{y\\})$ \\emph{est en position générale en} $(x,y)$ "
     "(``\\emph{position générale'' signifiant que l'intersection des cônes tangents en} $(x,y)$ \\emph{aux images "
     "des courbes du couple considéré est réduite à} $(x,y)$). \\emph{Alors}, \\emph{si}"),
    "The underline of the first 'est en position générale en' (end of the z ∈ C_1 conditions) is in this edit.")
add(144, "Corollaire 1.5, 'sont les morphismes définis par u,v (III 3.7.6), on a, avec les notations de 1.1.1 ,'",
    "underlined: 'sont les morphismes définis par' | 'on' + 'a' (across the line break) | 'avec les notations de'",
    "no underline", "underline", "high",
    ("sont les morphismes définis par $u,v$ (III~3.7.6), on a, avec les notations de 1.1.1,",
     "\\emph{sont les morphismes définis par} $u,v$ (III~3.7.6), \\emph{on a}, \\emph{avec les notations de} 1.1.1,"),
    "")
add(144, "Corollaire 1.5, conditions for z ∈ C_1: 'chacun des couples (A,B) , (A, X x {y}) , ({y} x Y,B) est en "
    "position générale'",
    "({y} x Y,B), clearly typed", "$(\\{y\\}\\times Y,B)$ (keeps the printed reading)",
    "misprint_in_print", "high", None,
    "Théorème 1.2, which is applied at the points of C_1, asks {x} x Y and B to be in general position (p. 142: "
    "'ainsi que {x} x Y et B'); {y} x Y is not a curve in X x_S Y. The TeX keeps the printed reading (both layers).",
    corrected="(\\{x\\}\\times Y,B)")
add(144, "1.6, 'M le faisceau F considéré par Langlands, L = αM'",
    "a comma after 'Langlands'", "considéré par Langlands; (semicolon)", "punctuation", "high",
    ("par Langlands;", "par Langlands,"), "")
add(144, "1.6, '(α ∈ Q_ℓ^*),A = la diagonale de X x X'", "'A = la diagonale': an equals sign",
    "$A$ la diagonale", "missing", "high", ("$A$ la diagonale", "$A=$ la diagonale"), "")
add(144, "1.6, 'b = la correspondance φ de (loc. cit.)'", "'b = la correspondance': an equals sign",
    "$b$ la correspondance", "missing", "high", ("$b$ la correspondance", "$b=$ la correspondance"), "")
add(144, "end of the page: 'b = la correspondance φ de (loc. cit.)' / top of p. 145 'u = la correspondance'",
    "p. 144 ends '(loc. cit.)' with no comma; p. 145 begins 'u = la correspondance'",
    "(loc. cit.), $u$ la (with a comma)", "misprint_in_print", "medium",
    ("(loc. cit.), ", "(loc. cit.) "),
    "The enumeration 'X = Y, M le faisceau F ..., L = αM (...), A = ..., b = ... , u = ..., v = ...' needs a comma "
    "here; the typist left it out at the page turn. The TeX silently supplies it; the fix restores the printed "
    "reading (diplomatic layer only). Independent of the next edit and of the folio-145 marker.",
    corrected="(loc. cit.), ")
add(144, "top of p. 145 (text under the folio-144 marker): 'u = la correspondance à support dans A'",
    "'u = la correspondance': an equals sign", "$u$ la (last words of page_144.tex)", "missing", "high",
    ("$u$ la", "$u=$ la"),
    "Printed on p. 145; filed under p. 144 because the words stand in page_144.tex until the folio-145 marker is "
    "moved (marker finding of p. 145). The marker anchor '$u' works before and after this edit.")

# ---------------------------------------------------------------- p. 145
add(145, "top of the page",
    "p. 145 begins 'u = la correspondance à support dans A donnée par α^-1 : L ⟶ M ,'; p. 144 ends 'b = la "
    "correspondance φ de (loc. cit.)'",
    "'$u$ la' ends s5.tex line 4506 (both layers, at 20:17), the last line of page 144; the folio-145 marker "
    "(line 4507) follows it, so page_145.tex begins 'correspondance à support dans $A$'",
    "marker", "high", None,
    "Page 145 really begins at '$u$ la' at the end of s5.tex line 4506 (after '$\\phi$ de (loc. cit.), '). Exact fix: "
    "python -I move_marker.py 5 145 '$u' --before (single quotes: the anchor contains $; --before takes the last "
    "'$u' before the marker, which is this one; simulated in memory on both layers, before and after the p. 144 "
    "edits: the marker then splits line 4506 after '(loc. cit.), ' (diplomatic after the misprint edit: '(loc. cit.) "
    "'), and page 145 begins '$u$ la' or '$u=$ la'). Run it once only: a second run would carry the marker back to "
    "an earlier '$u'. Text not moved. Line numbers as of 20:17.")
add(145, "'v = la correspondance Φ de (loc. cit.) ;'", "'v = la correspondance': an equals sign",
    "$v$ la correspondance", "missing", "high", ("$v$ la correspondance", "$v=$ la correspondance"), "")
add(145, "every cℓ of p. 145: 'la correspondance cℓ(A) (resp. cℓ(B) )' and (1.7.1) 'deg(a_2)deg(b_1) = < cℓ(A) , cℓ(B) >'",
    "cℓ: a typed c followed by a script ℓ", "\\cl(A), \\cl(B), with \\cl = \\operatorname{cl} (a roman l)",
    "font", "medium", None,
    "Convention of the transcription (macro \\cl, s5.tex line 81), not listed per occurrence; already reported for "
    "Exposé III (pp. 96-110). One decision for the volume (e.g. \\operatorname{c\\ell} where the print writes cℓ).")

# ---------------------------------------------------------------- write and check
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "findings")

snap = {p: (RUN / "b141_145" / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(141, 146)}
snap[140] = (RUN / "b136_140" / "page_140.tex").read_text(encoding="utf-8")
live = {}
for ed in ("diplomatic", "current"):
    pg = pages("5", ed)
    live[ed] = {p: "".join(f.read_text(encoding="utf-8")[s:e] for f, s, e in pg.get(p, [])) for p in range(140, 147)}

bad = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    o, n = x["fix"]["old"], x["fix"]["new"]
    if MARK.search(o) or MARK.search(n):
        print("MARKER IN FIX", i)
        bad += 1
    cs = snap[x["page"]].count(o)
    cd = live["diplomatic"][x["page"]].count(o)
    cc = live["current"][x["page"]].count(o)
    flag = "" if (cs == 1 and cd == 1 and (cc == 1 or x["kind"] == "misprint_in_print")) else "  <-- CHECK"
    if flag:
        bad += 1
    print(f"{i:2d} p{x['page']} {x['kind']:18s} snapshot {cs} live-dipl {cd} live-current {cc}{flag}")

# sequential application on the live spans (in memory)
for ed in ("diplomatic", "current"):
    texts = dict(live[ed])
    for i, x in enumerate(F):
        if not x["fix"] or (ed == "current" and x["kind"] == "misprint_in_print"):
            continue
        o, n = x["fix"]["old"], x["fix"]["new"]
        c = texts[x["page"]].count(o)
        if c != 1:
            print(ed, "sequential: finding", i, "old occurs", c)
            bad += 1
            continue
        texts[x["page"]] = texts[x["page"]].replace(o, n, 1)
    left = sum(t.count("\\LL") for p, t in texts.items() if 141 <= p <= 145)
    print(ed, "sequential application done; \\LL left on pp. 141-145:", left)
print("problems:", bad)
