import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

FOLDER = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b206_210"
OUT = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_206_210.json"

findings = [
    {
        "page": 206,
        "where": "3rd line of the page: 'peuvent s'interpréter comme desisomorphismes' (just before the displayed formula)",
        "scan": "desisomorphismes (no space: the typewriter cells run on, the gap between 'des' and 'i' is one letter pitch)",
        "tex": "desisomorphismes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "des isomorphismes",
        "note": "Typing error: missing word space. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 206,
        "where": "line after the displayed formula: 'où π_Q,q_1q_2 sont les trois morphismes'",
        "scan": "π_Q,q_1q_2 (no comma between q_1 and q_2)",
        "tex": "$\\pi_Q,q_1q_2$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$\\pi_Q,q_1,q_2$",
        "note": "Three morphisms are listed, as in the symmetric 'π_P,p_1,p_2' two lines below; the comma between q_1 and q_2 is missing in the print. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 206,
        "where": "same sentence: 'sont les trois morphismes P×Q×Q ⟶ Q déduits respectivement'",
        "scan": "P×Q×Q ⟶ Q",
        "tex": "$P\\times Q\\times Q \\longrightarrow Q$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$P\\times Q\\times Q \\longrightarrow P\\times Q$",
        "note": "π_Q, q_1, q_2 pull back the torsor E on P×Q (π_Q^*(E), q_1^*(E), q_2^*(E) in the formula above), so their target is P×Q; the symmetric maps are printed 'π_P,p_1,p_2: P×P×Q ⟶ P×Q'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 206,
        "where": "'que ψ définit sur E une structure d'extension commutative de P_Q par G_P . Enfin, la condition médiane'",
        "scan": "P_Q par G_P (capital P subscript on G)",
        "tex": "$P_Q$ par $G_P$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$P_Q$ par $G_Q$",
        "note": "Definition 2.1 has 'structure d'extension de P_Q par G_Q, défini par des isomorphismes (2.0.7)'; the parallel statement for φ just before reads 'Q_P par G_P'. The print's G_P is a slip for G_Q. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 208,
        "where": "first paragraph of 3.7: 'le comportement de l'équivalence de catégorie cofibrées 3.6.4'",
        "scan": "catégorie cofibrées",
        "tex": "de catégorie cofibrées",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "de catégories cofibrées",
        "note": "Agreement error (missing s); the same phrase is printed 'l'équivalence de catégories cofibrées 3.6.4' on p. 209 and 'équivalence de catégories cofibrées' on p. 207. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
]

ok = True
for f in findings:
    with open(f"{FOLDER}/page_{f['page']:03d}.tex", encoding="utf-8", newline="") as fh:
        text = fh.read()
    n = text.count(f["tex"])
    print(f["page"], repr(f["tex"]), "tex count:", n)
    if n != 1:
        ok = False
    if f["fix"] is not None:
        m = text.count(f["fix"]["old"])
        print("   fix old count:", m)
        if m != 1:
            ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

print("all unique:", ok, "written", OUT, len(findings))
