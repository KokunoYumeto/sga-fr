"""Write findings_086_090.json (SGA 5, pp. 86-90) and check every fix's old against the page files."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
OUT = RUN / "findings_086_090.json"


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = r"\overset{\mathrm{L}}{\otimes}"
fs = []

# ---------------------------------------------------------------- page 86
fs.append(F(86, "top of the page",
    "p. 86 begins with the commutative square f_*RHom(E,f^!Q) ⊗^L_S RHom(P',Q') --b--> f'_*RHom(E ⊗^L_S P',f^!Q ⊗^L_S Q'); "
    "p. 85 ends 'On doit prouver la commutativité du carré' (blank below)",
    "the folio-86 marker (diplomatic s5.tex line 2321) splits the opening of the square's display: '\\[' and "
    "'\\begin{tikzcd}[' end page_085.tex, 'column sep=large,row sep=large]' opens page_086.tex",
    "marker", "high",
    note="Page 86 really begins at the '\\[' of s5.tex line 2319 that opens the square. Exact fix: "
         "python -I move_marker.py 5 86 '\\[' --before (the nearest '\\[' before the marker; simulated in memory on both "
         "layers: the marker then stands between 'On doit prouver la commutativité du carré' and '\\[', the option list "
         "'\\begin{tikzcd}[' / 'column sep=large,row sep=large]' stays on two lines as now). Text not moved. "
         "Batch 081_085 may report the same move from the foot of p. 85: apply once."))
fs.append(F(86, "first square, label of the left vertical arrow 'a ⊗^L_S RHom(P',Q')'",
    "the label stands to the right of the arrow (the a against the shaft)",
    "\\arrow[d,\"{a" + L + "_S\\uRHom(P',Q')}\"'] (the swap mark sets it to the left)",
    "other", "high",
    "\\uRHom(P',Q')}\"']", "\\uRHom(P',Q')}\"]",
    note="tikz-cd sets an unswapped label to the right of a downward arrow. b (above) and a' (right) are right."))
fs.append(F(86, "first square, label of the bottom arrow RHom(f_!E,Q) ⊗ RHom(P',Q') -> RHom(f_!E ⊗ P',Q ⊗ Q')",
    "2.2.4 above the arrow",
    "\\arrow[r,\"2.2.4\"'] (below the arrow)",
    "other", "high",
    "\\arrow[r,\"2.2.4\"']", "\\arrow[r,\"2.2.4\"]",
    note="tikz-cd sets a swapped label below a rightward arrow."))
fs.append(F(86, "'de base f_!E ⊗^L_S P' --c--> f'_!(E ⊗^L_S P')'",
    "c above the arrow, ≃ below it: a typed tilde over a separate typed bar",
    "\\xrightarrow[\\sim]{c} (a bare tilde below the arrow)",
    "symbol", "high",
    "\\xrightarrow[\\sim]{c}", "\\xrightarrow[\\simeq]{c}",
    note="The sign under the arrow is the print's ≃ (tilde over a bar), as in 'f'_!(f^!Q ⊗ Q') ≃ f_!f^!Q ⊗ Q'' lower on "
         "the page, which the TeX gives as \\simeq. The arrow with a bare tilde above it at the foot of the page "
         "(\\xrightarrow{\\sim}) is right."))
fs.append(F(86, "'f^!Q ⊗^L_S Q' --d--> f'^!(Q ⊗^L_S Q')'",
    "d above the arrow, ≃ (tilde over a bar) below it",
    "\\xrightarrow[\\sim]{d}",
    "symbol", "high",
    "\\xrightarrow[\\sim]{d}", "\\xrightarrow[\\simeq]{d}",
    note="As the arrow c."))
fs.append(F(86, "(*), last derived tensor of the target, 'f'_!(f^!Q ⊗_S Q'))'",
    "a typed digit 1 above the ⊗ instead of L (sloping flag, as the 1 of 3.1.9.6; the l of 'la' has a flat serif); "
    "the three other tensors of (*) carry the L",
    "f^!Q" + L + "_SQ')),",
    "misprint_in_print", "high",
    "f^!Q" + L + "_SQ')),", "f^!Q\\overset{1}{\\otimes}_SQ')),",
    corrected="f^!Q" + L + "_SQ')),",
    note="A typing slip for the derived-tensor L; the TeX silently corrects. The fix restores the printed reading "
         "(diplomatic layer only)."))
fs.append(F(86, "second square, label of the left vertical arrow 'ch. base ≃'",
    "ch. base ≃ (a typed tilde over a typed bar)",
    "\\text{ch. base}\\ \\sim",
    "symbol", "high",
    "\\text{ch. base}\\ \\sim", "\\text{ch. base}\\ \\simeq",
    note="As the arrows c and d. The label's place (left of the arrow) is right."))
fs.append(F(86, "second square, label of the bottom arrow f_!f^!Q ⊗ Q' -> Q ⊗ Q'",
    "adj ⊗ 1 above the arrow",
    "\\arrow[r,\"{\\mathrm{adj}\\otimes 1}\"'] (below the arrow)",
    "other", "high",
    "\\arrow[r,\"{\\mathrm{adj}\\otimes 1}\"']", "\\arrow[r,\"{\\mathrm{adj}\\otimes 1}\"]",
    note="tikz-cd sets a swapped label below a rightward arrow. f'_!d (above) and adj (right) are right."))

# ---------------------------------------------------------------- page 87
fs.append(F(87, "top of the page",
    "p. 87 begins with the square RHom(f_!E,f_!f^!Q) ⊗^L_S RHom(P',Q') -> RHom(f_!E ⊗^L_S P',f_!f^!Q ⊗^L_S Q'); "
    "p. 86 ends 'jointes à la commutativité du carré' (blank below)",
    "the folio-87 marker (diplomatic s5.tex line 2364) splits the square's option list: '\\[' and "
    "'\\begin{tikzcd}[column sep=' end page_086.tex, 'large,row sep=large]' opens page_087.tex",
    "marker", "high",
    note="Page 87 really begins at the '\\[' of s5.tex line 2362 that opens the square. Exact fix: "
         "python -I move_marker.py 5 87 '\\[' --before (the nearest '\\[' before the marker; simulated in memory on both "
         "layers: the marker then stands between 'jointes à la commutativité du carré' and '\\[', the option list stays "
         "split after 'column sep=' as now). Text not moved."))
fs.append(F(87, "first square, end of the bottom row 'RHom(f_!E ⊗^L_S P',Q ⊗^L_S Q')'",
    "no punctuation after the square (clean paper to the margin)",
    "Q" + L + "_SQ'), (a comma added)",
    "punctuation", "high",
    "_SQ'),\n\\end{tikzcd}\n\\]\ndéfini", "_SQ')\n\\end{tikzcd}\n\\]\ndéfini",
    note="Punctuation added at the end of a display (the square on p. 86 does print its comma)."))
fs.append(F(87, "'il suffit de prouver la compatibilité suivante :'",
    "a colon after 'suivante'",
    "la compatibilité suivante. (a full stop)",
    "punctuation", "high",
    "la compatibilité suivante.", "la compatibilité suivante :"))
fs.append(F(87, "label of Lemme 2.6.3",
    "'Lemme 2.6.3 - Soient ...': 'Lemme' underlined, then the number and a typewriter dash, the statement run in",
    "\\subsection*{Lemme 2.6.3} (no dash)",
    "punctuation", "high",
    "\\subsection*{Lemme 2.6.3}", "\\subsection*{Lemme 2.6.3 -}",
    note="Run-in label of Exposé III with a dash, as the applied '\\subsection*{Proposition 1.7.4 -}'. The run-in and "
         "the label's underline are the accepted \\subsection* setting."))
fs.append(F(87, "statement of 2.6.3, 'Soient f, f', E, F, P', Q' comme en 2.6.1 . On a alors un carré commutatif'",
    "underlined: 'Soient', 'comme en 2.6.1', 'On a alors un carré' and 'commutatif'; the letters f, f', E, F, P', Q' "
    "and the full stop are not",
    "no underline",
    "underline", "high",
    "Soient $f$, $f'$, $E$, $F$, $P'$, $Q'$ comme en 2.6.1. On a alors un carré commutatif",
    "\\emph{Soient} $f$, $f'$, $E$, $F$, $P'$, $Q'$ \\emph{comme en 2.6.1}. \\emph{On a alors un carré commutatif}",
    note="The whole statement of the lemma (down to 'changement de base' before its last display) is underlined word "
         "by word, the formulas left plain, as the statement of 1.7.4 (p. 79); \\emph is this file's command for the "
         "print's underline in Exposé III. Five more edits below."))
fs.append(F(87, "square of 2.6.3, label of the bottom arrow (3)",
    "(3) above the arrow",
    "\\arrow[r,\"(3)\"'] (below the arrow)",
    "other", "high",
    "\\arrow[r,\"(3)\"']", "\\arrow[r,\"(3)\"]",
    note="tikz-cd sets a swapped label below a rightward arrow. (1) above, (2) left and (4) right are right."))
fs.append(F(87, "statement of 2.6.3, 'où (1) est composé de l'isomorphisme de changement de base'",
    "'où' and 'est composé de l'isomorphisme de changement de base' underlined; '(1)' not",
    "no underline",
    "underline", "high",
    "où (1) est composé de l'isomorphisme de changement de base",
    "\\emph{où} (1) \\emph{est composé de l'isomorphisme de changement de base}",
    note="As the opening of the statement."))
fs.append(F(87, "statement of 2.6.3, 'et f'_*(2.2.4), (2) est déduit de la flèche canonique'",
    "'et' and 'est déduit de la / flèche canonique' (across the line break) underlined; 'f'_*(2.2.4), (2)' not",
    "no underline",
    "underline", "high",
    "et $f'_*(2.2.4)$, (2) est déduit de la flèche canonique",
    "\\emph{et} $f'_*(2.2.4)$, (2) \\emph{est déduit de la flèche canonique}"))
fs.append(F(87, "statement of 2.6.3, 'SGA 4 XVIII 3.1.9.5) par application de'",
    "'SGA 4 XVIII 3.1.9.5)' and 'par applica-/tion de' underlined",
    "no underline",
    "underline", "high",
    "SGA~4~XVIII~3.1.9.5) par application de",
    "\\emph{SGA~4~XVIII~3.1.9.5) par application de}",
    note="Apply before the misprint fix that follows (missing opening parenthesis): its old is taken from the text "
         "after this edit."))
fs.append(F(87, "statement of 2.6.3, 'RHom(f_!E,f_!F)   SGA 4 XVIII 3.1.9.5) par application'",
    "no opening parenthesis before SGA (clean paper between the ) of RHom(f_!E,f_!F) and the S); the closing one is "
    "printed",
    "(SGA~4~XVIII~3.1.9.5) (the parenthesis supplied)",
    "misprint_in_print", "high",
    "(\\emph{SGA", "\\emph{SGA",
    corrected="(\\emph{SGA",
    note="The TeX silently corrects; the fix restores the printed reading (diplomatic layer only). Its old is the text "
         "after the underline edit just above (apply that one first)."))
fs.append(F(87, "statement of 2.6.3, ', (3) est donné par 2.2.4 , enfin (4) est composé de la flèche canonique'",
    "'est donné par', 'enfin' and 'est composé de la / flèche canonique' (across the line break) underlined; '(3)', "
    "'2.2.4 ,' and '(4)' not",
    "no underline",
    "underline", "high",
    ", (3) est donné par 2.2.4, enfin (4) est composé de la flèche canonique",
    ", (3) \\emph{est donné par} 2.2.4, \\emph{enfin} (4) \\emph{est composé de la flèche canonique}"))
fs.append(F(87, "statement of 2.6.3, '(loc. cit.) et des flèches définies par les isomorphismes de changement de base'",
    "the whole line underlined, '(loc. cit.)' included",
    "no underline",
    "underline", "high",
    "(loc. cit.) et des flèches définies par les isomorphismes de changement de base",
    "\\emph{(loc. cit.) et des flèches définies par les isomorphismes de changement de base}",
    note="The last underlined words of the statement; the proof ('Revenant à la définition ...') is plain."))
fs.append(F(87, "'a) Cas où f est une immersion ouverte.'",
    "typed plain, not underlined (clean baseline under the whole line)",
    "\\emph{a) Cas où $f$ est une immersion ouverte.}",
    "underline", "high",
    "\\emph{a) Cas où $f$ est une immersion ouverte.}", "a) Cas où $f$ est une immersion ouverte.",
    note="\\emph is this file's command for the print's underline; as 'b) Cas où f est un morphisme propre.' (p. 88)."))

# ---------------------------------------------------------------- page 88
fs.append(F(88, "top of the page",
    "p. 88 begins 'le carré que l'on obtient est commutatif. Or les sommets de ce carré sont nuls en dehors de X''; "
    "p. 87 ends with the display (f_!E ⊗ P') ⊗ RHom(f_!E ⊗ P' , f_!F ⊗ Q') -> f_!F ⊗ Q' , and the footnote",
    "'le carré que l'on obtient est commutatif. Or les sommets de ce carré sont nuls en' is s5.tex line 2406, the "
    "last line of page_087.tex; the folio-88 marker (line 2407) follows it",
    "marker", "high",
    note="Page 88 really begins at 'le carré que' (s5.tex line 2406). Exact fix: "
         "python -I move_marker.py 5 88 'le carré que' --before (single quotes; the anchor occurs once in s5.tex; "
         "simulated in memory on both layers: the marker then stands between the '\\]' of the evaluation display and "
         "'le carré que'). Text not moved."))
fs.append(F(88, "'b) Cas où f est un morphisme propre.'",
    "typed plain, not underlined",
    "\\emph{b) Cas où $f$ est un morphisme propre.}",
    "underline", "high",
    "\\emph{b) Cas où $f$ est un morphisme propre.}", "b) Cas où $f$ est un morphisme propre.",
    note="As a) on p. 87."))
fs.append(F(88, "last square, label of the bottom arrow (1')",
    "(1') above the arrow",
    "\\arrow[r,\"(1')\"'] (below the arrow)",
    "other", "high",
    "\\arrow[r,\"(1')\"']", "\\arrow[r,\"(1')\"]",
    note="tikz-cd sets a swapped label below a rightward arrow. (3) above the top arrow is right."))
fs.append(F(88, "'(prendre u : f*f_*E -> f_*E donné par l'identité de f*f_*E , et v : f -> f_*F donné par l'identité de f_*F )'",
    "v : f ----> f_*F, a small typed f (as the f of f_*F), not F",
    "$v:f\\to f_*F$ (as printed)",
    "misprint_in_print", "high",
    corrected="$v:F\\to f_*F$",
    note="v is the f-arrow of type 1 from F to f_*F given by the identity of f_*F (as u goes from f^*f_*E to f_*E). "
         "The TeX keeps the printed reading; the corrected layer already has v:F -> f_*F."))

# ---------------------------------------------------------------- page 89
fs.append(F(89, "heading of § 3, top of the page",
    "'3. Correspondances cohomologiques.': the number 3. and a full stop (the rule runs from 3. to cohomologiques)",
    "\\section*{Correspondances cohomologiques} (no number, no full stop)",
    "number", "high",
    "\\section*{Correspondances cohomologiques}", "\\section*{3. Correspondances cohomologiques.}",
    note="As the applied heading of § 1, '\\section*{1. Notations et rappels de formules de Künneth.}' (p. 76). The "
         "underline is the accepted \\section* setting."))
fs.append(F(89, "number of 3.1, '3.L   Soient, pour i : 1,2, ...'",
    "'3.L': a capital L (stem with a right foot and upturned serif, as the L of L_1, L_2), not the digit 1 of '1,2' "
    "in the same line",
    "\\subsection*{3.1}",
    "misprint_in_print", "high",
    "\\subsection*{3.1}", "\\subsection*{3.L}",
    corrected="\\subsection*{3.1}",
    note="A typing slip for 3.1; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only)."))
fs.append(F(89, "3.1, 'Soient, pour i : 1,2, X_i un S-schéma'",
    "'i : 1,2': a typed colon (two round dots), not the equals sign of 'X = X_1 x_S X_2' in the next line",
    "pour $i=1,2$",
    "misprint_in_print", "high",
    "pour $i=1,2$", "pour $i:1,2$",
    corrected="pour $i=1,2$",
    note="The TeX silently corrects; the fix restores the printed reading (diplomatic layer only)."))
fs.append(F(89, "3.1, 'p_i : X -> X_i et q_i : X_i -> S les projections canoniques :'",
    "the word 'et' between the two maps, no comma",
    "p_i:X\\longrightarrow X_i, \\qquad q_i:X_i\\longrightarrow S (a comma for 'et')",
    "word", "high",
    "X_i,\n\\qquad\nq_i", "X_i\n\\qquad\\text{et}\\qquad\nq_i",
    note="The print runs the three formulas into the text (the TeX's display is layout, not reported); the comma "
         "after X = X_1 x_S X_2 is printed."))
fs.append(F(89, "3.1, diagram, labels of the arrows X -> X_1 and X -> X_2",
    "P_1, P_2: capital P (bowl at cap height, stem ending on the baseline), against the small p_i (with descender) of "
    "the line above",
    "\\arrow[dl,\"P_1\"'] \\arrow[dr,\"P_2\"] (as printed)",
    "misprint_in_print", "high",
    corrected="\\arrow[dl,\"p_1\"'] \\arrow[dr,\"p_2\"]",
    note="The projections are p_1, p_2. The TeX keeps the printed reading; the corrected layer already has p_1, p_2 "
         "(Codex SGA-SRC-001849, FIXLOG_5_CURRENT). The bottom vertex is a typed X overwritten by a hand-drawn S, the "
         "typist's correction: the TeX's S is right."))
fs.append(F(89, "3.1, end of the diagram of the projections",
    "a typed full stop to the right of the diagram, on the line of its bottom vertex S (the size and shape of the "
    "full stops after the displays of the page)",
    "no punctuation after the diagram",
    "punctuation", "high",
    "& S &\n\\end{tikzcd}", "& S & .\n\\end{tikzcd}",
    note="Set in the empty cell right of S: the file appends the end punctuation of its diagrams to their last cell "
         "(the comma of the first square of p. 86)."))
fs.append(F(89, "every derived tensor product of p. 89 (6 signs), first the (2.2.4) display 'DL_1 ⊗^L_S L_2'",
    "a plain upright typed capital L standing above the hand-drawn ⊗ (as on pp. 86-88)",
    "\\overset{\\mathbf L}{\\otimes} (a bold L): s5.tex line 2454 'DL_1\\overset{\\mathbf L}{\\otimes}_S L_2', line 2461 "
    "'q_1^!A_S\\overset{\\mathbf L}{\\otimes}_S L_2', line 2473 'L_1^\\vee\\overset{\\mathbf L}{\\otimes}L_2'",
    "font", "high",
    note="Convention of the transcription from § 3 on, not listed per occurrence: s5.tex writes "
         "\\overset{\\mathbf L}{\\otimes} 66 times inside Exposé III (lines 2454-2964, pp. 89-100; the six of p. 89 at "
         "lines 2454, 2456, 2457, 2461, 2466, 2473, all printed with the plain L). The Exposé III form is "
         "\\overset{\\mathrm{L}}{\\otimes} (pp. 86-88): one scoped pass '\\overset{\\mathbf L}{\\otimes}' -> "
         "'\\overset{\\mathrm{L}}{\\otimes}' over lines 1929-4369 (subscripts stay). See the message."))
fs.append(F(89, "'Les éléments de Hom_S(L_1,L_2) s'appelleront correspondances cohomologiques de L_1 à L_2 .'",
    "'correspondances cohomologiques de' and 'à' underlined; L_1 and L_2 not",
    "\\emph{correspondances cohomologiques de $L_1$ à $L_2$}",
    "underline", "high",
    "\\emph{correspondances cohomologiques de $L_1$ à $L_2$}",
    "\\emph{correspondances cohomologiques de} $L_1$ \\emph{à} $L_2$",
    note="The rule breaks at each formula, as in the statement of 2.6.3 (p. 87)."))
fs.append(F(89, "'Au lieu de \"correspondance cohomologique de A_{X_1} à A_{X_2}\" nous dirons simplement'",
    "no comma after the closing quotes (clean paper before 'nous')",
    "$A_{X_2}$'', nous dirons",
    "punctuation", "high",
    "$A_{X_2}$'', nous dirons", "$A_{X_2}$'' nous dirons"))
fs.append(F(89, "'nous dirons simplement \"correspondance cohomologique de X_1 à X_2\" (sous-entendu : à coefficients dans A)'",
    "the phrase in typewriter double quotes; inside, 'correspondance cohomologique de' and 'à' underlined, X_1 and "
    "X_2 not",
    "simplement \\emph{correspondance cohomologique de $X_1$ à $X_2$} (no quotes; X_1, X_2 inside the emphasis)",
    "missing", "high",
    "simplement \\emph{correspondance cohomologique de $X_1$ à $X_2$} (sous",
    "simplement ``\\emph{correspondance cohomologique de} $X_1$ \\emph{à} $X_2$'' (sous",
    note="The quotes in the file's ``...'' form (as the first phrase of the sentence); the underline extent in the "
         "same edit (adjacent)."))
fs.append(F(89, "'p_2^!L_2 ≃ p_2^*L_2(r_1)[2r_1] , donc' (printed at the top of p. 90; in page_089.tex as the files stand)",
    "a long straight bar with a typed tilde above it, no arrowhead at either end (clean paper at both ends)",
    "p_2^!L_2\\xrightarrow{\\sim}p_2^*L_2(r_1)[2r_1]",
    "symbol", "high",
    "p_2^!L_2\\xrightarrow{\\sim}p_2^*L_2(r_1)[2r_1]", "p_2^!L_2\\simeq p_2^*L_2(r_1)[2r_1]",
    note="The print's ≃ (tilde over a bar, no head) drawn long, as the logged \\simeq fixes of pp. 10 and 16-20; the "
         "isomorphisms of 3.1 with a head are \\xrightarrow{\\sim} and right. Filed under p. 89; its old stays "
         "unique on p. 90 after the folio-90 marker move."))

# ---------------------------------------------------------------- page 90
fs.append(F(90, "top of the page",
    "p. 90 begins with the display 'p_2^!L_2 ≃ p_2^*L_2(r_1)[2r_1] , donc'; p. 89 ends 'et par le théorème de "
    "dualité (SGA 4 XVIII 3.2.5) , on a' (blank below)",
    "the display '\\[ p_2^!L_2\\xrightarrow{\\sim}p_2^*L_2(r_1)[2r_1], \\]' ends page_089.tex (s5.tex lines "
    "2485-2487); the folio-90 marker (line 2488) follows it",
    "marker", "high",
    note="Page 90 really begins at the '\\[' of s5.tex line 2485. Exact fix: "
         "python -I move_marker.py 5 90 '\\[' --before (the nearest '\\[' before the marker; simulated in memory on both "
         "layers: the marker then stands between '..., on a' and '\\['). Text not moved."))
fs.append(F(90, "3.2, '(on dit parfois que c est une correspondance entre X_1 et X_2 )'",
    "'correspondance' underlined",
    "une correspondance entre (no underline)",
    "underline", "high",
    "une correspondance entre", "une \\emph{correspondance} entre"))
fs.append(F(90, "3.2, 'Nous appellerons correspondances cohomologiques de L_1 à L_2 à support dans c'",
    "only 'correspondances cohomolo-/giques' (across the line break) and 'support dans' underlined; 'de', both 'à', "
    "L_1, L_2 and c not",
    "\\emph{correspondances cohomologiques de $L_1$ à $L_2$ à support dans $c$}",
    "underline", "high",
    "\\emph{correspondances cohomologiques de $L_1$ à $L_2$ à support dans $c$}",
    "\\emph{correspondances cohomologiques} de $L_1$ à $L_2$ à \\emph{support dans} $c$"))
fs.append(F(90, "3.2, '(= Hom(c_1^*L_1,c_2^!L_2) si c est propre)'",
    "'propre' underlined",
    "\\text{ est propre} (no underline)",
    "underline", "high",
    "\\text{ est propre}", "\\text{ est \\emph{propre}}",
    note="The print runs the group and this parenthesis into the text (the TeX's display is layout, not reported)."))
fs.append(F(90, "'Exemples : a) Supposons c propre'",
    "'Exemples' underlined, then a colon (not underlined)",
    "\\emph{Exemples.} (a full stop inside the emphasis)",
    "punctuation", "high",
    "\\emph{Exemples.}", "\\emph{Exemples} :",
    note="Label in the print's form, as the global '\\emph{Preuve} :'."))
fs.append(F(90, "3.2 a), 'une correspondance cohomologique de A_{X_1} à A_{X_2}(-N)[2N]'",
    "[2N] with no minus sign (clean paper inside the bracket; the display above prints [-2N])",
    "$A_{X_2}(-N)[2N]$ (as printed)",
    "misprint_in_print", "high",
    corrected="$A_{X_2}(-N)[-2N]$",
    note="By adjunction the trace Tr_{c_2} : c_{2!}A_C -> A_{X_2}(-N)[-2N] gives A_C -> c_2^!A_{X_2}(-N)[-2N]: a "
         "correspondence to A_{X_2}(-N)[-2N] (its class lies in H^{-2N}, 3.2.4). The TeX keeps the printed reading; the "
         "corrected layer already has [-2N] (Codex SGA-SRC-001850, FIXLOG_5_CURRENT)."))
fs.append(F(90, "foot of the page",
    "p. 90 ends '... de A_{X_1} à A_{X_2}(-N)[2N]'; p. 91 begins 'à support dans C , qu'on appellera classe de (c,N)'",
    "the 'à' at the end of s5.tex line 2534, the last line of page_090.tex, before the folio-91 marker (line 2535)",
    "marker", "high",
    note="Page 91 really begins at that 'à'. Exact fix: python -I move_marker.py 5 91 'à' --before (the nearest 'à' "
         "before the marker; simulated in memory on both layers: the marker then splits line 2534 after '[2N]$ ', and "
         "'à' opens p. 91 on its own line before 'support dans $C$'). Text not moved. Batch 091_095 may report the "
         "same move from the top of p. 91: apply once."))

# ---------------------------------------------------------------- checks
pages = {p: (RUN / "b086_090" / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(86, 91)}
work = dict(pages)
ok = True
for i, f in enumerate(fs):
    if f["fix"] is None:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    t = work[f["page"]]
    n_now, n_orig = t.count(old), pages[f["page"]].count(old)
    if n_now != 1:
        ok = False
        print("NOT UNIQUE", i, f["page"], n_now, repr(old))
    if n_orig != 1:
        print("note: old occurs", n_orig, "times in the original file (sequential edit)", i, f["page"], repr(old))
    if "%%%%%%%%%%" in old:
        ok = False
        print("MARKER IN OLD", i)
    work[f["page"]] = t.replace(old, new, 1)
# the p. 89 symbol fix after the folio-90 marker move: its old must be unique in the new p. 90 span
moved = "\\[\np_2^!L_2\\xrightarrow{\\sim}p_2^*L_2(r_1)[2r_1],\n\\]\n"
assert pages[89].endswith(moved), repr(pages[89][-120:])
p90_after = moved + pages[90]
print("p.89 symbol old in p.90 after move:", p90_after.count("p_2^!L_2\\xrightarrow{\\sim}p_2^*L_2(r_1)[2r_1]"))
for f in fs:
    assert f["kind"] in ("word", "formula", "symbol", "font", "underline", "missing", "extra", "number",
                         "punctuation", "accent", "misprint_in_print", "marker", "other")
OUT.write_text(json.dumps(fs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in fs)
print("written", OUT, len(fs), "ok" if ok else "PROBLEMS")
for p in range(86, 91):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
