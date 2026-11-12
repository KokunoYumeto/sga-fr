"""Write findings_061_065.json (SGA 5, folios 61-65) from the entries below.
usage: python -I make_findings.py"""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
OUT = here.parent / "findings_061_065.json"

NL = "\n"
DA_NOTE = (r"p. 55 (Appendice 1.1) writes this notation as printed, $\D({}_A X)$; on pp. 61-63 the TeX writes all seven "
           r"as \D_A(X), \D_A^+(X): each is listed.")

F = []


def add(page, where, scan, tex, kind, confidence, fix, note="", corrected=None):
    e = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        e["corrected"] = corrected
    e["note"] = note
    F.append(e)


# ---------------------------------------------------------------- p. 61
add(61, "top of the page: display (4.1) and 'est un'",
    "p. 61 begins with the display '(4.1) (μ_n)_Y^{⊗-d} [-2d] ⟶ ℝi^!(Z/nZ)_X', then 'est un isomorphisme.'",
    "page_061.tex begins with 'isomorphisme.'; the display (4.1) and 'est un' stood at the end of page_060.tex",
    "marker", "high", None,
    r"Already repaired: the folio-61 marker was moved by the pp. 56-60 report (with its fix of the (4.1) display). "
    r"Verified in both layers at 17:16: the marker stands right before '\begin{equation}\tag{4.1}' (s5.tex line 1663) "
    r"and the display now reads (\mu_n)_Y^{\otimes -d}[-2d] as printed. Nothing left to do; re-running "
    r"move_marker.py 5 61 '\begin{equation}\tag{4.1}' --before is a no-op (anchor not found).")
add(61, "'Alors, pour tout F ∈ ob D^+(_A X), on peut définir'",
    "D^+(_A X): the A is a left subscript of X inside the parentheses",
    r"\D_A^+(X)", "formula", "high",
    {"old": r"pour tout $F\in\ob\D_A^+(X)$, on peut", "new": r"pour tout $F\in\ob\D^+({}_A X)$, on peut"},
    DA_NOTE)
add(61, "same sentence, 'une flèche canonique de D^+(_A X) :'",
    "D^+(_A X), as above", r"\D_A^+(X)", "formula", "high",
    {"old": r"canonique de $\D_A^+(X)$:", "new": r"canonique de $\D^+({}_A X)$:"}, "")
add(61, "'Alors, la flèche (4.2) se définit pour tout F ∈ ob D(_A X).'",
    "D(_A X)", r"\D_A(X)", "formula", "high",
    {"old": r"pour tout $F\in\ob\D_A(X)$.", "new": r"pour tout $F\in\ob\D({}_A X)$."}, "")
add(61, "'Composant (4.1) et (4.2), on a donc, pour F ∈ ob D^+(_A X), une'",
    "D^+(_A X)", r"\D_A^+(X)", "formula", "high",
    {"old": r"pour $F\in\ob\D_A^+(X)$, une", "new": r"pour $F\in\ob\D^+({}_A X)$, une"}, "")
add(61, "display (4.3), printed at the top of p. 62 (it stands under the folio-61 marker)",
    "(4.3)  i^*(F) ⊗^L_{Z/nZ} (μ_n)_Y^{⊗-d} [-2d] ⟶ ℝi^!(F) . : the parenthesis closes after μ_n; Y is a "
    "subscript and ⊗-d a superscript after it, as in (4.1)",
    r"(\mu_n^{\otimes -d})_Y[-2d]\longrightarrow \R i^!(F).", "formula", "high",
    {"old": r"(\mu_n^{\otimes -d})_Y[-2d]\longrightarrow \R i^!(F)",
     "new": r"(\mu_n)_Y^{\otimes -d}[-2d]\longrightarrow \R i^!(F)"},
    "Filed under p. 61 because the display stands in page_061.tex; the old stays unique on p. 62 after the "
    "folio-62 marker move. The typed n under μ is struck over another character (a typist's correction): it "
    "reads n. Same fix as the logged (4.1) fix of p. 60 and the p. 64 restatement below.")

# ---------------------------------------------------------------- p. 62
add(62, "top of the page: display (4.3)",
    "p. 62 begins with the display '(4.3) i^*(F) ⊗^L_{Z/nZ} (μ_n)_Y^{⊗-d} [-2d] ⟶ ℝi^!(F) .', then the indented "
    "paragraph 'Supposons que A_X soit ...'; p. 61 ends with 'Composant (4.1) et (4.2), on a donc, pour "
    "F ∈ ob D^+(_A X), une flèche canonique' (blank below)",
    r"the display (4.3) (s5.tex lines 1688-1690 at 17:16) ends page_061.tex; the folio-62 marker (line 1691) "
    r"follows it",
    "marker", "high", None,
    r"Page 62 really begins at s5.tex line 1688 '\begin{equation}\tag{4.3}' (at 17:16). Exact fix: "
    r"python -I move_marker.py 5 62 '\begin{equation}\tag{4.3}' --before (single quotes keep the backslashes; "
    r"simulated in memory on both layers at 17:16: the marker then stands between 'une flèche canonique' and "
    r"'\begin{equation}\tag{4.3}'). Text not moved. The (4.3) fix is filed under p. 61; its old stays unique "
    r"after the move.")
add(62, "'Supposons que A_X soit localement constant' (after the display (4.3))",
    "'Supposons que' is indented: a new paragraph after the display",
    r"\end{equation} (end of page_061.tex), the marker line, then 'Supposons que' with no blank line: the "
    r"paragraph runs on from the display, unindented",
    "other", "high",
    {"old": r"Supposons que $A_X$", "new": NL + r"Supposons que $A_X$"},
    "The blank line after the marker comment line gives the paragraph break; it stays right after the folio-62 "
    "marker move (the display then ends just before it). Independent of the underline fix of the same line.")
add(62, "'Supposons que A_X soit localement constant, et soit'",
    "'localement constant,' underlined; the rule runs under the comma",
    "soit localement constant, et (no underline)", "underline", "high",
    {"old": r"soit localement constant, et", "new": r"soit \emph{localement constant,} et"},
    r"\emph is this file's command for the print's underline in the appendix (\emph{constructible}, "
    r"\emph{Preuve}, \emph{Démonstration}). The TeX has none of the four underlines of this statement.")
add(62, "same sentence, 'et soit F ∈ ob D^+(_A X) tel que, pour tout i'",
    "D^+(_A X)", r"\D_A^+(X)", "formula", "high",
    {"old": r"$F\in\ob\D_A^+(X)$ tel que, pour", "new": r"$F\in\ob\D^+({}_A X)$ tel que, pour"},
    "As on p. 61.")
add(62, "'H^i(F) soit un A_X-Module localement constant.'",
    "'localement constant' underlined; the rule stops before the full stop",
    "-Module localement constant. (no underline)", "underline", "high",
    {"old": r"-Module localement constant.", "new": r"-Module \emph{localement constant}."}, "")
add(62, "'Alors, si i^! est de dimension cohomologique finie, la flèche (4.2) (et par suite'",
    "underlined from 'si' to '(4.2)', the comma after 'finie' included; 'Alors,' and the parenthesis "
    "'(et par suite la flèche (4.3) si (Y,X) satisfait à la pureté)' are not",
    "no underline", "underline", "high",
    {"old": r"si $i^!$ est de dimension cohomologique finie, la flèche (4.2)",
     "new": r"\emph{si $i^!$ est de dimension cohomologique finie, la flèche (4.2)}"}, "")
add(62, "'... satisfait à la pureté) est un isomorphisme.'",
    "'est un isomorphisme' underlined; the rule stops before the full stop",
    "pureté) est un isomorphisme. (no underline)", "underline", "high",
    {"old": r"pureté) est un isomorphisme.", "new": r"pureté) \emph{est un isomorphisme}."}, "")
add(62, "Définition 4.4, 'étant donné (localement constant, annulé par n) nous dirons'",
    "no comma after the closing parenthesis (it ends the line; the next line begins 'nous dirons')",
    r"annulé par $n$), nous dirons", "punctuation", "high",
    {"old": r"annulé par $n$), nous", "new": r"annulé par $n$) nous"}, "Comma added by the TeX.")
add(62, "Définition 4.4, 'si, pour tout F ∈ ob D^+(_A X) tel que les H^i(F)'",
    "D^+(_A X)", r"\D_A^+(X)", "formula", "high",
    {"old": r"pour tout $F\in\ob\D_A^+(X)$ tel que les", "new": r"pour tout $F\in\ob\D^+({}_A X)$ tel que les"},
    "As on p. 61.")
add(62, "'D'après ce qu'on a vu, pour que (Y,X) satisfasse à la pureté au sens fort'",
    "begins a new, indented paragraph after '... satisfait à la pureté au sens fort.'",
    "run on in the paragraph 'Nous dirons que le théorème de pureté ...'", "other", "high",
    {"old": r"au sens fort. D'après", "new": r"au sens fort." + NL + NL + r"D'après"}, "")

# ---------------------------------------------------------------- p. 63
add(63, "section heading",
    "'5. Majoration de la dimension quasi-injective.' (underlined, with a full stop)",
    r"\subsection*{5. Majoration de la dimension quasi-injective}", "punctuation", "high",
    {"old": r"quasi-injective}", "new": r"quasi-injective.}"},
    "As the logged heading fixes of § 3 (p. 21) and § 5 (p. 50).")
add(63, "Proposition 5.1, '(Conditions toutes vérifiées si X est lisse'",
    "Conditions with a capital C after the parenthesis", "(conditions toutes vérifiées", "word", "high",
    {"old": r"(conditions toutes", "new": r"(Conditions toutes"}, "Capital against small letter.")
add(63, "Proposition 5.1, 'Soit F ∈ ob D^+(_A X) tel que les H^i(F)'",
    "D^+(_A X)", r"\D_A^+(X)", "formula", "high",
    {"old": r"Soit $F\in\ob\D_A^+(X)$", "new": r"Soit $F\in\ob\D^+({}_A X)$"}, "As on p. 61.")
add(63, "proof of Proposition 5.1, its label",
    "'Démonstration. Il n'y a qu'à ...': 'Démonstration' underlined; the rule stops before the full stop",
    r"\emph{Démonstration.}", "underline", "high",
    {"old": r"\emph{Démonstration.}", "new": r"\emph{Démonstration}."},
    r"Proof label in the print's form (as the global '\emph{Preuve} :'): here a full stop, not a colon.")
add(63, "end of the page and top of p. 64: '(A_Y = i^*A_X).' then 'Or on a l'isomorphisme de dualité'",
    "p. 64 begins 'Or on a' at the left margin, not indented (new paragraphs on these pages are indented: "
    "'Supposons que', 'En effet', 'Reste à prouver'): the argument goes on in the same paragraph",
    r"page_063.tex ends with '($A_Y=i^*A_X$).' and a blank line, so 'Or on a' starts a new paragraph",
    "other", "low",
    {"old": r"($A_Y=i^*A_X$)." + NL + NL, "new": r"($A_Y=i^*A_X$)." + NL},
    "The line break itself is the page end (p. 63 ends early, blank below). Drop if paragraph breaks at a page "
    "end are left to the transcription.")

# ---------------------------------------------------------------- p. 64
add(64, "first display, 'R Hom(i_!(M),F) <~ R i_* R Hom(M, R i^!F) .'",
    "the sign is a left-pointing arrow with a tilde over it (arrowhead at the left end of the bar)",
    r"\R\underline{\Hom}(i_!(M),F)\simeq \R i_*...", "symbol", "high",
    {"old": r"(i_!(M),F)\simeq", "new": r"(i_!(M),F)\xleftarrow{\sim}"},
    r"\xleftarrow is amsmath, like the file's \xrightarrow{\sim}.")
add(64, "second display, the isomorphism (4.3)",
    "i^*(F) ⊗^L_{Z/nZ} (μ_n)_Y^{⊗-d}[-2d] ⟶~ ℝi^!(F) . : the parenthesis closes after μ_n",
    r"(\mu_n^{\otimes -d})_Y[-2d]\xrightarrow{\sim}", "formula", "high",
    {"old": r"(\mu_n^{\otimes -d})_Y[-2d]\xrightarrow", "new": r"(\mu_n)_Y^{\otimes -d}[-2d]\xrightarrow"},
    "As (4.1) and (4.3).")
add(64, "'Comme M est localement constant constructible, on a (canoniquement)'",
    "(canoniquement) in parentheses", "on a canoniquement", "punctuation", "high",
    {"old": r"on a canoniquement", "new": r"on a (canoniquement)"}, "Parentheses left out.")
add(64, "display after '(canoniquement)': 'R Hom(M, R i^!F)_ȳ ≃ R Hom(M_ȳ, (R i^!F)_ȳ)', the R inside the first Hom",
    "a plain typewriter R with one stem (1-3 px, as the R of 'Résolvant' p. 62 and 'Reste' p. 65); the three "
    "other R of this display and all R of the next display have two separate stems (double-struck)",
    r"\R\underline{\Hom}(M,\R i^!F)_{\bar{y}} (\R = \mathbb{R})", "misprint_in_print", "high",
    {"old": r"(M,\R i^!F)_{\bar{y}}\simeq \R\underline{\Hom}(M_{\bar{y}},(",
     "new": r"(M,\mathrm{R} i^!F)_{\bar{y}}\simeq \R\underline{\Hom}(M_{\bar{y}},("},
    "The TeX silently gives the double-struck R; the fix restores the printed letter (diplomatic layer only), as "
    "the plain R of pp. 16, 38, 45.",
    corrected=r"\R i^!F")
add(64, "'On a alors F_x̄ ≃ F_ȳ , A_x̄ ≃ A_ȳ , puisque'",
    "the two isomorphisms are displayed, centred on a line of their own: 'F_x̄ ≃ F_ȳ ,   A_x̄ ≃ A_ȳ ,'; "
    "'puisque A_X et les H^i(F) ...' begins the next line at the margin",
    r"inline: On a alors $F_{\bar{x}}\simeq F_{\bar{y}}$, $A_{\bar{x}}\simeq A_{\bar{y}}$, puisque",
    "other", "high",
    {"old": r"On a alors $F_{\bar{x}}\simeq F_{\bar{y}}$, $A_{\bar{x}}\simeq A_{\bar{y}}$, puisque",
     "new": r"On a alors" + NL + r"\[" + NL + "        " + r"F_{\bar{x}}\simeq F_{\bar{y}},\qquad A_{\bar{x}}\simeq A_{\bar{y}},"
            + NL + r"\]" + NL + r"puisque"},
    "Display against inline formula, as the layout fix logged for p. 44.")
add(64, "cartesian square, label of the bottom arrow Z -> X",
    "k stands above the arrow (j stands to the left of the vertical arrow Y -> Z)",
    r'''Z \arrow[r,"k"'] (the ' sets the label below the arrow)''', "formula", "high",
    {"old": r'''\arrow[r,"k"']''', "new": r'''\arrow[r,"k"]'''},
    '''"j"' (left of the vertical arrow) is right as it stands.''')

# ---------------------------------------------------------------- p. 65
add(65, "'donc R^p i_* (G)_x̄ = 0 pour p > d + dim(O_X,x) + dim.inj(F_x̄) ,'",
    "R^p with a plain typewriter R (one stem, 2-3 px, as the R of 'Reste' below); the R^p of the display "
    "'R^p i_*(G)_x̄ = 0 pour p > 2d + ...' above has two stems about 2 px apart (double-struck, as the TeX)",
    r"\R^p i_*(G)_{\bar{x}}=0\quad\hbox{pour }p>d+ (\R = \mathbb{R})", "font", "high",
    {"old": r"\R^p i_*(G)_{\bar{x}}=0\quad\hbox{pour }p>d+",
     "new": r"\mathrm{R}^p i_*(G)_{\bar{x}}=0\quad\hbox{pour }p>d+"},
    "As the plain R^q, R^p of pp. 26-29 (logged as font). Does not overlap the two layout fixes of this line.")
add(65, "same line: the formula is run into the text after 'donc' (opening)",
    "'donc R^p i_* (G)_x̄ = 0 pour p > ... ,' is one line of running text beginning at the margin, not a "
    "display; 'donc a fortiori pour ...' follows on the next line",
    r"a display \[ ... \] between 'donc' and 'donc a fortiori'", "other", "high",
    {"old": "donc" + NL + r"\[" + NL + "        ", "new": r"donc $"},
    r"Apply together with the next finding (closing $): either alone breaks the LaTeX. The \quad\hbox{pour } "
    r"stays inside the inline formula.")
add(65, "same line: the formula is run into the text (closing)",
    "the comma after dim.inj(F_x̄) ends the formula; 'donc a fortiori' begins the next line",
    r"...\dim.\mathrm{inj}(F_{\bar{x}}), \] donc a fortiori", "other", "high",
    {"old": r"\mathrm{inj}(F_{\bar{x}})," + NL + r"\]" + NL + r"donc a fortiori",
     "new": r"\mathrm{inj}(F_{\bar{x}})$," + NL + r"donc a fortiori"},
    "Apply together with the previous finding.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(OUT, len(F), "entries")
