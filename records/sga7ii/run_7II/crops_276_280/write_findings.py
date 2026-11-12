import json, sys
sys.stdout.reconfigure(encoding='utf-8')
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_276_280_recheck.json'
F = []
def add(**kw):
    F.append(kw)

# ---------------- page 276 ----------------
add(page=276,
    where="display after 'Commençons par (4.2.3.1).'",
    scan="(0 ⊕ x) Λ (0 ⊕ y) = ? ⊕ ?' : the product sign is the typed capital Lambda (cap height, 24 px like the digit 0 of the line; thin left and heavy right stroke, the style of the Δ on this page)",
    tex=r"(0 \oplus x) \wedge (0 \oplus y)",
    kind="symbol", confidence="high",
    fix={"old": r"(0 \oplus x) \wedge (0 \oplus y)", "new": r"(0 \oplus x) \Lambda (0 \oplus y)"},
    note="The cup product of §4 is typed with the capital Λ here, as in (4.2.3.2)-(4.2.3.4) on p. 272. The one real small wedge of pp. 276-280 is in ?' = -g_*i*(i_*g*(x) ∧ i_*g*(y)) on p. 277 (20 px, even strokes), which the TeX rightly writes \\wedge.")

add(page=276,
    where="diagram after 'compte tenu de ce que', label of the arrow ~Δ → Δ × P^1",
    scan="g × ρ_i : the i is typed a half line below ρ",
    tex=r'\arrow[r, "g \times \rho_i"{yshift=7pt}',
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r'\arrow[r, "g \times \rho i"{yshift=7pt}',
    note="The map is (g, ρi), with ρi : ~Δ → ~X → P^1 the composite written (ρi) in Lemme 4.3 and (4.3.1); no ρ_i is defined. The TeX keeps the printed subscript (its STRUCTURE comment also says 'rho with subscript i').")

add(page=276,
    where="display after 'il suffit de démontrer'",
    scan="g_*(g*(x)[(ρi)* (c_1(ξ_P1)) - g*(c_1(ξ_Δ)]) = x",
    tex=r"- g^*(c_1(\xi_\Delta)]) = x",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"- g^*(c_1(\xi_\Delta))]) = x",
    note="One closing parenthesis is missing in the print: g*( is not closed before ']'. The TeX keeps the printed reading.")

add(page=276,
    where="formula (4.3.1)",
    scan="g_*(g*(x) (ρi)*(c_1(ξ_P1)) = x",
    tex=r"g_*(g^*(x) (\rho i)^*(c_1(\xi_{\mathbb{P}^1})) = x",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"g_*(g^*(x) (\rho i)^*(c_1(\xi_{\mathbb{P}^1}))) = x",
    note="The parenthesis opened by g_*( is never closed in the print. The TeX keeps the printed reading.")

add(page=276,
    where="computation of ?, first line",
    scan="? = f_*((i_*g*(x))(i_*g*(y))",
    tex=r"? &= f_*((i_*g^*(x))(i_*g^*(y)) \\",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"? &= f_*((i_*g^*(x))(i_*g^*(y))) \\",
    note="The parenthesis opened by f_*( is never closed in the print. The TeX keeps the printed reading.")

# ---------------- page 277 ----------------
add(page=277,
    where="'Quant à (4.2.3.2) : (a ⊕ 0)Λ(b ⊕ 0) = ab ⊕ 0'",
    scan="(a ⊕ 0)Λ(b ⊕ 0) : typed capital Lambda (24 x 25 px, thin left and heavy right stroke)",
    tex=r"(a \oplus 0) \wedge (b \oplus 0)",
    kind="symbol", confidence="high",
    fix={"old": r"(a \oplus 0) \wedge (b \oplus 0)", "new": r"(a \oplus 0) \Lambda (b \oplus 0)"},
    note="Same capital Λ for the cup product as on p. 276 and p. 272; the small ∧ in the first line of this page is a different glyph.")

add(page=277,
    where="display after 'de sorte que'",
    scan="(a ⊕ 0) Λ (0 ⊕ y) = 0 ⊕ ? , : typed capital Lambda (26 x 27 px, thin left and heavy right stroke)",
    tex=r"(a \oplus 0) \wedge (0 \oplus y)",
    kind="symbol", confidence="high",
    fix={"old": r"(a \oplus 0) \wedge (0 \oplus y)", "new": r"(a \oplus 0) \Lambda (0 \oplus y)"},
    note="Capital Λ for the cup product, as above.")

add(page=277,
    where="second line of the computation of ?'",
    scan="= -g_*i*(i_*(g*(xy) c_1(N_{~Δ/~X}))) par (4.3.2)",
    tex=r"\widetilde{X}}))) \qquad \text{par (4.3.2)} \\",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\widetilde{X}}))) \qquad \text{par (4.2.12)} \\",
    note="Wrong reference: the step i_*g*(x) ∧ i_*g*(y) = i_*(g*(xy) c_1(N)) is (4.2.12), i_*(x)i_*(y) = i_*(xy c_1(N)), cited for the identical step on p. 276; (4.3.2), g_*(g*(x) c_1(N)) = -x, plays no part. The TeX keeps the print.")

add(page=277,
    where="third line of the computation of ?'",
    scan="= -g_*(g*(xy)(c_1(N_{~Δ/~X}))^2) par (4.3.2) ,",
    tex=r"^2) \qquad \text{par (4.3.2)} \quad ,",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"^2) \qquad \text{par (4.2.11)} \quad ,",
    note="Wrong reference: the step i*i_*(w) = c_1(N) w is (4.2.11); (4.3.2) plays no part. The TeX keeps the print.")

add(page=277,
    where="display after 'or,', right-hand side",
    scan="(g*c_1(O_{Δ(1)}) - ... : the twist (1) is typed at subscript level with Δ",
    tex=r"c_1(\underline{O}_{\Delta(1)})",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"c_1(\underline{O}_{\Delta}(1))",
    note="The sheaf is O_Δ(1) = ξ_Δ (p. 275). The TeX keeps the printed position of (1); same slip as Z_{ℓ(-1)} on p. 280.")

add(page=277,
    where="line ?' = - g_*(...) + g_*(2g*(xy)...)",
    scan="+ g_*(2g*(xy)g*(c_1(ξ_Δ)(ρi)*(c_1(ξ_P1))",
    tex=r"+ g_*(2g^*(xy)g^*(c_1(\xi_\Delta)(\rho i)^*(c_1(\xi_{\mathbb{P}^1}))",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"+ g_*(2g^*(xy)g^*(c_1(\xi_\Delta))(\rho i)^*(c_1(\xi_{\mathbb{P}^1})))",
    note="Two closing parentheses are missing in the print: one for g*( and one for g_*(. The TeX keeps the printed reading.")

add(page=277,
    where="line '? = 0 + 2xy c_1(ξ_Δ) par (4.2.4) et (4.3.1)'",
    scan="? = 0 + 2xy c_1(ξ_Δ) (no prime, checked at 2x)",
    tex=r"? &= 0 + 2xy",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"?' &= 0 + 2xy",
    note="The line continues the computation of ?' (the second component; ? = j_*(-xy) was found on p. 276); the print drops the prime. The TeX keeps the printed '?'.")

add(page=277,
    where="'la formule de projection implique Ker f_* ∩ image f* ⊂ Ker f_*'",
    scan="Ker f_* ∩ image f* ⊂ Ker f_*",
    tex=r"\mathrm{Ker}\, f_* \cap \mathrm{image}\, f^*",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\mathrm{Ker}\, f_* \wedge \mathrm{image}\, f^*",
    note="With the intersection the inclusion is trivial; the projection formula f_*(u.f*(a)) = f_*(u).a gives that the cup product of Ker f_* with image f* lies in Ker f_*. ∧ is the product sign of §4; ∪ would do equally. The TeX keeps the printed ∩.")

# ---------------- page 278 ----------------
add(page=278,
    where="first line, continuation of (4.3.3)",
    scan="= - g_*(i*f*(a) g*(y) c_1(N_{~Δ/~X})) par (4.3.2)",
    tex=r"\mathrm{par} \; (4.3.2)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\mathrm{par} \; (4.2.11)",
    note="Wrong reference: the step i*(f*(a) i_*g*(y)) = i*f*(a) g*(y) c_1(N) is (4.2.11), i*i_*(x) = c_1(N) x; (4.3.2) is used only in the step to j*(a).y. Same slip as the two 'par (4.3.2)' of p. 277. The TeX keeps the print.")

# ---------------- page 279 ----------------
add(page=279,
    where="(5.1.2), label of the arrow",
    scan="m*+h* : the star of h sits a little lower than that of m but well above the baseline (not a lower star like k_* or h_* of (5.1.5))",
    tex=r"\xrightarrow{\;m^*+h^*\;}",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\xrightarrow{\;m^*+h_*\;}",
    note="The component H^{·-2}(Δ, Z_ℓ(-1)) → H^·(Y, Z_ℓ) raises the degree by 2: it is the Gysin map h_*; the proof on p. 280 gives k*i_*g* = h_*ℓ*g* with g.ℓ = id. The TeX keeps h^*.")

# ---------------- page 280 ----------------
add(page=280,
    where="'et de k*i_*g* = h_*ℓ*g* par (5.1.5)), et'",
    scan="k*i_*g*  = h_*ℓ*g*  par (5.1.5)), et",
    tex=r"$= h_*\ell^*g^*$ par (5.1.5)),",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"($= h_*\ell^*g^*$ par (5.1.5)),",
    note="Unbalanced closing parenthesis in the print: the opening parenthesis before '= h_*ℓ*g*' is missing. The TeX keeps the printed reading.")

add(page=280,
    where="second composite, source",
    scan="H˙^{-2}(Y,Z_{ℓ(-1)}) : the twist (-1) typed at subscript level with ℓ",
    tex=r"H^{\bullet-2}(Y,\mathbb{Z}_{\ell(-1)})",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"H^{\bullet-2}(Y,\mathbb{Z}_{\ell}(-1))",
    note="Everywhere else Z_ℓ(-1). The TeX keeps the printed position.")

add(page=280,
    where="second composite, label of the second arrow",
    scan="f_*⊕(g_*i*)",
    tex=r"\stackrel{f_*\oplus(g_*i^*)}{\longrightarrow}",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\stackrel{f_*\oplus(-g_*i^*)}{\longrightarrow}",
    note="The next line takes the second component as -g_*i*k_*, as ?' and (4.3.3) on p. 277 do; with g_*(g*(x) c_1(N)) = -x (4.3.2) the inverse of f*+i_*g* is f_* ⊕ (-g_*i*). The label copies (4.2.6)/(4.2.9) of p. 274, which print the same unsigned label (with (4.2.10) = X): correct them together or not at all. The TeX keeps the print.")

add(page=280,
    where="'et de -g_*i*k_* = g_*ℓ_*h* = -h*'",
    scan="-g_*i*k_* = g_*ℓ_*h* = -h* (no minus before the middle term)",
    tex=r"-g_*i^*k_* = g_*\ell_*h^* = -h^*",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"-g_*i^*k_* = -g_*\ell_*h^* = -h^*",
    note="By (5.1.5) i*k_* = ℓ_*h*, and g_*ℓ_* = id, so the middle term is -g_*ℓ_*h*. The TeX keeps the print.")

add(page=280,
    where="proof of 5.1.6, 'l'image de h* est égale'",
    scan="l'image de h* est égale",
    tex=r"l'image de $h^*$ est égale",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"l'image de $k^*$ est égale",
    note="Corollaire 5.1.6 concerns the image of k*, which by (5.1.2) is the sum of the images of m* and of h_* (= that of h_* j*). The TeX keeps h*.")

add(page=280,
    where="last composite, label of the second arrow",
    scan="—h*→ H^i(Y,Z_ℓ) (star raised)",
    tex=r"\stackrel{h^*}{\longrightarrow} H^i(Y,\mathbb{Z}_{\ell})",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\stackrel{h_*}{\longrightarrow} H^i(Y,\mathbb{Z}_{\ell})",
    note="H^{i-2}(Δ, Z_ℓ(-1)) → H^i(Y, Z_ℓ) is the Gysin map h_*, as in (5.1.2). Goes with 'l'image de h*' → k*. The TeX keeps h*.")

for f in F:
    if f['kind'] != 'misprint_in_print':
        f.pop('corrected', None)
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
F2 = [{k: f[k] for k in order if k in f} for f in F]
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F2, fh, ensure_ascii=False, indent=1)
print(len(F2), 'findings written')
