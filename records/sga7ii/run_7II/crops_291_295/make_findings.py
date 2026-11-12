import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
PAGES = os.path.join(RUN, "b291_295")
OUT = os.path.join(RUN, "findings_291_295_recheck.json")

BRACE_OLD = (
    "\\begin{equation}\\tag{5.6.2.1}\n"
    "E_2^{o,q} \\; (=H^{o}(\\mathbb{P}^1,R^q\\rho_*\\mathbb{Q}_\\ell)) \\quad \\simeq \\quad H^q(X_{\\overline{\\eta}},\\mathbb{Q}_\\ell)\n"
    "\\end{equation}\n"
    "\\begin{equation}\\tag{5.6.2.2}\n"
    "E_2^{2,q}(=H^2(\\mathbb{P}^1,R^q\\rho_*\\mathbb{Q}_\\ell)) \\quad \\simeq \\quad H^q(X_{\\overline{\\eta}},\\mathbb{Q}_\\ell(-1))\n"
    "\\end{equation}\n"
    "\\begin{equation}\\tag{5.6.2.3}\n"
    "E_2^{p,q}(=H^p(\\mathbb{P}^1,R^q\\rho_*\\mathbb{Q}_\\ell)) \\;=\\; 0,\\; p \\neq 0,2 \\qquad .\n"
    "\\end{equation}"
)
BRACE_NEW = (
    "\\begin{align}\n"
    "&E_2^{o,q} \\; (=H^{o}(\\mathbb{P}^1,R^q\\rho_*\\mathbb{Q}_\\ell)) \\quad \\simeq \\quad H^q(X_{\\overline{\\eta}},\\mathbb{Q}_\\ell) \\tag{5.6.2.1}\\\\\n"
    "\\smash{\\left\\{\\rule[-5ex]{0pt}{10ex}\\right.}\\;&E_2^{2,q}(=H^2(\\mathbb{P}^1,R^q\\rho_*\\mathbb{Q}_\\ell)) \\quad \\simeq \\quad H^q(X_{\\overline{\\eta}},\\mathbb{Q}_\\ell(-1)) \\tag{5.6.2.2}\\\\\n"
    "&E_2^{p,q}(=H^p(\\mathbb{P}^1,R^q\\rho_*\\mathbb{Q}_\\ell)) \\;=\\; 0,\\; p \\neq 0,2 \\qquad . \\tag{5.6.2.3}\n"
    "\\end{align}"
)

findings = [
    # ---------------- page 291 ----------------
    {
        "page": 291,
        "where": "(5.6.2.1)-(5.6.2.3)",
        "scan": "one large hand-drawn left brace, pointing at (5.6.2.2), groups the three formulas; the numbers stand to the left of the brace",
        "tex": "three separate equation environments, no brace",
        "kind": "formula",
        "confidence": "high",
        "fix": {"old": BRACE_OLD, "new": BRACE_NEW},
        "note": "The brace is absent from the TeX. amsmath cannot let \\left\\{ span separately tagged rows, so the edit sets the three formulas in one align (keeping each \\tag) and draws the brace on the middle row with \\smash; the three rows are otherwise unchanged.",
    },
    {
        "page": 291,
        "where": "sentence after (5.6.2.5), '(On trouvera ... ci-dessous).'",
        "scan": "(On trouvera la valeur manquante E_2^{1,n-1} dans 5.7 ci-dessous). with the underline starting under 'On' and ending under 'ci-dessous'; neither parenthesis is underlined",
        "tex": "\\underline{(On trouvera la valeur manquante} ... \\underline{ci-dessous)}.",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{(On trouvera la valeur manquante} $E_2^{1,n-1}$ \\underline{dans} 5.7 \\underline{ci-dessous)}.",
            "new": "(\\underline{On trouvera la valeur manquante} $E_2^{1,n-1}$ \\underline{dans} 5.7 \\underline{ci-dessous}).",
        },
        "note": "Both parentheses stand outside the underline in the print (checked at 1.5x).",
    },
    {
        "page": 291,
        "where": "(5.6.2.5), left-hand side",
        "scan": "E_2^{2,n-1}(=H^2(ℙ^1,R^{n-1}ρ_*ℚ_ℓ)   ≃ ...: one closing parenthesis only, so '(=' is never closed",
        "tex": "E_2^{2,n-1}(=H^2(\\mathbb{P}^1,R^{n-1}\\rho_*\\mathbb{Q}_\\ell)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "E_2^{2,n-1}(=H^2(\\mathbb{P}^1,R^{n-1}\\rho_*\\mathbb{Q}_\\ell))",
        "note": "Unbalanced parenthesis in the print (checked at 2x); (5.6.2.4) has '))'. The TeX keeps the printed reading.",
    },
    # ---------------- page 292 ----------------
    {
        "page": 292,
        "where": "end of first paragraph",
        "scan": "résulte de la dégénerescence, compte tenu de 5.1.6. (no accent on the second e after n)",
        "tex": "la dégénerescence",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "la dégénérescence",
        "note": "Missing acute accent; the next paragraph and p. 295 print 'dégénérescence'. The TeX keeps the printed reading.",
    },
    {
        "page": 292,
        "where": "(5.6.3), first line, end",
        "scan": "= Ker(H^{n+1}(X̃,ℚ_ℓ) ⟶ H^o(ℙ^1,R^{n+1}ρ_*ℚ_ℓ): 'Ker(' is never closed",
        "tex": "R^{n+1}\\rho_*\\mathbb{Q}_{\\ell})",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "R^{n+1}\\rho_*\\mathbb{Q}_{\\ell}))",
        "note": "Missing closing parenthesis of Ker( in the print. The TeX keeps the printed reading.",
    },
    {
        "page": 292,
        "where": "(5.6.5), first summand",
        "scan": "Prim^{n-1}(X,ℚ_ℓ(-1) ⊕ H^{n-3}(X,ℚ_ℓ(-2)) ⊕ ...",
        "tex": "\\mathrm{Prim}^{n-1}(X,\\mathbb{Q}_{\\ell}(-1) \\oplus",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\mathrm{Prim}^{n-1}(X,\\mathbb{Q}_{\\ell}(-1)) \\oplus",
        "note": "Missing closing parenthesis in the print. The TeX keeps the printed reading.",
    },
    {
        "page": 292,
        "where": "(5.6.5), label over the arrow",
        "scan": "m*L+m*L²h_* (no '+' between L² and h_*; the 2 and the h stand in adjacent type cells)",
        "tex": "m^*L+m^*L^2h_*",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "m^*L+m^*L^2+h_*",
        "note": "The arrow is m*L on Prim^{n-1}, m*L² on H^{n-3} and h_* on H^{n-1}(Δ) (cf. (5.6.4) m*+h_*); the print drops the second '+'. The TeX keeps the printed reading.",
    },
    {
        "page": 292,
        "where": "(5.6.5), target",
        "scan": "H^{n+1}(X_η̄,ℚ_ℓ with no closing parenthesis; the line runs into the right margin and ends at the ℓ",
        "tex": "\\mathbb{Q}_{\\ell}\n\\end{equation}",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "\\mathbb{Q}_{\\ell})\n\\end{equation}",
        "note": "The scan is cropped close to the ink (about 20 px beyond the ℓ), so the parenthesis is most likely missing from the print rather than lost at the edge. The TeX keeps the printed reading.",
    },
    {
        "page": 292,
        "where": "unnumbered display after 'Or, la flèche'",
        "scan": "H^{n-3}(X,ℚ_ℓ(-2) —m*L²→ H^{n+1}(X_η̄,ℚ_ℓ)",
        "tex": "H^{n-3}(X,\\mathbb{Q}_{\\ell}(-2) \\xrightarrow",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "H^{n-3}(X,\\mathbb{Q}_{\\ell}(-2)) \\xrightarrow",
        "note": "Missing closing parenthesis in the print. The TeX keeps the printed reading.",
    },
    {
        "page": 292,
        "where": "last line",
        "scan": "Donc le noyau de (5.6.8) s'identifie (par pr_1 ⊕ pr_3) à",
        "tex": "noyau de (5.6.8)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "noyau de (5.6.5)",
        "note": "Wrong reference: the kernel meant is that of the arrow (5.6.5), whose source has the three summands to which pr_1 ⊕ pr_3 refers; 5.6.8 is the theorem on the next page. The TeX keeps the printed reading.",
    },
    # ---------------- page 293 ----------------
    {
        "page": 293,
        "where": "Remarque 5.6.7, end",
        "scan": "comme DELIGNE m'a expliqué; (semicolon)",
        "tex": "expliqué:",
        "kind": "punctuation",
        "confidence": "medium",
        "fix": {"old": "expliqué:", "new": "expliqué;"},
        "note": "Measured against the page's colons and semicolons: the lower mark is larger than the upper dot and descends below the baseline, as the semicolons of '(LV);' and '(5.4) ;' do; the colon of 'Supposons que :' has two equal dots above the baseline. A colon may have been intended.",
    },
    # ---------------- page 294 ----------------
    {
        "page": 294,
        "where": "'la première classe de Chern de ...'",
        "scan": "O_{X(1)}: '(1)' typed at subscript level with the X",
        "tex": "$\\underline{O}_{X(1)}$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$\\underline{O}_X(1)$",
        "note": "Typing slip; the sheaf is O_X(1), as printed in (5.6.8.1). The TeX keeps the printed reading.",
    },
    {
        "page": 294,
        "where": "after the display ν : U → ℙ^1",
        "scan": "Par 5.6.8.1 et.5.2.6, (a full stop in the type cell between 'et' and '5')",
        "tex": "et.5.2.6",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "et 5.2.6",
        "note": "The dot is lighter than the other full stops but sits centred in the space cell after 'et', so it is a struck key, not a speck. The TeX keeps the printed reading.",
    },
    # ---------------- page 295 ----------------
    {
        "page": 295,
        "where": "(5.6.8.8), source of the arrow",
        "scan": "H^j(ℙ^1, R^{n-2-i}ρ_*ℚ_ℓ)",
        "tex": "R^{n-2-i}\\rho_* \\mathbb{Q}_\\ell",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "R^{n-1-i}\\rho_* \\mathbb{Q}_\\ell",
        "note": "The degrees n-2-i and n-1+i differ by an odd number, so no power of ξ_X links them; the formula combines (5.6.8.3) (i ≥ 2) with (5.6.8.6) (i = 1), i.e. R^{n-1-i} → R^{n-1+i}. The TeX keeps the printed reading.",
    },
    {
        "page": 295,
        "where": "(5.6.8.8), label over the arrow",
        "scan": "ξ_X over ≃ (no exponent)",
        "tex": "\\xrightarrow{\\substack{\\xi_X \\\\ \\sim}}",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "\\xrightarrow{\\substack{\\xi_X^i \\\\ \\sim}}",
        "note": "R^{n-1-i} → R^{n-1+i} is cup product with ξ_X^i, as in (5.6.8.3). The TeX keeps the printed reading.",
    },
    {
        "page": 295,
        "where": "(5.6.8.8), target",
        "scan": "H^j(ℙ^1,R^{n-1+i}ℚ_ℓ): no ρ_*",
        "tex": "R^{n-1+i}\\mathbb{Q}_\\ell",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "R^{n-1+i}\\rho_*\\mathbb{Q}_\\ell",
        "note": "ρ_* omitted in the print. The TeX keeps the printed reading.",
    },
    {
        "page": 295,
        "where": "display d_2 : H^o(...) → H^2(...)",
        "scan": "H^2( ℙ^1,R^{i-1}, ρ_*ℚ_ℓ): a comma typed after R^{i-1}, under the superscript",
        "tex": "R^{i-1}, \\rho_*",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "R^{i-1}\\rho_*",
        "note": "Stray comma inside R^{i-1}ρ_* (checked at 4x). The TeX keeps the printed reading.",
    },
    {
        "page": 295,
        "where": "sentence before (5.6.8.10), target of ξ_X",
        "scan": "H^p( ℙ^1, ℝ^1ρ_*ℚ_ℓ): double-struck R (like the ℙ) with exponent 1",
        "tex": "\\mathbb{R}^1 \\rho_*",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "R^n \\rho_*",
        "note": "ξ_X maps R^{n-2}ρ_* to R^nρ_* (cf. (5.6.8.4)-(5.6.8.6)). The TeX keeps the printed reading.",
    },
]

# ---- checks: every fix old / every tex of a misprint occurs exactly once on its page
ok = True
for f in findings:
    path = os.path.join(PAGES, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        src = fh.read()
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = src.count(old)
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, f["page"], f["where"])
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in f["fix"]["new"]:
            ok = False
            print("MARKER TOUCHED", f["page"], f["where"])
    if f["kind"] == "misprint_in_print":
        n = src.count(f["tex"])
        if n != 1:
            ok = False
            print("MISPRINT TEX COUNT", n, f["page"], f["where"])
        if "corrected" not in f:
            ok = False
            print("NO CORRECTED", f["page"], f["where"])
    elif "corrected" in f:
        ok = False
        print("CORRECTED ON NON-MISPRINT", f["page"], f["where"])

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "PROBLEMS")
print("; ".join("%d: %d/%d" % (p, c[0], c[1]) for p, c in sorted(counts.items())))
