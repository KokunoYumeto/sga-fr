"""Write findings_341_345.json and check that every fix's old string occurs exactly once in its page file.
In the TeX strings below the sign NL stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b341_345"
OUT = RUN / "findings_341_345.json"
NL = "\u23ce"


def t(s):
    return None if s is None else s.replace(NL, "\n")


def fx(old, new):
    return {"old": t(old), "new": t(new)}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": t(tex), "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = t(corrected)
    d["note"] = note
    F.append(d)


# ---------------- p. 341
add(341, "start of page, 'Comme l'anneau considéré est intègre, on en déduit la relation suivante'",
    "'Comme' is indented: a new paragraph after the display that ends p. 340 (both scans)",
    r"'Comme' follows the \end{align*} of p. 340 with only the marker line between",
    "other", "medium",
    fx(r"Comme l'anneau considéré est intègre", NL + r"Comme l'anneau considéré est intègre"),
    "Paragraph break of the print missing; the blank line comes after the marker line (as on p. 349).")
add(341, "end of the sentence before (5.4.2): '... λ^k(N') = 0 pour k > d' ;'",
    "a semicolon after d' (both scans; crops_341_345/m341_semicolon.png, w341_semicolon.png)",
    r"pour \(k>d'\) :",
    "punctuation", "high",
    fx(r"pour \(k>d'\) :", r"pour \(k>d'\)~;"),
    "The TeX has a colon for the printed semicolon.")
add(341, "'Ses opérations sont donc définie par :' (before (5.5.2))",
    "'définie' (both scans)",
    r"Ses opérations sont donc définie par",
    "misprint_in_print", "high", None,
    "Agreement slip (opérations ... définies). The TeX keeps the printed reading.",
    corrected=r"Ses opérations sont donc définies par")
add(341, "(5.5.2), first line '(n,x) + (n',x') = (n+n',x+x')'",
    "no punctuation after (n+n',x+x') (both scans)",
    r"(n,x)+(n',x')&=(n+n',x+x'),\\",
    "punctuation", "high",
    fx(r"(n+n',x+x'),", r"(n+n',x+x')"),
    "The TeX adds a comma at the end of the display line.")
add(341, "(5.5.2), second line '(n,x).(n',x') = (nn',nx'+n'x+x._N y)'",
    "no punctuation after the closing parenthesis (both scans)",
    r"(nn',nx'+n'x+x\cdot_N y).",
    "punctuation", "high",
    fx(r"x\cdot_N y).", r"x\cdot_N y)"),
    "The TeX adds a full stop at the end of the display. The misprint entry below has fix null, so nothing overlaps.")
add(341, "(5.5.2), second line, last term 'x._N y'",
    "x._N y: the letter y (both scans)",
    r"nx'+n'x+x\cdot_N y",
    "misprint_in_print", "high", None,
    "The product of (n,x) and (n',x') has the term x._N x'; y is a slip (the y of (5.5.1)). The TeX keeps the printed reading.",
    corrected=r"nx'+n'x+x\cdot_N x'")
add(341, "'On considère A comme plongé dans cet anneau par x ~> (0,x)'",
    "a wavy arrow x ⇝ (0,x) (both scans; crops_341_345/m341_arrow.png, w341_arrow.png)",
    r"x\mapsto(0,x)",
    "symbol", "high",
    fx(r"x\mapsto(0,x)", r"x\rightsquigarrow(0,x)"),
    r"The file writes this wavy arrow \rightsquigarrow elsewhere in the exposé (main.tex lines 8547, 8588).")
add(341, "after (5.5.1), before 'L'anneau A muni de cette multiplication'",
    "'L'anneau' is indented: a new paragraph (both scans)",
    r"\end{equation}" + NL + r"L'anneau \(A\) muni",
    "other", "medium",
    fx(r"\end{equation}" + NL + r"L'anneau \(A\) muni", r"\end{equation}" + NL + NL + r"L'anneau \(A\) muni"),
    "Paragraph break of the print missing after the display.")

# ---------------- p. 342
add(342, "'Pour x ∈ A, la valeur de γ^p calculée sur l'élément (0,x)'",
    "x ∈ Λ: the letter has no crossbar and no spur at its apex, in both scans (main scan: no trace of a bar between the fully inked legs); the page's other A's ('A est', 'de A ;') have both (crops_341_345/m342_A_compare.png, m342_xinA.png, w342_xinA.png)",
    r"Pour \(x\in A\)",
    "misprint_in_print", "medium",
    fx(r"Pour \(x\in A\)", r"Pour \(x\in\Lambda\)"),
    "Probably the typewriter's Greek capital lambda typed for A. The TeX silently corrects; the fix restores the printed reading. If the letter is read as an A whose crossbar failed, drop this entry.",
    corrected=r"Pour \(x\in A\)")
add(342, "display of 5.6, third line, the parenthesis '(car λ_t(1-L) = λ_t(1)/λ_t(L) = (1+t)/(1+Lt). et on applique (2.3.2))'",
    "a full stop after the fraction (1+t)/(1+Lt), on the line of its bar, one typewriter space after it and the size of the page's full stops; no comma before 'et on applique' (both scans; crops_341_345/m342_frac.png, w342_frac.png)",
    r"\frac{1+t}{1+Lt}\text{, et on applique }",
    "misprint_in_print", "medium",
    fx(r"\frac{1+t}{1+Lt}\text{, et on applique }", r"\frac{1+t}{1+Lt}.\text{ et on applique }"),
    "Full stop typed where the sentence goes on ('et on applique'). The TeX silently writes a comma; the fix restores the printed reading.",
    corrected=r"\frac{1+t}{1+Lt}\text{, et on applique }")
add(342, "display of 5.6, fourth line, denominator '1+...+λ^k(x.λ_{-1}(N))L^k t^k+..'",
    "+.. : two dots, while the numerator above ends +... (both scans; crops_341_345/m342_plusdots.png, w342_denoms.png)",
    r"L^k t^k+\cdots}",
    "misprint_in_print", "high",
    fx(r"L^k t^k+\cdots}", r"L^k t^k+..}"),
    "Two-dot ellipsis of the typist, handled as on pp. 349-350; the TeX writes the three-dot form.",
    corrected=r"L^k t^k+\cdots}")
add(342, "display of 5.6, last line, end",
    "no punctuation after the last fraction (both scans; crops_341_345/m342_denoms.png, w342_denoms.png)",
    r"L^k t^k}.",
    "punctuation", "high",
    fx(r"t^k}.", r"t^k}"),
    "The TeX adds a full stop at the end of the display. Disjoint from the next entry (apply in either order).")
add(342, "display of 5.6, last line, denominator '1+Σ_{k≥1} λ^k(N,x). λ_{-1}(N)..L^k t^k'",
    "two dots between λ_{-1}(N) and L^k, the second lighter, one typewriter space after the first (both scans; crops_341_345/m342_NdotdotL.png, w342_NdotdotL.png)",
    r"\lambda_{-1}(N)\cdot L^k t^k",
    "misprint_in_print", "medium",
    fx(r"(N)\cdot L^k", r"(N)\cdot\cdot L^k"),
    "Doubled product dot. The TeX silently writes one; the fix restores the printed reading.",
    corrected=r"(N)\cdot L^k")

# ---------------- p. 343
add(343, "start of page, 'Donc λ^p(N+L,x) est le coefficient de t^p dans la série :'",
    "'Donc' is indented: a new paragraph after the display that ends p. 342 (both scans)",
    r"'Donc' follows the \] of p. 342 with only the marker line between",
    "other", "medium",
    fx(r"Donc \(\lambda^p(N+L,x)\)", NL + r"Donc \(\lambda^p(N+L,x)\)"),
    "Paragraph break of the print missing; the blank line comes after the marker line (as on p. 349).")
add(343, "the series after 'dans la série :', numerator 'Σ_{k≥1} λ^k(N,x)(1+...+L^{k-1})t^k'",
    "(1+...+L^{k-1}): no L+ after 1+ (both scans; crops_341_345/m343_num.png, wit_343_small.png)",
    r"(1+L+\cdots+L^{k-1})",
    "extra", "high",
    fx(r"(1+L+\cdots+L^{k-1})", r"(1+\cdots+L^{k-1})"),
    "The TeX adds the term L.")
add(343, "Proposition 5.7, the statement",
    "underlined word groups: 'Soient', 'un anneau binomial', 'une', 'algèbre augmentée' (after 'K-λ-'), 'un élément de', 'tel que', 'pour' (before 'k > d'), 'Alors pour tout', 'et tout', 'on a'; each underline stops before the following comma or formula (both scans; crops_341_345/m343_prop1.png, m343_prop2.png, w343_prop.png)",
    r"the statement in roman (\textbf{Proposition 5.7.} Soient \(K\) un anneau binomial, ...)",
    "underline", "high", None,
    "Exposé V continues the Exposé II pattern of GLOBAL_ISSUES 82 (as reported for pp. 298, 306-315 and 336-340): not itemized, for the per-exposé decision; the word groups are listed for a scripted fix. It is the only statement on pp. 341-345; no \\emph on terms the print leaves plain, no category L.")
add(343, "after (5.7.1), before 'Soit A_o la K-λ-algèbre engendrée'",
    "'Soit' is indented: a new paragraph (both scans)",
    r"\end{equation}" + NL + r"Soit \(A_0\)",
    "other", "medium",
    fx(r"\end{equation}" + NL + r"Soit \(A_0\)", r"\end{equation}" + NL + NL + r"Soit \(A_0\)"),
    "Paragraph break of the print missing after the display.")

# ---------------- p. 344
add(344, "start of page (folio-344 marker)",
    "p. 344 begins 'sur x, d'où le résultat, l'homomorphisme étant compatible aux filtrations.'; p. 343 ends '... donc N_o sur N et X_o' (both scans; crops_341_345/wit_343_small.png, wit_344_small.png)",
    r"'sur \(x\), d'où le' ends the last line of page_343.tex, above the folio-344 marker; page_344.tex begins 'résultat,'",
    "marker", "high", None,
    "The folio-344 marker stands four words late. Page 344 really begins with 'sur \\(x\\), d'où le résultat'. Exact fix in main.tex (both layers): replace 'et \\(X_0\\) sur \\(x\\), d'où le\\n%%%%%%%%%%  scan idx 357  |  folio 344  %%%%%%%%%%\\nrésultat,' by 'et \\(X_0\\)\\n%%%%%%%%%%  scan idx 357  |  folio 344  %%%%%%%%%%\\nsur \\(x\\), d'où le résultat,' (simulated in memory on both layers with crops_341_345/sim_marker.py: once in each). Equivalent: python -I move_marker.py 6 344 \"sur \\(x\\), d'où le\" --before (leaves 'sur \\(x\\), d'où le' on a line of its own).")
add(344, "display after 'Par 1.9, on en déduit des morphismes :', second line 'Ĝ^t --γ'--> Ĝ^u∘i∘Ĝ^t_{g∇}'",
    "the last factor is Ĝ^t with the subscript g followed by ∇ (both scans; crops_341_345/m344_disp2.png, wit_344_small.png)",
    r"\circ\widehat G^t_g,",
    "formula", "high",
    fx(r"\circ\widehat G^t_g,", r"\circ\widehat G^t_{g\nabla},"),
    "The TeX drops the ∇ of the subscript (the law ∇, as in (Ĝ^t∘i)_∇ of the display of 6.1).")
add(344, "'avec le morphisme canonique : Ĝ --> 1+Gr.^+ (1.11)'",
    "1+\\widehat{Gr.}^+: the hat covers 'Gr.' with its dot (both scans; crops_341_345/m344_Gr.png, wit_344_small.png)",
    r"1+\widehat{\operatorname{Gr}}^{+}",
    "formula", "high",
    fx(r"1+\widehat{\operatorname{Gr}}^{+}", r"1+\widehat{\operatorname{Gr}\,\cdot\,}^{+}"),
    "The TeX drops the dot of Gr. (GLOBAL_ISSUES 88 lists p. 344); \\,\\cdot\\, is the form of the fixes on pp. 312-313 and 346.")

# ---------------- p. 345
add(345, "first display, second factor '(1+..^+)' of '(1+.^+)x(1+..^+) --*--> 1+.^+'",
    "two dots after 1+, the hand-drawn hat over the first; the first factor and the target have one (both scans; crops_341_345/m345_disp1.png, w345_disp1.png)",
    r"\times(1+\widehat{\cdot}{}^{+})",
    "misprint_in_print", "high",
    fx(r"\times(1+\widehat{\cdot}{}^{+})", r"\times(1+\widehat{\cdot}\cdot{}^{+})"),
    "Doubled placeholder dot. The TeX silently writes one; the fix restores the printed reading.",
    corrected=r"\times(1+\widehat{\cdot}{}^{+})")
add(345, "'muni des lois de composition définie par :'",
    "'définie' (both scans; crops_341_345/w345_forall.png)",
    r"muni des lois de composition définie par",
    "misprint_in_print", "medium", None,
    "Agreement slip (lois ... définies), as 'Ses opérations sont donc définie par' on p. 341. The TeX keeps the printed reading.",
    corrected=r"muni des lois de composition définies par")
add(345, "'∀ a,a' ∈ A, φ, φ' ∈ 1+Â^+,' before the display of the sum",
    "a,a' ∈ A (both scans; crops_341_345/m345_forall.png, w345_forall.png)",
    r"\(\forall\,a,a'\in A\)",
    "misprint_in_print", "medium", None,
    "The pairs (a,φ) lie in K x (1+Â^+), and (6.1.3) lets a act as a scalar, so a, a' are elements of K. The TeX keeps the printed reading.",
    corrected=r"\(\forall\,a,a'\in K\)")
add(345, "after (6.1.2), before 'L'anneau ainsi construit'",
    "'L'anneau' is indented: a new paragraph (both scans)",
    r"\end{equation}" + NL + r"L'anneau ainsi construit",
    "other", "medium",
    fx(r"\end{equation}" + NL + r"L'anneau ainsi construit", r"\end{equation}" + NL + NL + r"L'anneau ainsi construit"),
    "Paragraph break of the print missing after the display.")
add(345, "'L'anneau ainsi construit admet (1.1) pour l'élément unité'",
    "(1.1) with a full stop, no comma tail (both scans; crops_341_345/m345_unit.png, w345_unit.png)",
    r"admet (1.1) pour",
    "misprint_in_print", "high", None,
    "The unit element of K x (1+Â^+) is the pair (1,1). The TeX keeps the printed reading.",
    corrected=r"admet \((1,1)\) pour")

# ---------------- checks
ok = True
for d in F:
    src = (PAGES / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    if d["kind"] != "marker" and d["tex"] and not d["tex"].startswith("'") and not d["tex"].startswith("the "):
        if d["tex"] not in src:
            print("TEX NOT FOUND", d["page"], repr(d["tex"]))
    if d["fix"] is not None:
        n = src.count(d["fix"]["old"])
        marker_cross = "%%%%%%%%%%" in d["fix"]["old"]
        print(d["page"], d["kind"], n, "MARKER!" if marker_cross else "", repr(d["fix"]["old"][:60]))
        if n != 1 or marker_cross:
            ok = False
print("all unique:", ok, "| findings:", len(F))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted({d["page"] for d in F}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT)
