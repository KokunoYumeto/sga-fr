import json, pathlib
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_151_155.json")
C = "crops_151_155/"
F = []


def add(page, where, scan, tex, kind, conf, old, new, note=""):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}, "note": note}
    F.append(d)


BS = chr(92)
NL = chr(10)
RB = r"\mathbb{R}\underline{\Hom}"
RU = r"\mathrm R\underline{\Hom}"
MACRO = r"\RHom = \mathrm R\!\operatorname{Hom} (main.tex line 1847): plain R, Hom not underlined"
LB = BS + BS  # the LaTeX line break \\

# ---------------- page 151 ----------------
add(151, "proof of 7.2, display 'E -> Hom(Hom(E,F),F) .'",
    "both Hom underlined: Hom̲•(Hom̲•(E,F),F) (both scans)",
    r"E\longrightarrow\Hom^\bullet(\Hom^\bullet(E,F),F). (\Hom = \operatorname{Hom}, plain)",
    "underline", "high",
    r"E\longrightarrow\Hom^\bullet(\Hom^\bullet(E,F),F)",
    r"E\longrightarrow\underline{\Hom}^\bullet(\underline{\Hom}^\bullet(E,F),F)",
    r"\underline{\Hom} is the file's form (main.tex line 1939, pp. 135-136).")
add(151, "Définition 7.3, 'Nous poserons RHom(E,A) = E^v'",
    "ℝHom̲(E,A): double-struck R (doubled stem), Hom underlined (both scans; " + C + "w151_def73.png)",
    r"\(\RHom(E,A)=E^\vee\) (" + MACRO + ")",
    "font", "high",
    r"\(\RHom(E,A)=E^\vee\)", r"\(" + RB + r"(E,A)=E^\vee\)",
    r"The same edit underlines Hom. \mathbb{R}\underline{\Hom} as applied on pp. 116-118.")
add(151, "after 7.3, 'le foncteur RHom( ,A)'",
    "ℝHom̲: double-struck R, Hom underlined (both scans; " + C + "p151_foncteur.png, w151_foncteur.png)",
    r"\(\RHom(\,\cdot\,,A)\)",
    "font", "high",
    r"foncteur \(\RHom", r"foncteur \(" + RB,
    "Also underlines Hom. Independent of the next entry (adjacent texts, no overlap).")
add(151, "same formula, the argument place of 'RHom( ,A)'",
    "an empty place about three letters wide between '(' and ',A)': no dot, no letter (both scans; " + C + "p151_foncteur.png, w151_foncteur.png)",
    r"(\,\cdot\,,A)",
    "extra", "high",
    r"(\,\cdot\,,A)", r"(\quad,A)",
    "The TeX adds a centred dot. Where the typescript types a full stop as place-holder it was kept as '.' (pp. 89, 136, 141); here it has none.")
add(151, "after 7.3, '(resp. D(S)_parf (5.8.4.b)))'",
    "the second index 'parf' underlined (the notation of 5.8.4 b)); the first D(S)_parf of the sentence is plain (both scans)",
    r"\(\Dpx(S)_{\parf}\) (\parf = \operatorname{parf}, plain)",
    "underline", "high",
    r"\Dpx(S)_{\parf}", r"\Dpx(S)_{\underline{\mathrm{parf}}}",
    r"Form applied on p. 137 (main.tex line 3144).")
add(151, "Lemme 7.4, statement before the displays",
    "'Pour' and 'il existe des isomorphismes fonctoriels canoniques' underlined; the formulas and ' :' not (both scans)",
    r"no emphasis: the statement is in roman (Définition 7.3 above has \emph)",
    "underline", "high",
    r"Pour \(E\in\Ob\Dpx(S)\), \(F\in\Ob\Dpx^-(S)\), \(G\in\Ob\Dpx^+(S)\), il existe des isomorphismes fonctoriels canoniques",
    r"\emph{Pour \(E\in\Ob\Dpx(S)\), \(F\in\Ob\Dpx^-(S)\), \(G\in\Ob\Dpx^+(S)\), il existe des isomorphismes fonctoriels canoniques}",
    "Block form (volume decision); the colon stays outside.")
add(151, "Lemme 7.4, first display line",
    "RHom̲(E ⊗L F, G) ⥲ RHom̲(E, RHom̲(F,G)) , : a plain typed R, all three Hom underlined (both scans; " + C + "p151_cartan1.png, p151_cartan2.png)",
    r"\RHom three times (plain Hom); the TeX's first and second lines are identical",
    "underline", "high",
    r"\begin{aligned}" + NL + r"\RHom(E\otL F,G)&\xrightarrow{\sim}\RHom(E,\RHom(F,G)),",
    r"\begin{aligned}" + NL + RU + r"(E\otL F,G)&\xrightarrow{\sim}" + RU + r"(E," + RU + r"(F,G)),",
    r"The print tells the three lines apart by the underline: sheaf RHom̲ (line 1), global RHom (line 2, first two terms), Hom (line 3, first two terms). The R of these displays is a plain typed R, as \RHom has it.")
add(151, "Lemme 7.4, second display line, last term",
    "RHom(E ⊗L F, G) ⥲ RHom(E, RHom̲(F,G)) , : only the third Hom underlined (both scans; " + C + "p151_cartan2.png)",
    r"\RHom(E\otL F,G)&\xrightarrow{\sim}\RHom(E,\RHom(F,G)),",
    "underline", "high",
    r"\RHom(F,G))," + LB + NL + r"\Hom(E\otL",
    RU + r"(F,G))," + LB + NL + r"\Hom(E\otL",
    "The first two terms are the global RHom and stay plain.")
add(151, "Lemme 7.4, third display line, last term",
    "Hom(E ⊗L F, G) ⥲ Hom(E, RHom̲(F,G)) . : only RHom̲(F,G) underlined (both scans)",
    r"\Hom(E,\RHom(F,G)).",
    "underline", "high",
    r"\Hom(E,\RHom(F,G)).", r"\Hom(E," + RU + r"(F,G)).",
    "")

# ---------------- page 152 ----------------
add(152, "Lemme 7.5, statement before the display",
    "'Pour' and 'il existe un homomorphisme fonctoriel canonique' underlined; the formulas not (both scans)",
    "no emphasis",
    "underline", "high",
    r"Pour \(E\in\Ob\Dpx^-(S)\), \(F\in\Ob\Dpx^+(S)\), il existe un homomorphisme fonctoriel canonique",
    r"\emph{Pour \(E\in\Ob\Dpx^-(S)\), \(F\in\Ob\Dpx^+(S)\), il existe un homomorphisme fonctoriel canonique}",
    "Block form (volume decision).")
add(152, "Lemme 7.5, display 'E ⊗L RHom(E,F) -> F'",
    "a plain typed R, Hom underlined (both scans; " + C + "p152_l75disp.png, w152_l75disp.png)",
    r"E\otL\RHom(E,F)\longrightarrow F.",
    "underline", "high",
    r"E\otL\RHom(E,F)\longrightarrow", r"E\otL" + RU + r"(E,F)\longrightarrow",
    "Independent of the next entry.")
add(152, "Lemme 7.5, end of the display",
    "nothing after F (both scans; " + C + "p152_l75disp.png, w152_l75disp.png)",
    r"\longrightarrow F.",
    "punctuation", "high",
    "F." + NL + r"\]", "F" + NL + r"\]",
    "The TeX adds a full stop at the end of the display.")
add(152, "Proposition 7.6, 'Soient'",
    "'Soient' underlined; the formulas not (both scans)",
    "no emphasis: the whole proposition is in roman",
    "underline", "high",
    r"Soient \(E\in", r"\emph{Soient} \(E\in",
    "Word groups for this statement, so that the entry for the stop after D^+(S) stays independent; the statement continues in the next entries.")
add(152, "Proposition 7.6, 'F ∈ ob D^+(S) ,'",
    "the main scan has a pale speck between ')' and ',', smaller and lighter than the typed full stops of the page; the witness has nothing there (" + C + "p152_Fdot.png, w152_Fdot.png): no full stop is printed",
    r"\(F\in\Ob\Dpx^+(S)\).,",
    "punctuation", "medium",
    r"\(F\in\Ob\Dpx^+(S)\).,", r"\(F\in\Ob\Dpx^+(S)\),",
    "A speck (or the trace of an erased stop) taken for a full stop.")
add(152, "Proposition 7.6, 'Sous l'une des hypothèses suivantes'",
    "underlined (both scans)",
    "no emphasis",
    "underline", "high",
    r"Sous l'une des hypothèses suivantes", r"\emph{Sous l'une des hypothèses suivantes}",
    "")
add(152, "Proposition 7.6 i)",
    "'de tor-dimension finie' underlined, G and the comma not (both scans; " + C + "p152_items.png)",
    "no emphasis",
    "underline", "high",
    r"\(G\) de tor-dimension finie", r"\(G\) \emph{de tor-dimension finie}",
    "")
add(152, "Proposition 7.6 ii)",
    "'de tor-dimension finie et' underlined, the formulas not (both scans)",
    "no emphasis",
    "underline", "high",
    r"\(F\) de tor-dimension finie et", r"\(F\) \emph{de tor-dimension finie et}",
    "")
add(152, "Proposition 7.6, 'il existe un homomorphisme fonctoriel canonique' after the items",
    "underlined (both scans)",
    "no emphasis",
    "underline", "high",
    r"\end{enumerate}" + NL + "il existe un homomorphisme fonctoriel canonique",
    r"\end{enumerate}" + NL + r"\emph{il existe un homomorphisme fonctoriel canonique}",
    "")
add(152, "Proposition 7.6, display 'RHom(E,F) ⊗L G -> RHom(E, F ⊗L G) .'",
    "a plain typed R in both terms, both Hom underlined (both scans; " + C + "p152_76disp.png)",
    r"\RHom(E,F)\otL G ... \RHom(E,F\otL G). (plain Hom)",
    "underline", "high",
    r"\RHom(E,F)\otL G" + NL + r"  \longrightarrow" + NL + r"  \RHom(E,F\otL G)",
    RU + r"(E,F)\otL G" + NL + r"  \longrightarrow" + NL + "  " + RU + r"(E,F\otL G)",
    "")
add(152, "Proposition 7.6, 'Celui-ci est un isomorphisme quand E est parfait.'",
    "'Celui-ci est un isomorphisme quand' and 'est parfait' underlined; E and the full stop not (both scans)",
    "no emphasis",
    "underline", "high",
    r"Celui-ci est un isomorphisme quand \(E\) est parfait", r"\emph{Celui-ci est un isomorphisme quand \(E\) est parfait}",
    "End of the statement.")
add(152, "proof of 7.6, display 'E ⊗L RHom(E,F) ⊗L G -> F ⊗L G .'",
    "ℝ Hom̲(E,F): double-struck R, Hom underlined (both scans; " + C + "p152_proofdisp.png)",
    r"E\otL\RHom(E,F)\otL G (" + MACRO + ")",
    "font", "high",
    r"E\otL\RHom(E,F)\otL G", r"E\otL" + RB + r"(E,F)\otL G",
    "Also underlines Hom.")
add(152, "proof of 7.6, 'On applique le foncteur ⊗L G'",
    "the tensor sign with L over it, then G; nothing before the tensor sign (both scans; " + C + "p152_foncteur.png)",
    r"\(-\otL G\)",
    "extra", "high",
    r"\(-\otL G\)", r"\(\otL G\)",
    "The TeX adds the dash of the empty argument.")

# ---------------- page 153 ----------------
add(153, "Corollaire 7.7, 'Il existe, pour'",
    "'Il existe,' and 'pour' underlined; the formulas and 'et' not; then 'un isomorphisme fonctoriel' underlined (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    r"Il existe, pour", r"\emph{Il existe, pour}",
    "Word groups, so that the index entry of the same sentence stays independent.")
add(153, "Corollaire 7.7, 'E ∈ ob D(S)_parf'",
    "the index 'parf' underlined (both scans)",
    r"\Dpx(S)_{\mathrm{parf}}",
    "underline", "high",
    r"\Dpx(S)_{\mathrm{parf}}\) et", r"\Dpx(S)_{\underline{\mathrm{parf}}}\) et",
    "The notation of 5.8.4 b), as on p. 151 '(resp. D(S)_parf̲ (5.8.4.b)))'; also in the proof, 7.8, 7.9, 8.1 and 8.2.")
add(153, "Corollaire 7.7, 'un isomorphisme fonctoriel'",
    "underlined (both scans)",
    "no emphasis",
    "underline", "high",
    r"un isomorphisme fonctoriel", r"\emph{un isomorphisme fonctoriel}",
    "")
add(153, "Corollaire 7.7, display 'E^v ⊗L F ⥲ RHom(E,F) ,'",
    "ℝHom̲(E,F): double-struck R, Hom underlined (both scans; " + C + "p153_77disp.png)",
    r"\xrightarrow{\sim}\RHom(E,F) (" + MACRO + ")",
    "font", "high",
    r"\xrightarrow{\sim}\RHom(E,F)", r"\xrightarrow{\sim}" + RB + r"(E,F)",
    "Also underlines Hom. The arrow of this display has its head (unlike the three signs of the display in the proof of 7.8).")
add(153, "Corollaire 7.7, 'avec la notation de (7.3).'",
    "'avec la notation de' underlined, '(7.3).' not (both scans)",
    "no emphasis",
    "underline", "high",
    r"avec la notation de", r"\emph{avec la notation de}",
    "End of the statement.")
add(153, "proof of 7.7, 'que E^v ∈ ob D(S)_parf .'",
    "the index 'parf' underlined (both scans)",
    r"\Dpx(S)_{\mathrm{parf}}",
    "underline", "high",
    r"E^\vee\in\Ob\Dpx(S)_{\mathrm{parf}}", r"E^\vee\in\Ob\Dpx(S)_{\underline{\mathrm{parf}}}",
    "In the proof (roman text) the underline is the notation, not emphasis.")
add(153, "Corollaire 7.8, 'Soient'",
    "'Soient' underlined, the formula not (both scans)",
    "no emphasis: the statement is in roman",
    "underline", "high",
    r"7.8.} Soient", r"7.8.} \emph{Soient}",
    "Word groups, so that the index entry stays independent.")
add(153, "Corollaire 7.8, 'E, F ∈ ob D(S)_parf'",
    "the index 'parf' underlined (both scans); the sign ∈ is broken in both scans (physical, not reported)",
    r"\Dpx(S)_{\mathrm{parf}}",
    "underline", "high",
    r"E,F\in\Ob\Dpx(S)_{\mathrm{parf}}", r"E,F\in\Ob\Dpx(S)_{\underline{\mathrm{parf}}}",
    "")
add(153, "Corollaire 7.8, 'Il existe une flèche naturelle'",
    "underlined (both scans)",
    "no emphasis",
    "underline", "high",
    r"Il existe une flèche naturelle", r"\emph{Il existe une flèche naturelle}",
    "")
add(153, "Corollaire 7.8, display 'RHom(E,F) ⊗L RHom(F,E) -> A ,'",
    "both terms ℝHom̲: double-struck R, Hom underlined (both scans)",
    r"\RHom(E,F)\otL\RHom(F,E) (" + MACRO + ")",
    "font", "high",
    r"\RHom(E,F)\otL\RHom(F,E)", RB + r"(E,F)\otL" + RB + r"(F,E)",
    "Also underlines Hom.")
add(153, "Corollaire 7.8, 'qui est une \"dualité parfaite\", i.e. identifie modulo (7.4) chacun des complexes'",
    "underlined by word groups: 'qui est une', 'dualité parfaite' (inside the quotes), 'identifie modulo', 'chacun des complexes'; ', i.e.' and '(7.4)' not (both scans)",
    "no emphasis",
    "underline", "high",
    r"qui est une «~dualité parfaite~», i.e.\ identifie modulo (7.4) chacun des complexes",
    r"\emph{qui est une «~dualité parfaite~», i.e.\ identifie modulo (7.4) chacun des complexes}",
    "Block form up to the formulas, which have their own entry.")
add(153, "Corollaire 7.8, 'RHom(E,F) , RHom(F,E)' in the text",
    "both ℝHom̲: double-struck R, Hom underlined (both scans)",
    r"\(\RHom(E,F)\), \(\RHom(F,E)\)",
    "font", "high",
    r"\(\RHom(E,F)\), \(\RHom(F,E)\)", r"\(" + RB + r"(E,F)\), \(" + RB + r"(F,E)\)",
    "Also underlines Hom.")
add(153, "Corollaire 7.8, 'au dual de l'autre (au sens de (7.3)).'",
    "'au dual de l'autre' and 'au sens de' underlined; the parentheses, '(7.3)' and the full stop not (both scans)",
    "no emphasis",
    "underline", "high",
    r"au dual de l'autre (au sens de (7.3))", r"\emph{au dual de l'autre (au sens de (7.3))}",
    "End of the statement.")
add(153, "proof of 7.8, 'l'accouplement annoncé sur les RHom.'",
    "ℝ Hom̲: double-struck R, Hom underlined (both scans; " + C + "p153_lesRHom.png)",
    r"les \(\RHom\)",
    "font", "high",
    r"les \(\RHom\)", r"les \(" + RB + r"\)",
    "Also underlines Hom.")
add(153, "proof of 7.8, display, 'RHom(F^v ⊗L E , A)'",
    "double-struck R, Hom underlined (both scans; " + C + "p153_align.png)",
    r"\RHom(F^\vee\otL E,A)",
    "font", "high",
    r"\RHom(F^\vee\otL E", RB + r"(F^\vee\otL E",
    "Also underlines Hom. Independent of the sign entries below (no overlap).")
add(153, "proof of 7.8, display, 'RHom(F^v, E^v)'",
    "double-struck R, Hom underlined (both scans; " + C + "p153_align.png)",
    r"\RHom(F^\vee,E^\vee)",
    "font", "high",
    r"\RHom(F^\vee,E^\vee)", RB + r"(F^\vee,E^\vee)",
    "Also underlines Hom.")
add(153, "proof of 7.8, display, first sign (before (7.4))",
    "≃: a hand-drawn tilde over a straight stroke, no arrowhead (both scans; " + C + "p153_sim.png, w153_small.png); the arrow of the display of 7.7 on this page has its head",
    r"\xrightarrow{\sim}",
    "symbol", "high",
    r",A)&\xrightarrow{\sim}", r",A)&\simeq",
    "As the headless ≃ fixed on pp. 110 and 118. One entry per sign; the three are independent.")
add(153, "proof of 7.8, display, second sign (before (7.6))",
    "≃ without arrowhead, as the first (both scans)",
    r"\xrightarrow{\sim}",
    "symbol", "high",
    r"&\xrightarrow{\sim}F^{\vee\vee}", r"&\simeq F^{\vee\vee}",
    "")
add(153, "proof of 7.8, display, third sign (before (7.2))",
    "≃ without arrowhead, as the first (both scans)",
    r"\xrightarrow{\sim}",
    "symbol", "high",
    r"&\xrightarrow{\sim}F\otL E^\vee", r"&\simeq F\otL E^\vee",
    "")

# ---------------- page 154 ----------------
add(154, "Exercice 7.9, 'Soient E, F ∈ ob D(S)_parf'",
    "the index 'parf' underlined (both scans)",
    r"\Dpx(S)_{\mathrm{parf}}",
    "underline", "high",
    r"E,F\in\Ob\Dpx(S)_{\mathrm{parf}}", r"E,F\in\Ob\Dpx(S)_{\underline{\mathrm{parf}}}",
    "The notation of 5.8.4 b) (see p. 153).")
add(154, "8.1, 'Soit E ∈ ob D(S)_parf (5.8.4.b)).'",
    "the index 'parf' underlined (both scans)",
    r"\Dpx(S)_{\parf} (\parf = \operatorname{parf}, plain)",
    "underline", "high",
    r"\Dpx(S)_{\parf}", r"\Dpx(S)_{\underline{\mathrm{parf}}}",
    "")
add(154, "8.1, display 'τ : RHom(E,E) -> A ,'",
    "ℝ Hom̲(E,E): double-struck R, Hom underlined (both scans)",
    r"\tau:\RHom(E,E) (" + MACRO + ")",
    "font", "high",
    r"\tau:\RHom(E,E)", r"\tau:" + RB + r"(E,E)",
    "Also underlines Hom.")
add(154, "8.1, 'l'isomorphisme inverse de (7.7) RHom(E,E) ⥲ E^v ⊗L E'",
    "ℝ Hom̲(E,E): double-struck R, Hom underlined (both scans)",
    r"\(\RHom(E,E)\xrightarrow{\sim}E^\vee\otL E\)",
    "font", "high",
    r"(7.7) \(\RHom(E,E)", r"(7.7) \(" + RB + r"(E,E)",
    "Also underlines Hom.")
add(154, "'Appliquant à τ le foncteur H^o(U,.)'",
    "the empty argument is a typed full stop on the baseline: H^o(U,.) (both scans; " + C + "p154_H0dot.png)",
    r"\(H^0(U,\cdot)\)",
    "symbol", "medium",
    r"H^0(U,\cdot)", r"H^0(U,.)",
    "As the typed place-holder stops applied on pp. 89, 136, 141 (main.tex lines 1939, 3108, 3211).")
add(154, "'tenant compte du fait que H^o(U, RHom(E,E))'",
    "ℝ Hom̲(E,E): double-struck R, Hom underlined (both scans; " + C + "p154_H0RHom.png)",
    r"\(H^0(U,\RHom(E,E))\)",
    "font", "high",
    r"H^0(U,\RHom(E,E))", r"H^0(U," + RB + r"(E,E))",
    "Also underlines Hom. Hom_D(U)(E|U,E|U) after it is plain in the print, as in the TeX.")

# ---------------- page 155 ----------------
add(155, "start of page",
    "p. 155 begins '8.1.1. Si E = A, Tr_A|U : Hom(A|U,A|U) -> H^o(U,A) n'est autre que l'iso-'; p. 154 ends with '... qui découlent immédiatement de la définition.' and its footnote (both scans)",
    r"the line '\textbf{8.1.1.} Si \(E=A\), \(\Tr_{A|U}:...\) n'est' is the last line of page_154.tex (under the folio-154 marker); page_155.tex begins 'autre que'",
    "marker", "high", None, None,
    r"Page 155 really begins with the heading 8.1.1. Move the folio-155 marker above it: python -I move_marker.py 6 155 " + '"' + r"\textbf{8.1.1.}" + '"' + r" --before (simulated in memory on both layers: '... de la définition.', blank line, the marker, '\textbf{8.1.1.} Si ... n'est', 'autre que l'isomorphisme ...').")
add(155, "8.1.1, display 'e |-> Σ <e, x_i^v> x_i ,'",
    "a bare sum sign, nothing under it (both scans; " + C + "p155_mapsto.png)",
    r"\sum_i\langle e,x_i^\vee\rangle x_i",
    "formula", "high",
    r"\sum_i\langle e,", r"\sum\langle e,",
    "The TeX adds the summation index.")
add(155, "8.1.1, 'la trace correspondante est Σ <x_i , x_i^v>'",
    "a bare sum sign (both scans; " + C + "p155_sum1.png)",
    r"\(\sum_i\langle x_i,x_i^\vee\rangle\)",
    "formula", "high",
    r"\(\sum_i\langle x_i,", r"\(\sum\langle x_i,",
    "The TeX adds the summation index.")
add(155, "8.1.2, display 'Tr_E|U(u) = Σ (-1)^i Tr_E^i|U(u^i) .'",
    "a bare sum sign (both scans; " + C + "p155_812disp.png)",
    r"\Tr_{E|U}(u)=\sum_i(-1)^i\Tr_{E^i|U}(u^i).",
    "formula", "high",
    r"(u)=\sum_i(-1)^i", r"(u)=\sum(-1)^i",
    "The TeX adds the summation index.")
add(155, "proof of 8.1.2, 'une section de H^o(E^v ⊗ E)'",
    "H underlined (H̲^o, the cohomology sheaf) (both scans; " + C + "p155_H0.png)",
    r"\(H^0(E^\vee\otimes E)\)",
    "underline", "high",
    r"\(H^0(E^\vee\otimes E)\)", r"\(\underline{H}^0(E^\vee\otimes E)\)",
    "The H^o(U,...) of sections on pp. 154-155 are plain in the print, as in the TeX.")
add(155, "proof of 8.1.2, 'Explicitant la flèche (7.5) E^v ⊗ E -> A'",
    "a filled tensor sign with no L over it (both scans; " + C + "p155_75.png, w155_75.png)",
    r"\(E^\vee\otL E\to A\)",
    "symbol", "high",
    r"(7.5) \(E^\vee\otL E\to A\)", r"(7.5) \(E^\vee\otimes E\to A\)",
    "The same paragraph has the plain tensor sign in H^o(E^v ⊗ E) and x_ij^v ⊗ x_ij (E strictly perfect); the arrow (7.5) of 8.1 on p. 154 has the L.")
add(155, "proof of 8.1.2, display, first sum 'Σ (-1)^i <x_ij, x_ij^v>'",
    "a bare sum sign (both scans; " + C + "p155_cqfd.png)",
    r"\sum_{i,j}(-1)^i",
    "formula", "high",
    r"\sum_{i,j}(-1)^i", r"\sum(-1)^i",
    "The TeX adds the summation indices.")
add(155, "proof of 8.1.2, display, second sum 'Σ (-1)^i Tr_E^i|U(u^i) , cqfd.'",
    "a bare sum sign (both scans; " + C + "p155_cqfd.png)",
    r"\sum_i(-1)^i\Tr_{E^i|U}(u^i),",
    "formula", "high",
    r"\sum_i(-1)^i\Tr_{E^i|U}(u^i),", r"\sum(-1)^i\Tr_{E^i|U}(u^i),",
    "The TeX adds the summation index.")
add(155, "8.2, 'Soient E, F ∈ ob D(S)_parf'",
    "the index 'parf' underlined (both scans)",
    r"\Dpx(S)_{\mathrm{parf}}",
    "underline", "high",
    r"E,F\in\Ob\Dpx(S)_{\mathrm{parf}}", r"E,F\in\Ob\Dpx(S)_{\underline{\mathrm{parf}}}",
    "The notation of 5.8.4 b), as in 7.8.")
add(155, "8.2, display 'γ : RHom(E,F) ⊗L RHom(F,E) -> A .'",
    "both terms ℝ Hom̲: double-struck R, Hom underlined (both scans; " + C + "p155_last.png)",
    r"\gamma:\RHom(E,F)\otL\RHom(F,E) (" + MACRO + ")",
    "font", "high",
    r"\gamma:\RHom(E,F)\otL\RHom(F,E)", r"\gamma:" + RB + r"(E,F)\otL" + RB + r"(F,E)",
    "Also underlines Hom.")
add(155, "8.2, 'u ∈ H^o(U, RHom(E,F))'",
    "ℝ Hom̲(E,F): double-struck R, Hom underlined (both scans; " + C + "p155_last.png)",
    r"\(u\in H^0(U,\RHom(E,F))\)",
    "font", "high",
    r"u\in H^0(U,\RHom(E,F))", r"u\in H^0(U," + RB + r"(E,F))",
    "Also underlines Hom.")
add(155, "8.2, 'v ∈ H^o(U, RHom(F,E))'",
    "ℝ Hom̲(F,E): double-struck R, Hom underlined (both scans; " + C + "p155_last.png)",
    r"\(v\in H^0(U,\RHom(F,E))\)",
    "font", "high",
    r"v\in H^0(U,\RHom(F,E))", r"v\in H^0(U," + RB + r"(F,E))",
    "Also underlines Hom.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
