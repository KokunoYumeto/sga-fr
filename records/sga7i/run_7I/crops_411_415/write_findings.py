import json, sys
out = sys.argv[1]
F = []
F.append({
 "page": 411,
 "where": "7.4.7, first sentence: 'sans recours au lemme 5.2.4'",
 "scan": "sans recours au lemme 5.2.4.",
 "tex": "sans recours au lemme 5.2.4.",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "sans recours au lemme 5.2.5.",
 "note": "Wrong reference number. 5.2.4 (p. 373) is the paragraph 'La démonstration de (5.2.1) ...', not a lemma; the lemma is Lemme 5.2.5 (p. 374: if u_o is an isogeny, so is u), which 5.2.4 uses and which 7.4.7 replaces by the same fact for the homomorphism of abelian schemes u : B -> D(B') of (7.4.5). The TeX keeps the printed reading."
})
F.append({
 "page": 411,
 "where": "7.4.7: 'l'accouplement (5.2.3.1)=(7.4.2) s'annule sur les parties toriques'",
 "scan": "l'accouplement (5.2.3.1)=(7.4.2)",
 "tex": "$(5.2.3.1)=(7.4.2)$",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "$(5.2.4.2)=(7.4.2)$",
 "note": "Wrong reference number. (5.2.3.1) (p. 372) is the definition D(G) = Hom(G,T_l(G_m)), not a pairing. The pairing of the fixed parts over S, T_l(A^o)^f x T_l(A'^o)^f -> T_l(G_mS), which (7.4.2) gives for A^o, A'^o and whose toric parts and fibres the sentence discusses, is (5.2.4.2) (p. 373). If the print's 5.2.3/5.2.4 numbers are all one step behind (as 'lemme 5.2.4' for 5.2.5 suggests), the intended number may be (5.2.4.1), the same pairing on the generic fibres. The TeX keeps the printed reading."
})
F.append({
 "page": 413,
 "where": "paragraph after Prop. 7.5, line 1: 'de la formation des W^ab aves les images inverses'",
 "scan": "aves les images inverses",
 "tex": "aves les images",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "avec les images",
 "note": "Typing error for 'avec'. The TeX keeps the printed reading."
})
F.append({
 "page": 414,
 "where": "8.1, before (8.1.2): 'parties essentiellement fixe et essentiellement torique de T_l(A_K) (4.1 et 6.5)'",
 "scan": "(4.1 et 6.5)",
 "tex": "(4.1 et 6.5)",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "(4.1 et 6.3)",
 "note": "Wrong reference number. Exposé IX has no 6.5 (§6 is 6.1-6.4; §7 begins on p. 399). The essentially fixed and essentially toric parts are defined in 4.1 (l != p, (4.1.1)) and 6.3 (l = p, (6.3.1)); Prop. 6.3.3 cites the same definitions as '(4.1.1 et 6.3.1)'. Same dangling '6.5' as in 6.4 on p. 398 (reported there, low). The TeX keeps the printed reading."
})
F.append({
 "page": 414,
 "where": "(8.1.2), first isomorphism",
 "scan": "T_l(A_K^♮) ≃ T_l(A_K)^ef",
 "tex": r"T_{\ell}(A_K^{\natural}) \;\simeq\; T_{\ell}(A_K)^{ef}",
 "kind": "misprint_in_print",
 "confidence": "low",
 "fix": None,
 "corrected": r"T_{\ell}(A_K^{\natural\,o}) \;\simeq\; T_{\ell}(A_K)^{ef}",
 "note": "In the non-semi-stable case 8.1 defines only A_{K,K'}^♮ (depending on K') and its neutral component A_K^♮o; A_K^♮ is not defined, and (8.1.3) is obtained from (8.1.1), which concerns A_K^♮o. Possibly a deliberate shorthand (T_l of A_{K,K'}^♮ and of A_K^♮o coincide). The TeX keeps the printed reading."
})
F.append({
 "page": 415,
 "where": "before (8.1.5): 'on note qu'en vertu de (6.5.2) on a un isomorphisme canonique'",
 "scan": "(6.5.2)",
 "tex": "(6.5.2)",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "(6.3.2)",
 "note": "Wrong reference number: Exposé IX has no (6.5.2). The orthogonality T(A_K)^ef = (T(A'_K)^et)^perp that gives (8.1.5) is (6.3.2) (p. 397, case l = p; for l != p the NB after (4.1.2) on p. 355). Same dangling 6.5 as on p. 414. The TeX keeps the printed reading."
})
F.append({
 "page": 415,
 "where": "(8.1.6), middle term",
 "scan": "A'_K with superscript ♮o: the typed small letter o, as in (8.1.1) on p. 414",
 "tex": r"{A'_K}^{\natural\,\circ}",
 "kind": "symbol",
 "confidence": "medium",
 "fix": {"old": r"{A'_K}^{\natural\,\circ}", "new": r"{A'_K}^{\natural\,o}"},
 "note": r"The neutral-component index is the typed letter o here as everywhere; the TeX writes it o in (8.1.1) (A_K^{\natural\,o}) and throughout Exposé IX, and \circ only here."
})
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(F), "findings written")
