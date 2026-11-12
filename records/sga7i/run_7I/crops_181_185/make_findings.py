import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
FOLDER = os.path.join(RUN, "b181_185")
OUT = os.path.join(RUN, "findings_181_185.json")

NL = "\n"

findings = [
    {
        "page": 181,
        "where": "(3.1.6), middle term: 'Psi_{L.}(AxB) --> Psi_L(A) x Psi_{L.}(B) est une équivalence'",
        "scan": "Psi_L(A): underlined Psi with index L and no dot after it (checked at 2.5x zoom); the two outer terms have L.",
        "tex": r"\underline{\Psi}_{L}(A)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\underline{\Psi}_{L.}(A)",
        "note": "Wrong index: the category is Psi_{L.} everywhere else, including the other two terms of (3.1.6). The TeX keeps the printed reading (the current edition keeps it too).",
    },
    {
        "page": 182,
        "where": "after (3.1.8): 'L'isomorphisme (3.1.7.1) est évidemment fonctoriel en A.'",
        "scan": "(3.1.7.1)",
        "tex": "L'isomorphisme (3.1.7.1)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "L'isomorphisme (3.1.8)",
        "note": "Wrong reference number: the canonical isomorphism just displayed is (3.1.8), and the exposé has no (3.1.7.1). The diplomatic TeX keeps the printed reading; the current edition already reads (3.1.8).",
    },
    {
        "page": 182,
        "where": "3.1.9: 'l'ensemble des classes d'isomorphie de celle-ci est munie de façon naturelle d'une structure de groupe'",
        "scan": "munie",
        "tex": "est munie de façon",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "est muni de façon",
        "note": "Agreement slip: the subject is 'l'ensemble' (masculine). The TeX keeps the printed reading.",
    },
    {
        "page": 183,
        "where": "after (3.2.1): 'C'est une résolution de A, donc peut-être identifié à A en tant qu'objet de la catégorie dérivée'",
        "scan": "peut-être (hyphenated; checked at 1.5x zoom)",
        "tex": "peut-être identifié",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "peut être identifié",
        "note": "The verb phrase 'peut être identifié' (can be identified) is meant, not the adverb 'peut-être' (perhaps). The TeX keeps the printed reading.",
    },
    {
        "page": 183,
        "where": "end of the diagram (3.2.3) (anticommutative squares, bottom row '... 0 --> X --j--> L_o --> 0 ...')",
        "scan": "a full stop on the baseline of the bottom row, right of the last '...'",
        "tex": r"\end{tikzcd}" + NL + r"\end{equation}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\quad ."},
        "note": "Punctuation printed after a diagram that the TeX leaves out (its STRUCTURE comment records the full stop). Same form as the fixes on pp. 139 and 144.",
    },
    {
        "page": 183,
        "where": "equation numbers of the diagram after 'explicité dans le diagramme à carrés anticommutatifs' and of the display 'c(X,alpha) : L. --> A (hom. de degré 1 dans D(C))'",
        "scan": "both displays are numbered (3.2.3); the next display is (3.2.4)",
        "tex": r"\begin{equation}\tag{3.2.3}" + NL + r"c(X,\alpha)",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": None,
        "note": "The print gives the number (3.2.3) twice and the TeX keeps both tags. The later references 'l'homomorphisme de complexes u de (3.2.3)' (p. 184) and 'l'homomorphisme (3.2.3) relatif à (X,alpha)' (p. 185) point to the diagram, where u^{-1} and u^o are defined. No correction is proposed: the intended number of the second display is not evident.",
    },
    {
        "page": 184,
        "where": "after Théorème 3.2.5: 'Nous laisserons au lecteur le soin d'établir ... et nous bornerons à prouver qu'elle est bijective'",
        "scan": "et nous bornerons à (checked at 1.2x zoom)",
        "tex": "et nous bornerons à",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "et nous nous bornerons à",
        "note": "The pronominal verb 'se borner à' needs the reflexive pronoun; one 'nous' of 'nous nous' is lost (haplography). The TeX keeps the printed reading (the current edition keeps it too).",
    },
    {
        "page": 184,
        "where": "end of the diagram (*) (0 --> X --j--> L_o --> 0 over 0 --> C^o --j'--> C^1 --> C^2 --> ...)",
        "scan": "a comma on the baseline of the bottom row, right of the final '...'",
        "tex": r"\end{tikzcd}" + NL + r"\end{equation}",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\quad ,"},
        "note": "Punctuation printed after a diagram that the TeX leaves out (its STRUCTURE comment records the comma). Same form as the fixes on pp. 139 and 144.",
    },
    {
        "page": 185,
        "where": "'Ceci dit, la donnée d'un homomorphisme j : L_o --> X satisfaisant les conditions (3.2.5.1)'",
        "scan": "j : L_o --> X (checked at 2x zoom)",
        "tex": r"homomorphisme $j : L_o \longrightarrow X$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"homomorphisme $s : L_o \longrightarrow X$",
        "note": "Wrong letter: the morphism L_o --> X satisfying (3.2.5.1) (js = u^o = id, sd_o = alpha) is s; j : X --> L_o is the projection of the extension. The diplomatic TeX keeps the printed reading; the current edition already reads s.",
    },
]

pages = {}
for p in sorted({f["page"] for f in findings} | {181, 182, 183, 184, 185}):
    with open(os.path.join(FOLDER, "page_%03d.tex" % p), "r", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read()

ok = True
for i, f in enumerate(findings):
    text = pages[f["page"]]
    if "\r" in text:
        print("WARNING: CR in page", f["page"])
    fx = f.get("fix")
    if fx is not None:
        n = text.count(fx["old"])
        print(i, f["page"], "fix.old count =", n)
        if n != 1:
            ok = False
        # the old must not span a marker line
        if "%%%%%%%%%%" in fx["old"]:
            ok = False
            print("  old touches a marker line")
    else:
        n = text.count(f["tex"])
        print(i, f["page"], "tex count =", n)
        if n != 1:
            ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# reload to confirm valid JSON
with open(OUT, "r", encoding="utf-8") as fh:
    back = json.load(fh)
print("written", OUT, "entries:", len(back), "all unique:", ok)
