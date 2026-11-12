import json, sys

B = chr(92)   # backslash
NL = chr(10)  # LF

base = sys.argv[1]
out = sys.argv[2]

def ul(s):
    return B + "underline{" + s + "}"

F = []
F.append({
 "page": 271,
 "where": "Corollaire 4.8, second line of the statement",
 "scan": "B (nécessairement lisse et connexe) with the underline under the words only; it starts after '(' and stops before ')'",
 "tex": ul("(nécessairement lisse et connexe)"),
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": ul("(nécessairement lisse et connexe)"),
         "new": "(" + ul("nécessairement lisse et connexe") + ")"},
 "note": "Parentheses outside the underline in the typescript."
})
F.append({
 "page": 271,
 "where": "display after 'Alors le foncteur de catégories rigides'",
 "scan": "BIEXT(A,B,G_m) --> BIEXT(P,Q;G_m): comma before G_m in the source",
 "tex": B + "mathrm{BIEXT}(A,B," + ul("G") + "_m)",
 "kind": "misprint_in_print",
 "confidence": "low",
 "fix": None,
 "corrected": B + "mathrm{BIEXT}(A,B;" + ul("G") + "_m)",
 "note": "Typing slip: semicolon before the coefficient group everywhere else (target BIEXT(P,Q;G_m), (4.8.1) Biext^1(A,B;G_m)). The TeX keeps the printed comma."
})
F.append({
 "page": 271,
 "where": "statement of Corollaire 4.8, line before (4.8.1)",
 "scan": "elle donne naissanee",
 "tex": ul("elle donne naissanee"),
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "naissance",
 "note": "Typing error of the print (e for c); the TeX keeps the printed reading."
})
F.append({
 "page": 271,
 "where": "after (4.8.1)",
 "scan": "'Compte tenu de (4.7.1), il reste à prouver ...' begins a new indented paragraph (indented like 'En effet' on p. 272)",
 "tex": B + "end{equation}" + NL + "Compte tenu de (4.7.1)",
 "kind": "other",
 "confidence": "medium",
 "fix": {"old": B + "end{equation}" + NL + "Compte tenu",
         "new": B + "end{equation}" + NL + NL + "Compte tenu"},
 "note": "Without a blank line LaTeX continues the paragraph of the display; the print starts the proof as a new paragraph."
})
F.append({
 "page": 271,
 "where": "proof of 4.8, 'Cela se déduit comme (4.7.1)'",
 "scan": "CeIa (capital I, serifs on both sides at cap height, for the l)",
 "tex": "CeIa se déduit",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "Cela",
 "note": "Typing error of the print (I for l); the TeX keeps the printed reading."
})
F.append({
 "page": 274,
 "where": "end of the first paragraph, 'donc l'annulateur à gauche de l'accouplement (1.11.1)'",
 "scan": "(1.11.1)",
 "tex": "l'accouplement (1.11.1)",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "(4.11.1)",
 "note": "Wrong reference number of the print: the pairing meant is (4.11.1) (cf. 'En particulier, ... l'accouplement (4.11.1)' just after). The TeX keeps the printed reading."
})
F.append({
 "page": 274,
 "where": "paragraph 'En particulier', 'séparant à gauche i.e, que C' = 0'",
 "scan": "i.e, que (comma after the e: same size and descending tail as the comma after '0,' on the same line)",
 "tex": "gauche i.e. que $C' = 0$",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": {"old": "gauche i.e. que", "new": "gauche i.e, que"},
 "corrected": "i.e. que",
 "note": "The typescript types a comma for the abbreviation's final full stop; the TeX silently corrects it. Restore the printed comma in the diplomatic text."
})

ok = True
for f in F:
    src = open(base + "/page_" + str(f["page"]) + ".tex", encoding="utf-8").read()
    if f["fix"] is None:
        n = src.count(f["tex"])
        print(f["page"], "fix=null; tex excerpt count:", n, repr(f["tex"]))
        if n < 1:
            ok = False
        continue
    old = f["fix"]["old"]
    n = src.count(old)
    print(f["page"], repr(old), "count:", n)
    if n != 1 or "%%%%%%%%%%" in old:
        ok = False
print("ALL OK" if ok else "PROBLEM")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", len(F))
