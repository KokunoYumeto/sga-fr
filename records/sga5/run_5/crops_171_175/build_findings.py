"""Build findings_171_175.json and check that every fix's old occurs exactly once in its page file."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5"
PAGES = f"{RUN}/b171_175"
OUT = f"{RUN}/findings_171_175.json"

F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf}
    d["fix"] = None if old is None else {"old": old, "new": new}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 171 ----------------
add(171, "display of the two evaluation arrows after 'le produit tensoriel des flèches d'évaluation', before 'Il en résulte que'",
    "'E ⊗^L_K RHom_A(E,P) ⟶ P) . Il en résulte que, pour': the parenthesis opened at '(le point est que' closes after P",
    r"E\lten_K\uRHom_A(E,P)\longrightarrow P.",
    "punctuation", "high",
    r"E\lten_K\uRHom_A(E,P)\longrightarrow P.",
    r"E\lten_K\uRHom_A(E,P)\longrightarrow P).",
    "The closing parenthesis of '(le point est que ...' is missing in the TeX.")
add(171, "'Il en résulte que, pour u ∈ Hom_A(E,P ⊗^L_A F)'",
    "Hom_A plain, not underlined (the RHom of the line above are underlined)",
    r"$u\in\uHom_A(E,P\lten_AF)$",
    "underline", "high",
    r"$u\in\uHom_A(", r"$u\in\Hom_A(",
    "Plain Hom in the print (global Hom).")
add(171, "same line, 'v ∈ Hom(F,Q ⊗^L_A E)'",
    "Hom plain, not underlined",
    r"$v\in\uHom(F,Q\lten_AE)$",
    "underline", "high",
    r"$v\in\uHom(", r"$v\in\Hom(",
    "")
add(171, "heading 5.9",
    "'5.9. Traces et extension des scalaires.' (underlined; full stop after the title)",
    r"\subsubsection*{5.9. Traces et extension des scalaires}",
    "punctuation", "high",
    r"\subsubsection*{5.9. Traces et extension des scalaires}",
    r"\subsubsection*{5.9. Traces et extension des scalaires.}",
    "Underlined titles end with a full stop in the print.")

# ---------------- page 172 ----------------
add(172, "top of the page: 'a un carré commutatif de D(K)'",
    "p. 172 begins with 'a un carré commutatif de D(K)'; p. 171 ends with '(F ⊗^L_{A^e} B^e) ⊗^L_A G ∈ ob D^+(B) , on'",
    "'a un' ends the last line of page_171.tex ('..., on a un'); page_172.tex begins with 'carré commutatif'",
    "marker", "high", None, None,
    "Page 172 really begins at 'a un' at the end of the last line of folio 171 (s5.tex line ending '$(F\\lten_{A^e}B^e)\\lten_AG\\in\\ob D^+(B)$, on a un'). "
    "Exact fix: python -I move_marker.py 5 172 \"a un\" --before (simulated read-only on both layers: the marker line goes between 'on ' and 'a un', splitting that line). "
    "Text not moved; 'a un' agrees with the print.")
add(172, "first line, 'a un carré commutatif de D(K)' before diagram (5.9.2)",
    "'carré commutatif de D(K)'",
    "'carré commutatif' (no 'de D(K)')",
    "missing", "high",
    "carré commutatif\n" + r"\begin{equation}\tag{5.9.2}",
    "carré commutatif de $D(K)$\n" + r"\begin{equation}\tag{5.9.2}",
    "")
add(172, "diagram (5.9.2), lower right corner",
    "'RHom_B(B ⊗^L_A E,(F ⊗^L_{A^e} B^e) ⊗^L_B (B ⊗^L_A G))' with nothing after it (no comma)",
    r"\uRHom_B(B\lten_AE,(F\lten_{A^e}B^e)\lten_B(B\lten_AG)),",
    "punctuation", "high",
    r"(B\lten_AG)),", r"(B\lten_AG))",
    "Comma added by the TeX.")
add(172, "'où les flèches verticales sont définies par 5.6.1' before diagram (5.9.3)",
    "'définies par' / '5.6.1' alone on the next line, no colon",
    r"définies par 5.6.1:",
    "punctuation", "high",
    r"définies par 5.6.1:", r"définies par 5.6.1",
    "Colon added by the TeX.")
add(172, "last sentence, 'où la flèche verticale de gauche (resp. droite) est donnée'",
    "'de gauche (resp. droite) est donnée par l'extension des'",
    "de gauche, respectivement de droite, est donnée",
    "word", "high",
    r"de gauche, respectivement de droite, est donnée",
    r"de gauche (resp. droite) est donnée",
    "The TeX writes out the abbreviation, adds 'de' and turns the parentheses into commas.")
add(172, "same sentence, 'scalaires (resp. est la flèche canonique déduite de A ⟶ B ) .'",
    "'des scalaires (resp. est la flèche canonique déduite de A ⟶ B ) .'",
    r"des scalaires, respectivement est la flèche canonique déduite de $A\to B$.",
    "word", "high",
    r"des scalaires, respectivement est la flèche canonique déduite de $A\to B$.",
    r"des scalaires (resp. est la flèche canonique déduite de $A\to B$).",
    "Both parentheses in this edit.")

# ---------------- page 173 ----------------
add(173, "heading 5.10",
    "'5.10. Traces et restriction des scalaires.' (underlined; full stop after the title)",
    r"\subsubsection*{5.10. Traces et restriction des scalaires}",
    "punctuation", "high",
    r"\subsubsection*{5.10. Traces et restriction des scalaires}",
    r"\subsubsection*{5.10. Traces et restriction des scalaires.}",
    "Underlined titles end with a full stop in the print.")
add(173, "first paragraph, 'de présentation finie (i.e. localement facteur direct d'un A-module libre de type fini).'",
    "'(i.e. localement facteur direct d'un A-module libre de type fini). C'est le cas'",
    "', c'est-à-dire localement facteur direct d'un $A$-module libre de type fini. C'est'",
    "word", "high",
    r"de présentation finie, c'est-à-dire localement facteur direct d'un $A$-module libre de type fini. C'est",
    r"de présentation finie (i.e. localement facteur direct d'un $A$-module libre de type fini). C'est",
    "The TeX writes out 'i.e.' and drops the parentheses; both parentheses in this edit.")
add(173, "'à une flèche (de B-bimodules)' before (5.10.1)",
    "'à une flèche (de B-bimodules)'",
    r"à une flèche de $B$-bimodules",
    "punctuation", "high",
    r"à une flèche de $B$-bimodules", r"à une flèche (de $B$-bimodules)",
    "Parentheses dropped by the TeX.")
add(173, "'est l'homomorphisme f ⟼ Tr_A(f) (=dfn Tr_A(d_f) ,'",
    "'dfn' written over the equals sign: (=^{dfn} Tr_A(d_f)",
    r"($=\Tr_A(d_f)$",
    "formula", "high",
    r"($=\Tr_A(d_f)$", r"($\stackrel{\mathrm{dfn}}{=}\Tr_A(d_f)$",
    "The file writes this sign \\stackrel{\\mathrm{dfn}}{=} elsewhere in Exposé III B.")
add(173, "'à droite par f) , donc par la formule Tr_A(f_g) = Tr_A(gf)'",
    "'donc par la formule' (no comma after 'donc'; a short slanted stroke stands above the d of 'donc', not a comma)",
    "donc, par la formule",
    "punctuation", "high",
    "donc, par la formule", "donc par la formule",
    "Comma added by the TeX.")
add(173, "'par la formule Tr_A(f_g) = Tr_A(gf) (5.8.5)'",
    "Tr_A(f_g): the g is typed half a line low, at the level of the subscript A",
    r"\Tr_A(fg)",
    "misprint_in_print", "high",
    r"\Tr_A(fg)", r"\Tr_A(f_g)",
    "Typing slip for Tr_A(fg) (the formula 5.8.5 Tr_A(vu) = Tr_A(uv) with f, g). The TeX silently corrects it; the edit restores the printed reading.",
    corrected=r"\Tr_A(fg)")
add(173, "'Tr_{B/A} : B_♮ ⟶ A_♮ : on a donc un carré commutatif'",
    "a colon before 'on a donc'",
    r"A_\natural$; on a donc",
    "punctuation", "high",
    r"A_\natural$; on a donc", r"A_\natural$ : on a donc",
    "")
add(173, "after (5.10.3), 'comme on le vérifie aussitôt (il suffit de voir ... de type fini). Cet isomorphisme'",
    "'aussitôt (il suffit de voir que l'homomorphisme K-linéaire sous-jacent est un isomorphisme, et cela résulte de ce que B est localement facteur direct d'un A-module libre de type fini). Cet isomorphisme'",
    "'aussitôt: il suffit ... de type fini. Cet isomorphisme'",
    "punctuation", "high",
    r"vérifie aussitôt: il suffit de voir que l'homomorphisme $K$-linéaire sous-jacent est un isomorphisme, et cela résulte de ce que $B$ est localement facteur direct d'un $A$-module libre de type fini. Cet",
    r"vérifie aussitôt (il suffit de voir que l'homomorphisme $K$-linéaire sous-jacent est un isomorphisme, et cela résulte de ce que $B$ est localement facteur direct d'un $A$-module libre de type fini). Cet",
    "The TeX turns the parenthesis into a colon and drops the closing parenthesis; both in this edit.")
add(173, "display (5.10.4)",
    "RHom_B(E,P) ⊗_A B ⥲ RHom_B(E,P ⊗_A B) , with plain ⊗_A (no L above either sign; B is flat over A)",
    r"\uRHom_B(E,P)\lten_AB\xrightarrow{\sim}\uRHom_B(E,P\lten_AB)",
    "formula", "high",
    r"\uRHom_B(E,P)\lten_AB\xrightarrow{\sim}\uRHom_B(E,P\lten_AB)",
    r"\uRHom_B(E,P)\otimes_AB\xrightarrow{\sim}\uRHom_B(E,P\otimes_AB)",
    "")

# ---------------- page 174 ----------------
add(174, "first paragraph, 'P ∈ ob D^+(B ⊗_K A^o) (résoudre E par des modules'",
    "an opening parenthesis before 'résoudre' (closed after 'à droite')",
    r"D^+(B\otimes_KA^\circ)$: résoudre",
    "punctuation", "high",
    r"D^+(B\otimes_KA^\circ)$: résoudre", r"D^+(B\otimes_KA^\circ)$ (résoudre",
    "Apply together with the fix 'de l'ôter à droite).' (the two parentheses of one clause).")
add(174, "first paragraph, 'A étant plat sur K : cela permet'",
    "a colon before 'cela permet'",
    r"plat sur $K$; cela",
    "punctuation", "high",
    r"plat sur $K$; cela", r"plat sur $K$ : cela",
    "")
add(174, "first paragraph, 'cela permet \"d'ôter le R\" à gauche'",
    "'\"d'ôter le R\"' in typewriter double quotes",
    r"permet d'ôter le $\R$ à gauche",
    "punctuation", "high",
    r"permet d'ôter le $\R$ à gauche", r"permet ``d'ôter le $\R$'' à gauche",
    "Quotation marks missing in the TeX.")
add(174, "first paragraph, 'et la résolution qu'on a prise pour E'",
    "'la résolution qu'on a prise pour E'",
    "la résolution prise pour",
    "missing", "high",
    "la résolution prise pour", "la résolution qu'on a prise pour",
    "")
add(174, "first paragraph, end: 'permet aussi de l'ôter à droite).'",
    "'l'ôter à droite).'",
    "de l'ôter à droite.",
    "punctuation", "high",
    "de l'ôter à droite.", "de l'ôter à droite).",
    "Closing parenthesis; apply together with the fix '$ (résoudre'.")
add(174, "display (5.10.5), inner tensor products",
    "RHom_B(E,B ⊗_K M) ⊗^L_B F ⟶ RHom_A(E,A ⊗_K M) ⊗^L_A F : no L above the ⊗_K inside RHom (L only above ⊗_B and ⊗_A)",
    r"\uRHom_B(E,B\lten_KM)\lten_BF\longrightarrow\uRHom_A(E,A\lten_KM)\lten_AF",
    "formula", "high",
    r"B\lten_KM)\lten_BF\longrightarrow\uRHom_A(E,A\lten_KM)",
    r"B\otimes_KM)\lten_BF\longrightarrow\uRHom_A(E,A\otimes_KM)",
    "")
add(174, "display (5.10.5), end",
    "a comma after the formula",
    r"\lten_AF (no comma)",
    "punctuation", "high",
    r"\lten_AF" + "\n" + r"\end{equation}",
    r"\lten_AF," + "\n" + r"\end{equation}",
    "")
add(174, "composite after 'comme composée des flèches', source of (1)",
    "RHom_B(E,B ⊗_K M) ⊗^L_B F : plain ⊗_K",
    r'''\uRHom_B(E,B\lten_KM)\lten_BF \arrow[r,"(1)"]''',
    "formula", "high",
    r'''\uRHom_B(E,B\lten_KM)\lten_BF \arrow[r,"(1)"]''',
    r'''\uRHom_B(E,B\otimes_KM)\lten_BF \arrow[r,"(1)"]''',
    "")
add(174, "composite, target of (1)",
    "RHom_B(E,Hom_A(B,A) ⊗_A B ⊗^L_K M) ⊗^L_B F : plain ⊗_A, no parentheses around B ⊗ M, L only above ⊗_K and ⊗_B",
    r"\uRHom_B(E,\uHom_A(B,A)\lten_A(B\lten_KM))\lten_BF",
    "formula", "high",
    r"\uHom_A(B,A)\lten_A(B\lten_KM))\lten_BF",
    r"\uHom_A(B,A)\otimes_AB\lten_KM)\lten_BF",
    "The TeX adds an L over ⊗_A and the parentheses (B ⊗ M).")
add(174, "composite, target of (2)",
    "RHom_B(E,Hom_A(B,A) ⊗^L_K M) ⊗_A B ⊗^L_B F : plain ⊗_A",
    r"\uRHom_B(E,\uHom_A(B,A)\lten_KM)\lten_A B\lten_BF",
    "formula", "high",
    r"\lten_KM)\lten_A B\lten_BF", r"\lten_KM)\otimes_A B\lten_BF",
    "")
add(174, "composite, target of (3)",
    "RHom_B(E,Hom_A(B,A ⊗_K M)) ⊗^L_A F : plain ⊗_K inside Hom_A",
    r"\uRHom_B(E,\uHom_A(B,A\lten_KM))\lten_AF",
    "formula", "high",
    r"\uRHom_B(E,\uHom_A(B,A\lten_KM))\lten_AF",
    r"\uRHom_B(E,\uHom_A(B,A\otimes_KM))\lten_AF",
    "")
add(174, "composite, target of (4)",
    "RHom_A(E,A ⊗_K M) ⊗^L_A F , : plain ⊗_K",
    r"\uRHom_A(E,A\lten_KM)\lten_AF,",
    "formula", "high",
    r"\uRHom_A(E,A\lten_KM)\lten_AF,", r"\uRHom_A(E,A\otimes_KM)\lten_AF,",
    "")
add(174, "isomorphism of (3), 'Hom_A(B,A) ⊗^L_K M ⥲ Hom_A(B,A ⊗_K M) (5.4.2)'",
    "the target Hom_A(B,A ⊗_K M) has a plain ⊗_K (L only over the source's ⊗_K)",
    r"\uHom_A(B,A)\lten_KM\xrightarrow{\sim}\uHom_A(B,A\lten_KM)",
    "formula", "high",
    r"\xrightarrow{\sim}\uHom_A(B,A\lten_KM)", r"\xrightarrow{\sim}\uHom_A(B,A\otimes_KM)",
    "")
add(174, "label of Proposition 5.10.6",
    "'Proposition 5.10.6 - Supposons que' (dash after the number)",
    r"\begin{statement}{Proposition 5.10.6}",
    "punctuation", "high",
    r"\begin{statement}{Proposition 5.10.6}", r"\begin{statement}{Proposition 5.10.6 -}",
    "As the earlier statements of Exposé III B (Théorème 1.2 -, Lemme 2.2 -, ...).")
add(174, "statement of Proposition 5.10.6, first sentence",
    "'Supposons que' and 'On a alors un carré commu-tatif de' underlined; the formula M ⊗^L_K F ∈ ob D^+(B) and D(K) not underlined",
    "no underline",
    "underline", "high",
    r"Supposons que $M\lten_KF\in\ob D^+(B)$. On a alors un carré commutatif de $D(K)$",
    r"\emph{Supposons que} $M\lten_KF\in\ob D^+(B)$. \emph{On a alors un carré commutatif de} $D(K)$",
    "Statement text underlined word group by word group, as written with \\emph earlier in Exposé III B.")
add(174, "diagram (5.10.7), upper left corner",
    "RHom_B(E,B ⊗_K M) ⊗^L_B F : plain ⊗_K",
    r'''\uRHom_B(E,B\lten_KM)\lten_BF \arrow[r,"5.4.2"]''',
    "formula", "high",
    r'''\uRHom_B(E,B\lten_KM)\lten_BF \arrow[r,"5.4.2"]''',
    r'''\uRHom_B(E,B\otimes_KM)\lten_BF \arrow[r,"5.4.2"]''',
    "")
add(174, "diagram (5.10.7), lower left corner, inner tensor product",
    "RHom_A(E,A ⊗_K M) : plain ⊗_K",
    r'''\uRHom_A(E,A\lten_KM)\lten_AF \arrow[r,"5.4.2"']''',
    "formula", "high",
    r"\arrow[d]\\" + "\n" + r"\uRHom_A(E,A\lten_KM)",
    r"\arrow[d]\\" + "\n" + r"\uRHom_A(E,A\otimes_KM)",
    "Listed before the misprint of the same corner; the two edits are adjacent, not overlapping.")
add(174, "diagram (5.10.7), lower left corner, outer tensor product",
    "RHom_A(E,A ⊗_K M) ⊗_A F : no L above this ⊗_A (clean scan, nothing above the sign), while 5.10.5, the composite and the top row of the diagram have ⊗^L",
    r'''\lten_AF \arrow[r,"5.4.2"']''',
    "misprint_in_print", "medium",
    r'''\lten_AF \arrow[r,"5.4.2"']''',
    r'''\otimes_AF \arrow[r,"5.4.2"']''',
    "The reading (no L) is certain; the TeX silently supplies the L. Classed as a typing omission because the same term is RHom_A(E,A ⊗_K M) ⊗^L_A F in 5.10.5 and in the composite.",
    corrected=r'''\lten_AF \arrow[r,"5.4.2"']''')
add(174, "end of Proposition 5.10.6",
    "'où la flèche verticale de droite est la restriction des scalaires.' underlined (the full stop not)",
    "no underline",
    "underline", "high",
    "où la flèche verticale de droite est la restriction des scalaires.",
    r"\emph{où la flèche verticale de droite est la restriction des scalaires}.",
    "")

# ---------------- page 175 ----------------
add(175, "square after 'Il s'agit de vérifier', upper left corner",
    "E ⊗^L_K RHom_B(E,B ⊗_K M) ⊗^L_B F : plain ⊗_K inside RHom",
    r"E\lten_K\uRHom_B(E,B\lten_KM)\lten_BF",
    "formula", "high",
    r"E\lten_K\uRHom_B(E,B\lten_KM)\lten_BF", r"E\lten_K\uRHom_B(E,B\otimes_KM)\lten_BF",
    "")
add(175, "same square, label of the left vertical arrow",
    "'E ⊗^L 5.10.5' (L above the sign, no subscript K)",
    r"E\lten_K5.10.5",
    "formula", "high",
    r'''\arrow[d,"E\lten_K5.10.5"']''', r'''\arrow[d,"E\lten 5.10.5"']''',
    "Subscript K added by the TeX.")
add(175, "same square, lower left corner",
    "E ⊗^L_K RHom_A(E,A ⊗_K M) ⊗^L_A F : plain ⊗_K inside RHom",
    r"E\lten_K\uRHom_A(E,A\lten_KM)\lten_AF",
    "formula", "high",
    r"E\lten_K\uRHom_A(E,A\lten_KM)\lten_AF", r"E\lten_K\uRHom_A(E,A\otimes_KM)\lten_AF",
    "")
add(175, "triangle (*), top vertex",
    "RHom_B(E,B ⊗_K M) : plain ⊗_K",
    r'''\uRHom_B(E,B\lten_KM) \arrow[d,"(1)"']''',
    "formula", "high",
    r"\uRHom_B(E,B\lten_KM) \arrow[d", r"\uRHom_B(E,B\otimes_KM) \arrow[d",
    "")
add(175, "triangle (*), lower left vertex",
    "RHom_B(E,Hom_A(B,B ⊗_K M)) : plain ⊗_K",
    r"\uRHom_B(E,\uHom_A(B,B\lten_KM))",
    "formula", "high",
    r"\uHom_A(B,B\lten_KM)) \arrow", r"\uHom_A(B,B\otimes_KM)) \arrow",
    "")
add(175, "triangle (*), lower right vertex",
    "RHom_A(E,B ⊗_K M) , : plain ⊗_K",
    r"\uRHom_A(E,B\lten_KM),",
    "formula", "high",
    r"\uRHom_A(E,B\lten_KM),", r"\uRHom_A(E,B\otimes_KM),",
    "")
add(175, "'Or la flèche B ⊗_K M ⟶ Hom_A(B,B ⊗_K M) donnée par 5.10.1'",
    "both tensor products plain (no L)",
    r"$B\lten_KM\to\uHom_A(B,B\lten_KM)$",
    "formula", "high",
    r"$B\lten_KM\to\uHom_A(B,B\lten_KM)$", r"$B\otimes_KM\to\uHom_A(B,B\otimes_KM)$",
    "")
add(175, "paragraph 'Soient E ∈ ob D^-(B) , M ∈ ob D^b(K) tels que RHom_B(E,B ⊗_K M) ∈ ob D^b(B^o).'",
    "RHom_B(E,B ⊗_K M) with a plain ⊗_K",
    r"\uRHom_B(E,B\lten_KM)\in\ob D^b(B^\circ)$. On dispose",
    "formula", "high",
    r"B\lten_KM)\in\ob D^b(B^\circ)$. On dispose", r"B\otimes_KM)\in\ob D^b(B^\circ)$. On dispose",
    "")
add(175, "evaluation display after 'd'une flèche d'évaluation'",
    "RHom_B(E,B ⊗_K M) ⊗^L_B E ⟶ M ⊗^L_K (B ⊗^L_{B^e} B) : plain ⊗_K inside RHom",
    r"\uRHom_B(E,B\lten_KM)\lten_BE\longrightarrow M\lten_K(B\lten_{B^e}B),",
    "formula", "high",
    r"\uRHom_B(E,B\lten_KM)\lten_BE\longrightarrow M\lten_K(B",
    r"\uRHom_B(E,B\otimes_KM)\lten_BE\longrightarrow M\lten_K(B",
    "")
add(175, "display (5.10.8)",
    "RHom_B(E,B ⊗_K M) ⊗^L_B E ⟶ M ⊗^L_K B_♮ : plain ⊗_K inside RHom",
    r"\uRHom_B(E,B\lten_KM)\lten_BE\longrightarrow M\lten_KB_\natural.",
    "formula", "high",
    r"\uRHom_B(E,B\lten_KM)\lten_BE\longrightarrow M\lten_KB_\natural.",
    r"\uRHom_B(E,B\otimes_KM)\lten_BE\longrightarrow M\lten_KB_\natural.",
    "")
add(175, "label of Proposition 5.10.9",
    "'Proposition 5.10.9 - Supposons' (dash after the number)",
    r"\begin{statement}{Proposition 5.10.9}",
    "punctuation", "high",
    r"\begin{statement}{Proposition 5.10.9}", r"\begin{statement}{Proposition 5.10.9 -}",
    "")
add(175, "statement of Proposition 5.10.9, 'Supposons A de présentation finie ... tels que'",
    "underlined: 'Supposons', 'de présentation finie et plat en tant que', 'module' (not 'K-'), 'et', 'plats sur', 'Soient', 'tels que'; formulas, 'A', 'K' not underlined",
    "no underline",
    "underline", "high",
    r"Supposons $A$ de présentation finie et plat en tant que $K$-module, et $A_\natural$, $B_\natural$ plats sur $K$. Soient $E\in\ob D^-(B)$, $M\in\ob D^b(K)$ tels que",
    r"\emph{Supposons} $A$ \emph{de présentation finie et plat en tant que} $K$-\emph{module}, \emph{et} $A_\natural$, $B_\natural$ \emph{plats sur} $K$. \emph{Soient} $E\in\ob D^-(B)$, $M\in\ob D^b(K)$ \emph{tels que}",
    "")
add(175, "statement of Proposition 5.10.9, 'RHom_B(E,B ⊗_K M) ∈ ob D^b(B^o) . Alors RHom_A(E,A ⊗_K M)'",
    "both tensor products plain ⊗_K; 'Alors' underlined",
    r"$\uRHom_B(E,B\lten_KM)\in\ob D^b(B^\circ)$. Alors $\uRHom_A(E,A\lten_KM)",
    "formula", "high",
    r"$\uRHom_B(E,B\lten_KM)\in\ob D^b(B^\circ)$. Alors $\uRHom_A(E,A\lten_KM)",
    r"$\uRHom_B(E,B\otimes_KM)\in\ob D^b(B^\circ)$. \emph{Alors} $\uRHom_A(E,A\otimes_KM)",
    "The same edit underlines 'Alors' (\\emph), as the print; it lies between the two formulas.")
add(175, "statement of Proposition 5.10.9, end of the page: ', et l'on a un carré commutatif'",
    "'et l'on a un carré commutatif' underlined",
    "no underline",
    "underline", "high",
    "et l'on a un carré commutatif", r"\emph{et l'on a un carré commutatif}",
    "")
add(175, "end of the page: diagram (5.10.10) of Proposition 5.10.9",
    "p. 175 ends with 'et l'on a un carré commutatif' and blank space below; the diagram (5.10.10) is not on this page",
    "page_175.tex continues with \\begin{equation}\\tag{5.10.10} and the two rows of the diagram; the folio-176 marker stands inside the tikzcd, before \\end{tikzcd}",
    "marker", "high", None, None,
    "Page 176 really begins at '\\begin{equation}\\tag{5.10.10}'. Exact fix: python -I move_marker.py 5 176 \"\\begin{equation}\\tag{5.10.10}\" --before "
    "(simulated read-only on both layers: the marker goes on its own line just before that line). Text not moved. The diagram's content was not checked here "
    "(it is not on p. 175): after the move it must be checked against the scan of p. 176; on pp. 174-175 the print writes B ⊗_K M and A ⊗_K M without L, "
    "so check its \\uRHom_B(E,B\\lten_KM) and \\uRHom_A(E,A\\lten_KM) in particular.")

# ---------------- checks ----------------
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = open(f"{PAGES}/page_{d['page']:03d}.tex", encoding="utf-8").read()
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", n, d["page"], repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"]:
        ok = False
        print("MARKER IN OLD", d["page"])
# overlapping olds on the same page
for p in (171, 172, 173, 174, 175):
    t = open(f"{PAGES}/page_{p:03d}.tex", encoding="utf-8").read()
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "ok", ok)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
print("written", OUT)
