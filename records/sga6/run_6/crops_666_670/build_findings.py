"""Build findings_666_670.json and check that every fix's old string occurs exactly once in its page file."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
B = RUN + r"\b666_670"
OUT = RUN + r"\findings_666_670.json"
MK = "%%%%%%%%%%  scan idx {}  |  folio {}  %%%%%%%%%%"


def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


L = []

# ---------------------------------------------------------------- p. 666
L.append(F(666, "start of page (folio-666 marker)",
           "p. 665 ends 'On suppose que pour toute composante irréductible Y^i de Y,' (b661_665/page_665_s4.png); "
           "p. 666 begins 'les composantes irréductibles de X ∩ Y^i = V(φ|Y^i) sont de dimension ≥ 2.' "
           "(page_666_s1.png; witness crops_666_670/w666_tophalf.png)",
           "in page_666.tex the marker stands before '\\emph{Soient $k$ un corps ...', so the first two sentences of "
           "Corollaire 7.5 (printed on p. 665) sit under the folio-666 marker",
           "marker", "high", None,
           "Page 666 really begins at 'les composantes irr\\'eductibles de $X\\cap Y^i=V(\\varphi|Y^i)$'. Already "
           "done: when checked (main.tex of 17:03, both layers) the marker already stands on its own line between "
           "'de $Y$, ' and 'les composantes irr\\'eductibles' (the same as python -I move_marker.py 6 666 "
           "'les composantes irr'), so nothing is left to apply; listed because the batch file still had the old place."))
L.append(F(666, "heading of the bibliography",
           "BIBLIOGRAPHIE (capitals, underlined)",
           "\\subsection*{Bibliographie}",
           "word", "high", fx("\\subsection*{Bibliographie}", "\\subsection*{BIBLIOGRAPHIE}"),
           "The print types the heading in capitals (both scans). The other bibliographies of main.tex are written "
           "\\subsection*{BIBLIOGRAPHIE}; the missing underline of a section title is accepted as typesetting."))
L.append(F(666, "proof of Corollaire 7.5, 'supposer Y intègre'",
           "int + è g r underlined + e: a short typed underline under 'ègr' only (crops_666_670/c666_integre.png; "
           "witness w666_integre.png)",
           "int\\`egre", "misprint_in_print", "low", fx("int\\`egre", "int\\underline{\\`egr}e"),
           "A stray underline under three letters of 'intègre' in both scans; it emphasizes nothing, so it is a "
           "slip of the typist. The TeX silently drops it; the fix restores the printed form for the diplomatic "
           "layer (decide whether the diplomatic layer reproduces such a stray stroke).",
           corrected="int\\`egre"))
L.append(F(666, "proof of Corollaire 7.5, 'grâce à la formule de projection'",
           "graĉe: the circumflex stands over the c, not over the a (crops_666_670/c666_grace.png; witness "
           "w666_grace.png)",
           "gr\\^ace", "misprint_in_print", "medium", fx("gr\\^ace", "gra\\^ce"),
           "Misplaced accent of the typist (dead key struck before the c), the same in both scans. The TeX silently "
           "corrects it; the fix restores the printed reading.",
           corrected="gr\\^ace"))
L.append(F(666, "bibliography [2]",
           "Mumford D : Pathologies III, Amer. J. Math 1967 p. 94-103 / Amer. J. Math 1967 p.94-103. (the "
           "reference is typed twice, on two lines)",
           "Amer. J. Math 1967 p. 94-103 Amer. J. Math 1967 p.94-103.",
           "misprint_in_print", "medium", None,
           "Dittography of the typist. The TeX keeps the printed reading; the current layer already has the single "
           "reference.",
           corrected="Amer. J. Math 1967 p. 94-103."))
L.append(F(666, "bibliography [5]",
           "1960-66, J.H.E.S. (the first letter has the hooked descender of the J of 'Jussila' and 'J. Math'; "
           "crops_666_670/c666_jhes.png)",
           "J.H.E.S.", "misprint_in_print", "medium", None,
           "The Institut des Hautes Études Scientifiques is I.H.E.S. The TeX keeps the printed reading.",
           corrected="I.H.E.S."))

# ---------------------------------------------------------------- p. 667
L.append(F(667, "title of Exposé XIV",
           "'Exposé XIV' alone on the first line (underlined); then, centred, 'PROBLEMES OUVERTS EN THEORIE DES "
           "INTERSECTIONS' in capitals, double underlined, no full stop",
           "\\section*{Exposé XIV. Problèmes ouverts en théorie des intersections}",
           "word", "high",
           fx("\\section*{Exposé XIV. Problèmes ouverts en théorie des intersections}",
              "\\section*{\\underline{Exposé XIV}\\\\[3pt] \\underline{\\underline{PROBLÈMES OUVERTS EN THÉORIE DES "
              "INTERSECTIONS}}}"),
           "The TeX joins the two heading lines with an added full stop and sets the capital title in lower case. "
           "The fix uses the form of the headings of Exposés II, V and VI in main.tex. The typescript's capitals "
           "have no accents (PROBLEMES, THEORIE): the accented capitals stand by the global rule."))
L.append(F(667, "author line", "par A. Grothendieck (underlined)", "par A. Grothendieck",
           "underline", "medium", fx("par A. Grothendieck", "\\underline{par A. Grothendieck}"),
           "As in the other author lines of main.tex (\\underline{par A. Grothendieck} in Exposé 0 and in the "
           "Appendix of Exposé X, p. 560)."))
L.append(F(667, "first paragraph, line 1",
           "quelques uns des problè- (no hyphen; crops_666_670/c667_quelques.png, witness w667_top.png)",
           "quelques-uns", "misprint_in_print", "medium", fx("quelques-uns", "quelques uns"),
           "The compound lacks its hyphen in both scans (as 'au dessus' on p. 469). The TeX silently corrects it; "
           "the fix restores the printed reading.",
           corrected="quelques-uns"))
L.append(F(667, "first paragraph, reference to Kleiman",
           "à S. KLEIMAN, Algebraic (name in capitals)", "S. Kleiman,",
           "word", "high", fx("S. Kleiman,", "S. KLEIMAN,"),
           "The print types the name in capitals (both scans)."))
L.append(F(667, "first paragraph, titles of Kleiman's paper and of the book",
           "Algebraic cycles and the Weil conjectures dans Dix exposés sur la cohomologie des schémas (no "
           "underline on either title, no comma after 'conjectures'; crops_666_670/c667_cycles_a.png, "
           "c667_cycles_b.png)",
           "\\emph{Algebraic cycles and the Weil conjectures}, dans \\emph{Dix exposés sur la cohomologie des "
           "schémas}",
           "underline", "high",
           fx("\\emph{Algebraic cycles and the Weil conjectures}, dans \\emph{Dix exposés sur la cohomologie des "
              "schémas}",
              "Algebraic cycles and the Weil conjectures dans Dix exposés sur la cohomologie des schémas"),
           "The TeX adds emphasis to both titles and a comma the print does not have. The fragments 'es' after "
           "'Algebraic' and 'opo-' after 'des' are erased type (the typist moved 'cycles' and 'schémas' to the next "
           "line), visible in both scans (w667_remnants.png) and rightly left out; the faint tick between "
           "'schémas' and '(' is not a clear comma and is left as the TeX has it."))
L.append(F(667, "first paragraph, 'Dans le n° 4'", "n° 4 (n with a raised ring; crops_666_670/c667_schemas.png)",
           "no. 4", "symbol", "high", fx("no. 4", "n° 4"),
           "The file writes the numéro sign as n° elsewhere (bibliography of Exposé VI: 'n°22', 'n°20'). Exposé XIV writes "
           "no./no for every printed n° (see the coordinator message)."))
L.append(F(667, "second paragraph, '(où le premier membre ...'",
           "l'anneau des classes de Modules localement libres (capital M)",
           "classes de modules localement libres", "word", "high",
           fx("classes de modules localement libres", "classes de Modules localement libres"),
           "Grothendieck's capital M (sheaves of modules), in both scans."))
L.append(F(667, "display after 'l'homomorphisme naturel'",
           "K˙_naif(X) ⟶ K˙(X): both K carry the same raised dot (crops_666_670/c667_knaif.png)",
           "K^\\circ_{\\mathrm{naif}}(X)\\longrightarrow K^\\bullet(X)", "symbol", "high",
           fx("K^\\circ_{\\mathrm{naif}}", "K^\\bullet_{\\mathrm{naif}}"),
           "The print's raised dot is K^\\bullet in this TeX (the right-hand K of the same display); the ring is "
           "not in the print."))
L.append(F(667, "'soit un λ-homomorphisme'",
           "soit un    -homomorphisme: a blank where the handwritten λ belongs, in both scans "
           "(crops_666_670/c667_lhom.png; witness w667_bottom.png)",
           "soit un $\\lambda$-homomorphisme", "misprint_in_print", "high", fx("soit un $\\lambda$-", "soit un -"),
           "The hand insertion was never made. The TeX silently supplies λ; the fix restores the printed blank. "
           "Independent of the next entry (no overlap).",
           corrected="soit un $\\lambda$-"))
L.append(F(667, "end of the sentence before 'Dans ce but'",
           "-homomorphisme / Dans ce but, (no full stop at the end of the line, both scans)",
           "homomorphisme. Dans ce but", "misprint_in_print", "high",
           fx("homomorphisme. Dans ce but", "homomorphisme Dans ce but"),
           "The full stop is missing in both scans. The TeX silently adds it; the fix restores the printed reading.",
           corrected="homomorphisme. Dans ce but"))
L.append(F(667, "'(non addifs en général'", "non addifs", "non addifs", "misprint_in_print", "high", None,
           "Typing error for 'additifs'. The TeX keeps the printed reading.", corrected="non additifs"))
L.append(F(667, "'de \"puissance extérieure)'",
           "de \"puissance extérieure) : an opening quote, no closing quote (crops_666_670/c667_puiss.png, both "
           "scans)",
           "``puissance extérieure'')", "misprint_in_print", "high", fx("extérieure'')", "extérieure)"),
           "The TeX silently adds the closing quote; the fix restores the printed reading. (The closing parenthesis "
           "is also misplaced: the sense is '(non additifs en général) de \"puissance extérieure\"'.)",
           corrected="extérieure'')"))
L.append(F(667, "'vis à vis des triangles exacts'",
           "vis à vis (no hyphens; crops_666_670/c667_visavis.png, witness w667_bottom.png)",
           "vis-à-vis", "misprint_in_print", "medium", fx("vis-à-vis", "vis à vis"),
           "The compound lacks its hyphens in both scans. The TeX silently corrects it; the fix restores the "
           "printed reading.",
           corrected="vis-à-vis"))
L.append(F(667, "formula (1.1)",
           "λ^i(cℓ˙(L.)) = cℓ˙(Λ^i L.) . : both 'cl' carry the typed raised dot of K˙ (crops_666_670/c667_11.png; "
           "witness w667_11.png)",
           "\\lambda^i(\\cl(L^\\bullet))=\\cl(\\Lambda^i L^\\bullet).", "symbol", "medium",
           fx("\\lambda^i(\\cl(L^\\bullet))=\\cl(\\Lambda^i L^\\bullet)",
              "\\lambda^i(\\cl^\\bullet(L^\\bullet))=\\cl^\\bullet(\\Lambda^i L^\\bullet)"),
           "\\cl prints a plain cl; the print's class has the raised dot (the script ℓ is the typewriter's glyph, "
           "not reproduced). The L's lower dot is the convention entry below: apply this fix before that pass."))
L.append(F(667, "Exposé XIV §§1-2 (pp. 667-669): complexes L.",
           "L with a lower dot throughout: p. 667 (1.1) λ^i(cl˙(L.)), p. 668 (1.2) Λ^i L. = (⊗ L.)^alt and "
           "'lorsque L. est nul en degrés >0', L.' and Λ^i L'. (prime over the dot), p. 669 'et L. un complexe', "
           "Rf_*(L.), H^i(L.) (both scans)",
           "L^\\bullet (17 times on pp. 667-669) and L^{\\prime\\bullet} (twice on p. 668)", "symbol", "high", None,
           "Convention of the transcription, reported once: the print's lower dot (as in K.(X), written K_\\bullet) "
           "is written as a raised bullet. One pass for folios 667-669, both layers: L^\\bullet -> L_\\bullet, "
           "L^{\\prime\\bullet} -> L'_\\bullet, after the other fixes of these pages (three of them quote "
           "L^\\bullet). Folio 685 has 5 more L^\\bullet for its checker."))

# ---------------------------------------------------------------- p. 668
L.append(F(668, "first line, 'un faisceau de Q-algèbres'",
           "a plain typed Q (no double stroke; crops_666_670/c668_qalg.png), unlike the double-struck ℂ of p. 669 "
           "and the overstruck Q of Gr˙(X)_Q",
           "faisceau de $\\Q$-algèbres", "font", "low", fx("faisceau de $\\Q$", "faisceau de $Q$"),
           "The typist's plain Q where \\Q is \\mathbb Q (low confidence; volume decision with SGA 7 II issue 61)."))
L.append(F(668, "first line, 'Q-algèbres'", "algébres (acute accent; crops_666_670/c668_qalg.png)",
           "algèbres, le problème", "misprint_in_print", "high",
           fx("algèbres, le problème", "algébres, le problème"),
           "The TeX silently corrects the accent; the fix restores the printed reading (p. 669 'ℂ-algébres' is "
           "kept as printed in the TeX).",
           corrected="algèbres, le problème"))
L.append(F(668, "'le problème se résoud'", "se résoud", "se résoud", "misprint_in_print", "medium", None,
           "Spelling error of the print (third person of résoudre). The TeX keeps the printed reading.",
           corrected="se résout"))
L.append(F(668, "formula (1.2)",
           "Λ^i L. = ( ⊗ L. )^alt , : the tensor sign has i above it and a double-struck L at its upper right, in "
           "front of L., in one pair of parentheses; 'alt' is an exponent (crops_666_670/c668_12.png)",
           "\\Lambda^i L^\\bullet=\\left((L^\\bullet)^{\\otimes i}\\right)_{\\mathrm{alt}},", "formula", "high",
           fx("\\Lambda^i L^\\bullet=\\left((L^\\bullet)^{\\otimes i}\\right)_{\\mathrm{alt}},",
              "\\Lambda^i L^\\bullet=\\bigl(\\overset{i}{\\otimes}{}^{\\mathbb L}L^\\bullet\\bigr)^{\\mathrm{alt}},"),
           "The TeX drops the derived 𝕃, writes the power as (L)^{⊗i} and sets alt as a subscript, although the "
           "text says 'l'exposant alt'. The lower dot of L. is the convention entry of p. 667."))
L.append(F(668, "'la puissance tensorielle i.ème'", "i.ème (a full stop; crops_666_670/c668_ieme.png)",
           "$i$-ème", "punctuation", "medium", fx("$i$-ème", "$i$.ème"), "The print has a stop, not a hyphen."))
L.append(F(668, "'l'algèbre du groupe sysmétrique'", "sysmétrique (crops_666_670/c668_sysm.png)",
           "groupe symétrique", "misprint_in_print", "high", fx("groupe symétrique", "groupe sysmétrique"),
           "Typing error. The TeX silently corrects it; the fix restores the printed reading.",
           corrected="groupe symétrique"))
L.append(F(668, "'à coéfficients dans O_X'", "coéfficients", "coéfficients", "misprint_in_print", "high", None,
           "Spelling error of the print. The TeX keeps the printed reading.", corrected="coefficients"))
L.append(F(668, "'à un Module semi-simplicial L.''", "à un Module semi-simplicial (capital M)",
           "à un module semi-simplicial", "word", "high",
           fx("à un module semi-simplicial", "à un Module semi-simplicial"), "Capital M in both scans."))
L.append(F(668, "'au Module semi-simplicial Λ^i L'.'", "au Module semi-simplicial (capital M)",
           "au module semi-simplicial", "word", "high",
           fx("au module semi-simplicial", "au Module semi-simplicial"), "Capital M in both scans."))
L.append(F(668, "isomorphism after 'il ne semble pas qu'on ait un isomorphisme'",
           "in the running text: 'qu'on ait un isomorphisme Λ^i(L.[1]) ≃ (Λ^i L.)[i] qui permettrait de faire de' "
           "on one line; the parenthesis encloses Λ^i L. (crops_666_670/c668_iso.png)",
           "\\[ \\Lambda^i(L^\\bullet[1])\\simeq \\Lambda^i(L^\\bullet)[i] \\] (a display)", "formula", "high",
           fx("un isomorphisme\n\\[\n \\Lambda^i(L^\\bullet[1])\\simeq \\Lambda^i(L^\\bullet)[i]\n\\]\nqui permettrait",
              "un isomorphisme $\\Lambda^i(L^\\bullet[1])\\simeq(\\Lambda^i L^\\bullet)[i]$ qui permettrait"),
           "Two differences in one edit: the right member is (Λ^i L.)[i], not Λ^i(L.)[i]; and the print sets the "
           "formula inline where the TeX makes it a display (the same kind of fix as pp. 21, 34, 80)."))
L.append(F(668, "2.1, 'construit dans Exp. 0 4.4'", "Exp. O 4.4 , (no comma between 0 and 4.4; "
           "crops_666_670/c668_exp0.png)", "Exp. 0, 4.4,", "punctuation", "medium",
           fx("Exp. 0, 4.4", "Exp. 0 4.4"), "The TeX adds a comma; the typed letter O for the exposé 0 stays 0."))

# ---------------------------------------------------------------- p. 669
L.append(F(669, "start of page (folio-669 marker)",
           "p. 668 ends 'pourraient donner la clef' (page_668_s4.png); p. 669 begins 'd'une démonstration de la "
           "formule analogue' (page_669_s1.png; witness w669_small.png)",
           "'d'une' ends page_668.tex, above the folio-669 marker; page_669.tex begins 'démonstration'",
           "marker", "high", None,
           "Page 669 really begins at 'd'une'. In both layers: python -I move_marker.py 6 669 \"d'une\" --before "
           "(simulated in memory on both layers, crops_666_670/sim_markers.py: 'la clef' / marker / 'd'une' / "
           "'démonstration ...', text unchanged). By hand: replace 'donner la clef d'une\\n%%%%%%%%%%  scan idx 682  "
           "|  folio 669  %%%%%%%%%%\\ndémonstration' by 'donner la clef\\n%%%%%%%%%%  scan idx 682  |  folio 669  "
           "%%%%%%%%%%\\nd'une démonstration' (once in each layer)."))
L.append(F(669, "3.1, 'La formule de Riemann-Roch pour y ∈ K˙(Y) :'", "K˙(Y) : (a colon before the display)",
           "pour $y\\in K^\\bullet(Y)$", "punctuation", "high",
           fx("pour $y\\in K^\\bullet(Y)$", "pour $y\\in K^\\bullet(Y)$~:"), "The TeX leaves out the printed colon."))
L.append(F(669, "3.1, 'jointe à la formule générale (Exp. VII) :'", "(Exp. VII) : (a colon before the display)",
           "jointe à la formule générale (Exp. VII)", "punctuation", "high",
           fx("jointe à la formule générale (Exp. VII)", "jointe à la formule générale (Exp. VII)~:"),
           "The TeX leaves out the printed colon."))
L.append(F(669, "second display of 3.1, right member",
           "f_*(y')f_*(y\") = f (y'y\"c_d(N)) : the third f has no asterisk, a blank in its place, in both scans "
           "(crops_666_670/c669_disp2.png; witness w669_disp2a.png)",
           "=f_*\\bigl(y'y''c_d(\\underline N)\\bigr)", "misprint_in_print", "high",
           fx("=f_*\\bigl(y'y''", "=f\\bigl(y'y''"),
           "The handwritten asterisk was not inserted. The TeX silently supplies it; the fix restores the printed "
           "reading.",
           corrected="=f_*\\bigl(y'y''"))
L.append(F(669, "second display of 3.1, 'y',y\" ∈ Gr(Y)_Q'",
           "Gr(Y)_Q without the raised dot (both scans; crops_666_670/w669_disp2.png); the subscript Q is underlined",
           "y',y''\\in \\operatorname{Gr}^\\bullet(Y)_\\Q", "misprint_in_print", "medium",
           fx("y',y''\\in \\operatorname{Gr}^\\bullet(Y)_\\Q", "y',y''\\in \\operatorname{Gr}(Y)_\\Q"),
           "Every other Gr of these pages has the typed dot (Gr˙(X)_Q two lines below, Gr˙(Y)_Q on p. 670), so the "
           "dot was left out. The TeX silently adds it; the fix restores the printed reading. The underlined Q is "
           "the typist's mark for the double-struck Q: \\Q stands.",
           corrected="y',y''\\in \\operatorname{Gr}^\\bullet(Y)_\\Q"))
L.append(F(669, "2.2, 'annelés en ℂ-algébres'", "ℂ-algébres (acute accent; crops_666_670/c669_calg.png)",
           "$\\C$-algébres", "misprint_in_print", "high", None,
           "The TeX keeps the printed reading (p. 668 has the same misprint, silently corrected there).",
           corrected="$\\C$-algèbres"))
L.append(F(669, "2.2, 'plus généraux que des espéces analytiques'", "espéces (crops_666_670/c669_especes.png)",
           "des espéces analytiques", "misprint_in_print", "high", None,
           "Typing error for 'espaces' (analytic spaces). The TeX keeps the printed reading.",
           corrected="des espaces analytiques"))
L.append(F(669, "2.3, 'aient leurs groupes propres sur Y'", "aient leurs groupes propres sur Y "
           "(crops_666_670/c669_groupes.png)", "aient leurs groupes propres", "misprint_in_print", "low", None,
           "The hypothesis replacing properness of f is that the cohomology sheaves H^i(L.) have supports proper "
           "over Y; 'groupes propres' gives no sense. Possibly an author's slip. The TeX keeps the printed reading.",
           corrected="aient leurs supports propres"))
L.append(F(669, "formula (3.1) (printed at the top of p. 670; its TeX is still in page_669.tex), end",
           "(c_β(N))_β ))   ,, : two commas after the formula (the first smaller), in both scans "
           "(crops_666_670/c670_31end.png, w670_31end.png)",
           "(c_\\beta(\\underline N))_\\beta)\\bigr),", "misprint_in_print", "low",
           fx("(c_\\beta(\\underline N))_\\beta)\\bigr),", "(c_\\beta(\\underline N))_\\beta)\\bigr),,"),
           "Double punctuation of the typist (the first mark may be a light full stop). The TeX silently writes one "
           "comma; the fix restores the printed reading. The edit is by content, so it holds before or after the "
           "folio-670 marker is moved.",
           corrected="(c_\\beta(\\underline N))_\\beta)\\bigr),"))

# ---------------------------------------------------------------- p. 670
L.append(F(670, "start of page (folio-670 marker)",
           "p. 669 ends 'de f_*(y) dans Gr˙(X)_Q sous la forme' (page_669_s4.png); p. 670 begins with the display "
           "'(3.1) c_i(f_*(y)) = f_*(P_i(...))' (page_670_s1.png; witness w670_small.png)",
           "the folio-670 marker stands inside the equation environment of (3.1), between the formula line and "
           "\\end{equation}; page_670.tex begins '\\end{equation}'",
           "marker", "high", None,
           "Page 670 really begins at '\\begin{equation}\\tag{3.1}'. In both layers: python -I move_marker.py 6 670 "
           "'\\begin{equation}\\tag{3.1}' --before (simulated in memory on both layers, crops_666_670/sim_markers.py: "
           "'sous la forme' / marker / '\\begin{equation}\\tag{3.1}' / formula / '\\end{equation}' / 'où $P_i$', "
           "text unchanged). By hand: delete the marker line between ' ...\\bigr),' and '\\end{equation}' and put it "
           "on its own line between 'sous la forme' and '\\begin{equation}\\tag{3.1}'."))
L.append(F(670, "end of page (folio-671 marker)",
           "p. 670 ends 'L'hypothèse de caractéristique nulle est utilisée essentielle-' (page_670_s4.png); p. 671 "
           "begins 'ment pour disposer de formules du type (1.1), (1.2)' (witness crops_666_670/w671_top.png)",
           "'essentiellement' stands whole after the folio-671 marker",
           "marker", "high", None,
           "Page 671 really begins with 'ment' (the word is divided at the page break). As at folios 54 and 161: "
           "python -I marker_split_word.py 6 671 split essentielle ment (simulated in memory on both layers: "
           "'... est utilisée' / 'essentielle%' / marker / 'ment pour disposer ...'). The checker of p. 671 may "
           "report the same boundary: apply once."))
L.append(F(670, "after 'formule de Riemann-Roch \"sans dénominateurs\".'",
           "the print runs on: '... \"sans dénominateurs\". En fait, une telle formule pour' on one line",
           "a blank line (new paragraph) before 'En fait, une telle formule'", "other", "medium",
           fx("dénominateurs''.\n\nEn fait, une telle", "dénominateurs''. En fait, une telle"),
           "The TeX starts a paragraph the print does not have."))
L.append(F(670, "'de définir un homomorphisme f_*:Gr˙(Y) ⟶ Gr˙(X) donnant'",
           "the map stands in the running text, at the start of the line 'f_*:Gr˙(Y)⟶Gr˙(X) donnant "
           "l'homomorphisme naturel ...' (both scans)",
           "\\[ f_*:\\operatorname{Gr}^\\bullet(Y)\\longrightarrow \\operatorname{Gr}^\\bullet(X) \\] (a display)",
           "other", "medium",
           fx("un homomorphisme\n\\[\n f_*:\\operatorname{Gr}^\\bullet(Y)\\longrightarrow \\operatorname{Gr}^\\bullet(X)\n\\]\ndonnant",
              "un homomorphisme $f_*:\\operatorname{Gr}^\\bullet(Y)\\longrightarrow \\operatorname{Gr}^\\bullet(X)$ donnant"),
           "The TeX makes an inline formula a display (the same kind of fix as pp. 21, 34, 80)."))
L.append(F(670, "'donnant l'homomorphisme naturel f : Gr˙(Y)_Q ⟶ Gr˙(X)_Q'",
           "f : with no asterisk (crops_666_670/c670_fnat.png, both scans)",
           "$f:\\operatorname{Gr}^\\bullet(Y)_\\Q", "misprint_in_print", "medium", None,
           "The natural map Gr˙(Y)_Q -> Gr˙(X)_Q is f_*, as in the formulas around it; the asterisk is missing in "
           "the print. The TeX keeps the printed reading.",
           corrected="$f_*:\\operatorname{Gr}^\\bullet(Y)_\\Q"))
L.append(F(670, "after 'et non seulement dans Gr˙(X)_Q .'",
           "the print runs on: 'Gr˙(X), et non seulement dans Gr˙(X)_Q . Mais lorsque X est supposé régulier,' on "
           "one line",
           "a blank line (new paragraph) before 'Mais lorsque'", "other", "medium",
           fx("(X)_\\Q$.\n\nMais lorsque", "(X)_\\Q$. Mais lorsque"),
           "The TeX starts a paragraph the print does not have."))
L.append(F(670, "'donc K˙(X) ⥲ K.(X) (IV 2.5)'",
           "a tilde over a right arrow between K˙(X) and K.(X) (crops_666_670/c670_kiso.png; witness "
           "w670_kiso.png)",
           "K^\\bullet(X)\\simeq K_\\bullet(X)", "symbol", "high",
           fx("K^\\bullet(X)\\simeq K_\\bullet(X)", "K^\\bullet(X)\\xrightarrow{\\sim} K_\\bullet(X)"),
           "The print has an isomorphism arrow, not ≃ (main.tex writes it \\xrightarrow{\\sim} in Exposé V). The "
           "lower dot of the second K is not visible in either scan; the TeX's K_\\bullet stands (K.(X) two lines "
           "below has its dot)."))

json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)

# checks
bad = 0
for d in L:
    if d["fix"] is None:
        continue
    t = open(B + "\\page_%d.tex" % d["page"], encoding="utf-8").read()
    n = t.count(d["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        bad += 1
        print("MARKER IN FIX", d["page"])
for d in L:
    if d["kind"] == "misprint_in_print" and d["fix"] is None:
        t = open(B + "\\page_%d.tex" % d["page"], encoding="utf-8").read()
        if d["tex"] not in t:
            print("tex of kept misprint not in page file:", d["page"], repr(d["tex"]))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in L)
for p in (666, 667, 668, 669, 670):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(L), "bad", bad)
json.load(open(OUT, encoding="utf-8"))
print("json ok")
