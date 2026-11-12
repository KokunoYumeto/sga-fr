"""Build findings_316_320.json, check every fix's old (exactly once in the page file and, applied in order, at its
turn), and simulate the two marker moves on both layers in memory (nothing is written except the JSON)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
SRC = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
NL = "<NL>"


def F(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf}
    d["fix"] = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if corrected is not None:
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    return d


RNOTE = (r"Plain typewriter R (one stem); \R is \mathbb{R} in this file (double-struck). On pp. 316-317 every "
         r"derived-functor R is plain; only R\Gamma on p. 320 is double-struck, as the TeX.")
UNOTE = r"Exposé VII: the TeX has no underline markup for statements; \emph as in the applied statements of pp. 283-295."

L = []
# ---------------------------------------------------------------- p. 316
L.append(F(316, "top of the page (folio-316 marker)",
           "p. 316 begins 'faisceaux R^i t_*(t^*M), avec M un A_S-Module localement constant constructible, sont'; "
           "p. 315 ends '... épointés et par suite il résulte immédia-/tement de (1.1) et (1.2) que, notant "
           "t : B → S le morphisme canonique, les'",
           r"page_316.tex begins 'suite il résulte immédiatement de (1.1) et (1.2) que, notant $t:B\to S$ le "
           r"morphisme canonique, les' (printed at the foot of p. 315)",
           "marker", "high", None, None,
           r"Page 316 really begins at 'faisceaux $\R^it_*(t^*M)$' (the first 'faisceaux' after the marker). "
           r"Exact fix: python -I move_marker.py 5 316 faisceaux (simulated in memory on both layers: the marker "
           r"then stands on its own line between '... le morphisme canonique, les' and 'faisceaux $\R^it_*(t^*M)$'). "
           r"Text not moved. Both live layers (s5.tex as modified 12 Nov 15:46) already have the marker there; the "
           r"command leaves it in place."))
L.append(F(316, "'les faisceaux R^i t_*(t^*M)'", "plain typewriter R", r"$\R^it_*(t^*M)$", "font", "high",
           r"$\R^it_*(t^*M)$", r"$\mathrm{R}^it_*(t^*M)$",
           RNOTE + " Independent of the marker move (its anchor is 'faisceaux')."))
L.append(F(316, "'avec M un A_S-Module localement constant constructible, sont'", "Module with a capital M",
           r"$A_S$-module", "word", "high",
           r"un $A_S$-module localement constant constructible, sont",
           r"un $A_S$-Module localement constant constructible, sont",
           "The typescript's capital M (sheaf of modules), as the applied 'Module' of pp. 282-295."))
L.append(F(316, "'Soit maintenant M un A_S-Module localement constant constructible.'", "Module with a capital M",
           r"$A_S$-module", "word", "high",
           r"$A_S$-module localement constant constructible. Il",
           r"$A_S$-Module localement constant constructible. Il", ""))
L.append(F(316, "'les faisceaux R^i q_*(p^*M) sont localement constants constructibles'", "plain typewriter R",
           r"$\R^iq_*(p^*M)$", "font", "high",
           r"$\R^iq_*(p^*M)$ sont localement", r"$\mathrm{R}^iq_*(p^*M)$ sont localement", RNOTE))
L.append(F(316, "'et on en déduit en utilisant la suite spectrale de Leray'", "no comma after 'déduit'",
           "on en déduit, en utilisant", "punctuation", "high",
           "on en déduit, en utilisant", "on en déduit en utilisant", "The TeX adds a comma."))
L.append(F(316, "Leray display R^i r_*(R^j q_*)(p^*M) ⇒ R^{i+j} p_*(p^*M)", "all three R plain typewriter R",
           r"\R^ir_*(\R^jq_*)(p^*M)\Rightarrow \R^{i+j}p_*", "font", "high",
           r"\R^ir_*(\R^jq_*)(p^*M)\Rightarrow \R^{i+j}p_*",
           r"\mathrm{R}^ir_*(\mathrm{R}^jq_*)(p^*M)\Rightarrow \mathrm{R}^{i+j}p_*", RNOTE))
L.append(F(316, "end of the Leray display", "no punctuation after the display ('qu'il en est de même' follows)",
           r"(p^*M),", "punctuation", "high",
           r"(p^*M)," + NL + r"\]", r"(p^*M)" + NL + r"\]", "The TeX adds a comma at the end of the display."))
L.append(F(316, "'qu'il en est de même des faisceaux R^i p_*(p^*M). Enfin'", "plain typewriter R",
           r"$\R^ip_*(p^*M)$", "font", "high",
           r"$\R^ip_*(p^*M)$. Enfin", r"$\mathrm{R}^ip_*(p^*M)$. Enfin", RNOTE))
L.append(F(316, "'R^i q_*(p^*M) sont stables par changement de base'", "plain typewriter R",
           r"$\R^iq_*(p^*M)$", "font", "high",
           r"$\R^iq_*(p^*M)$ sont stables", r"$\mathrm{R}^iq_*(p^*M)$ sont stables", RNOTE))
L.append(F(316, "'les faisceaux R^i p_*(p^*M) sont également stables'", "plain typewriter R",
           r"$\R^ip_*(p^*M)$", "font", "high",
           r"$\R^ip_*(p^*M)$ sont également", r"$\mathrm{R}^ip_*(p^*M)$ sont également", RNOTE))
L.append(F(316, "Remarque 6.3, 'est localement pour la topologie étale image réciproque'", "no commas",
           "est localement, pour la topologie étale, image", "punctuation", "high",
           "est localement, pour la topologie étale, image", "est localement pour la topologie étale image",
           "The TeX adds two commas."))
L.append(F(316, "Remarque 6.3, 'le calcul de la cohomologie (à coefficients ... caractéristique) des schémas'",
           "the phrase in parentheses, no commas",
           "la cohomologie, à coefficients de torsion premier à la caractéristique, des", "punctuation", "high",
           "la cohomologie, à coefficients de torsion premier à la caractéristique, des",
           "la cohomologie (à coefficients de torsion premier à la caractéristique) des",
           "The TeX turns the parenthesis into commas."))
L.append(F(316, "end of Remarque 6.3, '(SGA 4 XI 4.4)'", "no full stop after the parenthesis (clean paper)",
           "(SGA 4 XI 4.4).", "misprint_in_print", "high",
           "(SGA 4 XI 4.4).", "(SGA 4 XI 4.4)",
           "The typist left out the stop that ends the remark; the TeX silently adds it (as the applied "
           "'spectrales [6]' of p. 285).", corrected="(SGA 4 XI 4.4)."))
L.append(F(316, "Corollaire 6.4, first sentence",
           "underlined: 'Soient' | 'un schéma et' | 'un' | 'schéma en groupes extension' / 'd'un' | 'schéma en "
           "groupes étale fini' | 'et d'un' | 'schéma en groupes réductif' (S, p : G→S, S-, F, H not)",
           "no underline markup", "underline", "high",
           r"Soient $S$ un schéma et $p:G\to S$ un $S$-schéma en groupes extension d'un $S$-schéma en groupes "
           r"étale fini $F$ et d'un $S$-schéma en groupes réductif $H$.",
           r"\emph{Soient} $S$ \emph{un schéma et} $p:G\to S$ \emph{un} $S$-\emph{schéma en groupes extension "
           r"d'un} $S$-\emph{schéma en groupes étale fini} $F$ \emph{et d'un} $S$-\emph{schéma en groupes "
           r"réductif} $H$.", UNOTE))
L.append(F(316, "Corollaire 6.4, 'Alors, les conclusions de (6.2)'",
           "a comma after 'Alors'; 'Alors, les conclusions de' underlined, (6.2) not",
           "Alors les conclusions de (6.2)", "punctuation", "high",
           "Alors les conclusions de (6.2)", r"\emph{Alors, les conclusions de} (6.2)",
           "The TeX drops the comma; the edit also gives the underline."))
L.append(F(316, "Corollaire 6.4, 'sont valables pour tout A_S-Module localement constant constructible M .'",
           "Module with a capital M; 'sont valables pour tout' and 'Module localement constant' / 'constructible' "
           "underlined (A_S-, M not)",
           r"$A_S$-module, no underline markup", "word", "high",
           r"sont valables pour tout $A_S$-module localement constant constructible $M$.",
           r"\emph{sont valables pour tout} $A_S$-\emph{Module localement constant constructible} $M$.",
           "The edit also gives the underline."))
# ---------------------------------------------------------------- p. 317
L.append(F(317, "Corollaire 6.5, first two lines",
           "underlined: 'Soient' | 'un schéma' | 'un' | 'schéma en groupes réductif et' | 'un' / 'sous-' | 'schéma "
           "en groupes réductif de' | 'tels que le faisceau quotient de' | 'par' (S, G, S-, H not)",
           "no underline markup", "underline", "high",
           r"Soient $S$ un schéma, $G$ un $S$-schéma en groupes réductif et $H$ un sous-$S$-schéma en groupes "
           r"réductif de $G$, tels que le faisceau quotient de $G$ par $H$",
           r"\emph{Soient} $S$ \emph{un schéma}, $G$ \emph{un} $S$-\emph{schéma en groupes réductif et} $H$ "
           r"\emph{un sous}-$S$-\emph{schéma en groupes réductif de} $G$, \emph{tels que le faisceau quotient de} "
           r"$G$ \emph{par} $H$", UNOTE))
L.append(F(317, "Corollaire 6.5, 'pour la topologie fidèlement plate quasicompacte soit représentable. Alors, notant'",
           "'quasicompacte' in one word (no hyphen); the whole line underlined",
           "quasi-compacte, no underline markup", "word", "high",
           "pour la topologie fidèlement plate quasi-compacte soit représentable. Alors, notant",
           r"\emph{pour la topologie fidèlement plate quasicompacte soit représentable. Alors, notant}",
           "The TeX adds a hyphen; the edit also gives the underline. (The print runs p : G/H → S into the line; "
           "the display is not reported.)"))
L.append(F(317, "Corollaire 6.5, 'le morphisme canonique, ... tout A_S-Module localement constant constructible M .'",
           "Module with a capital M; underlined: 'le morphisme canonique, les conclusions de' | 'sont valables pour "
           "tout' | 'Module localement constant constructible' ((6.2), A_S-, M not)",
           r"$A_S$-module, no underline markup", "word", "high",
           r"le morphisme canonique, les conclusions de (6.2) sont valables pour tout $A_S$-module localement "
           r"constant constructible $M$.",
           r"\emph{le morphisme canonique, les conclusions de} (6.2) \emph{sont valables pour tout} "
           r"$A_S$-\emph{Module localement constant constructible} $M$.",
           "The edit also gives the underline."))
L.append(F(317, "proof, 'Posons pour tout entier r ≥ 0' (before the display of G_r)", "no commas",
           r"Posons, pour tout entier $r\ge0$,", "punctuation", "high",
           r"Posons, pour tout entier $r\ge0$,", r"Posons pour tout entier $r\ge0$",
           "The TeX adds two commas."))
L.append(F(317, "display G_r = G ×_{G/H} G ×_{G/H} ×...×_{G/H} G (r+1 fois)",
           "'G x_{G/H} G x_{G/H} x...x_{G/H} G': a product sign without index right after the second x_{G/H}, "
           "before the dots",
           r"G\times_{G/H}G\times_{G/H}\cdots\times_{G/H}G", "misprint_in_print", "medium",
           r"G\times_{G/H}G\times_{G/H}\cdots", r"G\times_{G/H}G\times_{G/H}\times\cdots",
           "One product sign too many (the next display prints G x_S H x_S ... x_S H without it); the TeX "
           "silently drops it.", corrected=r"G\times_{G/H}G\times_{G/H}\cdots"))
L.append(F(317, "display G ×_S H ×_S ... ×_S H and the following words",
           "an underbrace from the first H to the last H with 'r fois' below it; the text then goes on "
           "'et notons' (no words before it)",
           r"no underbrace; the text adds 'où $H$ apparaît $r$ fois,'", "extra", "high",
           r"G\times_S H\times_S\cdots\times_S H," + NL + r"\]" + NL + r"où $H$ apparaît $r$ fois, et notons",
           r"G\times_S\underbrace{H\times_S\cdots\times_S H}_{r\text{ fois}}," + NL + r"\]" + NL + "et notons",
           "The TeX replaces the printed underbrace by words the print does not have."))
L.append(F(317, "'qui d'après SGA 3 V 1.5, s'identifie canoniquement à'", "no comma after 'qui'",
           "qui, d'après", "punctuation", "high", "qui, d'après", "qui d'après",
           "The TeX adds a comma (the print has only the one after '1.5')."))
L.append(F(317, "'Notons enfin, pour tout entier q ≥ 0 , H^q(M) le complexe'",
           "script H (a typed H with hand-drawn hooks), as in H^p(ℋ^q(M)) below and ℋ^q(F) on p. 319",
           r"$H^q(M)$", "font", "high",
           r"$H^q(M)$ le complexe", r"$\mathcal H^q(M)$ le complexe",
           r"The TeX writes \mathcal H for the same glyph on p. 319."))
L.append(F(317, "display of the complex H^q(M)",
           "R^q(g_o)_*(f_o^*M) ⇉ R^q(g_1)_*(f_1^*M) ⇶ ... [arrow, vertical dots, arrow] R^q(g_r)_*(f_r^*M)...: "
           "two parallel arrows after the first term, three after the second, a column 'arrow / vertical dots / "
           "arrow' after the dots; all three R plain typewriter R",
           r"\to, \rightrightarrows, \to; \R", "symbol", "high",
           r"\R^q(g_0)_*(f_0^*M)\to \R^q(g_1)_*(f_1^*M)\rightrightarrows\cdots\to \R^q(g_r)",
           r"\mathrm{R}^q(g_0)_*(f_0^*M)\rightrightarrows \mathrm{R}^q(g_1)_*(f_1^*M)"
           r"\mathrel{\substack{\to\\\to\\\to}}\cdots\mathrel{\substack{\to\\\vdots\\\to}} \mathrm{R}^q(g_r)",
           "The TeX has one arrow too few at each place (the print draws the r+1 arrows of the cosimplicial "
           "complex). The same edit sets the three R plain (font, as elsewhere in the exposé)."))
L.append(F(317, "end of the display of the complex", "the display ends with the dots, no full stop",
           r"\cdots .", "punctuation", "high",
           r"(f_r^*M)\cdots .", r"(f_r^*M)\cdots", "The TeX adds a full stop at the end of the display."))
L.append(F(317, "'on a une suite spectrale de descente (ou de Čech)'", "'(ou de Čech)' in parentheses, no commas",
           "de descente, ou de Čech,", "punctuation", "high",
           "de descente, ou de Čech,", "de descente (ou de Čech)",
           "The TeX turns the parenthesis into commas. The same line prints '(SGA          )' with a blank left "
           "for a reference that was never filled in (spacing only, not reported, as on p. 26)."))
L.append(F(317, "display E(M) : E_2^{pq} = H^p(ℋ^q(M)) ⇒ E^n = R^n p_*(M).",
           "hand-drawn double-struck E in E(M); script H (typed H with hooks) in ℋ^q(M); plain typewriter R in "
           "R^n p_*",
           r"E(M), H^q(M), \R^n", "font", "high",
           r"E(M):E_2^{pq}=H^p(H^q(M))\Rightarrow E^n=\R^np_*(M).",
           r"\mathbb E(M):E_2^{pq}=H^p(\mathcal H^q(M))\Rightarrow E^n=\mathrm{R}^np_*(M).",
           "Three letters in one display: double-struck E, script H, plain R."))
L.append(F(317, "'les termes E_2^{pq} sont localement courants constructibles'", "'courants'",
           "constants", "misprint_in_print", "high",
           "localement constants constructibles et", "localement courants constructibles et",
           "Typing error for 'constants'; the TeX silently corrects it.",
           corrected="localement constants constructibles et"))
# ---------------------------------------------------------------- p. 318
L.append(F(318, "section title 7", "'7. INTERSECTIONS COMPLETES': hand-lettered capitals, underlined, no full stop",
           r"\section*{7. Intersections complètes}", "word", "high",
           r"\section*{7. Intersections complètes}", r"\section*{7. INTERSECTIONS COMPLÈTES}",
           "Capitals as printed, as the applied '2. SCHÉMAS PROJECTIFS' (p. 285); accented capital as the "
           "volume's rule."))
L.append(F(318, "'on note pour tout k-schéma propre X et tout entier i ≥ 0 par'", "no commas",
           r"on note, pour tout $k$-schéma propre $X$ et tout entier $i\ge0$, par", "punctuation", "high",
           r"on note, pour tout $k$-schéma propre $X$ et tout entier $i\ge0$, par",
           r"on note pour tout $k$-schéma propre $X$ et tout entier $i\ge0$ par", "The TeX adds two commas."))
L.append(F(318, "'b_ℓ^i(X) [ou b^i(X) si aucune confusion n'est possible] le i^{ème} nombre'",
           "in the line, in square brackets, no comma after 'possible'",
           r"a display 'b_\ell^i(X)\quad\text{ou}\quad b^i(X)', then 'si aucune confusion n'est possible, le'",
           "punctuation", "high",
           r"\[" + NL + r"b_\ell^i(X)\quad\text{ou}\quad b^i(X)" + NL + r"\]" + NL +
           "si aucune confusion n'est possible,",
           r"$b_\ell^i(X)$ [ou $b^i(X)$ si aucune confusion n'est possible]",
           "The TeX drops the brackets and adds a comma; the formula goes back into the line to carry the "
           "brackets."))
L.append(F(318, "'le i^{ème} nombre de Betti'", "i with a raised 'ème' (no hyphen)", r"$i$-ème", "word", "high",
           r"$i$-ème", r"$i^{\text{ème}}$", "As the applied i^{ème} of p. 290."))
L.append(F(318, "'on appelle section hyperplane de X'", "'section hyperplane' underlined (defined term)",
           "no underline markup", "underline", "high",
           "appelle section hyperplane", r"appelle \emph{section hyperplane}", ""))
L.append(F(318, "'avec ℒ un O_X-Module inversible ample.'", "Module with a capital M (the O is a hand-drawn script O)",
           r"$\mathcal O_X$-module", "word", "high",
           r"$\mathcal O_X$-module inversible ample", r"$\mathcal O_X$-Module inversible ample",
           "O_X: hand-drawn script O, see the message."))
L.append(F(318, "Théorème 7.1, '(Théorème de Lefschetz)Soient'", "no full stop in the parenthesis",
           "(Théorème de Lefschetz.)", "punctuation", "high",
           "(Théorème de Lefschetz.)", "(Théorème de Lefschetz)", "The TeX adds a full stop."))
L.append(F(318, "Théorème 7.1, 'Soient X un k-schéma projectif lisse, connexe / de dimension n ,'",
           "no comma after 'connexe' (it ends the line); underlined: 'Soient' | 'un' | 'schéma projectif lisse, "
           "connexe' / 'de dimension' (X, k-, n not)",
           "connexe, de dimension; no underline markup", "punctuation", "high",
           r"Soient $X$ un $k$-schéma projectif lisse, connexe, de dimension $n$,",
           r"\emph{Soient} $X$ \emph{un} $k$-\emph{schéma projectif lisse, connexe de dimension} $n$,",
           "The TeX adds a comma after 'connexe' (Corollaire 7.2 on p. 320 prints it, this statement does not); "
           "the edit also gives the underline."))
L.append(F(318, "Théorème 7.1, 'Y un sous-schéma de X intersection de d sections hyperplanes / de X , et L un'",
           "underlined: 'un sous-schéma de' | 'intersection de' | 'sections hyperplanes' / 'de' | 'et' | 'un' "
           "(Y, X, d, L not)",
           "no underline markup", "underline", "high",
           r"$Y$ un sous-schéma de $X$ intersection de $d$ sections hyperplanes de $X$, et $L$ un",
           r"$Y$ \emph{un sous-schéma de} $X$ \emph{intersection de} $d$ \emph{sections hyperplanes de} $X$, "
           r"\emph{et} $L$ \emph{un}", UNOTE))
L.append(F(318, "Théorème 7.1, 'A_X-Module localement constant constructible. Alors :'",
           "Module with a capital M; 'Module localement constant constructible. Alors' underlined (A_X- and the "
           "colon not)",
           r"$A_X$-module, no underline markup", "word", "high",
           r"$A_X$-module localement constant constructible. Alors:",
           r"$A_X$-\emph{Module localement constant constructible. Alors}:",
           "The edit also gives the underline."))
L.append(F(318, "Théorème 7.1 (i), 'L'homomorphisme image réciproque'", "underlined", "no underline markup",
           "underline", "high",
           r"\item L'homomorphisme image réciproque", r"\item \emph{L'homomorphisme image réciproque}", ""))
L.append(F(318, "Théorème 7.1 (i), after the display",
           "underlined: 'est un isomorphisme pour' | 'et un monomorphisme pour' (formulas and comma not)",
           "no underline markup", "underline", "high",
           r"est un isomorphisme pour $i\le n-d-1$, et un monomorphisme pour $i=n-d$.",
           r"\emph{est un isomorphisme pour} $i\le n-d-1$, \emph{et un monomorphisme pour} $i=n-d$.", ""))
L.append(F(318, "Théorème 7.1 (ii), 'Supposons Y lisse sur k , de dimension n-d . Alors l'homomorphisme de / Gysin'",
           "underlined: 'Supposons' | 'lisse sur' | 'de dimension' | 'Alors l'homomorphisme de' / 'Gysin'",
           "no underline markup", "underline", "high",
           r"\item Supposons $Y$ lisse sur $k$, de dimension $n-d$. Alors l'homomorphisme de Gysin",
           r"\item \emph{Supposons} $Y$ \emph{lisse sur} $k$, \emph{de dimension} $n-d$. \emph{Alors "
           r"l'homomorphisme de Gysin}", ""))
L.append(F(318, "Théorème 7.1 (ii), after the display",
           "underlined: 'est un isomorphisme pour' | 'et un épimorphisme pour'", "no underline markup",
           "underline", "high",
           r"est un isomorphisme pour $i\ge n-d+1$ et un épimorphisme pour $i=n-d$.",
           r"\emph{est un isomorphisme pour} $i\ge n-d+1$ \emph{et un épimorphisme pour} $i=n-d$.", ""))
L.append(F(318, "proof, 'et par suite U = X ∸ Y est réunion'", "a typed dot centred over the minus sign (∸)",
           r"$U=X-Y$", "symbol", "high",
           r"$U=X-Y$", r"$U=X\mathbin{\dot{-}}Y$",
           r"As the applied C^r \mathbin{\dot{-}} 0 of p. 285; the dot is crisp and centred over the dash."))
L.append(F(318, "proof, exact sequence, '... → H_1^i(U,L|U) → H^i(X,L)'",
           "the subscript of H is the digit 1 (with its flag, as the 1 of the exponent i+1 in the same display), "
           "not '!'",
           r"H_!^i(U,L|U)", "misprint_in_print", "high",
           r"H_!^i(U,L|U)", r"H_1^i(U,L|U)",
           "Cohomology with proper supports H_! is meant (p. 284 prints a clear '!' under R); the TeX silently "
           "corrects.", corrected=r"H_!^i(U,L|U)"))
L.append(F(318, "proof, exact sequence, '--∂--> H_1^{i+1}(U,L|U) → ...'",
           "the subscript of H is the digit 1, not '!'", r"H_!^{i+1}(U,L|U)", "misprint_in_print", "high",
           r"H_!^{i+1}(U,L|U)", r"H_1^{i+1}(U,L|U)",
           "As the previous item; the TeX silently corrects.", corrected=r"H_!^{i+1}(U,L|U)"))
L.append(F(318, "Lemme 7.1.1, 'Soit U un k-schéma de type fini de dimension n , réunion de d ouverts / affines, et F un'",
           "underlined: 'Soit' | 'un' | 'schéma de type fini de dimension' | 'réunion de' | 'ouverts' / 'affines' "
           "| 'et' | 'un' (U, k-, n, d, F not)",
           "no underline markup", "underline", "high",
           r"Soit $U$ un $k$-schéma de type fini de dimension $n$, réunion de $d$ ouverts affines, et $F$ un",
           r"\emph{Soit} $U$ \emph{un} $k$-\emph{schéma de type fini de dimension} $n$, \emph{réunion de} $d$ "
           r"\emph{ouverts affines}, \emph{et} $F$ \emph{un}", UNOTE))
L.append(F(318, "Lemme 7.1.1, 'A_U-Module.'", "Module with a capital M, underlined", r"$A_U$-module.", "word",
           "high", r"$A_U$-module.", r"$A_U$-\emph{Module}.", "The edit also gives the underline."))
L.append(F(318, "Lemme 7.1.1, end of the first sentence",
           "no 'Alors :': p. 318 ends '... et F un A_U-Module.' and p. 319 begins 'a) Si F est constructible,'",
           "Alors:", "extra", "high",
           " Alors:" + NL + r"\begin{enumerate}[label=\alph*)]", NL + r"\begin{enumerate}[label=\alph*)]",
           "The TeX adds 'Alors:'."))
# ---------------------------------------------------------------- p. 319
L.append(F(319, "Lemme 7.1.1 a), 'Si F est constructible,'",
           "'Si' with a capital S; 'Si' and 'est constructible' underlined", "si, no underline markup", "word",
           "high",
           r"\item si $F$ est" + NL + "constructible,", r"\item \emph{Si} $F$ \emph{est constructible},",
           "The edit also gives the underline."))
L.append(F(319, "Lemme 7.1.1 a), display H^i(U,F) = 0 pour i ≥ n+d .",
           "a full stop at the end of the display; 'pour' underlined", r"\text{pour }i\ge n+d;", "punctuation",
           "high", r"\text{pour }i\ge n+d;", r"\text{\emph{pour} }i\ge n+d.",
           "The TeX has a semicolon for the print's full stop; the edit also underlines 'pour'."))
L.append(F(319, "Lemme 7.1.1 b), 'Si F est localement constant et U lisse sur k ,'",
           "'Si' with a capital S; underlined: 'Si' | 'est localement constant et' | 'lisse sur'",
           "si, no underline markup", "word", "high",
           r"\item si $F$ est localement constant et $U$ lisse sur $k$,",
           r"\item \emph{Si} $F$ \emph{est localement constant et} $U$ \emph{lisse sur} $k$,",
           "The edit also gives the underline."))
L.append(F(319, "Lemme 7.1.1 b), display H_c^i(U,F) = 0 pour i ≤ n-d .", "'pour' underlined",
           "no underline markup", "underline", "high",
           r"\text{pour }i\le n-d.", r"\text{\emph{pour} }i\le n-d.", ""))
L.append(F(319, "'notant 𝒰 un recouvrement de U par d ouverts affines'",
           "hand-drawn script (calligraphic) U, curl at the top left; not a Fraktur letter",
           r"$\mathfrak U$", "font", "high",
           r"notant $\mathfrak U$", r"notant $\mathcal U$", ""))
L.append(F(319, "Čech spectral sequence H^p(𝒰,ℋ^q(F)) ⇒ H^{p+q}(U,F)", "hand-drawn script U, as in the line above",
           r"\mathfrak U", "font", "high",
           r"H^p(\mathfrak U,", r"H^p(\mathcal U,", ""))
L.append(F(319, "display (7.1.2)", "the isomorphism sign is a tilde over an arrow (⥲)", r"\simeq", "symbol", "high",
           r"\simeq H^i_Y(X,L),", r"\xrightarrow{\sim} H^i_Y(X,L),",
           r"Written \xrightarrow{\sim}, as the file's other printed isomorphism arrows."))
# ---------------------------------------------------------------- p. 320
L.append(F(320, "Corollaire 7.2, first two lines",
           "underlined: 'Soient' | 'un' | 'schéma projectif lisse, connexe, de dimension' | 'un sous-schéma de' | "
           "'intersection de' | 'sections hyperplanes de' | 'et' | 'un' (X, k-, n, Y, d, L not)",
           "no underline markup", "underline", "high",
           r"Soient $X$ un $k$-schéma projectif lisse, connexe, de dimension $n$, $Y$ un sous-schéma de $X$ "
           r"intersection de $d$ sections hyperplanes de $X$, et $L$ un",
           r"\emph{Soient} $X$ \emph{un} $k$-\emph{schéma projectif lisse, connexe, de dimension} $n$, $Y$ "
           r"\emph{un sous-schéma de} $X$ \emph{intersection de} $d$ \emph{sections hyperplanes de} $X$, "
           r"\emph{et} $L$ \emph{un}", UNOTE))
L.append(F(320, "Corollaire 7.2, 'Z_ℓ-faisceau constant tordu constructible (ℓ ≠ car(k)). Alors :'",
           "'faisceau constant tordu constructible' and 'Alors' underlined", "no underline markup", "underline",
           "high",
           r"-faisceau constant tordu constructible $(\ell\ne\operatorname{car}(k))$. Alors:",
           r"-\emph{faisceau constant tordu constructible} $(\ell\ne\operatorname{car}(k))$. \emph{Alors}:", ""))
L.append(F(320, "Corollaire 7.2 (i), 'L'homomorphisme image réciproque'",
           "'L'homomorphisme' with a capital L; 'L'homomorphisme image réciproque' underlined",
           "l'homomorphisme, no underline markup", "word", "high",
           r"\item l'homomorphisme image réciproque", r"\item \emph{L'homomorphisme image réciproque}",
           "The edit also gives the underline."))
L.append(F(320, "Corollaire 7.2 (i), after the display",
           "underlined: 'est un isomorphisme pour' | 'et un monomorphisme pour' | 'Si de plus' | 'est localement "
           "libre constructible, le conoyau de' | 'est sans torsion' (formulas, L and the stops not)",
           "no underline markup", "underline", "high",
           r"est un isomorphisme pour $i\le n-d-1$, et un monomorphisme pour $i=n-d$. Si de plus $L$ est "
           r"localement libre constructible, le conoyau de $\alpha_{n-d}$ est sans torsion.",
           r"\emph{est un isomorphisme pour} $i\le n-d-1$, \emph{et un monomorphisme pour} $i=n-d$. \emph{Si de "
           r"plus} $L$ \emph{est localement libre constructible, le conoyau de} $\alpha_{n-d}$ \emph{est sans "
           r"torsion}.", ""))
L.append(F(320, "Corollaire 7.2 (ii), 'Supposons Y lisse sur k , de dimension n-d . Alors l'homomorphisme de / Gysin'",
           "'Supposons' with a capital S; underlined: 'Supposons' | 'lisse sur' | 'de dimension' | 'Alors "
           "l'homomorphisme de' / 'Gysin'",
           "supposons, no underline markup", "word", "high",
           r"\item supposons $Y$ lisse sur $k$, de dimension $n-d$. Alors l'homomorphisme de Gysin",
           r"\item \emph{Supposons} $Y$ \emph{lisse sur} $k$, \emph{de dimension} $n-d$. \emph{Alors "
           r"l'homomorphisme de Gysin}", "The edit also gives the underline."))
L.append(F(320, "Corollaire 7.2 (ii), after the display",
           "underlined: 'est un isomorphisme pour' | 'et un épimorphisme pour' | 'Si de plus' | 'est localement "
           "libre constructible, l'épimorphisme' | 'est direct et son noyau' / 'est sans torsion'",
           "no underline markup", "underline", "high",
           r"est un isomorphisme pour $i\ge n-d+1$ et un épimorphisme pour $i=n-d$. Si de plus $L$ est localement "
           r"libre constructible, l'épimorphisme $\beta_{n-d}$ est direct et son noyau est sans torsion.",
           r"\emph{est un isomorphisme pour} $i\ge n-d+1$ \emph{et un épimorphisme pour} $i=n-d$. \emph{Si de "
           r"plus} $L$ \emph{est localement libre constructible, l'épimorphisme} $\beta_{n-d}$ \emph{est direct "
           r"et son noyau est sans torsion}.", ""))
L.append(F(320, "Lemme 7.2.1, first sentence",
           "underlined: 'Soient' | 'un anneau de valuation discrète' | 'son corps résiduel' | 'un morphisme de' "
           "(V, k_V, u : K → L, D(V) not)",
           "no underline markup", "underline", "high",
           r"Soient $V$ un anneau de valuation discrète, $k_V$ son corps résiduel, $u:K\to L$ un morphisme de",
           r"\emph{Soient} $V$ \emph{un anneau de valuation discrète}, $k_V$ \emph{son corps résiduel}, "
           r"$u:K\to L$ \emph{un morphisme de}", UNOTE))
L.append(F(320, "Lemme 7.2.1, 'On suppose que K et L sont à cohomologie de type fini, et on note M / le mapping-cylinder de u .'",
           "a new, indented paragraph begins at 'On suppose que'; underlined: 'On suppose que' | 'et' | 'sont à "
           "cohomologie de type fini, et on note' | 'le mapping-cylinder de' (K, L, M, u not)",
           r"runs on after '$D(V)$.'; no underline markup", "other", "medium",
           r"$D(V)$. On suppose que $K$ et $L$ sont à cohomologie de type fini, et on note $M$ le "
           r"mapping-cylinder de $u$.",
           r"$D(V)$." + NL + NL + r"\emph{On suppose que} $K$ \emph{et} $L$ \emph{sont à cohomologie de type fini, "
           r"et on note} $M$ \emph{le mapping-cylinder de} $u$.",
           "The TeX runs the statement's two paragraphs together; the edit also gives the underline. Keep the "
           "underline and drop the break if paragraphing is left to a global pass."))
L.append(F(320, "Lemme 7.2.1, 'Alors pour tout m ∈ Z les conditions suivantes sont équi- / valentes :'",
           "underlined: 'Alors pour tout' | 'les conditions suivantes sont équivalentes' (m ∈ Z and the colon not)",
           "no underline markup", "underline", "high",
           r"Alors pour tout $m\in\mathbb Z$ les conditions suivantes sont équivalentes:",
           r"\emph{Alors pour tout} $m\in\mathbb Z$ \emph{les conditions suivantes sont équivalentes}:", ""))
L.append(F(320, "Lemme 7.2.1 (i)", "underlined: 'pour' | 'et' | 'est sans torsion'", "no underline markup",
           "underline", "high",
           r"\item $H^p(M)=0$ pour $p\le m-1$, et $H^m(M)$ est sans torsion.",
           r"\item $H^p(M)=0$ \emph{pour} $p\le m-1$, \emph{et} $H^m(M)$ \emph{est sans torsion}.", ""))
L.append(F(320, "end of the page (folio-321 marker)",
           "p. 320 ends '(i) H^p(M) = 0 pour p ≤ m-1 , et H^m(M) est sans torsion.'; p. 321 begins "
           "'(ii) Pour tout V-module N , le morphisme'",
           r"the last line of page_320.tex is '\item', which sets the label (ii) printed on p. 321",
           "marker", "high", None, None,
           r"Page 321 really begins at that '\item'. Exact fix: python -I move_marker.py 5 321 '\item' --before "
           r"(simulated in memory on both layers: the folio-321 marker then stands on its own line between "
           r"'... est sans torsion.' and '\item'). Text not moved. The live layers (12 Nov 15:46) still have '\item' "
           r"before the folio-321 marker."))

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for p in (316, 317, 318, 319, 320):
    pages[p] = (RUN / "b316_320" / f"page_{p}.tex").read_text(encoding="utf-8")
cur = dict(pages)
for i, d in enumerate(L):
    if d["fix"] is None:
        continue
    p, old, new = d["page"], d["fix"]["old"], d["fix"]["new"]
    n0 = pages[p].count(old)
    n1 = cur[p].count(old)
    if n0 != 1 or n1 != 1:
        ok = False
        print("NOT UNIQUE", i, p, n0, n1, repr(old[:60]))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
        ok = False
        print("MARKER IN FIX", i)
    if old.endswith(" ") or new.endswith(" "):
        print("trailing space", i, repr(old[-10:]), repr(new[-10:]))
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", old + new):
        ok = False
        print("CONTROL CHAR", i)
    cur[p] = cur[p].replace(old, new, 1)
# braces balanced after all fixes
for p in cur:
    t = re.sub(r"\\[{}]", "", cur[p])
    if t.count("{") != t.count("}"):
        ok = False
        print("UNBALANCED", p, t.count("{"), t.count("}"))
print("all olds unique (original and in order):", ok)

# misprint fixes change only the misprinted characters: report the diff span
for d in L:
    if d["kind"] == "misprint_in_print" and d["fix"]:
        o, n = d["fix"]["old"], d["fix"]["new"]
        a = 0
        while a < min(len(o), len(n)) and o[a] == n[a]:
            a += 1
        b = 0
        while b < min(len(o), len(n)) - a and o[-1 - b] == n[-1 - b]:
            b += 1
        print("misprint", d["page"], repr(o[a:len(o) - b]), "->", repr(n[a:len(n) - b]))

# marker moves simulated in memory, both layers
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for edition in ("diplomatic", "current"):
    t0 = (SRC / edition / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor, before in ((316, "faisceaux", False), (321, "\\item", True)):
        t = t0
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        j = t2.find(line)
        print("----", edition, folio)
        print(t2[j - 160:j + len(line) + 120])

out = RUN / "findings_316_320.json"
out.write_text(json.dumps(L, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print("wrote", out, len(L))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in L)
for p in (316, 317, 318, 319, 320):
    print(p, c[(p, False)], "/", c[(p, True)])
