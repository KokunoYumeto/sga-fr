import json, os
RUN = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7II"
OUT = os.path.join(RUN, "findings_416_420_recheck.json")
BS = "\\"

def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d

findings = [
# ---------------- page 416 ----------------
F(416, "(NB. ...) line after (4.1.5)",
  "converge dans Q_p(\u03be_p).) -- plain typed Q, without the second stroke of the double-struck Q in (4.1.1), (4.1.2), (4.1.4)",
  r"$\mathbb Q_p(\xi_p)$.)", "font", "medium",
  {"old": r"$\mathbb Q_p(\xi_p)$.)", "new": r"$Q_p(\xi_p)$.)"},
  r"The typist's plain Q (clean impression, no stroke lost). Same as (4.1.6) and p. 418 (4.4.1): apply the three together or none; the corrected edition can keep \mathbb Q."),
F(416, "(4.1.6)",
  "E(X) = exp(...) \u2208 Q_p[[X]] -- plain typed Q",
  r"\in\mathbb Q_p[[X]]", "font", "medium",
  {"old": r"\in\mathbb Q_p[[X]]", "new": r"\in Q_p[[X]]"},
  "Plain Q as in the NB line above (the Z of Z_p[[X]] in the next line is double-struck)."),
F(416, "line after (4.1.6): 'qui, ... miracle'",
  "qui, oh miracle, se trouve dans",
  "qui, \u00f4 miracle, se trouve dans", "word", "high",
  {"old": "qui, \u00f4 miracle,", "new": "qui, oh miracle,"},
  "The print has two letters after 'qui,': o and h. The second rises to full ascender height (as the l of 'miracle' and the d of 'dans'; an n would stop at x-height) and has the shape of the h in 'Teichm\u00fcller'. No circumflex."),
F(416, "(4.2.1)",
  "\u0398(X) = \u03a3 B_nX^n -- bare sum sign; the n below is the subscript of B",
  r"\Theta(X)=\sum_nB_nX^n", "formula", "high",
  {"old": r"\sum_nB_nX^n", "new": r"\sum B_nX^n"},
  "Summation index added by the TeX; the print has none."),
F(416, "(4.2.1)",
  "B_o = 1  A_1 = \u03c0",
  r"B_0=1\quad A_1=\pi", "misprint_in_print", "high",
  None,
  "The TeX keeps the printed A_1. The coefficients of \u0398 are B_n, and B_1 = \u03c0 (\u0398(X) = E(\u03c0X)). The print also has no comma after B_o = 1; the TeX follows it.",
  corrected=r"B_1=\pi"),
F(416, "(4.2.2)",
  "une racine p'i\u00e8me primitive de l'unit\u00e9.",
  r"\uline{une racine $p$'i" + "\u00e8me primitive de l'unit\u00e9.}", "misprint_in_print", "medium",
  None,
  "The TeX keeps the printed apostrophe; (4.1.3) prints 'p-i\u00e8me'.",
  corrected="$p$-i\u00e8me"),
F(416, "(4.2.3), 'dans W(F_{q^a})'",
  "the W is the double-struck typewriter W (left stroke doubled), like the double-struck F beside it",
  r"dans $W(\mathbb F_{q^a})\subset\Omega$", "font", "medium",
  {"old": r"dans $W(", "new": r"dans $\mathbb W("},
  "Same glyph twice on p. 417 (t \u2208 W(F_{q^a}), Tr_{W(F_{q^a})/Z_p}); apply the three together. The corrected edition may keep plain W."),
F(416, "(4.2.3), 'dans W(F_{q^a})'",
  "W(F_{q^a})",
  r"W(\mathbb F_{q^a})", "misprint_in_print", "medium",
  None,
  "The TeX keeps the printed q^a. t = t^{p^a} puts t in W(F_{p^a}); Corollary 4.3 has F_{p^a}, and the trace in the proof (p. 417) is right only over W(F_{p^a}). Same misprint twice on p. 417.",
  corrected=r"\mathbb F_{p^a}"),
# ---------------- page 417 ----------------
F(417, "(4.2.3.1), exponent on the right",
  "(\u0398(X))^{\u03a3_{j=0}^{a-1} t^j}",
  r"(\Theta(X))^{\sum_{j=0}^{a-1}t^j}", "misprint_in_print", "high",
  None,
  "The TeX keeps the printed t^j. The exponent is the sum of the t^{p^j}, as in the display just above and in the proof.",
  corrected=r"\sum_{j=0}^{a-1}t^{p^j}"),
F(417, "D\u00e9monstration, line 1",
  "Compte tenu de ce qui E(X) \u2208 Z_p[[X]]",
  "Compte tenu de ce qui", "misprint_in_print", "high",
  None,
  "The TeX keeps the printed 'ce qui'; the construction is 'compte tenu de ce que'.",
  corrected="ce que"),
F(417, "'sont les conjugu\u00e9s de t \u2208 W(F_{q^a})'",
  "double-struck W (as on p. 416)",
  r"$t\in W(\mathbb F_{q^a})$", "font", "medium",
  {"old": r"$t\in W(", "new": r"$t\in\mathbb W("},
  "See p. 416 (4.2.3); apply with the other two."),
F(417, "'sont les conjugu\u00e9s de t \u2208 W(F_{q^a})'",
  "W(F_{q^a})",
  r"W(\mathbb F_{q^a})", "misprint_in_print", "medium",
  None,
  "The TeX keeps the printed q^a; see p. 416 (4.2.3).",
  corrected=r"\mathbb F_{p^a}"),
F(417, "display \u03a3 t^{p^j} = Tr_{W(F_{q^a})/Z_p}(t)",
  "double-struck W in the subscript of Tr",
  r"\operatorname{Tr}_{W(\mathbb F_{q^a})/\mathbb Z_p}(t)", "font", "medium",
  {"old": r"\operatorname{Tr}_{W(", "new": r"\operatorname{Tr}_{\mathbb W("},
  "See p. 416 (4.2.3); apply with the other two."),
F(417, "display \u03a3 t^{p^j} = Tr_{W(F_{q^a})/Z_p}(t)",
  "Tr_{W(F_{q^a})/Z_p}",
  r"\operatorname{Tr}_{W(\mathbb F_{q^a})/\mathbb Z_p}", "misprint_in_print", "medium",
  None,
  "The TeX keeps the printed q^a; the sum of the a conjugates is the trace from W(F_{p^a}). See p. 416 (4.2.3).",
  corrected=r"\mathbb F_{p^a}"),
# ---------------- page 418 ----------------
F(418, "(4.4.1)",
  "\u03c4 \u2208 Gal ( K/Q_p(\u03be_p)) -- plain typed Q (the Q_p(\u03be_p) of 4.4, (4.4.0) and of the two Gal(K/Q_p(\u03be_p)) after (4.4.4) are double-struck)",
  r"\tau\in\Gal(K/\mathbb Q_p(\xi_p))", "font", "medium",
  {"old": r"\tau\in\Gal(K/\mathbb Q_p(\xi_p))", "new": r"\tau\in\Gal(K/Q_p(\xi_p))"},
  "Plain Q as on p. 416 (twice): apply the three together or none."),
F(418, "(4.4.2)",
  "Soit F(X) = \u03a3 A_W X^W -- bare sum sign; capital W (cap height, unlike the small w of (4.0.8) on p. 415)",
  r"F(X)=\sum_wA_wX^w", "formula", "high",
  {"old": r"F(X)=\sum_wA_wX^w", "new": r"F(X)=\sum A_WX^W"},
  "Two differences in one edit: the summation index the TeX adds, and the case of the index letter. From (4.4.2) to the end of p. 419 the print writes the multi-index as capital W; later pages of the TeX (A_WX_0X^W, X_1^{W_1}) already follow the print."),
F(418, "line after (4.4.2): 'v\u00e9rifient A_W^q = A_W'",
  "A_W^q = A_W (capital W)",
  r"$A_w^q=A_w$", "formula", "high",
  {"old": r"$A_w^q=A_w$", "new": r"$A_W^q=A_W$"},
  "Capital W as in (4.4.2)."),
F(418, "line before (4.4.3): '(4.1.0) de X'",
  "compte tenu de la d\u00e9finition (4.1.0) de X) -- typed capital X",
  "(compte tenu de la d\u00e9finition (4.1.0) de $X$)", "misprint_in_print", "medium",
  None,
  "The TeX keeps the printed X. (4.1.0) defines the character \u03c7, which p. 415 prints as a Greek chi.",
  corrected=r"$\chi$"),
F(418, "(4.4.3), second line",
  "\u03a0_W \u03a0_{j=0}^{ord(q^\u03bd)-1} \u0398(A_W^{p^j} X_o^{p^j} X^{p^j W}) -- capital W",
  r"\prod_w\prod_{j=0}^{...}\Theta\!\left(A_w^{p^j}X_0^{p^j}X^{p^jw}\right)", "formula", "high",
  {"old": r"\prod_w\prod_{j=0}^{\operatorname{ord}(q^\nu)-1}" + "\n" + r"\Theta\!\left(A_w^{p^j}X_0^{p^j}X^{p^jw}\right)",
   "new": r"\prod_W\prod_{j=0}^{\operatorname{ord}(q^\nu)-1}" + "\n" + r"\Theta\!\left(A_W^{p^j}X_0^{p^j}X^{p^jW}\right)"},
  "Capital W (three times) as in (4.4.2)."),
F(418, "(4.4.4)",
  "H(X) = \u03a0_W \u0398 (A_W X_o X_1^{W_1} ... X_{n+2}^{W_{n+2}}) . -- capital W",
  r"H(X)=\prod_w \Theta\!\left(A_wX_0X_1^{w_1}\cdots X_{n+2}^{w_{n+2}}\right)", "formula", "high",
  {"old": r"H(X)=\prod_w" + "\n" + r"\Theta\!\left(A_wX_0X_1^{w_1}\cdots X_{n+2}^{w_{n+2}}\right)",
   "new": r"H(X)=\prod_W" + "\n" + r"\Theta\!\left(A_WX_0X_1^{W_1}\cdots X_{n+2}^{W_{n+2}}\right)"},
  "Capital W (four times) as in (4.4.2)."),
# ---------------- page 419 ----------------
F(419, "first display, H^{\u03c4^j}(X)",
  "\u03a0_W \u0398 (A_W^{\u03c4^j} X_o X_1^W ... X_{n+2}^{W_{n+2}}) . -- capital W",
  r"\prod_w \Theta\!\left(A_w^{\tau^j}X_0X_1^{w}\cdots X_{n+2}^{w_{n+2}}\right)", "formula", "high",
  {"old": r"\prod_w" + "\n" + r"\Theta\!\left(A_w^{\tau^j}X_0X_1^{w}\cdots" + "\n" + r"X_{n+2}^{w_{n+2}}\right)",
   "new": r"\prod_W" + "\n" + r"\Theta\!\left(A_W^{\tau^j}X_0X_1^{W}\cdots" + "\n" + r"X_{n+2}^{W_{n+2}}\right)"},
  "Capital W as on p. 418. The edit keeps the printed X_1^W without index (misprint, next finding)."),
F(419, "first display, X_1^W",
  "X_1^W (no index 1 under the W)",
  r"X_1^{w}", "misprint_in_print", "high",
  None,
  "The TeX keeps the missing index. (4.4.4) has X_1^{W_1}. Reading after the case edit above: X_1^{W} becomes X_1^{W_1}.",
  corrected=r"X_1^{W_1}"),
F(419, "'Compte tenu de ce que A_W^{\u03c4^j} = A_W^{p^j}'",
  "A_W^{\u03c4^j} = A_W^{p^j} (capital W)",
  r"$A_w^{\tau^j}=A_w^{p^j}$", "formula", "high",
  {"old": r"$A_w^{\tau^j}=A_w^{p^j}$", "new": r"$A_W^{\tau^j}=A_W^{p^j}$"},
  "Capital W as on p. 418."),
F(419, "(4.5.4)",
  "= ord ( \u03a3 B_U X^U) . -- bare sum sign",
  r"\operatorname{ord}\!\left(\sum_U B_UX^U\right)", "formula", "high",
  {"old": r"\left(\sum_U B_UX^U\right)", "new": r"\left(\sum B_UX^U\right)"},
  "Summation index added by the TeX; the U below is the subscript of B."),
# ---------------- page 420 ----------------
F(420, "(4.5.5), second line",
  "\u03a8_k (\u03a3 B_UX^U) = \u03a3 B_{kU}X^U . -- bare sum signs",
  r"\psi_k\!\left(\sum_U B_UX^U\right)&=\sum_U B_{kU}X^U.", "formula", "high",
  {"old": r"\psi_k\!\left(\sum_U B_UX^U\right)&=\sum_U B_{kU}X^U.",
   "new": r"\psi_k\!\left(\sum B_UX^U\right)&=\sum B_{kU}X^U."},
  "Two summation indices added by the TeX."),
F(420, "(4.5.6), second line",
  "\u03a3 B_UX^U \u27fc \u03a3 B_UX^U . -- bare sum signs",
  r"\sum_U B_UX^U&\longmapsto\sum_U B_UX^U.", "formula", "high",
  {"old": r"\sum_U B_UX^U&\longmapsto\sum_U B_UX^U.",
   "new": r"\sum B_UX^U&\longmapsto\sum B_UX^U."},
  "Two summation indices added by the TeX."),
F(420, "paragraph before (4.5.6): 'op\u00e9rateur de \"restriction\"'",
  "op\u00e9rateur de (underlined, at the line end) / \"restriction\" with only the word underlined; the quotation marks stand outside the underline",
  r"\underline{op" + "\u00e9rateur de \"restriction\"}", "underline", "medium",
  {"old": r"\underline{op" + "\u00e9rateur de \"restriction\"}",
   "new": r"\underline{op" + "\u00e9rateur de} \"" + r"\underline{restriction}" + "\""},
  "The underline of 'restriction' starts under the r and stops after the n."),
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)

ok = True
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    path = os.path.join(RUN, "b416_420", "page_%d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        txt = fh.read()
    n = txt.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, f["page"], repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"]:
        ok = False
        print("MARKER in old", f["page"])
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in findings)
for p in range(416, 421):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("ALL OK" if ok else "PROBLEMS")
