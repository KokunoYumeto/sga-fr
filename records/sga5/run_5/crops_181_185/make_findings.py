"""Build findings_181_185.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
N = "\n"


def F(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------- page 181 ----------------
L.append(F(181, "top of the page",
           "p. 181 begins 'G un A-module à gauche, on a un isomorphisme évident'; p. 180 ends "
           "'Si F est un A-bimodule,'",
           "'$G$ un $A$-' ends page_180.tex (the line before the folio-181 marker); page_181.tex opens with "
           "'module à gauche'",
           "marker", "high", None, None,
           "Page 181 really begins at '$G$ un $A$-module à gauche'. The marker also splits the word: the line end "
           "after '$A$-' sets 'A- module' with a space. Exact fix (moves '$G$ un $A$-' from the end of the line "
           "before the marker to the start of the line after it, joined to 'module'): "
           "python -I marker_split_word.py 5 181 pull '$G$ un $A$-'  (simulated in memory on both editions: "
           "'...est un $A$-bimodule,' / marker / '$G$ un $A$-module à gauche, ...')."))
L.append(F(181, "second line, 'qui se dérive (trivialement) en'",
           "qui se dérive (trivialement) en", "qui se dérive trivialement en",
           "punctuation", "high", "qui se dérive trivialement en", "qui se dérive (trivialement) en",
           "Parentheses left out."))
L.append(F(181, "'Supposons A plat sur K' after the second display",
           "a new, indented paragraph", "runs on from the display (no blank line after \\])",
           "other", "high", r"\]" + N + "Supposons", r"\]" + N + N + "Supposons",
           "Paragraph break."))
L.append(F(181, "(5.13.3)",
           "Tr_{A,φ} : Hom_A(E,_{(φ)}E) ⟶ H^o(T,A_{♮,φ}) — Hom is not underlined (the RHom of 5.13.1-5.13.2 "
           "and the Hom of 5.13.4 are)",
           r"\uHom_A(E,{}_{(\varphi)}E)", "underline", "high",
           r"\uHom_A(E,{}_{(\varphi)}E)", r"\Hom_A(E,{}_{(\varphi)}E)",
           "Plain (global) Hom: the trace takes its values in H^0(T, A_{♮,φ})."))
L.append(F(181, "end of (5.13.3)", "no punctuation after the formula", r"H^0(T,A_{\natural,\varphi}),",
           "punctuation", "high", r"H^0(T,A_{\natural,\varphi}),", r"H^0(T,A_{\natural,\varphi})",
           "Comma added at the end of the display."))
L.append(F(181, "'l'action (g,x) ⟼ φ(g)xg^{-1} (les orbites ...)'",
           "(g,x) ⟼ φ(g)xg^{-1} (les orbites s'appellent parfois \"classes de φ-conjugaison\" de G ).",
           "$(g,x)\\mapsto\\varphi(g)xg^{-1}$; les orbites s'appellent parfois classes de $\\varphi$-conjugaison "
           "de $G$.",
           "punctuation", "high",
           "; les orbites s'appellent parfois classes de $\\varphi$-conjugaison de $G$.",
           " (les orbites s'appellent parfois ``classes de $\\varphi$-conjugaison'' de $G$).",
           "The parentheses became a semicolon and the quotes are left out."))
L.append(F(181, "'Les traces 5.14.2 coïncident, pour T ponctuel'",
           "5.14.2, clearly typed", "Les traces 5.14.2 coïncident",
           "misprint_in_print", "medium", None, None,
           "Wrong reference: there is no 5.14 (section 5 ends with 5.13; '5.14' occurs nowhere else in s5.tex). "
           "The traces meant are those just defined, with values in A_{♮,φ}, i.e. 5.13.3 (the case F = A of "
           "5.13.2; 5.13.2 is the other possible reading). The TeX keeps the printed reading.",
           corrected="5.13.3"))
L.append(F(181, "'rendant commutatif le carré (analogue à 5.10.2)'",
           "le carré (analogue à 5.10.2)", "le carré analogue à 5.10.2",
           "punctuation", "high", "le carré analogue à 5.10.2", "le carré (analogue à 5.10.2)",
           "Parentheses left out."))
L.append(F(181, "(5.13.4), label of the bottom arrow",
           "év (accented), above the arrow", "\\arrow[r,\"\\mathrm{ev}\"']",
           "accent", "high", "\\arrow[r,\"\\mathrm{ev}\"']", "\\arrow[r,\"\\mathrm{\\acute{e}v}\"]",
           "Accent left out; the print sets the label above the arrow (the ' puts it below). "
           "\\mathrm{\\acute{e}...} as in the file's \\et."))
L.append(F(181, "after (5.13.4), 'où év est la flèche d'évaluation'",
           "où év est la flèche d'évaluation", "où $\\mathrm{ev}$ est",
           "accent", "high", "où $\\mathrm{ev}$ est", "où $\\mathrm{\\acute{e}v}$ est",
           "Accent left out, as in the diagram."))
# ---------------- page 182 ----------------
L.append(F(182, "top of the page",
           "p. 182 begins 'B ⊗_K M) remplacé par (φ)A ⊗_K M'; p. 181 ends 'avec A ⊗_K M (resp.'",
           "'$B\\otimes_KM$)' ends page_181.tex (the line before the folio-182 marker); page_182.tex opens with "
           "'remplacé par'",
           "marker", "high", None, None,
           "Page 182 really begins at '$B\\otimes_KM$) remplacé par'. Exact fix: "
           "python -I move_marker.py 5 182 '$B\\otimes_KM$)' --before  (simulated in memory on both editions: "
           "'... (resp. ' / marker / '$B\\otimes_KM$)' / 'remplacé par ...'; the line ends keep the spaces)."))
L.append(F(182, "'notons Z_{g,φ} le φ-centralisateur de g dans G , i.e. l'ensemble'",
           "i.e. l'ensemble", "c'est-à-dire l'ensemble",
           "word", "high", "c'est-à-dire l'ensemble", "i.e.~l'ensemble",
           "Abbreviation written out (the file writes 'i.e.~' elsewhere)."))
L.append(F(182, "'soient E ∈ ob D(A)_parf , N ∈ ob D^b(K)'",
           "N, clearly typed", "$N\\in\\ob D^b(K)$",
           "misprint_in_print", "medium", None, None,
           "The object is the M of 5.10.5 and of the next line's u ∈ Hom_A(E,_{(φ)}(M ⊗^L_K E)); no N is used. "
           "The TeX keeps the printed reading.",
           corrected="$M\\in\\ob D^b(K)$"))
L.append(F(182, "'pour u ∈ Hom_A(E,_{(φ)}(M ⊗^L_K E)) , g ∈ G'",
           "Hom not underlined", "\\uHom_A(E,{}_{(\\varphi)}(M\\lten_KE))",
           "underline", "high", "\\uHom_A(E,{}_{(\\varphi)}(M\\lten_KE))", "\\Hom_A(E,{}_{(\\varphi)}(M\\lten_KE))",
           "Plain Hom, as in 5.13.3 (p. 181)."))
L.append(F(182, "end of (5.13.5)", "no punctuation after the formula", "\\Tr_{A,\\varphi}(u)(g^{-1}),",
           "punctuation", "high", "(u)(g^{-1}),", "(u)(g^{-1})",
           "Comma added at the end of the display."))
L.append(F(182, "after (5.13.5), last line of the page",
           "(les détails de la vérification sont laissés au lecteur).",
           "les détails de la vérification étant laissés au lecteur.",
           "word", "high", "les détails de la vérification étant laissés au lecteur.",
           "(les détails de la vérification sont laissés au lecteur).",
           "'sont' rewritten as 'étant' and the parentheses left out."))
# ---------------- page 183 ----------------
L.append(F(183, "section heading, first line of the page",
           "6.- Correspondances équivariantes et divisibilité de termes locaux.  (underlined; '.-' after the "
           "number, full stop at the end)",
           "\\section*{6. Correspondances équivariantes et divisibilité de termes locaux}",
           "punctuation", "high",
           "\\section*{6. Correspondances équivariantes et divisibilité de termes locaux}",
           "\\section*{6.- Correspondances équivariantes et divisibilité de termes locaux.}",
           "The title has '6.-' and ends with a full stop; the TeX drops both (as '3.- Réduction au cas modéré.' "
           "of this exposé)."))
L.append(F(183, "heading 6.1", "6.1. Notations.  (underlined, full stop)", "\\subsection*{6.1. Notations}",
           "punctuation", "high", "\\subsection*{6.1. Notations}", "\\subsection*{6.1. Notations.}",
           "Final full stop left out."))
L.append(F(183, "6.1, first sentence", "d'un corps de car. p", "d'un corps de caractéristique $p$",
           "word", "high", "corps de caractéristique $p$", "corps de car. $p$",
           "Abbreviation written out (the file has 'de car. $p>0$' elsewhere)."))
L.append(F(183, "6.1, 'les \"termes locaux de Lefschetz-Verdier non commutatifs\"'",
           "straight typewriter double quotes; a hyphen in Lefschetz-Verdier",
           "« termes locaux de Lefschetz--Verdier non commutatifs »",
           "punctuation", "high",
           "« termes locaux de Lefschetz--Verdier non commutatifs »",
           "``termes locaux de Lefschetz-Verdier non commutatifs''",
           "Guillemets for the print's straight quotes (the accepted forms are ``...'' and \"...\"), and an en "
           "dash for the print's hyphen; one edit for both."))
L.append(F(183, "6.1, 'plates (dans les applications, ...). Si X est un S-schéma'",
           "elles seront supposées plates (dans les applications, ce seront des algèbres de groupes finis). "
           "Si X est un S-schéma,  (same paragraph)",
           "plates; dans les applications, ce seront des algèbres de groupes finis. / new paragraph 'Si $X$'",
           "punctuation", "high",
           "plates; dans les applications, ce seront des algèbres de groupes finis." + N + N + "Si $X$",
           "plates (dans les applications, ce seront des algèbres de groupes finis). Si $X$",
           "The parentheses became a semicolon, and the TeX starts a new paragraph that the print does not have."))
L.append(F(183, "6.1, '(A,B)-bimodules (à gauche sur A , à droite sur B ).'",
           "(A,B)-bimodules (à gauche sur A , à droite sur B ).",
           "$(A,B)$-bimodules, à gauche sur $A$, à droite sur $B$.",
           "punctuation", "high", "$(A,B)$-bimodules, à gauche sur $A$, à droite sur $B$.",
           "$(A,B)$-bimodules (à gauche sur $A$, à droite sur $B$).",
           "Parentheses replaced by a comma."))
L.append(F(183, "number of no. 6.2", "'6.2.' with a full stop", "\\subsection*{6.2}",
           "punctuation", "high", "\\subsection*{6.2}", "\\subsection*{6.2.}",
           "As the logged '3.6.5.' (p. 97) and '1.1.' (p. 140)."))
L.append(F(183, "6.2, 'au cas \"non commutatif\".'", "straight typewriter double quotes",
           "au cas « non commutatif ».", "punctuation", "high",
           "au cas « non commutatif ».", "au cas ``non commutatif''.",
           "Guillemets for the print's straight quotes."))
L.append(F(183, "last lines of page_183.tex (printed at the top of p. 184)",
           "f = f_1 x_S f_2 : X = X_1 x_S X_2 ⟶ Y = Y_1 x_S Y_2 , A une Λ-algèbre.  (no 'et')",
           "\\] / et $A$ une $\\Lambda$-algèbre.",
           "extra", "high", "\\]" + N + "et $A$ une $\\Lambda$-algèbre.", "\\]" + N + "$A$ une $\\Lambda$-algèbre.",
           "Word added. This text is printed on p. 184 but stands under the folio-183 marker; apply before the "
           "p. 184 marker move."))
# ---------------- page 184 ----------------
L.append(F(184, "top of the page",
           "p. 184 begins 'f = f_1 x_S f_2 : X = X_1 x_S X_2 ⟶ Y = Y_1 x_S Y_2 , A une Λ-algèbre. Pour'; "
           "p. 183 ends 'Soient, pour i = 1, 2, f_i : X_i ⟶ Y_i un S-morphisme,'",
           "the display '\\[ f=f_1\\times_S f_2:... \\]' and 'et $A$ une $\\Lambda$-algèbre.' end page_183.tex; "
           "page_184.tex opens with 'Pour $L_1$'",
           "marker", "high", None, None,
           "Page 184 really begins at the display '\\[ f=f_1\\times_S f_2:X=...'. Exact fix, after this file's "
           "fixes are applied: python -I move_marker.py 5 184 '\\[' --before  (the anchor is the last '\\[' "
           "before the marker, the one that opens this display; simulated in memory on both editions: "
           "'...un $S$-morphisme,' / marker / '\\[' / 'f=f_1...')."))
L.append(F(184, "'on a une flèche de Künneth (dans D^-(Y))'", "(dans D^-(Y))", "dans $D^-(Y)$",
           "punctuation", "high", "Künneth dans $D^-(Y)$", "Künneth (dans $D^-(Y)$)",
           "Parentheses left out."))
L.append(F(184, "end of (6.2.1)", "no punctuation after the formula", "f_*(L_1\\lten_{S,A}L_2),",
           "punctuation", "high", "L_2)," + N + "\\tag{6.2.1}", "L_2)" + N + "\\tag{6.2.1}",
           "Comma added at the end of the display."))
L.append(F(184, "'(où L_1 ⊗^L_{S,A} L_2 =^{dfn} p_1^*L_1 ⊗^L_A p_2^*L_2) , dont'",
           "a comma after the closing parenthesis", "\\])  dont", "punctuation", "high",
           "\\])" + N + "dont", "\\])," + N + "dont", "Comma left out."))
L.append(F(184, "'(pour pouvoir définir ⊗^L_A : D^-(_B-_A) x D^-(_A-_C) ⟶ D^-(_B-_C) ) ,'",
           "the clause is in parentheses: '(pour pouvoir définir ... D^-(_B-_C) ) ,'",
           "pour pouvoir définir \\[ ... D^-({}_B{-}_C), \\]  (no parentheses)",
           "punctuation", "high",
           "pour pouvoir définir" + N + "\\[" + N
           + "\\lten_A:D^-({}_B{-}_A)\\times D^-({}_A{-}_C)\\longrightarrow D^-({}_B{-}_C)," + N + "\\]",
           "(pour pouvoir définir" + N + "\\[" + N
           + "\\lten_A:D^-({}_B{-}_A)\\times D^-({}_A{-}_C)\\longrightarrow D^-({}_B{-}_C)" + N + "\\]),",
           "Parentheses left out; the comma follows the closing parenthesis (as the TeX's '(où \\[...\\])')."))
L.append(F(184, "'on a un isomorphisme analogue à 6.2.1, dans D^-(_BY_C)'", "6.2.1, dans", "6.2.1 dans",
           "punctuation", "high", "analogue à 6.2.1 dans", "analogue à 6.2.1, dans", "Comma left out."))
L.append(F(184, "'L_2 ∈ ob D^-(_AX_{2B})'",
           "_A X_{2B}, clearly typed", "$L_2\\in\\Ob D^-({}_AX_{2B})$",
           "misprint_in_print", "high", None, None,
           "For ⊗^L_A : D^-(_B-_A) x D^-(_A-_C) ⟶ D^-(_B-_C) and the target D^-(_BY_C), L_2 is an (A,C)-bimodule "
           "(compare M_2 ∈ ob D^-(_AY_{2C}) below). The TeX keeps the printed reading.",
           corrected="$L_2\\in\\Ob D^-({}_AX_{2C})$"))
L.append(F(184, "'on a un isomorphisme de Künneth (dans D^-(X))'", "(dans D^-(X))", "dans $D^-(X)$",
           "punctuation", "high", "Künneth dans $D^-(X)$", "Künneth (dans $D^-(X)$)",
           "Parentheses left out."))
L.append(F(184, "end of (6.2.2)", "no punctuation after the formula", "f^!(M_1\\lten_{S,A}M_2),",
           "punctuation", "high", "M_2)," + N + "\\tag{6.2.2}", "M_2)" + N + "\\tag{6.2.2}",
           "Comma added at the end of the display."))
L.append(F(184, "after (6.2.2), '(et un isomorphisme analogue ... ). Enfin, soient'",
           "(et un isomorphisme analogue dans D^-(_BX_C) pour M_1 ∈ ob D^-(_BY_{1A}) , M_2 ∈ ob D^-(_AY_{2C}) ). "
           "Enfin, soient,  (one paragraph)",
           "no parentheses; 'Enfin, soient' begins a new paragraph",
           "punctuation", "high",
           "et un isomorphisme analogue dans $D^-({}_B X_C)$ pour $M_1\\in\\Ob D^-({}_BY_{1A})$, "
           "$M_2\\in\\Ob D^-({}_AY_{2C})$." + N + N + "Enfin",
           "(et un isomorphisme analogue dans $D^-({}_B X_C)$ pour $M_1\\in\\Ob D^-({}_BY_{1A})$, "
           "$M_2\\in\\Ob D^-({}_AY_{2C})$). Enfin",
           "Parentheses left out, and a paragraph break the print does not have."))
L.append(F(184, "'(D^+(X,A_2) quand A_2 est commutatif)' before (6.2.3)",
           "no punctuation after the parenthesis", "est commutatif),",
           "punctuation", "high", "commutatif),", "commutatif)", "Comma added."))
L.append(F(184, "'la flèche \"image inverse\" (III 2.1.1)'", "straight typewriter double quotes",
           "« image inverse »", "punctuation", "high", "« image inverse »", "``image inverse''",
           "Guillemets for the print's straight quotes."))
L.append(F(184, "'avec la flèche analogue à 5.4.2.' before the third display",
           "a full stop after 5.4.2, clearly typed, before the display that is the object of the sentence",
           "avec la flèche analogue à 5.4.2  (no full stop)",
           "misprint_in_print", "medium", "analogue à 5.4.2" + N, "analogue à 5.4.2." + N,
           "A stray full stop inside the sentence ('définie par composition de la flèche ... avec la flèche "
           "analogue à 5.4.2 [display] (adjointe ...)'). The TeX silently corrects; the fix restores the printed "
           "reading (diplomatic layer only).",
           corrected="analogue à 5.4.2"))
# ---------------- page 185 ----------------
L.append(F(185, "top of the page",
           "p. 185 begins 'que 6.2.3 est un isomorphisme. En particulier,'; p. 184 ends 'On déduit de 6.2.1, "
           "comme en (III 2.3),'",
           "'que 6.2.3 est un' ends page_184.tex (the line before the folio-185 marker); page_185.tex opens with "
           "'isomorphisme.'",
           "marker", "high", None, None,
           "Page 185 really begins at 'que 6.2.3 est un isomorphisme'. Exact fix: "
           "python -I move_marker.py 5 185 'que 6.2.3 est un' --before  (simulated in memory on both editions: "
           "'...comme en (III 2.3), ' / marker / 'que 6.2.3 est un' / 'isomorphisme. ...'; marker_split_word.py "
           "pull would glue 'un' to 'isomorphisme')."))
L.append(F(185, "number of no. 6.3", "'6.3.' with a full stop", "\\subsection*{6.3}",
           "punctuation", "high", "\\subsection*{6.3}", "\\subsection*{6.3.}", "As 6.2. (p. 183)."))
L.append(F(185, "'Il résulte de 6.2.2 qu'on a un isomorphisme'", "qu'on a", "que l'on a",
           "word", "high", "Il résulte de 6.2.2 que l'on a", "Il résulte de 6.2.2 qu'on a", ""))
L.append(F(185, "'un isomorphisme canonique (de D^+(_AT_A) )' before (6.3.2)",
           "(de D^+(_AT_A) )", "dans $D^+({}_AT_A)$",
           "word", "high", "canonique dans $D^+({}_AT_A)$", "canonique (de $D^+({}_AT_A)$)",
           "'de' rewritten as 'dans' and the parentheses left out."))
L.append(F(185, "'le foncteur RHom_A(-,KA_T) : il envoie'",
           "a colon after the formula, then 'il' in lower case",
           "\\uRHom_A(-,KA_T). \\] Il envoie", "punctuation", "high",
           "\\uRHom_A(-,KA_T)." + N + "\\]" + N + "Il envoie",
           "\\uRHom_A(-,KA_T) :" + N + "\\]" + N + "il envoie",
           "The colon became a full stop and a capital 'Il'."))
L.append(F(185, "'(et vice-versa), et la démonstration'", "(et vice-versa),", "et vice versa,",
           "punctuation", "high", "et vice versa,", "(et vice-versa),",
           "Parentheses and the hyphen of vice-versa left out."))
L.append(F(185, "number of no. 6.4", "'6.4.' with a full stop", "\\subsection*{6.4}",
           "punctuation", "high", "\\subsection*{6.4}", "\\subsection*{6.4.}", "As 6.2. (p. 183)."))
L.append(F(185, "6.4, 'Par 6.2.3 appliqué à A_1 = A_2 = A , E_1 = L_1 , F_2 = L_2 , E_2 = KA_{X_1}'",
           "E_2 = KA_{X_1}, clearly typed", "$E_2=KA_{X_1}$",
           "misprint_in_print", "high", None, None,
           "6.2.3 has no E_2: D_A L_1 = RHom_A(L_1,KA_{X_1}) needs F_1 = KA_{X_1} (then 6.2.3 gives the display "
           "RHom_A(p_1^*L_1,KA_{X_1} ⊗^L_{S,A} L_2)). The TeX keeps the printed reading.",
           corrected="$F_1=KA_{X_1}$"))
L.append(F(185, "'qui généralise (III 3.1.1). Soit c : C ⟶ X'",
           "same paragraph, same line", "a new paragraph at 'Soit $c$'",
           "other", "high", "qui généralise (III 3.1.1)." + N + N + "Soit", "qui généralise (III 3.1.1). Soit",
           "Paragraph break the print does not have."))
L.append(F(185, "'un isomorphisme canonique (analogue à (III 3.2.1))' before (6.4.2)",
           "(analogue à (III 3.2.1))", "canonique, analogue à (III 3.2.1),",
           "punctuation", "high", "canonique, analogue à (III 3.2.1),", "canonique (analogue à (III 3.2.1))",
           "Parentheses replaced by commas."))
L.append(F(185, "foot of the page / top of p. 186",
           "p. 185 ends 'd'où, en composant avec 6.4.1, un isomorphisme' (the rest of the page is blank); "
           "the display (6.4.3) opens p. 186 (the OCR of p. 186 begins '(6.4.3) H (X,c c^!(D_A L_1 ...')",
           "the display (6.4.3) '\\begin{equation} H^0(X,c_*c^!(...)) ... \\tag{6.4.3}' ends page_185.tex; the "
           "folio-186 marker stands inside the equation, before '\\end{equation}'",
           "marker", "high", None, None,
           "Page 186 really begins at '\\begin{equation}' of (6.4.3). Exact fix: "
           "python -I move_marker.py 5 186 '\\begin{equation}' --before  (the last \\begin{equation} before the "
           "marker; simulated in memory on both editions: '...un isomorphisme' / marker / '\\begin{equation}' / "
           "'H^0(X,...'). The display itself was not compared here (it belongs to p. 186)."))

out = RUN / "findings_181_185.json"
out.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
bad = 0
for d in L:
    if d["fix"]:
        t = (RUN / "b181_185" / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
        c = t.count(d["fix"]["old"])
        if c != 1 or "%%%%%%%%%%" in d["fix"]["old"]:
            bad += 1
            print("BAD", d["page"], c, repr(d["fix"]["old"][:60]))
cnt = {}
for d in L:
    k = cnt.setdefault(d["page"], [0, 0])
    k[1 if d["kind"] == "misprint_in_print" else 0] += 1
print(len(L), "findings;", bad, "bad;", cnt)
