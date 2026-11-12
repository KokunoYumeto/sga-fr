import json
import sys
from pathlib import Path

RUN = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
PAGES = RUN / "b396_400"
OUT = RUN / "findings_396_400_recheck.json"

findings = [
    {
        "page": 396,
        "where": "Théorème 5.6, '(jusqu'ici, on peut donc prendre N = 2 [1])'",
        "scan": "the opening parenthesis stands before the underline, which starts under the j of 'jusqu'ici'",
        "tex": "\\underline{(jusqu'ici, on peut donc prendre}",
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": "\\underline{(jusqu'ici,", "new": "(\\underline{jusqu'ici,"},
        "note": "The print leaves the parenthesis out of the underline.",
    },
    {
        "page": 396,
        "where": "proof, 'pour i = 0, j_*(j^*G) ne différe de G que sur Z'",
        "scan": "ne différe de",
        "tex": "ne différe de",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "ne diffère de",
        "note": "Acute accent on the first e and none on the second, for 'diffère'. The TeX keeps the printed reading.",
    },
    {
        "page": 396,
        "where": "proof, 'pour le faisceau j^*G et les morphisme j et f j'",
        "scan": "les morphisme j et f j",
        "tex": "les morphisme $j$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "les morphismes $j$",
        "note": "Plural s missing after 'les'. The TeX keeps the printed reading.",
    },
    {
        "page": 397,
        "where": "'Il reste donc à traiter le cas où les hypothèses suivantes sont vérifiées. :'",
        "scan": "vérifiées. :",
        "tex": "vérifiées. :",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "vérifiées :",
        "note": "Stray full stop before the colon that introduces (*). The TeX keeps the printed reading.",
    },
    {
        "page": 398,
        "where": "Lemme 5.6.2 (i), 'les faisceaux i^{o*}Rj_{1*}G sont constant tordus'",
        "scan": "sont constant tordus",
        "tex": "sont constant tordus",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "sont constants tordus",
        "note": "Agreement s missing on 'constant' (plural subject 'les faisceaux'; 'tordus' agrees). The TeX keeps the printed reading.",
    },
    {
        "page": 399,
        "where": "proof of 5.6.1, 'd'après 6.2 (i) et l'hypothèse de récurrence'",
        "scan": "d'après 6.2 (i)",
        "tex": "d'après 6.2 (i)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "d'après 5.6.2 (i)",
        "note": "Wrong reference: Exposé XXI has no section 6 (the bibliography follows on p. 400). The step uses the base change isomorphism of Lemme 5.6.2 (i), whose notation the same sentence invokes ('avec les notations de 5.6.2 (i)'). The TeX keeps the printed reading.",
    },
]

inertia_note = (
    "The inertia group is the same handwritten Fraktur capital as on p. 389, where the TeX writes "
    "\\mathfrak{I}_x ('et par \\mathfrak{I}_x le groupe d'inertie'); Fraktur has one form for I and J, "
    "and the letter is the I of inertia (Lemme 5.3.1: 'I le groupe d'inertie'). One reading for both pages: "
    "the four p. 399 edits go together (or p. 389 changes to \\mathfrak{J} instead)."
)
for where, old, new in [
    ("'et J le groupe d'inertie'", "$\\mathfrak{J}$ le groupe", "$\\mathfrak{I}$ le groupe"),
    ("'des isomorphismes de G/J-modules galoisiens'", "\\mathfrak{G}/\\mathfrak{J}", "\\mathfrak{G}/\\mathfrak{I}"),
    ("display (j_*G)_x = G^J", "\\underline{G}^{\\mathfrak{J}}", "\\underline{G}^{\\mathfrak{I}}"),
    ("display (R^1 j_*G)_x = G_J(-1)", "\\underline{G}_{\\mathfrak{J}}(-1)", "\\underline{G}_{\\mathfrak{I}}(-1)"),
]:
    findings.append({
        "page": 399,
        "where": where,
        "scan": "handwritten Fraktur capital for the inertia group (the glyph of p. 389)",
        "tex": old,
        "kind": "symbol",
        "confidence": "low",
        "fix": {"old": old, "new": new},
        "note": inertia_note,
    })

ok = True
for f in findings:
    fx = f["fix"]
    if fx is None:
        # check the tex substring of kept misprints exists exactly once too
        text = (PAGES / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
        n = text.count(f["tex"])
        if n != 1:
            print("tex count", f["page"], repr(f["tex"]), n)
            ok = False
        continue
    text = (PAGES / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    n = text.count(fx["old"])
    if n != 1:
        print("old count", f["page"], repr(fx["old"]), n)
        ok = False
    if "%%%%%%%%%%" in fx["old"]:
        print("marker in old", f["page"])
        ok = False

if not ok:
    sys.exit(1)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", len(findings))
