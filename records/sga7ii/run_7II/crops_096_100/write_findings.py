import json
import sys

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_096_100.json"
DIR = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b096_100"

F = []

# ---------------- page 97 ----------------
F.append({
    "page": 97,
    "where": "1.4.2, first line: 'Un complexe de faisceau de Λ-modules'",
    "scan": "Un complexe de faisceau de Λ-modules (singular 'faisceau', no x; checked at 2x)",
    "tex": "complexe de faisceau de",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "complexe de faisceaux de",
    "note": "Agreement slip of the print: 'complexe de faisceaux', as in a) just below and in 'des complexes de faisceaux de Λ-modules' at the end of the page. The TeX keeps the printed reading.",
})
F.append({
    "page": 97,
    "where": "1.4.2, first line: 'K sur X x_s S'",
    "scan": "K sur X x_s S (capital X; checked at 2x)",
    "tex": r"$X \times_s S$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"$Y \times_s S$",
    "note": "1.4.1 takes Y over s and works on Y x_s S; 1.4.3 and the end of this page also write Y x_s S, and no X is in play in 1.4. The TeX keeps the printed reading. The corrected layer already has Y here (SGA7II-FR-XIII-002) but keeps the two X at the top of p. 98.",
})
F.append({
    "page": 97,
    "where": "1.4.2 a), second line: 'action continue de Gal(s̄/s̄)'",
    "scan": "Gal(s̄/s̄) (bar over both s; checked at 2x), then (resp. Gal(η̄/η))",
    "tex": r"\mathrm{Gal}(\bar{s}/\bar{s})",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\mathrm{Gal}(\bar{s}/s)",
    "note": "The Galois group of s̄ over s, parallel to Gal(η̄/η) in the same line and to the exact sequence 0 -> I -> Gal(η̄/η) -> Gal(s̄/s) -> 0 earlier in the exposé; Gal(s̄/s̄) is trivial. The TeX keeps the printed reading (the corrected layer too).",
})

# ---------------- page 98 ----------------
F.append({
    "page": 98,
    "where": "first paragraph: 'à tout objet K de D(X x_s S, Λ)'",
    "scan": "D(X x_s S, Λ) (capital X; checked at 1.5x)",
    "tex": r"D(X \times_s S, \Lambda)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"D(Y \times_s S, \Lambda)",
    "note": "Same slip as in 1.4.2 on p. 97: the complexes of 1.4.2 live on Y x_s S, and 1.4.3 below writes D(Y x_s S, Λ). The TeX keeps the printed reading; the corrected layer keeps X here although it corrects the X of 1.4.2.",
})
F.append({
    "page": 98,
    "where": "first paragraph: 'un triangle distingué de D(X x_s η, Λ)'",
    "scan": "D(X x_s η, Λ) (capital X; checked at 1.5x)",
    "tex": r"D(X \times_s \eta, \Lambda)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"D(Y \times_s \eta, \Lambda)",
    "note": "The triangle (1.4.2.2) lies in K(Y x_s η, Λ) (end of p. 97). The TeX keeps the printed reading (the corrected layer too).",
})

# ---------------- page 99 ----------------
F.append({
    "page": 99,
    "where": "2.1.2, the diagram after 'Soit le diagramme commutatif (1.3.2.1)'",
    "scan": "the re-displayed diagram has no formula number (left margin empty); (1.3.2.1) appears only in the sentence before it",
    "tex": r"\begin{equation}\tag{1.3.2.1}",
    "kind": "extra",
    "confidence": "high",
    "fix": {"old": r"\begin{equation}\tag{1.3.2.1}", "new": r"\begin{equation}\notag"},
    "note": "The TeX prints a second (1.3.2.1) beside this diagram (the numbered original is in 1.3.2). \\notag (amsmath) removes the number and leaves the display as it is; the edit does not overlap the full-stop fix on \\end{tikzcd}.",
})
F.append({
    "page": 99,
    "where": "same diagram, after the bottom-right node X_η",
    "scan": "X_s ↪(i) X ↩(j) X_η .  (full stop after the diagram)",
    "tex": "X_{\\eta} \\arrow[l, hook', \"j\"']\n\\end{tikzcd}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\quad ."},
    "note": "Known pattern: the full stop printed after a diagram is left out (the STRUCTURE comment records the omission). Same form as the fixes on pp. 6, 40, 46, 79, 89.",
})
F.append({
    "page": 99,
    "where": "paragraph after the diagram: 'sa restriction à l'ouvert X_η et encore injective'",
    "scan": "et encore injective (checked at 2x)",
    "tex": "et encore injective",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "est encore injective",
    "note": "'et' for 'est'. The TeX keeps the printed reading (the corrected layer too).",
})

# ---------------- page 100 ----------------
F.append({
    "page": 100,
    "where": "(2.1.2.4), bottom-right node of the triangle",
    "scan": "RΨ_η(K_s) (subscript s on K; checked at 3x)",
    "tex": r"R\Psi_\eta(K_s) \arrow[ul]",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"R\Psi_\eta(K_\eta) \arrow[ul]",
    "note": "(2.1.2.4) is (1.4.2.2) written for RΨ(K): by (2.1.2.1) and (2.1.2.2) its terms are sp* i*K -> RΨ_η(K_η) -> RΦ(K); RΨ_η is defined on D^+(X_η, Λ), where K_s does not lie. The TeX keeps the printed reading. The corrected layer (SGA7II-FR-XIII-003) has K_\\eta alone, which drops RΨ_η: K_η is a complex on X_η, not an object of D^+(X_s x_s η, Λ). RΨ_η(K_η) (equal to RΨ_η(K) in the notation set on p. 99) is the term.",
})
F.append({
    "page": 100,
    "where": "2.1.3, last sentence: 'l'hensélisé strict S_nr de S , de point géométrique η_nr'",
    "scan": "de point géométrique η_nr (checked at 1.2x)",
    "tex": r"de point géométrique $\eta_{nr}$",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": r"de point générique $\eta_{nr}$",
    "note": "η_nr is the generic point of the strict henselization S_nr (the base of the fibre X_(x̄) x_{η_nr} η̄ in 2.1.4), not a geometric point; the geometric point is η̄. Probably 'générique' typed as 'géométrique' after the two 'point géométrique' earlier in the paragraph. Low confidence: review before use. The TeX keeps the printed reading.",
})
F.append({
    "page": 100,
    "where": "heading of Proposition 2.1.4",
    "scan": "Proposition 2.1.4.. (two full stops; checked at 1.2x)",
    "tex": "2.1.4..",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "2.1.4.",
    "note": "Doubled full stop of the typescript. The TeX keeps the printed reading.",
})
F.append({
    "page": 100,
    "where": "Proposition 2.1.4, first formula: 'RΓ(X_(x̄) x_{η_xr} η̄ , K)'",
    "scan": "x_{η_xr} (subscript xr under η; checked at 1.2x); the display below has x_{η_nr}",
    "tex": r"\times_{\eta_{xr}}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\times_{\eta_{nr}}",
    "note": "η_nr, the point named at the end of 2.1.3 and used in the display that follows. The TeX keeps the printed reading (the corrected layer too).",
})

# ---------------- checks ----------------
ok = True
for f in F:
    path = DIR + "\\page_%03d.tex" % f["page"]
    with open(path, encoding="utf-8", newline="") as h:
        txt = h.read()
    if "\r\n" in txt:
        print("CRLF in", path)
    if f["tex"] not in txt:
        print("TEX NOT FOUND", f["page"], repr(f["tex"]))
        ok = False
    fx = f["fix"]
    if fx is not None:
        n = txt.count(fx["old"])
        if n != 1:
            print("OLD COUNT", n, f["page"], repr(fx["old"]))
            ok = False
        # the old must not touch a marker line
        i = txt.find(fx["old"])
        seg = txt[max(0, i - 1): i + len(fx["old"]) + 1]
        if "%%%%%%%%%%" in seg:
            print("TOUCHES MARKER", f["page"])
            ok = False
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            print("NO CORRECTED", f["page"])
            ok = False
    else:
        f.pop("corrected", None)

# apply fixes sequentially per page to confirm they still apply in order
pages = sorted(set(f["page"] for f in F))
for p in pages:
    path = DIR + "\\page_%03d.tex" % p
    with open(path, encoding="utf-8", newline="") as h:
        txt = h.read()
    for f in F:
        if f["page"] == p and f["fix"] is not None:
            if txt.count(f["fix"]["old"]) != 1:
                print("SEQUENTIAL FAIL", p, repr(f["fix"]["old"]))
                ok = False
            txt = txt.replace(f["fix"]["old"], f["fix"]["new"], 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as h:
    json.dump(F, h, ensure_ascii=False, indent=1)
    h.write("\n")

from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in [96, 97, 98, 99, 100]:
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("OK" if ok else "PROBLEMS")
