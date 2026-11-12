import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
BATCH = os.path.join(RUN, "b301_305")
OUT = os.path.join(RUN, "findings_301_305_recheck.json")

def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

findings = [
    # ---------------- page 301 ----------------
    F(301, "Remarque 5.7.10, first line",
      "l'hypothèse (A) peut-être remplacée par celle",
      r"l'hypothèse (A) peut-être remplacée par celle",
      "misprint_in_print", "medium", None,
      "The verb 'peut être' (pouvoir + être) is typed with the hyphen of the adverb 'peut-être'. The TeX keeps the printed reading.",
      corrected=r"l'hypothèse (A) peut être remplacée par celle"),
    F(301, "sentence after (5.8.1.1)",
      "la suite spectrale de Leray est contenu dans le",
      r"la suite spectrale de Leray est contenu dans le",
      "misprint_in_print", "medium", None,
      "The participle does not agree with 'la suite spectrale'. The TeX keeps the printed reading.",
      corrected=r"la suite spectrale de Leray est contenue dans le"),
    F(301, "(5.8.1.3), left-hand side",
      "Prim˙(T_{/S},Q_ℓ(j)  =  Ker (",
      r"\mathbb{Q}_\ell(j) \ = \ \mathrm{Ker}",
      "misprint_in_print", "high", None,
      "The parenthesis opened after Prim˙ is never closed in the print (only (j) is closed). The TeX keeps the printed reading.",
      corrected=r"\mathbb{Q}_\ell(j)) \ = \ \mathrm{Ker}"),
    F(301, "(5.8.1.3), end of the right-hand side",
      "Ker (H˙(T,Q_ℓ(j)) ⟶ H^o(S,R˙f_*Q_ℓ(j)) .",
      r"H^0(S,R^{\cdot}f_*\mathbb{Q}_\ell(j)) \quad .",
      "misprint_in_print", "high", None,
      "The parenthesis opened after 'Ker' is never closed in the print. The TeX keeps the printed reading.",
      corrected=r"H^0(S,R^{\cdot}f_*\mathbb{Q}_\ell(j))) \quad ."),

    # ---------------- page 302 ----------------
    F(302, "(5.8.1.6), target H^1(S,R˙⁻¹f_*Q_ℓ(j))",
      "R followed by the raised degree dot and the superscript -1; the dot sits at the top of the R (measured: its centre 21 px above the baseline, R 22 px high), exactly where the degree dot of R˙f_* in (5.8.1.3) and of Prim˙, H˙ sits, at the level of the superscript's baseline",
      r"\mathrm{R}\cdot^{-1}f_*",
      "formula", "medium",
      {"old": r"\mathrm{R}\cdot^{-1}f_*", "new": r"\mathrm{R}^{\cdot-1}f_*"},
      "The TeX sets a centred binary-operator dot on the main line (with spaces around it) and hangs the -1 on it. The print has the same raised degree dot that the file writes ^{\\cdot} everywhere else (R^{\\cdot}f_* in (5.8.1.3) on p. 301, \\mathrm{Prim}^{\\cdot}, \\mathrm{H}^{\\cdot}), followed by the superscript -1; it is not a baseline dot. Apply together with the SOURCE DEFECTS comment edit below. The misprint (dot for i) is listed separately."),
    F(302, "SOURCE DEFECTS comment, item 2",
      "see the (5.8.1.6) formula finding above",
      r"set \"R\cdot^{-1}f_*\" — a baseline dot where the degree index",
      "other", "medium",
      {"old": "set \"R\\cdot^{-1}f_*\" \u2014 a baseline dot where the degree index",
       "new": "set \"R^{\\cdot-1}f_*\" \u2014 the raised degree dot of R^{\\cdot}f_* in (5.8.1.3) where the degree index"},
      "Comment only: keeps item 2 in step with the (5.8.1.6) formula fix; apply the two together."),
    F(302, "diagram (5.8.2.1), label f of the diagonal X̃ → X",
      "f stands below and to the right of the diagonal shaft (glyph centre about 35 px below the line through the shaft)",
      r"\arrow[dl, \"f\"']",
      "other", "medium",
      {"old": "\\arrow[dl, \"f\"']", "new": "\\arrow[dl, \"f\"]"},
      "Placement only. For a down-left arrow tikz-cd sets an unmarked label on the lower-right side and a label with the swap mark ' on the upper-left side; the print has f on the lower-right side."),
    F(302, "diagram (5.8.2.1), label ν of the bottom arrow U → ℙ^1",
      "ν stands below the shaft",
      r"\arrow[l, \"\nu\"']",
      "other", "medium",
      {"old": "\\arrow[l, \"\\nu\"']", "new": "\\arrow[l, \"\\nu\"]"},
      "Placement only. For a leftward arrow tikz-cd sets an unmarked label below the shaft and a label with the swap mark ' above it; the print has ν below (α on the top arrow is above, and its \"\\alpha\"' is right)."),
    F(302, "5.8.2, second line",
      "un pinceau d'hyperplansdont l'élément générique",
      r"un pinceau d'hyperplansdont l'élément générique",
      "misprint_in_print", "high", None,
      "The word space is missing in the print (the s is struck heavily and 'dont' follows in the next character cell). The TeX keeps the printed reading.",
      corrected=r"un pinceau d'hyperplans dont l'élément générique"),
    F(302, "(5.8.1.6), source",
      "U^i : Prim(T_{/S},Q_ℓ(j))",
      r"\mathrm{Prim}(\mathrm{T}_{/\mathrm{S}}",
      "misprint_in_print", "low", None,
      "U^i is the composite (5.8.1.5), defined on Prim^i; the print drops the superscript of Prim. The TeX keeps the printed reading.",
      corrected=r"\mathrm{Prim}^i(\mathrm{T}_{/\mathrm{S}}"),
    F(302, "(5.8.1.6), target",
      "H^1(S,R˙⁻¹f_*Q_ℓ(j))",
      r"\mathrm{R}^{\cdot-1}f_*",
      "misprint_in_print", "medium", None,
      "The degree dot stands where the index i belongs: the target of U^i is E_2^{1,i-1} = H^1(S,R^{i-1}f_*Q_ℓ(j)) of (5.8.1.5). The TeX keeps the printed reading (its comment says so). 'tex' is the text after the formula fix above; the current file has \\mathrm{R}\\cdot^{-1}f_*.",
      corrected=r"\mathrm{R}^{i-1}f_*"),
    F(302, "(5.8.1.5), bottom node H^1(S,R^{i-1}_{f_*}Q_ℓ(j))",
      "f_* is typed at subscript level under R^{i-1}",
      r"\mathrm{R}^{i-1}_{f_*}",
      "misprint_in_print", "low", None,
      "Typing slip: f_* belongs on the line, as in R˙f_* (5.8.1.3) and R˙⁻¹f_* (5.8.1.6). The TeX keeps the printed reading.",
      corrected=r"\mathrm{R}^{i-1}f_*"),

    # ---------------- page 303 ----------------
    F(303, "diagram (5.8.3.1), label Grif of the diagonal",
      "Grif stands above and to the right of the diagonal shaft (glyph centre about 45 px above the line through the shaft)",
      r"\arrow[dr, \"\mathrm{Grif}\"']",
      "other", "medium",
      {"old": "\\arrow[dr, \"\\mathrm{Grif}\"']", "new": "\\arrow[dr, \"\\mathrm{Grif}\"]"},
      "Placement only. For a down-right arrow tikz-cd sets an unmarked label on the upper-right side and a label with the swap mark ' on the lower-left side; the print has Grif on the upper-right side."),
    F(303, "(5.8.2.2), left-hand side",
      "Prim˙(X̃|U/U,Q_ℓ(j)  = Ker(",
      r"\mathbb{Q}_\ell(j) = \mathrm{Ker}",
      "misprint_in_print", "high", None,
      "The parenthesis opened after Prim˙ is never closed in the print (as in (5.8.1.3)). The TeX keeps the printed reading.",
      corrected=r"\mathbb{Q}_\ell(j)) = \mathrm{Ker}"),
    F(303, "Démonstration of 5.8.2.3, last line",
      "est primitif rel. à ℙ^1α]",
      r"rel. à $\mathbb{P}^1\alpha$]",
      "misprint_in_print", "medium", None,
      "A stray α follows ℙ^1 inside the bracket. The TeX keeps the printed reading.",
      corrected=r"rel. à $\mathbb{P}^1$]"),
    F(303, "Démonstration of 5.8.2.3, last line",
      "⟹ α*f*(α) l'est rel. à U",
      r"\Longrightarrow \alpha^*f^*(\alpha)$",
      "misprint_in_print", "high", None,
      "The argument is x, as in (5.8.2.4) and in f*(x) just before. The TeX keeps the printed reading.",
      corrected=r"\Longrightarrow \alpha^*f^*(x)$"),

    # ---------------- page 304 ----------------
    F(304, "diagram (5.8.3.2), label α of the top arrow X̃|U → X̃",
      "α stands above the shaft",
      r"\arrow[l, \"\alpha\"]",
      "other", "medium",
      {"old": "\\arrow[l, \"\\alpha\"]", "new": "\\arrow[l, \"\\alpha\"']"},
      "Placement only. For a leftward arrow tikz-cd sets an unmarked label below the shaft; the print (and the STRUCTURE comment) has α above, which needs the swap mark '."),
    F(304, "diagram (5.8.3.2), label ν of the bottom arrow U → ℙ^1",
      "ν stands above the shaft",
      r"\arrow[l, \"\nu\"]",
      "other", "medium",
      {"old": "\\arrow[l, \"\\nu\"]", "new": "\\arrow[l, \"\\nu\"']"},
      "Placement only. For a leftward arrow tikz-cd sets an unmarked label below the shaft; the print (and the STRUCTURE comment) has ν above, which needs the swap mark '."),
    F(304, "(5.8.4.1), bottom node",
      "H^1(U,E^{n-1}ρ_*(Q_ℓ(j)) ≃",
      r"H^1(U,E^{n-1}\rho_*(\mathbb{Q}_\ell(j)) \;\simeq\;",
      "misprint_in_print", "medium", None,
      "Unbalanced parentheses: a stray '(' before Q_ℓ, against the notation E^{n-1}ρ_*Q_ℓ(j) of (5.8.4.2)-(5.8.4.4). The TeX keeps the printed reading.",
      corrected=r"H^1(U,E^{n-1}\rho_*\mathbb{Q}_\ell(j)) \;\simeq\;"),

    # ---------------- page 305 ----------------
    F(305, "(5.8.4.3), left-hand side",
      "ν*R^{n-1}ρ_*Q_ℓ(j)) ≃",
      r"\nu^*R^{n-1}\rho_*\mathbb{Q}_\ell(j)) \;\simeq\;",
      "misprint_in_print", "high", None,
      "The print has an extra closing parenthesis. The TeX keeps the printed reading.",
      corrected=r"\nu^*R^{n-1}\rho_*\mathbb{Q}_\ell(j) \;\simeq\;"),
    F(305, "line before (5.8.4.5)",
      "la flèche (qui n'est défini que grâce à l'hypothèse (A))",
      r"la flèche (qui n'est défini que grâce à l'hypothèse (A))",
      "misprint_in_print", "medium", None,
      "The participle does not agree with 'la flèche' (the sentence ends 'est injective'). The TeX keeps the printed reading.",
      corrected=r"la flèche (qui n'est définie que grâce à l'hypothèse (A))"),
]

# fix up the two "tex" fields written with escaped quotes in raw strings
for d in findings:
    d["tex"] = d["tex"].replace('\\"', '"')

ok = True
for d in findings:
    fx = d["fix"]
    if fx is None:
        continue
    path = os.path.join(BATCH, "page_%03d.tex" % d["page"])
    text = open(path, encoding="utf-8", newline="").read()
    n = text.count(fx["old"])
    print(d["page"], n, repr(fx["old"]))
    if n != 1:
        ok = False
    # never across a marker line
    if "%%%%%%%%%%" in fx["old"]:
        ok = False
        print("  marker in old!")
    # check the edit would not touch the marker
# apply all fixes on copies to make sure they chain
for page in (301, 302, 303, 304, 305):
    path = os.path.join(BATCH, "page_%03d.tex" % page)
    text = open(path, encoding="utf-8", newline="").read()
    for d in findings:
        if d["page"] == page and d["fix"]:
            assert text.count(d["fix"]["old"]) == 1, (page, d["fix"]["old"])
            text = text.replace(d["fix"]["old"], d["fix"]["new"])
print("all unique:", ok)
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(findings, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("written", OUT, len(findings))
