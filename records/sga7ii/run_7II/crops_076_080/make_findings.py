import json
import os
import sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
BATCH = os.path.join(RUN, "b076_080")
OUT = os.path.join(RUN, "findings_076_080.json")

NL = "\n"
F = []

# ---------------- page 76 ----------------
F.append({
    "page": 76,
    "where": "Théorème 3.3 (iii), label of the first formula 'η^m = cℓ(α) + cℓ(β)'",
    "scan": "(a)    η^m = cℓ(α) + cℓ(β)",
    "tex": r"\begin{equation*}" + NL + r"\eta^{m} = c\ell(\alpha) + c\ell(\beta)" + NL + r"\end{equation*}",
    "kind": "missing",
    "confidence": "high",
    "fix": {"old": r"\begin{equation*}" + NL + r"\eta^{m}",
            "new": r"\begin{equation*}\tag{a}" + NL + r"\eta^{m}"},
    "note": "The print labels the three formulas of (iii) (a), (b), (c); the TeX gives them as unlabelled equation* displays. The labels are cited as 'Formule (a)' on p. 76, 'Formule (b)', 'Formule (c)', 'Les formules (b)' on p. 77 and '3.3 (iii) b' on p. 80. amsmath accepts \\tag in equation*."
})
F.append({
    "page": 76,
    "where": "Théorème 3.3 (iii), label of the second formula (the brace 'pour m pair : ... / pour m impair : ...')",
    "scan": "(b) { pour m pair : ... ; pour m impair : ...",
    "tex": r"\begin{equation*}" + NL + r"\left\{ \begin{array}{l}",
    "kind": "missing",
    "confidence": "high",
    "fix": {"old": r"\begin{equation*}" + NL + r"\left\{",
            "new": r"\begin{equation*}\tag{b}" + NL + r"\left\{"},
    "note": "Label (b) printed before the brace; absent in the TeX. See the finding for (a)."
})
F.append({
    "page": 76,
    "where": "Théorème 3.3 (iii), label of the third formula 'η.(cℓ(α) - cℓ(β)) = 0.'",
    "scan": "(c)  η.(cℓ(α) - cℓ(β)) = 0.",
    "tex": r"\begin{equation*}" + NL + r"\eta.(c\ell(\alpha) - c\ell(\beta)) = 0." + NL + r"\end{equation*}",
    "kind": "missing",
    "confidence": "high",
    "fix": {"old": r"\begin{equation*}" + NL + r"\eta.(",
            "new": r"\begin{equation*}\tag{c}" + NL + r"\eta.("},
    "note": "Label (c) absent in the TeX. See the finding for (a)."
})
F.append({
    "page": 76,
    "where": "Théorème 3.3 (iii), number of the display 'Z_ℓ^{Z(X)} → R^n p_* Z_ℓ(m)'",
    "scan": "(3.2.1)      Z_ℓ^{Z(X)} ----> R^n p_* Z_ℓ(m)  (checked at 2x)",
    "tex": r"\tag{3.2.1}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\tag{3.3.1}",
    "note": "Wrong formula number: (3.2.1) is already the map cℓ : Z(X) → R^n p_* Z_ℓ(m) of 3.2 (p. 75), from which this display is 'l'application déduite'; the proof cites the display as 3.3.1 ('Que 3.3.1 soit un isomorphisme', p. 77). The reference '(3.2.1)' in 'l'application déduite de (3.2.1)' is right and stays. The TeX keeps the printed reading."
})
F.append({
    "page": 76,
    "where": "Formule (a), ambient space of the quadric 'Σ_0^m x_i x_{i+m+1} = 0 dans P^{m+1}(k)'",
    "scan": "Σ_0^m x_i x_{i+m+1} = 0 dans IP^{m+1}(k)  (checked at 2x)",
    "tex": r"\mathbb{P}^{m+1}(k)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\mathbb{P}^{2m+1}(k)",
    "note": "Wrong exponent: the equation uses the 2m+2 coordinates x_0, ..., x_{2m+1} (the generatrix D_2 on p. 77 is cut out by x_{2m+1} = 0), and a quadric of dimension n = 2m lies in P^{n+1} = P^{2m+1}. The TeX keeps the printed reading."
})

# ---------------- page 77 ----------------
F.append({
    "page": 77,
    "where": "Formule (c), 'il suffit d'après (ii) de prouver que η^m.(cℓ(α)-cℓ(β) = 0'",
    "scan": "η^m.(cℓ(α)-cℓ(β) = 0.  (checked at 4x)",
    "tex": r"\eta^{m}.(c\ell(\alpha)-c\ell(\beta) = 0",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\eta^{m}.(c\ell(\alpha)-c\ell(\beta)) = 0",
    "note": "The parenthesis opened before cℓ(α) is never closed. The TeX keeps the printed reading."
})
F.append({
    "page": 77,
    "where": "Formule (c), 'En effet, Tr(η^m(cℓ(α)-cℓ(β)) = ...'",
    "scan": "Tr(η^m(cℓ(α)-cℓ(β)) = Tr(cℓ(α)^2-cℓ(β)^2)=0.  (two closing parentheses after β; checked at 4x)",
    "tex": r"\mathrm{Tr}(\eta^{m}(c\ell(\alpha)-c\ell(\beta))",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\mathrm{Tr}(\eta^{m}(c\ell(\alpha)-c\ell(\beta)))",
    "note": "The closing parenthesis of Tr( is missing. The TeX keeps the printed reading."
})
F.append({
    "page": 77,
    "where": "Vérification, line 'm pair', first term of the trace",
    "scan": "tr(cℓ(α^2)+ 2cℓ(α)cℓ(β) + cℓ(β)^2)  (square inside the parenthesis; checked at 2x)",
    "tex": r"c\ell(\alpha^{2})",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"c\ell(\alpha)^{2}",
    "note": "The line expands (cℓ(α) + cℓ(β))^2; the next line writes cℓ(α)^2, and α, a section of Z(X), has no square. The TeX keeps the printed reading."
})
F.append({
    "page": 77,
    "where": "Vérification, line 'm pair : 2 = tr(η^2) = ...'",
    "scan": "m pair : 2 = tr(η^2) = ...  (exponent 2; checked at 2x)",
    "tex": r"$m$ pair : $2 = \mathrm{tr}(\eta^{2})",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"$m$ pair : $2 = \mathrm{tr}(\eta^{2m})",
    "note": "Wrong exponent: the verification squares formula (a), η^m = cℓ(α) + cℓ(β), so the left side is tr((η^m)^2) = tr(η^n) = 2, the degree of the quadric; tr(η^2) is the right value only for m = 1. Same in the line 'm impair'. Only the exponent changes. The TeX keeps the printed reading."
})
F.append({
    "page": 77,
    "where": "Vérification, line 'm impair : 2 = tr(η^2) = ...'",
    "scan": "m impair : 2 = tr(η^2) = Tr(cℓ(α)^2 + ...",
    "tex": r"impair : $2 = \mathrm{tr}(\eta^{2})",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"impair : $2 = \mathrm{tr}(\eta^{2m})",
    "note": "As in the line 'm pair': the trace is that of (η^m)^2 = η^{2m}. The TeX keeps the printed reading."
})

# ---------------- page 79 ----------------
F.append({
    "page": 79,
    "where": "end of the diagram (3.6.1) X^o → X ← Y over S",
    "scan": "full stop on the baseline of S, to the right of the diagram",
    "tex": r"{} \end{tikzcd}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": {"old": r"{} \end{tikzcd}",
            "new": r"{} \end{tikzcd}\quad ."},
    "note": "The structure comment records the printed full stop, but the diagram code omits it."
})
F.append({
    "page": 79,
    "where": "paragraph after (3.6.3), 'Pour r = 2m + 1, r_{2m}(η^m) = η^m'",
    "scan": "Pour  r = 2m + 1,  r_{2m}(η^m) = η^m  (checked at 1.3x)",
    "tex": r"Pour $r = 2m + 1$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"Pour $n = 2m + 1$",
    "note": "Wrong letter: this is the case n odd, after 'Pour n = 2m' in the sentence before; r is the name of the restriction maps r_i. The TeX keeps the printed reading."
})
F.append({
    "page": 79,
    "where": "same paragraph, 'Par dualité, ou à l'aide de 3.5.3'",
    "scan": "Par dualité, ou à l'aide de 3.5.3, on montre de même",
    "tex": "3.5.3",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "3.6.3",
    "note": "Wrong reference number: 3.5 has no numbered formula; the computation of R^i f_* Z_ℓ uses the exact sequence (3.6.3), as that of R^i f_! Z_ℓ used (3.6.2). The TeX keeps the printed reading."
})
F.append({
    "page": 79,
    "where": "same paragraph, 'pour n impair, c'est un isomorphisme pour i ≠ n-1'",
    "scan": "pour n impair, c'est un isomorphisme pour i ≠ n-1.",
    "tex": r"pour $i \neq n-1$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"pour $i \neq n-1,2n$",
    "note": "Incomplete exception list: for every n, r_{2n} : R^{2n}p_*Z_ℓ = Z_ℓ(-n) → R^{2n}q_*Z_ℓ = 0 (Y has dimension n-1) is not an isomorphism; the n even case says 'i ≠ n,2n', and the conclusion R^{2n}f_!Z_ℓ ≠ 0 for both parities needs it. The slip may be the author's rather than the typist's. The TeX keeps the printed reading."
})


def page_text(p):
    with open(os.path.join(BATCH, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
        return fh.read()


ok = True
for f in F:
    t = page_text(f["page"])
    if "\r" in t:
        print("CRLF in page", f["page"])
    n = t.count(f["tex"])
    if n != 1:
        print("TEX count", n, "page", f["page"], repr(f["tex"]))
        ok = False
    if f["fix"] is not None:
        c = t.count(f["fix"]["old"])
        if c != 1:
            print("OLD count", c, "page", f["page"], repr(f["fix"]["old"]))
            ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("marker in old", f["page"])
            ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print("no corrected", f["where"])
        ok = False

if not ok:
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
cnt = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in (76, 77, 78, 79, 80):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("written", OUT, len(F))
