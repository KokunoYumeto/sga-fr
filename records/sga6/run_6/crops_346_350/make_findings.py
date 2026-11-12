"""Writes findings_346_350.json (SGA 6, folios 346-350) and checks every fix's old string page by page."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b346_350"
OUT = RUN / "findings_346_350.json"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


GRDOT = r"\widehat{\operatorname{Gr}\,\cdot\,}^{+}"

# ---------------- p. 346
add(346, "'Utilisant le morphisme canonique : G^ -> 1+(Gr.)^+'",
    "1+\\widehat{Gr.}^+: the hat covers 'Gr.' with its dot, the placeholder dot of 1+.^+ (both scans; crops_346_350/w346_line5.png)",
    r"1+\widehat{\operatorname{Gr}}^{+}", "formula", "high",
    {"old": r"1+\widehat{\operatorname{Gr}}^{+}\), qui donne", "new": "1+" + GRDOT + r"\), qui donne"},
    "The TeX drops the dot of Gr. (GLOBAL_ISSUES 88 lists p. 346); \\,\\cdot\\, is the form of the fixes on pp. 312-313.")
add(346, "'qui donne : G^ -> K x (1+Gr.^+)'",
    "Gr. with its dot (both scans; w346_line5.png)",
    r"K\times(1+\widehat{\operatorname{Gr}}^{+})", "formula", "high",
    {"old": r"K\times(1+\widehat{\operatorname{Gr}}^{+})\),", "new": r"K\times(1+" + GRDOT + r")\),"},
    "Dot of Gr. dropped, as the previous entry. Apply before the next entry, whose old is the text this edit leaves.")
add(346, "same place, 'K x (1+Gr.^+)'",
    "no hat over Gr. here (both scans; w346_line5.png, m346_line5.png), while the same expression has its hand-drawn hat "
    "on the same line (1+\\widehat{Gr.}^+) and in the display below (Kx(1+\\widehat{Gr.}^+))",
    r"K\times(1+\widehat{\operatorname{Gr}}^{+})", "misprint_in_print", "medium",
    {"old": r"K\times(1+" + GRDOT + r")\),", "new": r"K\times(1+\operatorname{Gr}\,\cdot\,{}^{+})\),"},
    "The hand-drawn hat was left out: the canonical morphism G^ -> 1+\\widehat{Gr.}^+ of the same sentence gives "
    "G^ -> K x (1+\\widehat{Gr.}^+), as the next display writes it. The TeX silently adds the hat; the fix restores the "
    "printed reading. Its old is the text the previous entry leaves (apply after it).",
    corrected=r"K\times(1+" + GRDOT + ")")
add(346, "first display 'G^t --gamma'--> G^u o i o (Kx(1+(Gr.)^+)) ,'",
    "Gr. with its dot under the hat (both scans; w346_disp1.png)",
    r"(K\times(1+\widehat{\operatorname{Gr}}^{+})),", "formula", "high",
    {"old": r"(K\times(1+\widehat{\operatorname{Gr}}^{+})),", "new": r"(K\times(1+" + GRDOT + ")),"},
    "Dot of Gr. dropped, as above.")
add(346, "'qui d'après 1.12 définit un morphisme de foncteurs sur   :'",
    "a blank between 'sur' and ':' (both scans; crops_346_350/m346_sur.png, w346_sur.png): the hand-drawn letter of the "
    "category was not written in",
    r"sur\qquad:", "misprint_in_print", "medium", None,
    "The TeX keeps the printed blank. The functors are defined on the category of graded K-algebras, the hand-drawn "
    "script G (\\mathcal G, GLOBAL_ISSUES 88); the parallel sentence at the foot of p. 344 reads 'deux morphismes de "
    "foncteurs sur G :' with that letter (witness).",
    corrected=r"foncteurs sur \(\mathcal G\) :")
add(346, "second display '1+.^+ --> G^u o i o (Kx(1+.^+)) .'",
    "only a typed prime above the arrow; the hand-drawn gamma is missing (both scans; w346_disp2.png, m346_disp2.png)",
    r"\xrightarrow{\gamma'}", "misprint_in_print", "high",
    {"old": r"{}^{+}\xrightarrow{\gamma'}", "new": r"{}^{+}\xrightarrow{'}"},
    "The arrow is the gamma' of the display above (and of 'seront notées gamma au lieu de gamma''); the gamma was not "
    "written in. The TeX silently supplies it; the fix restores the printed reading.",
    corrected=r"{}^{+}\xrightarrow{\gamma'}")

# ---------------- p. 347
add(347, "Définition 6.2, 'sa valeur pour A ∈ Ob(G)'",
    "Ob(G) with the hand-drawn script G of graded K-algebras (a C-like letter running into a long descender), the letter "
    "of pp. 308-313 and of the foot of p. 344 (both scans; m347_Ob.png, w347_Ob.png)",
    r"\operatorname{Ob}(\mathcal C_g)", "symbol", "high",
    {"old": r"\operatorname{Ob}(\mathcal C_g)", "new": r"\operatorname{Ob}(\mathcal G)"},
    "GLOBAL_ISSUES 88 asks to check folio 347: confirmed; written \\mathcal G as fixed on pp. 306-313.")
add(347, "'on déduit les relations :' before (6.2.1)",
    "'les relations :' with a typed colon (both scans)",
    "on déduit les relations", "punctuation", "high",
    {"old": "on déduit les relations\n", "new": "on déduit les relations :\n"},
    "The TeX drops the colon.")

# ---------------- p. 348
add(348, "start of page",
    "p. 348 begins '6.3. Pour toute K-algèbre graduée A' (both scans); p. 347 ends '... est un λ-homomorphisme).'",
    r"\textbf{6.3.} stands at the end of the text of p. 347, above the folio-348 marker", "marker", "high", None,
    "Page 348 really begins with the heading 6.3. Move the folio-348 marker above \\textbf{6.3.}: "
    "python -I move_marker.py 6 348 \"\\textbf{6.3.}\" --before (simulated on both layers: '... λ-homomorphisme).', "
    "blank line, the marker, \\textbf{6.3.}, 'Pour toute').")
add(348, "before 'Cet homomorphisme est compatible avec la multiplication'",
    "'Cet homomorphisme' is indented: a new paragraph after (6.3.1) (both scans)",
    r"\end{equation} followed directly by 'Cet homomorphisme'", "other", "high",
    {"old": "\\end{equation}\nCet homomorphisme", "new": "\\end{equation}\n\nCet homomorphisme"},
    "Paragraph break of the print missing.")
add(348, "'pour les éléments 1+X, 1+Y de 1+\\widehat{K[X,Y]}^+ ; or on a :'",
    "a hand-drawn hat over K[X,Y] (both scans; m348_KXY.png)",
    r"1+K[X,Y]^+", "formula", "high",
    {"old": r"\(1+K[X,Y]^+\)", "new": r"\(1+\widehat{K[X,Y]}{}^{+}\)"},
    "The TeX drops the hat; written as (1+\\widehat{K[X,Y]}{}^{+})^{2} on p. 345.")
add(348, "last display, first line '∀a ∈ K,  ch(1+X)^a)'",
    "ch(1+X)^a): one opening parenthesis after ch, two closing (both scans; m348_cha.png, w348_cha.png)",
    r"\ch((1+X)^a)", "misprint_in_print", "high",
    {"old": r"\ch((1+X)^a)", "new": r"\ch(1+X)^a)"},
    "The TeX silently supplies the missing parenthesis; the fix restores the printed reading.",
    corrected=r"\ch((1+X)^a)")

# ---------------- p. 349
add(349, "start of page, 'On peut donc de façon évidente étendre ch'",
    "'On peut donc' is indented: a new paragraph after the display that ends p. 348 (both scans)",
    r"'On' follows the \] of p. 348 with only the marker line between", "other", "high",
    {"old": "On\npeut donc", "new": "\nOn\npeut donc"},
    "Paragraph break of the print missing; the blank line comes after the marker line.")
add(349, "Proposition 6.5, 'où Â^{≥n} = ∏_{i≥n} A^i, On a les congruences suivantes'",
    "a comma after A^i: it reaches as far below the baseline as the page's commas (main scan 7-8 px, witness 5 px; "
    "full stops 4 and 3 px), both scans (m349_prod_mark.png, w349_mark8.png); a capital 'On' follows",
    r"A^i\). On a", "misprint_in_print", "medium",
    {"old": r"A^i\). On a", "new": r"A^i\), On a"},
    "Comma typed for the full stop that ends the sentence. The TeX silently corrects it; the fix restores the printed "
    "reading.",
    corrected=r"A^i\). On a")
add(349, "(6.5.2), 'ch(φ) = (-1)^{n-1}/(n-1)! .a_n +.. ;'",
    "+.. : two dots (both scans; m349_652.png, w349_652.png)",
    r".a_n+\cdots~;", "misprint_in_print", "high",
    {"old": r".a_n+\cdots~;", "new": r".a_n+..~;"},
    "Two-dot ellipsis of the typist, handled as on pp. 37, 50 and 332; the TeX writes the three-dot form.",
    corrected=r".a_n+\cdots~;")
add(349, "(6.5.3), 'a_m b_n +.. ,'",
    "+.. : two dots (both scans; m349_653.png, w349_653.png)",
    r"b_n+\cdots,", "misprint_in_print", "high",
    {"old": r"b_n+\cdots,", "new": r"b_n+..,"},
    "Two-dot ellipsis, as (6.5.2).",
    corrected=r"b_n+\cdots,")

# ---------------- p. 350
add(350, "first display '= (-1)^{n-1}/(n-1)! a_n + ...'",
    "the display ends with the three dots of the series; nothing follows them (both scans; m350_disp1.png, "
    "w350_disp1end.png)",
    r"a_n+\cdots .", "punctuation", "medium",
    {"old": r"a_n+\cdots .", "new": r"a_n+\cdots"},
    "The TeX adds a full stop after the series.")
add(350, "display after 'd'après (6.5.2) :', last factor '(1 + (-1)^{n-1}/(n-1)! .Y_n+..),'",
    "+.. : two dots, while Z_p +... and X_m + ... of the same display have three (both scans; m350_disp2.png, "
    "w350_disp2.png)",
    r"Y_n+\cdots\right)", "misprint_in_print", "high",
    {"old": r"Y_n+\cdots\right)", "new": r"Y_n+..\right)"},
    "Two-dot ellipsis, as (6.5.2) and (6.5.3).",
    corrected=r"Y_n+\cdots\right)")
add(350, "Proposition 6.6.1 i), 'λ^i(x) = 0 pour i ≥ n ;'",
    "i ≥ n: the slanted ≥ with its lower stroke (as in 'n ≥ 1' of p. 349), not the plain > of 'degré > n' at the end "
    "of the statement (both scans; m350_i.png, w350_items.png)",
    r"i>n", "misprint_in_print", "high",
    {"old": r"\text{pour }i>n~;", "new": r"\text{pour }i\ge n~;"},
    "By ii) λ^n(x) = (1,1+a_1) is not 0, so λ^i(x) = 0 only for i > n. The TeX silently corrects; the fix restores the "
    "printed reading.",
    corrected=r"\text{pour }i>n~;")
add(350, "Proposition 6.6.1 ii), 'λ^n(x) = (1,1+a_1)'",
    "no punctuation after (1,1+a_1) (both scans; m350_ii.png, w350_items.png)",
    r"(1,1+a_1),", "punctuation", "high",
    {"old": r"=(1,1+a_1),", "new": r"=(1,1+a_1)"},
    "The TeX adds a comma.")
add(350, "Proposition 6.6.1 iii), '= 0,1-(n-1)!a_n+...),'",
    "no opening parenthesis before 0; the closing one after '+...' is printed (both scans; m350_iii.png, w350_iii.png)",
    r"=(0,1-(n-1)!a_n", "misprint_in_print", "high",
    {"old": r"=(0,1-(n-1)!a_n", "new": r"=0,1-(n-1)!a_n"},
    "The TeX silently supplies the parenthesis; the fix restores the printed reading.",
    corrected=r"=(0,1-(n-1)!a_n")
add(350, "end of page",
    "p. 350 ends '... il suffit de faire la démonstration dans le cas'; p. 351 begins 'où A est l'anneau "
    "K[X_1,...,X_n]' (both scans)",
    r"'où \(A\) est l'%' stands above the folio-351 marker", "marker", "high", None,
    "Move the folio-351 marker before 'où': python -I move_marker.py 6 351 \"où \\(A\\) est l'\" --before (simulated "
    "on both layers: '... dans le cas ', the marker, \"où \\(A\\) est l'%\", 'anneau \\(K[X_1,\\ldots,X_n]\\)'; the % "
    "keeps l'anneau joined).")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- check: apply the fixes of each page in order; each old must occur exactly once at its turn and never contain a
# marker line.
ok = True
for page in sorted({f["page"] for f in F}):
    orig = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    cur = orig
    for f in F:
        if f["page"] != page or not f["fix"]:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        n_cur, n_orig = cur.count(old), orig.count(old)
        bad = n_cur != 1 or "%%%%%%%%%%  scan idx" in old or "%%%%%%%%%%  scan idx" in new
        ok = ok and not bad
        print(page, "BAD" if bad else "OK", "now", n_cur, "orig", n_orig, "|", f["kind"], "|",
              old.replace("\n", "\\n")[:60])
        cur = cur.replace(old, new, 1)
print("ALL OK" if ok else "PROBLEMS", len(F), "findings")
