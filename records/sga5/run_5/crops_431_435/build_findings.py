# Builds findings_431_435.json (helper for the scan check of SGA 5 pp. 431-435).
import json

OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_431_435.json'
F = []
NL = "\n"


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 431 ----------------
add(431, "first display, S_{x,l^n}(f,f',G,phi) : G -> Lambda_n",
    "S_{x,ℓ^n}(f,f',G,φ) : G ⟶ Λ_n ,",
    r"S_{x,\ell^n}(f,f',G,\varphi):G\longrightarrow\La_n",
    "punctuation", "high",
    r"G\longrightarrow\La_n", r"G\longrightarrow\La_n,",
    "The print ends the display with a comma; the TeX has none.")

add(431, "s'obtient à partir de la fonction i_l o S_x(f,F',G,phi)",
    "i_ℓ o S_x(f,F',G,φ)  (capital F')",
    r"$i_\ell\circ S_x(f,F',G,\varphi)$",
    "misprint_in_print", "high", None, None,
    "Capital F' (the sheaf) for the lift f', which the next display and 6.2 have. "
    "The TeX keeps the printed reading (its source comment documents the erratum).",
    corrected=r"i_\ell\circ S_x(f,f',G,\varphi)")

add(431, "heading 6.3",
    "6.3. Une formule de Lefschetz.  (title underlined, then a full stop)",
    r"\subsection*{6.3. Une formule de Lefschetz}",
    "punctuation", "high",
    r"\subsection*{6.3. Une formule de Lefschetz}",
    r"\subsection*{6.3. Une formule de Lefschetz.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")

add(431, "statement 6.3, first sentence",
    "Sous les hypothèse et avec les notations de 5.1, 6.1, 6.2, on a la formule :  "
    "(underlined up to 'formule'; the colon is not)",
    "Sous les hypothèses et avec les notations de 5.1, 6.1, 6.2, on a la formule :  (no underline)",
    "underline", "high",
    "Sous les hypothèses et avec les notations de 5.1, 6.1, 6.2, on a la formule :",
    r"\emph{Sous les hypothèses et avec les notations de 5.1, 6.1, 6.2, on a la formule} :",
    r"The statement of 6.3 is underlined in the print. Exposé XII writes underlined statements "
    r"with \emph (Conjecture 4.5, Proposition 4.6, Lemme 4.7). Apply before the misprint fix "
    r"'hypothèse' below: the two olds overlap.")

add(431, "statement 6.3: 'Sous les hypothèse'",
    "Sous les hypothèse", "Sous les hypothèses",
    "misprint_in_print", "high",
    "hypothèses", "hypothèse",
    r"The print has the singular 'hypothèse' after 'les'; the TeX silently corrects. "
    r"The old is the same word in the original text and after the \emph fix above.",
    corrected="hypothèses")

add(431, "'où on a posé' before (6.3.2)",
    "où on a posé.  (the words underlined, the full stop not)",
    "où on a posé  (no underline)",
    "underline", "high",
    "où on a posé", r"\emph{où on a posé}",
    "Part of the underlined statement 6.3.")

add(431, "full stop after 'où on a posé', before (6.3.2)",
    "où on a posé.", "où on a posé  (no full stop)",
    "misprint_in_print", "medium",
    NL + r"\begin{equation}" + NL + r"\tag{6.3.2}",
    "." + NL + r"\begin{equation}" + NL + r"\tag{6.3.2}",
    r"The print puts a full stop mid-sentence, before the display that completes 'où on a posé'; "
    r"the TeX silently drops it. The fix puts the stop at the end of that line (after the closing "
    r"brace once the \emph fix is applied: in the print the stop stands outside the underline).",
    corrected="où on a posé")

# ---------------- page 432 ----------------
add(432, "(6.3.4), middle term",
    "Tr_A(ℝΓ_X((u,f)_{u,x}))  (lowercase u,x)",
    r"\Tr_A(\RG_X((u,f)_{U,X}))+",
    "misprint_in_print", "high",
    r"_{U,X}))+", r"_{u,x}))+",
    "Lowercase u,x in the subscript (capitals U,X elsewhere, e.g. (6.3.6), (6.3.10)); the TeX silently corrects.",
    corrected=r"(u,f)_{U,X}")

add(432, "(6.3.4), last term",
    "Tr_A(ℝΓ_Y(u|_Y,f|_Y))  (Y after each bar at subscript level)",
    r"\Tr_A(\RG_Y(u|Y,f|Y)).",
    "formula", "high",
    r"u|Y,f|Y", r"u|_Y,f|_Y",
    "The Y after each bar is lowered in the print, as in (6.3.5) (where the TeX has u|_Y,f|_Y).")

add(432, "(6.3.6), left side",
    "ℝΓ_X(u,f)_{U,X})  (no second opening parenthesis)",
    r"\RG_X((u,f)_{U,X})",
    "misprint_in_print", "high",
    r"\tag{6.3.6}" + NL + r"\RG_X((u,f)_{U,X})", r"\tag{6.3.6}" + NL + r"\RG_X(u,f)_{U,X})",
    "Unbalanced parentheses in the print; the TeX silently adds the opening one.",
    corrected=r"\RG_X((u,f)_{U,X})")

add(432, "(6.3.6), right side",
    "ℝΓ^G ℝΓ_{X'}(u',f')_{U',X'})  (no second opening parenthesis)",
    r"\RG_{X'}((u',f')_{U',X'})",
    "misprint_in_print", "high",
    r"\RG_{X'}((u',f')_{U',X'}),\quad", r"\RG_{X'}(u',f')_{U',X'}),\quad",
    "Unbalanced parentheses in the print; the TeX silently adds the opening one.",
    corrected=r"\RG_{X'}((u',f')_{U',X'})")

add(432, "(6.3.7), isomorphism sign (convention entry; also (6.3.6), (6.3.8), (6.3.9))",
    "≈  (typed, two tildes)", r"\simeq",
    "symbol", "medium",
    r"F_{U',X'}\simeq", r"F_{U',X'}\approx",
    r"Convention: the print types the isomorphism sign as ≈ in (6.3.6)-(6.3.9); the TeX writes \simeq "
    r"(s5.tex has \simeq 223 times, \approx 4 times). Reported once, not itemized: decide globally "
    r"(or rule ≈ a typewriter substitute for ≃) and change all four on this page or none.")

add(432, "(6.3.7), first tensor product",
    "Λ_{n,U',X'} ⊗_{Λ_n} M,  (plain ⊗, no L)",
    r"\La_{n,U',X'}\otimes_{\La_n}^{\mathbf L}M,",
    "extra", "high",
    r"\otimes_{\La_n}^{\mathbf L}M", r"\otimes_{\La_n}M",
    "The print has a plain tensor product here; the TeX adds a derived L.")

add(432, "(6.3.8), left side",
    "ℝΓ_{X'}(u',f')_{U'X'}  (no comma in the subscript)",
    r"\RG_{X'}(u',f')_{U',X'}",
    "misprint_in_print", "high",
    r"\tag{6.3.8}" + NL + r"\RG_{X'}(u',f')_{U',X'}", r"\tag{6.3.8}" + NL + r"\RG_{X'}(u',f')_{U'X'}",
    "No comma between U' and X' in the print; the TeX silently adds it.",
    corrected=r"_{U',X'}")

add(432, "(6.3.8), tensor product",
    "⊗_{Λ_n} with a hand-drawn double-struck 𝕃 above",
    r"\otimes_{\La_n}^{\mathbf L}u_M.",
    "font", "high",
    r"\otimes_{\La_n}^{\mathbf L}u_M.", r"\otimes_{\La_n}^{\mathbb L}u_M.",
    r"Double-struck L in the print (the TeX of Exposé XII has \mathbb{L} elsewhere, (2.1)-(2.6)); "
    r"all five \mathbf L of the exposé are on this page.")

add(432, "(6.3.9), right side: f'Λ",
    "(ℝΓ_{X'}(f'Λ_{n,U',X'})^∨  (Λ on the line, not lowered after f')",
    r"(\RG_{X'}(f'_{\La_{n,U',X'}}))^\vee",
    "misprint_in_print", "medium",
    r"(\RG_{X'}(f'_{\La_{n,U',X'}}", r"(\RG_{X'}(f'\La_{n,U',X'}",
    "Here the print types Λ on the line after f' (in (6.3.7), (6.3.8), (6.3.10) it is lowered as the "
    "subscript of f'); the TeX silently sets the subscript. The old ends before the '))' that the "
    "parenthesis fix below changes.",
    corrected=r"f'_{\La_{n,U',X'}}")

add(432, "(6.3.9), outer parenthesis (1 of 2): after the f' term",
    "(ℝΓ_{X'}(f'Λ_{n,U',X'})^∨ ⊗^𝕃_{Λ_n} A)⊗^𝕃_A u^∨",
    r"(\RG_{X'}(f'_{\La_{n,U',X'}}))^\vee\otimes_{\La_n}^{\mathbf L}A\otimes_A^{\mathbf L}u_M^\vee",
    "formula", "high",
    r"))^\vee", r")^\vee",
    "The print closes the outer parenthesis after A, not after the f' term: remove one ')' here and "
    "add one after A (next finding). Apply both together.")

add(432, "(6.3.9), outer parenthesis (2 of 2): after A",
    "... ⊗^𝕃_{Λ_n} A)⊗^𝕃_A u^∨",
    r"A\otimes_A",
    "formula", "high",
    r"A\otimes_A", r"A)\otimes_A",
    "Second half of the parenthesis fix above; apply both together.")

add(432, "(6.3.9), first tensor product",
    "⊗_{Λ_n} with a double-struck 𝕃 above",
    r"\otimes_{\La_n}^{\mathbf L}A",
    "font", "high",
    r"^{\mathbf L}A", r"^{\mathbb L}A",
    "Double-struck L in the print.")

add(432, "(6.3.9), second tensor product",
    "⊗_A with a double-struck 𝕃 above",
    r"\otimes_A^{\mathbf L}",
    "font", "high",
    r"\otimes_A^{\mathbf L}", r"\otimes_A^{\mathbb L}",
    "Double-struck L in the print.")

add(432, "(6.3.9), last factor",
    "u^∨  (no index M)", r"u_M^\vee",
    "misprint_in_print", "high",
    r"_M^\vee.", r"^\vee.",
    "The print drops the index M (u_M in (6.3.8), u_M^∨ in (6.3.10), (6.3.11)); the TeX silently adds it.",
    corrected=r"u_M^\vee")

add(432, "(6.3.10), tensor product",
    "⊗_{A[G]} with a double-struck 𝕃 above",
    r"\otimes_{A[G]}^{\mathbf L}",
    "font", "high",
    r"\otimes_{A[G]}^{\mathbf L}", r"\otimes_{A[G]}^{\mathbb L}",
    "Double-struck L in the print.")

add(432, "(6.3.11), summation index",
    "g∈G♮φ  (no comma)", r"g\in G_{\natural,\varphi}",
    "formula", "medium",
    r"G_{\natural,\varphi}", r"G_{\natural\varphi}",
    r"No comma between the hand-drawn ♮ and φ in the print (the TeX itself has G_{\natural\varphi} "
    r"at source line 13903).")

add(432, "(6.3.11), argument of the trace",
    "(f'_{𝓗^∨_{n,U'X'}})  (∨ written after the hand-drawn H, at its level, below f')",
    r"(f'{}^\vee_{H_{n,U',X'}})",
    "formula", "medium",
    r"}\Tr_{\La_n[G],\varphi}(f'{}^\vee_{H", r"}\Tr_{\La_n[G],\varphi}(f'_{H^\vee",
    r"In (6.3.11) the print attaches ∨ to the H (f' on H^∨), not to f'; in (6.3.12) the ∨ stands at the "
    r"level of f', where the TeX's f'{}^\vee fits. The hand-drawn script H is the convention entry on p. 433.")

add(432, "(6.3.11), subscript of H",
    "n,U'X'  (no comma between U' and X')", r"n,U',X'",
    "misprint_in_print", "high",
    r"U',X'}})(g)", r"U'X'}})(g)",
    "No comma between U' and X' in the print; the TeX silently adds it. Independent of the ∨ fix above.",
    corrected=r"U',X'")

add(432, "'Mais la trace Tr(...) se calcule'",
    "Tr_{Λ_n[G],φ}(f'_{𝓗_{n,U',X'}})  (no ∨)",
    r"$\Tr_{\La_n[G],\varphi}(f'{}^\vee_{H_{n,U',X'}})$",
    "misprint_in_print", "medium",
    r"(f'{}^\vee_{H_{n,U',X'}})$", r"(f'_{H_{n,U',X'}})$",
    "The print omits the ∨ of the trace computed in (6.3.11)/(6.3.12); the TeX silently adds it.",
    corrected=r"(f'{}^\vee_{H_{n,U',X'}})")

add(432, "'(cf. Proposition 5.1 b))'",
    "(cf, Proposition", "(cf. Proposition",
    "misprint_in_print", "medium",
    "(cf. Proposition", "(cf, Proposition",
    "The mark after 'cf' has a comma's tail and sits lower than the round full stops of '5.1.b' and "
    "'cf.Exp.XI' on this page; the TeX silently gives a full stop.",
    corrected="(cf. Proposition")

add(432, "'Proposition 5.1 b)'",
    "5.1.b))", "5.1 b))",
    "punctuation", "high",
    "5.1 b))", "5.1.b))",
    "The print has a full stop between 1 and b.")

# ---------------- page 433 ----------------
add(433, "(6.3.12), argument of the trace",
    "Tr_{Λ_n[G],φ} f'^∨_{𝓗_{n,U',X'}})(g)  (no opening parenthesis)",
    r"\Tr_{\La_n[G],\varphi}(f'{}^\vee_{H_{n,U',X'}})(g)",
    "misprint_in_print", "high",
    r"\varphi}(f'", r"\varphi}f'",
    "Unbalanced parentheses in the print; the TeX silently adds the opening one.",
    corrected=r"\varphi}(f'")

add(433, "(6.3.12), the hand-drawn H (convention entry; also p. 432 (6.3.11) and 'Mais la trace')",
    "hand-drawn script H (curled left stem) in 𝓗_{n,U',X'}", r"H_{n,U',X'}",
    "font", "medium",
    r"{}^\vee_{H_{n,U',X'}}", r"{}^\vee_{\mathcal{H}_{n,U',X'}}",
    "Convention: the print hand-draws a script H here (a plain H would be typed); the TeX writes plain H "
    "here and throughout Exposé XII (from source line 13803). Reported once, not itemized: decide globally.")

add(433, "'la formule de l'énoncé'",
    "l'énnoncé", "l'énoncé",
    "misprint_in_print", "high",
    "l'énoncé", "l'énnoncé",
    "Double n in the print; the TeX silently corrects.",
    corrected="l'énoncé")

add(433, "heading 6.4",
    "6.4. Remarques sur les termes locaux.  (title underlined, then a full stop)",
    r"\subsection*{6.4. Remarques sur les termes locaux}",
    "punctuation", "high",
    r"\subsection*{6.4. Remarques sur les termes locaux}",
    r"\subsection*{6.4. Remarques sur les termes locaux.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")

add(433, "'La relation 6.4.1 permet'",
    "La relation 6.4.1. permet", "La relation 6.4.1 permet",
    "punctuation", "high",
    "La relation 6.4.1 permet", "La relation 6.4.1. permet",
    "The print has a full stop after the number.")

add(433, "'au cas où il existe'",
    "au cas ou il existe  (no grave accent)", "au cas où il existe",
    "misprint_in_print", "high",
    "au cas où", "au cas ou",
    "No accent in the print (the typewriter has ù, used for 'où' elsewhere on these pages); the TeX silently corrects.",
    corrected="au cas où")

add(433, "a), last line: 'au moins un point x' ∈ X'^f_x'",
    "x' ∈ X'^f_x", r"$x'\in X_x^{\prime f}$",
    "misprint_in_print", "medium", None, None,
    r"The fixed points meant are those of f' on X'_x (the source writes {X'_x}^{g^{-1}f'} in section 4); "
    r"the print has f, and the TeX keeps it. The source comment at b) says the TeX was normalized to f' "
    r"and \in; it was not.",
    corrected=r"x'\in X_x^{\prime f'}")

add(433, "b): 'Soit x' = X'^f_x'",
    "Soit x' = X'^f_x", r"Soit $x'=X_x^{\prime f}$",
    "misprint_in_print", "medium", None, None,
    "'=' for '∈' (and f for f', as in a)); the TeX keeps the printed reading.",
    corrected=r"x'\in X_x^{\prime f'}")

add(433, "b): 'G_{x'} la stabilisation du point x''",
    "la stabilisation", "la stabilisation",
    "misprint_in_print", "medium", None, None,
    "Wrong word for the stabilizer (section 4: 'G_{x'} étant le stabilisateur du point x''); the TeX keeps "
    "the printed reading (its comment documents it).",
    corrected="le stabilisateur")

add(433, "display φ_{x'} = φ|G_{x'}",
    "φ_{x'} = φ|G_{x'} : G_{x'} ⟶ G_{x'} .  (G_{x'} on the line after the bar)",
    r"\varphi|_{G_{x'}}",
    "formula", "high",
    r"\varphi|_{G_{x'}}", r"\varphi|G_{x'}",
    "The print sets G_{x'} on the line after the bar, not as a subscript.")

add(433, "'par F'/G_{x'} l'endomorphisme de X'/G_{x'}'",
    "F'/G_{x'}", r"$F'/G_{x'}$",
    "misprint_in_print", "high", None, None,
    "Capital F' for the endomorphism obtained from f' (p. 434 writes f'/G_{x'}); the TeX keeps the printed "
    "reading (its comment documents it).",
    corrected=r"f'/G_{x'}")

# ---------------- page 434 ----------------
add(434, "display v = p_2(u)",
    "v = p_2(u) : (f'/G_{x'})* (p_2^*(F)) ⟶ p_2^*(F) .",
    r"v = p_2(u)",
    "misprint_in_print", "low", None, None,
    "The text calls v the inverse image of u by p_2 and writes p_2^*(F) in the same display, so the star "
    "is probably missing; the TeX keeps the printed reading.",
    corrected=r"v = p_2^*(u)")

add(434, "(6.4.3), third argument of α_{x'}",
    "α_{x'}(f'/G_{x'},U,f',G_{x'},φ_{x'})",
    r"\alpha_{x'}(f'/G_{x'}, v, U, G_{x'}, \varphi_{x'})",
    "formula", "high",
    r"U, G_{x'}, \varphi_{x'})", r"f', G_{x'}, \varphi_{x'})",
    "The print's third argument is f' (as in α_x(f,u,f',G,φ) on the right); the TeX has U there and loses f'.")

add(434, "(6.4.3), second argument of α_{x'}",
    "U  (capital, second argument)", "v",
    "misprint_in_print", "high",
    r"/G_{x'}, v,", r"/G_{x'}, U,",
    "The print has U where the homomorphism v just defined is meant; the TeX silently corrects (and puts the "
    "U in the third place, previous finding). The two olds do not overlap.",
    corrected="v")

add(434, "heading c): 'modérément ramifié'",
    "modérement  (second e without accent)", "modérément",
    "misprint_in_print", "high",
    "modérément", "modérement",
    "The print lacks the second acute accent; the TeX silently corrects.",
    corrected="modérément")

add(434, "'l'ordre du groupe G_{x'} est premier'",
    "groupe G_x , est premier  (no prime; stray comma)", r"groupe $G_{x'}$ est premier",
    "misprint_in_print", "high",
    r"groupe $G_{x'}$ est", r"groupe $G_x$ , est",
    "The print has G_x without the prime and a comma before 'est'; the TeX silently corrects both.",
    corrected=r"groupe $G_{x'}$ est")

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), 'findings written')
