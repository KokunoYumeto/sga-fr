import json

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b121_125"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_121_125.json"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 121
add(121,
    "Corollary 5.7 (3), first line: 'and X an S-scheme of essentially finite type'",
    "'an' underlined; 'S-' not underlined; the underline resumes at 'scheme of' (checked in a crop)",
    r"\underline{S-scheme of essentially finite type. Given a closed subscheme}",
    "underline", "high",
    fx(r"\underline{S-scheme of essentially", r"$S$-\underline{scheme of essentially"),
    "The letter S and its hyphen stand outside the underline, as in 'S-adic' on pp. 119-120 and in the parallel statement 5.10 (4) on p. 123 (TeX $S$-\\underline{scheme of essentially ...}). The TeX also sets this S as text inside the underline.")

add(121,
    "Proof of 5.7, (1): 'Omega_{X'|S'} ~= O_{S'} (x)^_{O_S} Omega_{X|S}'",
    "isomorphism sign: a tilde over a single bar (checked in a crop)",
    r"\underline{\Omega}_{\mathfrak{X}'|S'} \cong \underline{O}_{S'}",
    "symbol", "high",
    fx(r"\mathfrak{X}'|S'} \cong", r"\mathfrak{X}'|S'} \simeq"),
    "The TeX writes \\cong (two bars); the print has the one-bar sign, which the TeX gives as \\simeq on p. 122 and elsewhere in this exposé.")

add(121,
    "Proof of 5.7, (2): 'O_{X_(x)} (x)^_{O_X} Omega_{X|S} ~= Omega_{X_(x)|S} .'",
    "isomorphism sign: a tilde over a single bar (checked in a crop)",
    r"\;\cong\; \underline{\Omega}_{\mathfrak{X}_{(x)}|S}",
    "symbol", "high",
    fx(r"\;\cong\; \underline{\Omega}", r"\;\simeq\; \underline{\Omega}"),
    "As in (1) just above.")

add(121,
    "Proof of 5.7, (4), first equivalence: 'is formally smooth at x <=> X_nu -> S_nu is formally smooth'",
    "a double-line equivalence arrow (hollow, two strokes; checked in a crop)",
    r"x \leftrightarrow X_\nu \to S_\nu",
    "symbol", "high",
    fx(r"x \leftrightarrow X_\nu", r"x \Leftrightarrow X_\nu"),
    "The TeX has the single-line \\leftrightarrow; the print's sign is the double arrow, which the TeX writes \\Leftrightarrow elsewhere (e.g. pp. 52, 63, 117). Three occurrences in this display; the other two follow.")

add(121,
    "Same display, second equivalence: 'for all nu <=> x notin J^n_{X_nu}(X_nu|S_nu)'",
    "double-line equivalence arrow (checked in a crop)",
    r"\nu \;\leftrightarrow\; x \notin J^{n}_{X_\nu}",
    "symbol", "high",
    fx(r"\nu \;\leftrightarrow\; x", r"\nu \;\Leftrightarrow\; x"),
    "As the previous entry.")

add(121,
    "Same display, third line: '<=> x notin lim-> J^n_{X_nu}(X_nu|S_nu) = J^n_X(X|S)'",
    "double-line equivalence arrow (checked in a crop)",
    r"\\ \leftrightarrow\; x \notin \varinjlim_{\nu}",
    "symbol", "high",
    fx(r"\\ \leftrightarrow\; x", r"\\ \Leftrightarrow\; x"),
    "As the previous entries.")

add(121,
    "Remark 5.8: 'we also consider the S-adic formal scheme X_(x^) = lim-> Spec(O^_{X_v,x})'",
    "subscript (X^) with a CAPITAL X under the hat: 28 px high against 20 px for the small x of X_(x) on the next line and of the (x^) subscripts at the foot of the page (measured in crops)",
    r"\mathfrak{X}_{(\hat{x})} = \varinjlim",
    "misprint_in_print", "high",
    fx(r"\mathfrak{X}_{(\hat{x})} = \varinjlim", r"\mathfrak{X}_{(\hat{X})} = \varinjlim"),
    "Capital/small slip, as in X_(X^_0) on p. 105: the formal scheme is the completion at the point x (Spec of O^_{X_v,x} on the same line), and the foot of this page and pp. 122-123 print the small x^. The TeX silently writes the small x; the fix restores the printed capital, 'corrected' is the current TeX.",
    corrected=r"\mathfrak{X}_{(\hat{x})} = \varinjlim")

add(121,
    "Remark 5.8: 'We thus have the natural morphisms X_(x^) -> X_(x) -> X'",
    "first subscript (X^) with a CAPITAL X (28 px against 19-20 px for the x of the following X_(x); measured in a crop)",
    r"morphisms $\mathfrak{X}_{(\hat{x})} \to",
    "misprint_in_print", "high",
    fx(r"morphisms $\mathfrak{X}_{(\hat{x})}", r"morphisms $\mathfrak{X}_{(\hat{X})}"),
    "As the previous entry. The TeX silently writes the small x; the fix restores the printed capital, 'corrected' is the current TeX.",
    corrected=r"morphisms $\mathfrak{X}_{(\hat{x})}")

add(121,
    "Remark 5.8: 'Now the natural map Omega_{A_v|R_v} -> Omega_{A^_v|R_v} induces an isomorphism'",
    "the small typed hat stands over the subscript A, right of the Omega (hat columns 272-294, A 274-296, Omega 251-271; measured in a crop)",
    r"\Omega_{A_\nu|R_\nu} \to \widehat{\Omega}_{A_\nu|R_\nu}",
    "formula", "high",
    fx(r"\to \widehat{\Omega}_{A_\nu|R_\nu}$ induces", r"\to \Omega_{\widehat{A}_\nu|R_\nu}$ induces"),
    "The hat belongs to A (A^_v is the completion O^_{X_v,x}, as in the definition below, where the hat stands over the O). Contrast p. 125, where Omega^_{A^|R} carries one hat over the Omega and a second over the A.")

add(121,
    "Remark 5.8: 'induces an isomorphism (Omega_{A_v|R_v})^ -> (Omega_{A_v|R_v})^'",
    "both sides printed identically: wide hat over Omega_{A_v|R_v}, no small hat over the second A (checked in a crop)",
    r"\widehat{\Omega_{A_\nu|R_\nu}} \to \widehat{\Omega_{A_\nu|R_\nu}}",
    "misprint_in_print", "medium",
    None,
    "The isomorphism induced by Omega_{A_v|R_v} -> Omega_{A^_v|R_v} goes to the completion of Omega_{A^_v|R_v}, as the next formula (lim (Omega_{A^_v|R_v})^ ) shows; the printed map is from a module to itself. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"\widehat{\Omega_{A_\nu|R_\nu}} \to \widehat{\Omega_{\widehat{A}_\nu|R_\nu}}")

add(121,
    "Remark 5.8: 'lim<-_v (Omega_{A_v|R_v})^ ~-> lim_v (Omega_{A^_v|R_v})^'",
    "inside the wide hat of the right-hand side the small hat stands over the subscript A, not over the Omega (hat columns 462-481, A 462-483, Omega 439-461; measured in a crop)",
    r"\lim_{\nu} \widehat{\widehat{\Omega}_{A_\nu|R_\nu}}",
    "formula", "high",
    fx(r"\lim_{\nu} \widehat{\widehat{\Omega}_{A_\nu|R_\nu}}", r"\lim_{\nu} \widehat{\Omega_{\widehat{A}_\nu|R_\nu}}"),
    "As in the natural map above. Does not overlap the misprint entry on this lim (which has no edit).")

add(121,
    "Same formula, right-hand lim",
    "lim with the index v below and no arrow; the left-hand lim has the arrow <- (checked in a crop)",
    r"\lim_{\nu}",
    "misprint_in_print", "low",
    None,
    "Both sides are projective limits over v; the arrow of the second lim was not typed or written in. Low: possibly the typist's shorthand. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"\varprojlim_{\nu}")

add(121,
    "Remark 5.8, definition: '(Omega_{X_(x^)|S})^ = lim<-_v (Omega_{O^_{X_v,x}|O_{S_v}})^'",
    "inside the wide hat the small hat stands over the underlined O, not over the Omega (hat columns 392-410, O 392-412, Omega 367-390; measured in a crop)",
    r"\widehat{\widehat{\Omega}_{\underline{O}_{X_\nu,x}|\underline{O}_{S_\nu}}}",
    "formula", "high",
    fx(r"\widehat{\widehat{\Omega}_{\underline{O}_{X_\nu,x}|\underline{O}_{S_\nu}}}", r"\widehat{\Omega_{\widehat{\underline{O}}_{X_\nu,x}|\underline{O}_{S_\nu}}}"),
    "The ring is O^_{X_v,x} = A^_v; the file's form for a hatted underlined O is \\widehat{\\underline{O}} (p. 105).")

add(121,
    "Remark 5.8: 'Now O^_{X_0,x} is in general not essentially finite type over S_(y)'",
    "not essentially finite type (no 'of')",
    r"is in general not essentially finite type",
    "misprint_in_print", "low",
    None,
    "Word left out; the exposé writes 'of essentially finite type' or 'essentially of finite type' throughout (e.g. the first sentence of this remark). Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"is in general not of essentially finite type")

# ---------------------------------------------------------------- page 122
add(122,
    "End of Remark 5.8: 'defined by the ideal sheaf I^p_{X_(x^)}(X_(x^)|S) = I^p_{X_(x^)}(Omega_{X_(x^)|S})'",
    "Omega_{X_(x^)|S} printed without a hat (checked in a crop)",
    r"I^{p}_{\mathfrak{X}_{(\hat{x})}}(\Omega_{\mathfrak{X}_{(\hat{x})}|S})",
    "misprint_in_print", "low",
    None,
    "The coherent module whose Fitting ideal is meant is the completed (Omega_{X_(x^)|S})^ defined at the foot of p. 121 ('then (Omega_{X_(x^)|S})^ is a coherent X_(x^)-module. Thus if we set ...'); the plain Omega_{X_(x^)|S} is not defined. Low: the hat may have been left out deliberately as notation. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"I^{p}_{\mathfrak{X}_{(\hat{x})}}(\widehat{\Omega_{\mathfrak{X}_{(\hat{x})}|S}})")

# ---------------------------------------------------------------- page 123
add(123,
    "Corollary 5.10 (2): 'J^p_S(X|S) commute with base change'",
    "J^p_S(X|S) with the typewriter Fraktur X",
    r"$J^p_S(\mathcal{X}|S)$  \underline{commute",
    "font", "high",
    fx(r"$J^p_S(\mathcal{X}|S)$  \underline{commute", r"$J^p_S(\mathfrak{X}|S)$  \underline{commute"),
    "Fraktur typed as \\mathcal. The same Fraktur X is \\mathfrak{X} on pp. 121-122 and 125. Page 123 writes \\mathcal{X}, \\mathcal{Y} throughout (20 places, all covered by the font entries below).")

add(123,
    "Same item: 'i.e., J^p_{S'}(X'|S') = J^p_S(X|S) x_S S''",
    "typewriter Fraktur X twice",
    r"$J^p_{S'}(\mathcal{X}'|S') = J^p_S(\mathcal{X}|S) \times_S S'$",
    "font", "high",
    fx(r"$J^p_{S'}(\mathcal{X}'|S') = J^p_S(\mathcal{X}|S) \times_S S'$", r"$J^p_{S'}(\mathfrak{X}'|S') = J^p_S(\mathfrak{X}|S) \times_S S'$"),
    "Fraktur typed as \\mathcal, as above.")

add(123,
    "Corollary 5.10 (3): 'If J^p_X(X|S) = coprod_{1<=i<=m} Y^(i)'",
    "typewriter Fraktur X twice",
    r"$J^p_{\mathcal{X}}(\mathcal{X}|S) =",
    "font", "high",
    fx(r"$J^p_{\mathcal{X}}(\mathcal{X}|S) =", r"$J^p_{\mathfrak{X}}(\mathfrak{X}|S) ="),
    "Fraktur typed as \\mathcal, as above.")

add(123,
    "Same formula: the disjoint-union sign",
    "an inverted Pi: two vertical strokes standing on a base bar that projects beyond both of them, the product sign of the next line turned upside down (checked in a crop)",
    r"\bigsqcup_{1\leq i\leq m}",
    "symbol", "medium",
    fx(r"\bigsqcup", r"\coprod"),
    "The printed sign is the coproduct sign; \\bigsqcup is a square cup without the projecting bar. The TeX writes the same printed sign \\coprod on p. 120 ('J^p_X(X|S) - coprod ...').")

add(123,
    "Same formula: 'Y^(i)'",
    "typewriter Fraktur Y",
    r"m} \mathcal{Y}^{(i)}$",
    "font", "high",
    fx(r"m} \mathcal{Y}^{(i)}$", r"m} \mathfrak{Y}^{(i)}$"),
    "Fraktur typed as \\mathcal; the TeX writes the same Fraktur Y \\mathfrak{Y} on pp. 126 and 128.")

add(123,
    "Corollary 5.10 (3), next line: 'I^p_S(X|S) = prod_{1<=i<=m} I^0_S(f_*O_{Y(i)})'",
    "typewriter Fraktur X",
    r"$\underline{I}^p_S(\mathcal{X}|S) = \prod_{1\leq i\leq m} \underline{I}^0_S",
    "font", "high",
    fx(r"$\underline{I}^p_S(\mathcal{X}|S) = \prod_{1\leq i\leq m} \underline{I}^0_S", r"$\underline{I}^p_S(\mathfrak{X}|S) = \prod_{1\leq i\leq m} \underline{I}^0_S"),
    "Fraktur typed as \\mathcal, as above.")

add(123,
    "Same formula: 'f_*O_{Y(i)}'",
    "typewriter Fraktur Y",
    r"f_*\underline{O}_{\mathcal{Y}^{(i)}}",
    "font", "high",
    fx(r"f_*\underline{O}_{\mathcal{Y}", r"f_*\underline{O}_{\mathfrak{Y}"),
    "Fraktur typed as \\mathcal, as above. Does not overlap the next entry.")

add(123,
    "Same formula: index of O_{Y(i)}",
    "the (i) stands on the same line as the subscript Y, not raised (in the line above, Y^(i) has a raised (i); checked in a crop)",
    r"\mathcal{Y}^{(i)}})$",
    "formula", "low",
    fx(r"^{(i)}})$", r"(i)})$"),
    "Typewriter placement inside a subscript; the TeX raises (i) to a superscript. Low: the coordinator may prefer to keep the superscript as the evident intent.")

add(123,
    "Display after 'is discrete, then': 'I^p_S(X|S) = prod I^p_S(X_(x_i)|S) = prod I^p_S(X_(x^_i)|S)'",
    "typewriter Fraktur X three times",
    r"\underline{I}^p_S(\mathcal{X}|S) = \prod_{1\leq i\leq m} \underline{I}^p_S(\mathcal{X}_{(x_i)}|S) = \prod_{1\leq i\leq m} \underline{I}^p_S(\mathcal{X}_{(\mathfrak{x}_i)}|S)",
    "font", "high",
    fx(r"\underline{I}^p_S(\mathcal{X}|S) = \prod_{1\leq i\leq m} \underline{I}^p_S(\mathcal{X}_{(x_i)}|S) = \prod_{1\leq i\leq m} \underline{I}^p_S(\mathcal{X}_{(",
       r"\underline{I}^p_S(\mathfrak{X}|S) = \prod_{1\leq i\leq m} \underline{I}^p_S(\mathfrak{X}_{(x_i)}|S) = \prod_{1\leq i\leq m} \underline{I}^p_S(\mathfrak{X}_{("),
    "Fraktur typed as \\mathcal, as above. Does not overlap the next entry (the subscript x^_i).")

add(123,
    "Same display, last subscript: 'X_(x^_i)'",
    "a small x with a typed hat (the same x^ as on pp. 121-122, written \\hat{x} there; checked in a crop)",
    r"\mathcal{X}_{(\mathfrak{x}_i)}",
    "accent", "high",
    fx(r"\mathfrak{x}_i)}|S)", r"\hat{x}_i)}|S)"),
    "The TeX reads the hatted x as a Fraktur x. It is the completion at x_i, X_(x^_i) (Remark 5.8: X_(x^) = lim Spec(O^_{X_v,x})); a typed circumflex sits on the small x.")

add(123,
    "Proof of 5.10: 'Supp f_*O_{J^p_X(X|S)} = |J^p_S(X|S)|'",
    "typewriter Fraktur X three times",
    r"$f_*\underline{O}_{J^p_{\mathcal{X}}(\mathcal{X}|S)}$ $=$ $|J^p_S(\mathcal{X}|S)|$",
    "font", "high",
    fx(r"$f_*\underline{O}_{J^p_{\mathcal{X}}(\mathcal{X}|S)}$ $=$ $|J^p_S(\mathcal{X}|S)|$", r"$f_*\underline{O}_{J^p_{\mathfrak{X}}(\mathfrak{X}|S)}$ $=$ $|J^p_S(\mathfrak{X}|S)|$"),
    "Fraktur typed as \\mathcal, as above.")

add(123,
    "Proof of 5.10: 'the isomorphism J^p_{X_(x^)}(X_(x^)|S) ~-> J^p_{X_(x)}(X_(x)|S)'",
    "typewriter Fraktur X four times; the first two subscripts are the small x with a typed hat (checked in a crop)",
    r"$J^p_{\mathcal{X}_{(\mathfrak{x})}}(\mathcal{X}_{(\mathfrak{x})}|S) \xrightarrow{\sim} J^p_{\mathcal{X}_{(x)}}(\mathcal{X}_{(x)}|S)$",
    "font", "high",
    fx(r"$J^p_{\mathcal{X}_{(\mathfrak{x})}}(\mathcal{X}_{(\mathfrak{x})}|S) \xrightarrow{\sim} J^p_{\mathcal{X}_{(x)}}(\mathcal{X}_{(x)}|S)$",
       r"$J^p_{\mathfrak{X}_{(\hat{x})}}(\mathfrak{X}_{(\hat{x})}|S) \xrightarrow{\sim} J^p_{\mathfrak{X}_{(x)}}(\mathfrak{X}_{(x)}|S)$"),
    "One edit for two differences that interleave: Fraktur typed as \\mathcal (4x) and the hatted x read as \\mathfrak{x} (2x), as in the display above. The same isomorphism is written J^p_{\\mathfrak{X}_{(\\hat{x})}}(\\mathfrak{X}_{(\\hat{x})}|S) -> J^p_{\\mathfrak{X}_{(x)}}(...) on p. 122.")

add(123,
    "Same sentence: 'for an isolated point x in J^p_X(X|S) .'",
    "typewriter Fraktur X twice",
    r"in  $J^p_{\mathcal{X}}(\mathcal{X}|S)$  .",
    "font", "high",
    fx(r"in  $J^p_{\mathcal{X}}(\mathcal{X}|S)$  .", r"in  $J^p_{\mathfrak{X}}(\mathfrak{X}|S)$  ."),
    "Fraktur typed as \\mathcal, as above.")

add(123,
    "Corollary 5.10 (2): 'J^p_S(X|S) commute with base change'",
    "commute (no s)",
    r"\underline{commute with base change}",
    "misprint_in_print", "low",
    None,
    "Verb agreement slip (singular subject J^p_S(X|S)); Remark 5.11 says the Jacobian ideal 'commutes with base change'. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"\underline{commutes with base change}")

add(123,
    "Remark 5.11: 'f is smooth at x if and only if x notin Supp O_X/O_{X|Y} by 3.13(a)'",
    "O_X/O_{X|Y}: both letters are underlined O's (checked in a crop)",
    r"\mathrm{Supp}\ \underline{O}_X/\underline{O}_{X|Y}",
    "misprint_in_print", "high",
    None,
    "The quotient is by the ideal sheaf I_{X|Y} obtained in the preceding sentence ('we obtain the ideal sheaf I_{X|Y}'); O_{X|Y} is not defined. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"\mathrm{Supp}\ \underline{O}_X/\underline{I}_{X|Y}")

# ---------------------------------------------------------------- page 124
add(124,
    "Section 6, second paragraph: 'is said to be a non-degenerate quadratic singu- / larity rational over k'",
    "singu- / larity: the word is divided at the line end",
    r"singu-larity",
    "other", "high",
    fx(r"singu-larity", r"singularity"),
    "The TeX keeps the print's line-end hyphen inside the word.")

add(124,
    "Same sentence: 'if O^_{X,x} - k[[x_1,...,x_n]]/(f)'",
    "a single dash at mid-height between O^_{X,x} and k; no tilde above it (checked in a crop)",
    r"$\hat{O}_{X,x}$ $-$ $k$",
    "misprint_in_print", "medium",
    None,
    "The definition requires an isomorphism O^_{X,x} ~= k[[x_1,...,x_n]]/(f), as in Lemma 6.2 on p. 125 ('A^_0 ~= k[[x_1,...,x_n]]/(f)'); only the bar of the sign was typed. Same kind of slip as the hyphen for '=' on p. 120. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"$\hat{O}_{X,x}$ $\simeq$ $k$")

add(124,
    "Proof of Lemma 6.1: 'If we set X_i^(1) = X_i - e_i^(1) , then f(x_1^(1),...,x_n^(1)) ='",
    "X_i^(1) and X_i: CAPITAL X, 27-28 px high against 20-21 px for the small x of f(x_1^(1),... on the same line (measured in a crop)",
    r"$X_i^{(1)} = X_i - \epsilon_i^{(1)}$",
    "misprint_in_print", "high",
    None,
    "Capital/small slip: the variables are x_1,...,x_n, and the next formula is f(x_1^(1),...,x_n^(1)); p. 125 has x_i^(v) = x_i - (...). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"$x_i^{(1)} = x_i - \epsilon_i^{(1)}$")

# ---------------------------------------------------------------- page 125
add(125,
    "Proof of Lemma 6.1, first line: 'such that Sum e_i^(2) df/dx_u^(1) == h_4 (mod M^5)'",
    "df/dx_u^(1): the subscript is a clear u (checked in a crop)",
    r"\partial f/\partial x_u^{(1)}",
    "misprint_in_print", "high",
    None,
    "Index slip: the sum runs over i (e_i^(2)), and the next line has Sum e_i^(2) df/dx_i^(1); p. 124 has Sum e_i^(1) df/dx_i. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"\partial f/\partial x_i^{(1)}")

add(125,
    "Lemma 6.2, first line: 'Let A_0 be a local k-algebra, essentially of finite type such that'",
    "'be a local' underlined; 'k-' not underlined; 'algebra, essentially of finite type such that' underlined (checked in a crop)",
    r"\underline{be a local k-algebra, essentially of finite type such that}",
    "underline", "high",
    fx(r"\underline{be a local k-algebra, essentially of finite type such that}", r"\underline{be a local} $k$-\underline{algebra, essentially of finite type such that}"),
    "The letter k and its hyphen stand outside the underline, as in 'S-adic' and 'S-scheme' on pp. 119-123; the TeX also sets this k as text inside the underline.")

add(125,
    "Lemma 6.2 (2): 'J_R(X|R) is a principal ideal in R generated by a free formal generator of R over Lambda i.e. I_R(X|R) = (t)'",
    "J_R(X|R) is a principal ideal",
    r"(2)  $J_R(\mathfrak{X}|R)$  \underline{is a principal ideal in}",
    "misprint_in_print", "low",
    None,
    "J_R(X|R) is the closed formal subscheme of Spec(R); the principal ideal is its ideal I_R(X|R) = (t), as the same item says after 'i.e.'. Low: possibly the author's loose wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"(2)  $I_R(\mathfrak{X}|R)$  \underline{is a principal ideal in}")

add(125,
    "Proof of Lemma 6.2, heading 'Proof:'",
    "the underline ends under the f; the colon is not underlined (checked in a crop)",
    r"\underline{Proof:}",
    "underline", "high",
    fx(r"\underline{Proof:}", r"\underline{Proof}:"),
    "As written for the other proofs of these pages (\\underline{Proof}: on pp. 121, 123, 124).")

add(125,
    "Last display: '0 -> A^ --df-- A^dx_1 (+) ... (+) A^dx_n ------ Omega^_{A^|R} -> 0', first map",
    "df over a plain ruled line with no arrowhead; the line ends cleanly at both sides (checked in a crop); the outer maps 0 -> A^ and -> 0 are typed arrows",
    r"\overset{df}{\longrightarrow}",
    "misprint_in_print", "medium",
    fx(r"\overset{df}{\longrightarrow}", r"\overset{df}{\relbar\joinrel\relbar\joinrel\relbar}"),
    "The heads of the two long maps of the exact sequence were never drawn. The TeX silently supplies them; the fix restores the printed headless rule in the form proposed for p. 85 (\\overset{...}{\\relbar\\joinrel\\relbar\\joinrel\\relbar}). 'corrected' is the current TeX.",
    corrected=r"\overset{df}{\longrightarrow}")

add(125,
    "Same display, second map (A^dx_1 (+) ... (+) A^dx_n to Omega^_{A^|R})",
    "a long plain ruled line with no arrowhead, no label (checked in a crop)",
    r"\xrightarrow{\hspace{3em}}",
    "misprint_in_print", "medium",
    fx(r"\xrightarrow{\hspace{3em}}", r"\relbar\joinrel\relbar\joinrel\relbar\joinrel\relbar\joinrel\relbar"),
    "As the previous entry. 'corrected' is the current TeX.",
    corrected=r"\xrightarrow{\hspace{3em}}")

add(125,
    "Same display, last term: 'Omega^_{A^|R}'",
    "two typed hats: one above the Omega and one above the subscript A (checked in a crop)",
    r"\Omega_{\hat{A}|R}",
    "accent", "high",
    fx(r"\Omega_{\hat{A}|R}", r"\hat{\Omega}_{\hat{A}|R}"),
    "The TeX has only the hat on A; the print also hats the Omega (the completed module of differentials, cf. Remark 5.8).")


# ---------------------------------------------------------------- checks
texts = {p: open(f"{BASE}\\page_{p}.tex", encoding="utf-8").read() for p in range(121, 126)}
ok = True
spans = {}
for i, d in enumerate(F):
    t = texts[d["page"]]
    if d["tex"] not in t:
        print("TEX NOT FOUND", i, d["page"], d["tex"])
        ok = False
    if d["fix"] is not None:
        old = d["fix"]["old"]
        n = t.count(old)
        if n != 1:
            print("OLD COUNT", n, i, d["page"], old)
            ok = False
        else:
            s = t.index(old)
            if "%%%%%%%%%%" in old or "\n" in old and "%%%%" in old:
                print("MARKER IN OLD", i)
                ok = False
            spans.setdefault(d["page"], []).append((s, s + len(old), i))
for p, lst in spans.items():
    lst.sort()
    for a, b in zip(lst, lst[1:]):
        if a[1] > b[0]:
            print("OVERLAP page", p, "entries", a[2], b[2])
            ok = False

# apply all fixes per page to check they compose
for p in range(121, 126):
    t = texts[p]
    for d in F:
        if d["page"] == p and d["fix"] is not None:
            assert t.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t = t.replace(d["fix"]["old"], d["fix"]["new"])
    if p == 123:
        print("mathcal left on 123:", t.count("\\mathcal"), " mathfrak{x} left:", t.count("\\mathfrak{x}"))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(121, 126):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("OK" if ok else "PROBLEMS", len(F))
