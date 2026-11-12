"""Build findings_326_330.json and check every fix: each 'old' must occur exactly once in its page file at the time
it is applied (fixes applied in the listed order); also report whether it occurs exactly once in the original file
and, for non-misprint fixes, in the current layer's text of the same page."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b326_330"
OUT = RUN / "findings_326_330.json"
CUR = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\current\s5.tex")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 326
add(326, "top of the page: the diagram",
    "p. 326 begins with the whole diagram (first row H^p(Y,(L|Y)(-1)) --Gysin--> H^{p+2}(X,L)); p. 325 ends with "
    "'... diagramme suivant, avec p <= n-1 .'",
    r"'\[', '\begin{array}{ccc}' and 'H^p(Y,(L|Y)(-1))&' end page_325.tex; the folio-326 marker stands inside the "
    r"array, before '\xrightarrow{\mathrm{Gysin}}&H^{p+2}(X,L)\\'",
    "marker", "high", None, None,
    r"Page 326 really begins at the '\[' that opens the diagram (the line after '... avec $p\le n-1$:'; diplomatic "
    r"s5.tex line 11006, current 11002, at the time of the check; the marker stands at 11009 and 11005). Exact fix: python -I move_marker.py 5 326 '\[' "
    r"--before (simulated in memory on both layers: the marker then stands on its own line between "
    r"'... avec $p\le n-1$:' and '\[', and the array is whole on p. 326). The anchor is the last '\[' above the "
    r"marker, so run the command once only (not again if batch 321-325 reports the same move). Text not moved.")
add(326, "diagram, end of the bottom row",
    "H^{2n-p}(X,L(n-1-p)) with no stop", r"H^{2n-p}(X,L(n-1-p)).", "punctuation", "high",
    r"H^{2n-p}(X,L(n-1-p)).", r"H^{2n-p}(X,L(n-1-p))",
    "The TeX adds a full stop at the end of the display.")
add(326, "last paragraph, the reference to Kleiman",
    "'... l'exposé de Kleiman (Algebraic cycles and the Weil conjectures, in \"Dix exposés ...' (title not "
    "underlined, opening straight quote)",
    r"'Kleiman, \emph{Algebraic cycles and the Weil conjectures}, dans «Dix'",
    "other", "high",
    r"Kleiman, \emph{Algebraic cycles and the Weil conjectures}, dans «Dix",
    r"Kleiman (Algebraic cycles and the Weil conjectures, in ``Dix",
    "One edit for four differences: the print's parenthesis for the TeX's comma (punctuation), no underline on the "
    "English title (the TeX adds \\emph), 'in' for 'dans' (word), and the straight quote, written ``, for the "
    "guillemet (as the applied fixes of pp. 110, 183, 249). The parenthesis closes after the title: next items but "
    "one.")
add(326, "last paragraph, 'cohomologie de schémas'",
    "'\"Dix exposés sur la cohomologie de schémas .).'", r"'cohomologie des schémas'",
    "misprint_in_print", "high",
    r"cohomologie des", r"cohomologie de",
    "The book is 'Dix exposés sur la cohomologie des schémas'; the TeX silently corrects the typist's 'de'.",
    corrected=r"cohomologie des")
add(326, "last paragraph, end of the reference",
    "'... de schémas .).' (closing parenthesis, then the final stop; no closing quote: next item)",
    r"'schémas».' (guillemet, no parenthesis)",
    "punctuation", "high",
    r"schémas».", r"schémas'').",
    "The TeX drops the print's closing parenthesis (it turns the parenthesis into commas, previous items but one); "
    "the edit also writes the closing quote in the file's form ''. This is the correct reading; the print's own "
    "reading of the quote is the next item. Apply this item before the next one.")
add(326, "last paragraph, end of the reference",
    "'schémas .).': the closing quote is missing; a full stop stands in its place",
    r"'schémas»' (the TeX supplies a closing quote and has no stray stop)",
    "misprint_in_print", "high",
    r"schémas'')", r"schémas .)",
    "Typing error: a full stop for the closing quote; the TeX silently corrects it. 'old' is taken from the text "
    "after the previous item (as instructed for overlapping fixes): apply that item first; this 'old' then occurs "
    "exactly once.",
    corrected=r"schémas'')")

# ---------------------------------------------------------------- p. 327
add(327, "section title 8", "'8. VARIETES ECLATEES' (capitals, underlined, no stop)",
    r"\section*{8. Variétés éclatées}", "word", "high",
    r"\section*{8. Variétés éclatées}", r"\section*{8. VARIÉTÉS ÉCLATÉES}",
    "Capitals as printed, as the logged '3. CLASSES DE CHERN' (p. 290) and '1. FIBRES VECTORIELS' (p. 282); "
    "accented capitals as the volume's rule. The print has no stop after the title.")
add(327, "first paragraph, 'le \"groupe des classes de cycles\"'", "straight typewriter quotes",
    r"«groupe des classes de cycles»", "punctuation", "high",
    r"«groupe des classes de cycles»", r"``groupe des classes de cycles''",
    "Guillemets for the print's straight quotes; the accepted forms are ``...'' and \"...\" (as the applied fixes "
    "of pp. 110, 183, 249).")
add(327, "first paragraph, 'le morphisme \"classe fondamentale\"'", "straight typewriter quotes",
    r"«classe fondamentale»", "punctuation", "high",
    r"«classe fondamentale»", r"``classe fondamentale''",
    "Guillemets for the print's straight quotes.")
add(327, "Théorème 8.1, 'Le morphisme de D+(X,A)'", "'Le morphisme de' underlined",
    r"Le morphisme de $D^+(X,A)$", "underline", "high",
    r"Le morphisme de $D^+(X,A)$", r"\emph{Le morphisme de} $D^+(X,A)$",
    "Exposé VII: the TeX has no underline markup for statements; \\emph is the file's command here (as the applied "
    "statements of pp. 283-295).")
add(327, "Théorème 8.1, 'défini par la matrice'", "underlined", "défini par la matrice", "underline", "high",
    r"défini par la matrice", r"\emph{défini par la matrice}")
add(327, "Théorème 8.1, 'est un isomorphisme.'", "underlined (the stop not)", "est un isomorphisme.",
    "underline", "high",
    r"est un isomorphisme.<NL>\end{statement}", r"\emph{est un isomorphisme}.<NL>\end{statement}")
add(327, "proof of 8.1, 'au-dessus de U = X ∸ Y'", "a minus with a dot above it (∸), dot crisp and centred",
    r"$U=X-Y$", "symbol", "high",
    r"$U=X-Y$", r"$U=X\mathbin{\dot{-}}Y$",
    "As the applied fix of p. 285 (C^r ∸ 0, now \\mathbb C^r\\mathbin{\\dot{-}}0 in both layers); the same sign on "
    "p. 330.")
add(327, "Lemme 8.2, statement",
    "underlined: 'Soient', 'un corps séparablement clos' (the comma not), 'un entier, et', 'Alors'",
    r"Soient $k$ un corps séparablement clos, $r\ge1$ un entier, et $P=\mathbb P_k^r$. Alors:",
    "underline", "high",
    r"Soient $k$ un corps séparablement clos, $r\ge1$ un entier, et $P=\mathbb P_k^r$. Alors:",
    r"\emph{Soient} $k$ \emph{un corps séparablement clos}, $r\ge1$ \emph{un entier, et} $P=\mathbb P_k^r$. "
    r"\emph{Alors} :",
    "The P of P^r_k is a plain typed P (see the message).")
add(327, "Lemme 8.2 a)", "'a) L'application canonique A → H°(P,A) est une bijection.' (underlined word groups)",
    r"\item l'application canonique $A\to H^0(P,A)$ est une bijection;", "underline", "high",
    r"\item l'application canonique $A\to H^0(P,A)$ est une bijection;",
    r"\item \emph{L'application canonique} $A\to H^0(P,A)$ \emph{est une bijection}.",
    "One edit: it also gives the print's capital L (word) and its full stop for the TeX's semicolon (punctuation).")
add(327, "Lemme 8.2 b)", "'b) H^1(P,A) = H^{2r-1}(P,A) = 0 .'", r"... =0$;", "punctuation", "high",
    r"=H^{2r-1}(P,A)=0$;", r"=H^{2r-1}(P,A)=0$.",
    "The TeX has a semicolon for the print's full stop.")

# ---------------------------------------------------------------- p. 328
add(328, "top of the page: item c) of Lemme 8.2",
    "p. 328 begins with 'c) Pour 0 ≤ p ≤ 2r-2 , ...'; p. 327 ends with 'b) H^1(P,A) = H^{2r-1}(P,A) = 0 .'",
    r"the '\item' that prints 'c)' is the last line of page_327.tex; the folio-328 marker follows it",
    "marker", "high", None, None,
    r"Page 328 really begins at the '\item' of c) (diplomatic s5.tex line 11056, current 11052, at the time of the "
    r"check). Exact fix: python -I move_marker.py 5 328 '\item' --before (simulated in memory on both layers: the "
    r"marker then stands on its own line between '\item $H^1(P,A)=H^{2r-1}(P,A)=0$;' and '\item'). The anchor is the "
    r"last '\item' above the marker, so run the command once only. Text not moved; independent of the p. 327 edits.")
add(328, "Lemme 8.2 c), 'Pour 0 ≤ p ≤ 2r-2 , la multiplication par'",
    "'Pour' (capital P) and 'la multiplication par' underlined",
    r"pour $0\le p\le2r-2$, la multiplication par", "underline", "high",
    r"pour $0\le p\le2r-2$, la multiplication par $",
    r"\emph{Pour} $0\le p\le2r-2$, \emph{la multiplication par} $",
    "One edit: it also gives the print's capital P (word).")
add(328, "Lemme 8.2 c), 'ξ = cℓ(O_P(1)) ∈ H^2(P,μ) .' before the display",
    "a full stop after H^2(P,μ), then the display and 'est un isomorphisme.'",
    r"no punctuation after $\xi=c\ell(\mathcal O_P(1))\in H^2(P,\mu)$",
    "misprint_in_print", "medium",
    r"\in H^2(P,\mu)$<NL>", r"\in H^2(P,\mu)$.<NL>",
    "A stray full stop in mid-sentence (the sentence goes on with the display and 'est un isomorphisme'); the TeX "
    "silently drops it. Drop this item if the stop is taken as the print's punctuation.",
    corrected=r"\in H^2(P,\mu)$<NL>")
add(328, "Lemme 8.2 c), 'est un isomorphisme.'", "underlined, full stop",
    "est un isomorphisme;", "underline", "high",
    r"est un isomorphisme;", r"\emph{est un isomorphisme}.",
    "One edit: it also gives the print's full stop for the TeX's semicolon (punctuation).")
add(328, "Lemme 8.2 d), 'Le morphisme trace'", "'Le morphisme trace' underlined, capital L",
    r"\item le morphisme trace", "underline", "high",
    r"\item le morphisme trace", r"\item \emph{Le morphisme trace}",
    "One edit: it also gives the print's capital L (word).")
add(328, "Lemme 8.2 d), 'est une bijection.'", "underlined", "est une bijection.", "underline", "high",
    r"est une bijection.<NL>\end{enumerate}", r"\emph{est une bijection}.<NL>\end{enumerate}")
add(328, "'tout complexe M de A_X-Modules' before the displays H*(T,M)", "capital M",
    r"$A_X$-modules", "word", "high",
    r"$A_X$-modules<NL>", r"$A_X$-Modules<NL>",
    "The typescript's capital M (sheaf of modules), as the applied 'Module' of pp. 282-295.")
add(328, "displays H*(T,M) = H*(T,h*(M)) and H*_Z(T,M) = H*_Z(T,h*(M)).",
    "two lines, the second preceded by 'et'; no comma after the first",
    r"H^*(T,M)=H^*(T,h^*(M)),\qquad", "missing", "high",
    r"H^*(T,M)=H^*(T,h^*(M)),\qquad<NL>", r"H^*(T,M)=H^*(T,h^*(M))<NL>\quad\text{et}\quad<NL>",
    "The TeX drops the printed 'et' and adds a comma (written as the applied fix of p. 283).")
add(328, "Corollaire 8.3, first sentence",
    "underlined: 'Pour tout complexe', 'de', '-Modules et tout', 'les applications'",
    r"Pour tout complexe $M$ de $A_X$-modules et tout $p\in\mathbb Z$, les applications",
    "underline", "high",
    r"Pour tout complexe $M$ de $A_X$-modules et tout $p\in\mathbb Z$, les applications",
    r"\emph{Pour tout complexe} $M$ \emph{de} $A_X$-\emph{Modules et tout} $p\in\mathbb Z$, "
    r"\emph{les applications}",
    "One edit: it also gives the print's capital M (word).")
add(328, "number of the display (8.3.1)", "'(8.3.1.)' with a stop; '(8.3.2)' has none", r"\tag{8.3.1}",
    "number", "high",
    r"\tag{8.3.1}", r"\tag{8.3.1.}",
    "As printed, as the logged '(3.5.1.)' of p. 293.")
add(328, "Corollaire 8.3, 'et' between (8.3.1) and (8.3.2)", "underlined", "et", "underline", "high",
    r"\]<NL>et<NL>\[", r"\]<NL>\emph{et}<NL>\[")
add(328, "Corollaire 8.3, 'définies par la matrice'", "underlined", "définies par la matrice", "underline", "high",
    r"définies par la matrice", r"\emph{définies par la matrice}")
add(328, "Corollaire 8.3, 'sont des bijections.'", "underlined (the stop not)", "sont des bijections.",
    "underline", "high",
    r"sont des bijections.", r"\emph{sont des bijections}.")
add(328, "proof of 8.3, 'sur les p^èmes objets de cohomologie'", "p with a raised 'èmes'", r"$p$-ièmes",
    "word", "high",
    r"$p$-ièmes", r"$p^{\text{èmes}}$",
    "As the applied ν^{èmes} of p. 282.")
add(328, "proof of 8.3, first morphism 'IRΓ(X, μ ⊗ id_M)'",
    "μ (Greek mu, with its descender) where u is meant",
    r"$\R\Gamma(X,u\otimes\operatorname{id}_M)$", "misprint_in_print", "high",
    r"morphismes $\R\Gamma(X,u", r"morphismes $\R\Gamma(X,\mu",
    "The morphism is u, 'le morphisme (8.1.1)' of the line above; the TeX silently corrects. Independent of the "
    "tensor-sign item that follows (the two olds do not overlap).",
    corrected=r"morphismes $\R\Gamma(X,u")
add(328, "proof of 8.3, first morphism, the tensor sign", "⊗ with two bars under it",
    r"\otimes", "symbol", "medium",
    r"\otimes\operatorname{id}_M)$ et", r"\mathbin{\underline{\underline{\otimes}}}\operatorname{id}_M)$ et",
    "Written as the applied fixes of pp. 285 and 289 (\\mathbin{\\underline{\\underline{\\otimes}}}); one decision "
    "with the other occurrences of the exposé.")
add(328, "proof of 8.3, second morphism 'IRΓ(X, u ⊗ id_M)'",
    "IRΓ(X, ...) without the subscript Y (no trace of it)",
    r"$\R\Gamma_Y(X,u\otimes\operatorname{id}_M)$", "misprint_in_print", "high",
    r"\R\Gamma_Y(X", r"\R\Gamma(X",
    "The arrows (8.3.2) are maps of cohomology with supports in Y and Y', so RΓ_Y is meant ('respectivement'); the "
    "TeX silently corrects. Independent of the tensor-sign item that follows.",
    corrected=r"\R\Gamma_Y(X")
add(328, "proof of 8.3, second morphism, the tensor sign", "⊗ with two bars under it",
    r"\otimes", "symbol", "medium",
    r"\otimes\operatorname{id}_M)$ respectivement",
    r"\mathbin{\underline{\underline{\otimes}}}\operatorname{id}_M)$ respectivement",
    "As the previous tensor-sign item.")
add(328, "numbered paragraph 8.4", "'8.4.' with a stop", r"\subsection*{8.4}", "punctuation", "high",
    r"\subsection*{8.4}", r"\subsection*{8.4.}",
    "As the applied '2.1.', '2.2.5.' (pp. 285, 289).")

# ---------------------------------------------------------------- p. 329
add(329, "Lemme 8.4.1, statement up to 'le O_p-Module'",
    "underlined: 'Soient', 'un schéma,' (with the comma), 'un', '-Module localement libre de rang constant', 'et', "
    "'le fibré projectif associé. Désignant par' (one stretch), 'le'",
    r"Soient $S$ un schéma, $E$ un $\mathcal O_S$-module localement libre ... Désignant par $F$ le",
    "underline", "high",
    r"Soient $S$ un schéma, $E$ un $\mathcal O_S$-module localement libre de rang constant $d$, et "
    r"$p:P=\mathbb P_S(E)\to S$ le fibré projectif associé. Désignant par $F$ le $",
    r"\emph{Soient} $S$ \emph{un schéma,} $E$ \emph{un} $\mathcal O_S$-\emph{Module localement libre de rang "
    r"constant} $d$, \emph{et} $p:P=\mathbb P_S(E)\to S$ \emph{le fibré projectif associé. Désignant par} $F$ "
    r"\emph{le} $",
    "One edit: it also gives the print's capital M (word). The P of P_S(E) is a plain typed P (see the message). "
    "Ends before the O_p of the next item (the olds do not overlap).")
add(329, "Lemme 8.4.1, 'le O_p-Module'",
    "the subscript is a small p: bowl 15 rows, stem 6 rows below it at 300 dpi (the capital P of 'P = P_S(E)' on "
    "the line: bowl 12, stem 9-10; the small p of 'p : P': bowl 14, stem 7)",
    r"$\mathcal O_P$-module", "misprint_in_print", "medium",
    r"$\mathcal O_P$-", r"$\mathcal O_p$-",
    "As the logged O_p items of pp. 286-295: the sheaf is O_P of P = P_S(E); the TeX silently corrects. On p. 328 "
    "the subscripts of O_P(1) and μ_P are capitals (bowl 11-12, stem 9-10).",
    corrected=r"$\mathcal O_P$-")
add(329, "Lemme 8.4.1, 'défini par la suite exacte canonique' (after O_p-Module)",
    "'-Module' and 'défini par la suite exacte canonique' underlined",
    r"module défini par la suite exacte canonique", "underline", "high",
    r"module défini par la suite exacte canonique", r"\emph{Module défini par la suite exacte canonique}",
    "One edit: it also gives the print's capital M (word).")
add(329, "Lemme 8.4.1, display 0 → F → p*(E) → O_p(1) → 0 ,",
    "small p subscript: bowl 14 rows, stem 7 (as the small p of p*(E) in the same display: bowl 15, stem 6)",
    r"\mathcal O_P(1)\to0,", "misprint_in_print", "medium",
    r"\mathcal O_P(1)\to0,", r"\mathcal O_p(1)\to0,",
    "As the previous O_p item; the TeX silently corrects.",
    corrected=r"\mathcal O_P(1)\to0,")
add(329, "Lemme 8.4.1, 'on a la relation'", "underlined", "on a la relation", "underline", "high",
    r"on a la relation<NL>\[<NL>p_*", r"\emph{on a la relation}<NL>\[<NL>p_*")
add(329, "proof of 8.4.1, 'posons ξ = c_1(O_p(1))'", "small p subscript: bowl 15 rows, stem 5-6",
    r"c_1(\mathcal O_P(1))", "misprint_in_print", "medium",
    r"c_1(\mathcal O_P(1))", r"c_1(\mathcal O_p(1))",
    "As the previous O_p items; the TeX silently corrects.",
    corrected=r"c_1(\mathcal O_P(1))")
add(329, "proof of 8.4.1, display 'c(F) = p*(c(E))(1+ξ)^{-1}   d'où'", "no comma after (1+ξ)^{-1}",
    r"(1+\xi)^{-1},", "punctuation", "high",
    r"(1+\xi)^{-1},", r"(1+\xi)^{-1}",
    "The TeX adds a comma at the end of the display.")
add(329, "Lemme 8.4.3, first sentence",
    "underlined: 'On note', 'le', '-Module localement libre défini par la suite exacte canonique'",
    r"On note $F$ le $\mathcal O_{Y'}$-module localement libre défini par la suite exacte canonique",
    "underline", "high",
    r"On note $F$ le $\mathcal O_{Y'}$-module localement libre défini par la suite exacte canonique",
    r"\emph{On note} $F$ \emph{le} $\mathcal O_{Y'}$-\emph{Module localement libre défini par la suite exacte "
    r"canonique}",
    "One edit: it also gives the print's capital M (word).")
add(329, "Lemme 8.4.3, second sentence",
    "underlined: 'Soient', 'un', '-Module localement constant constructible au voisinage de', 'et', 'un entier', "
    "'Pour tout', 'on a la relation'",
    r"Soient $M$ un $A_X$-module localement constant constructible ... on a la relation",
    "underline", "high",
    r"Soient $M$ un $A_X$-module localement constant constructible au voisinage de $Y$, et $p$ un entier $\ge0$. "
    r"Pour tout $y\in H^p(Y,M)$, on a la relation",
    r"\emph{Soient} $M$ \emph{un} $A_X$-\emph{Module localement constant constructible au voisinage de} $Y$, "
    r"\emph{et} $p$ \emph{un entier} $\ge0$. \emph{Pour tout} $y\in H^p(Y,M)$, \emph{on a la relation}",
    "One edit: it also gives the print's capital M (word).")
add(329, "Lemme 8.4.3, 'dans H^{p+2d}_{Y'}(X',M ⊗ μ^{⊗d}) .'", "'dans' underlined", "dans", "underline", "high",
    r"dans $H_{Y'}^{p+2d}", r"\emph{dans} $H_{Y'}^{p+2d}")

# ---------------------------------------------------------------- p. 330
add(330, "display (8.4.4)", "j*(z) = g*(y)[c_d(g*Ň) - c_{d-1}(F̌)c_1(O_{Y'}(-1))] = 0 .  (square brackets)",
    r"\bigl( ... \bigr)", "formula", "high",
    r"\bigl(c_d(g^*\check N)-c_{d-1}(\check F)c_1(\mathcal O_{Y'}(-1))\bigr)",
    r"\bigl[c_d(g^*\check N)-c_{d-1}(\check F)c_1(\mathcal O_{Y'}(-1))\bigr]",
    "The TeX has parentheses for the print's square brackets.")
add(330, "'Posant U = X ∸ Y et U' = X' ∸ Y''", "two minus signs with a dot above (∸)",
    r"$U=X-Y$ et $U'=X'-Y'$", "symbol", "high",
    r"$U=X-Y$ et $U'=X'-Y'$", r"$U=X\mathbin{\dot{-}}Y$ et $U'=X'\mathbin{\dot{-}}Y'$",
    "As p. 327 and the applied fix of p. 285.")
add(330, "diagram (8.4.5), top right", "H^{p+2d}(Y) (no prime; checked at 4x)",
    r"H^{p+2d}(Y')", "misprint_in_print", "high",
    r"\xrightarrow{j^*}&H^{p+2d}(Y')", r"\xrightarrow{j^*}&H^{p+2d}(Y)",
    "j : Y' → X', so j* lands in H^{p+2d}(Y'); the TeX silently corrects.",
    corrected=r"\xrightarrow{j^*}&H^{p+2d}(Y')")
add(330, "display f_*(z) = f_*f*(i_*(y)) - ...", "parentheses around i_*(y)", r"f_*f^*i_*(y)",
    "formula", "high",
    r"f_*f^*i_*(y)", r"f_*f^*(i_*(y))",
    "The TeX drops the parentheses.")
add(330, "'d'où en utilisant (4.2),'", "no comma after d'où", "d'où, en utilisant", "punctuation", "high",
    r"d'où, en utilisant", r"d'où en utilisant",
    "The TeX adds a comma.")
add(330, "Proposition 8.5, first sentence",
    "underlined: 'Soit', 'un', '-Module localement constant constructible au voisinage', 'de'",
    r"Soit $M$ un $A_X$-module localement constant constructible au voisinage de $Y$.", "underline", "high",
    r"Soit $M$ un $A_X$-module localement constant constructible au voisinage de $Y$.",
    r"\emph{Soit} $M$ \emph{un} $A_X$-\emph{Module localement constant constructible au voisinage de} $Y$.",
    "One edit: it also gives the print's capital M (word).")
add(330, "Proposition 8.5 a), 'Notant'", "underlined", r"\item Notant", "underline", "high",
    r"\item Notant", r"\item \emph{Notant}")
add(330, "Proposition 8.5 a), 'l'unique application définie par la relation'", "underlined",
    "l'unique application définie par la relation", "underline", "high",
    r"l'unique application définie par la relation", r"\emph{l'unique application définie par la relation}")
add(330, "Proposition 8.5 a), 'on a' before (8.5.2)", "underlined", "on a", "underline", "high",
    r"on a<NL>\[<NL>g_*", r"\emph{on a}<NL>\[<NL>g_*")


# ---------------------------------------------------------------- checks
def current_page(folio):
    t = CUR.read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return t[m.start():ms[i + 1].start()]
    return ""


ok = True
for page in sorted({f["page"] for f in F}):
    orig = (B / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    assert "\r" not in orig
    cur = current_page(page)
    t = orig
    for f in F:
        if f["page"] != page or f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        n_now, n_orig = t.count(old), orig.count(old)
        n_cur = cur.count(old)
        bad = n_now != 1
        ok &= not bad
        print(f"{page} {f['kind'][:12]:12} now={n_now} orig={n_orig} cur={n_cur} {'BAD' if bad else ''} "
              f"{old[:60]!r}")
        for line in old.split("\n"):
            assert not MARK.search(line), "old crosses a marker"
        t = t.replace(old, new, 1)
    # control characters
    assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", t)
print("ALL OK" if ok else "PROBLEMS")
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print(len(F), "findings written to", OUT)
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in sorted({f["page"] for f in F}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
