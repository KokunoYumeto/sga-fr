"""Build findings_191_195.json and check every fix's 'old' (exactly once, no overlaps on a page)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b191_195"
OUT = RUN / "findings_191_195.json"
NL = "<NL>"


def s(x):
    return None if x is None else x.replace(NL, "\n")


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    return d


pages = {n: (B / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(191, 196)}

# hooked arrows of (6.14.1), built from the file's own lines
p194 = pages[194].split("\n")
blk_old = "\n".join(p194[86:96])
blk_new = blk_old
for a in [r"\draw[->] (C1U) -- (C2U);", r"\draw[->] (U1) --", r"\draw[->] (U2) -- (X2);",
          r"\draw[->] (C2U) -- (C);", r"\draw[->] (C2XU) -- (C);", r"\draw[->] (XU1) --",
          r"\draw[->] (XU2) -- (X2);"]:
    assert blk_old.count(a) == 1, a
    blk_new = blk_new.replace(a, a.replace(r"\draw[->]", r"\draw[{Hooks[right]}->]"))

L = []
# ---------------- page 191
L.append(F(191, "end of the first paragraph: 'constructible). De même, si B ...'",
           "'(resp. de tor-dimension finie et à cohomologie constructible). De' / 'même, si B ...': one paragraph",
           "blank line before 'De même' (new paragraph)", "other", "high",
           "constructible).<NL><NL>De même", "constructible). De même", "Paragraph break the print does not have."))
L.append(F(191, "'un A[G]-module à gauche sur X (sans groupe d'opérateurs), donc'",
           "(sans groupe d'opérateurs),", "sans groupe d'opérateurs,", "punctuation", "high",
           "sur $X$ sans groupe d'opérateurs,", "sur $X$ (sans groupe d'opérateurs),", "Parentheses dropped."))
L.append(F(191, "'la définition des \"six opérations\"'", "straight typewriter double quotes",
           "« six opérations »", "punctuation", "high",
           "« six opérations »", r"""``six opérations''""",
           "Guillemets for the print's straight quotes (the accepted forms are ``...'' and \"...\"), as on p. 183."))
L.append(F(191, "'envisagées en (loc. cit) (changement de base,'",
           "(loc. cit) : no full stop after 'cit' (clean scan)", "(loc. cit.)", "misprint_in_print", "high",
           "(loc. cit.)", "(loc. cit)",
           "Typing slip of the print (abbreviation without its full stop); the TeX silently corrects it.",
           corrected="(loc. cit.)"))
L.append(F(191, "'Cette extension n'offre pas de difficulté (pour la définition ... équivariantes).'",
           "difficulté (pour la définition des foncteurs f_! , f^! , il suffit d'utiliser des compactifications équivariantes).",
           "difficulté: pour la définition ... équivariantes.", "punctuation", "high",
           "difficulté: pour la définition des foncteurs $f_!$, $f^!$, il suffit d'utiliser des compactifications équivariantes.",
           "difficulté (pour la définition des foncteurs $f_!$, $f^!$, il suffit d'utiliser des compactifications équivariantes).",
           "The print's parenthesis became a colon; one edit for both parentheses."))
L.append(F(191, "'dans le cadre des G-S-schémas. Si, pour i = 1, 2,'",
           "'... dans le cadre des G-S-schémas. Si, pour i = 1, 2, X_i est': one paragraph",
           "blank line before 'Si, pour' (new paragraph)", "other", "high",
           "$G$-$S$-schémas.<NL><NL>Si, pour", "$G$-$S$-schémas. Si, pour", "Paragraph break the print does not have."))
L.append(F(191, "'les éléments de Hom_A(c_1^*L_1,c_2^!L_2)'",
           "Hom_A not underlined (global Hom: its elements are the correspondences)", r"\uHom_A(c_1^*L_1,c_2^!L_2)",
           "underline", "high", r"\uHom_A(c_1^*L_1,c_2^!L_2)", r"\Hom_A(c_1^*L_1,c_2^!L_2)",
           "Plain Hom, as the u ∈ Hom_{A[G]}(c_1^*L,c_2^!L) further down and p. 181 (5.13.3)."))
L.append(F(191, "parenthesis after Hom_A(c_1^*L_1,c_2^!L_2)",
           "(Hom_A = Hom dans la catégorie D(G,_A-) ) s'appelleront",
           r"où $\Hom_A$ est pris dans la catégorie $D(G,{}_A-)$, s'appelleront", "word", "high",
           r"où $\Hom_A$ est pris dans la catégorie $D(G,{}_A-)$, s'appelleront",
           r"($\Hom_A=\Hom$ dans la catégorie $D(G,{}_A-)$) s'appelleront",
           "The TeX rewords the print's parenthesis ('où ... est pris'); Hom not underlined in it."))
L.append(F(191, "definition of the equivariant correspondences",
           "underlined: 'correspondances (cohomologiques) équivariantes de' | 'à support' + 'dans' (across the line break); not underlined: L_1 à L_2, c, the full stop",
           "correspondances cohomologiques équivariantes de $L_1$ à $L_2$ à support dans $c$.  (no underline, no parentheses)",
           "underline", "high",
           "correspondances cohomologiques équivariantes de $L_1$ à $L_2$ à support dans $c$.",
           r"\emph{correspondances (cohomologiques) équivariantes de} $L_1$ à $L_2$ \emph{à support dans} $c$.",
           "Also the print's parentheses around 'cohomologiques', dropped in the TeX; one edit for both. \\emph is this exposé's command for the print's underline (as pp. 146-150)."))
L.append(F(191, "'l'isomorphisme 6.4.1 (dans D(G,X) ) se \"raffine\"'", "(dans D(G,X) )", r"dans $D(G,X)$",
           "punctuation", "high", "6.4.1 dans $D(G,X)$", "6.4.1 (dans $D(G,X)$)", "Parentheses dropped."))
L.append(F(191, "same sentence: 'se \"raffine\" en un isomorphisme'", "\"raffine\" in straight double quotes",
           "se raffine en (no quotes)", "punctuation", "high", "se raffine en", "se ``raffine'' en",
           "Quotation marks dropped."))
L.append(F(191, "'et L ∈ ob D_ctf(_{A[G]}X) ⊂ D_ctf(G,_AX) ) on peut, pour'",
           "a stray closing parenthesis after D_ctf(G,_AX) and no comma (clean scan)",
           r"D_{\mathrm{ctf}}(G,{}_AX)$, on peut", "misprint_in_print", "medium",
           "{}_AX)$, on peut", "{}_AX)$) on peut",
           "Unbalanced parenthesis of the print; the TeX silently replaces it by a comma. The comma is the evident reading (alternatively an opening parenthesis is missing before 'avec action triviale').",
           corrected="{}_AX)$, on peut"))
L.append(F(191, "'plus fin (en un sens évident) que le terme local'", "plus fin (en un sens évident) que",
           "plus fin, en un sens évident, que", "punctuation", "high",
           "plus fin, en un sens évident, que", "plus fin (en un sens évident) que", "Parentheses became commas."))
# ---------------- page 192
L.append(F(192, "number of no. 6.10", "'6.10.' with a full stop", r"\subsection*{6.10}", "punctuation", "high",
           r"\subsection*{6.10}", r"\subsection*{6.10.}", "As 6.2. (p. 183)."))
L.append(F(192, "(6.10.1), right-hand side", "H^o(X^c;K_{X^c} ⊗ Λ[G_♮]) : a semicolon after X^c (clean scan)",
           r"=H^0(X^c,K_{X^c}\otimes\Lambda[G_{\natural}])", "misprint_in_print", "high",
           "=H^0(X^c,K_{X^c}", "=H^0(X^c;K_{X^c}",
           "The left side and the projection two lines below have the comma; the TeX silently corrects.",
           corrected="=H^0(X^c,K_{X^c}"))
L.append(F(192, "'on peut considérer la \"valeur de Tr_{Λ[G]}(u) en x\"'", "straight typewriter double quotes",
           r"« valeur de $\Tr_{\Lambda[G]}(u)$ en $x$ »", "punctuation", "high",
           r"« valeur de $\Tr_{\Lambda[G]}(u)$ en $x$ »", r"""``valeur de $\Tr_{\Lambda[G]}(u)$ en $x$''""",
           "Guillemets for the print's straight quotes."))
L.append(F(192, "after (6.10.2): 'où e désigne l'élément neutre de G . Plus généralement,'",
           "'... l'élément neutre de G . Plus généralement, soit g ∈ G , notons': one paragraph",
           "blank line before 'Plus généralement' (new paragraph)", "other", "high",
           "neutre de $G$.<NL><NL>Plus généralement", "neutre de $G$. Plus généralement",
           "Paragraph break the print does not have."))
L.append(F(192, "number of no. 6.11", "'6.11.' with a full stop", r"\subsection*{6.11}", "punctuation", "high",
           r"\subsection*{6.11}", r"\subsection*{6.11.}", "As 6.2. (p. 183)."))
L.append(F(192, "diagram (6.11.1)",
           "X x_S X <--c-- C above Y x_S Y <--d-- D: the products on the left, horizontal arrows pointing left with c and d above them, f x_S f to the left of the left vertical arrow, C -> D unlabelled on the right",
           "mirror image: C --c--> X x_S X over D --d--> Y x_S Y (d below), f x_S f on the right", "other", "high",
           r'''C \arrow[r,"c"] \arrow[d] & X\times_SX \arrow[d,"f\times_Sf"]\\<NL>D \arrow[r,"d"'] & Y\times_SY''',
           r'''X\times_SX \arrow[d,"f\times_Sf"'] & C \arrow[l,"c"'] \arrow[d]\\<NL>Y\times_SY & D \arrow[l,"d"']''',
           "Same morphisms; the TeX mirrors the printed diagram. In the new text the swapped labels (') put c and d above the leftward arrows and f x_S f on the left."))
# ---------------- page 193
L.append(F(193, "top of the page",
           "p. 193 begins with the display '(6.11.2) f^{c/d} (ou f^c) : X^c ---> Y^d', then 'le morphisme induit par 6.11.1'; p. 192 ends '... agit trivialement sur Y et D . On note'",
           "the display (6.11.2) and 'le' are the last five lines of page_192.tex (s5.tex lines 6243-6247 at the time of checking); the folio-193 marker (line 6248) follows them",
           "marker", "high", None, None,
           "Page 193 really begins at the '\\begin{equation}' of (6.11.2). Exact fix: python -I move_marker.py 5 193 '\\begin{equation}' --before (single quotes; the last \\begin{equation} before the marker is that of (6.11.2); simulated read-only on both layers: the marker then stands on its own line between '... sur $Y$ et $D$. On note' and '\\begin{equation}', no other text moves). The moved display and 'le' agree with the print."))
L.append(F(193, "'Soient L ∈ ob D_ctf(G,X) , et u ∈ Hom(...)'", "D_ctf(G,X): no index A (clean scan)",
           r"D_{\mathrm{ctf}}(G,{}_AX)", "formula", "high",
           r"D_{\mathrm{ctf}}(G,X)$, et", r"D_{\mathrm{ctf}}(G,X)$, et",
           "placeholder"))
L.append(F(193, "end of (6.11.4)", "gc =^{dfn} (gc_1 = c_1g,c_2) : C ---> X x_S X with no punctuation (only a speck below the baseline, much smaller than the page's typed full stops)",
           r"C\to X\times_SX,", "punctuation", "medium",
           r"X\times_SX,<NL>\tag{6.11.4}", r"X\times_SX<NL>\tag{6.11.4}", "Comma added by the TeX."))
L.append(F(193, "Proposition 6.12, label", "Proposition 6.12 - Sous les hypothèses de 6.11, ...",
           r"\begin{statement}{Proposition 6.12}", "punctuation", "high",
           r"\begin{statement}{Proposition 6.12}", r"\begin{statement}{Proposition 6.12 -}",
           "The print's ' -' after the label (as Lemme 2.2, p. 146)."))
L.append(F(193, "statement of Proposition 6.12, first line",
           "underlined: 'Sous les hypothèses de' | 'on suppose que l'on a'; not underlined: '6.11,'",
           "no underline", "underline", "high",
           "Sous les hypothèses de 6.11, on suppose que l'on a",
           r"\emph{Sous les hypothèses de} 6.11, \emph{on suppose que l'on a}",
           "Exposé III B has no underline markup for statements; \\emph as on pp. 146-150."))
L.append(F(193, "statement of Proposition 6.12, 'Alors, pour tout g ∈ G , on a'",
           "underlined: 'Alors' | 'pour tout' | 'on a'; not underlined: the commas, g ∈ G",
           "no underline", "underline", "high",
           r"Alors, pour tout $g\in G$, on a", r"\emph{Alors}, \emph{pour tout} $g\in G$, \emph{on a}", ""))
L.append(F(193, "statement of Proposition 6.12, after (6.12.1)",
           "underlined: 'où' | 'est le morphisme \"de Gysin\" défini par la' + 'flèche d'adjonction' (one line through the quotes); not underlined: the formulas and the full stop",
           "no underline", "underline", "high",
           r"""où<NL>\[<NL>f_*^{gc}:H^0(X^{gc},K_{X^{gc}})\longrightarrow H^0(Y^d,K_{Y^d})<NL>\]<NL>est le morphisme ``de Gysin'' défini par la flèche d'adjonction""",
           r"""\emph{où}<NL>\[<NL>f_*^{gc}:H^0(X^{gc},K_{X^{gc}})\longrightarrow H^0(Y^d,K_{Y^d})<NL>\]<NL>\emph{est le morphisme ``de Gysin'' défini par la flèche d'adjonction}""",
           "The display between the two pieces is unchanged."))
L.append(F(193, "number of no. 6.13", "'6.13.' with a full stop", r"\subsection*{6.13}", "punctuation", "high",
           r"\subsection*{6.13}", r"\subsection*{6.13.}", "As 6.2. (p. 183)."))
# ---------------- page 194
L.append(F(194, "top of the page",
           "p. 194 begins 'd'objets de D_ctf(G,X,Λ_n) tel que'; p. 193 ends '... soit L = (L_n) un système projectif'",
           "'d'%' ends the last line of page_193.tex (s5.tex line 6310); page_194.tex begins 'objets de'",
           "marker", "high", None, None,
           "Page 194 really begins at 'd'objets'. Exact fix: python -I move_marker.py 5 194 \"d'%\" --before (bash double quotes; simulated read-only on both layers: '... un système projectif ' / marker / 'd'%' / 'objets de', so the output still reads 'd'objets'). Do not use marker_split_word.py pull \"d'%\": it would put 'd'%objets' and comment out 'objets de'."))
L.append(F(194, "first line: 'L_m ⊗^L_{Λ_m} Λ_n ---~--> L_n pour m ≥ n , et soit'", "pour m ≥ n ,",
           r"L_n\quad (m\ge n),", "word", "high",
           r"L_n\quad (m\ge n),<NL>\]<NL>et soit", r"L_n<NL>\]<NL>pour $m\ge n$, et soit",
           "The word 'pour' replaced by parentheses."))
L.append(F(194, "'les termes locaux (pour g ∈ G ) Tr_{Λ_n}(gu_n)'", "(pour g ∈ G )",
           r"les termes locaux, pour $g\in G$,", "punctuation", "high",
           r"les termes locaux, pour $g\in G$,", r"les termes locaux (pour $g\in G$)", "Parentheses became commas."))
L.append(F(194, "'Supposons de plus que f_*M_n ∈ ob D_ctf(_{Λ_n[G]}Y)'", "f_*M_n (clean scan)",
           r"f_*L_n\in\Ob D_{\mathrm{ctf}}({}_{\Lambda_n[G]}Y)", "misprint_in_print", "high",
           r"f_*L_n\in\Ob", r"f_*M_n\in\Ob",
           "No M is defined (L = (L_n)); the TeX silently corrects.", corrected=r"f_*L_n\in\Ob"))
L.append(F(194, "number of no. 6.14", "'6.14.' with a full stop", r"\subsection*{6.14}", "punctuation", "high",
           r"\subsection*{6.14}", r"\subsection*{6.14.}", "As 6.2. (p. 183)."))
L.append(F(194, "6.14: 'j : U ---> X une immersion ouverte équivariante'", "j : U ---> X",
           r"$j:U\to X$", "misprint_in_print", "medium", None, None,
           "The diagram (6.14.1) labels U -> X with i and X-U -> X with j, and p. 195 uses i_!Λ_U, Λ_{U,X} = i_!Λ_U, j_*Λ_{X-U} and j^c : (X-U)^c -> X^c: the open immersion is i. The TeX keeps the printed j.",
           corrected=r"$i:U\to X$"))
L.append(F(194, "'On suppose que c_1^{-1}(U) ⊂ c_2^{-1}(U) ; on a donc'", "; on a donc", ". On a donc",
           "punctuation", "high",
           r"c_2^{-1}(U).<NL>\]<NL>On a donc", r"c_2^{-1}(U);<NL>\]<NL>on a donc",
           "Semicolon and lower-case 'on' in the print."))
L.append(F(194, "'on a donc des carré commutatifs'", "des carré commutatifs (no s)", "des carrés commutatifs",
           "misprint_in_print", "high", "des carrés commutatifs", "des carré commutatifs",
           "Agreement slip of the print; the TeX silently corrects.", corrected="des carrés commutatifs"))
L.append(F(194, "diagram (6.14.1), vertical arrows",
           "all seven vertical arrows are hooked (inclusions): U -> X (i), c_1^{-1}(U) -> c_2^{-1}(U), c_2^{-1}(U) -> C, U -> X (right) with the hook at the top; X-U -> X (j), c_2^{-1}(X-U) -> C, X-U -> X (right) with the hook at the bottom; the horizontal arrows are plain",
           r"all arrows \draw[->] (no hooks)", "symbol", "high", blk_old, blk_new,
           "Hooks[right] is the arrows.meta tip (loaded by tikz-cd); the side of the hook is a glyph detail. Only the seven vertical arrows change."))
L.append(F(194, "after diagram (6.14.1)", "a full stop to the right of the bottom row", "nothing after the diagram",
           "punctuation", "high", r"\end{tikzpicture}<NL>\tag{6.14.1}", r"\end{tikzpicture}\quad.<NL>\tag{6.14.1}",
           "Full stop dropped."))
# ---------------- page 195
L.append(F(195, "filtration of Λ_X", "i_!Λ_U (i.e. F^nΛ_X = Λ_X pour n ≤ 0 , F^1Λ_X = i_!Λ_U , F^nΛ_X = 0 pour n ≥ 1 ) .",
           r"$i_!\Lambda_U$, c'est-à-dire \[ F^n\Lambda_X=\Lambda_X\quad(n\le0),\qquad F^1\Lambda_X=i_!\Lambda_U,\qquad F^n\Lambda_X=0\quad(n\ge1). \]",
           "word", "high",
           r"$i_!\Lambda_U$, c'est-à-dire<NL>\[<NL>F^n\Lambda_X=\Lambda_X\quad(n\le0),\qquad<NL>F^1\Lambda_X=i_!\Lambda_U,\qquad<NL>F^n\Lambda_X=0\quad(n\ge1).<NL>\]",
           r"$i_!\Lambda_U$ (i.e. $F^n\Lambda_X=\Lambda_X$ pour $n\le0$, $F^1\Lambda_X=i_!\Lambda_U$, $F^n\Lambda_X=0$ pour $n\ge1$).",
           "The print's abbreviation 'i.e.' written out as 'c'est-à-dire', the parentheses dropped, 'pour n ≤ 0' and 'pour n ≥ 1' set as (n\\le0), (n\\ge1). The printed 'n ≥ 1' is a misprint (next finding)."))
L.append(F(195, "filtration of Λ_X: 'F^nΛ_X = 0 pour n ≥ 1'", "n ≥ 1 (clean scan)", r"(n\ge1)",
           "misprint_in_print", "high", None, None,
           "Contradicts F^1Λ_X = i_!Λ_U and gr^1 = i_!Λ_U (6.14.3): F^n = 0 for n ≥ 2. The TeX keeps the printed 1. The corrected reading is given for the text after the word fix above.",
           corrected=r"$F^n\Lambda_X=0$ pour $n\ge2$"))
L.append(F(195, "(6.14.3)",
           "gr^oc = c_{X-U,X} ∈ Hom(c*_1(Λ_{X-U,X}),c^!_2(Λ_{X-U,X})) , / gr^1c = c_{U,X} ∈ Hom(c*_1(Λ_{U,X}),c^!_2(Λ_{X-U,X})) , with the number (6.14.3) at the first line",
           "no parentheses around the Λ's; the first line unnumbered, \\tag{6.14.3} on the second", "formula", "high",
           r"\[<NL>\operatorname{gr}^0\underline c=\underline c_{X-U,X}<NL>\in\Hom(c_1^*\Lambda_{X-U,X},c_2^!\Lambda_{X-U,X}),<NL>\]<NL>\begin{equation}<NL>\operatorname{gr}^1\underline c=\underline c_{U,X}<NL>\in\Hom(c_1^*\Lambda_{U,X},c_2^!\Lambda_{X-U,X}),<NL>\tag{6.14.3}<NL>\end{equation}",
           r"\begin{equation}<NL>\operatorname{gr}^0\underline c=\underline c_{X-U,X}<NL>\in\Hom(c_1^*(\Lambda_{X-U,X}),c_2^!(\Lambda_{X-U,X})),<NL>\tag{6.14.3}<NL>\end{equation}<NL>\[<NL>\operatorname{gr}^1\underline c=\underline c_{U,X}<NL>\in\Hom(c_1^*(\Lambda_{U,X}),c_2^!(\Lambda_{X-U,X})),<NL>\]",
           "Four pairs of parentheses dropped, and the number moved to the second line; one edit for both. The second argument of the gr^1 line is a misprint of the print (next finding)."))
L.append(F(195, "(6.14.3), second line: c^!_2(Λ_{X-U,X})", "gr^1c = c_{U,X} ∈ Hom(c*_1(Λ_{U,X}),c^!_2(Λ_{X-U,X}))",
           r"c_2^!\Lambda_{X-U,X}", "misprint_in_print", "high", None, None,
           "gr^1 c is a correspondence from Λ_{U,X} to Λ_{U,X}: the print repeats the target of the line above. The TeX keeps the printed reading; corrected reading for the text after the formula fix above.",
           corrected=r"c_2^!(\Lambda_{U,X})"))
L.append(F(195, "(6.14.4)", "c_{X-U,U} = j_*c_{X-U} : index X-U,U (clean scan)", r"\underline c_{X-U,X}=j_*\underline c_{X-U},",
           "misprint_in_print", "high", r"\underline c_{X-U,X}=j_*", r"\underline c_{X-U,U}=j_*",
           "The correspondence is c_{X-U,X} (6.14.3, 6.14.5-6.14.7); the TeX silently corrects.",
           corrected=r"\underline c_{X-U,X}=j_*"))
L.append(F(195, "'Nous écrirons c , c_{U,X} , etc. , quand nous voudrons préciser l'anneau de base.'",
           "c and c_{U,X} without an index of the ring, a typed gap after each (handwritten symbols not filled in)",
           r"$\underline c$, $\underline c_{U,X}$, etc.", "misprint_in_print", "low", None, None,
           "Without the ring index the sentence introduces no notation; p. 196 writes c_ℓ, c_{ℓ,U,X}, c_{ℓ,X-U}. The TeX keeps the printed reading; the corrected reading is inferred, hence low confidence.",
           corrected=r"$\underline c_{\Lambda}$, $\underline c_{\Lambda,U,X}$"))
L.append(F(195, "'Rappelons (III 4.3) que si X est lisse,'", "que si (no comma)", "que, si",
           "punctuation", "high", "(III 4.3) que, si", "(III 4.3) que si", "Comma added by the TeX."))
L.append(F(195, "end of the page",
           "p. 195 ends '... alors la formule de Lefschetz'; p. 196 begins '(III 4.7) entraîne que' (page_196_s1.png)",
           "'Lefschetz' opens the line after the folio-196 marker (s5.tex line 6484 at the time of checking); page_195.tex ends 'alors la formule de'",
           "marker", "high", None, None,
           "Page 196 really begins at '(III 4.7) entraîne que'. Exact fix: python -I move_marker.py 5 196 '(III 4.7) entraîne' (no --before; simulated read-only on both layers: '... alors la formule de' / 'Lefschetz ' / marker / '(III 4.7) entraîne que'; no other text moves)."))

# p. 193 'D_ctf(G,X)': old and new must differ
for d in L:
    if d["note"] == "placeholder":
        d["fix"] = {"old": r"D_{\mathrm{ctf}}(G,{}_AX)$, et", "new": r"D_{\mathrm{ctf}}(G,X)$, et"}
        d["note"] = "The TeX adds an index A that the print does not have (the coefficients here are Λ: f_*u ∈ Hom_{Λ[G]})."

# ---------------- checks
bad = 0
spans = {}
for i, d in enumerate(L):
    for k, v in d.items():
        vals = [v] if isinstance(v, str) else (list(v.values()) if isinstance(v, dict) else [])
        for x in vals:
            if any(ord(c) < 32 and c != "\n" for c in x):
                print("CONTROL CHAR in", i, k, repr(x)); bad += 1
    if d["fix"]:
        t = pages[d["page"]]
        o, n = d["fix"]["old"], d["fix"]["new"]
        c = t.count(o)
        if c != 1:
            print("COUNT", c, "page", d["page"], repr(o)); bad += 1
            continue
        if o == n:
            print("old == new", i); bad += 1
        if "%%%%%%%%%%  scan idx" in o:
            print("marker line in old", i); bad += 1
        a = t.find(o)
        spans.setdefault(d["page"], []).append((a, a + len(o), i))
for p, sp in spans.items():
    sp.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(sp, sp[1:]):
        if a2 < b1:
            print("OVERLAP page", p, i1, i2); bad += 1
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
cnt = {}
for d in L:
    c = cnt.setdefault(d["page"], [0, 0])
    c[d["kind"] == "misprint_in_print"] += 1
print("findings:", len(L), "problems:", bad)
print({p: f"{a}/{b}" for p, (a, b) in sorted(cnt.items())})
