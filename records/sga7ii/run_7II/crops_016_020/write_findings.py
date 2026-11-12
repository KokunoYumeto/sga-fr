import json
import os
import sys

B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b016_020"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_016_020.json"

findings = [
    {
        "page": 17,
        "where": "2.8, last sentence ('en effet, les transformés ... de D sont isomorphes à D')",
        "scan": "les transformés pur D' de D ('pur' without s)",
        "tex": r"les transformés purs $D'$ de $D$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": r"transformés purs $D'$", "new": r"transformés pur $D'$"},
        "corrected": r"transformés purs $D'$",
        "note": "Agreement slip of the typescript. At the typewriter pitch (about 19.5 px per character) exactly one space slot separates 'pur' from D', so no s was typed or lost to the scan. The TeX silently corrects the misprint.",
    },
    {
        "page": 18,
        "where": "proof of Lemme 2.9.1, sentence 'Par construction, le conoyau de la flèche de O_E dans f_* O_E est fini'",
        "scan": "f_* O_E: the second subscript is a plain E with no prime (same width as the first O_E; nothing between it and 'est')",
        "tex": r"dans $f_* \underline{O}_E$ est fini",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"dans $f_* \underline{O}_{E'}$ est fini",
        "note": "f_* applies to a sheaf on S', and the arrow meant is O_E -> f_* O_{E'}: its finite cokernel gives chi(O_D (x) f_* O_{E'}) = chi(O_D (x) O_E) in the next display, which prints O_{E'} with a visible prime. The TeX keeps the printed reading.",
    },
    {
        "page": 18,
        "where": "(2.9.2), first line, coefficient of s*",
        "scan": "(D' + μ(S) s*,E') with the subscript s typed on the line below μ, i.e. μ_s(S)",
        "tex": r"\mu_s(S)\, s^*",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\mu_s(D)\, s^*",
        "note": "By (2.6.3) and 2.7 the total transform is D* = D' + μ_s(D) s* (as in (2.11.1)), and the second line of (2.9.2) continues with μ_s(D)(s*,E'). The TeX keeps the printed reading.",
    },
    {
        "page": 19,
        "where": "(2.11.3), left-hand side",
        "scan": "(s*,D) with no prime on D",
        "tex": r"(s^*,D) \;=\;",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"(s^*,D') \;=\;",
        "note": "The sentence before applies formula 2.9 to the divisors s* and D' of S_1, and assertion (i) for t = s is deduced by combining (2.11.3) with (2.11.2), which reads μ_s(D) = (s*,D').[k(s):k]^{-1}. D is a divisor on S, so (s*,D) is not defined. The TeX keeps the printed reading.",
    },
    {
        "page": 20,
        "where": "last display, the exact sequence after 'et'",
        "scan": "0 → f_*O_{D'}/O_D → f_*O_E → f_* O_{D'∩E} → 0 .",
        "tex": r"0 \longrightarrow f_*\underline{O}_{D'}/\underline{O}_D \longrightarrow f_*\underline{O}_E \longrightarrow f_*\ \underline{O}_{D'\cap E} \longrightarrow 0",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"0 \longrightarrow f_*\underline{O}_E \longrightarrow f_*\ \underline{O}_{D'\cap E} \longrightarrow f_*\underline{O}_{D'}/\underline{O}_D \longrightarrow 0",
        "note": "The author's slip in the mathematics: the three terms are in the wrong order. The sequence before it, 0 -> O_D -> f_*O_{D'} (+) f_*O_E -> f_*O_{D'∩E} -> 0, makes O_D the fibre product. So f_*O_E -> f_*O_{D'∩E} is injective with cokernel f_*O_{D'}/O_D. Check on a node (μ_s(D) = 2, k(s) = k): the lengths are 3 for f_*O_E by (2.11.6), 4 for f_*O_{D'∩E} by (2.11.8) and δ = 1 for f_*O_{D'}/O_D. The printed order has alternating sum 1 - 3 + 4 = 2, so it cannot be exact; the corrected order gives 3 - 4 + 1 = 0. (2.11.9) on page 21 follows the printed order, writing χ(f_*O_{D'}/O_D) = ½μ_s(D)(μ_s(D)+1)[k(s):k] - μ_s(D)²[k(s):k]. It reaches the right value ½μ_s(D)(μ_s(D)-1)[k(s):k] only through a sign slip, since ½μ(μ+1) - μ² = -½μ(μ-1). A corrected edition must change both: the first line of (2.11.9) becomes μ_s(D)²[k(s):k] - ½μ_s(D)(μ_s(D)+1)[k(s):k]. The TeX keeps the printed reading.",
    },
]

ok = True
for f in findings:
    path = os.path.join(B, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    marker = [ln for ln in text.split("\n") if ln.startswith("%%%%")]
    if f["fix"] is not None:
        n = text.count(f["fix"]["old"])
        print(f["page"], "fix.old count", n, repr(f["fix"]["old"]))
        if n != 1 or any(f["fix"]["old"] in m for m in marker):
            ok = False
    n2 = text.count(f["tex"])
    print(f["page"], "tex count", n2, repr(f["tex"]))
    if n2 != 1:
        ok = False

if not ok:
    print("CHECK FAILED; not writing")
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", OUT, len(findings), "findings")
