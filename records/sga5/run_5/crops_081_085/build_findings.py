"""Write findings_081_085.json and check every fix: each "old" must occur exactly once in its page file at the
moment it is applied (fixes applied in the listed order, page by page). Nothing else is written.
usage: python -I build_findings.py"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent
PAGES = HERE.parent / "b081_085"
OUT = HERE.parent / "findings_081_085.json"
N = "\n"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


RH = r"""Exposé III types the derived-functor R plain and underlines only Hom"""

# ---------------------------------------------------------------- page 81
add(81, "heading of § 2, top of the page",
    "'2. Fonctorialité de RHom et produits tensoriels externes.': the number 2. and a full stop after externes (the rule runs from 2. to externes.)",
    r"""\section*{Fonctorialité de \texorpdfstring{$\uRHom$}{RHom} et produits tensoriels externes} (no number, no full stop)""",
    "number", "high",
    {"old": r"""\section*{Fonctorialité de \texorpdfstring{$\uRHom$}{RHom} et produits tensoriels externes}""",
     "new": r"""\section*{2. Fonctorialité de \texorpdfstring{$\uRHom$}{RHom} et produits tensoriels externes.}"""},
    r"""As the § 1 heading of p. 76, now '\section*{1. Notations et rappels de formules de Künneth.}'. The underline is the accepted \section* setting.""")
add(81, "2.1, 'La flèche canonique évidente au niveau des complexes f*Hom˙(P,Q) ⟶ Hom˙(f*P,f*Q)'",
    "Hom˙ twice: the typed word Hom underlined, with a raised dot",
    r"""\mathcal Hom^{\bullet} twice (a script H followed by math-italic om, no underline)""",
    "font", "high",
    {"old": r"""f^{*}\mathcal Hom^{\bullet}(P,Q)\longrightarrow\mathcal Hom^{\bullet}(f^{*}P,f^{*}Q)""",
     "new": r"""f^{*}\underline{\Hom}^{\bullet}(P,Q)\longrightarrow\underline{\Hom}^{\bullet}(f^{*}P,f^{*}Q)"""},
    r"""\underline{\Hom} is this file's form for the underlined Hom (Exposé III). Two adjacent signs in one edit. The print runs the formula into the text (the TeX's display is layout, not reported). Same sign on p. 82.""")
add(81, "end of 2.1, 'RHom(u,v) est l'isomorphisme de \"dualité triviale\"'",
    "'isomorphisme de \"dualité triviale\"' underlined, from isomorphisme through the closing quote; l' not underlined",
    r"""est l'isomorphisme de ``dualité triviale'' (no underline)""",
    "underline", "high",
    {"old": r"""l'isomorphisme de ``dualité triviale''""",
     "new": r"""l'\emph{isomorphisme de ``dualité triviale''}"""},
    r"""\emph is this file's command for the print's underline in Exposé III (\emph{flèche d'évaluation} p. 82).""")

# ---------------------------------------------------------------- page 82
add(82, "start of the page",
    "p. 82 begins '2.2 Soient X un S-schéma. Rappelons que ...'; p. 81 ends with (2.1.6)",
    r"""\subsection*{2.2} is the last line of page_081.tex (both layers); the folio-82 marker follows it""",
    "marker", "high", None,
    r"""Page 82 really begins at '\subsection*{2.2}'. Exact fix: python -I move_marker.py 5 82 '\subsection*{2.2}' --before (single quotes; simulated in memory on both layers: the marker then stands on its own line after the blank line that follows (2.1.6), directly before \subsection*{2.2}).""")
add(82, "2.2, the complex-level evaluation arrow 'Hom˙(E,F) ⊗ E ⟶ F , f ⊗ x ⟼ f(x) .'",
    "Hom˙: the typed word Hom underlined, with a raised dot (the mark over the o is a speck)",
    r"""\mathcal Hom^{\bullet}(E,F) (script H, italic om, no underline)""",
    "font", "high",
    {"old": r"""\mathcal Hom^{\bullet}(E,F)\otimes E""",
     "new": r"""\underline{\Hom}^{\bullet}(E,F)\otimes E"""},
    "As p. 81.")
add(82, "label of Proposition 2.3",
    "'Proposition 2.3 - La flèche ...': Proposition underlined, then the number and a typewriter dash, the statement run in",
    r"""\subsection*{Proposition 2.3} (no dash)""",
    "punctuation", "high",
    {"old": r"""\subsection*{Proposition 2.3}""", "new": r"""\subsection*{Proposition 2.3 -}"""},
    r"""Exposé III label form, as '\subsection*{Proposition 1.7.4 -}' (p. 79).""")
add(82, "statement of Proposition 2.3",
    "'La flèche 2.2.4 est un isomorphisme' underlined; the rule stops before the full stop",
    "La flèche 2.2.4 est un isomorphisme. (no underline)",
    "underline", "high",
    {"old": "La flèche 2.2.4 est un isomorphisme.", "new": r"""\emph{La flèche 2.2.4 est un isomorphisme}."""},
    "As the statement of Proposition 1.7.4 (p. 79).")

# ---------------------------------------------------------------- page 83
add(83, "square (2), label of the upper horizontal arrow",
    "2.2.3 (clear)",
    r"""\arrow[r,"2.2.3"] (as printed)""",
    "misprint_in_print", "high", None,
    r"""The upper arrow RHom(f_1!A_U1,F_1) ⊗^L_S RHom(f_2!A_U2,F_2) ⟶ RHom(f_!A_U,F) is the external arrow 2.2.4 that Proposition 2.3 asserts to be an isomorphism (E_i = f_i!A_Ui, E = E_1 ⊗^L_S E_2); 2.2.3 is the arrow on a single scheme. The TeX keeps the printed reading; the corrected layer already has 2.2.4 (Codex SGA-SRC-001845).""",
    corrected=r"""\arrow[r,"2.2.4"]""")
add(83, "square (2), the two vertical arrows",
    "beside each vertical arrow a hand-drawn tilde over a short bar (≃), as the sign of the lower arrow of (4); the arrows of (1) and (3) carry a plain tilde",
    r"""\arrow[d,"\sim"'] and \arrow[d,"\sim"] (a plain tilde)""",
    "symbol", "high",
    {"old": r"""\arrow[d,"\sim"'] & \uRHom(f_{!}A_U,F) \arrow[d,"\sim"]""",
     "new": r"""\arrow[d,"\simeq"'] & \uRHom(f_{!}A_U,F) \arrow[d,"\simeq"]"""},
    "Two labels on one line in one edit; the edit also applies to the corrected layer (it does not touch the 2.2.3 label).")
add(83, "square (4), lower left corner 'f_1*F_1 ⊗ f_2*F_2'",
    "the L above the tensor sign but no S below it (clean paper; every other external product of (2) and (4) has its S)",
    r"""f_1^{*}F_1\overset{\mathrm{L}}{\otimes}_{S}f_2^{*}F_2""",
    "misprint_in_print", "high",
    {"old": r"""{\otimes}_{S}f_2^{*}F_2""", "new": r"""{\otimes}f_2^{*}F_2"""},
    r"""f_1*F_1 and f_2*F_2 live on U_1 and U_2: their product is the external product over S, as in the upper corner of (4) and the lower left corner of (2). The TeX silently supplies the S; the fix restores the printed reading (diplomatic layer only).""",
    corrected=r"""{\otimes}_{S}f_2^{*}F_2""")
add(83, "square (4), lower horizontal arrow",
    "a hand-drawn tilde over a short bar (≃) above the arrow",
    r"""\arrow[r,"\sim"]""",
    "symbol", "high",
    {"old": r"""\arrow[r,"\sim"]""", "new": r"""\arrow[r,"\simeq"]"""},
    "As the vertical arrows of (2).")
add(83, "2.4, end of the definitions 'Q = Q_1 ⊗^L_S Q_2 :'",
    "a colon after Q_2 (the diagram (2.4.0) follows)",
    "Q=Q_1\\overset{\\mathrm{L}}{\\otimes}_{S}Q_2. (a full stop)",
    "punctuation", "high",
    {"old": r"""{\otimes}_{S}Q_2.""", "new": r"""{\otimes}_{S}Q_2 :"""},
    "The print sets the four definitions inline on one line (the TeX's display is layout, not reported).")
add(83, "2.4, between the definitions and (2.4.0)",
    "no words: 'Q = Q_1 ⊗^L_S Q_2 :' is followed directly by '(2.4.0)' and the diagram",
    "Considérons le diagramme",
    "extra", "high",
    {"old": r"""\]""" + N + "Considérons le diagramme", "new": r"""\]"""},
    "Words added by the transcription. The diagram (2.4.0) that follows is printed on this page but stands under the folio-84 marker (see p. 84).")

# ---------------------------------------------------------------- page 84
add(84, "start of the page",
    "p. 84 begins 'Donnons-nous (u_1,v_1) ∈ Hom_{f_1}^(3,4)((E_1,F_1) , (P_1,Q_1)) ,'; the diagram (2.4.0) is printed at the foot of p. 83",
    r"""page_084.tex begins with \begin{equation}\tag{2.4.0} ... \end{equation} (both layers); 'Donnons-nous' follows it""",
    "marker", "high", None,
    r"""Page 84 really begins at 'Donnons-nous'. Exact fix: python -I move_marker.py 5 84 'Donnons-nous' (the anchor's first occurrence after the marker; simulated in memory on both layers: the marker then stands between \end{equation} of (2.4.0) and 'Donnons-nous'). The (2.4.0) edit below is listed under p. 84, where the TeX has it now.""")
add(84, "end of the diagram (2.4.0) (printed at the foot of p. 83)",
    "a round full stop far to the right, just below the line of the labels (P_2,Q_2), (E_2,F_2)",
    r"""no punctuation after the tikzpicture""",
    "punctuation", "medium",
    {"old": r"""node[below] {$f_2$} (Y2);""" + N + r"""\end{tikzpicture}}""",
     "new": r"""node[below] {$f_2$} (Y2);""" + N + r"""\end{tikzpicture}}\,."""},
    "Same size and shape as the typed full stop that ends 2.5.1, but set a little below the last line; medium for that reason. The 'old' is on p. 83 once the folio-84 marker is moved.")
add(84, "square 2.4.1, label of the right vertical arrow '(u_1 ⊗_S E_2 , v_1 ⊗^L_S F_2)'",
    "no L above the first tensor sign (clean paper at the height of the second label's L); the second tensor sign has its L",
    r"""(u_1\overset{\mathrm{L}}{\otimes}_S E_2,\,v_1\overset{\mathrm{L}}{\otimes}_S F_2)""",
    "misprint_in_print", "high",
    {"old": r"""{(u_1\overset{\mathrm{L}}{\otimes}_S E_2""", "new": r"""{(u_1\otimes_S E_2"""},
    "Every other tensor sign of 2.4.1 is the derived one, with its L; the typist left this L out. The TeX silently supplies it; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"""{(u_1\overset{\mathrm{L}}{\otimes}_S E_2""")
add(84, "end of the square 2.4.1",
    "a comma at the right of the lower row",
    "no punctuation",
    "punctuation", "high",
    {"old": r"""{\otimes}_S F_2) \arrow[l,""", "new": r"""{\otimes}_S F_2), \arrow[l,"""},
    r"""The comma goes into the last cell, as the file does for (2) on p. 83 ('f_{*}f^{*}F,').""")
add(84, "'dans la vérification de la formule de Lefschetz-Verdier.'",
    "Lefschetz-Verdier with a typed hyphen",
    "Lefschetz--Verdier (an en dash)",
    "punctuation", "high",
    {"old": "Lefschetz--Verdier", "new": "Lefschetz-Verdier"},
    "En dash added by the transcription.")
add(84, "label of Proposition 2.5",
    "'Proposition 2.5 - Le diagramme ...': Proposition underlined, then the number and a typewriter dash, the statement run in",
    r"""\subsection*{Proposition 2.5} (no dash)""",
    "punctuation", "high",
    {"old": r"""\subsection*{Proposition 2.5}""", "new": r"""\subsection*{Proposition 2.5 -}"""},
    "Exposé III label form, as Proposition 1.7.4 and 2.3.")
add(84, "statement of Proposition 2.5",
    "underlined: 'Le diagramme 2.5.1 ci-après' | 'où le carré de droite est déduit de' + '2.4.1 par application de' (across the line break) | 'au sens de 2.1.3 et 2.1.5' | 'est commutatif'; not underlined: the two commas, RHom (only its Hom, as everywhere), the final colon",
    "no underline",
    "underline", "high",
    {"old": r"""Le diagramme 2.5.1 ci-après, où le carré de droite est déduit de 2.4.1 par application de $\uRHom$ au sens de 2.1.3 et 2.1.5, est commutatif :""",
     "new": r"""\emph{Le diagramme 2.5.1 ci-après}, \emph{où le carré de droite est déduit de 2.4.1 par application de} $\uRHom$ \emph{au sens de 2.1.3 et 2.1.5}, \emph{est commutatif} :"""},
    "")
add(84, "diagram 2.5.1",
    "no equation number: the diagram starts at the left margin, nothing beside it (the statement names it 'Le diagramme 2.5.1 ci-après')",
    r"""\begin{equation}\tag{2.5.1}""",
    "extra", "high",
    {"old": r"""\begin{equation}\tag{2.5.1}""", "new": r"""\begin{equation}\notag"""},
    r"""Number added by the transcription. \notag (amsmath) in an equation environment suppresses the number (tested); one edit, the \end{equation} stays.""")
add(84, "diagram 2.5.1, upper left diagonal RHom(E,F) — RHom(E_1 ⊗^L_S P_2 , F_1 ⊗^L_S Q_2)",
    "a plain ruled line with no arrowhead at its lower end (crisp end, clean paper; the other three diagonals have drawn heads)",
    r"""\draw[->] (D) -- (E);""",
    "misprint_in_print", "medium",
    {"old": r"""\draw[->] (D) -- (E);""", "new": r"""\draw (D) -- (E);"""},
    "The arrow goes from RHom(E,F) to RHom(E_1 ⊗ P_2, F_1 ⊗ Q_2) (RHom of the (2,1) arrow of 2.4.1); the draughtsman left the head out. The TeX silently draws it; the fix restores the printed reading (diplomatic layer only). Medium: an omitted head rather than a misprint proper.",
    corrected=r"""\draw[->] (D) -- (E);""")
add(84, "end of diagram 2.5.1",
    "a full stop at the right of the lower row, after RHom(P,Q)",
    "no punctuation",
    "punctuation", "high",
    {"old": r"""\draw[->] (F) -- (G);""" + N + r"""\end{tikzpicture}}""",
     "new": r"""\draw[->] (F) -- (G);""" + N + r"""\end{tikzpicture}}\,."""},
    "")

# ---------------------------------------------------------------- page 85
add(85, "'on voit qu'il suffit de prouver les cas particuliers suivants de 2.5 :'",
    "a colon after 2.5 (Corollaire 2.6.1 follows)",
    "suivants de 2.5. (a full stop)",
    "punctuation", "high",
    {"old": "suivants de 2.5.", "new": "suivants de 2.5 :"},
    "")
add(85, "label of Corollaire 2.6.1",
    "'Corollaire 2.6.1. - Soient ...': Corollaire underlined, then the number with a full stop and a typewriter dash, the statement run in",
    r"""\subsection*{Corollaire 2.6.1} (no full stop, no dash)""",
    "punctuation", "high",
    {"old": r"""\subsection*{Corollaire 2.6.1}""", "new": r"""\subsection*{Corollaire 2.6.1. -}"""},
    "Exposé III label form ('Proposition 1.7.4 -'), here with the print's full stop after the number.")
add(85, "statement of Corollaire 2.6.1, first two lines",
    "underlined: Soient | un | morphisme (not S-) | un | schéma (not S-) | le morphisme déduit de | par le changement de base; the formulas, S' and f are not underlined",
    "no underline",
    "underline", "high",
    {"old": r"""Soient $f:X\to Y$ un $S$-morphisme, $S'$ un $S$-schéma, $f':X'\to Y'$ le morphisme déduit de $f$ par le changement de base $S'\to S$""",
     "new": r"""\emph{Soient} $f:X\to Y$ \emph{un} $S$-\emph{morphisme}, $S'$ \emph{un} $S$-\emph{schéma}, $f':X'\to Y'$ \emph{le morphisme déduit de} $f$ \emph{par le changement de base} $S'\to S$"""},
    "")
add(85, "statement of Corollaire 2.6.1, '(resp. Hom_f^(3,4)((E,F) , (P,Q)) )'",
    "resp underlined (not the parenthesis, not the full stop)",
    "(resp. (no underline)",
    "underline", "high",
    {"old": r"""(resp. $\Hom_f^{(3,4)}""", "new": r"""(\emph{resp}. $\Hom_f^{(3,4)}"""},
    "")
add(85, "statement of Corollaire 2.6.1, last sentence",
    "underlined: 'On a alors un' + 'carré commutatif' (across the line break) | 'où les flèches verticales sont de type' | 'au-dessus de'; not underlined: the comma, the 1, f' and the colon",
    "no underline",
    "underline", "high",
    {"old": r"""On a alors un carré commutatif, où les flèches verticales sont de type~1 au-dessus de $f'$ :""",
     "new": r"""\emph{On a alors un carré commutatif}, \emph{où les flèches verticales sont de type}~1 \emph{au-dessus de} $f'$ :"""},
    "")
add(85, "2.6.1.1, upper right corner 'RHom(E ⊗^L_S P' , F' ⊗^L_S Q')'",
    "F' with a prime (clear)",
    r"""F'\overset{\mathrm{L}}{\otimes}_SQ' (as printed)""",
    "misprint_in_print", "high", None,
    r"""The upper arrow is 2.2.4 for (E,F) on X and (P',Q') on S': its target is RHom(E ⊗^L_S P', F ⊗^L_S Q'); no F' is defined. The TeX keeps the printed reading; the corrected layer already has F.""",
    corrected=r"""\uRHom(E\overset{\mathrm{L}}{\otimes}_SP',F\overset{\mathrm{L}}{\otimes}_SQ')""")
add(85, "'Examinons d'abord le cas où (u,v) est le type (2,1).'",
    "est le type (clear: 'le', as in 'le cas' on the same line)",
    "est de type $(2,1)$",
    "misprint_in_print", "high",
    {"old": "est de type $(2,1)$", "new": "est le type $(2,1)$"},
    "'est de type (2,1)', as 'est de type (3,4)' below and in 2.4. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
    corrected="est de type $(2,1)$")
add(85, "unnumbered square after 'le carré', label of the left vertical arrow '2.1.1 ⊗^L 2.1.1'",
    "an L above the tensor sign",
    r"""{2.1.1\otimes 2.1.1} (no L)""",
    "formula", "high",
    {"old": r"""{2.1.1\otimes 2.1.1}""", "new": r"""{2.1.1\overset{\mathrm{L}}{\otimes} 2.1.1}"""},
    "Applies to both layers.")
add(85, "same square, upper right corner 'f*RHom(E ⊗^L L , F ⊗^L M))', first tensor product",
    "E ⊗ L: a capital L after the tensor sign (crisp, as the L of 'f*RHom(L,M)'), the L above the sign",
    r"""E\overset{\mathrm{L}}{\otimes}1 (the digit 1)""",
    "formula", "high",
    {"old": r"""{\otimes}1,""", "new": r"""{\otimes}L,"""},
    r"""The digit 1 is printed in the LOWER right corner ('f*(E ⊗ 1)', next findings); the TeX has the two readings swapped. Diplomatic layer only: the corrected layer reads P\otimes^LL, here and needs only the form change (P\overset{\mathrm{L}}{\otimes}L,).""")
add(85, "same corner, second tensor product 'F ⊗^L M'",
    "the L above the tensor sign",
    r"""F\otimes^LM (a math-italic L as a superscript to the right)""",
    "font", "high",
    {"old": r"""\otimes^LM) """, "new": r"""\overset{\mathrm{L}}{\otimes}M) """},
    r"""Not converted to the Exposé III form \overset{\mathrm{L}}{\otimes} (three such signs left in Exposé III, all in this square). Applies to both layers. Apply before the next edit.""")
add(85, "same corner, end 'M))'",
    "two closing parentheses after M (only one is open)",
    "M) (one parenthesis)",
    "misprint_in_print", "high",
    {"old": r"""M) \arrow[d,"2.1.1"]""", "new": r"""M)) \arrow[d,"2.1.1"]"""},
    "A stray parenthesis. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only). Listed after the form edit of the same corner, whose 'old' it shares in part.",
    corrected=r"""M) \arrow[d,"2.1.1"]""")
add(85, "same square, lower right corner 'RHom(f*(E ⊗^L 1),f*(F ⊗ M))', first tensor product",
    "the L above the tensor sign",
    r"""E\otimes^LL (a math-italic L as a superscript)""",
    "font", "high",
    {"old": r"""\otimes^LL)""", "new": r"""\overset{\mathrm{L}}{\otimes}L)"""},
    "Not converted to the Exposé III form. Applies to both layers. Apply before the next edit.")
add(85, "same corner, 'f*(E ⊗^L 1)'",
    "the digit 1 after the tensor sign (flag and foot, as the 1 of 2.1.1)",
    "L (silently corrected; the TeX's 1 stands in the upper right corner instead)",
    "misprint_in_print", "high",
    {"old": "L),f^{*}(", "new": "1),f^{*}("},
    "The second factor is L (as in the upper right corner and in the evaluation arrows): 1 is a typing error for L. The fix restores the printed reading (diplomatic layer only); listed after the form edit of the same sign.",
    corrected="L),f^{*}(")
add(85, "same corner, second tensor product 'f*(F ⊗ M)'",
    "a plain tensor sign without L (next finding); this edit only brings the TeX's sign to the Exposé III form, for the corrected layer",
    r"""F\otimes^LM (a math-italic L as a superscript)""",
    "font", "high",
    {"old": r"""\otimes^LM))""", "new": r"""\overset{\mathrm{L}}{\otimes}M))"""},
    "Form edit for the corrected layer (Exposé III form); applies to both layers. Must precede the next edit, whose 'old' it creates.")
add(85, "same corner, 'f*(F ⊗ M)'",
    "no L above this tensor sign (clean paper; the first sign of the corner has its L)",
    r"""F\otimes^LM (with L)""",
    "misprint_in_print", "high",
    {"old": r"""(F\overset{\mathrm{L}}{\otimes}M))""", "new": r"""(F\otimes M))"""},
    "The derived tensor product, as in the upper right corner; the typist left the L out. The TeX silently supplies it; the fix restores the printed reading (diplomatic layer only). Its 'old' is the text after the preceding form edit (it does not occur before it).",
    corrected=r"""(F\overset{\mathrm{L}}{\otimes}M))""")
add(85, "same square, all four corners",
    "E,F where the objects of Y are meant: f*RHom(E,F) ⊗ f*RHom(L,M) ; f*RHom(E ⊗ L , F ⊗ M)) ; RHom(f*E,f*F) ⊗ RHom(f*L,f*M) ; RHom(f*(E ⊗ 1),f*(F ⊗ M))",
    "E,F (as printed)",
    "misprint_in_print", "high", None,
    "After the reduction E = f*P, F = f*Q, the square concerns P,Q (and L,M) in D_ctf(Y): f* is applied to them, and RHom(f*P,f*Q) is the term of 2.1.1. The TeX keeps the printed reading; the corrected layer already has P,Q (Codex SGA-SRC-001847). 'corrected' gives the four corners, upper left, upper right, lower left, lower right.",
    corrected=r"""f^{*}\uRHom(P,Q)\overset{\mathrm{L}}{\otimes} f^{*}\uRHom(L,M) ; f^{*}\uRHom(P\overset{\mathrm{L}}{\otimes}L,Q\overset{\mathrm{L}}{\otimes}M) ; \uRHom(f^{*}P,f^{*}Q)\overset{\mathrm{L}}{\otimes}\uRHom(f^{*}L,f^{*}M) ; \uRHom(f^{*}(P\overset{\mathrm{L}}{\otimes}L),f^{*}(Q\overset{\mathrm{L}}{\otimes}M))""")
add(85, "first evaluation arrow 'f*E ⊗^L f*RHom(E,F) ⟶ f*F'",
    "E,F as printed",
    "E,F (as printed)",
    "misprint_in_print", "high", None,
    "The evaluation arrow of 2.2.2 for (P,Q), pulled back by f, as in the square above. The TeX keeps the printed reading; the corrected layer already has P,Q (Codex SGA-SRC-001847).",
    corrected=r"""f^{*}P\overset{\mathrm{L}}{\otimes} f^{*}\uRHom(P,Q)\longrightarrow f^{*}Q""")
add(85, "end of the page",
    "p. 85 ends 'On doit prouver la commutativité du carré'; the square that follows is printed at the top of p. 86",
    r"""page_085.tex ends with '\[' and '\begin{tikzcd}[': the folio-86 marker splits the tikzcd option list ('column sep=large,row sep=large]' is under folio 86; both layers)""",
    "marker", "high", None,
    r"""Page 86 really begins at the '\[' that opens this square. Exact fix: python -I move_marker.py 5 86 '\[' --before (single quotes; the last '\[' before the marker is that line; simulated in memory on both layers: the marker then stands on its own line between 'du carré' and '\[').""")


def main():
    by_page = {}
    for d in F:
        by_page.setdefault(d["page"], []).append(d)
    ok = True
    for page, items in sorted(by_page.items()):
        orig = (PAGES / f"page_{page:03d}.tex").read_bytes().decode("utf-8")
        assert "\r" not in orig
        cur = orig
        for d in items:
            fx = d["fix"]
            if not fx:
                continue
            old, new = fx["old"], fx["new"]
            n_orig, n_cur = orig.count(old), cur.count(old)
            flag = "" if n_cur == 1 else "  <-- NOT UNIQUE AT APPLICATION"
            if n_orig != 1:
                flag += f"  (occurs {n_orig}x in the original page file)"
            if "%%%%" in old:
                flag += "  <-- CROSSES MARKER"
            if n_cur != 1 or "%%%%" in old:
                ok = False
            print(page, d["kind"], repr(old[:60]), n_orig, n_cur, flag)
            cur = cur.replace(old, new, 1)
    counts = {}
    for d in F:
        c = counts.setdefault(d["page"], [0, 0])
        c[1 if d["kind"] == "misprint_in_print" else 0] += 1
    print("counts", counts, "total", len(F), "ok", ok)
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT)


main()
