import json, sys

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_196_200.json"
B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b196_200"

findings = [
    {
        "page": 196,
        "where": "(3.4.9.1), second term of the exact sequence",
        "scan": "Ext°(L!A): no comma between L'. and A (checked at 2.5x zoom); the other five terms print the comma: (L''.,A), (L.,A), (L''.,A), (L'.,A), (L.,A)",
        "tex": "\\mathrm{Ext}^o(L'.A)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\mathrm{Ext}^o(L'.,A)",
        "note": "Missing comma between the arguments. The TeX keeps the printed reading."
    },
    {
        "page": 196,
        "where": "end of the first paragraph: 'est équivalente à celle de (X'',α''), objet de Ψ_L. , ce qui prouve'",
        "scan": "Ψ (underlined) with subscript L. only, no double prime (checked at 3x zoom)",
        "tex": "$\\underline{\\Psi}_{L.}$ , ce qui",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$\\underline{\\Psi}_{L''.}$ , ce qui",
        "note": "X'' is an extension of L''_o by A and α'' : L''_1 -> X'' (same paragraph), so (X'',α'') is an object of Ψ_{L''.}, the source of the functor (3.4.8.2) Ψ_{L''.} -> Ψ_{[L. -> L'.]} whose equivalence this sentence concludes. Wrong subscript of the print; the TeX keeps the printed reading."
    },
    {
        "page": 197,
        "where": "'Considérons l'objet (0,ū) de Ψ_[L. → L']'",
        "scan": "subscript [L. → L'] : prime without the dot (checked at 2.5x zoom); p. 196 prints the same category as Ψ_[L. → L'.] and this sentence continues with Ψ_{L'.}",
        "tex": "\\underline{\\Psi}_{[L. \\to L']}",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\underline{\\Psi}_{[L. \\to L'.]}",
        "note": "The dot marking the chain complex L'. is missing in the print. The TeX keeps the printed reading."
    },
    {
        "page": 197,
        "where": "last line: 'Un complexe de chaînes L. de C peut-être interprété comme'",
        "scan": "peut-être, with hyphen (checked at 2x zoom)",
        "tex": "peut-être interprété",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "peut être interprété",
        "note": "The verb phrase 'peut être interprété' (can be interpreted) is meant, not the adverb 'peut-être'. The TeX keeps the printed reading."
    },
    {
        "page": 199,
        "where": "diagram (3.5.1)",
        "scan": "a comma printed at the right margin on the line of the bottom node P",
        "tex": "\\end{tikzcd} with no comma (only the STRUCTURE comment mentions it)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "\\end{tikzcd}", "new": "\\end{tikzcd}\\quad ,"},
        "note": "Punctuation printed after a diagram and left out by the TeX."
    },
    {
        "page": 199,
        "where": "display after 'qu'on a les relations': 'εd_o = 0 , d_1d_o = 0 .'",
        "scan": "d_1d_o = 0 (checked at 2x zoom)",
        "tex": "d_1 d_o = 0",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "d_o d_1 = 0",
        "note": "d_1 : L_2 -> L_1 and d_o : L_1 -> L_o, and composites are written right to left (εd_o in the same display, ud_o = 0 on p. 197), so the relation saying L.(P) is a complex is d_o d_1 = 0; d_1 d_o is not defined. Wrong order of the print; the TeX keeps the printed reading."
    },
    {
        "page": 199,
        "where": "last paragraph: 'les deux relations en questions exprimant respectivement'",
        "scan": "en ques-/tions (hyphenated across the line break)",
        "tex": "en questions",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "en question",
        "note": "The locution 'en question' is invariable. The TeX keeps the printed reading."
    },
    {
        "page": 200,
        "where": "commutative square after 'donnant naissance à un diagramme commutatif'",
        "scan": "a full stop printed to the right of P' on the bottom row",
        "tex": "\\end{tikzcd} with no full stop (only the STRUCTURE comment mentions it)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": "\\end{tikzcd}", "new": "\\end{tikzcd}\\quad ."},
        "note": "Punctuation printed after a diagram and left out by the TeX."
    },
]

ok = True
for f in findings:
    with open(f"{B}\\page_{f['page']:03d}.tex", encoding="utf-8", newline="") as fh:
        t = fh.read()
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        print(f["page"], "fix old count:", n)
        ok &= (n == 1)
    if f["kind"] == "misprint_in_print":
        n = t.count(f["tex"])
        print(f["page"], "misprint tex count:", n)
        ok &= (n == 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# reload check
json.load(open(OUT, encoding="utf-8"))
print("ALL UNIQUE" if ok else "PROBLEM")
