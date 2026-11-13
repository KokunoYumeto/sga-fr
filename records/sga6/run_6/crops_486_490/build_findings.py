"""Build findings_486_490.json and check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b486_490"
OUT = RUN / "findings_486_490.json"

M490 = "%%%%%%%%%%  scan idx 503  |  folio 490  %%%%%%%%%%"
M486 = "%%%%%%%%%%  scan idx 499  |  folio 486  %%%%%%%%%%"

F = []

# ---------------- p. 486 ----------------
F.append({
    "page": 486,
    "where": "statements of pp. 486-490: Proposition 3.7 and Lemme 3.8 (p. 486), Propositions 4.2, 4.3 and 4.4 (p. 489)",
    "scan": ("underlined word group by word group (both scans): Prop. 3.7 'Quels que soient', 'on a'; Lemme 3.8 'Soient', "
             "'et', 'deux morphismes v\u00e9rifiant les', 'hypoth\u00e8ses de', 'Alors', 'les v\u00e9rifie \u00e9galement', 'Si', "
             "'est un \u00e9l\u00e9ment de', 'et si', 'est v\u00e9rifi\u00e9 par', 'pour l'\u00e9l\u00e9ment', 'et par', "
             "'pour l'\u00e9l\u00e9ment', 'alors il est v\u00e9rifi\u00e9 par', 'pour l'\u00e9l\u00e9ment'; Prop. 4.2 'Le morphisme', "
             "'est projectif', 'd'intersection compl\u00e8te', 'et de dimension relative virtuelle nulle', 'On a de plus la relation'; "
             "Prop. 4.3 'Pour tout', 'on a la relation', 'o\u00f9', 'd\u00e9signe la', '-i\u00e8me classe de Chern'; Prop. 4.4 'Soit', "
             "'un sch\u00e9ma quasi-compact', 'Si', 'est un faisceau localement libre de type fini sur', 'de classe', 'dans', "
             "'et de rang', 'on a'; formulas, letters (except the sheaf E of Prop. 4.4, entry of p. 489) and punctuation plain; "
             "the labels underline only the word"),
    "tex": "the statements in roman (no \\underline, no \\emph); the Expos\u00e9 VIII TeX has no \\underline at all",
    "kind": "underline",
    "confidence": "high",
    "fix": None,
    "note": ("Expos\u00e9 VIII follows the Expos\u00e9 II pattern of GLOBAL_ISSUES 82 (pending volume decision): not itemized. "
             "No emphasized defined terms and no category letter on pp. 486-490."),
})

F.append({
    "page": 486,
    "where": "above the folio-486 marker (end of page_485.tex): '\\subsection*{Suite de la d\u00e9monstration du th\u00e9or\u00e8me 3.6}'",
    "scan": ("no heading: p. 485 ends with 'est commutatif.' and the rest of the page is blank; p. 486 begins under the running "
             "head directly with the indented 'La d\u00e9monstration du th\u00e9or\u00e8me 3.6 occupera la fin de cet expos\u00e9.' "
             "(both scans; b481_485/page_485_s4.png, crops_486_490/wit_485_half.png, wit_486_half.png)"),
    "tex": "\\subsection*{Suite de la d\u00e9monstration du th\u00e9or\u00e8me 3.6} between 'est commutatif.' and the folio-486 marker",
    "kind": "extra",
    "confidence": "high",
    "fix": None,
    "note": ("A heading the print does not have. It stands above the marker, so there is no fix in page_486.tex. Exact edit in "
             "main.tex, both layers (diplomatic about line 12444, current about line 12450 on 13 Nov; main.tex is being edited, "
             "so use the string): replace 'est commutatif.\\n\\n\\n\\n\\subsection*{Suite de la d\u00e9monstration du th\u00e9or\u00e8me 3.6}"
             "\\n\\n" + M486 + "\\n' by 'est commutatif.\\n\\n" + M486 + "\\n' (old string once per layer; simulated in memory: "
             "crops_486_490/sim_markers.py). The checker of p. 485 may report the same."),
})

F.append({
    "page": 486,
    "where": "after the display of Proposition 3.7, 'Par additivit\u00e9, on peut supposer x et y homog\u00e8nes'",
    "scan": ("'Par additivit\u00e9' starts at the left margin right after the display, as 'D'apr\u00e8s 3.2' and 'et :' on this page "
             "(the print runs on); the typescript indents its new paragraphs, also after displays ('La d\u00e9monstration', "
             "'Par hypoth\u00e8se', 'En combinant') (both scans)"),
    "tex": "blank line (new paragraph) before 'Par additivit\u00e9'",
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": "\\]\n\nPar additivit\u00e9", "new": "\\]\nPar additivit\u00e9"},
    "note": ("Paragraph break the print does not have (as findings_281_285, p. 281). It is the start of the proof of 3.7; the "
             "other proofs on pp. 486-490 begin with an indented paragraph."),
})

F.append({
    "page": 486,
    "where": "after (3.8.2), 'En combinant (3.8.1) et (3.8.2), on obtient :'",
    "scan": "indented: a new paragraph after the display (3.8.2) (both scans)",
    "tex": "runs on after \\end{equation} (no blank line)",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "\\end{equation}\nEn combinant", "new": "\\end{equation}\n\nEn combinant"},
    "note": "Paragraph break missing in the TeX.",
})

# ---------------- p. 487 ----------------
F.append({
    "page": 487,
    "where": "3.9, second paragraph 'En outre, on peut supposer que l'immersion i satisfait la condition de VII 4.1.'",
    "scan": ("after '... et dans le cas du morphisme structural : P^r_Y \u2192 Y.' a new line, indented: 'En outre' begins a "
             "new paragraph (both scans)"),
    "tex": "'En outre, ...' in the same paragraph as 3.9 (no blank line)",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "Y$.\nEn outre", "new": "Y$.\n\nEn outre"},
    "note": "Paragraph break missing in the TeX.",
})

F.append({
    "page": 487,
    "where": ("P of the projective spaces: p. 487 3.9 'P^r_Y \u2192 Y', 'la section de P^2_{P^r_Y}', "
              "'P^2_{P^r_Y} \u2192 P^r_Y et P^r_Y \u2192 Y' (7 P); p. 488 ii) 'P^r_Y \u2192 Y' (1 P)"),
    "scan": "a typed P doubly underlined in all 8 places (both scans), the same mark as the doubly underlined S, D, G of Expos\u00e9 VI",
    "tex": "\\mathbb P (double-struck) in all 8 places",
    "kind": "font",
    "confidence": "low",
    "fix": None,
    "note": ("Convention of the Expos\u00e9 VIII transcription, reported once: the exposé writes this P as \\mathbb P (13 in "
             "main.tex), while Expos\u00e9 VI \u00a7\u00a71-2 and Expos\u00e9 VII write the doubly underlined P as \\mathbf P "
             "(\\bfP) and VI \u00a7\u00a73-4 as \\mathbb P (findings_396_400 p. 397, findings_426_430). One decision for the volume; if "
             "bold: '\\mathbb P' -> '\\mathbf P' (7 places on p. 487, 1 on p. 488). Three examples: '$\\mathbb P^r_Y\\longrightarrow Y$' "
             "-> '$\\mathbf P^r_Y\\longrightarrow Y$' (p. 487); '\\(\\mathbb P^2_{\\mathbb P^r_Y}\\) introduite' -> "
             "'\\(\\mathbf P^2_{\\mathbf P^r_Y}\\) introduite' (p. 487); '\\(\\mathbb P^r_Y\\to Y\\)' -> '\\(\\mathbf P^r_Y\\to Y\\)' "
             "(p. 488). Low: a double-struck P may be kept for the doubly underlined P."),
})

# ---------------- p. 489 ----------------
F.append({
    "page": 489,
    "where": "after the display of Proposition 4.2, 'La premi\u00e8re assertion d\u00e9coule imm\u00e9diatement de (VII 1.8).'",
    "scan": "indented: a new paragraph after the display (both scans)",
    "tex": "runs on after \\] (no blank line)",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "\\]\nLa premi\u00e8re assertion", "new": "\\]\n\nLa premi\u00e8re assertion"},
    "note": "Paragraph break missing in the TeX. Independent of the next entry.",
})

F.append({
    "page": 489,
    "where": "'(VII 1.8). La deuxi\u00e8me relation est cons\u00e9quence de la relation :'",
    "scan": ("'La premi\u00e8re assertion ... (VII 1.8).' fills one line alone; 'La deuxi\u00e8me relation ...' begins the next line, "
             "indented like it: two paragraphs (both scans)"),
    "tex": "both sentences in one paragraph",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "(VII 1.8). La deuxi\u00e8me", "new": "(VII 1.8).\n\nLa deuxi\u00e8me"},
    "note": "Paragraph break missing in the TeX.",
})

F.append({
    "page": 489,
    "where": "'Cette relation est contenue dans VII 4.8, car elle n'est autre que v^gr\u2218u^gr = 0.'",
    "scan": ("the formula is part of the text line: it stands on the next line at the left margin, at the normal line spacing, "
             "with its full stop right after the 0 ('v^gr\u2218u^gr  =  0.'); the displays of the page are centred (both scans)"),
    "tex": "a display \\[ v^{\\mathrm{gr}}\\circ u^{\\mathrm{gr}}=0 . \\]",
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": "autre que\n\\[\n v^{\\mathrm{gr}}\\circ u^{\\mathrm{gr}}=0 .\n\\]",
            "new": "autre que \\(v^{\\mathrm{gr}}\\circ u^{\\mathrm{gr}}=0\\)."},
    "note": "In-text formula set as a display.",
})

F.append({
    "page": 489,
    "where": "Proposition 4.4, 'Si E est un faisceau localement libre de type fini sur X, de classe E dans K\u02d9(X)'",
    "scan": ("the first E (the sheaf) has its own short underline, separate from those of 'Si' and 'est un faisceau lo-'; "
             "the second E (its class, 'de classe E dans') is plain (both scans; crops_486_490/w489_E.png)"),
    "tex": "\\(E\\) plain in both places",
    "kind": "underline",
    "confidence": "high",
    "fix": {"old": "Si \\(E\\) est un faisceau", "new": "Si \\(\\underline{E}\\) est un faisceau"},
    "note": ("The print distinguishes the sheaf E (underlined) from its class E; the TeX merges them. The Expos\u00e9 VIII TeX has "
             "no \\underline at all, so this is the convention reported for the sheaf letters of Expos\u00e9 VII "
             "(findings_431_435); itemized here because pp. 486-490 have only these two places (p. 485 has the same underlined "
             "E, p. 491 J, F, N, O: for those batches)."),
})

F.append({
    "page": 489,
    "where": "proof of 4.4, 'en passant au fibr\u00e9 en drapeaux de E, supposer que E est somme de classes'",
    "scan": "the E of 'drapeaux de E' (the sheaf) underlined; the E of 'supposer que E est somme' (the class) plain (both scans)",
    "tex": "\\(E\\) plain in both places",
    "kind": "underline",
    "confidence": "high",
    "fix": {"old": "drapeaux de \\(E\\),", "new": "drapeaux de \\(\\underline{E}\\),"},
    "note": "As the entry before (the flag bundle of the sheaf).",
})

# ---------------- p. 490 ----------------
F.append({
    "page": 490,
    "where": "start of page (folio-490 marker)",
    "scan": ("p. 489 ends '... et se ramener \u00e0 montrer la formule pour un faisceau inversible. Soit'; p. 490 begins "
             "'\u03be la classe d'un tel faisceau. On a alors :' (both scans; crops_486_490/wit_489_half.png, wit_490_half.png)"),
    "tex": "page_489.tex ends 'Soit \\(\\xi\\) la' above the folio-490 marker; page_490.tex begins 'classe d'un tel faisceau.'",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": ("Page 490 really begins at '\\(\\xi\\) la'. Exact edit in main.tex, both layers (diplomatic about lines 12574-12576, "
             "current about 12580-12582 on 13 Nov; use the string): replace 'faisceau inversible. Soit \\(\\xi\\) la\\n" + M490 +
             "\\nclasse d'un tel faisceau.' by 'faisceau inversible. Soit\\n" + M490 + "\\n\\(\\xi\\) la classe d'un tel "
             "faisceau.' (old string once per layer; simulated in memory: crops_486_490/sim_markers.py). The sentence runs on, "
             "so no blank line."),
})

F.append({
    "page": 490,
    "where": "after the display ch(\u03bb_{-1}(\u03be)) = 1 - exp(c^1(\u03be)), 'Par ailleurs, \u03be est d'augmentation 1 ;'",
    "scan": "indented: a new paragraph after the display (both scans)",
    "tex": "runs on after \\] (no blank line)",
    "kind": "other",
    "confidence": "high",
    "fix": {"old": "\\]\nPar ailleurs", "new": "\\]\n\nPar ailleurs"},
    "note": "Paragraph break missing in the TeX.",
})

F.append({
    "page": 490,
    "where": "last display, after 'soit, d'apr\u00e8s VII 3.4 :', right member 'j_gr(ch(g^*(y)). Todd(g^*(\u0164_i)).c^{d-1}(F\u030c))'",
    "scan": "ch(g^*(y)) (both scans; crops_486_490/w490_lastdisp.png); the left member has g^*(x)",
    "tex": "\\ch(g^*(y))",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "\\ch(g^*(x))",
    "note": ("The right member comes from g^gr(ch(x).Todd(\u0164_i)) of the display before (g^gr(ch(x)) = ch(g^*(x))), and the "
             "left member is ch(j_*(g^*(x).\u03bb_{-1}(F))); p. 491 goes on with ch(g^*(x).\u03bb_{-1}(F)). The TeX keeps the "
             "printed reading; the current layer also still reads \\ch(g^*(y))."),
})

# ---------------- checks ----------------
ok = True
for f in F:
    fx = f.get("fix")
    if not fx:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
    print(f["page"], n, repr(fx["old"][:50]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("   marker line in fix!")
# no two fixes on a page may overlap
for p in sorted({f["page"] for f in F}):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = sorted((t.find(f["fix"]["old"]), t.find(f["fix"]["old"]) + len(f["fix"]["old"]))
                   for f in F if f["page"] == p and f.get("fix"))
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("overlap on page", p, a, b)
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
print({p: (c[(p, False)], c[(p, True)]) for p in range(486, 491)})
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "ok" if ok else "PROBLEM")
