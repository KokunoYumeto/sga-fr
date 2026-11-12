"""Build findings_211_215.json and check that every fix's 'old' occurs exactly once in its page_NNN.tex."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b211_215"
N = "\n"
F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 211
add(211, "page start",
    "p. 211 begins 'à S , peut se compléter en un diagramme du type (D_2)' , dans lequel t appartient à S :'",
    "the folio-211 marker stands after '... dans lequel $s$ appartient à $S$,' (last line of folio 210's text)",
    "marker", "high", None, None,
    r"Page 211 really begins at 'à $S$,' at the end of the last line of folio 210 ('\item[(c')] Tout diagramme du type "
    r"$(D_1)'$ ci-dessous, dans lequel $s$ appartient à $S$,'). Exact fix: python -I move_marker.py 5 211 'à $S$,' "
    r"--before (bash, single quotes; simulated read-only on both layers: '... dans lequel $s$ appartient ' / marker / "
    r"'à $S$,' / 'peut se compléter ...'). Text not moved. The same marker problem, with the same command, is filed "
    r"under page 210 in findings_206_210.json: apply it ONCE (a second run would move the marker back to the "
    r"earlier 'appartient à $S$, peut' of Définition 2.3.1 (c)).")
add(211, "(D_2)' diagram, bottom row", "X --u--> Y, no full stop after Y", r'''& X \arrow[r,"u"'] & Y .''',
    "punctuation", "high", r'\arrow[r,"u"'"'"'] & Y .', r'\arrow[r,"u"'"'"'] & Y',
    "The TeX adds a full stop at the end of the display; the print has none.")
add(211, "item (d)' of Définition 2.3.2", "(d)' Pour tout diagramme commutatif", r"\item[(d')]",
    "symbol", "high", r"\item[(d')]", r"\item[(d)']",
    "The print sets the prime outside the parenthesis, as in (D_1)' and (D_2)' on this page (and (a)', (b)', (c)' "
    "in the proofs on pp. 212-214). Folio 210's \\item[(a')]-(c') are outside these pages.")
add(211, "(d)', end of the sentence", "tel que t o f = t o g .", r"tel que $t\circ f=t\circ g$:",
    "punctuation", "high", r"t\circ f=t\circ g$:", r"t\circ f=t\circ g$.",
    "Full stop in the print, colon in the TeX.")
add(211, "(Delta) display, first arrow", "(Delta) X' ------> X : the arrow X' -> X carries no label",
    r'''X' \arrow[r,"s"] & X''', "extra", "high", r'''X' \arrow[r,"s"]''', r"X' \arrow[r]",
    "The TeX labels the arrow s; the print's arrow is unlabelled (s is only named in the text).")
add(211, "(Delta) display, end", "... Y (no full stop)", r'''\arrow[r,shift right,"g"'] & Y .''',
    "punctuation", "high", r'"g"' + "'" + r'] & Y .', r'"g"' + "'" + r'] & Y',
    "The TeX adds a full stop at the end of the display; the print has none.")
add(211, "2.3.3, first line", "partie de Fl(E) with Fl underlined", r"partie de $\Fl(\cE)$",
    "underline", "medium", r"Supposons que $S$ soit une partie de $\Fl", r"Supposons que $S$ soit une partie de $\underline{\Fl}",
    "The print underlines Fl here and in 2.3.4 (and in the underlined statement 2.4.1), but not in 2.3.5 (p. 212) "
    "or 2.4.3 (p. 215); \\Fl is plain \\operatorname{Fl}.")
add(211, "2.3.3, first line", "Fl(E) , permettant un calcul de fractions à droite",
    r"$\Fl(\cE)$ permettant un calcul de fractions à droite", "punctuation", "high",
    r"(\cE)$ permettant un calcul de fractions à droite", r"(\cE)$, permettant un calcul de fractions à droite",
    "The print has a comma after Fl(E); the TeX drops it.")
add(211, "2.3.3, second sentence", "de la partie (d) de (2.3.1) que", "de la partie (d) de 2.3.1 que,",
    "punctuation", "high", r"partie (d) de 2.3.1", r"partie (d) de (2.3.1)",
    "The print puts the reference in parentheses.")
add(211, "2.3.3, second sentence", "(2.3.1) que pour tout objet X de E", "2.3.1 que, pour tout objet",
    "punctuation", "high", r"que, pour tout objet", r"que pour tout objet",
    "The TeX adds a comma after 'que'; the print has none.")
add(211, "2.3.3, reference", "(SGA 4 1 2.7) : digit one (same glyph as the 1 of (2.3.1)), not a roman I",
    "(SGA 4 I 2.7)", "misprint_in_print", "medium", r"SGA 4 I 2.7", r"SGA 4 1 2.7",
    "The typist typed the digit 1 for the roman numeral of Exposé I (crop p211_sga4b.png against p211_231.png; "
    "elsewhere in the volume 'SGA 6 I 7.7' has a capital I). The TeX silently corrects; the fix restores the print.",
    corrected=r"SGA 4 I 2.7")
add(211, "2.3.3, list", "the two items begin with a hyphen: '- Les objets ...', '- Si X et Y ...'",
    r"\begin{itemize} (default bullet labels)", "symbol", "medium", r"\begin{itemize}", r"\begin{itemize}[label=-]",
    "The print's item labels are typewriter hyphens; the TeX's itemize prints bullets (enumitem is loaded and the "
    "file already uses [label=...]).")
add(211, "2.3.3, first item", "- Les objets de E_S", r"\item les objets de $\cE_S$", "word", "high",
    r"\item les", r"\item Les", "Capital L in the print.")
add(211, "2.3.3, first item, end", "sont les objets de E ,", r"sont les objets de $\cE$;", "punctuation", "high",
    r"objets de $\cE$;", r"objets de $\cE$,", "Comma in the print, semicolon in the TeX.")
add(211, "2.3.3, second item", "- Si X et Y sont deux objets de E ,", r"\item si $X$ et $Y$", "word", "high",
    r"\item si", r"\item Si", "Capital S in the print.")
add(211, "2.3.3, display Hom_{E_S}(X,Y)", "Lim (capital L) over a right arrow, (S/X)° below",
    r"\varinjlim_{(S/X)^\circ} (lower-case lim)", "symbol", "medium",
    r"\varinjlim_{(S/X)^\circ}", r"\mathop{\underrightarrow{\mathrm{Lim}}}\limits_{(S/X)^\circ}",
    "The print types 'Lim' with a capital L here (crop p211_lim.png); on p. 215 it types a lower-case 'lim' "
    "(\\varinjlim_r stands there).")
add(211, "2.3.4, first line", "partie de Fl(E) with Fl underlined", r"partie de $\Fl(\cE)$", "underline", "medium",
    r"Soit maintenant $S$ une partie de $\Fl", r"Soit maintenant $S$ une partie de $\underline{\Fl}",
    "As in 2.3.3: the print underlines Fl.")
add(211, "2.3.4, second sentence", "le foncteur p_S : E --> E(S^-1) (lower-case p with descender)",
    r"le foncteur $P_S:\cE\to\cE(S^{-1})$", "symbol", "high", r"foncteur $P_S:", r"foncteur $p_S:",
    "2.3.4 and 2.3.5 print a lower-case p_S (5 times, pp. 211-212; crops p211_pS1b.png, p211_pS2.png), 2.3.3 a "
    "capital P_S (twice, kept); the definition on p. 210 names the functor p and p. 217 has p_AR, so this is the "
    "print's notation, not a misprint. The TeX normalizes to P_S.")
add(211, "2.3.4, second sentence", "commute aux limites inductives finies (underlined)",
    "commute aux limites inductives finies (no underline)", "underline", "high",
    r"commute aux limites inductives finies", r"\emph{commute aux limites inductives finies}",
    "Underlined in the print; the file writes underlined words as \\emph.")
add(211, "2.3.4, last sentence", "et p_S est un foncteur additif (lower-case p)", r"et $P_S$ est un foncteur additif",
    "symbol", "high", r"et $P_S$ est un foncteur additif", r"et $p_S$ est un foncteur additif",
    "Lower-case p in the print (see the 2.3.4 finding above).")

# ---------------------------------------------------------------- page 212
add(212, "page start", "p. 212 begins '2.3.5. Si la catégorie E est abélienne ...'",
    "'\\subsubsection*{2.3.5}' and 'Si la' end folio 211's text; page 212's text begins 'catégorie $\\cE$ est abélienne'",
    "marker", "high", None, None,
    r"Page 212 really begins at '\subsubsection*{2.3.5}' (print p. 211 ends with 'et p_S est un foncteur additif.'). "
    r"Exact fix: python -I move_marker.py 5 212 '\subsubsection*{2.3.5}' --before (simulated read-only on both "
    r"layers: the marker then stands on its own line after the blank line that ends 2.3.4, before "
    r"'\subsubsection*{2.3.5}' / 'Si la' / 'catégorie ...'). Text not moved.")
add(212, "2.3.5, first line", "si S est un partie de Fl(E) ('un', not 'une'; crop p212_unpartie.png)",
    "si $S$ est une partie de $\\Fl(\\cE)$", "misprint_in_print", "high", r"est une partie", r"est un partie",
    "Wrong article in the print; the TeX silently corrects. The fix restores the printed reading.",
    corrected=r"est une partie")
add(212, "2.3.5", "le foncteur p_S est exact (lower-case p)", r"le foncteur $P_S$ est exact", "symbol", "high",
    r"$P_S$ est exact", r"$p_S$ est exact", "Lower-case p_S in the print, as in 2.3.4.")
add(212, "2.3.5", "le couple (p_S,E(S^-1)) (lower-case p)", r"le couple $(P_S,\cE(S^{-1}))$", "symbol", "high",
    r"$(P_S,\cE", r"$(p_S,\cE", "Lower-case p_S in the print.")
add(212, "2.3.5, end", "épaisse p_S^{-1}(0) (lower-case p)", r"épaisse $P_S^{-1}(0)$", "symbol", "high",
    r"$P_S^{-1}", r"$p_S^{-1}", "Lower-case p_S in the print.")
add(212, "2.3.5, last sentence", "est un quotient de E par sous-catégorie abélienne épaisse (no article)",
    "par sous-catégorie abélienne épaisse (as printed)", "misprint_in_print", "low", None, None,
    "The article 'la' seems to be missing ('par la sous-catégorie ...'); the TeX keeps the printed reading. Low "
    "confidence: may be the author's wording.", corrected=r"par la sous-catégorie abélienne épaisse")
add(212, "heading 2.4", "2.4. La catégorie P_AR = Hom_AR(N°,C) .  (title ends with a full stop)",
    r"\subsubsection*{2.4. La catégorie $P_{AR}=\Hom_{AR}(\NN^\circ,\cC)$}", "punctuation", "high",
    r"(\NN^\circ,\cC)$}", r"(\NN^\circ,\cC)$.}",
    "Underlined title ending with a full stop in the print; the TeX drops it.")
add(212, "heading 2.4", "Hom_AR(N°,C) with Hom underlined (functor category)", r"$P_{AR}=\Hom_{AR}(\NN^\circ,\cC)$",
    "underline", "high", r"P_{AR}=\Hom", r"P_{AR}=\uHom",
    "The print underlines the Hom of the functor categories Hom(N°,C), Hom_AR(N°,C) on pp. 212-215 (as on pp. "
    "207-208, where \\uHom was used). The underline of 'La catégorie' is the accepted title underline.")
add(212, "2.4, first paragraph", "(cf. 2.1) V_rX : X[r] --> X, with a capital V (cap height, crop p212_vrX2.png)",
    r"v_{rX}:X[r]\longrightarrow X,", "misprint_in_print", "medium", r"v_{rX}:X[r]", r"V_{rX}:X[r]",
    "Everywhere else (v_rY, v_rX, v_rZ, pp. 212-215) the print has a lower-case v; the defining occurrence has a "
    "capital V. The TeX silently writes v; the fix restores the print.", corrected=r"v_{rX}:X[r]")
add(212, "Proposition 2.4.1", "La partie / de / Fl / permet à la fois ... à gauche underlined; AR, (P) and the "
    "final full stop not underlined", "no underline", "underline", "high",
    r"La partie $AR$ de $\Fl(P)$ permet à la fois un calcul de fractions à droite et un calcul de fractions à gauche.",
    r"\emph{La partie} $AR$ \emph{de} $\underline{\Fl}(P)$ \emph{permet à la fois un calcul de fractions à droite "
    r"et un calcul de fractions à gauche}.",
    "Underlined statement (the TeX has no underline markup for statements in this exposé).")
add(212, "Preuve of 2.4.1", "(a) => (a)'", r"(a) $\Rightarrow$ (a')", "symbol", "high",
    r"(a) $\Rightarrow$ (a')", r"(a) $\Rightarrow$ (a)'", "Prime outside the parenthesis in the print.")
add(212, "Preuve of 2.4.1", "(b) => (b)'", r"(b) $\Rightarrow$ (b')", "symbol", "high",
    r"(b) $\Rightarrow$ (b')", r"(b) $\Rightarrow$ (b)'", "Prime outside the parenthesis in the print.")
add(212, "diagram (D_1)", "the label (D_1) stands at the left of the diagram",
    "no (D_1) label in the TeX diagram", "missing", "high",
    r"\begin{tikzcd}[column sep=large,row sep=large]" + N + r"& Y[r]",
    r"(D_1)\quad" + N + r"\begin{tikzcd}[column sep=large,row sep=large]" + N + r"& Y[r]",
    "Label written as for (Delta) on p. 211.")
add(212, "diagram (D_1), bottom row", "X -----> Y, no full stop", r"X \arrow[r] & Y .", "punctuation", "high",
    r"X \arrow[r] & Y .", r"X \arrow[r] & Y", "The TeX adds a full stop at the end of the display.")
add(212, "sentence before (D_2)", "d'où l'assertion.", "d'où l'assertion:", "punctuation", "high",
    r"d'où l'assertion:", r"d'où l'assertion.", "Full stop in the print, colon in the TeX.")
add(212, "diagram (D_2)", "the label (D_2) stands at the left of the diagram",
    "no (D_2) label in the TeX diagram", "missing", "high",
    r"\begin{tikzcd}[column sep=large,row sep=large]" + N + r"X[r]",
    r"(D_2)\quad" + N + r"\begin{tikzcd}[column sep=large,row sep=large]" + N + r"X[r]",
    "Label written as for (Delta) on p. 211.")
add(212, "diagram (D_2), bottom row", "X --u--> Y, no full stop", r'''X \arrow[r,"u"'] & Y .''', "punctuation",
    "high", r'"u"' + "'" + r'] & Y .', r'"u"' + "'" + r'] & Y',
    "The TeX adds a full stop at the end of the display.")

# ---------------------------------------------------------------- page 213
add(213, "page start", "p. 213 begins with the display X =f,g=> Z[r] --v_rZ--> Z .",
    "page 213's text begins '\\end{tikzcd}' / '\\]' / 'Montrons (d). Soit un diagramme commutatif :'",
    "marker", "high", None, None,
    r'''Page 213 really begins at the '\[' that opens 'X \arrow[r,shift left,"f"] ... & Z .'; the close of the (D_2) '''
    r"display and 'Montrons (d). Soit un diagramme commutatif :' are the end of print p. 212. Exact fix: "
    r"python -I move_marker.py 5 213 '\[' (the first '\[' after the marker; simulated read-only on both layers: "
    r"'Montrons (d). Soit un diagramme commutatif :' / marker / '\['). Text not moved.")
add(213, "Appliquant ...", 'la "translation" par r" (quotation marks round translation)', "la translation par $r$",
    "punctuation", "high", r"la translation", r"la ``translation''",
    "The TeX drops the print's quotation marks (written ``...'' elsewhere in Exposé V).")
add(213, "Appliquant ...", 'par r" , on en déduit : a third, unpaired closing quote after r',
    "par $r$, on en déduit", "misprint_in_print", "medium", r"par $r$,", r"par $r$'',",
    "Unbalanced quotation marks in the print (either 'translation' or 'translation par r' was meant to be quoted). "
    "The TeX omits the stray quote together with the pair; apply after or independently of the quotation-mark fix "
    "(disjoint strings).", corrected=r"par $r$,")
add(213, "Appliquant ...", "on en déduit un diagramme commutatif :", "on en déduit un diagramme commutatif",
    "punctuation", "high", r"déduit un diagramme commutatif", r"déduit un diagramme commutatif:",
    "Colon in the print, none in the TeX.")
add(213, "Montrons (c')", "Remarquons tout d'abord que si Y désigne", "Remarquons tout d'abord que, si",
    "punctuation", "high", r"d'abord que, si", r"d'abord que si", "The TeX adds a comma.")
add(213, "Montrons (c')", "et tel que pour tout objet X de P ,", "et tel que, pour tout objet", "punctuation",
    "high", r"et tel que, pour", r"et tel que pour", "The TeX adds a comma.")
add(213, "Montrons (c')", "l'homomorphisme de translation par r :", "l'homomorphisme de translation par $r$",
    "punctuation", "high", r"de translation par $r$", r"de translation par $r$:",
    "Colon before the display in the print, none in the TeX.")
add(213, "definition of T", "T_n est l'objet nul de C pour n >= r-1 et Y_{n-r} sinon",
    r"pour $n\ge r-1$ et $Y_{n-r}$ sinon (as printed)", "misprint_in_print", "high", None, None,
    "Since X[r] = (X_{n+r}) (2.1), Y = T[r] needs T_n = Y_{n-r} for n >= r and T_n = 0 for n <= r-1; with the "
    "printed >= the 'sinon' case has negative indices. The TeX keeps the printed reading. Correct together with "
    "the display w_n = 0 pour n >= r-1 below.", corrected=r"$n\le r-1$")
add(213, "display w_n", "w_n = 0 pour n >= r-1 , w_n = u_{n-r} .", r"w_n=0\quad\text{pour } n\ge r-1,",
    "misprint_in_print", "high", None, None,
    "Same slip as in the definition of T_n just above (w_n : T_{n+1} -> T_n is zero for n <= r-1). The TeX keeps "
    "the printed reading. Correct both or neither.", corrected=r"n\le r-1")
add(213, "last sentence", "dans l'énoncé de (c)' :", "dans l'énoncé de (c'):", "symbol", "high",
    r"l'énoncé de (c'):", r"l'énoncé de (c)':",
    "Prime outside the parenthesis here; 'Montrons (c')' earlier on this page has it inside in the print, as in the TeX.")

# ---------------------------------------------------------------- page 214
add(214, "first diagram", "X[r] --u'--> Y', v_rX down to X, no full stop", r"& Y'\\ X .", "punctuation", "high",
    "Y'\\\\" + N + "X .", "Y'\\\\" + N + "X", "The TeX adds a full stop after X.")
add(214, "display after 'l'application canonique'", "Hom_P(X,Y') --> Hom_P(X[r], Y')",
    r"\Hom_P(X,Y')\longrightarrow\Hom_P(X[r],Y') (as printed)", "misprint_in_print", "high", None, None,
    "The bijection used (u is the unique morphism X -> Y with u' = u[r]; translation as on p. 213) is "
    "Hom_P(X,Y) -> Hom_P(X[r],Y'); the printed Y' in the source is a slip. The diplomatic TeX keeps the printed "
    "reading; the corrected layer already reads \\Hom_P(X,Y).", corrected=r"\Hom_P(X,Y)")
add(214, "square, bottom row", "X --u--> Y, no full stop", r'''X \arrow[r,"u"'] & Y .''', "punctuation", "high",
    r'"u"' + "'" + r'] & Y .', r'"u"' + "'" + r'] & Y', "The TeX adds a full stop at the end of the display.")
add(214, "Montrons (d)'", "Montrons (d)' .", "Montrons (d').", "symbol", "high", r"Montrons (d').",
    r"Montrons (d)'.", "Prime outside the parenthesis in the print.")
add(214, "Montrons (d)', first sentence", "tel que w o f = w o g .", r"tel que $w\circ f=w\circ g$:",
    "punctuation", "high", r"w\circ f=w\circ g$:", r"w\circ f=w\circ g$.", "Full stop in the print, colon in the TeX.")
add(214, "second square, bottom row", "X =f,g=> Y, no full stop", r"& Y . (before 'En particulier')",
    "punctuation", "high", "& Y ." + N + r"\end{tikzcd}" + N + r"\]" + N + "En particulier",
    "& Y" + N + r"\end{tikzcd}" + N + r"\]" + N + "En particulier",
    "The TeX adds a full stop; the print has none (the display X[r] -> X => Y . above does have one and keeps it).")
add(214, "last sentence", "de la démonstration de (c)' ,", "de la démonstration de (c'),", "symbol", "high",
    r"démonstration de (c')", r"démonstration de (c)'", "Prime outside the parenthesis in the print.")

# ---------------------------------------------------------------- page 215
add(215, "first sentence", "des morphismes v_rT o f de v_rT o g sont égaux respectivement à ...",
    r"des morphismes $v_{rT}\circ f$ de $v_{rT}\circ g$ (as printed)", "misprint_in_print", "high", None, None,
    "'respectivement' needs two morphisms: 'de' is a slip for 'et'. The TeX keeps the printed reading.",
    corrected=r"$v_{rT}\circ f$ et $v_{rT}\circ g$")
add(215, "first sentence", "égaux respectivement à v_rY o f et v_rY o g[r] (no [r] after the first f)",
    r"à $v_{rY}\circ f$ et $v_{rY}\circ g[r]$ (as printed)", "misprint_in_print", "medium", None, None,
    "The translate of v_rT o f is v_rY o f[r] (T[r] = Y), and v_rY o f[r] = v_rY o g[r] is the equality of p. 214 "
    "that gives 'donc égaux'. The TeX keeps the printed reading.", corrected=r"$v_{rY}\circ f[r]$")
add(215, "Définition 2.4.2, first sentence", "Soit / une catégorie abélienne. On appelle catégorie des systèmes "
    "projectifs de / à translations près, et on note underlined; C not underlined",
    "no underline", "underline", "high",
    r"Soit $\cC$ une catégorie abélienne. On appelle catégorie des systèmes projectifs de $\cC$ à translations près, et on note $\Hom",
    r"\emph{Soit} $\cC$ \emph{une catégorie abélienne. On appelle catégorie des systèmes projectifs de} $\cC$ "
    r"\emph{à translations près, et on note} $\uHom",
    "Underlined statement; the Hom of the functor category Hom_AR(N°,C) is underlined too (\\uHom, as on pp. 207-208).")
add(215, "Définition 2.4.2", "et on note Hom_AR(N°, C) la catégorie décrite ci-dessous : (no comma)",
    r"et on note $\Hom_{AR}(\NN^\circ,\cC)$, la catégorie", "punctuation", "high",
    r"_{AR}(\NN^\circ,\cC)$, ", r"_{AR}(\NN^\circ,\cC)$ ",
    "The TeX adds a comma. (The C of this Hom_AR(N°, C) is a plain typed C, a typist variant of the script C: "
    "not reported, as the decision of item 78.)")
add(215, "Définition 2.4.2", "la catégorie décrite ci-dessous (underlined) :", "no underline", "underline", "high",
    r"la catégorie décrite ci-dessous:", r"\emph{la catégorie décrite ci-dessous}:", "Underlined statement.")
add(215, "Définition 2.4.2 (i)", "Les objets de / sont les objets de underlined (and Hom)", "no underline",
    "underline", "high",
    r"\item Les objets de $\Hom_{AR}(\NN^\circ,\cC)$ sont les objets de $\Hom(\NN^\circ,\cC)$.",
    r"\item \emph{Les objets de} $\uHom_{AR}(\NN^\circ,\cC)$ \emph{sont les objets de} $\uHom(\NN^\circ,\cC)$.",
    "Underlined statement, with the underlined Hom of both functor categories (\\uHom); the final full stop is not "
    "underlined.")
add(215, "Définition 2.4.2 (ii)", "Si / et / sont deux objets de / un morphisme de / dans / dans la catégorie / "
    "est un élément de l'ensemble underlined; X, Y and the comma not", "no underline", "underline", "high",
    r"\item Si $X$ et $Y$ sont deux objets de $\Hom(\NN^\circ,\cC)$, un morphisme de $X$ dans $Y$ dans la catégorie $\Hom_{AR}(\NN^\circ,\cC)$ est un élément de l'ensemble",
    r"\item \emph{Si} $X$ \emph{et} $Y$ \emph{sont deux objets de} $\uHom(\NN^\circ,\cC)$, \emph{un morphisme de} $X$ "
    r"\emph{dans} $Y$ \emph{dans la catégorie} $\uHom_{AR}(\NN^\circ,\cC)$ \emph{est un élément de l'ensemble}",
    "Underlined statement, with the underlined Hom of the functor categories (\\uHom).")
add(215, "Définition 2.4.2 (ii), after the display", "où, pour tout couple / d'entiers avec / l'application "
    "underlined; (r,s), s >= r and the comma not", "no underline", "underline", "high",
    r"où, pour tout couple $(r,s)$ d'entiers avec $s\ge r$, l'application",
    r"\emph{où, pour tout couple} $(r,s)$ \emph{d'entiers avec} $s\ge r$, \emph{l'application}",
    "Underlined statement.")
add(215, "Définition 2.4.2 (ii)", "provient du morphisme canonique (underlined)", "no underline", "underline",
    "high", r"provient du morphisme canonique", r"\emph{provient du morphisme canonique}", "Underlined statement.")
add(215, "Dans la suite ...", "P = Hom(N°,C) et P_AR = Hom_AR(N°,C) .",
    r"P=\Hom(\NN^\circ,\cC),\qquad P_{AR}=\Hom_{AR}(\NN^\circ,\cC).", "word", "high",
    r",\qquad P", r"\quad\text{et}\quad P",
    "The print joins the two definitions with 'et' (run in the text); the TeX replaces the word by a comma "
    "(display against run-in text is not reported).")
add(215, "Dans la suite ...", "P = Hom(N°,C) with Hom underlined", r"P=\Hom(\NN^\circ,\cC)", "underline", "high",
    r"P=\Hom(", r"P=\uHom(",
    "The print underlines the Hom of the functor categories Hom(N°,C), Hom_AR(N°,C) on pp. 212-215 (as on p. 207, "
    "written \\uHom there); the Hom of morphism sets (Hom_AR(X,Y), Hom(X[r],Y), Hom_P) is plain in print and TeX.")
add(215, "Dans la suite ...", "P_AR = Hom_AR(N°,C) with Hom underlined", r"P_{AR}=\Hom_{AR}(\NN^\circ,\cC)",
    "underline", "high", r"_{AR}=\Hom_{AR}", r"_{AR}=\uHom_{AR}", "As the preceding finding.")
add(215, "2.4.3", "Ceci nous permet (2.3.3) de considérer la catégorie :", "de considérer la catégorie",
    "punctuation", "high", r"de considérer la catégorie", r"de considérer la catégorie:",
    "Colon before the display in the print, none in the TeX.")

# ---------------------------------------------------------------- checks and output
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (B / ("page_%d.tex" % d["page"])).read_text(encoding="utf-8")
    old = d["fix"]["old"]
    c = t.count(old)
    if c != 1:
        ok = False
        print("NOT UNIQUE", d["page"], c, repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", d["page"], repr(old))
# disjointness of the olds on each page
for p in range(211, 216):
    t = (B / ("page_%d.tex" % p)).read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            k = t.find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["fix"]["old"][:30]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
out = RUN / "findings_211_215.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
for p in range(211, 216):
    n = sum(1 for d in F if d["page"] == p and d["kind"] != "misprint_in_print")
    m = sum(1 for d in F if d["page"] == p and d["kind"] == "misprint_in_print")
    print(p, "%d/%d" % (n, m))
print("all olds unique and disjoint" if ok else "PROBLEMS")
