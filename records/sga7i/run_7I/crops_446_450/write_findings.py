import json, io
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I"
findings = [
 {
  "page": 446,
  "where": "10.5.3, first sentence (end)",
  "scan": "lisse et géométrique connexe X_K sur X.",
  "tex": "sur $X$.",
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": "sur $K$.",
  "note": "X_K is a curve over the field K (its jacobian is Pic^o_{X_K/K}); 'sur X' is a typing error of the print for 'sur K'. The TeX keeps the printed reading."
 },
 {
  "page": 446,
  "where": "10.5.3, first sentence",
  "scan": "d'une courbe propre, lisse et géométrique connexe X_K",
  "tex": "géométrique connexe",
  "kind": "misprint_in_print",
  "confidence": "medium",
  "fix": None,
  "corrected": "géométriquement connexe",
  "note": "The print drops '-ment' from the standard term 'géométriquement connexe'. The TeX keeps the printed reading."
 },
 {
  "page": 448,
  "where": "heading of § 11",
  "scan": "comportement assymptotique",
  "tex": "assymptotique",
  "kind": "misprint_in_print",
  "confidence": "high",
  "fix": None,
  "corrected": "asymptotique",
  "note": "Spelling error of the print (double s). The TeX keeps it."
 },
 {
  "page": 448,
  "where": "11.0, line before (11.0.2)",
  "scan": "équivaut à celle des Φ_o(1), grâce à la formule (typed 1, faint; not the handwritten ℓ used elsewhere on the page)",
  "tex": "$\Phi_o(1)$",
  "kind": "misprint_in_print",
  "confidence": "medium",
  "fix": None,
  "corrected": "$\Phi_o(\ell)$",
  "note": "The typescript has a typed 1 where the handwritten ℓ belongs: the ℓ-primary components Φ_o(ℓ) of (11.0.2) are meant. The glyph is faint; its flag matches the typewriter's 1 (the l of this typeface has a flatter serif). The TeX keeps the printed reading."
 }
]
# verify every quoted tex span and every fix 'old' occurs exactly once on its page
ok = True
for f in findings:
    with io.open(f"{base}/b446_450/page_{f['page']}.tex", encoding="utf-8", newline="") as fh:
        txt = fh.read()
    n = txt.count(f["tex"])
    if n != 1:
        ok = False
        print("tex count", n, f["page"], f["tex"])
    if f["fix"] is not None:
        m = txt.count(f["fix"]["old"])
        if m != 1:
            ok = False
            print("old count", m, f["page"], f["fix"]["old"])
print("all unique:", ok)
with io.open(f"{base}/findings_446_450_recheck.json", "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
