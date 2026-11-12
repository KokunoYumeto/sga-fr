import json
import sys

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_161_165.json"

findings = [
    {
        "page": 161,
        "where": "proof of Lemme 4.18.5, second sentence: 'L'espace Ū* à k composantes connexes'",
        "scan": "Ū* à k composantes connexes: grave accent on the a (checked at 2.5x)",
        "tex": "L'espace $\\overline{U}^*$ à $k$ composantes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "L'espace $\\overline{U}^*$ a $k$ composantes",
        "note": "Accent slip: the verb avoir ('a k composantes connexes') is meant. The TeX keeps the printed reading.",
    },
    {
        "page": 161,
        "where": "same sentence: 'composantes connexes, paramétrée par les racines k^ièmes de l'unité'",
        "scan": "paramétrée, no final s (checked at 2x)",
        "tex": "paramétrée par les racines",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "paramétrées par les racines",
        "note": "Agreement slip: the participle refers to the k composantes connexes (one for each k-th root of unity, as the next clause 'sur celle, Ū*_ξ, d'indice ξ' shows); 'L'espace' would need 'paramétré'. The TeX keeps the printed reading.",
    },
    {
        "page": 161,
        "where": "same paragraph: 'coïncide avec l'image réciproque de la fonction ξ : ∏_1^d z_i^{n_i/k} sur U*'",
        "scan": "ξ : ∏ — a typed colon between ξ and the product (checked at 3x)",
        "tex": "$\\xi : \\prod_1^d z_i^{n_i/k}$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$\\xi \\cdot \\prod_1^d z_i^{n_i/k}$",
        "note": "Product, not a colon: on Ū* one has (z^{1/k})^k = f = (∏ z_i^{n_i/k})^k, so z^{1/k}/∏ z_i^{n_i/k} is a locally constant k-th root of unity, and the component of index ξ is where z^{1/k} = ξ·∏ z_i^{n_i/k}. The typescript writes products with a dot (p. 160: '(log f)^p/p! . (j^m_* Ω^n_{X*}(V))_o'); read as the French division sign the colon would give ξ/∏, which is wrong. The TeX keeps the printed reading.",
    },
    {
        "page": 161,
        "where": "proof of Lemme 4.18.5: 'Si Ker(φ) agit non trivialement sur V , les deux membres de 4.18.4 sont nuls'",
        "scan": "les deux membres de 4.18.4 sont nuls",
        "tex": "les deux membres de 4.18.4 sont nuls",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "les deux membres de 4.18.5 sont nuls",
        "note": "Wrong reference number: the paragraph proves Lemme 4.18.5 (4.18.4 was settled on the previous page, 'ce qui vérifie 4.18.4'). If Ker(φ) = π_1(Ū*_ξ) acts nontrivially on V, it acts nontrivially on every V ⊗ V_β (V_β comes from D*), so both members of 4.18.5, ⊕ H*(U*, V⊗V_β)/η H*(U*, V⊗V_β) and H*(Ū*, V), vanish; the next sentence's reduction to V = ℂ by V ↦ V ⊗ V_β is also a reduction for 4.18.5. The TeX keeps the printed reading.",
    },
    {
        "page": 161,
        "where": "display after 'On a alors en cohomologie complexe': first factor H^o(Ū*)",
        "scan": "H^o(Ū*): a small superscript o, the typescript's index zero, the same glyph as in H^o(U*, V_β) and H^o(Ū*, ℂ) of the last display (checked at 2x)",
        "tex": "H^O(\\overline{U}^*)",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "H^O(", "new": "H^0("},
        "note": "The TeX has a capital letter O, which renders as a capital italic O; the print has the small o that stands for zero (H^0 of the components of Ū*). The last display of the page has H^0 for the same glyph.",
    },
    {
        "page": 162,
        "where": "diagram after 'on trouve un diagramme commutatif', top-row arrow from ⊕_β H*Ψ^mu(...) to H*Ψ^m(Ω*_{X*}(V))_o",
        "scan": "leftward arrow: ~ above the shaft, 4.12 below it",
        "tex": "\\arrow[l, \"\\sim\", \"4.12\"']",
        "kind": "other",
        "confidence": "medium",
        "fix": {"old": "\"\\sim\", \"4.12\"']", "new": "\"\\sim\"', \"4.12\"]"},
        "note": "Placement only. Compiled: for a leftward arrow tikz-cd sets an unmarked label BELOW the shaft and a label with the swap mark ' ABOVE it, so the TeX prints 4.12 above and ~ below, the reverse of the print and of the file's own STRUCTURE comment ('\\sim (tilde) printed ABOVE the shaft, label 4.12 printed BELOW'). The new code reproduces the print (p. 141 already writes the leftward ~ as \"\\sim\"').",
    },
    {
        "page": 162,
        "where": "same diagram, top-row arrow from ⊕_β H*(U*,V⊗V_β)/η H*(U*,V⊗V_β)) to ⊕_β H*Ψ^mu(...)",
        "scan": "leftward arrow: ~ above the shaft, 4.18.4 below it",
        "tex": "\\arrow[l, \"\\sim\", \"4.18.4\"']",
        "kind": "other",
        "confidence": "medium",
        "fix": {"old": "\"\\sim\", \"4.18.4\"']", "new": "\"\\sim\"', \"4.18.4\"]"},
        "note": "Placement only, as for the 4.12 arrow (compiled): the TeX sets 4.18.4 above and ~ below the leftward shaft.",
    },
    {
        "page": 162,
        "where": "same diagram, bottom arrow from H*(Ū*, V) to H* RΨ(V)_o",
        "scan": "long leftward arrow with ~ above the middle of the shaft (checked at 1.5x)",
        "tex": "\\arrow[ll, \"\\sim\"]",
        "kind": "other",
        "confidence": "medium",
        "fix": {"old": "\\arrow[ll, \"\\sim\"]", "new": "\\arrow[ll, \"\\sim\"']"},
        "note": "Placement only (compiled): without the swap mark the ~ of a leftward arrow sits below the shaft; the print and the STRUCTURE comment have it above.",
    },
    {
        "page": 162,
        "where": "4.19, second paragraph: 'le sous-faisceau de j_* j* F formé des sections méromorphe, si f est l'équation de X_o'",
        "scan": "méromorphe, — no final s (checked at 2.5x)",
        "tex": "formé des sections méromorphe,",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "formé des sections méromorphes,",
        "note": "Agreement slip (plural 'sections'). The TeX keeps the printed reading.",
    },
    {
        "page": 163,
        "where": "first paragraph (proof of 4.19.2): 'Les noyaux et conoyaux de F → u_* u* F , et les R^i u_*F (i > 0) sont nuls en dehors de X_o'",
        "scan": "R^i u_*F — no u* between u_* and F (checked at 3x)",
        "tex": "et les $R^i u_* F$ $(i > 0)$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "et les $R^i u_* u^* F$ $(i > 0)$",
        "note": "Missing u*: F is a sheaf on X and u : Y → X, so R^i u_* applies to u*F; the sentence before names the coherent sheaves R^i u_* u* F (Grauert), and these vanish off X_o because u is an isomorphism over X*, which with the passage to the limit (4.19.1) gives R^i u_*(u* F)^m = 0 of 4.19.2. The TeX keeps the printed reading.",
    },
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# check: every fix's old occurs exactly once in its page file
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b161_165\page_{:03d}.tex"
ok = True
for f in findings:
    with open(base.format(f["page"]), encoding="utf-8", newline="") as fh:
        text = fh.read()
    if f["fix"] is not None:
        n = text.count(f["fix"]["old"])
        if n != 1:
            ok = False
        print(f["page"], "fix old count:", n)
    # the tex field of misprints should also be found on the page
    t = f["tex"]
    if f["kind"] == "misprint_in_print":
        n = text.count(t)
        print(f["page"], "misprint tex count:", n)
        if n != 1:
            ok = False
print("ALL OK" if ok else "PROBLEM")
sys.exit(0 if ok else 1)
