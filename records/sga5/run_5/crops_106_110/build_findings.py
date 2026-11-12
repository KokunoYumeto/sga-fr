"""Build findings_106_110.json and check that every fix's old occurs exactly once in its page file.
Strings use the placeholder ¶ for a line break (LF)."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
PAGES = RUN / "b106_110"
OUT = RUN / "findings_106_110.json"


def nl(s):
    return None if s is None else s.replace("¶", "\n")


def F(page, where, scan, tex, kind, confidence, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- page 106
L.append(F(106, "top of the page, between the two triangles of type-3 arrows (c'^!P, P, d'^!P and c''^!Q, Q, d''^!Q)",
           "a comma between the two triangles, at the height of their bottom rows",
           r"\end{tikzcd} \qquad \begin{tikzcd} (no comma)", "punctuation", "high",
           r"d'{}^!P\arrow[l]¶\end{tikzcd}¶\qquad", r"d'{}^!P\arrow[l]¶\end{tikzcd}¶,\qquad",
           "Comma left out between the two diagrams."))
L.append(F(106, "triangle after 'Par produit tensoriel externe, on en déduit un triangle commutatif'",
           "a comma after the triangle, at the right of its bottom row",
           r"d'{}^!P\otimes_X^{\mathbf L}d''{}^!Q\arrow[l] (no comma)", "punctuation", "high",
           r"\otimes_X^{\mathbf L}d''{}^!Q\arrow[l]", r"\otimes_X^{\mathbf L}d''{}^!Q,\arrow[l]",
           "Put in the last node, as the file does with the commas of its other diagrams."))
L.append(F(106, "square after 'un morphisme de flèches de type 3 au-dessus de g : C → D :', upper right corner",
           "c^!(P ⊗^L Q): c with the hand-drawn ! only, no prime (c'^!P at the left has a typed prime before its !)",
           r"c'{}^!(P\otimes^{\mathbf L}Q)", "formula", "high",
           r"&¶c'{}^!(P", r"&¶c^!(P",
           "c : C → X, as c_*c^!(P ⊗^L Q) in the square (A) of 4.4.2 (and the p. 105 fix)."))
L.append(F(106, "same square, lower right corner",
           "d^!(P ⊗^L Q): no prime on d",
           r"d'{}^!(P\otimes Q),", "formula", "high",
           r"d'{}^!(P", r"d^!(P",
           "Independent of the next fix (the olds do not overlap)."))
L.append(F(106, "same corner, the tensor sign of d^!(P ⊗^L Q)",
           "an L above the ⊗",
           r"P\otimes Q (no L)", "missing", "high",
           r"P\otimes Q),", r"P\otimes^{\mathbf L}Q),",
           r"Written in the form the page uses for its other derived tensors, for the global Exposé III pass (\overset{\mathrm{L}}{\otimes})."))
L.append(F(106, "square 'au-dessus de D', upper right corner",
           "g_*c^!(P ⊗^L Q): no prime on c",
           r"g_*c'{}^!(P\otimes^{\mathbf L}Q)", "formula", "high",
           r"g_*c'{}^!(P", r"g_*c^!(P",
           "As the first square."))
L.append(F(106, "same square, lower right corner",
           "'d (P ⊗^L Q)': no ! after d; clean paper in the gap (no typed placeholder either)",
           r"d(P\otimes^{\mathbf L}Q). (as printed)", "misprint_in_print", "high",
           note="The hand-drawn ! was never put in: the square lies over D and its lower right corner is d^!(P ⊗^L Q), "
                "as in the first square and in A_2 (d_*d^!(P ⊗^L Q)). The TeX keeps the printed reading.",
           corrected=r"d^!(P\otimes^{\mathbf L}Q)"))
L.append(F(106, "'d'où la commutativité de (A) dans le cas (i). Il reste à traiter le cas (ii).'",
           "one paragraph: 'Il reste à traiter le cas (ii).' runs on in the same line",
           "a blank line (new paragraph) before 'Il reste'", "other", "high",
           r"dans le cas (i).¶¶Il reste", r"dans le cas (i). Il reste",
           "Paragraph break; drop it if paragraphing is left to a global pass."))
L.append(F(106, "top of printed p. 107: the two squares of type-1 arrows (c'_*c'^!P ... and c''_*c''^!Q ...), which still stand "
                "at the end of page_106.tex, under the folio-106 marker",
           "a comma between the two squares, at mid-height",
           r"\end{tikzcd} \qquad \begin{tikzcd} (no comma)", "punctuation", "high",
           r"d'{}^!f_*P\arrow[l]¶\end{tikzcd}¶\qquad", r"d'{}^!f_*P\arrow[l]¶\end{tikzcd}¶,\qquad",
           "Keyed to page_106.tex, where the squares stand until the folio-107 marker is moved (see the p. 107 marker finding)."))
# ---------------------------------------------------------------- page 107
L.append(F(107, "top of the page",
           "p. 107 begins with the two squares of type-1 arrows (c'_*c'^!P ← c'^!P ..., c''_*c''^!Q ← c''^!Q ...), then "
           "'au-dessus des faces de 4.4.0 contenant f'; p. 106 ends '... des carrés commutatifs de flèches de type 1'",
           "the squares are the last display of page_106.tex; the folio-107 marker follows them", "marker", "high",
           note=r"Page 107 really begins at the '\[' that opens the two squares (diplomatic s5.tex line 3331). Exact fix: "
                r"python -I move_marker.py 5 107 '\[' --before (single quotes; rfind takes the last '\[' before the marker, "
                r"the opening of this display; simulated in memory on both layers: the marker then stands between "
                r"'... de flèches de type $1$' and '\[', and page 107 begins with the squares, then 'au-'). Text not moved."))
L.append(F(107, "'au-dessus des faces de 4.4.0 contenant f'",
           "au-dessus, one word",
           "'au-' and 'dessus' on two source lines, which typesets 'au- dessus'", "other", "high",
           r"au-¶dessus", r"au-dessus",
           "The line break after the hyphen typesets as a space."))
L.append(F(107, "(4.4.7), lower right corner",
           "g_*c^!(P ⊗^L Q): no prime on c",
           r"g_*c'{}^!(P\otimes^{\mathbf L}Q),", "formula", "high",
           r"g_*c'{}^!(P", r"g_*c^!(P",
           "As on p. 106."))
L.append(F(107, "'les flèches 4.2.1 c'^!P ⊗^L_X c''^!Q → c^!(P ⊗^L Q) , d'^!f_*P ⊗^L_Y d''^!f_*Q → d^!f_*(P ⊗^L Q)'",
           "c^!(P ⊗^L Q): no prime on c",
           r"\longrightarrow c'{}^!(P\otimes^{\mathbf L}Q),", "formula", "high",
           r"\longrightarrow c'{}^!(", r"\longrightarrow c^!(", ""))
L.append(F(107, "'dans c^!(P ⊗^L Q) → d^!f_*(P ⊗^L Q) , considérées comme flèches de type 1'",
           "c^!(P ⊗^L Q): no prime on c",
           r"c'{}^!(P\otimes^{\mathbf L}Q)\longrightarrow d^!f_*(P\otimes^{\mathbf L}Q),", "formula", "high",
           r"c'{}^!(P\otimes^{\mathbf L}Q)\longrightarrow", r"c^!(P\otimes^{\mathbf L}Q)\longrightarrow", ""))
L.append(F(107, "'les produits tensoriels de flèches d'adjonction c'_*c'^!P ⊗^L c''_*c''^!Q → P ⊗^L Q'",
           "⊗ with the L above and no index (clean paper below the sign)",
           r"c'_*c'{}^!P\otimes_X^{\mathbf L}c''_*c''{}^!Q", "extra", "high",
           r"c'{}^!P\otimes_X^{\mathbf L}c''_*", r"c'{}^!P\otimes^{\mathbf L}c''_*",
           "Both factors live on X; the print has the plain derived tensor, as in P ⊗^L Q."))
L.append(F(107, "same line, 'd'_*d'^!f_*P ⊗^L d''_*d''^!f_*Q → f_*P ⊗^L f_*Q'",
           "⊗ with the L above and no index",
           r"d'_*d'{}^!f_*P\otimes_Y^{\mathbf L}d''_*d''{}^!f_*Q", "extra", "high",
           r"f_*P\otimes_Y^{\mathbf L}d''_*", r"f_*P\otimes^{\mathbf L}d''_*", ""))
L.append(F(107, "'du produit tensoriel des flèches c'_*c'^!P → d'_*d'^!f_*P et c''_*c''^!Q → d''_*d''^!f_*Q'",
           "the two arrows joined by 'et', no comma",
           r"d'_*d'{}^!f_*P,\qquad c''_*c''{}^!Q... (a comma, no 'et')", "word", "high",
           r"d'_*d'{}^!f_*P,\qquad¶c''", r"d'_*d'{}^!f_*P\quad\text{et}\quad¶c''",
           "The print runs both formulas in the text (the display is layout)."))
L.append(F(107, "'dans le produit tensoriel des flèches P → f_*P et Q → f_*Q .'",
           "'et' between the two arrows, no comma",
           r"P\longrightarrow f_*P,\qquad Q\longrightarrow f_*Q.", "word", "high",
           r"f_*P,\qquad Q", r"f_*P\quad\text{et}\quad Q", ""))
# ---------------------------------------------------------------- page 108
L.append(F(108, "triangle after 'Il s'agit de voir que le triangle', label of the vertical arrow",
           "≃ (a tilde over a bar)",
           r'\arrow[d,"\sim"]', "symbol", "high",
           r'"\sim"]\arrow[dl]', r'"\simeq"]\arrow[dl]', ""))
L.append(F(108, "same triangle, end",
           "a comma at the right of the bottom row",
           r"d'_*d'{}^!f_*P\arrow[l] (no comma)", "punctuation", "high",
           r"d'_*d'{}^!f_*P\arrow[l]", r"d'_*d'{}^!f_*P,\arrow[l]", ""))
L.append(F(108, "square after 'à vérifier la commutativité du carré', label of the right vertical arrow",
           "≃ (a tilde over a bar)",
           r'''\arrow[u,"\sim"']''', "symbol", "high",
           r'''\arrow[u,"\sim"']''', r'''\arrow[u,"\simeq"']''', ""))
L.append(F(108, "same square, end",
           "a comma at the right of the bottom row",
           r"f^*d'_*d'{}^*R\arrow[u,...] (no comma)", "punctuation", "high",
           r"f^*d'_*d'{}^*R", r"f^*d'_*d'{}^*R,",
           "Independent of the label fix (the olds do not overlap)."))
L.append(F(108, "label of Corollaire 4.5",
           "'Corollaire 4.5 - Sous les hypothèses ...': the number, then a typewriter dash",
           r"\begin{statement}{Corollaire 4.5} (renders 'Corollaire 4.5.')", "punctuation", "high",
           r"\begin{statement}{Corollaire 4.5}", r"\begin{statement}{Corollaire 4.5 -}",
           r"Exposé III label form. The statement environment appends a full stop (\textbf{#1.}), so the label then "
           r"renders 'Corollaire 4.5 -.' until the environment's full stop is settled (see message)."))
L.append(F(108, "statement of Corollaire 4.5, 'Sous les hypothèses de 4.4, on a un carré commutatif'",
           "'Sous les hypothèses de' and 'on a un carré commutatif' underlined (not 4.4)",
           "no underline", "underline", "high",
           r"Sous les hypothèses de 4.4, on a un carré commutatif",
           r"\emph{Sous les hypothèses de} 4.4, \emph{on a un carré commutatif}",
           r"\emph is this file's command for the underline in Exposé III (statements of 1.7.4 and 4.4)."))
L.append(F(108, "Corollaire 4.5, 'où g_* est défini par la flèche d'adjonction g_*K_C = g_*g^!K_D → K_D .'",
           "'où' and 'est défini par la flèche d'adjonction' underlined (not g_*, not the formula)",
           "no underline", "underline", "high",
           r"où $g_*$ est défini par la flèche d'adjonction",
           r"\emph{où} $g_*$ \emph{est défini par la flèche d'adjonction}", ""))
L.append(F(108, "'En d'autres termes, pour u ∈ Hom(...) , v ∈ Hom(...) , on a'",
           "a new paragraph: the line is indented",
           "runs on after the display (no blank line)", "other", "high",
           r"\]¶En d'autres termes", r"\]¶¶En d'autres termes",
           "Paragraph break; drop it if paragraphing is left to a global pass."))
# ---------------------------------------------------------------- page 109
L.append(F(109, "every pairing < , > of pp. 109-110; examples: (4.5.1) and (4.7.1) on p. 109, the display of Corollaire 4.10 on p. 110",
           "typed less-than and greater-than signs: '< f_*u,f_*v > = g_* < u,v >', '< u_*,v_* > = ∫_C < u,v >', "
           "'< cℓ(C')_*,cℓ(C'')_* > = Σ (C'.C'')_z'",
           r"\langle ... \rangle", "symbol", "medium",
           note=r"Convention of the transcription (66 \langle in s5.tex), not listed per occurrence: the typewriter has no "
                r"angle brackets, as it has no product sign. One decision for the volume."))
L.append(F(109, "label of Corollaire 4.7",
           "'Corollaire 4.7 - (Formule de Lefschetz-Verdier).': a typewriter dash, the title in parentheses, a hyphen in "
           "Lefschetz-Verdier, a full stop after the parenthesis",
           r"\begin{statement}{Corollaire 4.7 -- Formule de Lefschetz--Verdier} (renders 'Corollaire 4.7 – Formule de "
           r"Lefschetz–Verdier.')", "punctuation", "high",
           r"{Corollaire 4.7 -- Formule de Lefschetz--Verdier}", r"{Corollaire 4.7 - (Formule de Lefschetz-Verdier)}",
           "Two en dashes added, the parentheses left out. With the environment's appended full stop this renders the print "
           "exactly; if that full stop is dropped for the dash labels, write '...Verdier).}' instead. The title's underline "
           r"is the accepted \textbf setting."))
L.append(F(109, "statement of Corollaire 4.7, 'Sous les hypothèses de 4.4, supposons que Y_1 = Y_2 = S = D' = D'' . Pour'",
           "'Sous les hypothèses de', 'sup-posons que' and 'Pour' underlined (not 4.4, not the formula)",
           "no underline", "underline", "high",
           r"Sous les hypothèses de 4.4, supposons que $Y_1=Y_2=S=D'=D''$. Pour",
           r"\emph{Sous les hypothèses de} 4.4, \emph{supposons que} $Y_1=Y_2=S=D'=D''$. \emph{Pour}", ""))
L.append(F(109, "Corollaire 4.7, ', on a' before (4.7.1)",
           "'on a' underlined",
           "no underline", "underline", "high",
           r"on a¶\begin{equation}", r"\emph{on a}¶\begin{equation}", ""))
L.append(F(109, "Corollaire 4.7, 'où u_* ∈ Hom(f_{1*}L_1,f_{2*}L_2)' after (4.7.1)",
           "'où' underlined",
           "no underline", "underline", "high",
           r"où¶\[¶u_*", r"\emph{où}¶\[¶u_*", ""))
L.append(F(109, "Corollaire 4.7, 'sont les homomorphismes déduits de u, v par image directe sur S (3.7.6) , et'",
           "'sont les homomorphismes dé-duits de', 'par image directe sur' and 'et' underlined (not u, v, not S (3.7.6))",
           "no underline", "underline", "high",
           r"sont les homomorphismes déduits de $u$, $v$ par image directe sur $S$ (3.7.6), et",
           r"\emph{sont les homomorphismes déduits de} $u$, $v$ \emph{par image directe sur} $S$ (3.7.6), \emph{et}", ""))
L.append(F(109, "Corollaire 4.7, 'est le cup-produit, au sens de (SGA 6 I 8.3), des homomorphismes de complexes parfaits u_* , v_* (4.1.5) .'",
           "'est le cup-produit', 'au sens de' and 'des homomorphismes de complexes par-faits' underlined (not the commas, "
           "the reference, u_*, v_*)",
           "no underline", "underline", "high",
           r"est le cup-produit, au sens de (SGA 6 I 8.3), des homomorphismes de complexes parfaits",
           r"\emph{est le cup-produit}, \emph{au sens de} (SGA 6 I 8.3), \emph{des homomorphismes de complexes parfaits}", ""))
L.append(F(109, "label of Corollaire 4.8",
           "'Corollaire 4.8 - Soient ...'",
           r"\begin{statement}{Corollaire 4.8} (renders 'Corollaire 4.8.')", "punctuation", "high",
           r"\begin{statement}{Corollaire 4.8}", r"\begin{statement}{Corollaire 4.8 -}",
           "As Corollaire 4.5 (p. 108)."))
L.append(F(109, "statement of Corollaire 4.8, 'Soient t : T → S un S-schéma propre, Δ ⊂ T x_S T la diagonale,'",
           "'Soient', 'un', 'schéma propre' and 'la diagonale' underlined (not the formulas, not the 'S-' of S-schéma)",
           "no underline", "underline", "high",
           r"Soient $t:T\longrightarrow S$ un $S$-schéma propre, $\Delta\subset T\times_S T$ la diagonale,",
           r"\emph{Soient} $t:T\longrightarrow S$ \emph{un} $S$-\emph{schéma propre}, $\Delta\subset T\times_S T$ \emph{la diagonale},",
           ""))
L.append(F(109, "Corollaire 4.8, 'F : T → T un S-endomorphisme de T,'",
           "'un' and 'endomorphisme de' underlined (not 'S-', not T)",
           "no underline", "underline", "high",
           r"un $S$-endomorphisme de $T$", r"\emph{un} $S$-\emph{endomorphisme de} $T$", ""))
L.append(F(109, "Corollaire 4.8, '... Δ le schéma des points fixes de F ,'",
           "'le schéma des points fixes de' underlined",
           "no underline", "underline", "high",
           r"le schéma des points fixes de $F$", r"\emph{le schéma des points fixes de} $F$", ""))
L.append(F(109, "Corollaire 4.8, 'u ∈ Hom(F*L,L) une correspondance de L à L à support dans le graphe de F ,'",
           "'une correspondance de', 'à' and 'à support dans le graphe de' underlined (not L, not F)",
           "no underline", "underline", "high",
           r"une correspondance de $L$ à $L$ à support dans le graphe de $F$",
           r"\emph{une correspondance de} $L$ \emph{à} $L$ \emph{à support dans le graphe de} $F$", ""))
L.append(F(109, "Corollaire 4.8, '1 ∈ Hom(L,L) la correspondance identique, à support dans Δ (3.2 b)). Alors on a'",
           "'la correspondance identique', 'à support dans' and 'Alors on a' underlined (not the comma, Δ, the reference)",
           "no underline", "underline", "high",
           r"la correspondance identique, à support dans $\Delta$ (3.2 b)). Alors on a",
           r"\emph{la correspondance identique}, \emph{à support dans} $\Delta$ (3.2 b)). \emph{Alors on a}", ""))
L.append(F(109, "Corollaire 4.8, 'où u_* est l'endomorphisme de t_*L composé de t_*L → t_*F^*L (image inverse) et de t_*u : ...'",
           "'où', 'est l'endomorphisme de', 'composé de', 'image inverse' (inside the parentheses), 'et' and 'de' underlined",
           "no underline", "underline", "high",
           r"où $u_*$ est l'endomorphisme de $t_*L$ composé de $t_*L\longrightarrow t_*F^*L$ (image inverse) et de $t_*u",
           r"\emph{où} $u_*$ \emph{est l'endomorphisme de} $t_*L$ \emph{composé de} $t_*L\longrightarrow t_*F^*L$ "
           r"(\emph{image inverse}) \emph{et de} $t_*u", ""))
L.append(F(109, "label of Corollaire 4.9",
           "'Corollaire 4.9 - Sous les hypothèses ...'",
           r"\begin{statement}{Corollaire 4.9} (renders 'Corollaire 4.9.')", "punctuation", "high",
           r"\begin{statement}{Corollaire 4.9}", r"\begin{statement}{Corollaire 4.9 -}",
           "As Corollaire 4.5 (p. 108)."))
L.append(F(109, "statement of Corollaire 4.9, 'Sous les hypothèses de 4.7, on suppose que X_i est lisse sur S ,'",
           "'Sous les hypothèses de', 'on suppose que' and 'est lisse sur' underlined",
           "no underline", "underline", "high",
           r"Sous les hypothèses de 4.7, on suppose que $X_i$ est lisse sur $S$,",
           r"\emph{Sous les hypothèses de} 4.7, \emph{on suppose que} $X_i$ \emph{est lisse sur} $S$,", ""))
L.append(F(109, "Corollaire 4.9, 'purement de dimension relative r_i , et que C' (resp. C'') est un sous-schéma'",
           "'purement de dimension relative', 'et que' and 'est un sous-schéma' underlined (not r_i, C', (resp. C''))",
           "no underline", "underline", "high",
           r"purement de dimension relative $r_i$, et que $C'$ (resp. $C''$) est un sous-schéma",
           r"\emph{purement de dimension relative} $r_i$, \emph{et que} $C'$ (resp. $C''$) \emph{est un sous-schéma}",
           "The underline runs on into 'fermé de' at the top of p. 110."))
# ---------------------------------------------------------------- page 110
L.append(F(110, "Corollaire 4.9 continued, 'fermé de X fini et de tor-dimension finie sur X_2 (resp. X_1) . Soient'",
           "'fermé de', 'fini et de tor-dimension finie sur', 'resp.' and 'Soient' underlined",
           "no underline", "underline", "high",
           r"fermé de $X$ fini et de tor-dimension finie sur $X_2$ (resp. $X_1$). Soient",
           r"\emph{fermé de} $X$ \emph{fini et de tor-dimension finie sur} $X_2$ (\emph{resp.} $X_1$). \emph{Soient}",
           "Here 'resp.' is underlined (on p. 109 '(resp. C'')' is not)."))
L.append(F(110, "Corollaire 4.9, 'les classes de cohomologie de C' et C'' ,'",
           "'les classes de cohomologie de' and 'et' underlined",
           "no underline", "underline", "high",
           r"les classes de cohomologie de $C'$ et $C''$,",
           r"\emph{les classes de cohomologie de} $C'$ \emph{et} $C''$,", ""))
L.append(F(110, "Corollaire 4.9, 'cℓ(C')_* ∈ Hom(Rf_{1*}A,Rf_{2*}A)'",
           "two plain typed R",
           r"\Hom(\R f_{1*}A,\R f_{2*}A), with \R = \mathbb{R} in the diplomatic s5.tex", "font", "high",
           r"\Hom(\R f_{1*}A,\R f_{2*}A)", r"\Hom(Rf_{1*}A,Rf_{2*}A)",
           r"Exposé III types the derived-functor R plain (as the applied fixes Rf_{!}, Rf_{*}, Ri_{1*} of pp. 76-79). "
           r"In the diplomatic preamble \newcommand{\R}{\mathbb{R}} (line 47) wins over \providecommand{\R}{\mathrm R} "
           r"(line 185); only the current layer has \mathrm{R}. Drop both \R fixes if the diplomatic \R becomes \mathrm{R}."))
L.append(F(110, "Corollaire 4.9, 'cℓ(C'')_* ∈ Hom(Rf_*A,Rf_{1*}A)'",
           "two plain typed R",
           r"\Hom(\R f_*A,\R f_{1*}A)", "font", "high",
           r"\Hom(\R f_*A,\R f_{1*}A)", r"\Hom(Rf_*A,Rf_{1*}A)",
           "As the previous finding; it keeps the misprint Rf_*A (next finding)."))
L.append(F(110, "same Hom, first argument 'Rf_*A'",
           "Rf_*A: no index 2 with the * (clean paper)",
           r"\R f_*A (as printed)", "misprint_in_print", "high",
           note="cℓ(C'')_* goes from Rf_{2*}A to Rf_{1*}A (C'' is the correspondence from X_2 to X_1; v_* ∈ "
                r"Hom(f_{2*}L_2,f_{1*}L_1) in 4.7). The TeX keeps the printed reading. Corrected reading given after the "
                r"font fix (\R f_{2*}A if that fix is dropped).",
           corrected=r"Rf_{2*}A"))
L.append(F(110, "Corollaire 4.9, 'les homomorphismes correspondants (3.2 a) , 3.7.6). On a alors :'",
           "'les homo-morphismes correspondants' and 'On a alors' underlined",
           "no underline", "underline", "high",
           r"les homomorphismes correspondants (3.2 a), 3.7.6). On a alors",
           r"\emph{les homomorphismes correspondants} (3.2 a), 3.7.6). \emph{On a alors}",
           "Independent of the colon fix (next finding): the olds do not overlap."))
L.append(F(110, "'On a alors :' before the display",
           "a colon after 'alors'",
           "On a alors (no colon)", "punctuation", "high",
           r"¶\[¶\langle \cl(C')_*,\cl(C'')_*\rangle¶=¶\int", r":¶\[¶\langle \cl(C')_*,\cl(C'')_*\rangle¶=¶\int",
           "The colon goes right after 'alors': the old starts at the line break after it."))
L.append(F(110, "Corollaire 4.9, display '< cℓ(C')_* , cℓ(C'')_* > = ∫_{C'∩C''} cℓ(C)cℓ(D) ,'",
           "cℓ(C)cℓ(D)",
           r"\int_{C'\cap C''}\cl(C)\cl(D), (as printed)", "misprint_in_print", "medium",
           note="Only cℓ(C') and cℓ(C'') are defined in 4.9, and it is their cup-product that is integrated over C'∩C'' "
                "(written cℓ(C')cℓ(C'') in 4.11.1-4.11.2); C, D are the letters of 4.3 (classes of c, d). "
                "The TeX keeps the printed reading.",
           corrected=r"\int_{C'\cap C''}\cl(C')\cl(C'')"))
L.append(F(110, "Corollaire 4.9, 'où cℓ(C) cℓ(D) ∈ H^{2(r_1+r_2)}_{C'∩C''}(X,A(r_1+r_2))'",
           "cℓ(C) cℓ(D)",
           r"\cl(C)\cl(D)\in (as printed)", "misprint_in_print", "medium",
           note="As the previous finding. The TeX keeps the printed reading.",
           corrected=r"\cl(C')\cl(C'')\in"))
L.append(F(110, "same display, '= H^0(C'∩C'', K_{(C'∩C'')})'",
           "the index of K in parentheses: K_{(C' ∩ C'')}",
           r"K_{C'\cap C''}", "formula", "high",
           r"K_{C'\cap C''})", r"K_{(C'\cap C'')})", ""))
L.append(F(110, "Corollaire 4.9, 'est le cup-produit habituel.'",
           "'est le cup-produit habituel' underlined (not the full stop)",
           "no underline", "underline", "high",
           r"est le cup-produit habituel", r"\emph{est le cup-produit habituel}", ""))
L.append(F(110, "label of Corollaire 4.10",
           "'Corollaire 4.10 - Sous les hypothèses ...'",
           r"\begin{statement}{Corollaire 4.10} (renders 'Corollaire 4.10.')", "punctuation", "high",
           r"\begin{statement}{Corollaire 4.10}", r"\begin{statement}{Corollaire 4.10 -}",
           "As Corollaire 4.5 (p. 108)."))
L.append(F(110, "statement of Corollaire 4.10, 'Sous les hypothèses de 4.9, supposons que C'∩C'' soit fini. Pour z ∈ C'∩C'' , notons'",
           "'Sous les hypothèses de', 'supposons que', 'soit fini', 'Pour' and 'notons' underlined",
           "no underline", "underline", "high",
           r"Sous les hypothèses de 4.9, supposons que $C'\cap C''$ soit fini. Pour $z\in C'\cap C''$, notons",
           r"\emph{Sous les hypothèses de} 4.9, \emph{supposons que} $C'\cap C''$ \emph{soit fini}. \emph{Pour} "
           r"$z\in C'\cap C''$, \emph{notons}", ""))
L.append(F(110, "Corollaire 4.10, 'notons (C'.C'')_z l'image dans A'",
           "(C'.C'')_z: a typed full stop on the baseline",
           r"$(C'\!\cdot C'')_z$ (a centred dot)", "symbol", "medium",
           r"$(C'\!\cdot C'')_z$", r"$(C'.C'')_z$",
           "As the applied fixes of 4.12 and (4.12.1), pp. 111-112."))
L.append(F(110, "Corollaire 4.10, 'l'image dans A de la multiplicité d'intersection de C' et C'' en z . Alors on a'",
           "'l'image dans', 'de la multiplicité d'in-tersection de', 'et', 'en' and 'Alors on a' underlined",
           "no underline", "underline", "high",
           r"l'image dans $A$ de la multiplicité d'intersection de $C'$ et $C''$ en $z$. Alors on a",
           r"\emph{l'image dans} $A$ \emph{de la multiplicité d'intersection de} $C'$ \emph{et} $C''$ \emph{en} $z$. "
           r"\emph{Alors on a}", ""))
L.append(F(110, "display of Corollaire 4.10, 'Σ_{z ∈ C'∩C''} (C'.C'')_z .'",
           "(C'.C'')_z: a baseline full stop",
           r"(C'\!\cdot C'')_z", "symbol", "medium",
           r"}(C'\!\cdot C'')_z.", r"}(C'.C'')_z.",
           "As the previous one."))
L.append(F(110, "label of 4.11",
           "'4.11', then the text; no punctuation after the number",
           r"\begin{statement}{4.11} (renders '4.11.')", "punctuation", "medium",
           note=r"The full stop comes from the statement environment (\textbf{#1.}); it goes with the decision on the "
                "environment's full stop for the dash labels (see message)."))
L.append(F(110, "4.11, 'du fait qu'on est dans une situation \"excédentaire\".'",
           "straight typewriter double quotes",
           "«excédentaire»", "punctuation", "high",
           r"«excédentaire»", r"``excédentaire''",
           "The accepted forms for the print's straight quotes are ``...'' and \"...\"; guillemets are another sign."))
L.append(F(110, "every cℓ of p. 110; examples: cℓ(C') ∈ H^{2r_1}_{C'}(X,A(r_1)) (4.9), the display of 4.10, (4.11.1)",
           "cℓ: a typed c followed by a hand-drawn script ℓ",
           r"\cl = \operatorname{cl} (a roman l)", "font", "medium",
           note=r"Convention of the transcription (macro \cl, s5.tex line 81), not listed per occurrence. One decision for the "
                r"volume (e.g. \operatorname{c\ell} for the diplomatic layer where the print writes cℓ)."))

# ---------------------------------------------------------------- checks
bad = 0
for f in L:
    if f["fix"] is None:
        continue
    t = (PAGES / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", n, f["page"], repr(f["fix"]["old"]))
    if "%%%%%%%%%%" in f["fix"]["old"]:
        bad += 1
        print("MARKER IN OLD", f["page"])
# overlap check: apply all fixes of a page in order and confirm each old still occurs once
for p in range(106, 111):
    t = (PAGES / f"page_{p}.tex").read_text(encoding="utf-8")
    for f in L:
        if f["page"] != p or f["fix"] is None:
            continue
        if t.count(f["fix"]["old"]) != 1:
            bad += 1
            print("SEQUENTIAL FAIL", p, repr(f["fix"]["old"]))
            continue
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
if bad:
    sys.exit(f"{bad} problems")
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in L)
for p in range(106, 111):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("written", OUT, len(L))
