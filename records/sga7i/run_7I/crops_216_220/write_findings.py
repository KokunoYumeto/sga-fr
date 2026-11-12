"""Write findings_216_220.json and check that every fix 'old' (and every misprint 'tex') occurs exactly once."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
B = RUN / "b216_220"
OUT = RUN / "findings_216_220.json"

F = []

# ---- page 217 -------------------------------------------------------------------------------------------------
F.append({
    "page": 217,
    "where": "Bibliographie [3] (Grothendieck, Sur quelques points d'Algèbre homologique)",
    "scan": "Toh. Math. Journal, vol. 9 (1956), p.119-221",
    "tex": "vol. 9 (1956)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "vol. 9 (1957)",
    "note": "Wrong year: the paper is Tôhoku Math. J. (2) 9 (1957), 119-221 (the second series has one volume a "
            "year from 1949, so volume 9 is 1957). Same reading in the DjVu witness. The TeX keeps the printed "
            "reading; the corrected layer also still reads 1956. 'corrected' replaces the 'tex' substring.",
})
F.append({
    "page": 217,
    "where": "Bibliographie [4] (Grothendieck, Catégories cofibrées additives ...)",
    "scan": "relatif, Lectures Notes in Math. n°79 1968 (Springer).",
    "tex": "Lectures Notes in Math.",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "Lecture Notes in Math.",
    "note": "Typing error of the print: the series is Lecture Notes in Mathematics (the same slip as in the "
            "bibliography of SGA 7 II, Exposé X). The TeX keeps the printed reading; the corrected layer already "
            "reads 'Lecture Notes in Mathematics'. 'corrected' replaces the 'tex' substring.",
})
F.append({
    "page": 217,
    "where": "Bibliographie [6] (Mumford), 'Tata Institute of Fun- / damental Research'",
    "scan": "Fun- | damental: the word is divided at the line end",
    "tex": "Tata Institute of Fun- \\\\\n\\hspace*{4em}damental Research",
    "kind": "other",
    "confidence": "medium",
    "fix": {
        "old": "Fun- \\\\\n\\hspace*{4em}damental",
        "new": "\\\\\n\\hspace*{4em}Fundamental",
    },
    "note": "The TeX reproduces the print's line breaks in the bibliography (\\\\ + \\hspace*{4em}) and so keeps "
            "the line-end hyphen inside the word. The fix joins 'Fundamental' and moves the forced break before "
            "it (layout only).",
})
F.append({
    "page": 217,
    "where": "Bibliographie [6] (Mumford), end of the entry (last line of Exposé VII)",
    "scan": "Research 1968 (à paraître). : a full stop (a dot on the baseline without the descending tail of the "
            "commas on the page, e.g. 'D. Mumford,'); the same dot in the DjVu witness (checked at 4x)",
    "tex": "Research 1968 (à paraître),",
    "kind": "punctuation",
    "confidence": "medium",
    "fix": {
        "old": "Research 1968 (à paraître),",
        "new": "Research 1968 (à paraître).",
    },
    "note": "Entries [1], [2], [4] and [5] also end with a full stop. In the PDF scan the dot has a thin spur "
            "above it but no tail below the baseline; in the DjVu witness it has the size and position of the "
            "full stop of 'D.'.",
})

# ---- page 218 -------------------------------------------------------------------------------------------------
F.append({
    "page": 218,
    "where": "title of Exposé VIII, first line",
    "scan": "COMPLEMENTS SUR LES BIEXTENSIONS. PROPRIETES GENERALES with a double underline (two parallel rules, "
            "checked at 2x); 'E X P O S E VIII', 'par A. Grothendieck' and 'S O M M A I R E' have single ones",
    "tex": "\\underline{COMPLEMENTS SUR LES BIEXTENSIONS. PROPRIETES GENERALES}",
    "kind": "underline",
    "confidence": "high",
    "fix": {
        "old": "\\underline{COMPLEMENTS SUR LES BIEXTENSIONS. PROPRIETES GENERALES}",
        "new": "\\underline{\\underline{COMPLEMENTS SUR LES BIEXTENSIONS. PROPRIETES GENERALES}}",
    },
    "note": "Same encoding as the double-underlined exposé titles fixed earlier (p. 1; p. 133 "
            "\\underline{\\underline{BIEXTENSIONS DE FAISCEAUX DE GROUPES}). Apply together with the second "
            "title line.",
})
F.append({
    "page": 218,
    "where": "title of Exposé VIII, second line",
    "scan": "DES BIEXTENSIONS DES SCHEMAS EN GROUPES with a double underline (two parallel rules, checked at 2x)",
    "tex": "\\underline{DES BIEXTENSIONS DES SCHEMAS EN GROUPES}",
    "kind": "underline",
    "confidence": "high",
    "fix": {
        "old": "\\underline{DES BIEXTENSIONS DES SCHEMAS EN GROUPES}",
        "new": "\\underline{\\underline{DES BIEXTENSIONS DES SCHEMAS EN GROUPES}}",
    },
    "note": "Second line of the same double-underlined title; apply together with the first line.",
})

# ---- page 220 -------------------------------------------------------------------------------------------------
F.append({
    "page": 220,
    "where": "1.1, before (1.1.3): 'les Tor_i(P,Q), qui sont nuls pour i ≥ 1'",
    "scan": "qui sont nuls pour i ≥ 1 :",
    "tex": "qui sont nuls pour $i \\geqslant 1$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "qui sont nuls pour $i \\geqslant 2$",
    "note": "Tor_1(P,Q) is not zero in general and is a term of (1.1.3) itself; the Tor_i of abelian sheaves "
            "vanish for i ≥ 2, which is what the exact sequence (1.1.3) uses. Same reading in the DjVu witness. "
            "The TeX keeps the printed reading. The corrected layer rewrites the sentence without the vanishing "
            "statement ('par la troncation standard de ...'), so it does not contain the 'tex' substring. "
            "'corrected' replaces the 'tex' substring.",
})
F.append({
    "page": 220,
    "where": "(1.1.4), first line, between Hom(P,Ext^1(Q,G)) and the second line",
    "scan": "the first line ends with Hom(P,Ext^1(Q,G)) and the second line begins with Ext^2(P,Hom(Q,P)): no "
            "arrow between them (blank margin after the first line in the PDF scan and in the DjVu witness)",
    "tex": "\\mathrm{Hom}(P,\\underline{\\mathrm{Ext}}^1(Q,G)) \\\\",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "\\mathrm{Hom}(P,\\underline{\\mathrm{Ext}}^1(Q,G)) \\longrightarrow \\\\",
    "note": "The 'suite exacte à 5 termes' of the spectral sequence Ext^p(P,Ext^q(Q,G)) => Ext^{p+q}(P,RHom(Q,G)) "
            "needs the map Hom(P,Ext^1(Q,G)) -> Ext^2(P,Hom(Q,G)) (compare the arrow that ends the first line of "
            "(1.1.3)). The TeX keeps the printed reading; the corrected layer also has no arrow here. "
            "'corrected' replaces the 'tex' substring.",
})
F.append({
    "page": 220,
    "where": "(1.1.4), second line, first term",
    "scan": "Ext^2(P,Hom(Q,P)) --> Ext^2(P,RHom(Q,G))  ,",
    "tex": "\\mathrm{Ext}^2(P,\\underline{\\mathrm{Hom}}(Q,P))",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "\\mathrm{Ext}^2(P,\\underline{\\mathrm{Hom}}(Q,G))",
    "note": "P typed for G: the fourth term of the five-term sequence is E_2^{2,0} = Ext^2(P,Hom(Q,G)) (the first "
            "is Ext^1(P,Hom(Q,G))). Same in the DjVu witness. The TeX keeps the printed reading; the corrected "
            "layer already reads (Q,G). 'corrected' replaces the 'tex' substring.",
})

# ---- checks ---------------------------------------------------------------------------------------------------
ok = True
for f in F:
    t = (B / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, f["page"], repr(f["fix"]["old"]))
        if "%%%%%%%%%%" in f["fix"]["old"] or "%%%%%%%%%%" in f["fix"]["new"]:
            ok = False
            print("MARKER IN FIX", f["page"])
    n = t.count(f["tex"])
    if n != 1:
        print("note: tex substring count", n, f["page"], repr(f["tex"]))
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            ok = False
            print("MISSING corrected", f["page"])
    elif "corrected" in f:
        ok = False
        print("corrected on non-misprint", f["page"])

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT, len(F), "findings; checks", "OK" if ok else "FAILED")
for p in (216, 217, 218, 219, 220):
    norm = sum(1 for f in F if f["page"] == p and f["kind"] != "misprint_in_print")
    mis = sum(1 for f in F if f["page"] == p and f["kind"] == "misprint_in_print")
    print(p, f"{norm}/{mis}")
