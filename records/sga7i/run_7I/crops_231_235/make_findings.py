import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

FOLDER = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b231_235"
OUT = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_231_235.json"

DIAG_END_OLD = "\\end{tikzcd}\n\\end{equation}"
DIAG_END_NEW = "\\end{tikzcd}\\quad ,\n\\end{equation}"
DIAG_NOTE = ("Punctuation printed after a diagram (NOTE_7I); same form as the applied fixes "
             "on pp. 212 and 230 (\\quad , after the tikzcd).")

findings = [
    # ---------------- page 232 ----------------
    {
        "page": 232,
        "where": "diagram (2.1.11.1) of Lemme 2.1.11, to the right of the bottom node Tor_1(P,Q)",
        "scan": "a comma printed far right on the bottom row of the diagram (also in the DjVu witness); "
                "the sentence continues 'où P_m : ...'",
        "tex": "no comma: the tikzcd ends with {\\underline{\\mathrm{Tor}}_1(P,Q)} & "
               "(the STRUCTURE comment records the comma but leaves it out)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": DIAG_END_OLD, "new": DIAG_END_NEW},
        "note": DIAG_NOTE,
    },
    {
        "page": 232,
        "where": "statement of Lemme 2.1.11 after the diagram: 'On a de même commutativité dans le "
                 "diagramme analogue (2.11.2)'",
        "scan": "(2.11.2) (same in the DjVu witness)",
        "tex": "\\underline{diagramme analogue} (2.11.2)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{diagramme analogue} (2.1.11.2)",
        "note": "Wrong reference number: the lemma is 2.1.11 and its diagram is numbered (2.1.11.1) on this "
                "page, so the analogous diagram is (2.1.11.2). Same slip twice more in this sentence "
                "(next two findings). The TeX keeps the printed reading; the corrected layer already "
                "reads (2.1.11.2). 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 232,
        "where": "same sentence: 'symétrique de (2.11.1)'",
        "scan": "(2.11.1) (same in the DjVu witness)",
        "tex": "\\underline{symétrique de} (2.11.1)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{symétrique de} (2.1.11.1)",
        "note": "Wrong reference number for the diagram (2.1.11.1) printed at the top of the page. The TeX "
                "keeps the printed reading; the corrected layer already reads (2.1.11.1). 'corrected' "
                "replaces the 'tex' substring.",
    },
    {
        "page": 232,
        "where": "same sentence: 'dont les sommets sont les mêmes que ceux de (2.11.1)'",
        "scan": "(2.11.1) (same in the DjVu witness)",
        "tex": "\\underline{sont les mêmes que ceux de} (2.11.1)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{sont les mêmes que ceux de} (2.1.11.1)",
        "note": "As the previous finding. The TeX keeps the printed reading; the corrected layer already "
                "reads (2.1.11.1). 'corrected' replaces the 'tex' substring.",
    },
    # ---------------- page 233 ----------------
    {
        "page": 233,
        "where": "first paragraph: 'Par suite, identifiant le sommetsupérieur de (2.1.11.1) à P/nP'",
        "scan": "'sommet' is retyped squeezed (the two m overlap) and only a narrow gap is left before "
                "'supérieur': 13 px in the IA scan (word space 31 px, letter gaps 3-8 px), 7 px in the "
                "DjVu witness (word space 23 px)",
        "tex": "sommetsupérieur",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "sommet supérieur",
        "note": "The typist's correction of 'sommet' used up most of the word space; treated like "
                "'contractéede' (p. 139): the TeX keeps the run-together reading. The corrected layer "
                "also still reads 'sommetsupérieur'. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 233,
        "where": "diagram (2.1.12.1) of Corollaire 2.1.12, to the right of the bottom-right node "
                 "_nTor_1(P,Q)",
        "scan": "a comma printed to the right of _nTor_1(P,Q) on the bottom row (also in the DjVu "
                "witness); the sentence continues 'où, dans la description des flèches horizontales, ...'",
        "tex": "no comma: the tikzcd ends with {{}_{n}\\underline{\\mathrm{Tor}}_1(P,Q)} "
               "(the STRUCTURE comment records the comma but leaves it out)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": DIAG_END_OLD, "new": DIAG_END_NEW},
        "note": DIAG_NOTE,
    },
    {
        "page": 233,
        "where": "after diagram (2.1.12.1): 'induits par m.id_E (pour E égal respectivement à P,Q'",
        "scan": "the underline starts under the p of 'pour'; the opening parenthesis is not underlined "
                "(IA scan and DjVu witness)",
        "tex": "\\underline{(pour}",
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": "\\underline{(pour}", "new": "(\\underline{pour}"},
        "note": "The parenthesis stands before the underlined word in the print.",
    },
    # ---------------- page 234 ----------------
    {
        "page": 234,
        "where": "diagram (2.1.13.3), to the right of the bottom-right node T_l(Tor_1(Q,P))",
        "scan": "a comma printed to the right of T_l(Tor_1(Q,P)) on the bottom row (also in the DjVu "
                "witness); the sentence continues 'où les flèches horizontales sont les flèches de "
                "symétrie.'",
        "tex": "no comma: the tikzcd ends with T_\\ell(\\underline{\\mathrm{Tor}}_1(Q,P)) "
               "(the STRUCTURE comment records the comma but leaves it out)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": DIAG_END_OLD, "new": DIAG_END_NEW},
        "note": DIAG_NOTE,
    },
    {
        "page": 234,
        "where": "Remarque 2.1.14: '(qui dans le cas traités précédemment se réduisent au même Idéal "
                 "nZ_T de'",
        "scan": "le cas traités (same in the DjVu witness)",
        "tex": "dans le cas traités",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "dans les cas traités",
        "note": "Agreement slip: 'traités' is plural (the cases n treated in 2.1.1-2.1.13). The TeX keeps "
                "the printed reading; the corrected layer also still reads 'le cas traités'. 'corrected' "
                "replaces the 'tex' substring.",
    },
    # ---------------- page 235 ----------------
    {
        "page": 235,
        "where": "diagram (2.1.14.3), to the right of the bottom-right node Hom(a∩b/a.b,Tor_1(Q,P))",
        "scan": "a comma printed to the right of the bottom row (a speck above it, not a semicolon; "
                "a plain comma in the DjVu witness); the sentence continues 'où les flèches "
                "horizontales sont les flèches de symétrie.'",
        "tex": "no comma: the tikzcd ends with the node "
               "{\\underline{\\mathrm{Hom}}(...,\\underline{\\mathrm{Tor}}_1(Q,P))} "
               "(the STRUCTURE comment records the comma but leaves it out)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": DIAG_END_OLD, "new": DIAG_END_NEW},
        "note": DIAG_NOTE,
    },
    {
        "page": 235,
        "where": "last line: 'd'où un isomorphisme injectif fonctoriel en le A-Module T'",
        "scan": "isomorphisme injectif ('injectif fonctoriel' faint but legible; same in the DjVu witness)",
        "tex": "un isomorphisme injectif",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "un homomorphisme injectif",
        "note": "The map Hom(a/a^2,T) -> _aT displayed at the top of p. 236 is induced by the epimorphism "
                "A/a -> a/a^2: it is injective, not an isomorphism in general. 'isomorphisme' is a slip "
                "for 'homomorphisme'. The TeX keeps the printed reading; the corrected layer already "
                "reads 'homomorphisme injectif'. 'corrected' replaces the 'tex' substring.",
    },
]

# ---- checks: every fix 'old' and every misprint 'tex' occurs exactly once on its page ----
ok = True
pages = {}
for p in (231, 232, 233, 234, 235):
    with open(f"{FOLDER}/page_{p}.tex", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read()
    if "\r" in pages[p]:
        print("CR found in page", p)
        ok = False

for f in findings:
    text = pages[f["page"]]
    if f["fix"]:
        n = text.count(f["fix"]["old"])
        print(f["page"], "fix old count", n, repr(f["fix"]["old"][:50]))
        if n != 1:
            ok = False
    if f["kind"] == "misprint_in_print":
        n = text.count(f["tex"])
        print(f["page"], "misprint tex count", n, repr(f["tex"][:50]))
        if n != 1:
            ok = False
    # the fixes must not cross a marker line
    if f["fix"] and "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False

print("ALL OK" if ok else "PROBLEM")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(findings, fh, ensure_ascii=False, indent=1)
    print("written", OUT, len(findings))
