"""Build findings_091_095.json (SGA 5 pp. 91-95). Newlines in old/new are written as the placeholder ⏎."""
import json
import pathlib


def N(s):
    return None if s is None else s.replace("⏎", "\n")


OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_091_095.json")
F = []


def add(page, where, scan, tex, kind, confidence, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence,
             fix=None if old is None else {"old": N(old), "new": N(new)})
    if kind == "misprint_in_print":
        d["corrected"] = N(corrected)
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 91
add(91, "top of the page: 'à support dans C'",
    "p. 91 begins 'à support dans C , qu'on appellera classe de (c,N)'; p. 90 ends '... une correspondance "
    "cohomologique de A_{X_1} à A_{X_2}(-N)[2N]'.",
    "The 'à' that ends the last line of page_090.tex ('... de $A_{X_1}$ à $A_{X_2}(-N)[2N]$ à', s5.tex line 2534 "
    "diplomatic, 2535 current) stands above the folio-91 marker; page_091.tex begins 'support dans $C$'.",
    "marker", "high", None, None,
    "Page 91 really begins with that 'à'. Already reported on p. 90 (findings_086_090.json) and applied: in the "
    "live s5.tex (both layers, 19:56) the folio-91 marker stands before 'à'. Nothing to do; listed because "
    "page_091.tex predates the move.")

add(91, "formulas that the print runs into the text, pp. 91-93",
    "p. 91: 'se récrit H_C^{2(r_1-N)}(X,A_X(r_1-N)) , et la classe de (c,N)'; 'C'est l'élément 1 ∈ Hom(L_1,L_1) = "
    "H^O(X,Δ_*Δ^!RHom_S(L_1,L_1)) (groupe qui ...'. p. 92: 'l'isomorphisme canonique F*L_1 ⟶~ L_1 (loc. cit. §2 "
    "prop. 1)'; the five definitions of 3.3 (text lines from the left margin). p. 93: '(SGA 4 XVIII 3.1.9.6) "
    "Df_{1!}L_1 ⟶~ f_{1*}DL_1 par application de'; 'l'isomorphisme de Künneth f_{1*}DL_1 ⊗ f_{2*}L_2 ⟶~ "
    "f_*(DL_1 ⊗ L_2) et de f_*(3.1.1)'.",
    "Each set as a display \\[...\\].",
    "other", "high", None, None,
    "Layout convention of the transcription, as reported for pp. 96-100 (findings_096_100.json); the content "
    "agrees. Not listed per occurrence; the colon of 3.3 is listed on p. 92.")

add(91, "first line: 'qu'on appellera classe de (c,N) , et qu'on notera'",
    "'classe de' underlined; the rule stops before '(c,N)'.",
    r"\emph{classe de $(c,N)$}",
    "underline", "high",
    r"\emph{classe de $(c,N)$}", r"\emph{classe de} $(c,N)$",
    "")

add(91, "b), the quotation '(\"ensemble des points (fx,x) \")'",
    "(\"ensemble des points: no article before 'ensemble'.",
    r"(``l'ensemble des points",
    "extra", "high",
    r"(``l'ensemble", r"(``ensemble",
    "")

add(91, "b), the same quotation: the point (fx,x)",
    "(fx,x) with a small f; the map is the capital F of 'Soit F : X_2 → X_1' and 'définie par F'.",
    r"$(Fx,x)$: silent correction.",
    "misprint_in_print", "high",
    r"$(Fx,x)$", r"$(fx,x)$",
    "The graph of F is the set of points (Fx,x); the typed small f is a typing error. The TeX silently corrects "
    "it; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"$(Fx,x)$")

add(91, "(3.2.6), first line",
    "RHom(c_1(F*)*L_1,c_2(F)^!L_2) = RHom(F*L_1,L_2) : 'c_1(F*)' with a star inside the parenthesis; the second "
    "line has Hom(c_1(F)*L_1,c_2(F)^!L_2).",
    r"\uRHom\bigl(c_1(F^*)^*L_1,c_2(F)^!L_2\bigr): as printed.",
    "misprint_in_print", "high",
    None, None,
    "c_1(F) is the first projection of the graph C(F), as in the second line; the star in (F*) is a typing "
    "error. The TeX keeps the printed reading; the corrected layer already has c_1(F).",
    corrected=r"\uRHom\bigl(c_1(F)^*L_1,c_2(F)^!L_2\bigr)")

add(91, "(i): 'F = l'identité de X_1'",
    "F = l'identité de X_1 : one character between '=' and the apostrophe (the l of l'identité); no separate 1.",
    r"$F=1$ l'identité de $X_1$",
    "extra", "high",
    r"$F=1$ l'identité", r"$F=$ l'identité",
    "The typewriter's l and 1 look alike; the TeX reads the one character both as the identity 1 and as the "
    "article.")

add(91, "(i): 's'appelle correspondances diagonale'",
    "'correspondances diagonale' underlined, with an s on 'correspondances'.",
    r"\emph{correspondance diagonale}: silent correction.",
    "misprint_in_print", "high",
    "correspondance diagonale", "correspondances diagonale",
    "Singular, as 'La correspondance à support dans Δ ... s'appelle'. The TeX silently corrects it; the fix "
    "restores the printed reading (diplomatic layer only).",
    corrected="correspondance diagonale")

add(91, "last line: '(groupe qui d'identifie à'",
    "'d'identifie' with d apostrophe.",
    "'(groupe qui s'%' (page_091.tex) + 'identifie à' (page_092.tex): s', silent correction.",
    "misprint_in_print", "high",
    "qui s'%", "qui d'%",
    "'s'identifie à' is meant (the group is identified with H^{2r}_Δ(...)); the typed d' is a typing error. The "
    "TeX silently corrects it; the fix restores the printed reading (diplomatic layer only). 'identifie à' "
    "stands under the folio-92 marker (marker finding of p. 92).",
    corrected="qui s'identifie")

# ---------------------------------------------------------------- p. 92
add(92, "top of the page: 'H^{2r}_Δ(X,RHom_S(L_1,L_1)(r)) quand X_1 est lisse'",
    "p. 92 begins with the formula H^{2r}_Δ(X,RHom_S(L_1,L_1)(r)); p. 91 ends '(groupe qui d'identifie à'.",
    "page_092.tex begins 'identifie à $\\H^{2r}_\\Delta(...)$' (s5.tex line 2573 in both layers at 19:56): "
    "'identifie à' ends p. 91 in the print.",
    "marker", "high", None, None,
    "Page 92 really begins at '$\\H^{2r}_\\Delta'. Exact fix: python -I move_marker.py 5 92 '$\\H^{2r}_\\Delta' "
    "(single quotes; forward search from the marker; simulated in memory on both layers: the marker then splits "
    "that line after 'identifie à ', and the '%' after 's'' still joins 's'' and 'identifie'). Text not moved.")

add(92, "3.3, the last of the five definitions before the diagram (3.3.0): 'p'_2 = f_1 x_S X_2 :'",
    "'p'_2 = f_1 x_S X_2 :' ends with a colon, which introduces the diagram.",
    "'p'_2=f_1\\times_S X_2.' with a full stop.",
    "punctuation", "high",
    r"\times_S X_2.", r"\times_S X_2:",
    "The five definitions are text lines from the left margin in the print (layout convention, see the p. 91 "
    "entry).")

add(92, "diagram (3.3.0), label of the diagonal arrow X → Y",
    "f stands above the diagonal, to its upper left, clear of the line.",
    "\\arrow[dl,\"f\" description]: the label set on the arrow.",
    "other", "medium",
    r"""\arrow[dl,"f" description]""", r"""\arrow[dl,"f"']""",
    "")

add(92, "diagram (3.3.0), bottom arrow Y_1 x_S X_2 → Y",
    "f'_2 above the arrow, as p'_1 above the top arrow.",
    "\\arrow[l,\"f'_2\"]: label below a leftward arrow.",
    "other", "high",
    r"""\arrow[l,"f'_2"]""", r"""\arrow[l,"f'_2"']""",
    "As the label fixes of pp. 38, 57, 64.")

add(92, "diagram (3.3.0)",
    "A full stop to the right of the diagram's bottom row.",
    "No punctuation after the diagram.",
    "punctuation", "high",
    r"\end{tikzcd}⏎\tag{3.3.0}", r"\end{tikzcd}\quad .⏎\tag{3.3.0}",
    "Same form as the p. 31 and p. 38 fixes.")

# ---------------------------------------------------------------- p. 93
add(93, "the square at the top of the page, right side RHom_S(f_{1!}L_1,f_{2*}L_2) — f_*RHom_S(L_1,L_2)",
    "A plain vertical line, no arrowhead at either end; the left side (1) has its head.",
    "\\arrow[d]: an arrow with a head (silent correction).",
    "misprint_in_print", "high",
    r"f_{2*}L_2) \arrow[d] \\", r"f_{2*}L_2) \arrow[d,dash] \\",
    "The vertical map is the inverse of 3.3.1 ('dont l'inverse rende commutatif le carré', p. 92), drawn "
    "downward like (1) to (4) on pp. 94-95; the drawing omits the head. If the coordinator takes the plain line "
    "as deliberate, file it as 'symbol' (both layers). 'dash' as in s5.tex line 1843.",
    corrected=r"\arrow[d]")

add(93, "the same square, bottom arrow, label (2)",
    "(2) above the arrow, as 3.1.1 above the top arrow.",
    "\\arrow[r,\"(2)\"']: label below.",
    "other", "high",
    r"""\arrow[r,"(2)"']""", r"""\arrow[r,"(2)"]""",
    "")

add(93, "'par application de ⊗^L_S f_{2*}L_2 , et (2) est composé'",
    "The tensor sign (L above, S below) follows 'de' directly: no dash before it.",
    r"$-\overset{\mathbf L}{\otimes}_S f_{2*}L_2$",
    "extra", "high",
    r"de $-\overset", r"de $\overset",
    "")

add(93, "label of Proposition 3.4",
    "'Proposition 3.4 - Avec les notations ...': 'Proposition' underlined, then the number and a typewriter dash, "
    "the statement run in.",
    "\\begin{statement}{Proposition 3.4}: no dash.",
    "punctuation", "high",
    r"\begin{statement}{Proposition 3.4}", r"\begin{statement}{Proposition 3.4 -}",
    "Exposé III's statement environment prints the label as given (s5.tex line 1938), as 'Exemple 4.3 -', "
    "'Théorème 4.4 -' later in the exposé.")

add(93, "statement of Proposition 3.4, first sentence",
    "'Avec les notations de 3.3.0, on a un diagramme commutatif d'iso-morphismes de' underlined; 'D_ctf(Y) :' "
    "not.",
    "No underline.",
    "underline", "high",
    "Avec les notations de 3.3.0, on a un diagramme commutatif d'isomorphismes de",
    r"\emph{Avec les notations de 3.3.0, on a un diagramme commutatif d'isomorphismes de}",
    "\\emph is this file's command for the print's underline (\\emph{image directe} on this page).")

add(93, "diagram (3.4.1), top vertex RHom_S(f_{1!}L_1,f_{2*}L_2)",
    "No rule under Hom (clean paper); the other three RHom of the diagram and the top right vertex of the square "
    "above are underlined.",
    "\\uRHom_S(f_{1!}L_1,f_{2*}L_2): silent correction.",
    "misprint_in_print", "high",
    r"& \uRHom_S(f_{1!}L_1,f_{2*}L_2)⏎  \arrow[dl",
    r"& \mathrm{R}\mathrm{Hom}_S(f_{1!}L_1,f_{2*}L_2)⏎  \arrow[dl",
    "The typist left out the underline (as the H^i_c underlines of SGA 7 II, issue 79). \\mathrm{R}\\mathrm{Hom} "
    "is Exposé III's \\uRHom without the underline. Diplomatic layer only.",
    corrected=r"\uRHom_S(f_{1!}L_1,f_{2*}L_2)")

add(93, "diagram (3.4.1), middle vertical arrow",
    "The vertical arrow from the top vertex to f_*RHom_S(L_1,L_2) has no label (clean paper on both sides); the "
    "text below calls it (5): 'où (5) est l'inverse de 3.3.1'.",
    "\\arrow[dd,\"(5)\" description]: silent correction.",
    "misprint_in_print", "high",
    r"""\arrow[dd,"(5)" description]""", r"\arrow[dd]",
    "(1) to (4) are written on their arrows; (5) was left out. The TeX supplies it; the fix restores the printed "
    "unlabelled arrow (diplomatic layer only).",
    corrected=r"""\arrow[dd,"(5)" description]""")

add(93, "diagram (3.4.1)",
    "A comma to the right of the bottom vertex f_*RHom_S(L_1,L_2).",
    "No punctuation after the diagram.",
    "punctuation", "high",
    r"\end{tikzcd}⏎\tag{3.4.1}", r"\end{tikzcd}\quad ,⏎\tag{3.4.1}",
    "")

add(93, "statement of Proposition 3.4 after (3.4.1): 'où (5) est l'inverse de 3.3.1 et les flèches (1) à (4) ...'",
    "Underlined: 'où', 'est l'inverse de', 'et les flèches', 'sont définies par les diagrammes commutatifs "
    "ci-après', 'dans lesquels', 'désigne une flèche déduite'. Not underlined: (5), 3.3.1, (1) à (4), the comma, "
    "\"ch. b.\".",
    "No underline.",
    "underline", "high",
    "où (5) est l'inverse de 3.3.1 et les flèches (1) à (4) sont définies par les diagrammes commutatifs "
    "ci-après, dans lesquels ``ch. b.'' désigne une flèche déduite",
    r"\emph{où} (5) \emph{est l'inverse de} 3.3.1 \emph{et les flèches} (1) à (4) \emph{sont définies par les "
    r"diagrammes commutatifs ci-après}, \emph{dans lesquels} ``ch. b.'' \emph{désigne une flèche déduite}",
    "The underline runs on into p. 94 from 'd'un', which ends page_093.tex but begins p. 94 (folio-94 marker "
    "finding); it is not touched here, so that the marker move finds it.")

# ---------------------------------------------------------------- p. 94
add(94, "top of the page: 'd'un isomorphisme de changement de base'",
    "p. 94 begins 'd'un isomorphisme de changement de base ou de Künneth'; p. 93 ends '... dans lesquels "
    "\"ch. b.\" désigne une flèche déduite'.",
    "'d'un' ends the last line of page_093.tex (s5.tex line 2664 in both layers at 19:56); page_094.tex begins "
    "'isomorphisme de changement'.",
    "marker", "high", None, None,
    "Page 94 really begins with that 'd'un'. Exact fix: python -I move_marker.py 5 94 \"d'un\" --before "
    "(simulated in memory on both layers: the last 'd'un' before the marker is this one; the marker then splits "
    "the line after 'déduite '). After the move, underline it as the rest of the line: 'd'un' -> '\\emph{d'un}' "
    "(not given as a fix: it would change the anchor). Text not moved.")

add(94, "first line: 'd'un isomorphisme de changement de base ou de Künneth de l'un des types envisagés au'",
    "The whole line underlined, from 'd'un' to 'au'.",
    "No underline.",
    "underline", "high",
    "isomorphisme de changement de base ou de Künneth de l'un des types envisagés au",
    r"\emph{isomorphisme de changement de base ou de Künneth de l'un des types envisagés au}",
    "Its first word 'd'un' stands at the end of page_093.tex (marker finding).")

add(94, "'de l'un des types envisagés au n°1'",
    "n°1: n with a raised small circle (the typewriter's degree sign), then 1.",
    "no~1",
    "symbol", "high",
    "no~1", "n°1",
    "As 'n°2' at s5.tex line 12554.")

add(94, "'\"dual.\" une flèche déduite d'un isomorphisme de dualité de type 2.1.4 ou'",
    "'une flèche déduite d'un isomorphisme de dualité de type' and 'ou' underlined; '2.1.4' not.",
    "No underline.",
    "underline", "high",
    "une flèche déduite d'un isomorphisme de dualité de type 2.1.4 ou (SGA",
    r"\emph{une flèche déduite d'un isomorphisme de dualité de type} 2.1.4 \emph{ou} (SGA",
    "")

add(94, "'(SGA 4 XVIII 3.1.9.6), \"triv.\" un isomorphisme trivial'",
    "No 'et' before \"triv.\".",
    r"3.1.9.6), et ``triv.''",
    "extra", "high",
    r"3.1.9.6), et ``triv.''", r"3.1.9.6), ``triv.''",
    "")

add(94, "same line: 'un isomorphisme trivial'",
    "'un isomorphisme trivial' underlined.",
    "No underline.",
    "underline", "high",
    "un isomorphisme trivial", r"\emph{un isomorphisme trivial}",
    "")

add(94, "end of the statement's text, before the diagram of (1)",
    "No punctuation after 'trivial' (clean paper to the end of the line).",
    "'trivial:'",
    "punctuation", "high",
    r":⏎\[⏎\begin{tikzcd}", r"⏎\[⏎\begin{tikzcd}",
    "")

add(94, "diagram of (1), bottom arrow f'_{1*}RHom(L_1 ⊗ A_{Y_2},K_{X_1} ⊗ f_{2*}L_2) → f'_{1*}RHom_S(L_1,f_{2*}L_2)",
    "\"ch. b.\" above the arrow, as on the top arrow.",
    "\\arrow[r,\"\\mathrm{ch.b.}\"']: label below.",
    "other", "high",
    r"""\arrow[r,"\mathrm{ch.b.}"']⏎& f'_{1*}""", r"""\arrow[r,"\mathrm{ch.b.}"]⏎& f'_{1*}""",
    "")

add(94, "diagram of (1), after the bottom right vertex",
    "No punctuation after f'_{1*}RHom_S(L_1,f_{2*}L_2) (clean paper).",
    "'f'_{1*}\\uRHom_S(L_1,f_{2*}L_2),' with a comma.",
    "punctuation", "high",
    r"\uRHom_S(L_1,f_{2*}L_2),⏎\end{tikzcd}", r"\uRHom_S(L_1,f_{2*}L_2)⏎\end{tikzcd}",
    "")

# ---------------------------------------------------------------- p. 95
add(95, "top of the page: the diagram of (3), 'RHom(L_1 ⊗ A_{Y_2},K_{X_1} ⊗ f_{2*}L_2) → RHom_S(L_1,f_{2*}L_2)'",
    "p. 95 begins with the diagram of (3); p. 94 prints the whole diagram of (2), down to its bottom row "
    "f'_{2*}RHom(f_{1!}L_1 ⊗ A_{X_2},K_{Y_1} ⊗ L_2) → f'_{2*}RHom_S(f_{1!}L_1,L_2).",
    "The folio-95 marker (s5.tex line 2686 in both layers at 19:56) stands inside the tikzcd of (2), between "
    "'\\arrow[d,\"' and '\\mathrm{dual.}\"']'; page_095.tex begins with the last rows of the diagram of (2).",
    "marker", "high", None, None,
    "Page 95 really begins at the '\\[' of the diagram of (3) (page_095.tex line 11). Exact fix: python -I "
    "move_marker.py 5 95 '\\[' (forward search: the first '\\[' after the marker is that one; simulated in memory "
    "on both layers: the marker then stands on its own line between '\\]' and '\\['). The two fixes of the diagram "
    "of (2) filed under p. 95 (label, comma) find their old only before the move; after it, apply them on p. 94. "
    "The move leaves the label '\\arrow[d,\"' + line break + '\\mathrm{dual.}\"']' split over two lines "
    "(harmless; rejoin if wanted). Text not moved.")

add(95, "diagram of (2) (printed on p. 94), bottom arrow f'_{2*}RHom(f_{1!}L_1 ⊗ A_{X_2},K_{Y_1} ⊗ L_2) → "
        "f'_{2*}RHom_S(f_{1!}L_1,L_2)",
    "\"ch. b.\" above the arrow.",
    "\\arrow[r,\"\\mathrm{ch.b.}\"']: label below.",
    "other", "high",
    r"""\arrow[r,"\mathrm{ch.b.}"']⏎& f'_{2*}""", r"""\arrow[r,"\mathrm{ch.b.}"]⏎& f'_{2*}""",
    "Filed under p. 95 because the TeX stands in page_095.tex (marker finding); the old is unique on p. 94 too.")

add(95, "diagram of (2) (printed on p. 94), after the bottom right vertex",
    "No punctuation after f'_{2*}RHom_S(f_{1!}L_1,L_2) (clean paper).",
    "'f'_{2*}\\uRHom_S(f_{1!}L_1,L_2),' with a comma.",
    "punctuation", "high",
    r"\uRHom_S(f_{1!}L_1,L_2),⏎\end{tikzcd}", r"\uRHom_S(f_{1!}L_1,L_2)⏎\end{tikzcd}",
    "Filed under p. 95 for the same reason; the old is unique on p. 94 too.")

add(95, "diagram of (3), bottom arrow p'_{1*}RHom(L_1 ⊗ A_{X_2},K_{X_1} ⊗ L_2) → p'_{1*}RHom_S(L_1,L_2)",
    "\"ch. b.\" above the arrow.",
    "\\arrow[r,\"\\mathrm{ch.b.}\"']: label below.",
    "other", "high",
    r"""\arrow[r,"\mathrm{ch.b.}"']⏎& p'_{1*}""", r"""\arrow[r,"\mathrm{ch.b.}"]⏎& p'_{1*}""",
    "")

add(95, "diagram of (3), after the bottom right vertex",
    "No punctuation after p'_{1*}RHom_S(L_1,L_2) (clean paper).",
    "'p'_{1*}\\uRHom_S(L_1,L_2),' with a comma.",
    "punctuation", "high",
    r"\uRHom_S(L_1,L_2),⏎\end{tikzcd}", r"\uRHom_S(L_1,L_2)⏎\end{tikzcd}",
    "")

add(95, "diagram of (4), bottom arrow p'_{2*}RHom(L_1 ⊗ A_{X_2},K_{X_1} ⊗ L_2) → p'_{2*}RHom_S(L_1,L_2)",
    "\"ch. b.\" above the arrow.",
    "\\arrow[r,\"\\mathrm{ch.b.}\"']: label below.",
    "other", "high",
    r"""\arrow[r,"\mathrm{ch.b.}"']⏎& p'_{2*}""", r"""\arrow[r,"\mathrm{ch.b.}"]⏎& p'_{2*}""",
    "")

add(95, "'f_1^!K_{Y_1} ⟶~ K_{X_1} , (u_2,v_2) : (A_{X_2},L_2) ⟶ (A_{Y_2},f_{2*}L_2) par'",
    "Only a comma between K_{X_1} and (u_2,v_2): no 'et où'.",
    r"K_{X_1}$, et où $(u_2,v_2)",
    "extra", "high",
    r"K_{X_1}$, et où $(u_2,v_2)", r"K_{X_1}$, $(u_2,v_2)",
    "")

add(95, "same sentence: '(A_{Y_2},f_{2*}L_2) par l'isomorphisme'",
    "'par' follows the formula directly: no 'est donné'.",
    r"L_2)$ est donné par",
    "extra", "high",
    r"L_2)$ est donné par", r"L_2)$ par",
    "")

add(95, "'par l'isomorphisme caninique A_{X_2} ⟶~ f_2^*A_{Y_2}'",
    "'caninique'.",
    "'canonique': silent correction.",
    "misprint_in_print", "high",
    r"canonique $A_{X_2}", r"caninique $A_{X_2}",
    "Typing error for 'canonique' (the line above prints 'l'iso-morphisme canonique'). The TeX silently corrects "
    "it; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"canonique $A_{X_2}")

add(95, "label of Corollaire 3.5",
    "'Corollaire 3.5 - On suppose que ...': 'Corollaire' underlined, then the number and a typewriter dash, the "
    "statement run in.",
    "\\begin{statement}{Corollaire 3.5}: no dash.",
    "punctuation", "high",
    r"\begin{statement}{Corollaire 3.5}", r"\begin{statement}{Corollaire 3.5 -}",
    "As the label of Proposition 3.4 (p. 93).")

add(95, "statement of Corollaire 3.5",
    "Underlined: 'On suppose que', 'Soit', 'L'image directe', 'peut s'obtenir des deux manières équiva-lentes "
    "suivantes'. Not underlined: the formulas, '(3.3.2)', the full stops after S and L_2), the colon.",
    "No underline.",
    "underline", "high",
    r"On suppose que $Y_1=Y_2=S$. Soit $u\in\Hom_S(L_1,L_2)$. L'image directe $f_*u\in\Hom(f_{1!}L_1,f_{2*}L_2)$ "
    r"(3.3.2) peut s'obtenir des deux manières équivalentes suivantes",
    r"\emph{On suppose que} $Y_1=Y_2=S$. \emph{Soit} $u\in\Hom_S(L_1,L_2)$. \emph{L'image directe} "
    r"$f_*u\in\Hom(f_{1!}L_1,f_{2*}L_2)$ (3.3.2) \emph{peut s'obtenir des deux manières équivalentes suivantes}",
    "")

add(95, "end of the page: 'a) On s'identifie u'",
    "p. 95 ends with Corollaire 3.5's '... suivantes :'; p. 96 begins 'a). On s'identifie u , par dualité "
    "triviale'.",
    "'\\begin{enumerate}[label=\\alph*)]' and '\\item On s'%' (s5.tex lines 2723-2724 diplomatic, 2724-2725 "
    "current) stand above the folio-96 marker, at the end of page_095.tex.",
    "marker", "high", None, None,
    "Page 96 really begins at '\\begin{enumerate}[label=\\alph*)]'. Already reported on p. 96 "
    "(findings_096_100.json) and applied: in the live s5.tex (both layers, 19:56) the folio-96 marker stands "
    "after the \\end{statement} of Corollaire 3.5. Nothing to do; listed because page_095.tex predates the move.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
