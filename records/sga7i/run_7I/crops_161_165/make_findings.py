import json
import os

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b161_165"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_161_165.json"

F = []

# ---------------- page 161 ----------------
F.append({
    "page": 161,
    "where": "first line after (2.2.3)",
    "scan": "qu'on appelera par abus de langage",
    "tex": "qu'on appelera",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "qu'on appellera",
    "note": "Spelling error of the typescript (appeler doubles the l before a mute e: appellera). The TeX keeps the printed reading.",
})
F.append({
    "page": 161,
    "where": "first paragraph, end of the sentence 'on note qu'elles sont caractérisées ...'",
    "scan": "pour les deux lois de compositions φ et ψ.",
    "tex": "lois de compositions",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": "lois de composition",
    "note": "Plural 'compositions' is a slip; the same paragraph later prints 'les deux lois de composition'. The TeX keeps the printed reading.",
})
F.append({
    "page": 161,
    "where": "first paragraph, sentence 'Appliquant alors (2.1.1.2) ...'",
    "scan": "on trouve que des deux membres sont égaux respectivement à e et e'",
    "tex": "on trouve que des deux membres",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "on trouve que les deux membres",
    "note": "'des' is a typing error for 'les' (the two sides of (2.1.1.2) applied to e,e',e',e). The TeX keeps the printed reading.",
})
F.append({
    "page": 161,
    "where": "paragraph 'Notons également ...', first sentence",
    "scan": "une structure d'extension de Q par G sur l'image inverse de 1_P×Q dans G.",
    "tex": "de $1_{P}\\times Q$ dans $G$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "de $1_{P}\\times Q$ dans $E$",
    "note": "The inverse image of 1_P×Q is taken in the biextension E, which lies over P×Q, not in G. The TeX keeps the printed reading.",
})

# ---------------- page 163 ----------------
F.append({
    "page": 163,
    "where": "formula (2.3.4), second factor",
    "scan": "BIEXT(T̲) → GRAB(T̲) × GRAB̲(T) ,  (the underline is under GRAB, not under T)",
    "tex": "\\underline{\\mathrm{GRAB}}(T)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "\\mathrm{GRAB}(\\underline{T})",
    "note": "The typist underlined GRAB instead of the topos T; everywhere else the print has GRAB(T̲). The TeX keeps the printed reading.",
})
F.append({
    "page": 163,
    "where": "sentence after (2.3.3), 'celle des Groupes abéliens sur T.'",
    "scan": "des Groupes abéliens sur T.  (T not underlined)",
    "tex": "Groupes abéliens sur $T$",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": "Groupes abéliens sur $\\underline{T}$",
    "note": "The topos is T̲ elsewhere in the same sentence ('sur T̲', 'GRAB(T̲)'); the underline is missing here. The TeX keeps the printed reading.",
})
F.append({
    "page": 163,
    "where": "heading 2.4",
    "scan": "2.4. La catégorie BIEXT(P,Q,G)  pour P,Q,G variables. Je dis que le foncteur ...  (heading runs into the text on the same line)",
    "tex": "\\underline{variables}.\n\nJe dis que",
    "kind": "other",
    "confidence": "low",
    "fix": {"old": "\\underline{variables}.\n\nJe dis que", "new": "\\underline{variables}. Je dis que"},
    "note": "The print runs the heading into the paragraph; the TeX starts a new paragraph after the heading. Same at 2.5 on page 165; 2.3 on page 162 is run in, as printed.",
})
F.append({
    "page": 163,
    "where": "2.4, first sentence",
    "scan": "le foncteur canonique (2.3.4) en fibrant, et le foncteur canonique (2.3.5) est cofibrant",
    "tex": "\\underline{en fibrant}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "\\underline{est fibrant}",
    "note": "'en' is a typing error for 'est' (parallel to 'est cofibrant'; the next sentence speaks of 'La première assertion'). The TeX keeps the printed reading.",
})
F.append({
    "page": 163,
    "where": "2.4, explanation of the second assertion",
    "scan": "pour une biextension E de (P,G) par G",
    "tex": "biextension $E$ de $(P,G)$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "biextension $E$ de $(P,Q)$",
    "note": "A biextension of (P,Q) by G is meant. The TeX keeps the printed reading.",
})

# ---------------- page 164 ----------------
F.append({
    "page": 164,
    "where": "line after (2.4.1)",
    "scan": "la catégorie des biextensions de (P;Q) par G",
    "tex": "$(P;Q)$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "$(P,Q)$",
    "note": "Semicolon typed for the comma (the two share a key on the typewriter). The TeX keeps the printed reading.",
})
F.append({
    "page": 164,
    "where": "formula (2.4.2), left side",
    "scan": "BIEXT(P,G;G×G') → BIEXT(P,Q;G) × BIEXT(P,Q;G')",
    "tex": "\\mathrm{BIEXT}(P,G;G\\times G')",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "\\mathrm{BIEXT}(P,Q;G\\times G')",
    "note": "P,Q are fixed and only G varies; the left side is BIEXT(P,Q;G×G'). The TeX keeps the printed reading.",
})

# ---------------- page 165 ----------------
F.append({
    "page": 165,
    "where": "end of Remarque 2.4.3",
    "scan": "(produit tensoriel pris dans une catégorie dérivée)..",
    "tex": "dérivée)..",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "dérivée).",
    "note": "Doubled full stop. The TeX keeps the printed reading.",
})
F.append({
    "page": 165,
    "where": "heading 2.5",
    "scan": "2.5. Structure de la catégorie BIEXT(P,Q;G)   Les considérations générales ...  (heading runs into the text on the same line, no full stop)",
    "tex": "BIEXT$(P,Q;G)$\n\nLes considérations",
    "kind": "other",
    "confidence": "low",
    "fix": {"old": "BIEXT$(P,Q;G)$\n\nLes considérations", "new": "BIEXT$(P,Q;G)$ Les considérations"},
    "note": "The print runs the heading into the paragraph; the TeX starts a new paragraph after the heading. Same case as 2.4 on page 163.",
})
F.append({
    "page": 165,
    "where": "2.5.1, 'quand on interprète E et E', soient comme ... soit comme ...'",
    "scan": "quand on interprète E et E', soient comme des extensions de Groupes de Q_P par G_P, soit comme des extensions",
    "tex": "$E'$, soient comme",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "$E'$, soit comme",
    "note": "The correlative 'soit ... soit' is invariable; 'soient' is a typing error. The TeX keeps the printed reading.",
})

# ---------------- checks ----------------
ok = True
for f in F:
    p = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
    with open(p, encoding="utf-8", newline="") as fh:
        t = fh.read()
    assert "\r\n" not in t
    nt = t.count(f["tex"])
    if nt < 1:
        ok = False
        print("TEX NOT FOUND", f["page"], repr(f["tex"]))
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = t.count(old)
        if n != 1:
            ok = False
            print("OLD COUNT", n, f["page"], repr(old))
        if "%%%%%%%%%%" in old:
            ok = False
            print("OLD CROSSES MARKER", f["page"])
        # applying the fix must change the text
        if old == f["fix"]["new"]:
            ok = False
            print("NO-OP FIX", f["page"])
    else:
        # misprint kept: corrected reading should apply to a unique tex substring
        if f["kind"] == "misprint_in_print" and nt != 1:
            ok = False
            print("TEX NOT UNIQUE FOR MISPRINT", nt, f["page"], repr(f["tex"]))
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        print("NO CORRECTED", f["page"])
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        ok = False
        print("CORRECTED ON NON-MISPRINT", f["page"])

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# re-read and validate the written JSON
with open(OUT, encoding="utf-8") as fh:
    back = json.load(fh)
print("written", len(back), "findings; checks", "OK" if ok else "FAILED")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in back)
for pg in (161, 162, 163, 164, 165):
    print(pg, "normal", c[(pg, False)], "misprint", c[(pg, True)])
