import json, sys
from pathlib import Path

folder = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b001_005")
outfile = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_001_005.json")

findings = [
    {
        "page": 1,
        "where": "title of the exposé",
        "scan": "INTERSECTIONS SUR LES SURFACES REGULIERES, underlined twice (two parallel rules)",
        "tex": r"\underline{INTERSECTIONS SUR LES SURFACES REGULIERES}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": r"\underline{INTERSECTIONS SUR LES SURFACES REGULIERES}",
            "new": r"\underline{\underline{INTERSECTIONS SUR LES SURFACES REGULIERES}}",
        },
        "note": "The title carries a double underline; the author line 'par P. Deligne' has a single one.",
    },
    {
        "page": 2,
        "where": "Exemple 1.2, third line",
        "scan": "coîncidant (circumflex over the i)",
        "tex": "coïncidant",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "coïncidant", "new": "coîncidant"},
        "corrected": "coïncidant",
        "note": "The accent over the i is a peaked circumflex, not two dots. The TeX silently corrects the misprint.",
    },
    {
        "page": 2,
        "where": "Lemme 1.4, third line",
        "scan": "faisceauxcchérents",
        "tex": "faisceauxcchérents",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "faisceaux cohérents",
        "note": "Typing error in the print (no space; c where o is meant). The TeX keeps the printed reading. The second c has a gap on its right side like the other c's of the page; an o with a lost stroke is less likely.",
    },
    {
        "page": 2,
        "where": "Lemme 1.4, third line, before '-modules'",
        "scan": "O_{ℤ_o}: the O is not underlined and the subscript is the typewriter's double-struck ℤ (two parallel diagonals)",
        "tex": r"$\underline{O}_{Z_o}$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": r"$\underline{O}_{Z_o}$", "new": r"$O_{\mathbb{Z}_o}$"},
        "corrected": r"$\underline{O}_{Z_o}$",
        "note": "Elsewhere in the lemma Z_o is an ordinary Z and the structure sheaf is an underlined O. The TeX silently corrects both.",
    },
    {
        "page": 5,
        "where": "Preuve of 1.7, last line of the displayed computation",
        "scan": "(D_i D_j) with no comma",
        "tex": "(D_i, D_j)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {
            "old": r"a_j)^2\, (D_i, D_j) \;-\; \sum_i",
            "new": r"a_j)^2\, (D_i\ D_j) \;-\; \sum_i",
        },
        "corrected": "(D_i, D_j)",
        "note": "The comma is printed in every other (D_i,D_j) on the page; here the space between D_i and D_j is blank. The TeX silently adds it.",
    },
    {
        "page": 5,
        "where": "Corollaire 1.9, end of the second line",
        "scan": "O_s (underlined O; the subscript is an s, heavily struck, apparently over an a)",
        "tex": r"$\underline{O}_a$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": r"$\underline{O}_a$", "new": r"$\underline{O}_s$"},
        "note": "The subscript has a closed upper loop with a left side and ends at the lower left with no right tail, which no a of this typeface has; it matches an s struck over an a. s is the closed point of Exemple 1.2, so O_s is the local ring meant. Check against another copy if one is available.",
    },
]

ok = True
for f in findings:
    if f["fix"] is None:
        continue
    text = (folder / ("page_%03d.tex" % f["page"])).read_text(encoding="utf-8")
    n = text.count(f["fix"]["old"])
    if n != 1:
        ok = False
    print(f["page"], repr(f["fix"]["old"]), "occurrences:", n)
    if "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False
        print("  touches a marker line")

if not ok:
    print("CHECK FAILED; not writing")
    sys.exit(1)

outfile.write_text(json.dumps(findings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("written", outfile)
