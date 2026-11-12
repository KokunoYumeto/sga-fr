import json
import sys

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b006_010"
OUTFILE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_006_010.json"

findings = [
    {
        "page": 6,
        "where": "1.10, second paragraph, last line before (1.10.1)",
        "scan": "un faisceau inversible \u03c9_{X/S} sur S, unique \u00e0 isomorphisme unique pr\u00e8s",
        "tex": r"un faisceau inversible $\omega_{X/S}$ sur $S$, unique",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"un faisceau inversible $\omega_{X/S}$ sur $X$",
        "note": "omega_{X/S} is an invertible sheaf on X: (1.10.1) identifies it with Rf^! O_S[-1], a complex on X, and omega = O(K) with K a divisor on X. The TeX keeps the printed reading.",
    },
    {
        "page": 6,
        "where": "1.10, second paragraph, second line",
        "scan": "il n'est pas fatiguant de d\u00e9finir",
        "tex": "il n'est pas fatiguant de d\u00e9finir",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "fatigant",
        "note": "Spelling slip of the typescript: the adjective is 'fatigant' ('fatiguant' is the participle). The TeX keeps the printed reading.",
    },
    {
        "page": 6,
        "where": "end of the triangle diagram D, X, S (after 'son faisceau conormal :')",
        "scan": "a full stop typed to the right of the diagram, on the baseline of S; the next line starts the new sentence 'On a'",
        "tex": "no full stop; the STRUCTURE comment says it is omitted from the tikzcd",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": r"{} \end{tikzcd}", "new": r"{} \end{tikzcd}\quad ."},
        "note": "The sentence-final full stop belongs after the tikzcd environment, as the TeX does for the displayed formulas ('\\quad .'). Same pattern on page 8.",
    },
    {
        "page": 7,
        "where": "first display, second member",
        "scan": "deg_D (Rg^! O_D) (subscript D, clearly printed)",
        "tex": r"\deg_D\,(Rg^{!}\underline{O}_D)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\deg_D\,(Rg^{!}\underline{O}_S)",
        "note": "g : D -> S, so g^! applies to O_S; page 6 computes chi(Rg^! O_S) and (1.10.2) gives Rg^! O_S = omega|D (x) N^v, which the next member uses. The TeX keeps the printed reading.",
    },
    {
        "page": 7,
        "where": "Proposition 1.11, first line",
        "scan": "quelque soit le diviseur (underlined)",
        "tex": r"\underline{quelque soit le diviseur}",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"\underline{quel que soit le diviseur}",
        "note": "Spelling slip of the typescript ('quel que soit'). The TeX keeps the printed reading.",
    },
    {
        "page": 8,
        "where": "end of the two-row diagram (snake lemma), before 'le diagramme du serpent'",
        "scan": "a comma after the bottom row of the diagram, at the right margin",
        "tex": "no comma; the STRUCTURE comment says it cannot be placed inside the tikzcd body",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\qquad ,"},
        "note": "The sentence continues after the diagram ('..., le diagramme du serpent fournit ...'); the comma belongs after the tikzcd environment. Same pattern on page 6.",
    },
    {
        "page": 8,
        "where": "line 'Par construction ...' after the exact sequence",
        "scan": "deg_E(O(-D) = - (D,E) < 0 (only one closing parenthesis)",
        "tex": r"$\deg_E(\underline{O}(-D) = - (D,E) < 0$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"$\deg_E(\underline{O}(-D)) = - (D,E) < 0$",
        "note": "The parenthesis opened after deg_E is never closed in the print. The TeX keeps the printed reading.",
    },
    {
        "page": 9,
        "where": "paragraph after Th\u00e9or\u00e8me 1.14 ('On appelle un diviseur D ...')",
        "scan": "poss\u00e8dant (grave accent)",
        "tex": "poss\u00e9dant",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "poss\u00e9dant", "new": "poss\u00e8dant"},
        "corrected": "poss\u00e9dant",
        "note": "The accent falls to the right, unlike the acute accents of 'propri\u00e9t\u00e9s' on the same line. The TeX silently corrects the misprint.",
    },
]

ok = True
for f in findings:
    fix = f["fix"]
    if fix is None:
        continue
    path = FOLDER + "\\page_%03d.tex" % f["page"]
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    n = text.count(fix["old"])
    status = "OK" if n == 1 else "BAD"
    if n != 1:
        ok = False
    print(status, f["page"], n, repr(fix["old"]))

# also confirm the quoted 'tex' readings of the fix:null misprints exist on the page
for f in findings:
    if f["fix"] is None:
        path = FOLDER + "\\page_%03d.tex" % f["page"]
        with open(path, encoding="utf-8", newline="") as fh:
            text = fh.read()
        print("tex-present" if f["tex"] in text else "TEX-NOT-FOUND", f["page"], repr(f["tex"]))

if not ok:
    sys.exit("a fix 'old' string is not unique; nothing written")

with open(OUTFILE, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("written", OUTFILE, len(findings))
