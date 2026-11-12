import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:/Users/user/Documents/sga_scan_check_20261105/run_5/'
BDIR = RUN + 'b126_130/'
OUT = RUN + 'findings_126_130.json'

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, corrected=None, note=''):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


R_NOTE = ("Exposé III's statement environment prints the label as given (no full stop), as 'Théorème 4.4 -' (p. 102) "
          "and 'Corollaire 4.5 -' (p. 108).")
EMPH = "\\emph is this file's command for the print's underline in Exposé III (statements of pp. 84-95)."

# ---------------------------------------------------------------- page 126
add(126, "label of Théorème 6.7",
    "'Théorème 6.7 - Soient, ...': 'Théorème' underlined, the number, then a typewriter dash; the statement run in",
    "\\begin{statement}{Théorème 6.7}: no dash", "punctuation", "high",
    r"\begin{statement}{Théorème 6.7}", r"\begin{statement}{Théorème 6.7 -}", note=R_NOTE)
add(126, "statement of 6.7, first line: 'Soient, pour i = 1,2, f_i : X_i -> Y_i un S-morphisme propre,'",
    "underlined: 'Soient', 'pour', 'un', 'morphisme propre' (not 'S-'); the commas and the formulas not",
    "no underline", "underline", "high",
    r"Soient, pour $i=1,2$, $f_i:X_i\to Y_i$ un $S$-morphisme propre,",
    r"\emph{Soient}, \emph{pour} $i=1,2$, $f_i:X_i\to Y_i$ \emph{un} $S$-\emph{morphisme propre},",
    note="The whole statement of 6.7 is underlined word by word, the formulas, numbers and most punctuation left plain, "
         "as the statements of pp. 84-95; " + EMPH + " Eight more underline edits below (none overlaps another edit).")
add(126, "statement of 6.7: 'les projections. Soit d'autre part un cube 4.4.0 à faces horizontales cartésiennes, avec'",
    "underlined: 'les projections', 'Soit' + 'd'autre part un cube' (one rule across the line break), "
    "'à faces horizontales cartésiennes', 'avec'; the full stop, 4.4.0 and the comma not",
    "no underline", "underline", "high",
    r"les projections. Soit d'autre part un cube 4.4.0 à faces horizontales cartésiennes, avec",
    r"\emph{les projections}. \emph{Soit d'autre part un cube} 4.4.0 \emph{à faces horizontales cartésiennes}, \emph{avec}")
add(126, "statement of 6.7: 'propres, et c', c'' (resp. d', d'') de tor-dimension finie aux points au-dessus de c(C) (resp. d(D)) . On pose'",
    "underlined: 'propres', 'et', both 'resp' (not the parenthesis, not the full stop), "
    "'de tor-dimension finie aux points au-dessus' + 'de' (across the line break), 'On pose'",
    "no underline", "underline", "high",
    r"propres, et $c'$, $c''$ (resp. $d'$, $d''$) de tor-dimension finie aux points au-dessus de $c(C)$ (resp. $d(D)$). On pose",
    r"\emph{propres}, \emph{et} $c'$, $c''$ (\emph{resp}. $d'$, $d''$) \emph{de tor-dimension finie aux points au-dessus de} $c(C)$ (\emph{resp}. $d(D)$). \emph{On pose}")
add(126, "statement of 6.7: 'On pose c'_i = p_ic', c''_i = p_ic'', d'_i = q_id', d''_i = p_id''.'",
    "'d''_i = p_i d''' (p, as for c'_i and c''_i; d'_i = q_i d' just before)",
    "$d_i''=p_id''$ (the printed reading)", "misprint_in_print", "high",
    corrected=r"$d_i''=q_id''$",
    note="The TeX keeps the printed reading. d'' is a morphism D'' -> Y (the right column of (6.7.1) is built from d', d'' "
         "over Y), so its components are q_i d'', like d'_i = q_i d'.")
add(126, "statement of 6.7: 'Soient enfin L_i ∈ ob D(X_i)_parf/S . On suppose les couples'",
    "underlined: 'Soient enfin', 'On suppose les couples'",
    "no underline", "underline", "high",
    r"Soient enfin $L_i\in\operatorname{ob}D(X_i)_{\mathrm{parf}/S}$. On suppose les couples",
    r"\emph{Soient enfin} $L_i\in\operatorname{ob}D(X_i)_{\mathrm{parf}/S}$. \emph{On suppose les couples}")
add(126, "statement of 6.7: '... tor-indépendants sur S , et X_i et Y_i de tor-dimension finie sur S . On a alors un carré commutatif'",
    "underlined: 'tor-indépendants sur', 'et', 'et', 'de tor-dimension finie' + 'sur' (across the line break), "
    "'On a alors un carré commutatif'; S, X_i, Y_i, the comma and the full stop not",
    "no underline", "underline", "high",
    r"tor-indépendants sur $S$, et $X_i$ et $Y_i$ de tor-dimension finie sur $S$. On a alors un carré commutatif",
    r"\emph{tor-indépendants sur} $S$, \emph{et} $X_i$ \emph{et} $Y_i$ \emph{de tor-dimension finie sur} $S$. \emph{On a alors un carré commutatif}")
add(126, "(6.7.1), top row, second factor 'f_*c''_*RHom(c''_2^*L_2,c''_1^!L_1)'",
    "no rule under this RHom (clean paper); the other four RHom of the square have Hom underlined",
    "c''_*\\uRHom(c_2''{}^*L_2,c_1''{}^!L_1): silent correction", "misprint_in_print", "high",
    r"c''_*\uRHom(c_2''{}^*L_2", r"c''_*\mathrm{R}\mathrm{Hom}(c_2''{}^*L_2",
    corrected=r"c''_*\uRHom(c_2''{}^*L_2",
    note="The typist left out the underline, as the top vertex of (3.4.1) on p. 93 (logged the same way). "
         "\\mathrm{R}\\mathrm{Hom} is Exposé III's \\uRHom without the underline. Diplomatic layer only.")
add(126, "statement of 6.7 after (6.7.1): 'où M_i = f_{i*}L_i , (3) est donné par 6.6.2, (1) est déduit de 6.6.2 par application de f_* et composition avec la flèche canonique'",
    "underlined: 'où', 'est donné par', 'est déduit de', 'par application' + 'de' (across the line break), "
    "'et composition avec la flèche canonique'; the formulas, (3), (1) and the numbers not",
    "no underline", "underline", "high",
    r"où $M_i=f_{i*}L_i$, $(3)$ est donné par 6.6.2, $(1)$ est déduit de 6.6.2 par application de $f_*$ et composition avec la flèche canonique",
    r"\emph{où} $M_i=f_{i*}L_i$, $(3)$ \emph{est donné par} 6.6.2, $(1)$ \emph{est déduit de} 6.6.2 \emph{par application de} $f_*$ \emph{et composition avec la flèche canonique}")
add(126, "statement of 6.7: '(2) est produit tensoriel des flèches 6.5.4 relatives aux faces contenant f , et (4) est composé de l'isomorphisme de dualité 6.1.1 et de la flèche définie par la flèche canonique'",
    "underlined: 'est produit tensoriel des flèches', 'relatives aux faces contenant', 'et', "
    "'est composé de l'isomorphisme de dualité', 'et de la flèche définie par la flèche' + 'canonique' (across the line break); "
    "(2), 6.5.4, f, (4), 6.1.1 not",
    "no underline", "underline", "high",
    r"$(2)$ est produit tensoriel des flèches 6.5.4 relatives aux faces contenant $f$, et $(4)$ est composé de l'isomorphisme de dualité 6.1.1 et de la flèche définie par la flèche canonique",
    r"$(2)$ \emph{est produit tensoriel des flèches} 6.5.4 \emph{relatives aux faces contenant} $f$, \emph{et} $(4)$ \emph{est composé de l'isomorphisme de dualité} 6.1.1 \emph{et de la flèche définie par la flèche canonique}",
    note="Its old ends at 'canonique'; the display edit that follows starts at the line break after it (no overlap).")
DISP126 = ("the arrow runs in the text: 'par la flèche / canonique Rd'_*O_D' ⊗ Rd''_*O_D'' -> f_*(Rc'_*O_C' ⊗ Rc''_*O_C'') "
           "(adjointe du produit tensoriel ...' on one text line")
add(126, "statement of 6.7, the canonical arrow Rd'_*O_D' ⊗ Rd''_*O_D'' -> f_*(Rc'_*O_C' ⊗ Rc''_*O_C'') (opening)",
    DISP126, "a display \\[ ... \\] between 'la flèche canonique' and '(adjointe'", "other", "high",
    "\n" + r"\[" + "\n" + r"\R d'_*\cO_{D'}", r" $\R d'_*\cO_{D'}",
    note="Display against inline formula (as pp. 117, 120, 122-124). Edit 1 of 2: apply together with the next edit "
         "(closing $); either alone breaks the LaTeX.")
add(126, "statement of 6.7, the same arrow (closing), before '(adjointe du produit tensoriel'",
    DISP126, "...\\R c''_*\\cO_{C''}) + line break + \\] + line break + (adjointe", "other", "high",
    r"\cO_{C''})" + "\n" + r"\]" + "\n" + "(", r"\cO_{C''})$ (",
    note="Edit 2 of 2; apply together with the previous edit.")
add(126, "statement of 6.7: '(adjointe du produit tensoriel des flèches \"de changement de base\" f^*Rd'_*O_D' -> ...'",
    "'des flèches \"de changement de base\"' with typewriter double quotes; 'adjointe du produit tensoriel' + "
    "'des flèches \"de changement de base\"' underlined (across the line break, closing quote included; "
    "the opening parenthesis not)",
    "des flèches de changement de base (no quotes, no underline)", "punctuation", "high",
    r"adjointe du produit tensoriel des flèches de changement de base",
    r"\emph{adjointe du produit tensoriel des flèches ``de changement de base''}",
    note="Missing quotes; the same edit sets the underline of this last run of the statement (the quotes lie inside it, "
         "so one edit). Quote form `` '' as elsewhere in Exposé III (``ch. b.'' p. 93).")

# ---------------------------------------------------------------- page 127
DISP127 = ("the arrow runs in the text: 'par la flèche / canonique Rd'_*O_D' ⊗ Rd''_*O_D'' -> f_*(Rc'_*O_C' ⊗ Rc''_*O_C'') "
           "citée dans 6.7 . Quand' on one text line")
add(127, "after (6.7.3): 'et de la flèche induite par la flèche canonique Rd'_*O_D' ⊗ Rd''_*O_D'' -> f_*(...) citée dans 6.7' (opening)",
    DISP127, "a display \\[ ... \\] between 'la flèche canonique' and 'citée dans 6.7'", "other", "high",
    "canonique\n" + r"\[" + "\n", r"canonique $",
    note="Display against inline formula. Edit 1 of 2: apply together with the next edit (closing $).")
add(127, "same arrow (closing), before 'citée dans 6.7'",
    DISP127, "...\\R c''_*\\cO_{C''}) + line break + \\] + line break + citée", "other", "high",
    r"\cO_{C''})" + "\n" + r"\]" + "\n" + "citée", r"\cO_{C''})$ citée",
    note="Edit 2 of 2; apply together with the previous edit.")
add(127, "6.8: 'Soient f = X -> S un morphisme lisse purement de dimension relative N'",
    "'f = X ---> S': an equals sign where the colon of a map is meant (clear)",
    "$f=X\\to S$ (the printed reading)", "misprint_in_print", "high",
    corrected=r"$f:X\to S$",
    note="The TeX keeps the printed reading. Every other map of the passage is written with a colon (i : Y -> X, g = fi).")
add(127, "6.8: '... dans une terminologie équivalente ((8 III 1), (SGA 6 VIII 1)) une immersion fermée'",
    "'(8 III 1)': the reference number without its square brackets",
    "((8 III 1), (SGA~6 VIII 1)) (the printed reading)", "misprint_in_print", "medium",
    corrected=r"(([8] III 1), (SGA~6 VIII 1))",
    note="The TeX keeps the printed reading. The same work is cited '([8] III 9)' and '([8] III 7.2)' on this page and "
         "'([8] III 9 R6)' on p. 128.")
add(127, "6.8: 'On associe alors à Y un élement'",
    "'élement': the second e typed plain (clean, no accent)",
    "un élément", "misprint_in_print", "high",
    r"un élément", r"un élement", corrected=r"un élément",
    note="Typing error of the print; the TeX silently corrects it. The fix restores the printed reading (diplomatic layer only).")
add(127, "after (6.8.1): 'appelé classe de cohomologie associée à Y , défini ...'",
    "'classe de cohomologie associée à' underlined; Y not",
    "\\emph{classe de cohomologie associée à $Y$}", "underline", "high",
    r"\emph{classe de cohomologie associée à $Y$}", r"\emph{classe de cohomologie associée à} $Y$",
    note="The rule stops before the formula, as 'correspondances (cohomologiques) de ... à ...' (pp. 89, 124).")
add(127, "(6.8.2), left-hand side 'Ext^i_{O_X}(O_Y , Ω^d_X/S)'",
    "Ext underlined (the sheaf Ext; the global Ext of (6.8.1) and (6.8.3) is not)",
    "\\Ext^i_{\\cO_X} (no underline)", "underline", "high",
    r"\Ext^i_{\cO_X}", r"\underline{\Ext}^i_{\cO_X}",
    note="Written like the \\underline{\\Hom} of the same display. A small stray tick above the superscript i is not part of the text.")
add(127, "(6.8.2), first case 'O si i ≠ d'",
    "'0 si i ≠ d': the word si, no comma after 0 and none at the end of the line",
    "0,& i\\ne d,\\\\ (no si; two commas)", "missing", "high",
    r"0,& i\ne d,\\", r"0& \text{si } i\ne d\\",
    note="One edit for the missing word and the two added commas. \\text{si } as elsewhere in the file (\\text{si }p\\text{ est impair}).")
add(127, "(6.8.2), second case 'Hom(Λ^d N_Y/X , Ω^d_X/S ⊗ O_Y) si i = d ,' (the exterior power)",
    "a hand-drawn capital Λ, the same sign as the exterior powers of pp. 128-130",
    "\\bigwedge^d N_{Y/X}", "symbol", "medium",
    r"\bigwedge^d N_{Y/X}", r"\Lambda^d N_{Y/X}",
    note="pp. 128-130 (Λ^{d∨}N, Λ^{m∨}N, Λ^{n∨}N, Λ^{m+n∨}N) are transcribed \\Lambda; only the two of p. 127 are \\bigwedge.")
add(127, "(6.8.2), second case, end: '... ⊗ O_Y) si i = d ,'",
    "'si i = d ,': the word si; no comma between the parenthesis and si",
    "...\\otimes\\cO_Y),& i=d,", "missing", "high",
    r"\cO_Y),& i=d,", r"\cO_Y)& \text{si } i=d,",
    note="One edit for the missing word and the added comma; the final comma is printed.")
add(127, "(6.8.3), 'H^o(Y,Hom(Λ^d N_Y/X , Ω^d_X/S ⊗ O_Y))'",
    "a hand-drawn capital Λ",
    "\\bigwedge^dN_{Y/X}", "symbol", "medium",
    r"\bigwedge^dN_{Y/X}", r"\Lambda^dN_{Y/X}",
    note="As in (6.8.2).")
add(127, "every cℓ of pp. 127-130; examples: (6.8.1) cℓ_X/S(Y) p. 127, (6.8.5) Res_Y/S(y cℓ_X/S(Y)) p. 128, (6.9.4) p. 130",
    "cℓ: a typed c followed by a hand-drawn script ℓ",
    "\\cl = \\operatorname{cl} (a roman l)", "font", "high",
    note="Convention of the transcription (macro \\cl; already reported for pp. 96-97 and 110), not listed per occurrence: "
         "1 on p. 127, 3 on p. 128, 10 on p. 130. One decision for the volume (e.g. c\\ell in the diplomatic layer).")

# ---------------------------------------------------------------- page 128
add(128, "top of the page",
    "p. 128 begins 'La différentielle d_X/S : O_X -> Ω^1_X/S induit une application O_Y-linéaire'; "
    "(6.8.3) is the last line of p. 127",
    "the folio-128 marker stands inside the equation environment of (6.8.3), before its \\end{equation}; "
    "page_128.tex begins '\\end{equation}'", "marker", "high",
    note="Page 128 really begins at 'La différentielle' (the \\end{equation} closes the last display of p. 127). "
         "Exact fix: python -I move_marker.py 5 128 \"La différentielle\" (forward search, no --before; simulated in memory "
         "on both layers: the marker then stands on its own line after '\\end{equation}' and the blank line, before "
         "'La différentielle'). Text not moved.")
add(128, "'induit une application O_Y-linéaire d_X/S ⊗ 1 : N_Y/X -> Ω^1_X/S ⊗ O_Y . La puissance extérieure'",
    "the arrow runs in the text (it opens the second line, followed by '. La puissance extérieure d-ième ...'); "
    "the full stop stands after the formula",
    "a display \\[ ... .\\] between 'linéaire' and 'La puissance'", "other", "high",
    "linéaire\n" + r"\[" + "\n" + r"d_{X/S}\otimes 1:N_{Y/X}\longrightarrow \Omega^1_{X/S}\otimes\OO_Y." + "\n" + r"\]" + "\nLa puissance",
    r"linéaire $d_{X/S}\otimes 1:N_{Y/X}\longrightarrow \Omega^1_{X/S}\otimes\OO_Y$. La puissance",
    note="Display against inline formula; one self-contained edit.")
add(128, "'est une section globale, sur Y , de Λ^{d∨}N_Y/S ⊗ Ω^d_X/S'",
    "'N_Y/S' (index Y/S)",
    "$\\Lambda^d N_{Y/S}^{\\vee}\\otimes\\Omega^d_{X/S}$ (the printed reading)", "misprint_in_print", "medium",
    corrected=r"\Lambda^d N_{Y/X}^{\vee}",
    note="The TeX keeps the printed reading. N is the conormal sheaf N_Y/X = I/I^2 of Y in X (p. 127, 6.8.2); the d-th "
         "exterior power of N_Y/X -> Ω^1_X/S ⊗ O_Y is a section of Λ^d N_Y/X^∨ ⊗ Ω^d_X/S, and Y is not embedded in S "
         "(6.9 writes N_A/Z, N_B/Z, N_C/Z). Printed Y/S three times on this page (this and the next two findings). "
         "Corrected edition only.")
add(128, "'dont l'image dans Ext^d(O_Y,Ω^d_X/S) par l'isomorphisme 6.8.3 est par définition la classe 6.8.1'",
    "'6.8.3' (clear, two full stops)",
    "l'isomorphisme 6.83 est", "number", "high",
    r"l'isomorphisme 6.83 est", r"l'isomorphisme 6.8.3 est",
    note="The TeX has the two references of this page swapped: here the print has 6.8.3 and the TeX 6.83; further down "
         "(misprint finding '6.83 et de la flèche') the print has 6.83 and the TeX 6.8.3. The two edits do not overlap.")
add(128, "'Soit ω ∈ H^o(Y,Λ^{d∨}N_Y/S ⊗ Ω^d_X/S)'",
    "'N_Y/S'",
    "H^0(Y,\\Lambda^d N_{Y/S}^{\\vee}\\otimes\\Omega^d_{X/S}) (the printed reading)", "misprint_in_print", "medium",
    corrected=r"\Lambda^d N_{Y/X}^{\vee}",
    note="As the previous N_Y/S. The TeX keeps the printed reading.")
DISP128 = ("the arrow runs in the text: 'O_Y -> g^!O_S(= Λ^{d∨}N_Y/S ⊗ Ω^d_X/S) , donc, par adjonction, comme un homomorphisme' "
           "on one text line")
add(128, "'on peut voir ω comme un homomorphisme O_Y -> g^!O_S(= ...) , donc, par adjonction,' (opening)",
    DISP128, "a display \\[ ... ,\\] between 'comme un homomorphisme' and 'donc, par adjonction'", "other", "high",
    "homomorphisme\n" + r"\[" + "\n" + r"\OO_Y\longrightarrow", r"homomorphisme $\OO_Y\longrightarrow",
    note="Display against inline formula. Edit 1 of 2: apply together with the next edit (closing $). The two edits leave "
         "out the misprinted N_Y/S between them.")
add(128, "same formula: 'g^!O_S(= Λ^{d∨}N_Y/S ⊗ Ω^d_X/S)'",
    "'N_Y/S'",
    "g^!\\OO_S(=\\Lambda^d N_{Y/S}^{\\vee}\\otimes\\Omega^d_{X/S}) (the printed reading)", "misprint_in_print", "medium",
    corrected=r"\Lambda^d N_{Y/X}^{\vee}",
    note="As the first N_Y/S of the page. The TeX keeps the printed reading.")
add(128, "same formula (closing), before 'donc, par adjonction'",
    DISP128, "...\\Omega^d_{X/S}), + line break + \\] + line break + donc", "other", "high",
    r"\Omega^d_{X/S})," + "\n" + r"\]" + "\ndonc", r"\Omega^d_{X/S})$, donc",
    note="Edit 2 of 2; apply together with the previous edit. The comma stands after the formula, as printed.")
add(128, "'On définit le résidu (relatif à g) de ω comme la section de O_S'",
    "'résidu' underlined",
    "le résidu (no underline)", "underline", "high",
    r"le résidu (relatif", r"le \emph{résidu} (relatif",
    note="\\emph is this file's command for the print's underline in Exposé III (\\emph{formule de Lefschetz-Verdier} p. 127).")
add(128, "'l'image de ω par le composé de l'isomorphisme 6.83 et de la flèche canonique'",
    "'6.83' (one full stop, clear)",
    "l'isomorphisme 6.8.3 et de la flèche: silent correction", "misprint_in_print", "high",
    r"6.8.3 et de la", r"6.83 et de la", corrected=r"6.8.3 et de la",
    note="Typing error of the print (the isomorphism (6.8.3)); the TeX silently corrects it, while it writes 6.83 for the "
         "correctly printed 6.8.3 above (number finding). Diplomatic layer only.")
add(128, "'et de la flèche canonique Ext^N_{O_X}(O_Y,Ω^N_X/S) -> H^N(X,Ω^N_X/S) . Quand f est propre'",
    "the arrow runs in the text (line 'canonique Ext^N ... -> H^N(X,Ω^N_X/S) . Quand f est propre, il découle ...'); "
    "the full stop stands after the formula",
    "a display \\[ ... .\\] between 'la flèche canonique' and 'Quand'", "other", "high",
    "canonique\n" + r"\[" + "\n" + r"\Ext^N_{\OO_X}(\OO_Y,\Omega^N_{X/S})\longrightarrow H^N(X,\Omega^N_{X/S})." + "\n" + r"\]" + "\nQuand",
    r"canonique $\Ext^N_{\OO_X}(\OO_Y,\Omega^N_{X/S})\longrightarrow H^N(X,\Omega^N_{X/S})$. Quand",
    note="Display against inline formula; one self-contained edit (no overlap with the 6.83 misprint fix before it or "
         "the 'propre' underline after it).")
add(128, "'Quand f est propre, il découle de la transitivité'",
    "'propre' underlined; the comma not",
    "est propre, (no underline)", "underline", "high",
    r"est propre, il découle", r"est \emph{propre}, il découle")
add(128, "(6.8.6) 'g^*F -> g^!F = g^*F ⊗ g^!O_S'",
    "a plain typed L above the tensor sign",
    "g^*F\\otimes^{\\LL}g^!\\OO_S (\\LL = \\mathbf L, set as a right superscript)", "font", "high",
    r"g^*F\otimes^{\LL}g^!\OO_S", r"g^*F\overset{\mathrm{L}}{\otimes}g^!\OO_S",
    note="The Exposé III form of the derived tensor (handled globally, 11 Nov) is \\overset{\\mathrm{L}}{\\otimes}; this "
         "\\otimes^{\\LL} and the one of (6.8.7) are the only two left in Exposé III.")
add(128, "(6.8.7) 'g_*g^*F = F ⊗ g_*O_Y -> F' (printed at the top of p. 129)",
    "a plain typed L above the tensor sign",
    "F\\otimes^{\\LL}g_*\\OO_Y", "font", "high",
    r"F\otimes^{\LL}g_*\OO_Y", r"F\overset{\mathrm{L}}{\otimes}g_*\OO_Y",
    note="As (6.8.6). Printed on p. 129; filed here because (6.8.7) sits under the folio-128 marker until that marker is "
         "moved (p. 129 marker finding): apply before the move, or look for it on p. 129 afterwards. The letter after g^* is "
         "darker than its neighbours (an F typed over an E); read as F, as the TeX.")

# ---------------------------------------------------------------- page 129
add(129, "top of the page",
    "p. 129 begins with the display (6.8.7) 'g_*g^*F = F ⊗ g_*O_Y -> F', then 'définie par Tr_Y/S : g_*O_Y -> O_S .'; "
    "p. 128 ends 'donnée par le produit par cℓ_X/S(Y) correspond par adjonction à la flèche'",
    "the display (6.8.7) stands in page_128.tex; the folio-129 marker follows its \\end{equation}", "marker", "high",
    note="Page 129 really begins at the \\begin{equation} of (6.8.7). Exact fix (bash): python -I move_marker.py 5 129 "
         r"$'\\begin{equation}\n\\tag{6.8.7}' --before (the anchor is '\begin{equation}', a line break, '\tag{6.8.7}'; "
         "simulated in memory on both layers: the marker then stands between '... correspond par adjonction à la flèche' "
         "and '\\begin{equation}'). The display agrees with the print apart from its tensor (p. 128 finding).")
add(129, "6.9: '(l'indice part signifie \"parfait au sens absolu\"'",
    "'part' (t, clear)",
    "l'indice parf: silent correction", "misprint_in_print", "high",
    r"l'indice parf", r"l'indice part", corrected=r"l'indice parf",
    note="Typing error of the print (the index is parf, as in D(X)_parf just before); the TeX silently corrects it. "
         "Diplomatic layer only.")
DISP129 = "the formula runs in the text: 'Ω^1_X/S = Ω^1_Z/Y ⊕ Ω^1_Z/X , d'où, pour tout entier r , une décomposition' on one text line"
add(129, "'et une décomposition Ω^1 = Ω^1_Z/Y ⊕ Ω^1_Z/X , d'où, pour tout entier r' (opening)",
    DISP129, "a display \\[ ... ,\\] between 'et une décomposition' and 'd'où'", "other", "high",
    "et une décomposition\n" + r"\[" + "\n", r"et une décomposition $",
    note="Display against inline formula. Edit 1 of 2: apply together with the edit 'closing' below. The misprint fix "
         "between them does not overlap either.")
add(129, "same formula, left-hand side",
    "'Ω^1_X/S = Ω^1_Z/Y ⊕ Ω^1_Z/X' (X/S, clear)",
    "\\Omega^1_{Z/S}: silent correction", "misprint_in_print", "high",
    r"\Omega^1_{Z/S}", r"\Omega^1_{X/S}", corrected=r"\Omega^1_{Z/S}",
    note="The decomposition is that of Ω^1 of Z = X ×_S Y (the summands are Ω^1_Z/Y and Ω^1_Z/X; (6.9.0) has Ω^r_Z/S). "
         "The TeX silently corrects; diplomatic layer only.")
add(129, "same formula (closing), before 'd'où, pour tout entier'",
    DISP129, "...\\Omega^1_{Z/X}, + line break + \\] + line break + d'où", "other", "high",
    r"\Omega^1_{Z/X}," + "\n" + r"\]" + "\nd'où", r"\Omega^1_{Z/X}$, d'où",
    note="Edit 2 of 2; apply together with the opening edit. The comma stands after the formula, as printed.")

# ---------------------------------------------------------------- page 130
add(130, "first line of the page: 'La section Tr(u_C v_C) = Tr(v_C u_C) , où ...'",
    "'La' with a capital L (clear); the sentence continues 'notons <u,v> ∈ H^o(C,O_C)' at the foot of p. 129",
    "la (lower case): silent correction", "misprint_in_print", "high",
    "la\nsection", "La\nsection", corrected="la\nsection",
    note="Slip of the print at the page turn; the TeX silently corrects it. Diplomatic layer only.")
add(130, "label of Théorème 6.10",
    "'Théorème 6.10 - Sous les hypothèses ...': 'Théorème' underlined, the number, then a typewriter dash",
    "\\begin{statement}{Théorème 6.10}: no dash", "punctuation", "high",
    r"\begin{statement}{Théorème 6.10}", r"\begin{statement}{Théorème 6.10 -}", note=R_NOTE)
add(130, "statement of 6.10, first line: 'Sous les hypothèses du premier alinéa de 6.9, soient'",
    "underlined: 'Sous les hypothèses du premier alinéa de', 'soient'; '6.9,' not",
    "no underline", "underline", "high",
    r"Sous les hypothèses du premier alinéa de 6.9, soient",
    r"\emph{Sous les hypothèses du premier alinéa de} 6.9, \emph{soient}",
    note="The statement of 6.10 is underlined word by word, as that of 6.7 (p. 126); " + EMPH +
         " Two more edits below; the statement continues on p. 131.")
add(130, "statement of 6.10: ', et considérons la correspondance cohomologique u^! (resp. v^!) de L à M (resp. M à L ) à support dans A (resp. B) déduite de u (resp. v) par composition avec la trace'",
    "underlined: 'et considérons la correspondance cohomologique', each 'resp', 'de', 'à', 'à', 'à support dans', "
    "'déduite de', 'par composition avec la trace'; the letters, u^!, v^! and the parentheses not",
    "no underline", "underline", "high",
    r", et considérons la correspondance cohomologique $u^!$ (resp. $v^!$) de $L$ à $M$ (resp. $M$ à $L$) à support dans $A$ (resp. $B$) déduite de $u$ (resp. $v$) par composition avec la trace",
    r", \emph{et considérons la correspondance cohomologique} $u^!$ (\emph{resp}. $v^!$) \emph{de} $L$ \emph{à} $M$ (\emph{resp}. $M$ \emph{à} $L$) \emph{à support dans} $A$ (\emph{resp}. $B$) \emph{déduite de} $u$ (\emph{resp}. $v$) \emph{par composition avec la trace}")
add(130, "statement of 6.10: '(resp. b_{1*}b_1^*L -> L ) (6.8.7), et l'homomorphisme (u^!)_* : f_*L -> g_*M (resp. ...) déduit de u^! (resp. v^!) par image directe'",
    "underlined: each 'resp', 'et l'homomorphisme', 'déduit de', 'par image directe'; (6.8.7), (6.5.5) and the formulas not",
    "no underline", "underline", "high",
    r"(resp. $b_{1*}b_1^*L\to L$) (6.8.7), et l'homomorphisme $(u^!)_*:f_*L\to g_*M$ (resp. $(v^!)_*:g_*M\to f_*L$) déduit de $u^!$ (resp. $v^!$) par image directe",
    r"(\emph{resp}. $b_{1*}b_1^*L\to L$) (6.8.7), \emph{et l'homomorphisme} $(u^!)_*:f_*L\to g_*M$ (\emph{resp}. $(v^!)_*:g_*M\to f_*L$) \emph{déduit de} $u^!$ (\emph{resp}. $v^!$) \emph{par image directe}")

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for p in range(126, 131):
    pages[p] = open(BDIR + 'page_%03d.tex' % p, encoding='utf-8', newline='').read()
    assert '\r' not in pages[p]
for i, f in enumerate(F):
    if f['fix'] is None:
        continue
    old = f['fix']['old']
    n = pages[f['page']].count(old)
    if n != 1:
        ok = False
        print('NOT UNIQUE', n, f['page'], repr(old[:70]))
    if '%%%%%%%%%%' in old:
        ok = False
        print('MARKER IN OLD', f['page'])
# sequential application on a copy (the order of the list), checks the olds still match and the result balances
for p in range(126, 131):
    t = pages[p]
    for f in F:
        if f['page'] != p or f['fix'] is None:
            continue
        old, new = f['fix']['old'], f['fix']['new']
        if t.count(old) != 1:
            ok = False
            print('SEQ FAIL', p, repr(old[:70]), t.count(old))
            continue
        t = t.replace(old, new)
    body = t.split('\n', 2)[2]
    print(p, 'braces', body.count('{') - body.count('}'), 'dollars', body.count('$') % 2,
          'emph', body.count('\\emph{'), '\\[', body.count('\\['), '\\]', body.count('\\]'))
print('all olds unique:', ok, '| findings:', len(F))
for p in range(126, 131):
    nm = sum(1 for f in F if f['page'] == p and f['kind'] == 'misprint_in_print')
    nn = sum(1 for f in F if f['page'] == p and f['kind'] != 'misprint_in_print')
    print(p, nn, '/', nm)
if ok and '--write' in sys.argv:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print('written', OUT)
