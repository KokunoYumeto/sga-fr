import json, sys
out = sys.argv[1]
F = []
def add(**kw):
    F.append(kw)

add(page=441, where="1st paragraph, line 2: 'des fibres epéciales'",
    scan="fibres epéciales (first letter a heavily struck e; checked in a crop)",
    tex=r"fibres epéciales", kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"fibres spéciales",
    note="Typing error of the print (e for s). No s is legible in the overstruck first letter. The TeX keeps the printed reading.")

add(page=441, where="(10.2.7), the formula after the comma",
    scan="φ^t(x,y) = φ^t(x,ξ_t(y))",
    tex=r"\varphi^t(x,y) = \varphi^t(x,\xi_t(y))", kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\varphi^t(x,y) = u_\ell(x,\xi_t(y))",
    note="As printed the definition is circular. ξ_t(y) lies in M'_ℓ, so the right-hand side is the monodromy pairing u_ℓ : M_ℓ ⊗ M'_ℓ → Z_ℓ, as in (10.2.4) (u_ℓ^{A_K}(x,ξ_t(y))) and (10.4.2) (u(x,ξ_t(y))). The bare φ^t on the left is the print's own habit (also in (10.4.2)) and stays. The TeX keeps the printed reading.")

add(page=441, where="paragraph after (10.2.7): 'pour un schéma abélien A_K a réduction semi-stable variable'",
    scan="A_K a réduction (a without grave accent; checked in a crop)",
    tex=r"$A_K$ a réduction", kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"$A_K$ à réduction",
    note="Missing grave accent in the print; the same sentence later prints 'à réduction semi-stable sur (K,S)'. The TeX keeps the printed reading.")

add(page=441, where="'l'accouplement (10.2.7) n'est autre que l'accouplement de monodromie (9.2.1)'",
    scan="(9.2.1)",
    tex=r"monodromie (9.2.1)", kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"monodromie (9.1.2)",
    note="Wrong reference number (transposed digits). The monodromy pairing is (9.1.2) (folio 418) and is cited as (9.1.2) on folios 439 and 444; (9.2.1) is the relation gx - x in V^perp (folio 419). The TeX keeps the printed reading.")

add(page=442, where="last paragraph: 'On peut donc considérer l'accouplement u_ℓ^{A_K} défini par A_{K'}'",
    scan="u_ℓ^{A_K} (no prime on K; checked in a crop)",
    tex=r"$u_\ell^{A_K}$ défini par", kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"$u_\ell^{A_{K'}}$ défini par",
    note="The pairing defined by A_{K'} is u_ℓ^{A_{K'}}, as in the display that follows and in (10.3.5). The print drops the prime; the TeX keeps the printed reading.")

add(page=443, where="1st paragraph: 'jointe à la formule (10.2.3)'",
    scan="(10.2.3) (last digit faint, but a 3)",
    tex=r"la formule (10.2.3)", kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"la formule (10.3.4)",
    note="(10.2.3) is the homomorphism ξ_t : M → M' defined by a polarisation and plays no part here; the factor e(S'/S) in (10.3.5) comes from the inertia formula (10.3.4) g_*(x) = e(S'/S) x. Probably a wrong reference number; the TeX keeps the printed reading. Check before correcting.")

add(page=443, where="1st paragraph: 'montre inmédiatement qu'on a alors'",
    scan="inmédiatement (n then m; checked in a crop against 'immédiatement' on folio 445)",
    tex=r"inmédiatement", kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"immédiatement",
    note="Typing error of the print; the TeX keeps it.")

add(page=444, where="last paragraph: 'Quand à l'accouplement (10.4.1)'",
    scan="Quand à",
    tex=r"Quand à", kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"Quant à",
    note="Spelling error of the print (folio 445 prints 'Quant à b)'). The TeX keeps it.")

add(page=444, where="last paragraph: 'on l'appelera encore'",
    scan="appelera",
    tex=r"appelera", kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"appellera",
    note="Spelling error of the typescript (appeler doubles the l before a mute e), as on folios 161, 171, 283, 331 and 380. The TeX keeps the printed reading.")

add(page=445, where="display after 'qu'il existe un homomorphisme': '... Z_S ⊂ Q_S'",
    scan="Q_S with an ordinary typewriter Q, without the added stroke (checked in a crop); every other Q and Z on the page is double-struck",
    tex=r"\subset \mathbb{Q}_S", kind="misprint_in_print", confidence="medium",
    fix={"old": r"\subset \mathbb{Q}_S", "new": r"\subset Q_S"},
    corrected=r"\subset \mathbb{Q}_S",
    note="The print omits the double stroke of the rational-number Q here; the TeX silently corrects it. The fix restores the printed plain Q.")

add(page=445, where="10.5.2: 'un schéma abélien Ā_K sur k à réduction semi-stable'",
    scan="Ā_K sur k (small k; checked in a crop)",
    tex=r"$\bar{A}_K$ sur $k$", kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"$\bar{A}_K$ sur $K$",
    note="Ā_K is an abelian scheme over the fraction field K (cf. 'A_K un schéma abélien sur K' in 10.4), not over the residue field k. The TeX keeps the printed reading.")

order = ["page","where","scan","tex","kind","confidence","fix","corrected","note"]
F = [{k: f[k] for k in order if k in f} for f in F]
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(F), "findings written")
