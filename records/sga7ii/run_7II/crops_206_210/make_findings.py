import json
import sys

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_206_210.json"
DIR = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b206_210"

F = []

F.append({
    "page": 207,
    "where": "first of the three displays after 'que' (labelled (a), (b), (c) in the print): Σ (-1)^q dim(R^q f_* Z/ℓ)_η̄ - dim(R^q f_* Z/ℓ)_s = Σ_{x∈F(s)} Σ (-1)^q dim Φ^q_η̄ (Z/ℓ)_x",
    "scan": "the label (a) is typed at the left margin on the first line of the display",
    "tex": "\\begin{equation*}\n\\begin{aligned} &\\sum (-1)^q \\dim(R^q",
    "kind": "missing",
    "confidence": "high",
    "fix": {
        "old": "\\begin{equation*}\n\\begin{aligned} &\\sum (-1)^q \\dim(R^q",
        "new": "\\begin{equation*}\\tag{a}\n\\begin{aligned} &\\sum (-1)^q \\dim(R^q"
    },
    "note": "The TeX tags only the third display (\\tag{c}); (a) is missing. \\tag inside equation* is standard amsmath (test-compiled: prints (a)). Equivalent alternative in the file's own style for (c): \\begin{equation}\\tag{a} ... \\end{equation}."
})

F.append({
    "page": 207,
    "where": "second display after 'que': Σ (-1)^q dim Sw(R^q f_* Z/ℓ)_η̄ = Σ_{x∈F(s)} Σ (-1)^q dim Sw Φ^q_η̄ (Z/ℓ)_x",
    "scan": "the label (b) is typed at the left margin of the display",
    "tex": "\\begin{equation*}\n\\sum (-1)^q \\dim \\mathrm{Sw}",
    "kind": "missing",
    "confidence": "high",
    "fix": {
        "old": "\\begin{equation*}\n\\sum (-1)^q \\dim \\mathrm{Sw}",
        "new": "\\begin{equation*}\\tag{b}\n\\sum (-1)^q \\dim \\mathrm{Sw}"
    },
    "note": "The label (b) is missing, as (a) above (same remark on \\tag in equation*)."
})

F.append({
    "page": 207,
    "where": "display defining the local term: ε_s(G) = dim(G_η̄) - dim(G_s) - dim Sw(G_η̄)",
    "scan": "both operators are minus signs (checked at 2x)",
    "tex": "\\dim(G_s) \\; - \\; \\dim \\mathrm{Sw}(G_{\\bar{\\eta}})",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "\\dim(G_s) \\; + \\; \\dim \\mathrm{Sw}(G_{\\bar{\\eta}})",
    "note": "Sign slip: the local term of the Euler-Poincaré formula ([4], SGA 5 X 7.2) is dim G_η̄ - dim G_s + Sw. The page itself needs +: (c) is (a) + (b), and Σ_x dim tot Φ_x follows only with +, since dim tot = dim Sw + dim (p. 200). The TeX keeps the printed reading."
})

F.append({
    "page": 208,
    "where": "Théorème 2.4, last sentence: 'Alors, le nombre total (1.8) de cycles évanescents de X/S en x̄'",
    "scan": "'Alors, le nombre' and '(1.8)' are underlined, 'total' is not (checked at 2.5x); likewise 'total' in Corollaire 2.2 (p. 206), which the TeX already leaves outside the underline",
    "tex": "\\underline{Alors, le nombre total (1.8) de cycles évanescents de}",
    "kind": "underline",
    "confidence": "high",
    "fix": {
        "old": "\\underline{Alors, le nombre total (1.8) de",
        "new": "\\underline{Alors, le nombre} total \\underline{(1.8) de"
    },
    "note": "The TeX underlines 'total' with the rest of the phrase."
})

F.append({
    "page": 208,
    "where": "paragraph 'Soit S' le trait hensélien ...': 'et soit X' = X ×_s S''",
    "scan": "the subscript of the product sign is a small s: 15 px high against 20-21 px for the capital S of S' beside it, the same height as the s of X_s on the page (checked at 8x, pixel-measured)",
    "tex": "et soit $X' = X \\times_s S'$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "et soit $X' = X \\times_S S'$",
    "note": "X' is the base change of X/S to S', a fibre product over S, not over the closed point s. The TeX keeps the printed reading. The same slip in the next paragraph: correct both or neither."
})

F.append({
    "page": 208,
    "where": "paragraph 'Pour un tel S , soit S' le complété de S , et X' = X ×_s S''",
    "scan": "small s again: 16 px high against 21 px for the capital S of S' (checked at 4x, pixel-measured)",
    "tex": "et $X' = X \\times_s S'$ . Le nombre",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "et $X' = X \\times_S S'$ . Le nombre",
    "note": "As in the previous paragraph (fibre product over S). The TeX keeps the printed reading. Correct both or neither."
})

F.append({
    "page": 209,
    "where": "Proposition 2.5 (b): 'il existe un S-isomorphisme entre l'hensélisé de X en x'",
    "scan": "'S-' is not underlined; the underline starts under the i of 'isomorphisme' (checked at 2x)",
    "tex": "\\underline{S-isomorphisme entre l'hensélisé de}",
    "kind": "underline",
    "confidence": "high",
    "fix": {
        "old": "\\underline{S-isomorphisme",
        "new": "$S$-\\underline{isomorphisme"
    },
    "note": "The TeX underlines 'S-' with the word. S (the base) written $S$ as the file writes '$k$-schéma' and '$k$-jets'."
})

F.append({
    "page": 209,
    "where": "paragraph 'Montrons que 2.5 ⇒ 2.4': 'le nombre de Milnor de Y/T en y_o'",
    "scan": "Y/T with a clearly typed capital T (checked at 4x)",
    "tex": "le nombre de Milnor de $Y/T$ en $y_o$",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": "le nombre de Milnor de $Y/\\mathbb{P}^1$ en $y_o$",
    "note": "No T is defined in Exposé XVI; in 2.5 the morphism is f : Y → P^1_k, and 2.3 is applied to Y over P^1 (the next paragraph: 'on prendra pour Y/P^1'). Probably the author's slip; review before using in the corrected edition. The TeX keeps the printed reading."
})

F.append({
    "page": 210,
    "where": "paragraph 'Fixons d' et d''': 'alors, pour d' et d'' assez grand, l'application de restriction'",
    "scan": "'assez grand,' without s",
    "tex": "$d''$ assez grand, l'application",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": "$d''$ assez grands, l'application",
    "note": "Agreement with the two degrees; the same page later prints 'si d' et d'' sont assez grands'. The TeX keeps the printed reading."
})

F.append({
    "page": 210,
    "where": "last sentence: 'Il résoud le problème posé.'",
    "scan": "'résoud' with final d",
    "tex": "Il résoud le problème posé.",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "Il résout le problème posé.",
    "note": "Spelling: the third person singular of résoudre is résout. The TeX keeps the printed reading."
})

# verify fixes and tex substrings
ok = True
for f in F:
    p = f["page"]
    txt = open(DIR + "\\page_%03d.tex" % p, encoding="utf-8").read()
    if f["fix"] is not None:
        n = txt.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", p, n, repr(f["fix"]["old"]))
        if "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", p)
    nt = txt.count(f["tex"])
    if nt < 1:
        ok = False
        print("TEX NOT FOUND", p, repr(f["tex"]))
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        print("NO CORRECTED", p)
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        ok = False
        print("CORRECTED ON NON-MISPRINT", p)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
sys.stdout.reconfigure(encoding="utf-8")
print("written", len(F), "ok" if ok else "PROBLEMS")
