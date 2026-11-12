import json
import os
import sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
PAGES = os.path.join(RUN, "b416_420")
OUT = os.path.join(RUN, "findings_416_420_recheck.json")

findings = [
    {
        "page": 416,
        "where": "8.2, l. 4: «d'où une isogénie A_K ⟶ A_{K'}»",
        "scan": "d'où une isogénie A_K ⟶ A_{K'}, (the prime is typed after the lowered K, not next to the A as in B'_K on the same page)",
        "tex": "$A_K \\longrightarrow A_{K'}$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$A_K \\longrightarrow A'_K$",
        "note": "The polarization gives an isogeny onto the dual A'_K, whose extension is (8.1.6); A_{K'} is the notation of 8.1 for the base change to the extension K'. The TeX keeps the printed reading.",
    },
    {
        "page": 416,
        "where": "8.3, l. 2: «deux extensions isomorphes K', K'_1 de K'»",
        "scan": "deux extensions isomorphes K', K'_1 de K' donnent des groupes",
        "tex": "$K'_1$ de $K'$ donnent",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "$K'_1$ de $K$ donnent",
        "note": "K' and K'_1 are extensions of K. The TeX keeps the printed K'.",
    },
    {
        "page": 417,
        "where": "after (8.3.1): «on voit que les A_{K,K'} forment ainsi»",
        "scan": "les A_{K,K'} forment (no handwritten ♮ over the A)",
        "tex": "les $A_{K,K'}$ forment",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "les $A^{\\natural}_{K,K'}$ forment",
        "note": "The groups of (8.3.1)-(8.3.3) are A^♮_{K,K'}; the print omits the handwritten ♮. The TeX keeps the printed reading.",
    },
    {
        "page": 417,
        "where": "after (8.3.3): «Comme les morphismes de transition dans le système inductif envisagé dans des immersions ouvertes»",
        "scan": "envisagé dans des immersions ouvertes",
        "tex": "envisagé dans des immersions ouvertes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "envisagé sont des immersions ouvertes",
        "note": "The clause has no verb: 'dans' is typed for 'sont'. The TeX keeps the printed reading.",
    },
    {
        "page": 418,
        "where": "9.1, l. 4: «deux Z-Modules constants tordus M et M' (5.5.2)»",
        "scan": "M̲ et M' (5.5.2) (only M is underlined)",
        "tex": "$\\underline{M}$ et $M'$ (5.5.2)",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$\\underline{M}$ et $\\underline{M}'$ (5.5.2)",
        "note": "Both are the twisted constant Z-Modules (underlined M̲' in (9.1.1)); the plain M, M' a line later are their values. The print omits the underline of M'. The TeX keeps the printed reading.",
    },
    {
        "page": 419,
        "where": "9.2, l. 4: «les éléments gx - x (u ∈ U, g ∈ I)»",
        "scan": "gx - x (u ∈ U, g ∈ I)",
        "tex": "($u \\in U$, $g \\in I$)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "($x \\in U$, $g \\in I$)",
        "note": "The variable is x, as in (9.2.1). The TeX keeps the printed u.",
    },
    {
        "page": 420,
        "where": "l. 1: «appliqué a la fois pour A_K et A'_K»",
        "scan": "appliqué a la fois",
        "tex": "appliqué a la fois",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "appliqué à la fois",
        "note": "Grave accent missing on à. The TeX keeps the printed reading.",
    },
    {
        "page": 420,
        "where": "before (9.2.5): «peut s'interprèter comme un homomorphisme canonique»",
        "scan": "peut s'interprèter (grave accent, the same stroke as in s'interprète at the foot of the page and in théorème, l. 1)",
        "tex": "peut s'interpréter comme",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "s'interpréter", "new": "s'interprèter"},
        "corrected": "s'interpréter",
        "note": "The print types è in the infinitive; the TeX silently corrects it to é. The fix restores the printed reading.",
    },
    {
        "page": 420,
        "where": "(9.2.7), first line",
        "scan": "W ≃ T_ℓ(T_o)(k̄)) ≃ M̌ ⊗ Z_ℓ(1) (two closing parentheses after k̄)",
        "tex": "T_{\\ell}(T_o)(\\overline{k}))",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "T_{\\ell}(T_o)(\\overline{k})",
        "note": "Unbalanced parentheses. The TeX keeps the printed reading.",
    },
    {
        "page": 420,
        "where": "(9.2.7), second line: T_o without prime",
        "scan": "W' ≃ T_ℓ(T_o(k̄))",
        "tex": "T_{\\ell}(T_o(\\overline{k}))",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "T_{\\ell}(T'_o(\\overline{k}))",
        "note": "W' comes from the special fibre T'_o (preceding sentence and (9.2.8)). The TeX keeps the printed T_o.",
    },
    {
        "page": 420,
        "where": "(9.2.7), second line: M' without check",
        "scan": "≃ M' ⊗ Z_ℓ(1) , (no handwritten check over M', unlike M̌ in the first line)",
        "tex": "\\simeq\\ M' \\otimes",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\simeq\\ \\check{M}' \\otimes",
        "note": "Since T'_o = D(M') (9.2.8), T_ℓ(T'_o)(k̄) ≃ M̌'⊗Z_ℓ(1), parallel to the first line; folio 421 continues with (M̌'⊗M̌)⊗Z_ℓ. The TeX keeps the printed M'.",
    },
]

texts = {}
for p in (416, 417, 418, 419, 420):
    with open(os.path.join(PAGES, "page_%d.tex" % p), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()

ok = True
for f in findings:
    src = texts[f["page"]]
    n_tex = src.count(f["tex"])
    if n_tex != 1:
        print("tex count", n_tex, f["page"], repr(f["tex"]))
        ok = False
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = src.count(old)
        print("fix old count", n, f["page"], repr(old))
        if n != 1 or "%%%%%%%%%%" in old:
            ok = False

if not ok:
    print("CHECK FAILED; not writing")
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for f in findings:
    k = "m" if f["kind"] == "misprint_in_print" else "n"
    c = counts.setdefault(f["page"], {"n": 0, "m": 0})
    c[k] += 1
print("; ".join("%d: %d/%d" % (p, counts.get(p, {"n": 0})["n"], counts.get(p, {"m": 0})["m"]) for p in (416, 417, 418, 419, 420)))
print("written", OUT)
