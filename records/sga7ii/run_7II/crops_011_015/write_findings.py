import json, sys, os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
BATCH = os.path.join(RUN, "b011_015")
OUT = os.path.join(RUN, "findings_011_015.json")

findings = [
    {
        "page": 11,
        "where": "formula (*), the intersection number after the sum",
        "scan": "n_i (D_i D_j): no comma between D_i and D_j",
        "tex": "(D_i, D_j) \\qquad\\qquad .",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "(D_i, D_j) \\qquad\\qquad .", "new": "(D_i\\ D_j) \\qquad\\qquad ."},
        "note": "All three intersection numbers on this page are printed without a comma: in (*), in (**) and in the last sentence before section 2. This is the page's notation, not an isolated slip. The fix leaves the coefficient n_i (see the next finding) untouched."
    },
    {
        "page": 11,
        "where": "formula (*), coefficient inside the sum",
        "scan": "\\sum_{j \\neq i} n_i (D_i D_j): subscript i on the coefficient",
        "tex": "\\sum_{j \\neq i} n_i",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\sum_{j \\neq i} n_j",
        "note": "Wrong index in the print. From (X_s . D_i) = 0 and (D_i . D_i) = -2 one gets 2 n_i = sum over j != i of n_j (D_i . D_j), so the coefficient inside the sum is n_j. The TeX keeps the printed reading."
    },
    {
        "page": 11,
        "where": "condition (**), end ('avec ... \\neq 0')",
        "scan": "(D_{i_k} D_{i_{k+1}}) with no comma",
        "tex": "(D_{i_k}, D_{i_{k+1}})",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "(D_{i_k}, D_{i_{k+1}})", "new": "(D_{i_k}\\ D_{i_{k+1}})"},
        "note": "Same notation as in (*)."
    },
    {
        "page": 11,
        "where": "last sentence before section 2 ('les nombres d'intersection ... sont égaux à zéro ou un')",
        "scan": "(D_iD_j): no comma, the two letters set close together",
        "tex": "$(D_i, D_j)$ sont",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "$(D_i, D_j)$ sont", "new": "$(D_i D_j)$ sont"},
        "note": "Same notation as in (*) and (**)."
    },
    {
        "page": 11,
        "where": "paragraph 'On cherchera alors ...', first line",
        "scan": "toutes les solutions en nombre entiers",
        "tex": "en nombre entiers",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "en nombres entiers",
        "note": "Agreement slip in the typescript. The TeX keeps the printed reading."
    },
    {
        "page": 14,
        "where": "Proposition 2.3, label of the first condition",
        "scan": "(i)",
        "tex": "(1)",
        "kind": "number",
        "confidence": "high",
        "fix": {"old": "(1)\\quad", "new": "(i)\\quad"},
        "note": "At high zoom the glyph shows the dot and the short left serif of the typewriter's i, as in the '(ii)' below it. It lacks the top flag of the 1 (compare '2.1' on the same page). The next condition is labelled (ii)."
    },
    {
        "page": 14,
        "where": "paragraph after the order on S*, end ('(n = #[s*,t])')",
        "scan": "(n = #[s*,t]) with closed brackets on both sides",
        "tex": "($n = \\#[s^*,t]$)",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "($n = \\#\\,]s^*,t]$)",
        "note": "Off by one as printed. s* has order 0 (Proposition 2.3 with n = 0, t_0 = s), and the closed interval [s*,t] has n+1 elements, while the distance from s* to t is n. The suggested reading is the half-open interval ]s*,t]; n+1 = #[s*,t] is the other possibility. This may be the author's slip rather than a typing error. The TeX keeps the printed reading."
    },
    {
        "page": 15,
        "where": "paragraph after Proposition 2.4, first line",
        "scan": "Soient D est un diviseur \u2265 O sur S",
        "tex": "Soient $D$ est un diviseur",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Soient $D$ un diviseur",
        "note": "Superfluous 'est': the sentence mixes 'Soient D un diviseur' and 'Si D est un diviseur'. The TeX keeps the printed reading."
    },
    {
        "page": 15,
        "where": "paragraph after Définition 2.5, last line",
        "scan": "t_n n'est pas proche de t_i pour 0<i\u2264n-1",
        "tex": "pour $0 < i \\leq n-1$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "pour $0 < i < n-1$",
        "note": "As printed the claim fails for i = n-1 when n >= 2. t_n is an immediate successor of t_{n-1}, so by the first sentence of the same paragraph it is proche de t_{n-1}. The bound must exclude n-1. The TeX keeps the printed reading."
    },
]

# check every fix's old occurs exactly once in its page file
ok = True
for f in findings:
    if f["fix"] is None:
        continue
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    n = txt.count(f["fix"]["old"])
    if n != 1:
        ok = False
    print(f["page"], repr(f["fix"]["old"]), "occurrences:", n)
# check tex fields occur in the page files (informational)
for f in findings:
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    t = f["tex"]
    print("tex-field", f["page"], repr(t), "found" if t in txt else "NOT FOUND")

if not ok:
    print("UNIQUENESS CHECK FAILED; not writing")
    sys.exit(1)
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
print("wrote", OUT, len(findings))
