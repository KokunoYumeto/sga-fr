import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_471_475.json")


def L(s):
    return None if s is None else s.replace("¶", "\n")


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


f = []
# ---------------- page 471 ----------------
f.append(F(471, "top of the page: the display f^{-n}_{F_x̄} = fr^n_{F_x̄} = (Fr^*_{F_x̄/x̄})^n",
  r"p. 471 begins with the display 'f^{-n}_{F_x̄} = fr^n_{F_x̄} = (Fr^*_{F_x̄/x̄})^n', then '(x̄ = point géométrique défini par un plongement de F_q dans F̄_p) .'; p. 470 ends with '... Nous obtenons :' and the footnote (*) (b466_470/page_470_s4.png)",
  r"the display '\[', 'f^{-n}_{F_{\bar x}}=\fr^n_{F_{\bar x}}=(\Fr^*_{F_{\bar x}/\bar x})^n', '\]' is the last three lines of page_470.tex; the folio-471 marker follows it, and page_471.tex begins '($\bar x=$ point'",
  "marker", "high",
  note=r"Page 471 really begins at the '\[' of that display (the line after 'Nous obtenons:'). Exact fix: python -I move_marker.py 5 471 '\[' --before (simulated in memory on both live layers at 17:08: the marker moves back 75 characters to its own line between 'Nous obtenons:' and '\['). Run it once only: a second run would move the marker 245 characters further back, to the display f^{-n}_{H^i(\bar X,\bar F)}=\fr^n_{H^i(\bar X,\bar F)} of p. 470. Batch 466-470 may report the same move: apply once. Text not moved; the display agrees with the print of p. 471 (no bars over fr and Fr, no final punctuation)."))
f.append(F(471, "'au lieu de X̄ , F̄ , fr^n_X et (Fr̄^*_{F/X})^n'",
  r"fr^n_X without a bar: the double-underlined fr has clean paper above it, while X̄, F̄ and the following F̄r̄^*_{F/X} carry their bars, as do the other fr̄_X of the page (crop c471_frn.png)",
  r"$\bar{\fr}_X^n$ et",
  "misprint_in_print", "high", r"$\bar{\fr}_X^n$ et", r"$\fr_X^n$ et",
  corrected=r"$\bar{\fr}_X^n$",
  note=r"h is the n-th power of the geometric Frobenius \bar{fr}_X of X̄ (the correspondence (\bar{fr}_X, \overline{Fr}^*_{F/X}) just above); fr_X^n acts on X, not on X̄. The TeX silently corrects; the fix restores the printed reading."))
f.append(F(471, "'en effet h opère par : T ⇝ T^{p^n}'",
  r"opère par : T ⇝ T^{p^n} (colon after 'par')",
  r"opère par $T\mapsto T^{p^n}$",
  "punctuation", "high", r"opère par $T", r"opère par: $T",
  note=r"The file writes the colon without a space before it (babel adds it), as in 'résultat suivant:'."))
f.append(F(471, "'T ⇝ T^{p^n}'",
  r"a hand-drawn squiggly arrow (⇝) between T and T^{p^n}, not a maps-to arrow (crop c471_T.png)",
  r"T\mapsto T^{p^n}",
  "symbol", "high", r"\mapsto T^{p^n}", r"\rightsquigarrow T^{p^n}",
  note=r"The file sets this typescript arrow as \rightsquigarrow in Exposé X (E\rightsquigarrow B_{[u]}\otimes_A E); the same arrow on p. 474 (T : L ⇝ L ⊗_A A_0) is \longmapsto there."))
f.append(F(471, "Proposition 2, first two lines",
  r"Soient | une courbe projective et lisse sur un corps algébriquement clos | de caractéristique | un faisceau : underlined (not X, k, p, F or the comma); the label 'Proposition 2.' is underlined too (accepted setting)",
  r"Soient $X$ une courbe projective et lisse sur un corps algébriquement clos $k$ de caractéristique $p$, $F$ un faisceau (no underline markup)",
  "underline", "high",
  r"Soient $X$ une courbe projective et lisse sur un corps algébriquement clos $k$ de caractéristique $p$, $F$ un faisceau",
  r"\emph{Soient} $X$ \emph{une courbe projective et lisse sur un corps algébriquement clos} $k$ \emph{de caractéristique} $p$, $F$ \emph{un faisceau}",
  note=r"Exposé XV has no underline markup at all; \emph is the file's command for the print's underline (as itemized in Exposés III B and V). The old stops before '$\ell$-', which goes to p. 472 with the folio-472 marker fix. The statement continues on p. 472 (filed there)."))
# ---------------- page 472 ----------------
f.append(F(472, r"top of the page: '$\ell$-' of 'ℓ-adique'",
  r"p. 472 begins with 'ℓ -adique constructible sur X_ét (avec ℓ = nombre premier ≠ p),'; p. 471 ends with '... de caractéristique p , F un faisceau'",
  r"'$\ell$-' ends the last line of page_471.tex; the folio-472 marker follows it and page_472.tex begins 'adique constructible'. The line end before the marker line also prints a space inside 'ℓ- adique'.",
  "marker", "high",
  note=r"Page 472 really begins at '$\ell$-'. Exact fix: python -I marker_split_word.py 5 472 pull '$\ell$-' (simulated in memory on both live layers at 17:08: p. 471 then ends '... $F$ un faisceau' and p. 472 begins '$\ell$-adique constructible sur $X_{\et}$', which also removes the space). Text not moved."))
f.append(F(472, "Proposition 2 (cont.), lines 1-3: '-adique constructible sur ... et'",
  r"-adique constructible sur | avec | nombre premier | un endomorphisme de | dont tous les points fixes sont de mul-tiplicité | et : underlined (not X_ét, ℓ, h, X, 1 or the punctuation)",
  r"adique constructible sur $X_{\et}$ (avec $\ell=$ nombre premier $\ne p$), $h$ un endomorphisme de $X$ dont tous les points fixes sont de multiplicité $1$, et (no underline markup)",
  "underline", "high",
  r"adique constructible sur $X_{\et}$ (avec $\ell=$ nombre premier $\ne p$), $h$ un endomorphisme de $X$ dont tous les points fixes sont de multiplicité $1$, et",
  r"\emph{adique constructible sur} $X_{\et}$ (\emph{avec} $\ell=$ \emph{nombre premier} $\ne p$), $h$ \emph{un endomorphisme de} $X$ \emph{dont tous les points fixes sont de multiplicité} $1$, \emph{et}",
  note=r"The print's underline starts under the hyphen of '-adique'; the hyphen is left outside \emph (after the folio-472 marker fix the text reads '$\ell$-\emph{adique ...}')."))
f.append(F(472, "Proposition 2 (cont.), lines 3-5",
  r"un morphisme de faisceaux | La formule suivante | où | désigne l'endomorphisme de | défini par | est vraie : underlined (not the formulas, the commas or the colon)",
  r"un morphisme de faisceaux. La formule suivante, où $h_{H^i(X,F)}$ désigne l'endomorphisme de $H^i(X,F)$ défini par $(h,h_F)$, est vraie: (no underline markup)",
  "underline", "high",
  r"F$ un morphisme de faisceaux. La formule suivante, où $h_{H^i(X,F)}$ désigne l'endomorphisme de $H^i(X,F)$ défini par $(h,h_F)$, est vraie:",
  r"F$ \emph{un morphisme de faisceaux}. \emph{La formule suivante}, \emph{où} $h_{H^i(X,F)}$ \emph{désigne l'endomorphisme de} $H^i(X,F)$ \emph{défini par} $(h,h_F)$, \emph{est vraie}:"))
f.append(F(472, "display (2''), left member",
  r"Σ_{x∈X^h} Tr(h_{F_x}) : h with the subscript F_x (x a subscript of F), no parentheses (crop c472_2pp.png)",
  r"\Tr((h_F)_x)",
  "formula", "high", r"\Tr((h_F)_x)", r"\Tr(h_{F_x})",
  note=r"Same notation as h_{(F_\nu)_x} in (3), which the diplomatic layer keeps as printed (the current layer has (h_{F_\nu})_x there and (h_F)_x here)."))
f.append(F(472, "'un faisceau de torsion constructible'",
  r"'torsion' underlined (crop c472_tors.png)",
  r"de torsion constructible (no underline)",
  "underline", "high", r"de torsion constructible", r"de \emph{torsion} constructible"))
f.append(F(472, "display (3), end",
  r"Σ_{x∈X^h} Tr(h_{(F_ν)_x}) = Tr^*h_{RΓ_X(F_ν)} with no punctuation after it; the next line begins 'où les deux membres' (crop c472_3.png)",
  r"\Tr^*h_{\R\Gamma_X(F_\nu)}, (comma before \tag{3})",
  "punctuation", "high", r"\R\Gamma_X(F_\nu)},¶\tag{3}", r"\R\Gamma_X(F_\nu)}¶\tag{3}",
  note="Comma added at the end of the display."))
f.append(F(472, "'s'écrive F = (F_ν)_{ν∈N} , avec F annulé par ℓ^{ν+1}'",
  r"avec F annulé par ℓ^{ν+1} (F without the index ν; crop c472_avecF.png)",
  r"avec $F$ annulé par $\ell^{\nu+1}$",
  "misprint_in_print", "high", corrected=r"avec $F_\nu$ annulé par $\ell^{\nu+1}$",
  note=r"The ℓ-adic sheaf F is not killed by ℓ^{ν+1}; its components F_ν are. The TeX keeps the printed reading."))
f.append(F(472, "'un entier ℓ-adique égal à Σ(-1)^i Tr(h_{H^i(X,F)}) , avec'",
  r"Σ(-1)^i Tr(h_{H^i(X,F)}) with no index under the Σ (run into the text; crop c472_sum.png)",
  r"\sum_i(-1)^i\Tr(h_{H^i(X,F)}),",
  "extra", "high", r"\sum_i(-1)^i\Tr(h_{H^i(X,F)}),", r"\sum(-1)^i\Tr(h_{H^i(X,F)}),",
  note="Summation index added by the TeX."))
# ---------------- page 473 ----------------
f.append(F(473, "line 1: 'morphisme de transition : K_{ν+1} → K_ν'",
  r"morphisme de transition : K_{ν+1} → K_ν (colon after 'transition'; crop c473_l1.png)",
  r"morphisme de transition $K_{\nu+1}\to K_\nu$",
  "punctuation", "high", r"transition $K_{\nu+1}\to K_\nu$", r"transition: $K_{\nu+1}\to K_\nu$"))
f.append(F(473, "lines 1-2: 'au sens des catégories dérivées'",
  r"'au sens des catégories dérivées' underlined",
  r"au sens des catégories dérivées (no underline)",
  "underline", "high", r"au sens des catégories dérivées", r"\emph{au sens des catégories dérivées}"))
f.append(F(473, "line 2: 'au morphisme canonique : K_{ν+1} → ...'",
  r"au morphisme canonique : K_{ν+1} → K_{ν+1}/ℓ^{ν+1}K_{ν+1} . (colon after 'canonique')",
  r"au morphisme canonique (then the display, no colon)",
  "punctuation", "high", r"morphisme canonique¶\[", r"morphisme canonique:¶\["))
f.append(F(473, "'on prendra K_ν = RΓ_X(F_ν) et h_ν = h_{RΓ_X(F_ν)} ;'",
  r"the two formulas are joined by the word 'et' (run into the text), no comma",
  r"K_\nu=\R\Gamma_X(F_\nu),\qquad h_\nu=h_{\R\Gamma_X(F_\nu)};",
  "missing", "high", r"(F_\nu),\qquad h_\nu=", r"(F_\nu)\quad\text{et}\quad h_\nu=",
  note=r"'et' missing and a comma added; \quad\text{...}\quad as the file writes '\quad\text{avec}\quad' on p. 472."))
f.append(F(473, "condition 1), line 1: 'le morphisme de transition : K'_{ν+1} → K'_ν'",
  r"1) le morphisme de transition : K'_{ν+1} → K'_ν (colon after 'transition'; crop c473_items.png)",
  r"le morphisme de transition $K'_{\nu+1}\to K'_\nu$",
  "punctuation", "high", r"transition $K'_{\nu+1}", r"transition: $K'_{\nu+1}"))
f.append(F(473, "condition 1): '(comme morphisme de complexes)'",
  r"est isomorphe (comme morphisme de complexes) à (parentheses)",
  r"est isomorphe, comme morphisme de complexes, à",
  "punctuation", "high", r"est isomorphe, comme morphisme de complexes, à", r"est isomorphe (comme morphisme de complexes) à"))
f.append(F(473, "condition 1): after K'_{ν+1} → K'_{ν+1}/ℓ^{ν+1}K'_{ν+1}",
  r"... /ℓ^{ν+1}K'_{ν+1} , pour (comma after the formula)",
  r"K'_{\nu+1}\to K'_{\nu+1}/\ell^{\nu+1}K'_{\nu+1} (display without the comma)",
  "punctuation", "high", r"/\ell^{\nu+1}K'_{\nu+1}¶\]", r"/\ell^{\nu+1}K'_{\nu+1},¶\]"))
f.append(F(473, "condition 1), end: 'pour tout ν ∈ N .'",
  r"pour tout ν ∈ N . (full stop)",
  r"pour tout $\nu\in\mathbb N$;",
  "punctuation", "high", r"pour tout $\nu\in\mathbb N$;", r"pour tout $\nu\in\mathbb N$."))
f.append(F(473, "condition 2), end",
  r"est compatible avec les morphismes de transition. (full stop)",
  r"est compatible avec les morphismes de transition;",
  "punctuation", "high", r"avec les morphismes de transition;", r"avec les morphismes de transition."))
f.append(F(473, "'on peut alors écrire : Tr^*h_ν = ...'",
  r"on peut alors écrire : Tr^*h_ν = Tr^*h'_ν = Σ(-1)^i Tr h'^i_ν (colon after 'écrire'; crop c473_sum.png)",
  r"on peut alors écrire (then the display, no colon)",
  "punctuation", "high", r"on peut alors écrire¶\[", r"on peut alors écrire:¶\["))
f.append(F(473, "'Tr^*h_ν = Tr^*h'_ν = Σ(-1)^i Tr h'^i_ν'",
  r"Σ(-1)^i Tr h'^i_ν with no index under the Σ (crop c473_sum.png)",
  r"\sum_i(-1)^i\Tr h_\nu'^i",
  "extra", "high", r"=\sum_i(-1)^i\Tr h_\nu'^i", r"=\sum(-1)^i\Tr h_\nu'^i",
  note="Summation index added by the TeX."))
f.append(F(473, "'Soient K' = lim K'_ν , et h' = lim h'_ν (endo-'",
  r"K' = lim_{←ν} K'_ν , et h' = lim_{←ν} h'_ν (the word 'et' between the formulas)",
  r"K'=\varprojlim_\nu K'_\nu, / \qquad h'=\varprojlim_\nu h'_\nu",
  "missing", "high", r"K'_\nu,¶\qquad h'=", r"K'_\nu,¶\quad\text{et}\quad h'=",
  note="'et' missing."))
# ---------------- page 474 ----------------
f.append(F(474, "top of the page: 'endo-' / 'morphisme de K')'",
  r"p. 473 ends with '... h' = lim h'_ν (endo-'; p. 474 begins with 'morphisme de K') . On voit que'",
  r"page_473.tex ends with '(' on its own line; the folio-474 marker follows it and page_474.tex begins 'endomorphisme de $K'$).'",
  "marker", "high",
  note=r"Page 474 really begins at 'morphisme', the second half of 'endo-morphisme'. Exact fix: python -I marker_split_word.py 5 474 split 'endo' 'morphisme' (simulated in memory on both live layers at 17:08: p. 473 then ends with the line '(' and the line 'endo%', and p. 474 begins 'morphisme de $K'$)'). Text not moved. Optional: the line end after '(' prints a space after the parenthesis, now and after the fix ('( endomorphisme'); writing '(endo%' on one line removes it."))
f.append(F(474, "display 'H^i(K') ⥲ lim H^i(K'_ν)'",
  r"an arrow with a tilde over it (hand-drawn ⥲), the same sign as in u : T(L) ⥲ M of Lemme 1 below (crop c474_iso.png)",
  r"H^i(K')\simeq\varprojlim_\nu H^i(K'_\nu)",
  "symbol", "high", r"H^i(K')\simeq", r"H^i(K')\xrightarrow{\sim}",
  note=r"Lemme 1 on this page writes the same printed sign as \xrightarrow{\sim}."))
f.append(F(474, "'le foncteur T : L ⇝ L ⊗_A A_0'",
  r"a hand-drawn squiggly arrow (⇝) between L and L ⊗_A A_0 (crop c474_T.png)",
  r"T:L\longmapsto L\otimes_A A_0",
  "symbol", "high", r"T:L\longmapsto L", r"T:L\rightsquigarrow L",
  note=r"As on p. 471 (T ⇝ T^{p^n}, there \mapsto); the file writes \rightsquigarrow for this arrow in Exposé X."))
f.append(F(474, "Lemme 1, lines 1-3",
  r"Supposons l'idéal | nilpotent | Considérons un complexe | plat en chaque degré | un complexe | projectif en chaque degré et un isomorphisme : underlined (not I, L ∈ D^-(A), M ∈ D^-(A_0) or the punctuation; crop c474_lem1a.png)",
  r"Supposons l'idéal $I$ nilpotent. Considérons un complexe ... et un isomorphisme (no underline markup)",
  "underline", "high",
  r"Supposons l'idéal $I$ nilpotent. Considérons un complexe $L\in D^-(A)$ plat en chaque degré, un complexe $M\in D^-(A_0)$ projectif en chaque degré et un isomorphisme",
  r"\emph{Supposons l'idéal} $I$ \emph{nilpotent}. \emph{Considérons un complexe} $L\in D^-(A)$ \emph{plat en chaque degré}, \emph{un complexe} $M\in D^-(A_0)$ \emph{projectif en chaque degré et un isomorphisme}"))
f.append(F(474, "Lemme 1, lines 3-5",
  r"dans | Il existe un complexe de | modules (of A-modules) | borné à droite et projec-tif en chaque degré | un isomorphisme : underlined (crop c474_lem1b.png)",
  r"dans $D^-(A_0)$. Il existe un complexe de $A$-modules $L'$, borné à droite et projectif en chaque degré, un isomorphisme (no underline markup)",
  "underline", "high",
  r"dans $D^-(A_0)$. Il existe un complexe de $A$-modules $L'$, borné à droite et projectif en chaque degré, un isomorphisme",
  r"\emph{dans} $D^-(A_0)$. \emph{Il existe un complexe de} $A$-\emph{modules} $L'$, \emph{borné à droite et projectif en chaque degré}, \emph{un isomorphisme}"))
f.append(F(474, "Lemme 1, lines 5-6",
  r"dans | et un isomorphisme de complexes : underlined ('et' at the line end, 'un isomorphisme de complexes' on the next line)",
  r"dans $D^-(A)$, et un isomorphisme de complexes (no underline markup)",
  "underline", "high", r"dans $D^-(A)$, et un isomorphisme de complexes",
  r"\emph{dans} $D^-(A)$, \emph{et un isomorphisme de complexes}"))
f.append(F(474, "Lemme 1, last line",
  r"tels que | dans : underlined",
  r"tels que $u=w\circ T(v)$ dans $D^-(A_0)$. (no underline markup)",
  "underline", "high", r"tels que $u=w\circ T(v)$ dans $D^-(A_0)$.",
  r"\emph{tels que} $u=w\circ T(v)$ \emph{dans} $D^-(A_0)$."))
f.append(F(474, "Remarque, line 1: 'supposé libre (resp. de type fini) en chaque degré'",
  r"libre (resp. de type fini) en chaque degré",
  r"libre, respectivement de type fini, en chaque degré",
  "word", "high", r"supposé libre, respectivement de type fini, en", r"supposé libre (resp. de type fini) en",
  note="Abbreviation written out and the parentheses replaced by commas."))
f.append(F(474, "Remarque, line 2: 'aussi libre (resp. de type fini) en cha-'",
  r"aussi libre (resp. de type fini) en cha-",
  r"aussi libre, respectivement de type fini, en chaque",
  "word", "high", r"aussi libre, respectivement de type fini, en", r"aussi libre (resp. de type fini) en",
  note="As above. The old stops before 'chaque', whose 'que' goes to p. 475 with the folio-475 marker fix."))
f.append(F(474, "'h_ν = h_{RΓ_X(F_ν)} , on': below the X",
  r"a stray typed 'i' under the X of h_{RΓ_X(F_ν)}, between the lines, just above the 'm' of 'endomorphisme' on the next line (crop c474_stray.png); it belongs to no formula",
  r"$h_\nu=h_{\R\Gamma_X(F_\nu)}$ (nothing there)",
  "other", "low",
  note=r"A typing slip of the typescript, not a subscript; no edit proposed (the TeX's omission is the sensible reading). Listed only for completeness."))
# ---------------- page 475 ----------------
f.append(F(475, "top of the page: 'cha-' / 'que degré.'",
  r"p. 474 ends with '... (resp. de type fini) en cha-'; p. 475 begins with 'que degré. En effet si un A-module plat N'",
  r"'chaque' ends the last line of page_474.tex; the folio-475 marker follows it and page_475.tex begins 'degré. En effet'",
  "marker", "high",
  note=r"Page 475 really begins at 'que', the second half of 'cha-que'. Exact fix, two steps to apply together: python -I move_marker.py 5 475 'que' --before (its last occurrence before the marker is the end of 'chaque'), then add '%' after the 'cha' that now ends the line before the marker ('... en cha' -> '... en cha%'), so that the halves join without a space. Simulated in memory on both live layers at 17:08: p. 474 then ends 'en cha%', and p. 475 begins 'que' + line end + 'degré. En effet' (printed 'chaque degré'). marker_split_word.py has no mode for a word that lies wholly before the marker. Text not moved."))
f.append(F(475, "lines 1-2: 'soit libre (resp. de type fini), on montre'",
  r"soit libre (resp. de type fini), on montre",
  r"soit libre, respectivement de type fini, on montre",
  "word", "high", r"soit libre, respectivement de type fini, on montre", r"soit libre (resp. de type fini), on montre",
  note="Abbreviation written out and the parentheses replaced by commas."))
f.append(F(475, "lines 2-3: 'N est libre (resp. de type fini) (Bourbaki,'",
  r"N est libre (resp. de type fini) (Bourbaki,",
  r"$N$ est libre, respectivement de type fini (Bourbaki,",
  "word", "high", r"est libre, respectivement de type fini (Bourbaki", r"est libre (resp. de type fini) (Bourbaki",
  note="As above."))
f.append(F(475, "the Bourbaki reference",
  r"(Bourbaki, Alg. Comm., Chap.II, §3, prop. 5): capital C in 'Comm.' and 'Chap.' (crop c475_bourb.png)",
  r"(Bourbaki, Alg. comm., chap.~II, §3, prop.~5)",
  "word", "high", r"Alg. comm., chap.~II", r"Alg. Comm., Chap.~II",
  note="The print has no space in 'Chap.II' (spacing, not reported)."))
f.append(F(475, "'soit L ∈ Ob D^-(A)'",
  r"L ∈ Ob D^-(A) with a capital O (crop c475_ob.png)",
  r"$L\in\Ob D^-(A)$, and \Ob prints 'ob' in this file",
  "word", "high", r"$L\in\Ob D^-(A)$", r"$L\in\operatorname{Ob} D^-(A)$",
  note=r"\Ob is \operatorname{ob}: the first \providecommand{\Ob}{\operatorname{ob}} (s5.tex line 101) wins over the later \operatorname{Ob} definitions (as reported for Exposé VIII). If \Ob is redefined for Exposé XV instead, this edit is not needed."))
f.append(F(475, "'tel que L ⊗^L_A A_0 soit un'",
  r"the L above the tensor sign is a double-struck L (typed I struck over L; crop c475_L.png)",
  r"$L\lten_A A_0$ (\lten is \overset{\mathrm L}{\otimes}: a plain L)",
  "font", "high", r"$L\lten_A A_0$", r"$L\overset{\mathbb L}{\otimes}_A A_0$",
  note=r"The file writes \overset{\mathbb L}{\otimes} for this typescript sign in Exposé X ((X^\bullet,Y^\bullet)\rightsquigarrow X^\bullet\overset{\mathbb L}{\otimes}_A Y^\bullet)."))
f.append(F(475, "'pseudo-cohérent resp. parfait (i.e. isomor-phe'",
  r"pseudo-cohérent resp. parfait (i.e. isomorphe (no comma before 'resp.', 'i.e.' abbreviated, parenthesis opened before 'i.e.'; crop c475_cor.png)",
  r"pseudo-cohérent, respectivement parfait, c'est-à-dire isomorphe",
  "word", "high", r"pseudo-cohérent, respectivement parfait, c'est-à-dire isomorphe", r"pseudo-cohérent resp. parfait (i.e. isomorphe",
  note="Abbreviations written out, commas added, the parenthesis dropped (it closes after 'en chaque degré', two findings below)."))
f.append(F(475, "'borné supérieurement, resp. borné, et'",
  r"borné supérieurement, resp. borné, et",
  r"borné supérieurement, respectivement borné, et",
  "word", "high", r"supérieurement, respectivement borné,", r"supérieurement, resp. borné,",
  note="Abbreviation written out."))
f.append(F(475, "'projectif de type fini en chaque degré). Alors'",
  r"en chaque degré). Alors (the parenthesis opened before 'i.e.' closes here)",
  r"en chaque degré. Alors",
  "punctuation", "high", r"en chaque degré. Alors", r"en chaque degré). Alors"))
f.append(F(475, "end of the Remarque: 'pseudo-cohérent (resp. parfait).'",
  r"de A-modules pseudo-cohérent (resp. parfait).",
  r"pseudo-cohérent, respectivement parfait.",
  "word", "high", r"pseudo-cohérent, respectivement parfait.", r"pseudo-cohérent (resp. parfait).",
  note="Abbreviation written out and the parentheses replaced by a comma."))
f.append(F(475, "Lemme 2, lines 1-4",
  r"Considérons un complexe de | modules borné à droite (of A-modules) | projectif en chaque degré | muni d'un endomorphisme | et un en-domorphisme | de | coïncidant avec | au sens de la catégorie dérivée : underlined (not the formulas or the punctuation; crop c475_lem2.png)",
  r"Considérons un complexe de $A$-modules borné à droite $L$, ... au sens de la catégorie dérivée $D^-(A_0)$. (no underline markup)",
  "underline", "high",
  r"Considérons un complexe de $A$-modules borné à droite $L$, projectif en chaque degré, muni d'un endomorphisme $\varphi$, et un endomorphisme $\varphi_0$ de $M=T(L)$ coïncidant avec $T(\varphi)$ au sens de la catégorie dérivée $D^-(A_0)$.",
  r"\emph{Considérons un complexe de} $A$-\emph{modules borné à droite} $L$, \emph{projectif en chaque degré}, \emph{muni d'un endomorphisme} $\varphi$, \emph{et un endomorphisme} $\varphi_0$ \emph{de} $M=T(L)$ \emph{coïncidant avec} $T(\varphi)$ \emph{au sens de la catégorie dérivée} $D^-(A_0)$."))
f.append(F(475, "Lemme 2, lines 4-5",
  r"Il existe un endomorphisme | de | qui coïncide avec | au sens de | et vérifie : underlined",
  r"Il existe un endomorphisme $\varphi'$ de $L$ qui coïncide avec $\varphi$ au sens de $D^-(A)$ et vérifie (no underline markup)",
  "underline", "high",
  r"Il existe un endomorphisme $\varphi'$ de $L$ qui coïncide avec $\varphi$ au sens de $D^-(A)$ et vérifie",
  r"\emph{Il existe un endomorphisme} $\varphi'$ \emph{de} $L$ \emph{qui coïncide avec} $\varphi$ \emph{au sens de} $D^-(A)$ \emph{et vérifie}",
  note="The colon after 'vérifie' is the next finding (its old begins where this one's ends)."))
f.append(F(475, "Lemme 2, last line: 'et vérifie : T(φ') = φ_0 .'",
  r"et vérifie : T(φ') = φ_0 . (colon after 'vérifie')",
  r"et vérifie $T(\varphi')=\varphi_0$.",
  "punctuation", "high", r" $T(\varphi')=\varphi_0$", r": $T(\varphi')=\varphi_0$",
  note="The old begins with the space after 'vérifie'."))
f.append(F(475, "'avec A = Z/ℓ^{ν+1}Z et I = ℓ^νZ/ℓ^{ν+1}Z'",
  r"the two formulas are joined by the word 'et' (run into the text), no comma (crop c475_AI.png)",
  r"A=\mathbb Z/\ell^{\nu+1}\mathbb Z, / \qquad / I=\ell^\nu\mathbb Z/\ell^{\nu+1}\mathbb Z",
  "missing", "high", r"A=\mathbb Z/\ell^{\nu+1}\mathbb Z,¶\qquad¶I=", r"A=\mathbb Z/\ell^{\nu+1}\mathbb Z¶\quad\text{et}\quad¶I=",
  note="'et' missing and a comma added."))
f.append(F(475, "'compte tenu de la remarque 2,'",
  r"compte tenu de la remarque 2, l'existence (crop c475_rem2.png)",
  r"compte tenu de la remarque 2,",
  "misprint_in_print", "low", corrected=r"compte tenu de la remarque,",
  note=r"No 'remarque 2' exists: the remark used here (L' free of finite type when M is) is the unnumbered 'Remarque' after Lemme 1 (p. 474), the only remark of the exposé besides 'la remarque précédente' of § 1. The TeX keeps the printed reading. Low confidence: the intended reference is uncertain."))
f.append(F(475, "'en un endomorphisme de K' au sens de D^-(A)'",
  r"en un endomorphisme de K' au sens de D^-(A) (K' without the index ν; crop c475_Kp.png)",
  r"en un endomorphisme de $K'$ au sens de $D^-(A)$",
  "misprint_in_print", "medium", corrected=r"en un endomorphisme de $K'_\nu$ au sens de $D^-(A)$",
  note=r"v : K_ν = L ⥲ L' = K'_ν, so h_ν is transported to K'_ν (K' = lim K'_ν of p. 473 is another object); h''_ν : K'_ν → K'_ν follows. The TeX keeps the printed reading."))
f.append(F(475, "end of the page (folio-476 marker)",
  r"p. 475 ends with 'Appliquons alors le deuxième lemme avec L = K'_ν ,'; p. 476 begins with 'φ = h'' et φ_0 = h'_{ν-1} ; nous obtenons' (b476_480/page_476_s1.png)",
  r"page_475.tex ends with '... avec $L=K'_\nu$, $\varphi=h''_\nu$ et $\varphi_0=h'_{\nu-1}$;' before the folio-476 marker",
  "marker", "high",
  note=r"Page 476 really begins at '$\varphi=h'''. ALREADY DONE in both live layers (s5.tex as modified 12 Nov 17:07: the folio-476 marker stands directly before '$\varphi=h''$ et', and the diplomatic layer there reads h'' without the index ν, as printed; this batch's page file still had '$\varphi=h''_\nu$'); nothing to do. A rerun of python -I move_marker.py 5 476 '$\varphi=h' --before prints 'anchor not found' and changes nothing (the anchor occurs once in each layer, after the marker)."))

OUT.write_text(json.dumps(f, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(f), "findings written")
