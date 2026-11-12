import json, pathlib

BASE = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b176_180")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_176_180.json")
NL = "\n"

F = []

# ---------------- page 176 ----------------
F.append({
    "page": 176,
    "where": "end of Corollaire 1.3.2 (ii), top of the page: 'et que le S-schéma hensélisé de X en x soit isomorphe'",
    "scan": "'S-' is not underlined: the underline of 'soit non dégénérée et que le' stops after 'le' and resumes under 'schéma hensélisé de' (checked at 3x)",
    "tex": r"\underline{soit non dégénérée et que le S-schéma hensélisé de}",
    "kind": "underline",
    "confidence": "high",
    "fix": {"old": r"et que le S-schéma hensélisé de}",
            "new": r"et que le} $S$-\underline{schéma hensélisé de}"},
    "note": "The symbol S stands outside the underlining, like the other symbols of the statement; p. 175 writes the same phrase of 1.3.2 (i) as $S$-\\underline{schéma hensélisé de}.",
})
F.append({
    "page": 176,
    "where": "Remarque 1.3.3, case (i): 'si l'hensélisé x de X_s est isomorphe par un isomorphisme φ'",
    "scan": "l'hensélisé  x  de  X_s — no 'en' before x (checked at 2x)",
    "tex": r"si l'hensélisé $x$ de $X_s$ est isomorphe",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"si l'hensélisé en $x$ de $X_s$ est isomorphe",
    "note": "Missing word: the henselization at the point x is meant, as in case (ii) of the same remark ('si l'hensélisé en x de X_s est isomorphe'). The TeX keeps the printed reading.",
})

# ---------------- page 177 ----------------
F.append({
    "page": 177,
    "where": "2.1.1, list of notations: 'X_1 ⊂ P^{r+1} est le cône projectant projectif de Y'",
    "scan": "projectant, with a c (checked at 2x); the line above prints 'cône projetant affine'",
    "tex": r"est le cône projetant projectif de $Y$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": {"old": "projetant projectif", "new": "projectant projectif"},
    "corrected": "projetant projectif",
    "note": "Spelling slip (the previous notation line has 'projetant'). The TeX silently corrects it; the fix restores the printed reading.",
})
F.append({
    "page": 177,
    "where": "last paragraph: 'K ∈ Ob D^+(U,Λ) et L ∈ Ob D^+(V,X)'",
    "scan": "D^+(V,X): a typed capital X (checked at 3x)",
    "tex": r"$L \in \mathrm{Ob}\ D^+(V,X)$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"$L \in \mathrm{Ob}\ D^+(V,\Lambda)$",
    "note": "Wrong letter: the coefficient ring is Λ, as in K ∈ Ob D^+(U,Λ) on the same line; the next page pairs (U,K) with (V,L) through φ : f^*L → K. The TeX keeps the printed reading.",
})

# ---------------- page 178 ----------------
F.append({
    "page": 178,
    "where": "square U × T → U, T → k after 'Soient', after the bottom row",
    "scan": "a full stop typed well to the right of the bottom row T → k",
    "tex": r'T \arrow[r, "t"] & k' + NL + r"\end{tikzcd}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r'T \arrow[r, "t"] & k' + NL + r"\end{tikzcd}",
            "new": r'T \arrow[r, "t"] & k' + NL + r"\end{tikzcd}\quad ."},
    "note": "The full stop closes the sentence 'Soient ...'; the file's STRUCTURE comment records it but the code omits it.",
})
F.append({
    "page": 178,
    "where": "factorisation diagram of f_i^*: up-left arrow H^n(U,K) → H^o(T,t^* H^n(U,K)) labelled ≀",
    "scan": "the iso squiggle stands below-left of the shaft (checked at 2x)",
    "tex": r'\arrow[ul, "\wr"' + "']",
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": r'\arrow[ul, "\wr"' + "']",
            "new": r'\arrow[ul, "\wr"]'},
    "note": "Placement only (compiled): for an up-left arrow the swap mark puts the label above-right of the shaft; without it tikz-cd sets it below-left, as in the print and in the file's own STRUCTURE comment.",
})

# ---------------- page 179 ----------------
F.append({
    "page": 179,
    "where": "ladder after 'se déduit du lemme des 5 et du diagramme': vertical arrow H^i(X_1^*) → H^i(Y) labelled ≀",
    "scan": "the iso squiggle stands to the RIGHT of the shaft (checked at 1.5x)",
    "tex": r'\arrow[r, "\partial"] \arrow[d, "\wr"' + "']",
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": r'\arrow[r, "\partial"] \arrow[d, "\wr"' + "']",
            "new": r'\arrow[r, "\partial"] \arrow[d, "\wr"]'},
    "note": "Placement only (compiled): with the swap mark tikz-cd sets the label of a downward arrow on the left; the print and the STRUCTURE comment have it on the right.",
})
F.append({
    "page": 179,
    "where": "same ladder, after the bottom row",
    "scan": "a full stop typed well to the right of the bottom row",
    "tex": r'H^i(Y) \arrow[r, "\partial"] & {}' + NL + r"\end{tikzcd}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r'H^i(Y) \arrow[r, "\partial"] & {}' + NL + r"\end{tikzcd}",
            "new": r'H^i(Y) \arrow[r, "\partial"] & {}' + NL + r"\end{tikzcd}\quad ."},
    "note": "Recorded in the STRUCTURE comment, missing from the code.",
})
F.append({
    "page": 179,
    "where": "ladder after 'On applique le lemme des 5 au diagramme': vertical arrow H^i_{{0}}(X) → H^i_{{0}}(X_{(0)}) labelled ≀",
    "scan": "the iso squiggle stands to the LEFT of the shaft (checked at 1.5x)",
    "tex": r'\arrow[d, "\wr"] & H^i(X)',
    "kind": "other",
    "confidence": "medium",
    "fix": {"old": r'\arrow[d, "\wr"] & H^i(X)',
            "new": r'\arrow[d, "\wr"' + "'] & H^i(X)"},
    "note": "Placement only (compiled): without the swap mark the label of a downward arrow sits on the right; the print and the STRUCTURE comment have it on the left.",
})
F.append({
    "page": 179,
    "where": "same ladder: vertical arrow H^i(X) → H^i(X_{(0)}) with the labels (2.1.2(i)) and ≀",
    "scan": "(2.1.2(i)) typed to the LEFT of the shaft, the iso squiggle to the RIGHT (checked at 1.5x)",
    "tex": r'\arrow[d, "\wr"' + "', " + r'"(2.1.2(\mathrm{i}))"]',
    "kind": "other",
    "confidence": "high",
    "fix": {"old": r'\arrow[d, "\wr"' + "', " + r'"(2.1.2(\mathrm{i}))"]',
            "new": r'\arrow[d, "\wr", "(2.1.2(\mathrm{i}))"' + "']"},
    "note": "Labels on the wrong sides (compiled): the TeX sets ≀ on the left and (2.1.2(i)) on the right, the reverse of the print and of the file's STRUCTURE comment.",
})
F.append({
    "page": 179,
    "where": "same ladder, after the bottom row",
    "scan": "a full stop typed well to the right of the bottom row",
    "tex": r"H^i(X^*_{(0)}) \arrow[r] & {}" + NL + r"\end{tikzcd}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r"H^i(X^*_{(0)}) \arrow[r] & {}" + NL + r"\end{tikzcd}",
            "new": r"H^i(X^*_{(0)}) \arrow[r] & {}" + NL + r"\end{tikzcd}\quad ."},
    "note": "Recorded in the STRUCTURE comment, missing from the code.",
})

# ---------------- checks ----------------
ok = True
for x in F:
    src = (BASE / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    assert "\r" not in src
    if x["fix"]:
        n = src.count(x["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", x["page"], n, repr(x["fix"]["old"]))
        if "%%%%%%%%%%" in x["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", x["page"])
    # 'tex' field should quote the file (sanity check)
    if x["tex"] not in src:
        print("tex field not verbatim (info only)", x["page"], repr(x["tex"][:60]))
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        ok = False
        print("misprint without corrected", x["page"])

# simulate sequential application per page: every later old must still be unique
for p in sorted({x["page"] for x in F}):
    src = (BASE / f"page_{p}.tex").read_text(encoding="utf-8")
    for x in [y for y in F if y["page"] == p and y["fix"]]:
        n = src.count(x["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL CONFLICT", p, n, repr(x["fix"]["old"]))
        src = src.replace(x["fix"]["old"], x["fix"]["new"], 1)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ok" if ok else "PROBLEMS", len(F), "findings ->", OUT)
from collections import Counter
c = Counter((x["page"], "misprint" if x["kind"] == "misprint_in_print" else "normal") for x in F)
for p in range(176, 181):
    print(p, c[(p, "normal")], "/", c[(p, "misprint")])
