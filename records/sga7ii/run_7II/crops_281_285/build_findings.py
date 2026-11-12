import io
import json
import os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(RUN, 'b281_285')
OUT = os.path.join(RUN, 'findings_281_285_recheck.json')


def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 281 ----------------
    F(281, "5.2.2, '(muni de u)'",
      "(muni de u): only 'muni de' is underlined; the u (heavier type) stands outside the underline",
      r"(\underline{muni de u})",
      "underline", "high",
      {"old": r"(\underline{muni de u})", "new": r"(\underline{muni de} $u$)"},
      "The underline stops after 'de'. The fix also sets u in math, like the neighbouring $S$; "
      r"'(\underline{muni de} u)' would match the print equally."),
    F(281, "first display (projection formula)",
      "h_*(h*(m*(x)) = m*(x)h_*(1)",
      r"h_*(h^*(m^*(x)) =",
      "misprint_in_print", "high", None,
      "The print opens three parentheses after h_* and closes two. The TeX keeps the printed reading.",
      corrected=r"h_*(h^*(m^*(x))) ="),
    F(281, "5.2.1, parenthesis opened at '(de sorte que u s'obtient'",
      "... classe qui se trouve dans H²(IP , ℤ_ℓ(1)), et désignons par",
      r"\mathbb{Z}_{\ell}(1))$, et désignons par",
      "misprint_in_print", "medium", None,
      "The prose parenthesis '(de sorte que' is never closed: the two parentheses after (1) close "
      "ℤ_ℓ( and H²(. The TeX keeps the printed reading.",
      corrected=r"\mathbb{Z}_{\ell}(1))$), et désignons par"),
    F(281, "5.2.1, display defining L_S",
      "L_S : H^•(S,ℚ_ℓ(j) ⟶ H^{•+2}(S,ℚ_ℓ(j+1))",
      r"H^{\bullet}(S,\mathbb{Q}_{\ell}(j) \longrightarrow",
      "misprint_in_print", "high", None,
      "The source group lacks its closing parenthesis. The TeX keeps the printed reading.",
      corrected=r"H^{\bullet}(S,\mathbb{Q}_{\ell}(j)) \longrightarrow"),

    # ---------------- page 282 ----------------
    F(282, "(5.2.2.2), Tate twist of the target",
      "H^{2n-i+2}(S,ℚ_ℓ(j+2n-2i+2)).  (twist handwritten)",
      r"j+2n-2i+2",
      "misprint_in_print", "medium", None,
      "L raises the twist by 1 (5.2.1: H^•(S,ℚ_ℓ(j)) → H^{•+2}(S,ℚ_ℓ(j+1)); 5.2.2: L^i lands in "
      "ℚ_ℓ(i+j)), so L^{n-i+1} lands in ℚ_ℓ(j+n-i+1); the print doubles the shift. The TeX keeps "
      "the printed reading. Span does not overlap the parenthesis finding below.",
      corrected=r"j+n-i+1"),
    F(282, "(5.2.2.2), end of the formula",
      "Ker (L^{n-i+1} : ... ⟶ H^{2n-i+2}(S,ℚ_ℓ(j+2n-2i+2)).",
      r")).",
      "misprint_in_print", "high", None,
      "The parenthesis opened at 'Ker (' is never closed (two closing parentheses at the end). "
      "The TeX keeps the printed reading.",
      corrected=r")))."),
    F(282, "proof of Proposition 5.2.3, first line",
      "la formule de projection pour m : Y ⟶ X",
      r"$m : Y \longrightarrow X$",
      "misprint_in_print", "low", None,
      "The proposition names the inclusion τ : Y ↪ X and diagram (5.2.3.2) uses τ^*, τ_*; m is the "
      "name of the inclusion in 5.1. The TeX keeps the printed m.",
      corrected=r"$\tau : Y \longrightarrow X$"),

    # ---------------- page 283 ----------------
    F(283, "diagram (5.2.3.2), right-hand diagonal arrow τ_*",
      "arrow labelled τ_* drawn from H^{n+2}(X,ℚ_ℓ(j+1)) down-left, arrowhead at H^n(Y,ℚ_ℓ(j))",
      "H^{n+2}(X,\\mathbb{Q}_\\ell(j+1)) \\arrow[dl, \"\\tau_*\"] \\\\\n{} & H^n(Y,\\mathbb{Q}_\\ell(j))",
      "misprint_in_print", "high", None,
      "τ_* is the Gysin map H^n(Y,ℚ_ℓ(j)) → H^{n+2}(X,ℚ_ℓ(j+1)), as the display just below states, "
      "and the commutativity is L = τ_*τ^* (5.2.4.3). The print draws the head at H^n(Y). The TeX and "
      "its STRUCTURE comment keep the printed direction.",
      corrected="H^{n+2}(X,\\mathbb{Q}_\\ell(j+1)) \\\\\n{} & H^n(Y,\\mathbb{Q}_\\ell(j)) \\arrow[ur, \"\\tau_*\"']"),
    F(283, "sentence after the display τ_* : H^n(Y,...) ⟶ H^{n+2}(X,...)",
      "est la transposée d'une isomorphisme",
      r"d'une isomorphisme",
      "misprint_in_print", "high", None,
      "'isomorphisme' is masculine (same sentence: 'donc un isomorphisme'). The TeX keeps the printed "
      "reading.",
      corrected=r"d'un isomorphisme"),

    # ---------------- page 284 ----------------
    F(284, "(5.2.4.7), Tate twist of the target of the bilinear form",
      "H^{2n}(X,ℚ_ℓ(2j+2)",
      r"(2j+2",
      "misprint_in_print", "medium", None,
      "a ∈ H^{n-1}(X,ℚ_ℓ(j)) and L_X(b) ∈ H^{n+1}(X,ℚ_ℓ(j+1)) by (5.2.4.6), so a.L_X(b) lies in "
      "H^{2n}(X,ℚ_ℓ(2j+1)). The TeX keeps the printed 2j+2. Span does not overlap the parenthesis "
      "finding below.",
      corrected=r"(2j+1"),
    F(284, "(5.2.4.7), end of the first line",
      "H^{2n}(X,ℚ_ℓ(2j+2)  (one closing parenthesis)",
      ")\n\\end{equation*}\n\\begin{equation*}\n(a,b)",
      "misprint_in_print", "high", None,
      "The parenthesis opened at H^{2n}( is never closed. The TeX keeps the printed reading.",
      corrected="))\n\\end{equation*}\n\\begin{equation*}\n(a,b)"),

    # ---------------- page 285 ----------------
    F(285, "first line",
      "Mais par (5.2.5) et la formule de projection",
      r"Mais par (5.2.5)",
      "misprint_in_print", "medium", None,
      "The step a.L_X(b) = a.τ_*(τ^*(b)) uses L_X = τ_*τ^*, which is (5.2.4.3); 5.2.5 is the "
      "corollary stated below. The TeX keeps the printed reading.",
      corrected=r"Mais par (5.2.4.3)"),
    F(285, "Corollaire 5.2.5",
      "l'inclusion d'une section hyperplan lisse",
      r"section hyperplan lisse",
      "misprint_in_print", "high", None,
      "Elsewhere 'section hyperplane' (5.2.3, 5.2.4). The TeX keeps the printed reading.",
      corrected=r"section hyperplane lisse"),
    F(285, "diagram of the proof of 5.2.5, top-right node",
      "H^{n-i}(X,ℚ_ℓ(j+i+1))",
      r"H^{n-i}(X,\mathbb{Q}_\ell(j+i+1)) \arrow[d",
      "misprint_in_print", "high", None,
      "L_X^i maps H^{n-i}(X) to H^{n+i}(X), and τ^* lands in H^{n+i}(Y). The print has a minus; "
      "the TeX and its STRUCTURE comment keep it.",
      corrected=r"H^{n+i}(X,\mathbb{Q}_\ell(j+i+1)) \arrow[d"),
    F(285, "diagram of the proof of 5.2.5, bottom arrow L_Y^{i+1}",
      "hand-drawn wave ∼ under the label L_Y^{i+1}, above the arrow shaft (isomorphism mark)",
      r'\arrow[r, "L_Y^{i+1}"]',
      "missing", "medium",
      {"old": r'\arrow[r, "L_Y^{i+1}"]', "new": r'\arrow[r, "L_Y^{i+1}"{yshift=7pt}, "\sim"]'},
      "Folio 276 has the same hand-drawn wave between label and shaft (under g × ρ_i), and its TeX "
      r"writes it '\sim' with the label raised by {yshift=7pt}; the fix follows that. The proof rests "
      "on L_Y^{i+1} being an isomorphism (Y satisfies (LV) by 5.2.4). The STRUCTURE comment calls the "
      "stroke an ink artifact: apply together with the two comment edits below."),
    F(285, "STRUCTURE comment of the same diagram, list of absent features",
      "see the ∼ finding above",
      "no iso\n%   labels,",
      "other", "medium",
      {"old": "no iso\n%   labels,", "new": "no iso\n%   labels other than the $\\sim$ on arrow (4),"},
      r"Keeps the comment consistent with the \sim fix; apply together with it."),
    F(285, "STRUCTURE comment of the same diagram, last sentence",
      "see the ∼ finding above",
      "it is an ink artifact of the typescript, carries no label, and is not reproduced.",
      "other", "medium",
      {"old": "it is an ink artifact of the typescript, carries no label, and is not reproduced.",
       "new": "it is the isomorphism mark of arrow (4), read as $\\sim$ as on folio 276, and is set "
              "directly above the shaft, below the raised label."},
      r"Keeps the comment consistent with the \sim fix; apply together with it."),
]

# ---- checks ----
texts = {}
for p in range(281, 286):
    with io.open(os.path.join(BATCH, 'page_%d.tex' % p), encoding='utf-8', newline='') as fh:
        texts[p] = fh.read()

ok = True
for i, f in enumerate(findings):
    t = texts[f['page']]
    if f['fix'] is not None:
        old = f['fix']['old']
        n = t.count(old)
        marker_hit = any('scan idx' in line for line in old.split('\n'))
        print('fix  #%d p%d old count=%d%s' % (i, f['page'], n, ' MARKER!' if marker_hit else ''))
        if n != 1 or marker_hit:
            ok = False
    n = t.count(f['tex'])
    print('tex  #%d p%d count=%d' % (i, f['page'], n))
    if n < 1:
        ok = False

# applying all fixes per page must succeed sequentially
for p in range(281, 286):
    t = texts[p]
    for f in findings:
        if f['page'] == p and f['fix'] is not None:
            assert t.count(f['fix']['old']) == 1, (p, f['fix']['old'])
            t = t.replace(f['fix']['old'], f['fix']['new'])

print('ALL OK' if ok else 'PROBLEMS')
with io.open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
print('wrote', OUT, len(findings))
