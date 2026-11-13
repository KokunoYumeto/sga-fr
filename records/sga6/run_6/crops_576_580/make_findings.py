import json, pathlib, sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b576_580"
OUT = RUN / "findings_576_580.json"
NL = "\n"

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 576 ----------------
add(576, "first display, c^i(E) in H^{2i}(T, Z_l(i))",
    "c^i(E) ∈ H^{2i}(T,Z_ℓ(i)) — the twist is the letter i (heavy ink fuses its dot with the stem, but it has the i's serif at x-height, not the flag of a typed 1; the DjVu witness agrees)",
    r"\mathbb Z_\ell(1)",
    "formula", "high",
    {"old": r"\mathbb Z_\ell(1)", "new": r"\mathbb Z_\ell(i)"},
    "The TeX reads the heavy i as the digit 1; c^i lands in H^{2i}(T,Z_l(i)), as in (7.13.0) and (7.13.1).")

add(576, "(7.13.0), the factor after the arrow",
    "Ĝ(H^{2*}(T,Z_ℓ(*)) = 1 + ... — only two closing parentheses after (*), so the parenthesis opened after Ĝ is never closed (both scans)",
    r"\widehat G\bigl(H^{2*}(T,\mathbb Z_\ell(*))\bigr)",
    "misprint_in_print", "high",
    {"old": r"\mathbb Z_\ell(*))\bigr)", "new": r"\mathbb Z_\ell(*))"},
    "Missing closing parenthesis in the print; the TeX silently adds it (\\bigr)). The fix restores the printed reading; the corrected reading is the current TeX.",
    corrected=r"\widehat G\bigl(H^{2*}(T,\mathbb Z_\ell(*))\bigr)")

add(576, "sentence after (7.13.0): (où l'objet but ... \"naïf\").",
    "(où l'objet but est un groupe par le produit, comme expliqué dans V 1, et où le K˙(T) est le K˙ \"naïf\"). — the whole remark stands in parentheses",
    "où l'objet but ... «~\\emph{naïf}~». — no parentheses",
    "missing", "high",
    {"old": r"où l'objet but est un groupe par le produit, comme expliqué dans V 1, et où le \(K^\bullet(T)\) est le \(K^\bullet\) «~\emph{naïf}~».",
     "new": r"(où l'objet but est un groupe par le produit, comme expliqué dans V 1, et où le \(K^\bullet(T)\) est le \(K^\bullet\) «~\emph{naïf}~»)."},
    "Both parentheses of the print are missing; one edit adds the pair.")

add(576, "(7.13.2), lower right corner",
    "K^{2i}(X_s, Z_ℓ(i))",
    r"K^{2i}(X_s,\mathbb Z_\ell(i))",
    "misprint_in_print", "high",
    None,
    "Typing error K for H: c^i takes values in H^{2i}(X_s, Z_l(i)) (cf. the top row, the following text and (7.13.4)). The TeX keeps the printed K.",
    corrected=r"H^{2i}(X_s,\mathbb Z_\ell(i))")

# ---------------- page 577 ----------------
add(577, "last line: trouve un carré commutatif (cf. 7.16) :",
    "(cf. 7.16) :",
    "(cf. 7.16)",
    "punctuation", "high",
    {"old": "(cf. 7.16)", "new": "(cf. 7.16) :"},
    "The colon that introduces the square (printed at the top of p. 578) is missing.")

add(577, "the mu_n square printed at the top of p. 578 (its TeX sits in page_577.tex, see the p. 578 marker finding): label of the right vertical arrow",
    "σ⁻¹ — hand-drawn σ with the raised -1, the same form the TeX reads \\sigma^{-1} in (7.13.2), in 'et où σ^{-1} est' (p. 576) and in 'l'homomorphisme σ^{-1} de spécialisation' (p. 578), which names this very arrow",
    r"""\arrow[d,"\sigma'"]""",
    "symbol", "medium",
    {"old": r"""\arrow[d,"\sigma'"]""", "new": r"""\arrow[d,"\sigma^{-1}"]"""},
    "Same glyph as the other three sigma^{-1} of pp. 576-578; a plain sigma (left labels) has no raised stroke.")

add(577, "the mu_n square at the top of p. 578 (TeX in page_577.tex): direction of the right vertical arrow",
    "arrow drawn downward, from H^{2i}(X_t̄, μ_n^{⊗i}) to H^{2i}(X_s̄, μ_n^{⊗i}), labelled σ⁻¹ (both scans)",
    r"""H^{2i}(X_{\bar t},\mu_n^{\otimes i}) \arrow[d,"\sigma'"] — downward, as printed""",
    "misprint_in_print", "medium",
    None,
    "sigma^{-1} maps H(X_s) to H(X_t) (defined on p. 576; upward in (7.13.2) and (7.13.9)), and the next sentence 'inverts' this arrow to obtain the downward ≀ of (7.13.4). The print draws it downward; the TeX keeps the printed direction. Corrected reading: the arrow goes up from the lower right corner, as in (7.13.2); written after the label fix above.",
    corrected=r"H^{2i}(X_{\bar t},\mu_n^{\otimes i})\\" + NL + r"""K^\bullet(X_{\bar s}) \arrow[r,"c^i"] &""" + NL + r"""H^{2i}(X_{\bar s},\mu_n^{\otimes i}) \arrow[u,"\sigma^{-1}"']""")

# ---------------- page 578 ----------------
add(578, "page start",
    "p. 578 opens with the unnumbered square K˙(X_t̄) → H^{2i}(X_t̄, μ_n^{⊗i}), K˙(X_s̄) → H^{2i}(X_s̄, μ_n^{⊗i}) followed by ','; p. 577 ends with 'trouve un carré commutatif (cf. 7.16) :' and blank space (both scans)",
    "the square (\\[ \\begin{tikzcd} ... \\;, \\]) stands under the folio-577 marker, as the last lines (7-15) of page_577.tex",
    "marker", "high",
    None,
    "Page 578 really begins at the \\[ that opens the mu_n square: move the folio-578 marker up to its own line between '(cf. 7.16)' and that \\[ (a display at the top of a page, which the script did not move).")

add(578, "(7.13.4), right vertical arrow",
    "≀ (vertical tilde) beside the arrow",
    r"""\arrow[d,"\sim"']""",
    "symbol", "low",
    {"old": r"""\arrow[d,"\sim"']""", "new": r"""\arrow[d,"\wr"']"""},
    "Same rendering as the applied p. 388 fix (\\wr); elsewhere the volume mostly writes \\sim on vertical arrows.")

# ---------------- page 579 ----------------
add(579, "page start",
    "p. 579 opens with 'K˙(T) et la filtration par le degré sur le deuxième membre ...'; p. 578 ends with '(Le fait que (7.13.0) est compatible avec la λ-filtration sur' (both scans)",
    "'\\(K^\\bullet(T)\\) et la' is the end of the last line of page_578.tex, above the folio-579 marker",
    "marker", "high",
    None,
    "Page 579 really begins at '\\(K^\\bullet(T)\\) et la': move the folio-579 marker up to its own line between '\\(\\lambda\\)-filtration sur' and '\\(K^\\bullet(T)\\) et la'.")

add(579, "(7.13.8), the coefficient",
    "cℓ(x^{(i)}) = (1/(-1)^{i-1}(i-1)!) ψ_i(x^{(i)}) — inline slash fraction in parentheses",
    r"\frac{1}{(-1)^{i-1}(i-1)!}\,\psi_i(x^{(i)})",
    "formula", "medium",
    {"old": r"\frac{1}{(-1)^{i-1}(i-1)!}", "new": r"(1/(-1)^{i-1}(i-1)!)"},
    "The TeX stacks the coefficient with \\frac and drops the print's parentheses and slash.")

add(579, "(7.13.9), label of the right (upward) arrow",
    "σ⁻¹ — the same hand-drawn form as the right label of (7.13.2), which the TeX writes \\sigma^{-1}; it is the same map H(X_s) → H(X_t)",
    r"""\arrow[u,"\sigma'"]""",
    "symbol", "high",
    {"old": r"""\arrow[u,"\sigma'"]""", "new": r"""\arrow[u,"\sigma^{-1}"]"""},
    "")

add(579, "between (7.13.9) and (7.13.10)",
    "nothing between the two diagrams: (7.13.9) ends with ',' and (7.13.10) follows after blank space (both scans)",
    "et",
    "extra", "high",
    {"old": r"\end{equation}" + NL + "et" + NL + r"\begin{equation}", "new": r"\end{equation}" + NL + r"\begin{equation}"},
    "The TeX adds the word 'et' between the diagrams.")

add(579, "(7.13.10), right vertical arrow",
    "≀ (vertical tilde) beside the arrow",
    r"""\arrow[d,"\sim"]""",
    "symbol", "low",
    {"old": r"""\arrow[d,"\sim"]""", "new": r"""\arrow[d,"\wr"]"""},
    "As the (7.13.4) finding on p. 578.")

add(579, "every 'cl' of 7.13.7-7.13.12 (pp. 579-580)",
    "cℓ — c (typed, or handwritten as in (7.13.8) and cℓ(Z)) followed by the hand-drawn script ℓ, the same ℓ as in ℓ-adique",
    r"\operatorname{cl}",
    "symbol", "medium",
    None,
    "Convention of these pages, reported once and not itemized: all 12 printed cℓ are \\operatorname{cl} in the TeX: page_579.tex lines 5 (7.13.7), 11 (7.13.8), 17, 19 (7.13.9), 27, 29 (7.13.10); page_580.tex lines 3 ('l'homomorphisme cl'), 6, 8 (7.13.12), 13 (cl(Z), cl(Z_t), cl(Z_s)). Suggested: \\operatorname{cl} -> \\operatorname{c\\ell} at these places.")

# ---------------- page 580 ----------------
add(580, "line 2: que ce trouve défini naturellement",
    "ce trouve",
    "ce trouve",
    "misprint_in_print", "high",
    None,
    "Typing error 'ce' for 'se'; the TeX keeps the printed reading.",
    corrected="se trouve")

add(580, "end of the sentence on sigma: dans X (cf. 7.15)).",
    "(cf. 7.15)). — one closing parenthesis too many; no parenthesis is open earlier in the sentence (both scans)",
    "(cf. 7.15)).",
    "misprint_in_print", "medium",
    None,
    "Extra closing parenthesis in the print; the TeX keeps it.",
    corrected="(cf. 7.15).")

add(580, "page end",
    "p. 580 ends with 'zéro en cycles rationnellement équivalents à zéro (X étant projectif sur S),'; p. 581 opens with 'on peut dans ce diagramme remplacer les Z^i par les A^i' (both scans)",
    "'on' is the last word of page_580.tex, above the folio-581 marker",
    "marker", "high",
    None,
    "Page 581 really begins at that 'on': move the folio-581 marker up to its own line before it (after '(\\(X\\) étant projectif sur \\(S\\)),').")

# ---------------- checks ----------------
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    text = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = text.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", d["page"])
for d in F:
    if d["kind"] == "misprint_in_print" and "corrected" not in d:
        ok = False
        print("MISSING corrected", d["page"], d["where"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
cnt = {}
for d in F:
    c = cnt.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "PROBLEMS", len(F), cnt)
