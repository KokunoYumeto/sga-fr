import json, pathlib, sys, io
from collections import defaultdict, Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b161_165")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_161_165.json")
NL = "\n"


def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


L = []
# ---------------- page 161
L.append(F(161, "start of the page, first word",
  "Page 161 begins with 'plexes acycliques', the second half of 'com-plexes' divided at the page break (both scans).",
  "The folio-161 marker stands before the whole word 'complexes'.",
  "marker", "medium", None,
  "Page 161 really begins with 'plexes'. Split the word at the marker as at folios 18, 36, 46 and 54: "
  "python -I marker_split_word.py 6 161 split com plexes (simulated on both layers: '... formée des' / 'com%' / marker / "
  "'plexes acycliques, est pleinement ...'). The checker of p. 160 may report the same boundary: apply once."))
L.append(F(161, "Preuve a), display 0 -> L -> L^0 -> ... -> L^m -> 0",
  "L^o ---> . . . ---> L^m: three typed baseline stops (both scans).",
  r"L^0\longrightarrow\cdots\longrightarrow L^m",
  "symbol", "medium", fx(r"L^0\longrightarrow\cdots\longrightarrow L^m", r"L^0\longrightarrow\ldots\longrightarrow L^m"),
  r"Typed baseline stops written \cdots; same fix as pp. 79, 80, 86, 95, 102, 127 (\cdots -> \ldots)."))
L.append(F(161, "b), 'On a donc un suite exacte'",
  "'On a donc un suite exacte' (both scans).",
  "On a donc un suite exacte",
  "misprint_in_print", "high", None,
  "Gender slip of the typescript (suite is feminine). The TeX keeps the printed reading; the corrected layer "
  "(current main.tex line 3802) also still reads 'un suite'.",
  corrected="une suite exacte"))
L.append(F(161, "statements of Exposé II (here: end of Prop. 1.1 c) and Prop. 1.2)",
  "The typescript underlines the word groups of every statement, e.g. Prop. 1.2: 'Supposons', 'localement relevable dans', "
  "'et', 'localement stable par noyau d'épimorphisme', 'et faisons les hypo-'.",
  r"Statements in roman, no \emph or \underline: 'Supposons $\mathcal C_0$ localement relevable dans $\mathcal C$ (I 1.2) "
  r"et localement stable par noyau d'épimorphisme (I 1.2), et faisons les hypothèses'.",
  "underline", "high", None,
  r"Convention of this TeX for Exposé II, not itemized: in main.tex lines 3743-4777 \emph occurs only for 'Preuve' and seven "
  r"isolated terms, never for a statement (Exposé I sets statements in \emph). Three examples: p. 161 Prop. 1.2 'Supposons ... "
  r"localement relevable dans ...'; p. 163 Lemme 2.1.1 'Soient $(S,A)$ un topos annelé, et $S\in\Ob S$. On suppose que $S$ est "
  r"quasi-compact'; p. 165 Lemme 2.1.3 'Soient ... des catégories abéliennes, et ... un foncteur exact'. Also Prop. 1.1 c) "
  r"(top of p. 161), Prop. 1.2 a)-d) (p. 162), Lemme 2.1.2 (pp. 163-164). One decision for the exposé."))
# ---------------- page 162
L.append(F(162, "start of the page",
  "Page 162 begins with 'thèses (1.1 (i) et (ii) respée). Notons ...'; 'hypo-' ends p. 161 (both scans).",
  "'hypothèses (1.1 (i) et (ii)' stands at the end of p. 161, above the folio-162 marker; the TeX of p. 162 begins at 'respée).'.",
  "marker", "high", None,
  "Move the folio-162 marker before the divided word and split it, in this order: python -I move_marker.py 6 162 "
  "'hypothèses (1.1' --before, then python -I marker_split_word.py 6 162 split hypo thèses (simulated in this order on both "
  "layers: '... et faisons les ' / 'hypo%' / marker / 'thèses (1.1 (i) et (ii)' / 'respée). Notons ...'). 'respée' is the "
  "volume's word for the resp. variant, not a misprint."))
L.append(F(162, "Preuve b), display of the truncated complex",
  "E^{m+1} ---> . . . ---> E^n: typed baseline stops (both scans).",
  r"E^{m+1}\longrightarrow\cdots\longrightarrow E^n",
  "symbol", "medium", fx(r"E^{m+1}\longrightarrow\cdots\longrightarrow E^n", r"E^{m+1}\longrightarrow\ldots\longrightarrow E^n"),
  r"As on p. 161 and pp. 79-127 (\cdots -> \ldots)."))
# ---------------- page 163
L.append(F(163, "proof of 1.2, parts c) and d)",
  "'d) Le fait que ...' begins a new paragraph at the margin, after the same extra space that separates a) and b) on p. 162 (both scans).",
  "'(I 4.12.2). d) Le fait que' runs on in the paragraph of c).",
  "other", "medium", fx("(I 4.12.2). d) Le fait", "(I 4.12.2)." + NL + NL + "d) Le fait"),
  "The TeX sets the other proof parts as paragraphs (b), c) on p. 161, b) on p. 162). '(I 4 12.2)': the stop is missing in "
  "both scans; the TeX's 4.12.2 stands (not reported)."))
L.append(F(163, "Lemme 2.1.1, reference '(cf. EGA 0_I 5.2.3)'",
  "(cf. EGA O_I 5.2.3): no comma after the subscript I (both scans).",
  r"(cf. EGA $0_{\mathrm I}$, 5.2.3)",
  "punctuation", "high", fx(r"EGA $0_{\mathrm I}$, 5.2.3", r"EGA $0_{\mathrm I}$ 5.2.3"),
  "The TeX adds a comma."))
L.append(F(163, "Lemme 2.1.2, 'S ∈ ob S, C'_S une sous-catégorie additive'",
  "C'_S typed without the underline (both scans), unlike every other category letter on pp. 161-165; on p. 164 C'_S is underlined throughout.",
  r"$\mathcal C'_S$ une sous-catégorie",
  "underline", "low", fx(r"$\mathcal C'_S$ une sous-catégorie", r"$C'_S$ une sous-catégorie"),
  r"The TeX writes \mathcal C for the underlined typed C; this one C' has no underline (typist's omission). Low: tied to the "
  r"pending decision on the category letter."))
# ---------------- page 164
L.append(F(164, "start of the page",
  "Page 164 begins with the display 'H^1(S,F) = 0   pour tout F ∈ ob C'_S .'.",
  r"The display's opening \[ stands at the end of p. 163, above the folio-164 marker (the marker sits inside the display).",
  "marker", "high", None,
  r"Move the folio-164 marker above \[: python -I move_marker.py 6 164 '\[' --before (single quotes; simulated on both layers: "
  r"'... On suppose que' / marker / \[ / H^1(S,F)=0\quad ...), as at folio 11."))
L.append(F(164, "Lemme 2.1.2 a), 'telle que Hom(G,E) ∈ ob C'_S'",
  "Hom underlined (sheaf Hom; the underline covers Hom only), both scans.",
  r"telle que $\operatorname{Hom}(G,E)",
  "underline", "high", fx(r"telle que $\operatorname{Hom}(G,E)", r"telle que $\underline{\Hom}(G,E)"),
  r"Underlined Hom written \underline{\Hom} as on pp. 89, 116-118; the same sheaf Hom is underlined in the proof below and on p. 165."))
L.append(F(164, "Preuve a), spectral sequence, E_2 term",
  "H^p(S,Ext^q(G,E)) with the typed Ext underlined (sheaf Ext), both scans.",
  r"H^p(S,\mathcal{E}xt^q(G,E))",
  "underline", "high", fx(r"\mathcal{E}xt^q(G,E)", r"\underline{\Ext}^q(G,E)"),
  r"The print has an underlined typed Ext, not a script E; \underline{\Ext} is the file's form (main.tex has it once). The E "
  r"inside (G,E) is struck over another letter in the typescript; E is the corrected reading."))
L.append(F(164, "Preuve a), spectral sequence, abutment",
  "Ext^*(G,E): the superscript is the typed asterisk, the same glyph as the tags (*) and (**) on p. 165 (both scans).",
  r"\Ext^{n}(G,E)",
  "symbol", "high", fx(r"\Ext^{n}(G,E)", r"\Ext^{*}(G,E)"),
  "The TeX reads n for the printed asterisk."))
L.append(F(164, "Preuve a), isomorphism H^1(S,Hom(G,E)) ≃ Ext^1(G,E)",
  "Hom underlined (both scans).",
  r"H^1(S,\operatorname{Hom}(G,E))",
  "underline", "high", fx(r"H^1(S,\operatorname{Hom}(G,E))", r"H^1(S,\underline{\Hom}(G,E))"),
  "Sheaf Hom, underlined in the print."))
# ---------------- page 165
L.append(F(165, "first paragraph, 'on a Hom(G,E) ∈ ob C'_S'",
  "Hom underlined (both scans).",
  r"on a $\operatorname{Hom}(G,E)\in\Ob\mathcal C'_S$",
  "underline", "high", fx(r"on a $\operatorname{Hom}(G,E)\in", r"on a $\underline{\Hom}(G,E)\in"),
  "Sheaf Hom, as on p. 164."))
L.append(F(165, "'D'autre part ... le foncteur exact à gauche Hom_{A_S}(.,G)'",
  "Hom_{A_S}(.,G): the placeholder is a typed full stop on the line.",
  r"\operatorname{Hom}_{A_S}(\cdot,G)",
  "symbol", "medium", fx(r"\operatorname{Hom}_{A_S}(\cdot,G)", r"\operatorname{Hom}_{A_S}(.,G)"),
  r"The file writes the typed placeholder as '.' elsewhere (\underline{\Hom}(P,.), main.tex line 1939)."))
L.append(F(165, "same sentence, '(resp. Hom_{A(S)}(.,Γ_S(F)))'",
  "Hom_{A(S)}(.,Γ_S(F)): typed full stop as placeholder.",
  r"\operatorname{Hom}_{A(S)}(\cdot,\Gamma_S(F))",
  "symbol", "medium", fx(r"\operatorname{Hom}_{A(S)}(\cdot,\Gamma_S(F))", r"\operatorname{Hom}_{A(S)}(.,\Gamma_S(F))"),
  "As the previous entry. The misprint F (for G) in this expression is the next entry (fix null)."))
L.append(F(165, "same sentence, '(resp. Hom_{A(S)}(.,Γ_S(F)))'",
  "Hom_{A(S)}(.,Γ_S(F)) (both scans).",
  r"(resp. $\operatorname{Hom}_{A(S)}(\cdot,\Gamma_S(F))$)",
  "misprint_in_print", "high", None,
  r"The functor applied to (**) is Hom_{A(S)}(.,Γ_S(G)): the bottom row of the diagram has Γ_S(G). The TeX keeps the printed "
  r"reading; the corrected layer already reads \Gamma_S(G).",
  corrected=r"\operatorname{Hom}_{A(S)}(.,\Gamma_S(G))"))
L.append(F(165, "diagram, bottom row, first Hom",
  "0 -> Hom_{A(S)}(F,G) -> Hom_{A(S)}(A(S)^{(J)},Γ_S(G)) -> ... (both scans).",
  r"\operatorname{Hom}_{A(S)}(F,G) \arrow[r]",
  "misprint_in_print", "medium", None,
  "Applying Hom_{A(S)}(.,Γ_S(G)) to (**) gives Hom_{A(S)}(Γ_S(F),Γ_S(G)) on the left; the print writes (F,G). The TeX keeps "
  "the printed reading; the corrected layer still has (F,G).",
  corrected=r"\operatorname{Hom}_{A(S)}(\Gamma_S(F),\Gamma_S(G))"))
L.append(F(165, "after the diagram, 'sont visiblement des isomorphismes il en est donc de même'",
  "'des isomorphismes' ends the line with no punctuation; the next line begins 'il en est donc' (both scans).",
  "des isomorphismes il en est donc",
  "misprint_in_print", "medium", None,
  "A stop between the two clauses is missing in the print (';' or ','). The TeX keeps the printed reading, as does the "
  "corrected layer (line 3920).",
  corrected="isomorphismes ; il en est donc"))
L.append(F(165, "Lemme 2.1.3, 'Soient A et B des catégories abéliennes'",
  "Plain typed A and B, not underlined (both scans).",
  r"Soient $\mathcal A$ et $\mathcal B$ des",
  "font", "high", fx(r"Soient $\mathcal A$ et $\mathcal B$ des", r"Soient $A$ et $B$ des"),
  r"The abelian categories of Lemme 2.1.3 are plain typed A, B in the whole statement (unlike the underlined C of the "
  r"S-categories); the TeX writes \mathcal A, \mathcal B. Five more entries follow; the proof on p. 166 continues the notation."))
L.append(F(165, "Lemme 2.1.3, 'φ : A -> B'",
  "Plain A and B.",
  r"$\varphi:\mathcal A\to\mathcal B$",
  "font", "high", fx(r":\mathcal A\to\mathcal B$", r":A\to B$"),
  "As the previous entry."))
L.append(F(165, "a), 'Pour M ∈ ob A'",
  "Plain A.",
  r"$M\in\Ob\mathcal A$",
  "font", "high", fx(r"$M\in\Ob\mathcal A$", r"$M\in\Ob A$"),
  "As above."))
L.append(F(165, "(i), 'pour tout L ∈ ob A, la flèche canonique (induite par φ)'",
  "Plain A.",
  r"$L\in\Ob\mathcal A$, la flèche canonique (induite",
  "font", "high", fx(r"$L\in\Ob\mathcal A$, la flèche canonique (", r"$L\in\Ob A$, la flèche canonique ("),
  "As above."))
L.append(F(165, "(i), display Ext^n_A(L,M) -> Ext^n_B(φ(L),φ(M))",
  "Plain subscripts A and B.",
  r"\Ext^n_{\mathcal A}(L,M)\longrightarrow\Ext^n_{\mathcal B}",
  "font", "high", fx(r"\Ext^n_{\mathcal A}(L,M)\longrightarrow\Ext^n_{\mathcal B}", r"\Ext^n_{A}(L,M)\longrightarrow\Ext^n_{B}"),
  "As above."))
L.append(F(165, "(ii), 'pour tout L ∈ ob A, la flèche canonique' (last line)",
  "Plain A.",
  r"$L\in\Ob\mathcal A$, la flèche canonique",
  "font", "high", fx(r"$L\in\Ob\mathcal A$, la flèche canonique" + NL, r"$L\in\Ob A$, la flèche canonique" + NL),
  "As above; the 'old' ends with the line break before the folio-166 marker (the marker line itself is not touched)."))
L.append(F(165, "Lemme 2.1.3, 'et φ : A -> B'",
  "The drawn phi is the closed form, a circle crossed by a stroke (both scans).",
  r"et $\varphi:\mathcal A\to\mathcal B$",
  "symbol", "medium", fx(r"et $\varphi", r"et $\phi"),
  r"Closed form, which TeX sets as \phi (as changed on pp. 3 and 12); two more entries follow."))
L.append(F(165, "(i), '(induite par φ)'",
  "Closed-form phi.",
  r"(induite par $\varphi$)",
  "symbol", "medium", fx(r"par $\varphi$)", r"par $\phi$)"),
  "As the previous entry."))
L.append(F(165, "(i), display, 'Ext^n_B(φ(L),φ(M))'",
  "Closed-form phi, twice.",
  r"(\varphi(L),\varphi(M))",
  "symbol", "medium", fx(r"(\varphi(L),\varphi(M))", r"(\phi(L),\phi(M))"),
  "As above."))

# ---- checks: every old occurs exactly once in its page file; no marker text; no overlaps
bad = 0
spans = defaultdict(list)
for f in L:
    if f["fix"] is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", f["page"], n, repr(f["fix"]["old"]))
    if "%%%%%%%%%%" in f["fix"]["old"] or "%%%%%%%%%%" in f["fix"]["new"]:
        bad += 1
        print("MARKER IN FIX", f["page"])
    i = t.find(f["fix"]["old"])
    spans[f["page"]].append((i, i + len(f["fix"]["old"]), f["where"]))
for p, s in spans.items():
    s.sort()
    for a, b in zip(s, s[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP", p, a[2], "|", b[2])
print("findings", len(L), "bad", bad)
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in L)
for p in range(161, 166):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
if bad == 0:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
