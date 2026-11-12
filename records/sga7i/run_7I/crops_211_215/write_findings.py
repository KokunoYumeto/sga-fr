import json
import sys

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b211_215"
OUTFILE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_211_215.json"

findings = [
    {
        "page": 211,
        "where": "first line, end of the sentence begun on p. 210: 'l'homomorphisme cobord de la théorie des catégories cofibrées exactes à gauches sur C = GRAB(T)°'",
        "scan": "à gauches, with s (checked in a crop)",
        "tex": "\\underline{cofibrées exactes à gauches sur}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{cofibrées exactes à gauche sur}",
        "note": "The locution 'à gauche' is invariable: p. 210 prints 'catégorie cofibrée exacte à gauche (3.3.6)' and this page 'L'exactitude à gauche annoncée'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 211,
        "where": "end of the second paragraph: 'la suite exacte (3.7.5.2) donne une suite exacte de complexe de chaînes'",
        "scan": "de complexe de chaînes, singular (checked in a crop)",
        "tex": "suite exacte de complexe de chaînes",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "suite exacte de complexes de chaînes",
        "note": "Agreement slip: (3.7.6.1) is an exact sequence of three chain complexes, and the next sentence calls it 'cette suite exacte de complexes'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 211,
        "where": "end of display (3.7.6.1), followed by 'L'exactitude à gauche annoncée résulte alors de 3.4.8 ...'",
        "scan": "the display ends with a comma (checked in a crop); the next line begins a new sentence with a capital L",
        "tex": "P'' \\otimes L.(Q) \\longrightarrow 0 \\quad ,",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "P'' \\otimes L.(Q) \\longrightarrow 0 \\quad .",
        "note": "The sentence 'Ceci posé, la suite exacte (3.7.5.2) donne une suite exacte ...' ends with the display; 'L'exactitude à gauche annoncée résulte alors de 3.4.8 ...' is a new sentence, so the comma is a slip for a full stop. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 212,
        "where": "end of display (3.8.1), followed by 'Nous nous proposons de décrire ...'",
        "scan": "no punctuation after the second sequence '0 → M_1 → M_o → Q → 0' (checked in a crop up to the right margin); the next line begins a new sentence with a capital N",
        "tex": "M_o \\xrightarrow{\\ v\\ } Q \\longrightarrow 0",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "M_o \\xrightarrow{\\ v\\ } Q \\longrightarrow 0 \\quad .",
        "note": "Full stop omitted at the end of the sentence 'Considérons d'abord deux suites exactes de Groupes abéliens (3.8.1)'; the other displays of pp. 211-215 that end a sentence carry the typed full stop ((3.8.7), (3.8.10), (3.8.11)). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 212,
        "where": "diagram (3.8.2)",
        "scan": "a comma printed on the bottom row, to the right of L_o×M_o (the sentence continues 'et satisfaisant la condition d'additivité ...')",
        "tex": "\\end{tikzcd} with no comma (only the STRUCTURE comment mentions it)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "\\end{tikzcd}", "new": "\\end{tikzcd}\\quad ,"},
        "note": "Punctuation printed after a diagram and left out by the TeX. Placed after the tikzcd as in the earlier diagram fixes of this volume (e.g. p. 199).",
    },
    {
        "page": 213,
        "where": "second line: 'coïncident sur L_1⊗M_1, i.e qu'on a'",
        "scan": "i.e with a full stop between i and e only (checked in a crop)",
        "tex": "i.e qu'on a",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "i.e. qu'on a",
        "note": "Abbreviation full stop missing in the typescript; the same page prints '(i.e. le noyau', p. 212 'i.e. telles qu'il existe', p. 215 'i.e. une trivialisation'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 213,
        "where": "end of display (3.8.4), followed by 'pour des sections x_1,y_1 de L_1 , M_1 sur un objet de T.'",
        "scan": "the display ends with a full stop (checked in a crop); the next line continues the sentence with a small p",
        "tex": "g(x_1 \\otimes y_1) \\qquad .",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "g(x_1 \\otimes y_1) \\qquad ,",
        "note": "The clause 'pour des sections x_1,y_1 de L_1 , M_1 sur un objet de T' completes the sentence of (3.8.4), so the full stop is a slip for a comma. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 213,
        "where": "'les autres trivialisations sont les morphismes s': L_o×M_o ⟶ E de la forme'",
        "scan": "the typed product sign between L_o and M_o, the same X-shaped glyph as in 'E_o = L_o×M_o×G' on p. 212 (compared in crops)",
        "tex": "$L_o \\mathrm{X} M_o \\longrightarrow E$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "L_o \\mathrm{X} M_o", "new": "L_o \\times M_o"},
        "note": "The TeX gives the typed product sign as a roman letter X. The same typed glyph is \\times everywhere else (p. 212: 'E_o = L_o \\times M_o \\times G' and 'L_o \\times M_o' in diagram (3.8.2)), as the volume's convention for the typed product sign provides; this is the only \\mathrm{X} in the page files of this run (pp. 1-215).",
    },
    {
        "page": 213,
        "where": "Proposition 3.8.8, first line: 'Le sous-groupe de Biext^1(P,Q;G) formée des classes de'",
        "scan": "the underline stops after 'de'; Biext^1(P,Q;G) is not underlined (checked in a crop)",
        "tex": "\\underline{Le sous-groupe de Biext}$^1(P,Q;G)$",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{Le sous-groupe de Biext}$^1(P,Q;G)$",
            "new": "\\underline{Le sous-groupe de} $\\mathrm{Biext}^1(P,Q;G)$",
        },
        "note": "The TeX extends the underline over 'Biext' and sets Biext as text outside the formula; the fix underlines only 'Le sous-groupe de' and writes \\mathrm{Biext}^1(P,Q;G) as in the second Biext^1 of the same proposition.",
    },
    {
        "page": 213,
        "where": "Proposition 3.8.8: 'Le sous-groupe de Biext^1(P,Q;G) formée des classes de biextensions'",
        "scan": "formée",
        "tex": "\\underline{formée des classes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{formé des classes",
        "note": "Agreement slip: the participle refers to 'Le sous-groupe' (masculine). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
]

# Verify: every fix 'old' occurs exactly once in its page file; every 'tex' of a
# kept misprint occurs in the page file; no 'old' crosses a marker line.
ok = True
for f in findings:
    path = FOLDER + "\\page_%03d.tex" % f["page"]
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = text.count(old)
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, f["page"], repr(old))
        if "%%%%%%%%%%" in old:
            ok = False
            print("OLD CROSSES MARKER", f["page"], repr(old))
    if f["kind"] == "misprint_in_print":
        if f["fix"] is None:
            t = f["tex"]
            n = text.count(t)
            if n != 1:
                ok = False
                print("MISPRINT TEX COUNT", n, f["page"], repr(t))

with open(OUTFILE, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# Re-read and re-check the written file
with open(OUTFILE, encoding="utf-8") as fh:
    back = json.load(fh)
print("written", len(back), "findings; checks ok =", ok)
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in back)
for p in (211, 212, 213, 214, 215):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
