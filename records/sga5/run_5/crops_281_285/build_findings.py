"""Build findings_281_285.json; check that every fix's 'old' occurs exactly once in its page_NNN.tex
(and, for information, once in that page's span of the live diplomatic and current s5.tex).
Strings are raw; the character '¶' stands for a line break (LF) and is replaced before writing."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b281_285"
OUT = RUN / "findings_281_285.json"
NL = "¶"


def F(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if corrected is not None:
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    return d


R_NOTE = r"Plain typewriter R (one stem); \R is \mathbb{R} in this file (double-struck). The hand-drawn double-struck R of the print occurs only in Rp_* (proof of 1.2), R_!p and Rf_* (p. 285)."

L = []
# ---------------------------------------------------------------- p. 281
L.append(F(281, "exposé heading (printed at the top of p. 282; in page_281.tex as the files stand)",
    "'E X P O S E  VII': letter-spaced capitals, dashed underline (the typescript's capital E has no accent)",
    r"\section*{Exposé VII}", "word", "high",
    r"\section*{Exposé VII}", r"\section*{EXPOSÉ VII}",
    "Capitals as printed, as the logged EXPOSÉ V (p. 204) and EXPOSÉ VI (p. 250); accented capital as the volume's rule. "
    "Filed under p. 281, where the line stands now. Independent of the marker move of p. 282 (its anchor '\\section*{E' "
    "matches before and after this edit)."))

# ---------------------------------------------------------------- p. 282
L.append(F(282, "top of the page: the heading EXPOSÉ VII",
    "p. 282 begins with 'E X P O S E  VII', then the title 'COHOMOLOGIE DE QUELQUES SCHEMAS CLASSIQUES / ET / THEORIE "
    "COHOMOLOGIQUE DES CLASSES DE CHERN', 'par', 'J. P. JOUANOLOU'; p. 281 ends with the two footnotes (*) and (**)",
    r"'\section*{Exposé VII}' and '\begin{center}' end page_281.tex (after '\end{flushleft}' of the footnotes); the "
    r"folio-282 marker stands inside the center environment, before '\textbf{COHOMOLOGIE'",
    "marker", "high", None, None,
    "Page 282 really begins at '\\section*{Exposé VII}' (diplomatic s5.tex line 9358, current 9353, at the time of the "
    "check; the file is being edited, line numbers move). Exact fix: python -I move_marker.py 5 282 '\\section*{E' "
    "--before (simulated in memory on both layers, before and after the EXPOSÉ VII capitals fix filed under p. 281: the "
    "marker then stands on its own line between the blank lines after '\\end{flushleft}' and '\\section*{Exposé VII}', and "
    "the center environment is whole on p. 282). Text not moved."))
L.append(F(282, "byline",
    "'J. P. JOUANOLOU': a space between the initials, no hyphen, surname in capitals",
    r"J.-P. Jouanolou", "word", "high",
    r"J.-P. Jouanolou", r"J. P. JOUANOLOU",
    "As the logged bylines of Exposés V and VI (pp. 204, 251: 'par J.P. JOUANOLOU'); here the print has a space after 'J.'."))
L.append(F(282, "'on note μ_X le faisceau des racines ν^èmes de l'unité'",
    "ν with a raised 'èmes' (no hyphen, no i)", r"$\nu$-ièmes", "word", "high",
    r"$\nu$-ièmes", r"$\nu^{\text{èmes}}$", ""))
L.append(F(282, "section title 1",
    "'1. FIBRES VECTORIELS': hand-drawn capitals, underlined, no full stop",
    r"\subsection*{1. Fibres vectoriels}", "word", "high",
    r"\subsection*{1. Fibres vectoriels}", r"\subsection*{1. FIBRES VECTORIELS}",
    "Capitals as printed (as the title of Exposé V, p. 204). The same for '2. SCHEMAS PROJECTIFS' on p. 285."))
L.append(F(282, "'E un O_S-Module localement libre'",
    "Module with a capital M", r"$\mathcal O_S$-module", "word", "high",
    r"$\mathcal O_S$-module", r"$\mathcal O_S$-Module",
    "The typescript's capital M (sheaf of modules), as the logged 'Module' of pp. 159, 263, 267. The O is a plain typed O "
    "here (no underline): see the message."))
L.append(F(282, "'localement libre (sous-entendu : de type fini).'",
    "parentheses, and a colon after 'sous-entendu'",
    r"libre, sous-entendu de type fini.", "punctuation", "high",
    r"libre, sous-entendu de type fini.", r"libre (sous-entendu : de type fini).",
    "The TeX turns the parenthesis into commas and drops the colon."))
L.append(F(282, "'U = V(E)* (complémentaire de la section nulle) et on'",
    "parentheses, no comma", r"$U=\V(E)^*$, complémentaire de la section nulle, et on", "punctuation", "high",
    r", complémentaire de la section nulle, et", r" (complémentaire de la section nulle) et",
    "The TeX turns the parenthesis into commas."))

# ---------------------------------------------------------------- p. 283
L.append(F(283, "first line: 'note p : X → S et q : U → S les projections canoniques.'",
    "'et' between the two maps, no comma",
    r"p:X\to S,  \qquad  q:U\to S (display)", "missing", "high",
    r"p:X\to S,¶\qquad¶q:U\to S", r"p:X\to S¶\quad\text{et}\quad¶q:U\to S",
    "The TeX drops the word 'et' and adds a comma. (Inline in the print; the display is not reported.)"))
L.append(F(283, "Proposition 1.1, first sentence 'Soit L un A-Module.'",
    "'Soit', 'un' and 'Module' underlined (L and 'A-' not); Module with a capital M",
    r"Soit $L$ un $A$-module.", "underline", "high",
    r"Soit $L$ un $A$-module.", r"\emph{Soit} $L$ \emph{un} $A$-\emph{Module}.",
    "Exposé VII: the TeX has no underline markup for statements; \\emph is the file's command here (as \\emph{Preuve} "
    "and the logged statements of Exposé V). One edit: it also gives the print's capital M (word)."))
L.append(F(283, "Proposition 1.1 (i) a), 'Pour tout entier j>0 on a'",
    "'Pour tout entier' underlined", r"\item Pour tout entier $j>0$", "underline", "high",
    r"\item Pour tout entier", r"\item \emph{Pour tout entier}", ""))
L.append(F(283, "Proposition 1.1 (i) a), 'j > 0  on a'",
    "no comma after j > 0; 'on a' underlined", r"$j>0$, on a", "punctuation", "high",
    r"$j>0$, on a", r"$j>0$ \emph{on a}",
    "The TeX adds a comma. The edit also underlines 'on a', as printed."))
L.append(F(283, "Proposition 1.1 (i) a), R^j p_*(p^*L) = 0", "R^j: plain typewriter R",
    r"\R^j p_*(p^*L)=0.", "font", "high",
    r"\R^j p_*(p^*L)=0.", r"\mathrm{R}^j p_*(p^*L)=0.", R_NOTE))
L.append(F(283, "Proposition 1.1 (i) b)",
    "'Le morphisme d'adjonction' and 'est un isomorphisme' underlined",
    "no underline markup", "underline", "high",
    r"\item Le morphisme d'adjonction¶\[¶L\longrightarrow p_*p^*(L)¶\]¶est un isomorphisme.",
    r"\item \emph{Le morphisme d'adjonction}¶\[¶L\longrightarrow p_*p^*(L)¶\]¶\emph{est un isomorphisme}.", ""))
L.append(F(283, "Proposition 1.1 (ii), 'On suppose E de rang constant r .'",
    "'On suppose' and 'de rang constant' underlined", "no underline markup", "underline", "high",
    r"\item On suppose $E$ de rang constant $r$.", r"\item \emph{On suppose} $E$ \emph{de rang constant} $r$.", ""))
L.append(F(283, "Proposition 1.1 (ii) a), R^i_! p(p^*L) = 0", "plain typewriter R",
    r"\R_!^i p(p^*L)=0", "font", "high",
    r"\R_!^i p(p^*L)=0", r"\mathrm{R}_!^i p(p^*L)=0", R_NOTE))
L.append(F(283, "Proposition 1.1 (ii) a), 'si i ≠ 2r'", "'si' underlined", r"\text{si }i\ne 2r.", "underline", "high",
    r"\text{si }i\ne 2r.", r"\text{\emph{si} }i\ne 2r.", ""))
L.append(F(283, "Proposition 1.1 (ii) b), 'Le morphisme trace (SGA 4 XVIII)'",
    "'Le morphisme trace' underlined, the reference not", "no underline markup", "underline", "high",
    r"\item Le morphisme trace (SGA 4 XVIII)", r"\item \emph{Le morphisme trace} (SGA 4 XVIII)", ""))
L.append(F(283, "Proposition 1.1 (ii) b), display R^{2r}_! p(p^*L) → L ⊗ μ_S^{⊗-r}", "plain typewriter R",
    r"\R_!^{2r}p(p^*L)", "font", "high",
    r"\R_!^{2r}p(p^*L)", r"\mathrm{R}_!^{2r}p(p^*L)", R_NOTE))
L.append(F(283, "Proposition 1.1 (ii) b), 'est un isomorphisme.' after the display", "underlined",
    "no underline markup", "underline", "high",
    r"\mu_S^{\otimes -r}¶\]¶est un isomorphisme.", r"\mu_S^{\otimes -r}¶\]¶\emph{est un isomorphisme}.", ""))
L.append(F(283, "Corollaire 1.2, statement before the display",
    "underlined: 'Soit' | 'un' | 'Module. Pour tout entier' | 'le morphisme image réciproque'; L, A_S-, i not; Module "
    "with a capital M", r"Soit $L$ un $A_S$-module. Pour tout entier $i$, le morphisme image réciproque", "underline", "high",
    r"Soit $L$ un $A_S$-module. Pour tout entier $i$, le morphisme image réciproque",
    r"\emph{Soit} $L$ \emph{un} $A_S$-\emph{Module. Pour tout entier} $i$, \emph{le morphisme image réciproque}",
    "One edit: it also gives the print's capital M (word)."))
L.append(F(283, "Corollaire 1.2, 'est un isomorphisme.' after the display", "underlined", "no underline markup",
    "underline", "high",
    r"H^i(X,p^*L)¶\]¶est un isomorphisme.", r"H^i(X,p^*L)¶\]¶\emph{est un isomorphisme}.", ""))
L.append(F(283, "Proposition 1.3, first sentences",
    "'... Pour tout A_S-Module L , les propriétés suivantes sont vérifiées :': underlined 'Supposons' | 'de rang "
    "constant' | 'Pour tout' | 'Module' | 'les propriétés suivantes sont vérifiées'; Module with a capital M; a colon at "
    "the end", r"... Pour tout $A_S$-module $L$, les propriétés suivantes sont vérifiées.", "underline", "high",
    r"Supposons $E$ de rang constant $r$. Pour tout $A_S$-module $L$, les propriétés suivantes sont vérifiées.",
    r"\emph{Supposons} $E$ \emph{de rang constant} $r$. \emph{Pour tout} $A_S$-\emph{Module} $L$, \emph{les propriétés suivantes sont vérifiées} :",
    "One edit: it also gives the capital M (word) and the print's colon for the TeX's full stop (punctuation)."))
L.append(F(283, "Proposition 1.3 (i) a), R^i q_*(q^*L) = 0", "plain typewriter R",
    r"\R^i q_*(q^*L)=0", "font", "high",
    r"\R^i q_*(q^*L)=0", r"\mathrm{R}^i q_*(q^*L)=0", R_NOTE))
L.append(F(283, "Proposition 1.3 (i) a), 'si i ≠ 0 , 2r-1'", "'si' underlined", r"\text{si }i\ne 0,2r-1.",
    "underline", "high", r"\text{si }i\ne 0,2r-1.", r"\text{\emph{si} }i\ne 0,2r-1.", ""))
L.append(F(283, "Proposition 1.3 (i) b)",
    "'Le morphisme d'adjonction' and 'est un isomorphisme' underlined", "no underline markup", "underline", "high",
    r"\item Le morphisme d'adjonction¶\[¶L\longrightarrow q_*q^*(L)¶\]¶est un isomorphisme.",
    r"\item \emph{Le morphisme d'adjonction}¶\[¶L\longrightarrow q_*q^*(L)¶\]¶\emph{est un isomorphisme}.", ""))
L.append(F(283, "Proposition 1.3 (i) c), 'Désignant par Y le complémentaire de U'",
    "'Désignant par' and 'le complémentaire de' underlined", "no underline markup", "underline", "high",
    r"\item Désignant par $Y$ le complémentaire de $U$", r"\item \emph{Désignant par} $Y$ \emph{le complémentaire de} $U$",
    "The rest of the line ('dans X , le morphisme' and the display) is printed on p. 283 too but stands in page_284.tex: "
    "filed under p. 284."))

# ---------------------------------------------------------------- p. 284
L.append(F(284, "top of the page: 'composé du morphisme \"bord\",'",
    "p. 284 begins with 'composé du morphisme \"bord\",' (then the display (1)); p. 283 ends with '... dans X , le "
    "morphisme' and the display 'R^{2r-1} q_*(q^*L) → L ⊗ μ_S^{⊗-r}'",
    r"page_284.tex begins 'dans $X$, le morphisme' and the display '\R^{2r-1}q_*(q^*L)\longrightarrow L\otimes\mu_S^{\otimes -r}' (printed on p. 283)",
    "marker", "high", None, None,
    "Page 284 really begins at 'composé du morphisme bord' (the first line after that display). Exact fix: python -I "
    "move_marker.py 5 284 'composé du morphisme' (no --before; run it before the underline fix of that line, after which "
    "the anchor is '\\emph{composé du morphisme'). Simulated in memory on both layers, both ways: the marker then stands "
    "on its own line between '\\]' and the line 'composé du morphisme ...'. Text not moved; the text that moves to p. 283 is checked "
    "there: its underline and plain R are the next two items."))
L.append(F(284, "Proposition 1.3 (i) c), 'dans X , le morphisme' (printed on p. 283)",
    "'dans' and 'le morphisme' underlined", "no underline markup", "underline", "high",
    r"dans $X$, le morphisme", r"\emph{dans} $X$, \emph{le morphisme}",
    "Filed under p. 284, where the line stands until the marker move; the edit does not touch the move's anchor."))
L.append(F(284, "display R^{2r-1} q_*(q^*L) → L ⊗ μ_S^{⊗-r} (printed at the foot of p. 283)", "plain typewriter R",
    r"\R^{2r-1}q_*(q^*L)\longrightarrow L", "font", "high",
    r"\R^{2r-1}q_*(q^*L)\longrightarrow L", r"\mathrm{R}^{2r-1}q_*(q^*L)\longrightarrow L",
    R_NOTE + " Filed under p. 284, where the display stands until the marker move."))
L.append(F(284, "'composé du morphisme \"bord\",'",
    "'bord' in typewriter double quotes and a comma after it; 'composé du morphisme \"bord\"' underlined (the comma not)",
    r"composé du morphisme bord", "punctuation", "high",
    r"composé du morphisme bord", r"\emph{composé du morphisme ``bord''},",
    "The TeX drops the quotes and the comma; the edit also gives the underline. ``...'' as the file's 'd'``algèbre "
    "généralisée''' (p. 285). Apply after the marker move of p. 284 or use the anchor given there."))
L.append(F(284, "display (1), R^{2r-1} q_*(q^*L) → R^{2r}_Y p_*(p^*L)", "both R plain typewriter R",
    r"\R^{2r-1}q_*(q^*L)\longrightarrow \R_Y^{2r}p_*(p^*L)", "font", "high",
    r"\R^{2r-1}q_*(q^*L)\longrightarrow \R_Y^{2r}p_*(p^*L)",
    r"\mathrm{R}^{2r-1}q_*(q^*L)\longrightarrow \mathrm{R}_Y^{2r}p_*(p^*L)", R_NOTE))
L.append(F(284, "'et de l'isomorphisme de pureté (SGA 4 XVIII)'",
    "'et de l'isomorphisme de pureté' underlined, the reference not", "no underline markup", "underline", "high",
    r"et de l'isomorphisme de pureté (SGA 4 XVIII)", r"\emph{et de l'isomorphisme de pureté} (SGA 4 XVIII)", ""))
L.append(F(284, "display R^{2r}_Y p_*(p^*L) → L ⊗ μ_S^{⊗-r}", "plain typewriter R",
    r"\R_Y^{2r}p_*(p^*L)\longrightarrow L", "font", "high",
    r"\R_Y^{2r}p_*(p^*L)\longrightarrow L", r"\mathrm{R}_Y^{2r}p_*(p^*L)\longrightarrow L", R_NOTE))
L.append(F(284, "Proposition 1.3 (i) c), 'est un isomorphisme.'", "underlined", "no underline markup", "underline", "high",
    r"est un isomorphisme.¶\end{enumerate}¶\item", r"\emph{est un isomorphisme}.¶\end{enumerate}¶\item", ""))
L.append(F(284, "Proposition 1.3 (ii) a), R^i_! q(q^*L) = 0", "plain typewriter R",
    r"\R_!^i q(q^*L)=0", "font", "high",
    r"\R_!^i q(q^*L)=0", r"\mathrm{R}_!^i q(q^*L)=0", R_NOTE))
L.append(F(284, "Proposition 1.3 (ii) a), 'si i ≠ (1,2r) .'",
    "'(1,2r)' in parentheses; 'si' underlined", r"\text{si }i\ne 1,2r.", "formula", "high",
    r"\text{si }i\ne 1,2r.", r"\text{\emph{si} }i\ne (1,2r).",
    "The TeX drops the parentheses; the edit also underlines 'si'."))
L.append(F(284, "Proposition 1.3 (ii) b), 'Le morphisme bord'", "underlined", "no underline markup", "underline", "high",
    r"\item Le morphisme bord", r"\item \emph{Le morphisme bord}", ""))
L.append(F(284, "Proposition 1.3 (ii) b), L ⟶ R^1_! q(q^*L)", "plain typewriter R",
    r"L\longrightarrow \R_!^1 q(q^*L)", "font", "high",
    r"L\longrightarrow \R_!^1 q(q^*L)", r"L\longrightarrow \mathrm{R}_!^1 q(q^*L)", R_NOTE))
L.append(F(284, "Proposition 1.3 (ii) b), 'provenant de la suite exacte illimitée (f : Y ⟶ S proj. can.)'",
    "the abbreviation in parentheses: '(f : Y ⟶ S proj. can.)'; 'provenant de la suite exacte illimitée' and 'proj. can' "
    "underlined (f : Y ⟶ S and the final stop not)",
    r"provenant de la suite exacte illimitée, où $f:Y\to S$ est la projection canonique,", "word", "high",
    r"provenant de la suite exacte illimitée, où $f:Y\to S$ est la projection canonique,",
    r"\emph{provenant de la suite exacte illimitée} ($f:Y\to S$ \emph{proj. can}.)",
    "The TeX writes the abbreviation out as a clause; the edit also gives the underlines."))
L.append(F(284, "Proposition 1.3 (ii) b), the exact sequence",
    "'⟶ R^i_! q(q^*L) → R^i_! p(p^*L) → R^i f_*(f^*L) → R^{i+1}_! q(q^*L) → ...': no dots before the first arrow; all "
    "four R plain typewriter R", r"\cdots\longrightarrow \R_!^i q(q^*L)... (leading \cdots, \R)", "extra", "high",
    r"\cdots\longrightarrow \R_!^i q(q^*L)\longrightarrow \R_!^i p(p^*L)¶\longrightarrow \R^i f_*(f^*L)\longrightarrow \R_!^{i+1}q(q^*L)",
    r"\longrightarrow \mathrm{R}_!^i q(q^*L)\longrightarrow \mathrm{R}_!^i p(p^*L)¶\longrightarrow \mathrm{R}^i f_*(f^*L)\longrightarrow \mathrm{R}_!^{i+1}q(q^*L)",
    "The TeX adds '\\cdots' at the start. One edit with the four plain R (font)."))
L.append(F(284, "Proposition 1.3 (ii) b) 'est un isomorphisme.' and (ii) c) 'Le morphisme trace'",
    "both underlined", "no underline markup", "underline", "high",
    r"est un isomorphisme.¶\item Le morphisme trace", r"\emph{est un isomorphisme}.¶\item \emph{Le morphisme trace}", ""))
L.append(F(284, "Proposition 1.3 (ii) c), display R^{2r}q(q^*L) → L ⊗ μ_S^{⊗-r}", "plain typewriter R",
    r"\R^{2r}q(q^*L)\longrightarrow", "font", "high",
    r"\R^{2r}q(q^*L)\longrightarrow", r"\mathrm{R}^{2r}q(q^*L)\longrightarrow",
    R_NOTE + r" Listed before the misprint item on the same R. The current layer already reads \R_!^{2r}q there: its old is '\R_!^{2r}q(q^*L)\longrightarrow'."))
L.append(F(284, "Proposition 1.3 (ii) c), display R^{2r}q(q^*L) → L ⊗ μ_S^{⊗-r}",
    "R^{2r} q(q^*L): no '!' under the R (the '!' is clear under the R of (ii) a) and b) and of 1.1 (ii))",
    r"\R^{2r}q(q^*L) (the printed reading)", "misprint_in_print", "medium", None, None,
    "The trace morphism is defined on R^{2r}_! q (as R^{2r}_! p in 1.1 (ii) b)); R^{2r} q_* vanishes by (i) a). The TeX "
    r"keeps the printed reading; the current layer already has \R_!^{2r}q. Corrected reading given after the font fix of the previous item.",
    corrected=r"\mathrm{R}_!^{2r}q(q^*L)"))
L.append(F(284, "Proposition 1.3 (ii) c), 'est un isomorphisme.'", "underlined", "no underline markup", "underline", "high",
    r"est un isomorphisme.¶\end{enumerate}¶\end{enumerate}", r"\emph{est un isomorphisme}.¶\end{enumerate}¶\end{enumerate}", ""))
L.append(F(284, "proof of 1.3, 'que, posant F = p*(L) , on a :'", "colon after 'on a'",
    r"posant $F=p^*(L)$, on a", "punctuation", "high",
    r"posant $F=p^*(L)$, on a", r"posant $F=p^*(L)$, on a :", "The TeX drops the colon before the display."))
L.append(F(284, "proof of 1.3, display '... et (R^jα_*)α^*(F) = 0 si j ≠ 0,2r-1'", "plain typewriter R",
    r"(\R^j\alpha_*)\alpha^*(F)=0", "font", "high",
    r"(\R^j\alpha_*)\alpha^*(F)=0", r"(\mathrm{R}^j\alpha_*)\alpha^*(F)=0", R_NOTE))
L.append(F(284, "proof of 1.3, end of the display '... si j ≠ 0,2r-1 ,'",
    "a comma (dot on the baseline with a tail below; no upper dot), although the next sentence 'Par ailleurs' begins "
    "with a capital", r"j\ne0,2r-1.", "misprint_in_print", "medium",
    r"j\ne0,2r-1.", r"j\ne0,2r-1,",
    "Typing error, comma for full stop; the TeX silently gives the stop. Drop this item if the mark is read as a stop "
    "with a speck under it.", corrected=r"j\ne0,2r-1."))
L.append(F(284, "proof of 1.3, 'les faisceaux (R^jα_*)(α^*F) pour j ≥ 1'", "plain typewriter R",
    r"$(\R^j\alpha_*)\alpha^*F$", "font", "high",
    r"faisceaux $(\R^j", r"faisceaux $(\mathrm{R}^j", R_NOTE))
L.append(F(284, "proof of 1.3, 'les faisceaux (R^jα_*)(α^*F) pour j ≥ 1'", "(α^*F) in parentheses",
    r"$(\R^j\alpha_*)\alpha^*F$", "formula", "high",
    r"\alpha_*)\alpha^*F$ pour", r"\alpha_*)(\alpha^*F)$ pour", "The TeX drops the parentheses."))
L.append(F(284, "proof of 1.3, Leray spectral sequence R^i p_*(R^jα_*)(q^*L) ⇒ R^n q_*(q^*L)", "all three R plain typewriter R",
    r"\R^i p_*\bigl(\R^j\alpha_*\bigr)(q^*L)\Longrightarrow \R^n q_*(q^*L)", "font", "high",
    r"\R^i p_*\bigl(\R^j\alpha_*\bigr)(q^*L)\Longrightarrow \R^n q_*(q^*L)",
    r"\mathrm{R}^i p_*\bigl(\mathrm{R}^j\alpha_*\bigr)(q^*L)\Longrightarrow \mathrm{R}^n q_*(q^*L)", R_NOTE))
L.append(F(284, "proof of 1.3, the exact sequence after 'la suite exacte illimitée'",
    "'⟶ R^i_Y p_*(p^*L) → R^i p_*(p^*L) → R^i q_*(q^*L) → R^{i+1}_Y p_*(p^*L) → ... .': no dots before the first arrow; "
    "all four R plain typewriter R", r"\cdots\longrightarrow \R_Y^i p_*(p^*L)... (leading \cdots, \R)", "extra", "high",
    r"\cdots\longrightarrow \R_Y^i p_*(p^*L)\longrightarrow \R^i p_*(p^*L)\longrightarrow \R^i q_*(q^*L)¶\longrightarrow \R_Y^{i+1}p_*(p^*L)",
    r"\longrightarrow \mathrm{R}_Y^i p_*(p^*L)\longrightarrow \mathrm{R}^i p_*(p^*L)\longrightarrow \mathrm{R}^i q_*(q^*L)¶\longrightarrow \mathrm{R}_Y^{i+1}p_*(p^*L)",
    "The TeX adds '\\cdots' at the start. One edit with the four plain R (font)."))
L.append(F(284, "footnote at the foot of the page",
    "below a rule: '(*) Le faisceau R^{2r}_Y p_*(p^*L) est associé au préfaisceau U ↦ H^{2r}_{Y×_S U}(X ×_S U, p^*L) .'; "
    "no (*) call is visible in the text of pp. 284-285",
    r"'Le faisceau ...' runs on as a paragraph of the proof, without the mark (*)", "missing", "high",
    r"\]¶Le faisceau", r"\]¶¶\(\quad (*)\) Le faisceau",
    "The footnote mark, written as the file writes the footnotes of p. 281. The footnote has no call in the print."))
L.append(F(284, "footnote, 'Le faisceau R^{2r}_Y p_*(p^*L)'", "plain typewriter R",
    r"$\R_Y^{2r}p_*(p^*L)$", "font", "high",
    r"$\R_Y^{2r}p_*(p^*L)$ est associé", r"$\mathrm{R}_Y^{2r}p_*(p^*L)$ est associé", R_NOTE))

# ---------------------------------------------------------------- p. 285
L.append(F(285, "'les assertions ii) a) et b).'", "'ii)' without the opening parenthesis",
    r"(ii) a) et b).", "misprint_in_print", "high",
    r"(ii) a) et b).", r"ii) a) et b).",
    "Typing error; the TeX silently corrects it (the proof writes '(i) a) et b)' on p. 284).", corrected=r"(ii) a) et b)."))
L.append(F(285, "Remarque 1.4, 'Pour S = spec(C)'", "'spec' with a small s", r"\operatorname{Spec}(\mathbb C)", "word", "high",
    r"\operatorname{Spec}(\mathbb C)", r"\operatorname{spec}(\mathbb C)", ""))
L.append(F(285, "Remarque 1.4, 'rétracte par déformation de C^r ∸ 0 .'",
    "a typed dot centred over the minus sign (∸)", r"\mathbb C^r-0", "symbol", "low",
    r"\mathbb C^r-0", r"\mathbb C^r\mathbin{\dot{-}}0",
    "The dot is crisp and centred over the dash. Drop this item if it is read as a stray typed mark."))
L.append(F(285, "label of Corollaire 1.5", "'COROLLAIRE 1.5. (Suite exacte de GYSIN)-': capital S, GYSIN in capitals",
    r"\begin{statement}{Corollaire 1.5 (suite exacte de Gysin)}", "word", "high",
    r"(suite exacte de Gysin)}", r"(Suite exacte de GYSIN)}",
    "The print's stop after '1.5' and the final '-' belong to the label convention of Exposé VII (message)."))
L.append(F(285, "Corollaire 1.5, 'La suite spectrale de Leray'", "underlined", "no underline markup", "underline", "high",
    r"La suite spectrale de Leray", r"\emph{La suite spectrale de Leray}", ""))
L.append(F(285, "Corollaire 1.5, display H^i(S, R^j q_*(q^*L)) ⇒ H^{i+j}(U,q^*L)", "R^j: plain typewriter R",
    r"H^i(S,\R^j q_*(q^*L))", "font", "high",
    r"H^i(S,\R^j q_*(q^*L))", r"H^i(S,\mathrm{R}^j q_*(q^*L))", R_NOTE))
L.append(F(285, "Corollaire 1.5, 'définit une suite exacte illimitée (appelée suite exacte de Gysin)'",
    "the parenthesis, no commas; 'définit une suite exacte illimitée' underlined",
    r"définit une suite exacte illimitée, appelée suite exacte de Gysin,", "punctuation", "high",
    r"définit une suite exacte illimitée, appelée suite exacte de Gysin,",
    r"\emph{définit une suite exacte illimitée} (appelée suite exacte de Gysin)",
    "The TeX turns the parenthesis into commas; the edit also gives the underline."))
L.append(F(285, "Corollaire 1.5, end of the Gysin sequence", "'→ H^{i+1}(S,L) → ...' with no full stop",
    r"\longrightarrow H^{i+1}(S,L)\longrightarrow\cdots.", "punctuation", "high",
    r"H^{i+1}(S,L)\longrightarrow\cdots.", r"H^{i+1}(S,L)\longrightarrow\cdots",
    "The TeX adds a full stop at the end of the display."))
L.append(F(285, "section title 2", "'2. SCHEMAS PROJECTIFS': hand-drawn capitals, underlined, no full stop",
    r"\subsection*{2. Schémas projectifs}", "word", "high",
    r"\subsection*{2. Schémas projectifs}", r"\subsection*{2. SCHÉMAS PROJECTIFS}",
    "Capitals as printed, as '1. FIBRES VECTORIELS' (p. 282); accented capital as the volume's rule."))
L.append(F(285, "end of the introductory paragraph of section 2, 'suites spectrales [6]'",
    "no full stop after [6]", r"spectrales [6].", "misprint_in_print", "high",
    r"spectrales [6].", r"spectrales [6]",
    "The typist left out the stop; the TeX silently adds it.", corrected=r"spectrales [6]."))
L.append(F(285, "numbered paragraph 2.1", "'2.1.' (with a full stop)", r"\subsubsection*{2.1}", "punctuation", "high",
    r"\subsubsection*{2.1}", r"\subsubsection*{2.1.}", "As the logged '1.1.4.' of p. 253."))
L.append(F(285, "display (2.1.1), the tensor sign",
    "⊗ with two short bars under it (no letter L); the R of Rf_* hand-drawn double-struck",
    r"\otimes^L", "symbol", "medium",
    r"\otimes^L", r"\mathbin{\underline{\underline{\otimes}}}",
    "The print has no L at the tensor sign; the two bars may be the typist's mark for the derived tensor. One decision "
    "with the later occurrences of the exposé."))
L.append(F(285, "'Notons pour cela C•(X, A_X)'", "a raised dot (bullet), as A•(X) on p. 282", r"C^*(X,A_X)", "symbol", "high",
    r"C^*(X,A_X)", r"C^{\bullet}(X,A_X)", "The TeX has a star; written like the file's A^{\\bullet}(X) of p. 282."))

# ---------------------------------------------------------------- checks
pages = {n: (B / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(281, 286)}
bad = 0
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    t = pages[d["page"]]
    c = t.count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", i, d["page"], c, repr(fx["old"][:80]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print("MARKER IN FIX", i)
    if NL in fx["old"] or NL in fx["new"]:
        print("NL LEFT", i)
# overlap check within each page: spans of olds must be disjoint
for n in range(281, 286):
    spans = []
    for i, d in enumerate(L):
        if d["page"] == n and d["fix"]:
            k = pages[n].find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP page", n, a[2], b[2])
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", len(L), "findings; not unique:", bad)
cnt = {}
for d in L:
    k = "mis" if d["kind"] == "misprint_in_print" else ("marker" if d["kind"] == "marker" else "norm")
    cnt.setdefault(d["page"], {}).setdefault(k, 0)
    cnt[d["page"]][k] += 1
print(cnt)
