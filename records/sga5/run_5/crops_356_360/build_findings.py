"""Build findings_356_360.json and check that every fix's old occurs exactly once in its page_NNN.tex.
Strings are raw; the character ⏎ stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
OUT = RUN / "findings_356_360.json"
PAGEFILE = {n: RUN / "b356_360" / f"page_{n}.tex" for n in range(356, 361)}
PAGEFILE[355] = RUN / "b351_355" / "page_355.tex"
NL = "⏎"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 355 (text printed on p. 356)
add(355, "display of Proposition 3.1 (printed at the top of p. 356)",
    r"'K(B) --K(i)--> K(A) --K(Q)--> K(A/B) --> 0' with nothing after the 0",
    r"K(\cB)\xrightarrow{K(i)}K(\cA)\xrightarrow{K(Q)}K(\cA/\cB)\longrightarrow 0.",
    "punctuation", "high",
    fx(r"\longrightarrow 0.⏎\]", r"\longrightarrow 0⏎\]"),
    r"The TeX adds a full stop at the end of the display. Printed on p. 356; filed under p. 355, where the display "
    r"stands until the folio-356 marker is moved (see the marker item of p. 356); the edit does not touch the move's "
    r"anchor '\['. Batch 351-355 may report the same display: apply once.")

# ---------------------------------------------------------------- p. 356
add(356, "top of the page: the display of Proposition 3.1",
    r"p. 356 begins with the display 'K(B) --K(i)--> K(A) --K(Q)--> K(A/B) --> 0', then 'Démonstration. Il est "
    r"clair ...'; p. 355 ends with 'Alors la suite suivante est exacte :' and blank space",
    r"the display '\[ K(\cB)\xrightarrow{K(i)}K(\cA)\xrightarrow{K(Q)}K(\cA/\cB)\longrightarrow 0. \]' and "
    r"'\end{statement}' end page_355.tex; the folio-356 marker follows them, before '\emph{Démonstration.}'",
    "marker", "high", None,
    r"Page 356 really begins at the '\[' that opens that display (inside the statement of Proposition 3.1, the line "
    r"after '... Alors la suite suivante est exacte:'; diplomatic s5.tex line 12198, current 12194; the marker stands "
    r"at 12203 and 12199). Exact fix: python -I move_marker.py 5 356 '\[' --before (simulated in memory on both "
    r"layers: the marker then stands on its own line between '... est exacte:' and '\[', and '\end{statement}', the "
    r"blank line and '\emph{Démonstration.}' follow the display). The anchor is the last '\[' above the marker, so run "
    r"the command once only (also if batch 351-355 reports the same move). Text not moved. The display's added full "
    r"stop is filed under p. 355.")

add(356, "'Démonstration.' (proof label)",
    r"'Démonstration' underlined, the full stop after the underline",
    r"\emph{Démonstration.} (the full stop inside the emphasis)",
    "underline", "high",
    fx(r"\emph{Démonstration.}", r"\emph{Démonstration}."),
    r"As the file's own '\emph{Démonstration}.' at s5.tex lines 1714 and 1888.")

add(356, "'D'autre part il existe une application évidente'",
    r"'D'autre part il existe' (no comma)",
    r"D'autre part, il existe",
    "punctuation", "high",
    fx(r"D'autre part, il existe", r"D'autre part il existe"),
    "The TeX adds a comma.")

add(356, "'Soient X,Y ∈ Ob(A/B) et supposons qu'ils sont isomorphes'",
    r"no comma after 'Ob(A/B)' (only a faint speck below the line)",
    r"Soient $X,Y\in\Ob(\cA/\cB)$, et supposons",
    "punctuation", "high",
    fx(r"$, et supposons", r"$ et supposons"),
    "The TeX adds a comma.")

add(356, "'(S est un système multiplicatif saturé).'",
    r"'saturé).' (the full stop after the parenthesis)",
    r"($S$ est un système multiplicatif saturé.)",
    "punctuation", "high",
    fx(r"saturé.)", r"saturé)."),
    "")

add(356, "'X_1 --s--> X , X_1 --t--> Y tel que s,t ∈ S'",
    r"nothing after Y (the sentence goes on with 'tel que')",
    r"X_1\xrightarrow{s}X,\qquad X_1\xrightarrow{t}Y,",
    "punctuation", "high",
    fx(r"\xrightarrow{t}Y,", r"\xrightarrow{t}Y"),
    "The TeX adds a comma at the end of the display.")

add(356, "'de la forme (X_1,X,Z,s,...) avec Z ∈ Ob B'",
    r"'(X_1,X,Z,s,...) avec' (no comma)",
    r"(X_1,X,Z,s,\ldots), (display), then 'avec'",
    "punctuation", "high",
    fx(r"s,\ldots),", r"s,\ldots)"),
    "The TeX adds a comma at the end of the display.")

add(356, "'ce qui résulte de fait qu'il existe un triangle distingué'",
    r"'résulte de fait' (for 'résulte du fait')",
    r"ce qui résulte de fait qu'il existe",
    "misprint_in_print", "high", None,
    r"The TeX keeps the printed reading.",
    corrected=r"ce qui résulte du fait qu'il existe")

add(356, "heading of section 4",
    r"'4. Comparaison avec le cas des catégories abéliennes.' (the title underlined, then a full stop)",
    r"\subsection*{4. Comparaison avec le cas des catégories abéliennes} (no full stop)",
    "punctuation", "high",
    fx(r"\subsection*{4. Comparaison avec le cas des catégories abéliennes}",
       r"\subsection*{4. Comparaison avec le cas des catégories abéliennes.}"),
    "The TeX drops the full stop that ends the underlined title.")

add(356, "every \\Ob of pp. 356-359 (convention, reported once)",
    r"'Ob' with a capital O: 'Ob(A/B) = Ob(A)', 'Z ∈ Ob B' (p. 356), 'Ob(K^{b,b}(C))' (p. 357), "
    r"'X,Y ∈ Ob C_o', 'Ker u ∈ Ob C_o', 'L ∈ Ob C_o' (p. 358), 'L_1 ∈ Ob C_o' (p. 359)",
    r"\Ob, which prints 'ob': the first definition in s5.tex, line 101 '\providecommand{\Ob}{\operatorname{ob}}' "
    r"(again lines 163, 269), wins; the later '\providecommand{\Ob}{\operatorname{Ob}}' (lines 226, 300) does nothing",
    "word", "high", None,
    r"Convention, not itemized (the macro, not the page text, differs from the print). Examples: p. 356 "
    r"'$\Ob(\cA/\cB)=\Ob(\cA)$', p. 357 '\Ob(K^{b,b}(\cC))', p. 358 'X,Y\in\Ob\cC_o'. Exposé VIII has \Ob on 17 lines "
    r"(s5.tex 12038-12503); Exposé III B (lines 4594-6711) and Exposé X onwards (12702, 12810, 13345-13702, "
    r"15195-15838) also use it, and line 12960 writes \operatorname{Ob} by hand: decide per exposé against the print "
    r"(e.g. \operatorname{Ob} for the 17 lines of Exposé VIII).")

add(356, "category letters of pp. 356-360 (convention, reported once)",
    r"plain typed capitals A, B, C, C_o (no underline, not script): 'Ob(A/B) = Ob(A)' (p. 356), "
    r"'K(C) --μ--> K(D^b(C))' (p. 357), 'C_o une sous-catégorie pleine de C' (p. 360)",
    r"\cA, \cB, \cC (\mathcal)",
    "font", "high", None,
    r"Convention of Exposé VIII, not itemized: 94 lines with \cC and 8 each with \cA, \cB (s5.tex 11996-12683). "
    r"Examples: p. 356 '$\Ob(\cA/\cB)=\Ob(\cA)$', p. 357 '$K(\cC)$', p. 360 '$\cC_o$ une sous-catégorie pleine de "
    r"$\cC$'. One decision for the exposé (compare SGA 6 global item 81).")

# ---------------------------------------------------------------- p. 357
add(357, "top of the page (and foot of p. 356): 'en-gendrée par les complexes bornés'",
    r"p. 356 ends 'la sous-catégorie pleine de D(C) en-'; p. 357 begins 'gendrée par les complexes bornés.'",
    r"page_356.tex ends '... pleine de $D(\cC)$ engendrée par les'; the folio-357 marker stands before 'complexes "
    r"bornés.'",
    "marker", "high", None,
    r"Page 357 really begins with 'gendrée', the second half of 'engendrée' divided at the page break ('par les' is "
    r"also on p. 357). Two commands, in this order, each once: python -I move_marker.py 5 357 'engendrée' --before, "
    r"then python -I marker_split_word.py 5 357 split en gendrée (simulated in memory on both layers: '... pleine de "
    r"$D(\cC)$ ' / 'en%' / marker / 'gendrée par les' / 'complexes bornés. ...'; diplomatic s5.tex line 12234, "
    r"current 12230). A second run of the move would go back to an earlier 'engendrée' 142,000 characters up. Text "
    r"not moved.")

add(357, "'D^b(C) ≅ K^{b,b}(C)/K^{b,∅}(C) , K^{b,∅}(C) étant la sous-catégorie épaisse'",
    r"the second index is a slashed circle, the stroke slanted and running through it (∅, the empty set: "
    r"complexes with no cohomology)",
    r"K^{b,\phi} twice (Greek phi)",
    "symbol", "medium",
    fx(r"/K^{b,\phi}(\cC),⏎\]⏎$K^{b,\phi}(\cC)$", r"/K^{b,\emptyset}(\cC),⏎\]⏎$K^{b,\emptyset}(\cC)$"),
    r"\emptyset as elsewhere in the file (lines 907, 1894). The only two \phi of Exposé VIII.")

add(357, "the isomorphism sign in 'D^b(C) ≅ K^{b,b}(C)/K^{b,∅}(C)'",
    r"a hand-drawn sign of three strokes: two wavy lines over a straight one (≊)",
    r"\simeq (one wavy line over a straight one)",
    "symbol", "medium",
    fx(r"D^b(\cC)\simeq K^{b,b}", r"D^b(\cC)\approxeq K^{b,b}"),
    r"Unlike the two-stroke ≃ of p. 359 (four times), which \simeq renders. \approxeq is amssymb (loaded). If the "
    r"volume treats hand-drawn isomorphism signs as one glyph, drop this item.")

add(357, "'Soit X^•=(X_i) ∈ Ob(K^{b,b}(C)) Si l'on pose'",
    r"no full stop after 'Ob(K^{b,b}(C))' at the end of the line; the next line begins 'Si l'on pose'",
    r"\Ob(K^{b,b}(\cC))$. Si l'on pose",
    "misprint_in_print", "medium",
    fx(r"(\cC))$. Si l'on pose", r"(\cC))$ Si l'on pose"),
    r"The print omits the full stop that ends the sentence; the TeX silently corrects. The space after the line's "
    r"last parenthesis is clean.",
    corrected=r"(\cC))$. Si l'on pose")

add(357, "'K(D^b(C)) --ν--> K(C) et il est immédiat de vérifier'",
    r"'K(C) et il est' (no comma)",
    r"K(D^b(\cC))\xrightarrow{\nu}K(\cC), (display), then 'et il est immédiat'",
    "punctuation", "high",
    fx(r"\xrightarrow{\nu}K(\cC),", r"\xrightarrow{\nu}K(\cC)"),
    "The TeX adds a comma at the end of the display.")

add(357, "'lorsque C est \"trop grosse\", il y a'",
    r"straight typewriter double quotes",
    r"«trop grosse»",
    "punctuation", "high",
    fx(r"«trop grosse»", r"``trop grosse''"),
    r"Guillemets for the print's straight quotes (the accepted forms are ``...'' and plain double quotes). Exposé VIII has "
    r"guillemets on 6 lines (s5.tex 12161, 12167, 12254, 12364, 12422, 12621).")

# ---------------------------------------------------------------- p. 358
add(358, "'alors Ker u ∈ Ob C_o .' / 'En raisonnant comme plus haut'",
    r"'En raisonnant comme plus haut, ...' opens a new, indented paragraph after condition (B)",
    r"runs on: 'alors $\operatorname{Ker}u\in\Ob\cC_o$. En raisonnant'",
    "other", "high",
    fx(r"$. En raisonnant", r"$.⏎⏎En raisonnant"),
    "Paragraph break of the print.")

add(358, "Proposition 4.1 (C): the diagram A --u--> B <--v-- L",
    r"a comma after the diagram (to the right of L)",
    r"no punctuation after \end{tikzcd}",
    "punctuation", "high",
    fx(r"\end{tikzcd}⏎\]⏎où $u$", r"\end{tikzcd},⏎\]⏎où $u$"),
    "The TeX drops the comma printed after the diagram.")

add(358, "'peut être complété en un diagramme commutatif :'",
    r"'commutatif :' (with a colon)",
    r"un diagramme commutatif (no colon)",
    "punctuation", "high",
    fx(r"un diagramme commutatif⏎\[", r"un diagramme commutatif:⏎\["),
    r"Written 'commutatif:' like the file's 'suivante:'.")

# ---------------------------------------------------------------- p. 359
add(359, "top of the page: 'tel que L_1 ∈ Ob C_o et que w est un épimorphisme.'",
    r"p. 359 begins 'tel que L_1 ∈ Ob C_o et que w est un épimorphisme.'; p. 358 ends with the square diagram "
    r"(A, B, L_1, L) and blank space",
    r"'tel que $L_1\in\Ob\cC_o$ et que $w$ est un' is the last line of page_358.tex; page_359.tex begins "
    r"'épimorphisme.'",
    "marker", "high", None,
    r"Page 359 really begins at 'tel que $L_1' (the line after the '\]' of the square diagram; diplomatic s5.tex "
    r"line 12299, current 12295). Exact fix: python -I move_marker.py 5 359 'tel que $L_1' --before (single quotes "
    r"keep the $ literal; simulated in memory on both layers: the marker then stands on its own line between '\]' and "
    r"'tel que'; a second run finds no anchor and changes nothing). Text not moved.")

add(359, "'... est un épimorphisme.' / 'Dans ces conditions, les foncteurs canoniques'",
    r"'Dans ces conditions, ...' opens a new, indented paragraph",
    r"runs on: 'épimorphisme. Dans ces conditions'",
    "other", "high",
    fx(r"épimorphisme. Dans ces conditions", r"épimorphisme.⏎⏎Dans ces conditions"),
    "Paragraph break of the print (inside the statement of Proposition 4.1). Independent of the marker move.")

add(359, "display 'D^b_o(C) --> D^b(C)' / 'D^-_o(C) --> D^-(C)'",
    r"two lines, no punctuation",
    r"D_o^b(\cC)\longrightarrow D^b(\cC),\qquad D_o^-(\cC)\longrightarrow D^-(\cC)",
    "punctuation", "high",
    fx(r"D^b(\cC),\qquad", r"D^b(\cC)\qquad"),
    "The TeX adds a comma between the two arrows (one line or two is layout).")

add(359, "'un critère de Verdier ([2], 4-2 Théorème)'",
    r"'4-2' with a hyphen",
    r"4--2 (en dash)",
    "punctuation", "high",
    fx(r"4--2 Théorème", r"4-2 Théorème"),
    "")

add(359, "Corollaire, display 'K(C_o) ≃ K_o(C) ≃ K(D^b(C_o)) ≃ K(D^b(C)_o) .(*)'",
    r"the (*) after the full stop is a raised footnote call; the footnote '(*) cf. (SGA 6 IV 1.6) .' stands at the "
    r"foot of p. 359",
    r"\tag{*} (an equation number) on this display; the \footnote is attached to the Observation's display "
    r"'K_{\cC_o}(\cC)\simeq K(\cC).'",
    "other", "high",
    fx(r"K(D^b(\cC)_o).⏎\tag{*}", r"K(D^b(\cC)_o).\footnote{cf. (SGA 6 IV 1.6).}"),
    r"Apply together with the next item (which removes the misplaced \footnote): one alone gives the footnote twice. "
    r"\footnote in a display as the file's line 12514; the file numbers its footnotes, so the (*) mark is not kept.")

add(359, "Observation, display 'K_{C_o}(C) ≃ K(C) .'",
    r"no footnote call at this display",
    r"\footnote{cf. (SGA 6 IV 1.6).} on the line after the display's '\]'",
    "extra", "high",
    fx(r"\]⏎\footnote{cf. (SGA 6 IV 1.6).}", r"\]"),
    r"Apply together with the previous item, which puts the footnote at its printed place.")

add(359, "'Observation. Supposons que la sous-catégorie C_o'",
    r"'Observation.' not underlined",
    r"\emph{Observation.}",
    "underline", "high",
    fx(r"\emph{Observation.} Supposons", r"Observation. Supposons"),
    r"In Exposé VIII \emph stands for the print's underline ('Démonstration', 'Exemples', 'Remarques' are "
    r"underlined); this label is not.")

# ---------------------------------------------------------------- p. 360
add(360, "heading of section 5",
    r"'5. Complexes pseudo-cohérents.' (the title underlined, then a full stop)",
    r"\subsection*{5. Complexes pseudo-cohérents} (no full stop)",
    "punctuation", "high",
    fx(r"\subsection*{5. Complexes pseudo-cohérents}", r"\subsection*{5. Complexes pseudo-cohérents.}"),
    "The TeX drops the full stop that ends the underlined title.")

add(360, "'seront appelés des complexes C_o-pseudo-cohérents.'",
    r"'pseudo-cohérents' underlined (the defined term; 'C_o-' and the full stop not)",
    r"$\cC_o$-pseudo-cohérents. (no underline markup)",
    "underline", "high",
    fx(r"$\cC_o$-pseudo-cohérents. Donc", r"$\cC_o$-\emph{pseudo-cohérents}. Donc"),
    r"\emph, the file's command for the print's underline in Exposé VIII.")

add(360, "'des objets de la sous-catégorie D^-_o(C)_coh , est isomorphe à un triangle'",
    r"a comma after 'D^-_o(C)_coh'",
    r"$D_o^-(\cC)_{\coh}$ est isomorphe (no comma)",
    "punctuation", "high",
    fx(r"$D_o^-(\cC)_{\coh}$ est isomorphe", r"$D_o^-(\cC)_{\coh}$, est isomorphe"),
    "The TeX drops the printed comma.")

add(360, "'et si le triangle :'",
    r"'le triangle :' (with a colon)",
    r"et si le triangle (no colon)",
    "punctuation", "high",
    fx(r"et si le triangle⏎\[", r"et si le triangle:⏎\["),
    r"Written 'triangle:' like the file's 'suivante:'.")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = PAGEFILE[d["page"]].read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", d["page"], repr(d["fix"]["old"]))
# fixes on one page must not overlap
for p in sorted(PAGEFILE):
    t = PAGEFILE[p].read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, a[2], "|", b[2])
    # apply all fixes of the page in memory to be sure they compose
    t2 = t
    for d in F:
        if d["page"] == p and d["fix"]:
            assert t2.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t2 = t2.replace(d["fix"]["old"], d["fix"]["new"], 1)
print("checks ok" if ok else "CHECKS FAILED")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted({d["page"] for d in F}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "findings")
