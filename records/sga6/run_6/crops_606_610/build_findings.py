"""Build findings_606_610.json; check that every fix's old occurs exactly once in its page file (also after the
other fixes of the page are applied), and simulate the p. 610 marker move in memory on both layers of main.tex."""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b606_610"
OUT = RUN / "findings_606_610.json"
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
NL = "\n"
UP = r"\underline{\Pic}"

def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d

def fx(old, new):
    return {"old": old, "new": new}

PICNOTE = ("Exposé XII writes \\Pic plain everywhere (no \\underline{\\Pic} in folios 595-630); the file's own form for the "
           "underlined Pic is \\underline{\\Pic} (Exposé XIII, 66 places). The print underlines only 'Pic', not its indices.")

M610_OLD = "\\item" + NL + "%%%%%%%%%%  scan idx 623  |  folio 610  %%%%%%%%%%" + NL + "Pour \\(i,j\\ge0\\)"
M610_NEW = "%%%%%%%%%%  scan idx 623  |  folio 610  %%%%%%%%%%" + NL + "\\item" + NL + "Pour \\(i,j\\ge0\\)"

findings = [
    # ---------------- page 606
    F(606, "start of page: 'En effet on peut évidemment supposer S et T affines.'",
      "'En effet' is indented as a new paragraph at the top of p. 606, after the display '3.2. Im δ*_T = Im δ_T' that ends p. 605 (both scans; the typescript's continuation lines after displays start flush left, e.g. 'en tenant compte' on this page)",
      "'\\]' of the 3.2 display, then the marker line, then 'En' with no blank line: the paragraph runs on after the display",
      "other", "high", fx("En" + NL + "effet on peut", NL + "En" + NL + "effet on peut"),
      "Missing paragraph break. The edit adds the blank line after the folio-606 marker line (the marker line itself is unchanged)."),
    F(606, "after 'et n_β ∈ nilrad(Γ(X,O_X')).': 'D'après i), (n_β⊗t_β) I_T = 0.'",
      "'D'après i)' begins a new, indented paragraph (both scans; crops_606_610/wit_606_half.png)",
      "'...\\operatorname{nilrad}(\\Gamma(X,\\mathcal O_{X'}))\\). D'après i),' in one paragraph",
      "other", "high", fx("\\). D'après i),", "\\)." + NL + NL + "D'après i),"),
      "Missing paragraph break."),
    F(606, "'Finalement soit g = Σ g_β⊗t_α ∈ Γ(X_T,O_X'_T)'",
      "'g = Σ g_β⊗t_α' with index alpha on t (both scans: page_606_s2.png; crops_606_610/wit_606_half.png)",
      "'\\(g=\\sum g_\\beta\\otimes t_\\alpha\\in': the TeX keeps the printed reading",
      "misprint_in_print", "high", None,
      "Wrong index: the sum is the decomposition g = Σ g_β⊗t_β of the preceding paragraph. The current layer already reads t_\\beta.",
      corrected="g=\\sum g_\\beta\\otimes t_\\beta"),
    F(606, "'Soit g_β = v(h) + n_β où'",
      "'g_β = v(h) + n_β' (both scans)",
      "'\\(g_\\beta=v(h)+n_\\beta\\)': the TeX keeps the printed reading",
      "misprint_in_print", "medium", None,
      "Omitted index: as in 'g_β = v(h_β) + n_β' of the preceding paragraph (h is not defined here; the h of the paragraph before is Σ v(h_β)⊗t_β). The current layer already reads v(h_\\beta).",
      corrected="v(h_\\beta)"),
    F(606, "'n_β ∈ nilrad(Γ(X,O_X));on a alors'",
      "'nilrad(Γ(X,O_X))' with subscript X, no prime (both scans; crops_606_610/w606_finalement.png)",
      "'\\operatorname{nilrad}(\\Gamma(X,\\mathcal O_X))': the TeX keeps the printed reading",
      "misprint_in_print", "medium", None,
      "n_β = g_β - v(h_β) lies in Γ(X,O_X'), as in 'n_β ∈ nilrad(Γ(X,O_X'))' of the preceding paragraph. The current layer already reads \\mathcal O_{X'}.",
      corrected="\\operatorname{nilrad}(\\Gamma(X,\\mathcal O_{X'}))"),
    F(606, "display after 'fonctorielle en T :', second term 'R^1(f_t)_*(O*_X_T)'",
      "'R^1(f_t)_*(O*_{X_T} )' with a small t (both scans; crops_606_610/w606_display1.png)",
      "'R^1(f_t)_*(\\mathcal O_{X_T}^{*})': the TeX keeps the printed reading",
      "misprint_in_print", "high", None,
      "The next term of the same display and the diagram of p. 605 have f_T. The current layer already reads f_T.",
      corrected="R^1(f_T)_*"),
    F(606, "same display, third term 'R^1(f_T)_*(O_X'_T)'",
      "'R^1(f_T)_*(O_{X'_T} )' without the star (both scans; crops_606_610/w606_display1.png: a gap where the first term has its star)",
      "'R^1(f_T)_*(\\mathcal O_{X'_T})': the TeX keeps the printed reading",
      "misprint_in_print", "high", None,
      "The sequence is that of the units (the bottom row of the diagram of p. 605 has R^1(f_T)_*(O*_{X'_T})). The current layer already reads \\mathcal O_{X'_T}^{*}.",
      corrected="R^1(f_T)_*(\\mathcal O_{X'_T}^{*})"),
    F(606, "'qui par passage aux faisceaux f.p.p.f. associés donne une suite exacte'",
      "no commas: 'qui par passage aux faisceaux f.p.p.f. associés donne' (both scans)",
      "'qui, par passage aux faisceaux f.p.p.f. associés, donne'",
      "punctuation", "high", fx("qui, par passage aux faisceaux f.p.p.f. associés, donne", "qui par passage aux faisceaux f.p.p.f. associés donne"),
      "Two commas added by the TeX."),
    F(606, "display '0 ⟶ V(E^v) ⟶ Pic_X/S ⟶ Pic_X'/S ⟶(u) V(Q) .'",
      "both Pic underlined (both scans; wit_606_half.png)",
      "'\\Pic_{X/S}' and '\\Pic_{X'/S}' plain",
      "underline", "high", fx("\\Pic_{X/S}" + NL + "  \\longrightarrow\\Pic_{X'/S}\\xrightarrow{u}", UP + "_{X/S}" + NL + "  \\longrightarrow" + UP + "_{X'/S}\\xrightarrow{u}"),
      PICNOTE),
    F(606, "'Si P = Ker(u), le monomorphisme P ↪ Pic_X'/S s'obtient'",
      "Pic underlined (both scans; crops_606_610/w606_pic.png)",
      "'\\(P\\hookrightarrow\\Pic_{X'/S}\\)' plain",
      "underline", "high", fx("monomorphisme \\(P\\hookrightarrow\\Pic_{X'/S}\\)", "monomorphisme \\(P\\hookrightarrow" + UP + "_{X'/S}\\)"),
      "The second 'P ↪ Pic_X'/S' of the paragraph ('il résulte que P ↪ Pic_X'/S est représentable', last line) is plain in both scans and stays plain."),
    F(606, "after the display ending 'V(Q) .': 'Si P = Ker(u), le monomorphisme'",
      "'Si P = Ker(u)' begins a new, indented paragraph (both scans; crops_606_610/w606_pic.png), unlike 'qui par passage' after the display before",
      "'\\]' followed directly by 'Si \\(P=\\Ker(u)\\)' (the paragraph runs on)",
      "other", "high", fx("\\]" + NL + "Si \\(P=\\Ker(u)\\)", "\\]" + NL + NL + "Si \\(P=\\Ker(u)\\)"),
      "Missing paragraph break."),
    # ---------------- page 607
    F(607, "'Enfin 0 → V(E^v) ⟶ Pic_X/S ⟶(w) P ⟶ 0 est un torseur'",
      "Pic underlined (both scans)",
      "'\\Pic_{X/S}\\xrightarrow{w}P' plain",
      "underline", "high", fx("\\Pic_{X/S}\\xrightarrow{w}P", UP + "_{X/S}\\xrightarrow{w}P"),
      PICNOTE),
    F(607, "'(voir : Oort, \"Commutative group schemes\", Proposition (17.4))'",
      "the title in straight double quotes, not underlined (both scans)",
      "'\\emph{Commutative group schemes}' without quotes",
      "other", "high", fx("\\emph{Commutative group schemes}", "«~Commutative group schemes~»"),
      "Emphasis the print does not have, quotes the TeX drops; written with the volume's guillemets, as «~splittage~» in the same sentence."),
    F(607, "Corollaire 3.3 i), first line: 'Si Pic_(zar)(X'/S) ⟶ Pic_(fppf)(X'/S) est un isomorphisme'",
      "both Pic underlined (both scans; wit_607_half.png)",
      "'\\Pic_{(\\zar)(X'/S)}\\to\\Pic_{(\\fppf)(X'/S)}' plain",
      "underline", "high", fx("Si \\(\\Pic_{(\\zar)(X'/S)}\\to\\Pic_{(\\fppf)(X'/S)}\\)", "Si \\(" + UP + "_{(\\zar)(X'/S)}\\to" + UP + "_{(\\fppf)(X'/S)}\\)"),
      "The second line of i), 'Pic_(zar)(X/S) ⟶ Pic_(fppf)(X/S) est un isomorphisme', is plain in both scans and stays plain. " + PICNOTE),
    F(607, "Corollaire 3.3 ii): 'si Pic(X'_T) ⟶ Pic_(zar)(X'/S)^(T) est surjectif'",
      "Pic_(zar)(X'/S)^(T) underlined, Pic(X'_T) plain (both scans)",
      "'\\to\\Pic_{(\\zar)(X'/S)}^{(T)}' plain",
      "underline", "high", fx("\\to\\Pic_{(\\zar)(X'/S)}^{(T)}", "\\to" + UP + "_{(\\zar)(X'/S)}^{(T)}"),
      PICNOTE),
    F(607, "Corollaire 3.3 ii): 'alors Pic(X_T) ⟶ Pic_(zar)(X/S)^(T) est surjectif'",
      "Pic_(zar)(X/S)^(T) underlined, Pic(X_T) plain (both scans)",
      "'\\to\\Pic_{(\\zar)(X/S)}^{(T)}' plain",
      "underline", "high", fx("\\to\\Pic_{(\\zar)(X/S)}^{(T)}", "\\to" + UP + "_{(\\zar)(X/S)}^{(T)}"),
      PICNOTE),
    F(607, "after Corollaire 3.3: 'En effet (i) résulte du diagramme suivant'",
      "'En effet (i)' begins a new, indented paragraph after item ii) (both scans)",
      "'\\end{enumerate}' followed directly by 'En effet (i)' (the paragraph runs on)",
      "other", "medium", fx("\\end{enumerate}" + NL + "En effet (i)", "\\end{enumerate}" + NL + NL + "En effet (i)"),
      "Missing paragraph break."),
    F(607, "diagram of (i), top row: 'Pic_(zar)(X/S) ⟶ Pic_(zar)(X'/S)'",
      "both Pic underlined (both scans)",
      "'\\Pic_{(\\zar)(X/S)}', '\\Pic_{(\\zar)(X'/S)}' plain",
      "underline", "high", fx("\\Pic_{(\\zar)(X/S)} \\arrow[r] \\arrow[d] &" + NL + "  \\Pic_{(\\zar)(X'/S)}", UP + "_{(\\zar)(X/S)} \\arrow[r] \\arrow[d] &" + NL + "  " + UP + "_{(\\zar)(X'/S)}"),
      PICNOTE),
    F(607, "diagram of (i), bottom row: 'Pic_(fppf)(X/S) → Pic_(fppf)(X'/S)'",
      "both Pic underlined (both scans; crops_606_610/w607_diag2.png)",
      "'\\Pic_{(\\fppf)(X/S)}', '\\Pic_{(\\fppf)(X'/S)}' plain",
      "underline", "high", fx("\\Pic_{(\\fppf)(X/S)} \\arrow[r] &" + NL + "\\Pic_{(\\fppf)(X'/S)}", UP + "_{(\\fppf)(X/S)} \\arrow[r] &" + NL + UP + "_{(\\fppf)(X'/S)}"),
      PICNOTE),
    F(607, "diagram of (ii), last entry 'H°(T,R^2f_*I_T)'",
      "no punctuation after 'H°(T,R^2f_*I_T)' (both scans; crops_606_610/w607_diag2b.png, m607_diag2_end.png)",
      "'H^0(T,R^2f_*I_T),' with a comma",
      "punctuation", "high", fx("H^0(T,R^2f_*I_T),", "H^0(T,R^2f_*I_T)"),
      "Comma added at the end of the diagram (the diagram of (i) does end with a printed comma)."),
    # ---------------- page 608
    F(608, "Corollaire 3.4: 'On suppose que Pic_X_réd/k possède un faisceau inversible universel'",
      "Pic underlined (both scans; wit_608_half.png)",
      "'\\(\\Pic_{X_{\\red}/k}\\)' plain",
      "underline", "high", fx("\\(\\Pic_{X_{\\red}/k}\\)", "\\(" + UP + "_{X_{\\red}/k}\\)"),
      "The other Pic of this page ('ouvert affine V de Pic_X/k' and the display f*: Pic_Y/S|V ⟶ Pic_X/S|V of Prop. 3.5) are plain in both scans and stay plain. " + PICNOTE),
    F(608, "'I_o= I ⊃ I_1 ⊃ ... ⊃ I_n=0'",
      "typed baseline dots '...' (both scans; crops_606_610/w608_dots.png)",
      "'\\supset\\cdots\\supset' (centred dots)",
      "symbol", "low", fx("\\supset\\cdots\\supset", "\\supset\\ldots\\supset"),
      "As GLOBAL_ISSUES 87 (Exposé V: typed baseline '...' written \\cdots, a volume decision); the only case on pp. 606-610."),
    # ---------------- page 609
    F(609, "3.6 Remarque: 'Pic_X_i-1/S ⟶ Pic_X_i/S ⟶ V(Q_i)'",
      "both Pic underlined (both scans; wit_609_half.png)",
      "'\\Pic_{X_{i-1}/S}', '\\Pic_{X_i/S}' plain",
      "underline", "high", fx("\\(\\Pic_{X_{i-1}/S}\\longrightarrow\\Pic_{X_i/S}", "\\(" + UP + "_{X_{i-1}/S}\\longrightarrow" + UP + "_{X_i/S}"),
      PICNOTE),
    F(609, "3.6 display: 'coker(Pic^0_X_s/s ⟶ Pic^0_Y_s/s)'",
      "both Pic underlined (both scans)",
      "'\\Pic^0_{X_s/s}', '\\Pic^0_{Y_s/s}' plain",
      "underline", "high", fx("\\Pic^0_{X_s/s}\\longrightarrow\\Pic^0_{Y_s/s}", UP + "^0_{X_s/s}\\longrightarrow" + UP + "^0_{Y_s/s}"),
      PICNOTE),
    F(609, "3.6 display: 'coker(...)'",
      "'coker' with a small c (both scans)",
      "'\\coker', which prints 'Coker': the first definition, \\providecommand{\\coker}{\\operatorname{Coker}} (main.tex about line 3735, folio 159), wins; the later \\providecommand{\\coker}{\\operatorname{coker}} (folios 221, 561, 594) do nothing",
      "word", "high", fx("\\coker\\bigl(", "\\operatorname{coker}\\bigl("),
      "The volume's only two \\coker are here and on p. 610 (both print 'coker'); the file already writes \\operatorname{coker}(\\pi_1-\\pi_2) on a later page."),
    # ---------------- page 610
    F(610, "start of page: '3) Pour i,j≥0, R^if_* O_X et R^jg_* O_XxYX sont plats sur S.'",
      "p. 609 ends with item '2) λ_* O_X = O_S, μ_*O_Y = O_S universellement.'; p. 610 begins with the item label '3)' (both scans: page_609_s4.png, page_610_s1.png; crops_606_610/wit_609_half.png, wit_610_half.png)",
      "the '\\item' of item 3) stands above the folio-610 marker (end of page_609.tex); page_610.tex begins 'Pour \\(i,j\\ge0\\)'",
      "marker", "high", None,
      "Page 610 really begins at the '\\item' of item 3). Exact edit in main.tex, both layers (diplomatic and current about line 15591 at 16:44 on 13 Nov; the file is being edited, use the string; it occurs once per layer): replace "
      + json.dumps(M610_OLD, ensure_ascii=False) + " by " + json.dumps(M610_NEW, ensure_ascii=False)
      + " (simulated in memory: crops_606_610/build_findings.py)."),
    F(610, "item 4): 'est exacte et coker(π_1-π_2) est un O_Y-module plat sur S'",
      "'coker' with a small c (both scans; wit_610_half.png)",
      "'\\coker(\\pi_1-\\pi_2)', which prints 'Coker' (see p. 609: \\coker is \\operatorname{Coker} by its first \\providecommand)",
      "word", "high", fx("\\coker(\\pi_1-\\pi_2)", "\\operatorname{coker}(\\pi_1-\\pi_2)"),
      "The other \\coker of the volume is on p. 609."),
]

# ---- checks
ok = True
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(606, 611)}
for p, txt in pages.items():
    assert "\r" not in txt, p
for i, f in enumerate(findings):
    if f["fix"] is None:
        continue
    old = f["fix"]["old"]
    n = pages[f["page"]].count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE", n, f["page"], repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in f["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", f["page"], repr(old))
# apply all fixes of each page in order; every old must still occur once when its turn comes
for p in pages:
    txt = pages[p]
    for f in findings:
        if f["page"] == p and f["fix"] is not None:
            old, new = f["fix"]["old"], f["fix"]["new"]
            if txt.count(old) != 1:
                ok = False
                print("SEQUENTIAL FAIL", p, repr(old))
            txt = txt.replace(old, new, 1)
    marker_lines = [l for l in txt.split("\n") if l.startswith("%%%%%%%%%%")]
    orig_markers = [l for l in pages[p].split("\n") if l.startswith("%%%%%%%%%%")]
    if marker_lines != orig_markers:
        ok = False
        print("MARKER CHANGED", p)
# marker simulation on both layers
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    n = t.count(M610_OLD)
    t2 = t.replace(M610_OLD, M610_NEW, 1)
    m = re.search(r"%%%%%%%%%%  scan idx 623  \|  folio 610  %%%%%%%%%%\n", t2)
    after = t2[m.end():m.end() + 60]
    before = t2[max(0, m.start() - 80):m.start()]
    line = t[:t.find(M610_OLD)].count("\n") + 1 if n else None
    print(layer, "marker-610 string count", n, "line", line, "| before:", repr(before[-60:]), "| after:", repr(after))
    if n != 1:
        ok = False
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
for f in findings:
    assert f["kind"] in kinds, f["kind"]
    assert f["confidence"] in {"high", "medium", "low"}
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f and f["fix"] is None
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in findings)
for p in range(606, 611):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("ALL CHECKS OK" if ok else "CHECKS FAILED", len(findings), "findings ->", OUT)
