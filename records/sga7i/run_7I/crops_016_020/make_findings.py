import json
import os
import sys

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b016_020"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_016_020.json"

findings = [
    # ---------------- page 16 ----------------
    {
        "page": 16,
        "where": "4.8, first sentence (definition of Z)",
        "scan": "soit Z le lieu de non / de f . On peut encore conclure",
        "tex": "le lieu de non de  $f$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "le lieu de non lissité de  $f$",
        "note": "The print omits the word 'lissité' at the line break after 'non'; the TeX keeps the printed reading. Z is the non-smooth locus of f (cf. 4.10 (a), 'point de non lissité'). 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 16,
        "where": "4.10 (b), first inequality",
        "scan": "prof et_y(X_η̄) ⩾ n - d(g) , i.e.",
        "tex": "$n - d(g)$ ,  i.e.",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$n - d(y)$ ,  i.e.",
        "note": "The typescript clearly has d(g) (typewriter g, not y); the point is y and its dimension was just defined as d(y). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 16,
        "where": "4.10 (b), second inequality",
        "scan": "H^i_{y}(X_η̄) = 0 pour i ⩽ n - d(g)",
        "tex": "$\\leqslant$ $n - d(g)$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$\\leqslant$ $n - d(y)$",
        "note": "Same misprint g for y as in the preceding inequality; the TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    # ---------------- page 18 ----------------
    {
        "page": 18,
        "where": "Proposition 5.1.1, 'sur le normalisé S' de S dans ...'",
        "scan": "sur le normalisé S' de S dans η telle que",
        "tex": "\\underline{dans}  $\\eta$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{dans}  $\\eta'$",
        "note": "The print has η without a prime. S' must be the normalization of S in the extension η' (the display uses X' ⊗_{S'} η'); the normalization of the trait S in η is S itself. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 18,
        "where": "proof of 5.1.1, 'chaînes de composantes ...'",
        "scan": "santes rationelles lisses de self intersection",
        "tex": "rationelles",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "rationnelles",
        "note": "Spelling error of the typescript (one n); the TeX keeps the printed reading.",
    },
    {
        "page": 18,
        "where": "(5.2.1), first arrow",
        "scan": "0 ——— π_1(X_η̄,ξ)  (plain rule, no arrowhead)",
        "tex": "0 \\arrow[r, dash] &",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "0 \\arrow[r] &",
        "note": "The first map of the exact sequence is drawn as a plain rule without an arrowhead (no trace of a lost head); the TeX keeps the printed reading. The other three arrows have heads.",
    },
    {
        "page": 18,
        "where": "(5.2.1), middle term",
        "scan": "π_1(X,ξ)",
        "tex": "& \\pi_1(X,\\xi) \\arrow[r]",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "& \\pi_1(X_\\eta,\\xi) \\arrow[r]",
        "note": "The print has X without subscript; 5.2 introduces only X_η, and the exact sequence is 0 → π_1(X_η̄) → π_1(X_η) → Gal(η̄/η) → 0. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 18,
        "where": "last paragraph, 'la suite exacte (5.2.2) splitte'",
        "scan": "la suite exacte (5.2.2) splitte canonique-ment",
        "tex": "la suite exacte (5.2.2) splitte",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "la suite exacte (5.2.1) splitte",
        "note": "Wrong reference number: the exact sequence that splits by the rational point is (5.2.1); (5.2.2) is the homomorphism Gal → Aut ext. The TeX keeps the printed reading.",
    },
    # ---------------- page 19 ----------------
    {
        "page": 19,
        "where": "5.3.1, 'Pour k = 1 ou 2 et p_k(y_j) ∈ X'_{iη}'",
        "scan": "p _k(y_j) ∈ X'_{iη}",
        "tex": "$p_k(y_j) \\in X'_{i\\eta}$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "$\\mathrm{pr}_k(y_j) \\in X'_{i\\eta}$",
        "note": "The print has 'p' followed by a blank space and the subscript k; the same projection is written pr_k(ȳ_j) in the next clause. Probably a dropped 'r'; the TeX keeps the printed reading.",
    },
    {
        "page": 19,
        "where": "5.3.1, '(le même modulo Ker(π → π^{(p)}) .'",
        "scan": "correspondant (le même modulo Ker(π ⟶ π^(p)) . On peut prendre",
        "tex": "\\pi^{(p)})$ .",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\pi^{(p)})$) .",
        "note": "Unbalanced parenthesis in the print: the parenthesis opened before 'le même' is never closed. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 19,
        "where": "'Dès lors ...' paragraph, 'X'_{iη̄} → X_{iη̄} est de descente effective'",
        "scan": "X'_{iη̄} ⟶ X_{iη̄} est de descente effective",
        "tex": "\\longrightarrow X_{i\\bar{\\eta}}$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "\\longrightarrow X_{\\bar{\\eta}}$",
        "note": "The target is printed X_{iη̄}, which is not defined (only the components X'_{iη} of the normalization carry an index i); the descent morphism is to X_η̄. The intended source may also be X'_η̄. The TeX keeps the printed reading.",
    },
    {
        "page": 19,
        "where": "5.3.2, 'd'un A^n_S'",
        "scan": "double-struck 𝔸^n_S",
        "tex": "\\mathbf{A}^n_S",
        "kind": "font",
        "confidence": "medium",
        "fix": {"old": "\\mathbf{A}^n_S", "new": "\\mathbb{A}^n_S"},
        "note": "The print's A has the doubled stroke of a double-struck letter, not a bold one. The global note covers only Z, Q, F, C.",
    },
    {
        "page": 19,
        "where": "5.3.2, '(dont il nous est loisible d'augmenter le nombre.'",
        "scan": "x_i ,(dont il nous est loisible d'augmenter le nombre. Appliquant",
        "tex": "d'augmenter le nombre.",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "d'augmenter le nombre).",
        "note": "Unbalanced parenthesis in the print: '(dont ...' is never closed. The TeX keeps the printed reading.",
    },
    # ---------------- page 20 ----------------
    {
        "page": 20,
        "where": "Théorème 5.4, 'Soit x un point rationnel de X'",
        "scan": "Soit x  (ordinary typewriter x, same weight as the surrounding text; also plain in 'xξ')",
        "tex": "$\\mathbf{x}$",
        "kind": "font",
        "confidence": "high",
        "fix": {"old": "$\\mathbf{x}$", "new": "$x$"},
        "note": "The print does not set this x in bold.",
    },
]

errors = []
for f in findings:
    path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if "\r\n" in text:
        errors.append("CRLF in %s" % path)
    n_tex = text.count(f["tex"])
    if n_tex != 1:
        errors.append("page %d tex occurs %d times: %r" % (f["page"], n_tex, f["tex"]))
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = text.count(old)
        if n != 1:
            errors.append("page %d fix.old occurs %d times: %r" % (f["page"], n, old))
        if "%%%%%%%%%%" in old:
            errors.append("fix crosses marker: %r" % old)
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        errors.append("corrected on non-misprint")

if errors:
    print("\n".join(errors))
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for f in findings:
    key = f["page"]
    c = counts.setdefault(key, [0, 0])
    if f["kind"] == "misprint_in_print":
        c[1] += 1
    else:
        c[0] += 1
for p in (16, 17, 18, 19, 20):
    c = counts.get(p, [0, 0])
    print("p%d: %d/%d" % (p, c[0], c[1]))
print("written", OUT, len(findings))
