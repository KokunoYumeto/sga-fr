# -*- coding: utf-8 -*-
import json, os, sys
from collections import Counter

BATCH = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b056_060"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_056_060.json"

F = []

F.append({
    "page": 56,
    "where": "Proof of Lemma 2.8, third condition, '(such that P(g) : R' → R' ×_k k[Ker f] is given by r' → (r', r'(0)) ⇔ there exists an arrow'",
    "scan": "r' → (r', r'(0)) ⇔ : only two closing parentheses; the '(such that' opened before P(g) at the end of the preceding line is never closed",
    "tex": r"""r' \to (r',\ r'(0))""",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"""r' \to (r',\ r'(0)))""",
    "note": "Missing closing parenthesis of the clause '(such that P(g) ...'; the parallel clauses for P(ρ), P(h) and P(γ) in the same proof are closed (the last one by 'r'(0))'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 57,
    "where": "Proposition 2.9(b), 'there exists α : a' → a in Â and a Ĉ_Λ-isomorphism ρ : φ̂(a') ⥲ b''",
    "scan": "a hat over the underlined C of 'C_Λ-isomorphism' (like the hats over Â and φ̂(a') on the same line; clear in a crop)",
    "tex": r"""$\underline{C}_{\Lambda}$\underline{-isomorphism}""",
    "kind": "symbol",
    "confidence": "high",
    "fix": {
        "old": r"""$\underline{C}_{\Lambda}$\underline{-isomorphism}""",
        "new": r"""$\widehat{\underline{C}}_{\Lambda}$\underline{-isomorphism}""",
    },
    "note": r"""The TeX drops the hat. The 'C_Λ-isomorphism' in the proof of (a) on the same page and on p. 59 has no hat in the print and stays as it is. \widehat{\underline{C}} is the file's own form (\widehat{\underline{C}}_\wedge in § 1).""",
})

F.append({
    "page": 57,
    "where": "Proof of 2.9(a), 'Since the composite functor φ ∘ ψ is smooth, there exists an arrow a' → a in A'",
    "scan": "φ ∘ ψ (the composition circle printed solid)",
    "tex": r"""$\varphi \circ \psi$""",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"""$\psi \circ \varphi$""",
    "note": "The composite functor A → C of 2.9(a) is ψ ∘ φ (statement on p. 56 and the first line of this proof); φ ∘ ψ is not defined. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 57,
    "where": "Proof of 2.9(a), 'and hence (f̃)_*(b'') = 0 be the hypothesis (ii).'",
    "scan": "be the hypothesis (ii)",
    "tex": "be the hypothesis (ii)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "by the hypothesis (ii)",
    "note": "Typing error for 'by'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 58,
    "where": "Diagram of solid and dotted arrows, vertical arrow b'_{n+1} → φ(a_{n+1})",
    "scan": "label β_{n+1} typed to the RIGHT of the downward arrow (inside the square); β_n is typed to the LEFT of its own arrow",
    "tex": r"""\ar[d, "\beta_{n+1}"']""",
    "kind": "other",
    "confidence": "low",
    "fix": {
        "old": r"""\ar[d, "\beta_{n+1}"']""",
        "new": r"""\ar[d, "\beta_{n+1}"]""",
    },
    "note": "The swap mark ' sets the label to the left of a downward arrow; without it tikz-cd sets it to the right, as printed (the file's comment block also records β_{n+1} to the right). The swap mark on β_n is correct: the print has β_n to the left of its arrow, although the comment block says right.",
})

F.append({
    "page": 58,
    "where": "'Now A is, by hypotheses, semi-homogeneous and α_n : a'_n → a_n is surjective'",
    "scan": "α_n : a'_n → a_n (no prime on α, a prime on the source a'_n; checked in a crop)",
    "tex": r"""$\alpha_{n} : a_{n}' \to a_{n}$""",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"""$\alpha_{n} : a_{n+1} \to a_{n}$""",
    "note": "In the diagrams just above and just below, α_n : a_{n+1} → a_n and α'_n : a'_n → a_n; the printed map joins the name of one to the source of the other. The surjectivity that the semi-homogeneity of A needs here is that of α_n : a_{n+1} → a_n, one of the hypotheses of the preceding paragraph ('in which α_n , β_n , β_{n+1} , β'_n are surjective'); the other possible reading is α'_n : a'_n → a_n (prime dropped from α). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 59,
    "where": "Diagram after 'We then obtain the commutative diagram', arrow φ(a'_n) → b'_n",
    "scan": "the hand-drawn ~ lies BELOW the shaft (on the side towards φ(a_n)), not above it",
    "tex": r"""\arrow[dl, "\sim"']""",
    "kind": "other",
    "confidence": "low",
    "fix": {
        "old": r"""\arrow[dl, "\sim"']""",
        "new": r"""\arrow[dl, "\sim"]""",
    },
    "note": "For an arrow running down-left the swap mark ' sets the label above-left of the shaft; without it tikz-cd sets it below-right, as printed. The file's comment block says 'above the shaft'; the scan shows it below.",
})

F.append({
    "page": 59,
    "where": "Same diagram, bottom-left node 'φ(a_{n+1}'",
    "scan": "φ(a_{n+1} with no closing parenthesis",
    "tex": r"""\varphi(a_{n+1} \arrow[r]""",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"""\varphi(a_{n+1}) \arrow[r]""",
    "note": "Closing parenthesis missing in the print (the same node is φ(a_{n+1}) in the diagrams of p. 58); the file's comment block records it. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 59,
    "where": "Corollary 2.10(b), 'then for any map α : η → ξ in Â , P(ξ) is a formal power-series ring over P(η)'",
    "scan": "Â with its hat but without underline (the A of 'objects of A' in the line above and B̂ in (a) are underlined; checked in a crop)",
    "tex": r"""$\hat{A}$""",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"""$\underline{\hat{A}}$""",
    "note": r"""Category letter without its underline (cf. 'in B̂' in (a), written \underline{\hat{B}} in the file). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.""",
})

F.append({
    "page": 60,
    "where": "'A \"cocartegory in C\" is a diagram'",
    "scan": "cocartegory",
    "tex": "cocartegory",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "cocategory",
    "note": "Spelling slip; the same page goes on 'If (R_0, R_1, s_1, s_2, ε, c) is a cocategory in C'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

F.append({
    "page": 60,
    "where": "Diagram defining a cocategory, arrow h_{R_1} ×_{h_{R_0}} h_{R_1} → h_{R_1}",
    "scan": "the arrow carries no label",
    "tex": r"""h_{R_1} \times_{h_{R_0}} h_{R_1} \arrow[r] &""",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": r"""h_{R_1} \times_{h_{R_0}} h_{R_1} \arrow[r, "c"] &""",
    "note": "This arrow is the composition c of (i), (ii) and of 'the composition rule of arrows is given by c : h_{R_1} ×_{h_{R_0}} h_{R_1} → h_{R_1}' below; unlabelled, c is never introduced. Low: an omitted label rather than a wrong character. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
})

# ---- checks ----
ok = True
for f in F:
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    n_tex = txt.count(f["tex"])
    if n_tex != 1:
        print("TEX count", n_tex, "page", f["page"], repr(f["tex"]))
        ok = False
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = txt.count(old)
        if n != 1:
            print("OLD count", n, "page", f["page"], repr(old))
            ok = False
        if "%%%%%%%%%%" in old:
            print("marker in old", f["page"])
            ok = False
        # the edited text must still contain the other findings' tex strings untouched
        new_txt = txt.replace(old, f["fix"]["new"], 1)
        for g in F:
            if g is not f and g["page"] == f["page"] and g["tex"] not in new_txt:
                print("fix on page", f["page"], "destroys tex of another finding", repr(g["tex"]))
                ok = False
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            print("missing corrected", f["page"])
            ok = False
    else:
        if "corrected" in f:
            print("corrected on non-misprint", f["page"])
            ok = False

if not ok:
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", OUT, len(F))
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(56, 61):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
