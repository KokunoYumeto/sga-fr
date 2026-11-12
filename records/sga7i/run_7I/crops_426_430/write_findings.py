import json, os
run = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
batch = os.path.join(run, "b426_430")
out = os.path.join(run, "findings_426_430_recheck.json")

F = []
F.append({
 "page": 426,
 "where": "display after 'on voit aussitôt que l'on obtient' (before 'grâce à la formule d'associativité (9.3.7)')",
 "scan": "c_{X_1}(Y') = c_X(Y) - cl(H')  (no prime on the Y of the right-hand side)",
 "tex": "c_{X_1}(Y') \;=\; c_X(Y) - \mathrm{cl}(H')",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "c_X(Y')",
 "note": "The print drops the prime: the class c_X is taken of the element Y' throughout. The TeX keeps the printed reading c_X(Y)."
})
F.append({
 "page": 427,
 "where": "'Pour ceci, nous appliquons les considérations de9.3, en prenant pour r ...'",
 "scan": "de9.3 (no space between 'de' and '9.3')",
 "tex": "de9.3",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "de 9.3",
 "note": "Typing error of the print (missing word space). The TeX keeps the printed reading."
})
F.append({
 "page": 428,
 "where": "Lemme 9.4.3, formula c), sign between H^i(S,D(H) and H^i(η,D(H)_η)",
 "scan": "= (a typed equals sign: same width and shape as the typed '=' before 0 on the same line and in 'H = H_oS'; its lower bar is partly faint)",
 "tex": "\simeq",
 "kind": "symbol",
 "confidence": "medium",
 "fix": {"old": "H^i(S,D(H) \simeq H^i(\eta", "new": "H^i(S,D(H) = H^i(\eta"},
 "note": "The isomorphism signs of a), b), d) and e) are handwritten, a long bar with a tilde over it, more than twice as wide; this sign is the narrow typewriter '='. The parallel formula H^i(S,G_m) = H^i(η,G_m) = 0 further down also uses '='."
})
F.append({
 "page": 428,
 "where": "Lemme 9.4.3, formula c), first term",
 "scan": "H^i(S,D(H)  (closing parenthesis missing)",
 "tex": "H^i(S,D(H) \simeq",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "H^i(S,D(H))",
 "note": "Unbalanced parenthesis in the print; the TeX keeps the printed reading. (The sign after it is a separate finding, listed first.)"
})
F.append({
 "page": 428,
 "where": "Lemme 9.4.3, formula d), second isomorphism: H^1(η,D(H_η)) ≃ G_m(η) ⊗ H_o = K*⊗Ȟ_o",
 "scan": "G_m(η) ⊗ H_o  (no ∨ over this H; the three other H_o of d) carry the handwritten ∨)",
 "tex": "G_m(\eta) \otimes H_o",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "G_m(\eta) \otimes \check{H}_o",
 "note": "The handwritten check is left out on this H_o (no trace of it on the scan); the formula requires Ȟ_o, as in the first isomorphism of d) and in K*⊗Ȟ_o. The TeX keeps the printed reading."
})
F.append({
 "page": 428,
 "where": "'et alors la auite exacte de cohomologie associée à la suite exacte de Kummer'",
 "scan": "la auite exacte",
 "tex": "la auite exacte",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "la suite exacte",
 "note": "Typing error 'auite' for 'suite'; the TeX keeps the printed reading. The small stroke above 'exacte' on the scan is a stray mark."
})
F.append({
 "page": 429,
 "where": "composite after 'en prenant le composé', second term",
 "scan": "H^1(U ,μ_m) ⊗ Ȟ^o  (the o set as a superscript beside the ∨)",
 "tex": "H^1(U ,\mu_m) \otimes \check{H}^o",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "\check{H}_o",
 "note": "Index o raised to an exponent in the print (everywhere else Ȟ_o); the TeX keeps the printed reading."
})
F.append({
 "page": 429,
 "where": "composite after 'en prenant le composé', last term",
 "scan": "H^1(U, D(H_oS))",
 "tex": "H^1(U, D(H_{oS}))",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "D(H_{oU})",
 "note": "The composite describes (9.4.3.1), whose target is H^1(U,D(H_oU)) over an arbitrary base U; the print's index S is a slip for U. The TeX keeps the printed reading."
})
F.append({
 "page": 429,
 "where": "Corollaire 9.4.4, formula e)",
 "scan": "Im H^1(S,D(H)  (closing parenthesis missing)",
 "tex": "\mathrm{Im}\, H^1(S,D(H) \quad \simeq",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "H^1(S,D(H))",
 "note": "Unbalanced parenthesis in the print; the TeX keeps the printed reading."
})

# check every fix's old occurs exactly once on its page
ok = True
for f in F:
    if f["fix"] is None:
        continue
    p = os.path.join(batch, "page_%03d.tex" % f["page"])
    txt = open(p, encoding="utf-8").read()
    n = txt.count(f["fix"]["old"])
    print(f["page"], repr(f["fix"]["old"]), "count =", n)
    if n != 1:
        ok = False
# check tex quotes exist on page (informational)
for f in F:
    p = os.path.join(batch, "page_%03d.tex" % f["page"])
    txt = open(p, encoding="utf-8").read()
    print(f["page"], "tex-present" if f["tex"] in txt else "tex-NOT-literal", repr(f["tex"]))
with open(out, "w", encoding="utf-8") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", out, "ok" if ok else "PROBLEM")
