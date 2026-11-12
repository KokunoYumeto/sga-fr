import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = "C:/Users/user/Documents/sga_scan_check_20261105/run_5"
NL = chr(10)


def J(*lines):
    return NL.join(lines)


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


LABEL_NOTE = ("Exposé III B prints its run-in labels with ' -', as Exposé III does. The III B statement environment "
              "(s5.tex line 4360) still appends a full stop, so this edit gives the print's 'LABEL -' only together "
              "with the Exposé III environments (no automatic full stop) for III B.")

# ---------------- page 146 ----------------
add(146, "§2 heading, first line of the page",
    "2. - Réduction à un théorème d'annulation.  (underlined; ' - ' after the number, full stop at the end)",
    r"\subsection*{2. Réduction à un théorème d'annulation}",
    "punctuation", "high",
    (r"\subsection*{2. Réduction à un théorème d'annulation}",
     r"\subsection*{2. - Réduction à un théorème d'annulation.}"),
    "The underlined title has ' - ' after '2.' and ends with a full stop; the TeX drops both.")

add(146, "first diagram (squares (1), (2)), the three vertical arrows",
    "all three vertical arrows are hooked inclusion arrows, hook at the top: U → X (i), a_1^{-1}(U) → A, V → Y (j)",
    r'U \arrow[d,"i"] ... \arrow[d] ... V \arrow[d,"j"]  (plain arrows)',
    "symbol", "high",
    (r'''U \arrow[d,"i"] \arrow[rd,phantom,"(1)"{description}] & a_1^{-1}(U) \arrow[l,"a'_1"'] \arrow[r,"a'_2"] \arrow[d] \arrow[rd,phantom,"(2)"{description}] & V \arrow[d,"j"]''',
     r'''U \arrow[d,hook,"i"] \arrow[rd,phantom,"(1)"{description}] & a_1^{-1}(U) \arrow[l,"a'_1"'] \arrow[r,"a'_2"] \arrow[d,hook] \arrow[rd,phantom,"(2)"{description}] & V \arrow[d,hook,"j"]'''),
    "tikz-cd's hook option puts the hook at the tail (the top), as in the print. Label sides left as they are.")

add(146, "end of the first diagram",
    "the first diagram is followed by a comma (right of its bottom row), like the second",
    r'''X & A \arrow[l,"a_1"] \arrow[r,"a_2"'] & Y  (no comma)''',
    "punctuation", "high",
    (r'''\arrow[r,"a_2"'] & Y''', r'''\arrow[r,"a_2"'] & Y ,'''),
    "The TeX has the comma only after the second diagram.")

add(146, "second diagram (squares (3), (4)), vertical arrows",
    "the outer vertical arrows are hooked (U → X labelled i, V → Y labelled j); the middle arrow b_2^{-1}(V) → B is plain",
    r'U \arrow[d,"i"] ... V \arrow[d,"j"]  (plain arrows)',
    "symbol", "high",
    (r'''U \arrow[d,"i"] \arrow[rd,phantom,"(3)"{description}] & b_2^{-1}(V) \arrow[l,"b'_1"'] \arrow[r,"b'_2"] \arrow[d] \arrow[rd,phantom,"(4)"{description}] & V \arrow[d,"j"]''',
     r'''U \arrow[d,hook,"i"] \arrow[rd,phantom,"(3)"{description}] & b_2^{-1}(V) \arrow[l,"b'_1"'] \arrow[r,"b'_2"] \arrow[d] \arrow[rd,phantom,"(4)"{description}] & V \arrow[d,hook,"j"]'''),
    "Only the i and j arrows are hooked in this diagram; the middle arrow stays plain.")

add(146, "Lemme 2.2, label",
    "Lemme 2.2 - Pour prouver 1.2, ...",
    r"\begin{statement}{Lemme 2.2}  (renders 'Lemme 2.2.')",
    "punctuation", "high",
    (r"\begin{statement}{Lemme 2.2}", r"\begin{statement}{Lemme 2.2 -}"),
    LABEL_NOTE.replace("LABEL", "Lemme 2.2"))

add(146, "Lemme 2.2, case b)",
    "b) L|U = 0 , M|U = 0 .",
    r"\text{b) } L|U=0,\quad M|U=0 .",
    "misprint_in_print", "high", None,
    "M is a complex on Y and V = Y - {y} (Lemme 2.3 on p. 147: L|U = 0, M|V = 0); the print's M|U is a misprint "
    "for M|V. The TeX keeps the printed reading.",
    corrected=r"M|V=0")

add(146, "display of F^nL",
    "F^nL = { L si n ≤ 0 / i_!i^*L si n = 1 / 0 si n > 1 }  ('si' before each condition, no commas)",
    J(r"L,& n\le 0,\\", r"i_!i^*L,& n=1,\\", r"0,& n>1,"),
    "word", "high",
    (J(r"L,& n\le 0,\\", r"i_!i^*L,& n=1,\\", r"0,& n>1,"),
     J(r"L & \text{si } n\le 0\\", r"i_!i^*L & \text{si } n=1\\", r"0 & \text{si } n>1")),
    "The TeX replaces the print's 'si' by commas and adds commas at the line ends.")

add(146, "between the displays of F^nL and F^nM",
    "F^nL = {...} , F^nM = {...} .  (comma between the two systems)",
    J(r"\end{cases}", r"\qquad"),
    "punctuation", "high",
    (J(r"\end{cases}", r"\qquad"), J(r"\end{cases}", r",\qquad")),
    "Missing comma between the two systems.")

add(146, "display of F^nM",
    "F^nM = { M si n ≤ 0 / j_!j^*M si n = 1 / 0 si n > 1 } .",
    J(r"M,& n\le 0,\\", r"j_!j^*M,& n=1,\\", r"0,& n>1."),
    "word", "high",
    (J(r"M,& n\le 0,\\", r"j_!j^*M,& n=1,\\", r"0,& n>1."),
     J(r"M & \text{si } n\le 0\\", r"j_!j^*M & \text{si } n=1\\", r"0 & \text{si } n>1.")),
    "As for F^nL: 'si' before each condition, no commas at the line ends.")

add(146, "display F^1a_{2*}a_1^*L = ...",
    "F^1a_{2*}a^*_1L = j_!(a'_{2!}a'^*_1i^*L) .",
    r"F^1a_{2*}a_1^*L=j_!(a'_2)_!(a'_1)^*i^*L.",
    "formula", "high",
    (r"j_!(a'_2)_!(a'_1)^*i^*L.", r"j_!(a'_{2!}a'^*_1i^*L)."),
    "The print opens the parenthesis after j_! and closes it after L, with the shriek inside the subscript of "
    "a'_2 (a'_{2!}); the TeX parenthesizes the maps instead.")

add(146, "display F^nb_{1*}b_2^*M after 'On a de même' (printed on p. 147)",
    "F^nb_{1*}b^*_2M = { b_{1*}b^*_2M si n ≤ 0 / i_!(b'_{1!}b'^*_2j^*M) si n = 1 / 0 si n > 1 } .",
    J(r"b_{1*}b_2^*M,& n\le 0,\\", r"i_!(b'_1)_!(b'_2)^*j^*M,& n=1,\\", r"0,& n>1."),
    "formula", "high",
    (J(r"b_{1*}b_2^*M,& n\le 0,\\", r"i_!(b'_1)_!(b'_2)^*j^*M,& n=1,\\", r"0,& n>1."),
     J(r"b_{1*}b_2^*M & \text{si } n\le 0\\", r"i_!(b'_{1!}b'^*_2j^*M) & \text{si } n=1\\",
       r"0 & \text{si } n>1.")),
    "Two differences in one edit: 'si' and no end commas, as in the displays of F^nL and F^nM; and the n = 1 case "
    "is i_!(b'_{1!}b'^*_2j^*M) in the print (parenthesis after i_!), not i_!(b'_1)_!(b'_2)^*j^*M. Printed on "
    "p. 147; listed under page 146 because the text stands before the folio-147 marker (see the marker finding).")

add(146, "throughout pp. 146-150: formulas run into the text",
    "the print runs many formulas in the text line, e.g. p. 146 'donc a_1^{-1}(U) ⊂ a_2^{-1}(V) , "
    "b_2^{-1}(V) ⊂ b_1^{-1}(U) , et l'on a des diagrammes commutatifs'; p. 147 'que nous noterons encore "
    "u ∈ Hom_DF(...) (resp. ...) . par l'additivité'; p. 149 'la flèche de Künneth (III 4.2.1) "
    "a^!P ⊗_Z b^!Q → c^!(P ⊗ Q) en une \"flèche de changement de base\"'",
    r"sets these formulas as displays \[ ... \]",
    "other", "medium", None,
    "A convention of the transcription on all five pages (also p. 146 'filtré par F^na_{2*}a^*_1L = ...', "
    "p. 147 'u : a_{2*}a^*_1L → M (resp. ...)', 'L = h_{1*}L', ...', p. 148 '< u_z,v_z > = < u,v >_z', "
    "'h_* : Hom(...) → Hom(...)', p. 149 '< u,v > = < u',v' >' and the base-change and projection arrows). "
    "Reported once, not itemized; the other edits keep the TeX's displays.")

# ---------------- page 147 ----------------
add(147, "top of the page",
    "p. 147 begins 'On a de même' and the display F^nb_{1*}b^*_2M = {...} ., then 'On peut supposer u (resp. v) "
    "défini'; p. 146 ends with the display F^1a_{2*}a^*_1L = j_!(...) . and blank space",
    "'On a de même' and the first lines of its cases display stand at the end of page_146.tex (s5.tex lines "
    "4611-4617); the folio-147 marker (line 4618) sits inside the cases environment, before \\end{cases}",
    "marker", "high", None,
    "Page 147 really begins at 'On a de même' (s5.tex line 4611; 4610 in the current layer). Exact fix: "
    "python -I move_marker.py 5 147 \"On a de même\" --before (the anchor occurs once on p. 146; simulated in "
    "memory on both layers: the marker then stands on its own line between the '\\]' that closes "
    "F^1a_{2*}a_1^*L=... and 'On a de même'). Apply the page-146 edit of that cases display before the move.")

add(147, "display u : a_{2*}a_1^*L → M",
    "u : a_{2*}a^*_1L ⟶ M with u underlined (the homomorphism of complexes)",
    r"u:a_{2*}a_1^*L\longrightarrow M",
    "underline", "high",
    (r"u:a_{2*}a_1^*L\longrightarrow M", r"\underline{u}:a_{2*}a_1^*L\longrightarrow M"),
    "On this page the print underlines u and v where they denote the homomorphisms of complexes, not where they "
    "denote the correspondences ('On peut supposer u (resp. v)', 'Ainsi u (resp. v)', < u_z,v_z >, < u,v >).")

add(147, "same display, resp. part",
    "(resp. v : b_{1*}b^*_2M ⟶ L) with v underlined",
    r"(\text{resp. }u:b_{1*}b_2^*M\longrightarrow L).",
    "symbol", "high",
    (r"(\text{resp. }u:b_{1*}b_2^*M", r"(\text{resp. }\underline{v}:b_{1*}b_2^*M"),
    "The TeX has u for the print's v, and drops the underline.")

add(147, "the composite F^1a_{2*}a_1^*L → a_{2*}a_1^*L → M, arrow label",
    "label u underlined",
    r"\xrightarrow{u}M",
    "underline", "high",
    (r"\xrightarrow{u}M", r"\xrightarrow{\underline{u}}M"),
    "Underlined label.")

add(147, "(resp. F^1b_{1*}b_2^*M → b_{1*}b_2^*M → L), arrow label",
    "label underlined",
    r"\xrightarrow{v}L",
    "underline", "high",
    (r"\xrightarrow{v}L", r"\xrightarrow{\underline{v}}L"),
    "Apply before the misprint edit of the same label (next finding).")

add(147, "(resp. F^1b_{1*}b_2^*M → b_{1*}b_2^*M → L), arrow label",
    "the label is an underlined u, where v (underlined) is meant",
    r"\xrightarrow{v}L  (silently corrected)",
    "misprint_in_print", "high",
    (r"\xrightarrow{\underline{v}}L", r"\xrightarrow{\underline{u}}L"),
    "The resp. composite goes through v : b_{1*}b^*_2M → L; the print's u is a misprint, which the TeX silently "
    "corrects. The 'old' is the text after the preceding underline edit: apply the two in order.",
    corrected=r"\xrightarrow{\underline{v}}L")

add(147, "'se factorise (de manière unique)'",
    "se factorise (de manière unique) à travers F^1M",
    r"se factorise de manière unique à travers $F^1M$",
    "punctuation", "high",
    ("se factorise de manière unique à travers", "se factorise (de manière unique) à travers"),
    "Parentheses dropped by the TeX.")

add(147, "'(resp. F^1L), en d'autres termes que'",
    "(resp. F^1L), en d'autres termes que u (resp. v) est un homomorphisme",
    r"(resp. $F^1L$); en d'autres termes, $u$ (resp. $v$) est un homomorphisme",
    "word", "high",
    ("(resp. $F^1L$); en d'autres termes,", "(resp. $F^1L$), en d'autres termes que"),
    "The print has a comma after (resp. F^1L) and 'que' after 'en d'autres termes', with no comma; the TeX has a "
    "semicolon, adds a comma and drops 'que'.")

add(147, "'que u (resp. v) est un homomorphisme de complexes filtrés'",
    "u and v underlined",
    r"$u$ (resp. $v$) est un homomorphisme",
    "underline", "high",
    ("$u$ (resp. $v$) est un homomorphisme", r"$\underline{u}$ (resp. $\underline{v}$) est un homomorphisme"),
    "Underlined in the print (homomorphisms of complexes).")

add(147, "'correspondance filtrée (au sens de (III 4.13))'",
    "une correspondance filtrée (au sens de (III 4.13)), que nous noterons encore",
    "une correspondance filtrée, au sens de (III 4.13), que nous noterons encore",
    "punctuation", "high",
    ("filtrée, au sens de (III 4.13), que", "filtrée (au sens de (III 4.13)), que"),
    "Parentheses dropped by the TeX.")

add(147, "'que nous noterons encore u ∈ Hom_DF(...) (resp. v ∈ Hom_DF(...))'",
    "u ∈ Hom_DF(a^*_1L,a^!_2M)   (resp. v ∈ Hom_DF(b^*_2M,b^!_1L)) .   (u, v underlined)",
    J(r"u\in\Hom_{DF}(a_1^*L,a_2^!M),\qquad", r"v\in\Hom_{DF}(b_2^*M,b_1^!L)."),
    "missing", "high",
    (J(r"u\in\Hom_{DF}(a_1^*L,a_2^!M),\qquad", r"v\in\Hom_{DF}(b_2^*M,b_1^!L)."),
     J(r"\underline{u}\in\Hom_{DF}(a_1^*L,a_2^!M)\qquad", r"(\text{resp. }\underline{v}\in\Hom_{DF}(b_2^*M,b_1^!L)).")),
    "The TeX drops '(resp. ...)' round the second correspondence, puts a comma between the two, and drops the "
    "underlines.")

add(147, "'. par l'additivité des cup-produits'",
    "(resp. v ∈ Hom_DF(b^*_2M,b^!_1L)) . par l'additi-vité  (lower-case p after the full stop)",
    "Par l'additivité",
    "misprint_in_print", "high",
    ("Par l'additivité", "par l'additivité"),
    "Lower-case 'par' after a full stop, a typing error; the TeX silently corrects it.",
    corrected="Par l'additivité")

add(147, "first cup-product display",
    "< u_z,v_z > = < gr^0 u_z , gr^0 v_z > + < gr^1 u_z , gr^1 v_z > ,  (u, v underlined in the gr terms only)",
    J(r"=\langle \operatorname{gr}^0u_z,\operatorname{gr}^0v_z\rangle",
      r" +\langle \operatorname{gr}^1u_z,\operatorname{gr}^1v_z\rangle,"),
    "underline", "high",
    (J(r"=\langle \operatorname{gr}^0u_z,\operatorname{gr}^0v_z\rangle",
       r" +\langle \operatorname{gr}^1u_z,\operatorname{gr}^1v_z\rangle,"),
     J(r"=\langle \operatorname{gr}^0\underline{u}_z,\operatorname{gr}^0\underline{v}_z\rangle",
       r" +\langle \operatorname{gr}^1\underline{u}_z,\operatorname{gr}^1\underline{v}_z\rangle,")),
    "The left side < u_z,v_z > is not underlined in the print.")

add(147, "between the two cup-product displays",
    "the two formulas stand one under the other, the first ending with a comma; no 'et'",
    J(r"\]", "et", r"\["),
    "extra", "high",
    (J(r"\]", "et", r"\["), J(r"\]", r"\[")),
    "Word added by the TeX.")

add(147, "second cup-product display",
    "< u,v > = < gr^0 u , gr^0 v > + < gr^1 u , gr^1 v > .  (u, v underlined in the gr terms only)",
    J(r"=\langle \operatorname{gr}^0u,\operatorname{gr}^0v\rangle",
      r" +\langle \operatorname{gr}^1u,\operatorname{gr}^1v\rangle."),
    "underline", "high",
    (J(r"=\langle \operatorname{gr}^0u,\operatorname{gr}^0v\rangle",
       r" +\langle \operatorname{gr}^1u,\operatorname{gr}^1v\rangle."),
     J(r"=\langle \operatorname{gr}^0\underline{u},\operatorname{gr}^0\underline{v}\rangle",
       r" +\langle \operatorname{gr}^1\underline{u},\operatorname{gr}^1\underline{v}\rangle.")),
    "The left side < u,v > is not underlined in the print.")

add(147, "'tandis que gr^0L (resp. gr^1M) est concentré en x (resp. y)'",
    "tandis que gr^oL (resp. gr^1M) est concentré en x (resp. y)",
    r"tandis que $\operatorname{gr}^0L$ (resp. $\operatorname{gr}^1M$) est concentré",
    "misprint_in_print", "high", None,
    "gr^1M = j_!j^*M has zero fibre at y (same sentence); the part concentrated at y is gr^0M. The TeX keeps the "
    "printed reading.",
    corrected=r"$\operatorname{gr}^0M$")

add(147, "Lemme 2.3, label",
    "Lemme 2.3 - Sous les hypothèses de 1.1, ...",
    r"\begin{statement}{Lemme 2.3}  (renders 'Lemme 2.3.')",
    "punctuation", "high",
    (r"\begin{statement}{Lemme 2.3}", r"\begin{statement}{Lemme 2.3 -}"),
    LABEL_NOTE.replace("LABEL", "Lemme 2.3"))

add(147, "'concentrés au points fermés'",
    "de correspondances entre complexes concentrés au points fermés",
    "complexes concentrés aux points fermés",
    "misprint_in_print", "high",
    ("concentrés aux points", "concentrés au points"),
    "The print has 'au' for 'aux'; the TeX silently corrects it.",
    corrected="concentrés aux points")

add(147, "'la formule de Lefschetz pour les projections s → S , y → S'",
    "pour les projections s ⟶ S , y ⟶ S",
    r"pour les projections $s\to S$, $y\to S$",
    "misprint_in_print", "medium", None,
    "The reduced data have complexes on the closed points x and y, and the proof on p. 148 applies 'la formule "
    "de Lefschetz pour {x} → S , {y} → S'; s (the image of z in A) is a misprint for x. The TeX keeps the "
    "printed reading.",
    corrected=r"$x\to S$")

add(147, "'tels que A x_(X x_S Y) B soit réduit à un point fermé'",
    "A x_{(X x_S Y)} B  (the subscript in parentheses)",
    r"$A\times_{X\times_SY}B$",
    "formula", "high",
    (r"A\times_{X\times_SY}B", r"A\times_{(X\times_SY)}B"),
    "Parentheses round the subscript dropped by the TeX.")

add(147, "'L = h_{1*}L' , m = h_{2*}M''",
    "L = h_{1*}L' , m = h_{2*}M'",
    r"L=h_{1*}L',\quad m=h_{2*}M',\quad",
    "misprint_in_print", "high", None,
    "Lower-case m for M (L = h_{1*}L', M = h_{2*}M'); the TeX keeps the printed reading.",
    corrected=r"M=h_{2*}M'")

# ---------------- page 148 ----------------
add(148, "first line of the page",
    "h_1 : {x} ⟶ X et h_2 : {y} ⟶ Y désignant les inclusions canoniques.  (no 'où'; p. 147 ends "
    "'M' ∈ ob D_ctf({y}) ,')",
    r"où $h_1:\{x\}\to X$ et $h_2:\{y\}\to Y$ désignant",
    "extra", "high",
    (r"où $h_1:\{x\}\to X$", r"$h_1:\{x\}\to X$"),
    "Word added by the TeX.")

add(148, "'On a RΓ(X;L) = RΓ_c(X,L) = L_x'",
    "RΓ(X;L) = RΓ_c(X,L) = L_x  (semicolon)",
    r"\R\Gamma(X,L)=\R\Gamma_c(X,L)=L_x",
    "misprint_in_print", "high",
    (r"\Gamma(X,L)=\R\Gamma_c", r"\Gamma(X;L)=\R\Gamma_c"),
    "Semicolon typed for the comma (RΓ(X,L) everywhere else on the page); the TeX silently corrects it. The edit "
    "changes only that character.",
    corrected=r"\R\Gamma(X,L)")

add(148, "'(III 3.5 b)). D'autre part, si h = ...'",
    "the print runs on in the same line: '... le procédé de calcul (III 3.5 b)). D'autre part, si h = h_1 x_S h_2 ...'",
    "a blank line (new paragraph) before 'D'autre part, si'",
    "other", "high",
    (J("(III 3.5 b)).", "", "D'autre part, si"), "(III 3.5 b)). D'autre part, si"),
    "No paragraph break in the print.")

add(148, "'désignent les fibres de a , b en (x,y) (réduites chacune à un point)'",
    "en (x,y) (réduites chacune à un point), on a des isomorphismes canoniques",
    "en $(x,y)$, réduites chacune à un point, on a",
    "punctuation", "high",
    ("$(x,y)$, réduites chacune à un point, on a", "$(x,y)$ (réduites chacune à un point), on a"),
    "Parentheses dropped by the TeX.")

add(148, "'s'écrivent donc (de manière unique)'",
    "Les correspondances u et v s'écrivent donc (de manière unique)",
    "s'écrivent donc de manière unique",
    "punctuation", "high",
    ("s'écrivent donc de manière unique", "s'écrivent donc (de manière unique)"),
    "Parentheses dropped by the TeX.")

add(148, "Lemme 2.4, label",
    "Lemme 2.4 - Pour prouver 1.2, ...",
    r"\begin{statement}{Lemme 2.4}  (renders 'Lemme 2.4.')",
    "punctuation", "high",
    (r"\begin{statement}{Lemme 2.4}", r"\begin{statement}{Lemme 2.4 -}"),
    LABEL_NOTE.replace("LABEL", "Lemme 2.4"))

add(148, "the derived-functor R, pp. 148 and 150",
    "a plain typed R: RΓ(X,L), RΓ_c(Y,M) (p. 148), RΓ_A(T,...), RΓ(T-A,...), RΓ_z(B,...) (p. 150); never "
    "double-struck on these pages",
    r"\R\Gamma ..., and \R is \mathbb{R} again from Exposé III B on (s5.tex line 4362)",
    "font", "high", None,
    "8 occurrences on p. 148 and 12 on p. 150. Reported once as a convention, no per-occurrence edit: "
    r"\renewcommand{\R}{\mathrm{R}} for Exposé III B, as in Exposé III, if the other pages of III B agree.")

# ---------------- page 149 ----------------
add(149, "'images de a et b vérifient les mêmes hypothèses'",
    "b' : B' ⟶ Z , images de a et b vérifient  (no comma after b)",
    "images de $a$ et $b$, vérifient",
    "punctuation", "high",
    ("images de $a$ et $b$, vérifient", "images de $a$ et $b$ vérifient"),
    "Comma added by the TeX.")

add(149, "'d'où la première assertion. D'après 2.2 et 2.3'",
    "the print runs on in the same line: '< u,v > = < u',v' > , d'où la première assertion. D'après 2.2 et 2.3, "
    "on peut supposer'",
    "a blank line (new paragraph) before 'D'après 2.2 et 2.3'",
    "other", "high",
    (J("d'où la première assertion.", "", "D'après 2.2 et 2.3"), "d'où la première assertion. D'après 2.2 et 2.3"),
    "No paragraph break in the print.")

add(149, "the Künneth arrow (III 4.2.1)",
    "a^!P ⊗^L_Z b^!Q ⟶ c^!(P ⊗^L Q)  (a, b without primes)",
    r"a'{}^!P\lten_Z b'{}^!Q\longrightarrow c^!(P\lten Q)",
    "formula", "high",
    (r"a'{}^!P\lten_Z b'{}^!Q\longrightarrow c^!", r"a^!P\lten_Z b^!Q\longrightarrow c^!"),
    "Here a, b are the closed immersions A → Z, B → Z; the primed a', b' are the inclusions of {z}. The TeX adds "
    "the primes.")

add(149, "the base-change arrow ('flèche de changement de base')",
    "a^!P ⊗^L_Z b^!Q ⟶ a'^!b*P ⊗^L a'*b^!Q ,",
    r"a'{}^!P\lten_Z b'{}^!Q\longrightarrow a'{}^!b^*P\lten a^*b'{}^!Q,",
    "formula", "high",
    (r"a'{}^!P\lten_Z b'{}^!Q\longrightarrow a'{}^!b^*P\lten a^*b'{}^!Q,",
     r"a^!P\lten_Z b^!Q\longrightarrow a'{}^!b^*P\lten a'{}^*b^!Q,"),
    "No primes on the left side; on the right the prime is on a (a'*), not on b (b^!).")

add(149, "the projection arrows ('flèches de projection')",
    "a'^!b*P ⊗^L a'*b^!Q ⟶ a'^!(b*P ⊗^L b^!Q) ⟶ a'^!b^!(P ⊗^L Q))",
    J(r"a'{}^!b^*P\lten a^*b'{}^!Q", r" \longrightarrow a'{}^!(b^*P\lten b'{}^!Q)",
      r" \longrightarrow a'{}^!b'{}^!(P\lten Q))."),
    "formula", "high",
    (J(r"\lten a^*b'{}^!Q", r" \longrightarrow a'{}^!(b^*P\lten b'{}^!Q)", r" \longrightarrow a'{}^!b'{}^!(P"),
     J(r"\lten a'{}^*b^!Q", r" \longrightarrow a'{}^!(b^*P\lten b^!Q)", r" \longrightarrow a'{}^!b^!(P")),
    "The print has a'* (prime on a) and b^! without prime throughout; the TeX moves the prime from a to b.")

# ---------------- page 150 ----------------
add(150, "'du résultat plus précis suivant :'",
    "1.2 va donc découler du résultat plus précis suivant :",
    "du résultat plus précis suivant.",
    "punctuation", "high",
    ("plus précis suivant.", "plus précis suivant:"),
    "Colon in the print (written without the space, as the file does elsewhere, e.g. 'suivants:' p. 146).")

add(150, "Proposition 2.5, label",
    "Proposition 2.5 - Sous les hypothèses de 1.2, ...",
    r"\begin{statement}{Proposition 2.5}  (renders 'Proposition 2.5.')",
    "punctuation", "high",
    (r"\begin{statement}{Proposition 2.5}", r"\begin{statement}{Proposition 2.5 -}"),
    LABEL_NOTE.replace("LABEL", "Proposition 2.5"))

add(150, "2.6, 'le reste du n° 2'",
    "va occuper le reste du n° 2",
    "le reste du numéro 2",
    "word", "high",
    ("du numéro 2", r"du n\textsuperscript{o}~2"),
    "Abbreviation written out by the TeX; the file writes n° as n\\textsuperscript{o}~ elsewhere (III B "
    "introduction).")

add(150, "2.6, 'et les n°s 3 et 4'",
    "et les n°s 3 et 4 .",
    "et les numéros 3 et 4.",
    "word", "high",
    ("les numéros 3 et 4", r"les n\textsuperscript{o}s~3 et 4"),
    "Abbreviation written out by the TeX.")

add(150, "first isomorphism after 'les triangles de cohomologie relative'",
    "RΓ_A(T,(DL ⊗^L_S M)T)[1]  (no restriction bar before T)",
    r"\R\Gamma_A(T,(DL\lten_SM)T)[1],",
    "misprint_in_print", "high", None,
    "Restriction bar missing, cf. (DL ⊗ M)|T in Proposition 2.5 and (DL ⊗ M)|T-A on the left; the TeX keeps the "
    "printed reading.",
    corrected=r"\R\Gamma_A(T,(DL\lten_SM)|T)[1]")

exec(open("C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_146_150/extra_findings.py", encoding="utf-8").read())
F.sort(key=lambda d: d["page"])

# ---------------- checks ----------------
bad = 0
for d in F:
    for k in ("where", "scan", "tex", "note", "corrected"):
        v = d.get(k)
        if v and any(c in v for c in "\t\r\x0b\x0c\x08\x07"):
            print("CONTROL CHAR", d["page"], k, repr(v[:60]))
            bad += 1
    if d["fix"]:
        for k in ("old", "new"):
            v = d["fix"][k]
            if any(c in v for c in "\t\r\x0b\x0c\x08\x07"):
                print("CONTROL CHAR in fix", d["page"], k, repr(v[:60]))
                bad += 1

texts = {}
for p in sorted({d["page"] for d in F}):
    texts[p] = open(f"{RUN}/b146_150/page_{p}.tex", encoding="utf-8", newline="").read()
for d in F:
    if not d["fix"]:
        continue
    p = d["page"]
    old, new = d["fix"]["old"], d["fix"]["new"]
    n = texts[p].count(old)
    if n != 1:
        print("NOT UNIQUE/ABSENT", p, n, repr(old[:80]))
        bad += 1
        continue
    if "%%%%%%%%%%" in old:
        print("touches marker", p)
        bad += 1
    texts[p] = texts[p].replace(old, new, 1)

# misprint olds against the original text too (for information)
for d in F:
    if d["kind"] == "misprint_in_print" and d["fix"]:
        p = d["page"]
        t0 = open(f"{RUN}/b146_150/page_{p}.tex", encoding="utf-8", newline="").read()
        print("misprint old in original:", p, t0.count(d["fix"]["old"]), repr(d["fix"]["old"]))

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "total", len(F), "bad", bad)
if not bad:
    with open(f"{RUN}/findings_146_150.json", "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written")
