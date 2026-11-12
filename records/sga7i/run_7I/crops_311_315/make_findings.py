import json
import sys

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
OUT = BASE + r"\findings_311_315.json"

findings = [
    {
        "page": 312,
        "where": "BIBLIOGRAPHIE, entry [1]: 'Séminaire Orsay 1967/68, à paraître.'",
        "scan": "parâitre (the circumflex is typed over the second a; the i keeps its dot)",
        "tex": "à paraître.",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "à paraître.", "new": "à parâitre."},
        "corrected": "paraître",
        "note": "The typist put the circumflex on the a instead of the i; entry [2] on the same page prints 'paraître' correctly. The TeX silently corrects the misprint; the fix restores the printed reading.",
    },
    {
        "page": 313,
        "where": "SOMMAIRE, item 1: 'l'accouplement canonique Φ_o × Φ'_o → (Q/ℤ)_k'",
        "scan": "(Q/ℤ)_k with an ordinary typewriter Q beside the double-struck ℤ",
        "tex": "(Q/\\mathbb{Z})_k",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "(\\mathbb{Q}/\\mathbb{Z})_k",
        "note": "The same pairing in the heading of §1 (p. 319) is printed with a double-struck ℚ. The TeX keeps the printed plain Q.",
    },
    {
        "page": 313,
        "where": "SOMMAIRE, item 11: 'relation de dualité, comportement assymptotique'",
        "scan": "assymptotique",
        "tex": "assymptotique",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "asymptotique",
        "note": "Spelling error of the print (double s). The TeX keeps the printed reading.",
    },
    {
        "page": 314,
        "where": "0.1, 'une étude détaillée des phénomènes de monodromie locale pour les H^1 ℓ-adiques'",
        "scan": "the underline ends under 'les'; H^1 at the end of the line is not underlined",
        "tex": "\\underline{phénomènes de monodromie locale pour les $H^1$}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{phénomènes de monodromie locale pour les $H^1$}",
            "new": "\\underline{phénomènes de monodromie locale pour les} $H^1$",
        },
        "note": "The TeX extends the underline over $H^1$. The next underline begins with 'adiques' after the unemphasized 'ℓ-', which the TeX already has.",
    },
    {
        "page": 315,
        "where": "0.2, last text line before the footnote: 'n'utilisant pas la résolution des singula-'",
        "scan": "singula- (line-end hyphen at the foot of the page; the word ends with 'rités' at the top of p. 316, after the footnote (*))",
        "tex": "singula CONT>>",
        "kind": "extra",
        "confidence": "high",
        "fix": {"old": "singula CONT>>", "new": "singula"},
        "note": "'CONT>>' is a transcription marker, not printed text. The master file \\input's expose_IX_body.tex unprocessed, so the marker prints literally. Apply together with p. 316: '<<CONT rités' -> 'rités'. Exposé IX uses this CONT>>/<<CONT pairing for text that continues past a footnote or page break (126 'CONT>>', 124 '<<CONT'). Joining 'singularités' across the footnote and the page marker is a global decision.",
    },
]

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(findings, f, ensure_ascii=False, indent=1)
    f.write("\n")

# Check: every fix's "old" occurs exactly once in its page file.
ok = True
for i, fd in enumerate(findings):
    fx = fd["fix"]
    if fx is None:
        continue
    path = BASE + r"\b311_315\page_%03d.tex" % fd["page"]
    with open(path, encoding="utf-8") as g:
        text = g.read()
    n = text.count(fx["old"])
    print(i, fd["page"], repr(fx["old"]), "count =", n)
    if n != 1:
        ok = False
    if "%%%%%%%%%%" in fx["old"]:
        print("  old crosses a marker line")
        ok = False
print("ALL OK" if ok else "PROBLEM")
sys.exit(0 if ok else 1)
