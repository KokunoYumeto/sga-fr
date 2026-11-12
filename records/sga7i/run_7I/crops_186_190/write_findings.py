import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b186_190")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_186_190.json")

KEEP = " The TeX keeps the printed reading; 'corrected' replaces the 'tex' substring."

F = [
    {
        "page": 186,
        "where": "end of the proof of 3.2.5: 'l'extension C^o. Comme l'homomorphisme précédent est un homomorphisme de résolutions de A'",
        "scan": "one paragraph: the full line '... comme image inverse de l'extension C°.' is followed by 'Comme l'homomorphisme précédent ...' at the left margin, without the paragraph indent that 'Dans le présent numéro' and 'Nous explicitons' have on this page",
        "tex": "l'extension $C^o$.\n\nComme l'homomorphisme",
        "kind": "other",
        "confidence": "low",
        "fix": {"old": "l'extension $C^o$.\n\nComme", "new": "l'extension $C^o$. Comme"},
        "note": "Layout only: the TeX starts a new paragraph inside the printed paragraph. Not the heading run-in case decided globally.",
    },
    {
        "page": 186,
        "where": "Théorème 3.3.1, first line: 'est exacte à gauche (loc. cit. 2.2) elle admet un objet quasi-maximal (loc. cit. 4.4), et pour tout objet'",
        "scan": "(loc. cit. 2.2) elle admet (no comma after the parenthesis)",
        "tex": "(loc. cit. 2.2) \\underline{elle admet",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "(loc. cit. 2.2), \\underline{elle admet",
        "note": "Missing comma between the first two clauses of the statement; the following clauses are separated by commas ('(loc. cit. 4.4), et pour tout objet')." + KEEP,
    },
    {
        "page": 186,
        "where": "3.3.2, first line: 'Dire la catégorie cofibrée Psi_{L.} est exacte à gauche signifie qu'elle est additive'",
        "scan": "Dire la catégorie cofibrée (no 'que'; checked at 1.4x zoom)",
        "tex": "Dire la catégorie cofibrée",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "Dire que la catégorie cofibrée",
        "note": "The conjunction 'que' is missing ('Dire que ... est exacte à gauche signifie que ...')." + KEEP,
    },
    {
        "page": 187,
        "where": "(3.3.2.1), the display after 'de C, le foncteur naturel (notations de loc. cit. 1.8)'",
        "scan": "Psi_{L.}(A) --> Psi_{L.}([A --> A'']): the first argument is A without a prime (checked at 2x zoom)",
        "tex": "\\underline{\\Psi}_{L.}\\,(A) \\longrightarrow",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{\\Psi}_{L.}\\,(A') \\longrightarrow",
        "note": "The functor of the left-exactness condition starts from the fibre over A': the next paragraph says 'La définition du foncteur Psi(A') --> Psi([A --> A'']) de (3.3.2.1) est évidente', and its proof produces an extension X' of L_o by A' = Ker v." + KEEP,
    },
    {
        "page": 187,
        "where": "last paragraph, first line: 'Lorsque v: A --> A'' s'insère dans une suite exacte courte comme dans 3.2.3'",
        "scan": "comme dans 3.2.3",
        "tex": "suite exacte courte comme dans 3.2.3",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "suite exacte courte comme dans 3.3.2",
        "note": "Wrong reference number (digits transposed): the short exact sequence 0 --> A' --> A --> A'' --> 0 is that of 3.3.2, (3.3.2.1); the two displays numbered (3.2.3) on p. 183 are the diagram of complexes and c(X,alpha). Same slip as '(3.2.3)' at the end of the paragraph (next entry)." + KEEP,
    },
    {
        "page": 187,
        "where": "last sentence of the page: 'Ceci établit, modulo des compatibilités dont la vérification est évidente, l'exactitude à gauche explicitée dans (3.2.3).'",
        "scan": "explicitée dans (3.2.3).",
        "tex": "explicitée dans (3.2.3)",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "explicitée dans (3.3.2)",
        "note": "Wrong reference number: left exactness is made explicit in 3.3.2, (3.3.2.1) (3.3.5 cites it as 'exacte à gauche (3.3.2)'); (3.2.3) is the diagram of complexes of p. 183." + KEEP,
    },
    {
        "page": 188,
        "where": "3.3.3, definition of quasi-maximal: 'de telle sorte que E soit majoré par E_o i.e. qu'il existe un morphisme, E_o --> E''",
        "scan": "que E soit majoré (E without a prime; checked at 3x zoom)",
        "tex": "de telle sorte que $E$ soit",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "de telle sorte que $E'$ soit",
        "note": "The object majorized by E_o is E': the gloss 'i.e. qu'il existe un morphisme E_o --> E'' says so (majorized by E_o = receiving a morphism from E_o)." + KEEP,
    },
    {
        "page": 188,
        "where": "3.3.3: 'i.e. qu'il existe un morphisme, E_o --> E''",
        "scan": "after 'morphisme' a mark at the baseline that the TeX reads as a comma (a thin downstroke ending in a blob, not shaped like the page's typed commas), with a thin stray stroke above it in the interline",
        "tex": "un morphisme, $E_o \\longrightarrow E'$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "un morphisme $E_o \\longrightarrow E'$",
        "note": "Comma or correction mark, the sentence takes no comma before the formula. If the two strokes are a deletion mark, the diplomatic text should drop the comma as well." + KEEP,
    },
    {
        "page": 188,
        "where": "after the display L'_1 = Coker(d_1 : L_2 --> L_1): 'et où alpha_o a comme composantes (d'_1,id_{L'_1}) , d'_1 : L_1 --> L_o étant déduit de d_1 : L_1 --> L_o par passage au quotient'",
        "scan": "déduit de d_1 : L_1 --> L_o (index 1 on d; checked at 1.1x zoom)",
        "tex": "déduit de $d_1 : L_1 \\longrightarrow L_o$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "déduit de $d_o : L_1 \\longrightarrow L_o$",
        "note": "Wrong index: the differential L_1 --> L_o is d_o ((3.1.3), (3.2.3)); d_1 is L_2 --> L_1, as in the display just above. Same phrase as the next entry." + KEEP,
    },
    {
        "page": 188,
        "where": "same phrase: 'd'_1 : L_1 --> L_o étant déduit de ... par passage au quotient'",
        "scan": "d'_1 : L_1 --> L_o (no prime on the source L_1)",
        "tex": "$d_1' : L_1 \\longrightarrow L_o$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "$d_1' : L_1' \\longrightarrow L_o$",
        "note": "The map obtained 'par passage au quotient' lives on the quotient L'_1 = Coker d_1, and the components (d'_1, id_{L'_1}) of alpha_o need the common source L'_1. The printed name d'_1 is kept (d'_o would match d_o)." + KEEP,
    },
    {
        "page": 188,
        "where": "end of the paragraph 'Pour voir que E_o est bien quasi-maximal': 'il est immédiat qu'un objet (X',alpha') de Psi tel que l'extension X' soit scindée, est majorée par E_o.'",
        "scan": "est majorée par E_o (checked at 1.6x zoom)",
        "tex": "scindée, est majorée par",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "scindée, est majoré par",
        "note": "Agreement slip: the subject is 'un objet' (masculine), as in 'est majoré par E_o' of 3.3.3." + KEEP,
    },
    {
        "page": 189,
        "where": "3.3.4: 'si le foncteur précédent est représentable par un objet Omega_E de C.'",
        "scan": "de C. with no underline under the C (checked at 2.5x zoom); the other C's of the page are underlined",
        "tex": "$\\Omega_E$ de $C$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$\\Omega_E$ de $\\underline{C}$",
        "note": "Category letter without its underline." + KEEP,
    },
    {
        "page": 189,
        "where": "end of 3.3.4: 'n'étant autre que le composé A --j--> X --can--> Coker alpha'",
        "scan": "the label over A --> X is j: its descender hooks to the left like the j of (3.1.2) on p. 180, not the footed i there (pixel comparison of the three glyphs)",
        "tex": "A \\xrightarrow{\\ j\\ } X",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "A \\xrightarrow{\\ i\\ } X",
        "note": "In (3.1.2) the extension is 0 --> A --i--> X --j--> L_o --> 0: the map A --> X is i, j goes from X to L_o." + KEEP,
    },
    {
        "page": 189,
        "where": "3.3.5: 'on montre que Psi se réconstitue, à équivalence de catégories fibrées sur C près'",
        "scan": "réconstitue (acute accent on the first e; checked at 1.6x zoom)",
        "tex": "se réconstitue",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "se reconstitue",
        "note": "Spelling: 'reconstituer' has no accent." + KEEP,
    },
    {
        "page": 190,
        "where": "second paragraph: 'le complexe typique de l'objet quasi-maximal décrit dans 3.3.3) est canoniquement isomorphe à L.'",
        "scan": "décrit dans 3.3.3) (a closing parenthesis without an opening one)",
        "tex": "décrit dans 3.3.3)",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "décrit dans 3.3.3",
        "note": "Stray closing parenthesis: the parenthesis of the preceding sentence closes before 'Mais alors'." + KEEP,
    },
    {
        "page": 190,
        "where": "(3.3.6.1), the arrow Psi^o_{L.}(A'') --> Psi^1_{L.}(A')",
        "scan": "the arrow is labelled with a small o like the degree superscripts (checked at 4x zoom); the next line names it 'la flèche notée ∂' with a typed ∂",
        "tex": "\\xrightarrow{\\ o\\ }",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\xrightarrow{\\ \\partial\\ }",
        "note": "The connecting map is the arrow the following sentence calls ∂." + KEEP,
    },
]

ok = True
for f in F:
    t = (B / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    if f["fix"]:
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, f["page"], repr(f["fix"]["old"]))
        if "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", f["page"])
    n = t.count(f["tex"])
    if n != 1:
        ok = False
        print("TEX COUNT", n, f["page"], repr(f["tex"]))
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        print("NO CORRECTED", f["page"], f["where"])
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        ok = False
        print("STRAY CORRECTED", f["page"], f["where"])

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(186, 191):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("OK" if ok else "PROBLEMS")
