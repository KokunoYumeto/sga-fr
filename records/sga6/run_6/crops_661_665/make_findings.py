"""Build findings_661_665.json for SGA 6 pp. 661-665 and check that every fix's old string occurs exactly once in its
page file (and every misprint's tex string, where the fix is null). Run: python -I -B make_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
BATCH = HERE.parent / "b661_665"
OUT = HERE.parent / "findings_661_665.json"
NL = chr(10)
C = "crops_661_665/"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 661
add(661, "Corollaire 6.14, statement: 'et tout idéal de l'anneau de polynômes k_o[T_1,...,T_N], engendré par ...'",
    "tout idéal de l'anneau: no letter I after 'idéal' (both scans)",
    r"tout id\'eal de l'anneau", "misprint_in_print", "medium", None,
    "The ideal is not named, yet the same sentence uses it as I ('la racine √I de I'). The TeX keeps the printed "
    "reading (the corrected layer too).",
    corrected=r"tout id\'eal $I$ de l'anneau")
add(661, "Corollaire 6.14, statement: 'la racine √I de I est engendré par des éléments de degré ≤ R_N(m)'",
    "est engendré, without the feminine e (both scans)",
    r"est engendr\'e", "misprint_in_print", "medium", None,
    "Agreement slip (la racine ... engendrée). The TeX keeps the printed reading; the corrected layer already reads "
    "engendrée.",
    corrected=r"est engendr\'ee")
add(661, "proof of 6.14, line 2: 'Introduisant une indéterminée auxilaire, considérons Y (resp. X)'",
    "auxilaire, with one i (both scans; " + C + "c661_auxil.png, wit_661.png)",
    "auxiliaire", "misprint_in_print", "high", {"old": "auxiliaire", "new": "auxilaire"},
    "Typing slip of the print; the TeX silently corrects it (both layers). The fix restores the printed reading.",
    corrected="auxiliaire")
add(661, "after 'd'après 6.13.': 'Soit X = ∪X^q la décomposition suivant la dimension.'",
    "'Soit X' begins a new, indented paragraph (both scans)",
    r"d'apr\`es 6.13. Soit $X=\bigcup X^q$ (one paragraph)", "other", "high",
    {"old": r"d'apr\`es 6.13. Soit", "new": r"d'apr\`es 6.13." + NL + NL + "Soit"},
    "Missing paragraph break.")
add(661, "after 'h^o(O_Y) ≤ e_q.': 'Par conséquent, O_{X^q} est un (0,...,0,e_q)-faisceau grâce à 6.10.'",
    "'Par conséquent' begins a new, indented paragraph (both scans)",
    r"\le e_q$. Par cons\'equent (one paragraph)", "other", "high",
    {"old": r"\le e_q$. Par cons\'equent", "new": r"\le e_q$." + NL + NL + r"Par cons\'equent"},
    "Missing paragraph break.")
add(661, "'Il résulte donc de l'injection O_X ⟶ ∏O_{X^q} que O_X est un (e_o,...,e_N)-faisceau'",
    "a bare product sign, no index under it (both scans; " + C + "c661_prod.png, w661_prod_sum.png)",
    r"\prod_q\mathcal O_{X^q}", "extra", "high", {"old": r"\prod_q", "new": r"\prod"},
    "The TeX adds a product index the print does not have.")
add(661, "'dans le polynôme de Hilbert χ(O_X(n)) = Σ_{i=0}^{n} a_i (n+i over i)'",
    "upper limit a small n (both scans; " + C + "w661_prod_sum.png); the sum for the b_i above has a capital N",
    r"\sum_{i=0}^{n}a_i", "misprint_in_print", "high", None,
    "n is the variable of the Hilbert polynomial; the sum runs to N, as for the b_i. The TeX keeps the printed "
    "reading; the corrected layer already reads N.",
    corrected=r"\sum_{i=0}^{N}a_i")
add(661, "'on a |a_i| ≤ f_i avec f_i = A_{N-i}(e_i,...,e_N;0) d'après 6.7'",
    "|a_i| ≤ _i: after the bold hand-drawn ≤ a blank cell, then the subscript i; no f (both scans; "
    + C + "c661_fi.png, w661_fi.png)",
    r"|a_i|\le f_i", "misprint_in_print", "medium", {"old": r"|a_i|\le f_i", "new": r"|a_i|\le {}_i"},
    "The f was not typed (f_i is defined right after). The TeX silently supplies it (both layers); the fix restores "
    "the printed reading.",
    corrected=r"|a_i|\le f_i")
add(661, "structure sheaves throughout pp. 661-665",
    "a plain typed capital O, neither underlined nor script: O_Y(n), O_{X^q}, O_X (p. 661), O_X(D), O_X(1), O_Y "
    "(p. 663), O_Y, O_{X'} (p. 664) (both scans; " + C + "c661_O.png, c664_M.png)",
    r"\mathcal O", "font", "medium", None,
    r"CONVENTION, not itemized (the pending volume decision covers the underlined O; these pages type it plain): "
    r"p. 661 \chi(\mathcal O_Y(n)), p. 663 H=\mathcal O_X(1), p. 664 I\cdot\mathcal O_{X'}.")

# ---------------------------------------------------------------- p. 662
add(662, "Théorème 7.1, display '< c_1(L). c_1(H) > = 0 et < c_1(L)^2 > ≥ 0 ,'",
    "the word et underlined (both scans; " + C + "c662_disp.png)",
    r"\hbox{et}", "underline", "high", {"old": r"\hbox{et}", "new": r"\hbox{\emph{et}}"},
    r"Underlined word in the display of the statement; the page writes the statement's underlines as \emph.")
add(662, "after (ii) of Lemme 7.1.2: 'En effet, (ii) implique ...' (the first line of p. 663)",
    "'En effet' begins a new, indented paragraph after the list (both scans)",
    r"\end{enumerate} followed by 'En' on the next line (no blank line)", "other", "high",
    {"old": r"\end{enumerate}" + NL, "new": r"\end{enumerate}" + NL + NL},
    "Missing paragraph break before 'En effet'. Works before or after the marker move of p. 663 (the marker then "
    "stands between the blank line and 'En').")
add(662, "intersection and other products throughout pp. 662-665",
    "the product is a typed full stop on the baseline: < c_1(L). c_1(H) >, <c_1(N).c_1(H_1)>, I.O_{X'}, "
    "< c_1(L).Y > (both scans; " + C + "c662_N.png, c664_M.png, c664_proj.png)",
    r"\cdot", "symbol", "medium", None,
    r"CONVENTION, not itemized: the TeX writes \cdot (mid-height) for every typed product stop, e.g. p. 662 "
    r"\langle c_1(L)\cdot c_1(H)\rangle, p. 664 I\cdot\mathcal O_{X'}, p. 665 \langle c_1(L)^2\cdot c_1(H)^{r-2}\rangle. "
    r"Earlier batches changed single typed stops written \cdot back to '.' (pp. 89, 117); one decision for the products.")

# ---------------------------------------------------------------- p. 663
add(663, "start of the page: 'En effet, (ii) implique qu'il existe un diviseur effectif D tel que ...'",
    "the page begins with the indented 'En effet,'; p. 662 ends with (ii) of Lemme 7.1.2 (both scans)",
    "the word 'En' is the last line of page_662.tex, above the marker; page_663.tex begins with 'effet,'",
    "marker", "high", None,
    "The marker of folio 663 stands one word too late: move it up one line, before 'En' "
    "(move_marker.py 6 663 En --before). The paragraph break before 'En effet' is the separate p. 662 fix.")
add(663, "exact sequence display, second term 'H^2(N^{⊗n}(p-1)'",
    "H^2(N^{⊗n}(p-1) with one closing parenthesis only, then the arrow (both scans; " + C + "c663_seq.png, "
    "wit_663.png)",
    r"H^2\bigl(N^{\otimes n}(p-1)\bigr)", "misprint_in_print", "high", {"old": r"(p-1)\bigr)", "new": r"(p-1)"},
    "The print drops the closing parenthesis of H^2(...); the TeX silently adds it (both layers). The fix restores "
    "the printed reading.",
    corrected=r"(p-1)\bigr)")
add(663, "display 'h^o(N^{⊗n}) = χ(N^{⊗n}) + h^1(N^{⊗n}) ≥ χ(N^{⊗n}) = 1/2 < c_1(N)^2 > n^2+...>0,'",
    "1/2 typed on the line with a slash (both scans; " + C + "c663_chi.png)",
    r"=\frac{1}{2}\langle", "formula", "high", {"old": r"=\frac{1}{2}\langle", "new": r"=1/2\langle"},
    "Built-up fraction for the print's slash.")
add(663, "same display, 'n^2+...>0'",
    "three typed full stops on the baseline (both scans)",
    r"n^2+\cdots>0", "symbol", "low", {"old": r"n^2+\cdots>0", "new": r"n^2+\ldots>0"},
    r"\cdots sets the dots at mid-height (as the fixes of pp. 49, 79, 80, 608; GLOBAL_ISSUES 87). Independent of the "
    "1/2 fix.")

# ---------------------------------------------------------------- p. 664
add(664, "start of the page: 'qu'un nombre fini de points singuliers, réduction justifiée ...'",
    "the page begins with 'qu'un nombre fini'; p. 663 ends with 'de sorte que X n'a' (both scans)",
    "'qu'un' ends the last line of page_663.tex ('... de sorte que $X$ n'a qu'un'), above the marker; page_664.tex "
    "begins with 'nombre fini'",
    "marker", "high", None,
    "The marker of folio 664 stands one word too late: move it before 'qu'un' (move_marker.py 6 664 \"qu'un\" "
    "--before).")
add(664, "'Soit f: X' ⟶ X l'éclatement de l'idéal I de O_Y.'",
    "de O_Y, subscript Y (both scans; " + C + "c664_M.png)",
    r"l'id\'eal $I$ de $\mathcal O_Y$", "misprint_in_print", "medium", None,
    "The ideal blown up is the ideal of the curve Y in O_X (it makes I.O_{X'} invertible on X'). The TeX keeps the "
    r"printed reading; the corrected layer already reads \mathcal O_X.",
    corrected=r"l'id\'eal $I$ de $\mathcal O_X$")
add(664, "'L'idéal M = I.O_{X'} est inversible'",
    "a plain typed capital M (both scans; " + C + "c664_M.png)",
    r"\mathcal M=I\cdot\mathcal O_{X'}", "font", "high", {"old": r"$\mathcal M=I", "new": r"$M=I"},
    "Script M in the TeX for the print's plain M (the same in the next finding).")
add(664, "'on a que < c_1(f*L).c_1(M) > = - < c_1(f*L).Y' > - ...'",
    "c_1(M) with a plain typed M (both scans; " + C + "c664_proj.png)",
    r"c_1(\mathcal M)", "font", "high", {"old": r"c_1(\mathcal M)", "new": r"c_1(M)"},
    "As the previous finding.")
add(664, "Corollaire 7.3: 'qui n'est pas numériquement équivalent à H, etssoient d = ...'",
    "etssoient, one word, underlined (both scans; " + C + "c664_etss.png, w664_etss.png)",
    "et soient", "misprint_in_print", "high", {"old": "et soient", "new": "etssoient"},
    "Typing slip of the print (an s typed for the space); the TeX silently corrects it (both layers). The fix "
    "restores the printed reading.",
    corrected="et soient")
add(664, "Corollaire 7.3, conclusion '< c_1(M)^2 > ≤ d^2/h'",
    "a thin hand-drawn < with a short separate stroke above the end of its upper arm and no bar under it (both "
    "scans; " + C + "c664_leq_z.png, w664_leq_z.png); the typed ≤ of p. 661 has its bar under the sign",
    r"\langle c_1(M)^2\rangle\leq d^2/h", "symbol", "low", {"old": r"\rangle\leq d^2/h", "new": r"\rangle<d^2/h"},
    "Reading uncertain: the stroke above may be a stray mark or a misplaced bar. For <: the proof gives the strict "
    "inequality (<c_1(L)^2> < 0) and 7.4 (ii), proved 'd'après le raisonnement de 7.3', prints a strict <. For ≤: "
    "with the hypothesis as printed (M not numerically equivalent to H) only ≤ holds (equality for M = H^2). Check "
    "the glyph before applying.")
add(664, "proof of Corollaire 7.3: 'soit L = M^{⊗n} ⊗ H^{⊗-d}'",
    "M^{⊗n}: a handwritten n after the ⊗, no ascender (both scans; " + C + "c664_L.png, w664_L.png)",
    r"L=M^{\otimes n}", "misprint_in_print", "high", None,
    "With d = <c_1(M).c_1(H)> and h = <c_1(H)^2>, <c_1(L).c_1(H)> = nd - dh vanishes only for n = h. The TeX keeps "
    "the printed reading; the corrected layer already reads h.",
    corrected=r"L=M^{\otimes h}")

# ---------------------------------------------------------------- p. 665
add(665, "Corollaire 7.4 (i), display '< c_1(L).c_1(H)^{r-1} > = 0 et < c_1(L)^2. c_1(H)^{r-2} > ≥ 0 .'",
    "the word et underlined (both scans)",
    r"\hbox{et}", "underline", "high", {"old": r"\hbox{et}", "new": r"\hbox{\emph{et}}"},
    "As p. 662: the underlined et in the display of the statement.")
add(665, "Corollaire 7.4 (i), end of the display",
    "'> ≥ 0   .': a full stop (both scans)",
    r"\geq0;", "punctuation", "high",
    {"old": r"c_1(H)^{r-2}\rangle\geq0;", "new": r"c_1(H)^{r-2}\rangle\geq0."},
    "Semicolon in the TeX where the print has a full stop.")
add(665, "Corollaire 7.4 (ii), display",
    "'< c_1(M)^2.c_1(H)^{r-2} > < < c_1(M).c_1(H)^{r-1} >^2 / < c_1(H)^r >  .': the quotient typed on the line with "
    "a slash (both scans)",
    r"\frac{\langle c_1(M)\cdot c_1(H)^{r-1}\rangle^2}{\langle c_1(H)^r\rangle}", "formula", "high",
    {"old": r"\frac{\langle c_1(M)\cdot c_1(H)^{r-1}\rangle^2}" + NL + r"        {\langle c_1(H)^r\rangle}",
     "new": r"\langle c_1(M)\cdot c_1(H)^{r-1}\rangle^2/\langle c_1(H)^r\rangle"},
    "Built-up fraction for the print's slash.")
add(665, "after the list (i)-(ii): 'En effet, (ii) résulte tout de suite de (i), ...'",
    "'En effet' begins a new, indented paragraph (both scans)",
    r"\end{enumerate} followed by 'En effet' on the next line (no blank line)", "other", "high",
    {"old": r"\end{enumerate}" + NL, "new": r"\end{enumerate}" + NL + NL},
    "Missing paragraph break.")
add(665, "'Alors les hypersurfaces Z de degré ν_o qui contiennent Y, n'ont pas de points communs en dehors de Y.'",
    "a comma after Y (both scans; " + C + "c665_comma.png)",
    r"qui contiennent $Y$ n'ont", "punctuation", "high",
    {"old": r"contiennent $Y$ n'ont", "new": r"contiennent $Y$, n'ont"},
    "The TeX drops the print's comma.")
add(665, "'X' = Z_1 ∩...∩ Z_{r-2} ∩ X soit irréductible'",
    "three typed full stops on the baseline between the two ∩ (both scans)",
    r"Z_1\cap\cdots\cap Z_{r-2}", "symbol", "low", {"old": r"Z_1\cap\cdots\cap", "new": r"Z_1\cap\ldots\cap"},
    r"As p. 663 (typed baseline dots written \cdots).")
add(665, "'... équivalent à 0 sur X'. Or par la formule de projection, on a que'",
    "'Or' without a comma: 'Or' ends the line, the next line begins 'par la formule' (both scans; "
    + C + "w665_Or.png)",
    "Or, par la formule", "punctuation", "high", {"old": "Or, par la formule", "new": "Or par la formule"},
    "The TeX adds a comma.")
add(665, "end of the page: the opening of Corollaire 7.5",
    "p. 665 ends with the first three lines of the statement, 'Corollaire 7.5. Soient k un corps algébriquement "
    "clos, Y un k-schéma projectif, muni d'un faisceau ample H, et X le schéma des zéros d'une section φ de H. On "
    "suppose que pour toute composante irréductible Y^i de Y,'; p. 666 begins with 'les composantes irréductibles "
    "de X ∩ Y^i = V(φ|Y^i) sont de dimension ≥ 2.' (both scans; " + C + "wit_665.png, w666_top.png)",
    r"page_665.tex ends with '\textbf{Corollaire 7.5.}'; the marker of folio 666 follows it, so '\emph{Soient $k$ "
    r"... composante irr\'eductible $Y^i$ de $Y$,' stands under folio 666",
    "marker", "high", None,
    r"The marker of folio 666 stands three printed lines too early. Page 666 really begins with 'les composantes "
    r"irr\'eductibles de $X\cap Y^i$': move the marker forward to just before that text (move_marker.py 6 666 "
    "\"les composantes irr\"; the first match after the present marker). The text that moves to p. 665 matches the "
    "print.")

# ---------------------------------------------------------------- checks
bad = 0
for d in F:
    t = (BATCH / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    if d["fix"] is not None:
        old = d["fix"]["old"]
        n = t.count(old)
        if n != 1 or "%%%%%%%%%%" in old or "%%%%%%%%%%" in d["fix"]["new"]:
            bad += 1
            print("BAD fix", d["page"], repr(old), n)
    elif d["kind"] == "misprint_in_print":
        n = t.count(d["tex"])
        if n != 1:
            bad += 1
            print("BAD misprint tex", d["page"], repr(d["tex"]), n)
for p in range(661, 666):
    ps = [d for d in F if d["page"] == p]
    mis = sum(d["kind"] == "misprint_in_print" for d in ps)
    print(p, "normal", len(ps) - mis, "misprint", mis)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + NL, encoding="utf-8")
print("written", OUT, len(F), "findings;", "bad", bad)
