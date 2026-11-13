"""Build findings_671_675.json from the entries below and check every fix's old string against its page file.
Strings are raw; the token <NL> stands for a line break (LF). An entry with "after": k is checked on the page text
after entry k's fix has been applied (misprint fix whose old is taken from the text after the other fix)."""
import json
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b671_675")
OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_671_675.json")
CR = "crops_671_675/"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None, after=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if old is None else {"old": nl(old), "new": nl(new)})
    if corrected is not None:
        d["corrected"] = nl(corrected)
    d["note"] = note
    if after is not None:
        d["_after"] = after
    return d


R2 = "Second reading (Codex fr_r1, 5 Aug): "
L = []

# ---------------- page 671 ----------------
L.append(F(671, "3.1, last line: 'la question soulevée au n° 1.'",
           "au n° 1 (n with the raised degree-like o, both scans)", "au no. 1", "symbol", "high",
           r"au no. 1", r"au n\textsuperscript{o} 1",
           "The file writes the numéro sign n\\textsuperscript{o} (22 times in the volume); 'no.' adds a full stop the print does not have. Same on pp. 671-675: (cf. n° 6) p. 671, (n° 6) and (cf n° 8) p. 672, (Cf.. n° 5) p. 674, au n° 3 p. 675 (each listed)."))
L.append(F(671, "3.2: 'qu'on vient d'introduire, -ces dernières classes de Chern'",
           "', -ces dernières': a typed hyphen directly before 'ces' (both scans; " + CR + "c671_dash.png)",
           "introduire, ces dernières (no dash)", "missing", "high",
           r"introduire, ces dernières", r"introduire, -ces dernières",
           "The typescript's dash (a hyphen) is dropped. Written as the plain hyphen the typist typed, not as an en dash."))
L.append(F(671, "3.2: 'l'équivalence rationelle des cycles algébriques'",
           "rationelle (one n, both scans)", "rationelle (printed reading kept)", "misprint_in_print", "high",
           note="Kept by the TeX, correctly for the diplomatic layer.", corrected=r"rationnelle"))
L.append(F(671, "3.2: 'il ne semble pas y avoir de raison bien convainquante'",
           "convainquante (both scans)", "convainquante (printed reading kept)", "misprint_in_print", "medium",
           note="The adjective is spelled convaincante (convainquant is the participle). Kept by the TeX.",
           corrected=r"convaincante"))
L.append(F(671, "3.2: 'Une bonne façon de la tester, vue notre ignorance quasi totale'",
           "vue notre ignorance (both scans)", "vue notre ignorance (printed reading kept)", "misprint_in_print", "low",
           note="The preposition vu is invariable (vu notre ignorance). Author's slip rather than a typing error; kept by the TeX.",
           corrected=r"vu notre ignorance"))
L.append(F(671, "3.2, end: 'en transformant les deux membres de (3.1) par g_* : A(X) ⟶ A(Z) , où g:X⟶Z est un morphisme propre'",
           "the formula g_* : A(X)⟶A(Z) stands in the running text at the start of a line, followed on the same line by ', où g:X⟶Z est ...' (both scans)",
           "set as a display \\[ g_*:A(X)\\longrightarrow A(Z), \\] with 'où' on a new line", "other", "medium",
           r"(3.1) par<NL>\[<NL> g_*:A(X)\longrightarrow A(Z),<NL>\]<NL>où", r"(3.1) par $g_*:A(X)\longrightarrow A(Z)$, où",
           "In-line in the print, not displayed (compare f_*: A(Y)⟶A(X), which the print does display)."))
L.append(F(671, "3.3: display of the Gysin homomorphism f_*: H^p(Y,μ_n^{⊗i}) ⟶ H^{p+2d}(X,μ_n^{⊗(i+d)})",
           "no punctuation after the display; the sentence goes on with '(cf. n° 6), ce qui est le cas ...' (both scans)",
           "H^{p+2d}(X,\\mu_n^{\\otimes(i+d)}). (full stop added)", "extra", "high",
           r"H^{p+2d}(X,\mu_n^{\otimes(i+d)}).", r"H^{p+2d}(X,\mu_n^{\otimes(i+d)})",
           "The added stop also breaks the sentence, which continues after the display."))
L.append(F(671, "3.3, after the display: '(cf. n° 6), ce qui est le cas'",
           "(cf. n° 6) (both scans)", "(cf. no.~6)", "symbol", "high",
           r"(cf. no.~6)", r"(cf. n\textsuperscript{o}~6)", "As the n° entry above."))
L.append(F(671, "3.3, top of p. 672 in the print: '(grâce au théorème de pureté cohomologique relatif SGA 4 XVI 3.7), et, conjecturalement'",
           "p. 672 begins 'SGA 4 XVI 3.7), et, conjecturalement' with no parenthesis before SGA: the line starts at the left margin with S, like the '(d'après' line below starts with its parenthesis (both scans; " + CR + "c672_first.png, w672_top.png)",
           "relatif (SGA 4 XVI 3.7), et, (an opening parenthesis added; it leaves '(grâce' unclosed)", "extra", "high",
           r"relatif (SGA 4 XVI 3.7)", r"relatif SGA 4 XVI 3.7)",
           "In the print the ')' after 3.7 closes '(grâce'. This text is printed on p. 672 but sits in page_671.tex (see the p. 672 marker entry); apply this fix before moving that marker. " + R2 + "', grâce au théorème ... relatif (SGA 4 XVI 3.7), et,' (it drops the other parenthesis); the print agrees with neither."))
L.append(F(671, "footnote (*): 'a été prouvée depu par P. JOUANOLOU'",
           "'prouvée depu' at the end of the line, then 'par P. JOUANOLOU' (both scans; " + CR + "c671_fn.png, w671_bot.png)",
           "prouvée depuis par (silently corrected)", "misprint_in_print", "high",
           r"depuis par", r"depu par",
           "Typing error: the end of 'depuis' is missing; the line is full length, nothing is lost at the margin.",
           corrected=r"depuis par"))
L.append(F(671, "footnote (*): 'par P. JOUANOLOU (nov. 1969)'",
           "JOUANOLOU in capitals (both scans)", "P. Jouanolou", "word", "high",
           r"P. Jouanolou (nov.", r"P. JOUANOLOU (nov.",
           "The TeX keeps typed capitals of names elsewhere ('J. P. JOUANOLOU', main.tex line 17142; 'par A. GROTHENDIECK', p. 20). Same on p. 675."))
L.append(F(671, "throughout Exposé XIV: the typewriter phi (ø) of φ: A(X) ⟶ Gr_top(X), of the diagram (4.1) and of (4.4)",
           "the typed slashed o ø, i.e. the straight phi ϕ, at all 9 places of pp. 671-675 (p. 671 display; p. 673 diagram (4.1) and 'L'homomorphisme ø'; p. 674 4.2 and (4.4) five times; p. 675 'le fait que ø soit')",
           "\\varphi (19 times in Exposé XIV, no \\phi)", "symbol", "medium",
           note="Convention of the transcription, reported once: three examples p. 671 '\\varphi:A(X)\\longrightarrow \\Gtop^\\bullet(X).', p. 673 '\\arrow[r,\"\\varphi\"]', p. 674 '\\psi\\varphi(x)&='. One replacement \\varphi -> \\phi over Exposé XIV, as was applied on pp. 3 and 12 (FIXLOG_6: '\\varphi:A(X)' -> '\\phi:A(X)'). " + R2 + "also \\varphi."))

# ---------------- page 672 ----------------
L.append(F(672, "start of page",
           "p. 671 ends '... pureté cohomologique relatif'; p. 672 begins 'SGA 4 XVI 3.7), et, conjecturalement, si Y et X sont tous deux réguliers' (both scans)",
           "'(SGA 4 XVI 3.7), et,' ends the last line of page_671.tex (under the folio-671 marker); page_672.tex begins 'conjecturalement,'",
           "marker", "high",
           note="Page 672 really begins with 'SGA 4 XVI 3.7), et,'. First apply the p. 671 fix 'relatif (SGA 4 XVI 3.7)' -> 'relatif SGA 4 XVI 3.7)', then move the folio-672 marker before it: python -I move_marker.py 6 672 \"SGA 4 XVI 3.7), et,\" --before (gives '... cohomologique relatif', the marker, 'SGA 4 XVI 3.7), et,', 'conjecturalement, ...' in both layers). If the parenthesis fix is not taken, use the anchor \"(SGA 4 XVI 3.7), et,\"."))
L.append(F(672, "3.3: 'est établie dans ce cas par Atiyah et Hirzebruch [1]'",
           "Atiyah and Hirzebruch each underlined, 'et' not (both scans)", "plain", "underline", "high",
           r"par Atiyah et Hirzebruch [1]", r"par \emph{Atiyah} et \emph{Hirzebruch} [1]",
           R2 + "\\uline{Atiyah} et \\uline{Hirzebruch}: the print agrees with it."))
L.append(F(672, "3.3: '(en travaillant avec le K˙ \"naif\")'",
           "K with the raised typed dot, as in 'groupes K˙' (3.5) and the heading of §4 (both scans; " + CR + "c672_naif.png)",
           "$K^\\circ$", "symbol", "high",
           r"$K^\circ$", r"$K^\bullet$",
           "The rest of the exposé writes this K^\\bullet (40 times; this and one other place have K^\\circ). " + R2 + "K' (the print agrees with neither); 'naif' without diaeresis is the print's reading and the TeX's."))
L.append(F(672, "3.3, end: 'sur un corps k de caractéristique nulle k, lorsque k n'est pas algébriquement clos'",
           "'nulle k,' (both scans)", "nulle $k$, (printed reading kept)", "misprint_in_print", "medium",
           note="The second k repeats the first. Kept by the TeX. " + R2 + "drops it (silent correction); the print agrees with our TeX.",
           corrected=r"sur un corps $k$ de caractéristique nulle, lorsque"))
L.append(F(672, "3.4: 'puisque l'on sait de toutes façons (n° 6) que'",
           "(n° 6) (both scans)", "(no.~6)", "symbol", "high",
           r"(no.~6)", r"(n\textsuperscript{o}~6)", R2 + "n\\textsuperscript{o}~6: the print agrees with it."))
L.append(F(672, "4.1: 'sur un corps k (cf n° 8 pour un cas plus général)'",
           "'(cf n° 8': no full stop after cf (both scans; " + CR + "c672_cf8.png, w672_bot.png)",
           "(cf. no.~8 (stop supplied)", "misprint_in_print", "medium",
           r"corps $k$ (cf.", r"corps $k$ (cf",
           "Typing slip; the TeX silently supplies the stop. Independent of the n° entry below (no common text).",
           corrected=r"corps $k$ (cf."))
L.append(F(672, "4.1: '(cf n° 8 pour un cas plus général)'",
           "n° 8 (both scans)", "no.~8", "symbol", "high",
           r"no.~8", r"n\textsuperscript{o}~8", R2 + "n\\textsuperscript{o}~8: the print agrees with it."))

# ---------------- page 673 ----------------
L.append(F(673, "4.1: 'des classes de cycles à équivalence rationelle près [4]'",
           "rationelle (both scans)", "rationelle (printed reading kept)", "misprint_in_print", "high",
           note="As p. 671. " + R2 + "rationnelle (silent correction); the print agrees with our TeX.",
           corrected=r"rationnelle"))
L.append(F(673, "4.1, display: 'c_i(E̲) ∈ H^{2i}(X,Z̲_ℓ(i)) ,'",
           "E underlined (both scans; " + CR + "c673_ciE_zoom.png)", "c_i(E)", "underline", "high",
           r"c_i(E)\in", r"c_i(\underline{E})\in",
           R2 + "c_i(\\underline E): the print agrees with it. For Z̲_ℓ see the \\Zell entry."))
L.append(F(673, "4.1: '(où E̲ est un fibré vectoriel sur X'",
           "E underlined (both scans)", "$E$", "underline", "high",
           r"(où $E$ est", r"(où $\underline{E}$ est", R2 + "\\underline E: the print agrees with it."))
L.append(F(673, "throughout Exposé XIV: H^{2*}(X, Z̲_ℓ(*)) of the diagram (4.1), its definition and pp. 674 (twice in the text, (4.2))",
           "the typewriter asterisk (the same glyph as in f_*, g_*), in the exponent 2* and in the twist (*), at all 6 places of pp. 673-674 (" + CR + "c673_Zl_zoom.png, c674_42.png)",
           "H^{2\\bullet}(X,\\Zell(\\bullet)) (21 H^{2\\bullet} in Exposé XIV, no H^{2*})", "symbol", "high",
           note="Convention of the transcription, reported once: three examples p. 673 diagram 'H^{2\\bullet}(X,\\Zell(\\bullet)) & {}', p. 673 'H^{2\\bullet}(X,\\Zell(\\bullet))=\\bigoplus_i', p. 674 (4.2) 'H^{2\\bullet}(X,\\Qell(\\bullet))='. One replacement over Exposé XIV: H^{2\\bullet} -> H^{2*} and the twist (\\bullet) -> (*) in these groups. " + R2 + "H^{2*}(X,\\underline{\\Z}_\\ell(*)): the print agrees with it."))
L.append(F(673, "throughout Exposé XIV: the coefficient rings Z̲_ℓ, Q̲_ℓ (4.1, (4.1), (4.2), p. 674 text)",
           "a typed Z (and Q) underlined, with a hand-written ℓ: Z̲_ℓ, Q̲_ℓ, not double-struck (both scans; " + CR + "c673_Zl_zoom.png, c673_ciE_zoom.png, c674_42.png)",
           "\\Zell = \\mathbb Z_\\ell and \\Qell = \\mathbb Q_\\ell (main.tex lines 76-77): double-struck, no underline (26 \\Zell and 10 \\Qell in Exposé XIV)",
           "underline", "medium",
           note="Convention of the transcription, reported once: three examples p. 673 'c_i(E)\\in H^{2i}(X,\\Zell(i))', p. 674 'H^{2\\bullet}(X,\\Zell(\\bullet))\\otimes_{\\Zell}\\Qell' ((4.2), print H^{2*}(X,Z̲_ℓ(*)) ⊗_{Z̲_ℓ} Q̲_ℓ), p. 674 'dans $H^{2\\bullet}(X,\\Zell(\\bullet))$'. Fix in Exposé XIV by local macros, e.g. \\underline{Z}_\\ell and \\underline{Q}_\\ell (the typed letter, as for the typist's plain Q), or \\underline{\\mathbb Z}_\\ell as done for the underlined double-struck Z of pp. 323, 330, 408. " + R2 + "\\underline{\\Z}_\\ell, \\underline{\\Q}_\\ell: the print agrees with it on the underline."))
L.append(F(673, "diagram (4.1): label j of the vertical arrow Gr˙(X) ⟶ Gr˙_top(X)",
           "j stands to the left of the arrow, like γ on the left arrow (both scans)",
           "\\arrow[u,\"j\"'] (the prime puts j on the right)", "formula", "medium",
           r'''\arrow[u,"j"']''', r'''\arrow[u,"j"]''',
           "Label side, as the FIXLOG_6 correction of p. 59. " + R2 + "\\arrow[u,\"j\"]: the print agrees with it."))
L.append(F(673, "diagram (4.1): after Gr˙(X), bottom right",
           "'Gr˙(X)   ,' : a comma after the diagram (both scans)", "no comma", "missing", "high",
           r"{} & \operatorname{Gr}^\bullet(X)", r"{} & \operatorname{Gr}^\bullet(X),",
           "Independent of the label fix of the same cell (no common text). " + R2 + "no comma either."))
L.append(F(673, "definition of H^{2*}: '= ∐_i H^{2i}(X,Z̲_ℓ(i))'",
           "the coproduct sign ∐ (an inverted Π) with i below (both scans; " + CR + "c673_coprod.png)",
           "\\bigoplus_i", "symbol", "high",
           r"\bigoplus_i H^{2i}", r"\coprod_i H^{2i}",
           "The file uses \\coprod elsewhere. " + R2 + "\\bigoplus_i as well; the print agrees with neither."))
L.append(F(673, "4.1: 'L'homomorphisme ø est defini par exemple dans [RRR]'",
           "defini without accent (both scans; " + CR + "c673_defini.png, w673_bot.png)",
           "est défini par exemple (silently corrected)", "misprint_in_print", "high",
           r"est défini par exemple", r"est defini par exemple",
           "Typing error (accent left out; the lower-case e is not covered by the rule for unaccented capitals).",
           corrected=r"est défini par exemple"))
L.append(F(673, "4.1: 'associé à un sous-schéma fermé Y de X codimension i'",
           "'de X codimension i' (both scans)", "de $X$ codimension $i$ (printed reading kept)", "misprint_in_print", "medium",
           note="A 'de' is missing. Kept by the TeX. " + R2 + "'de $X$ de codimension $i$' (silent correction); the print agrees with our TeX.",
           corrected=r"de $X$ de codimension $i$"))
L.append(F(673, "4.1: 'l'élément cℓ˙(O̲_Y) de Filt...'",
           "after the script ℓ a raised typed dot, the dot of K˙ and Gr˙, not an i (both scans; " + CR + "c673_cl_zoom.png, w673_bot.png)",
           "$\\cl^i(\\mathcal O_Y)$", "symbol", "high",
           r"$\cl^i(\mathcal O_Y)$", r"$\cl^\bullet(\mathcal O_Y)$",
           "Written \\bullet like the raised dot of Gr. (O̲_Y written \\mathcal O_Y: pending decision, not itemized.) " + R2 + "\\cl_X^i(\\underline O_Y); the print agrees with neither."))
L.append(F(673, "4.1: '... de Filt^i_top(K˙(X)) mod Filt^{i+1}_top(K˙(X)). C'est un homomorphisme surjectif'",
           "in the running text, on the same line as cℓ˙(O̲_Y) and 'C'est un homomorphisme sur-': Filt (four letters) with i above and top below, (K˙(X)) in parentheses, and the word 'mod' between (both scans; " + CR + "c673_cl.png)",
           "a display \\[ \\Fil^i_{\\mathrm{top}}K^\\bullet(X)/\\Fil^{i+1}_{\\mathrm{top}}K^\\bullet(X). \\]: \\Fil prints Fil, a slash for 'mod', no parentheses",
           "formula", "high",
           r"de<NL>\[<NL> \Fil^i_{\mathrm{top}}K^\bullet(X)/\Fil^{i+1}_{\mathrm{top}}K^\bullet(X).<NL>\]<NL>C'est",
           r"de $\operatorname{Filt}^i_{\mathrm{top}}(K^\bullet(X))$ mod $\operatorname{Filt}^{i+1}_{\mathrm{top}}(K^\bullet(X))$. C'est",
           "\\Filt is not usable: main.tex line 13829 defines it as \\operatorname{Fil}. Independent of the cℓ˙ entry just before (no common text). The other 8 \\Fil of Exposé XIV may hide more printed Filt. " + R2 + "in-line '$\\Ftop^i(K'(X))$ mod $\\Ftop^{i+1}(K'(X))$': the print agrees with it on the in-line form, the parentheses and 'mod'."))
L.append(F(673, "4.1: 'à l'aide de l'un ou l'autre de ses anneaux (tensorisés par Q)'",
           "ses anneaux (both scans; " + CR + "c673_Q.png)", "ses anneaux (printed reading kept)", "misprint_in_print", "high",
           note="Kept by the TeX. " + R2 + "ces anneaux (silent correction); the print agrees with our TeX.",
           corrected=r"ces anneaux"))

# ---------------- page 674 ----------------
L.append(F(674, "start of page",
           "p. 673 ends '... et en particulier pour tout schéma'; p. 674 begins '(régulier ou non). Il a par contre' (both scans)",
           "the opening '(' ends the last line of page_673.tex ('pour tout schéma ('); page_674.tex begins 'régulier ou non).'",
           "marker", "high",
           note="Page 674 really begins with '(régulier'. Move the folio-674 marker before the parenthesis: python -I move_marker.py 6 674 \"(\" --before (the nearest '(' before the marker is the one ending 'schéma ('), then in both layers join the line '(' to the next one, so that it reads '(régulier ou non). Il a par contre ...' after the marker."))
L.append(F(674, "4.1: 'qu'une fois tensorisé par Q. Autre avantage de A(X)'",
           "'Autre avantage' follows 'par Q.' on the same line: no new paragraph (both scans; " + CR + "c674_concurrents.png)",
           "blank line: 'Autre avantage' opens a new paragraph", "other", "high",
           r"par $\Q$.<NL><NL>Autre avantage", r"par $\Q$. Autre avantage",
           R2 + "also a new paragraph."))
L.append(F(674, "4.1: 'sur ses concurrents Gr˙_top et Gr˙(X)'",
           "Gr˙_top without (X) before 'et' (both scans; " + CR + "c674_concurrents.png, w674_top.png)",
           "$\\Gtop^\\bullet(X)$ (the (X) supplied)", "misprint_in_print", "high",
           r"concurrents $\Gtop^\bullet(X)$", r"concurrents $\Gtop^\bullet$",
           "Typing slip; the TeX silently supplies (X). " + R2 + "has (X) too.",
           corrected=r"concurrents $\Gtop^\bullet(X)$"))
L.append(F(674, "4.1: 'qui transforme classes de Chern en classes de Chern (Cf.. n° 5)'",
           "'(Cf..' with two full stops at the end of the line (both scans; " + CR + "c674_cf.png, w674_top.png)",
           "(Cf. (one stop)", "misprint_in_print", "high",
           r"(Cf. ", r"(Cf.. ",
           "Typing error, silently corrected in the TeX. Independent of the n° entry below (no common text).",
           corrected=r"(Cf. "))
L.append(F(674, "4.1: '(Cf.. n° 5)'",
           "n° 5 (both scans)", "no 5", "symbol", "high",
           r"no 5)", r"n\textsuperscript{o} 5)", R2 + "n\\textsuperscript{o}~5: the print agrees with it."))
L.append(F(674, "4.1: 'lorsqu'on tensorise par Q̲, et on trouve un homomorphisme'",
           "a typed Q underlined at the start of the line (both scans; " + CR + "c674_Q.png); the 'tensorisé par Q.' four lines up is the hand-drawn double-struck Q",
           "$\\Q$ (= \\mathbb Q)", "font", "low",
           r"$\Q$, et on trouve", r"$\underline{Q}$, et on trouve",
           "The typist's Q (here underlined) against \\mathbb Q: volume decision with SGA 7 II issue 61. " + R2 + "$\\Q$."))
L.append(F(674, "4.2, display 'K˙(X) ⟶ Ch(A(X))'",
           "no punctuation after the display (both scans; " + CR + "c674_Ch.png)", "\\Ch(A(X)), (comma added)", "extra", "high",
           r"\Ch(A(X)),<NL>", r"\Ch(A(X))<NL>", R2 + "no comma: the print agrees with it."))
L.append(F(674, "(4.4), first line: 'ψø(x) = (-1)^{i-1}(i-1)! x  mod. torsion  pour x ∈ A^i(X)'",
           "'mod. torsion' with a full stop (both scans)", "\\bmod \\text{ torsion} (prints 'mod' without stop)", "punctuation", "high",
           r"\bmod \text{ torsion}\quad \text{pour } x\in A^i", r"\text{mod. torsion}\quad \text{pour } x\in A^i",
           "(4.5) on p. 675 prints 'mod torsion' without stop and is right as it stands. " + R2 + "\\text{mod. torsion}: the print agrees with it."))
L.append(F(674, "(4.4), first line, end: 'pour x ∈ A^i(X)'",
           "no punctuation at the end of the first line (both scans)", "A^i(X),\\\\ (comma added)", "extra", "high",
           r"(X),\\<NL> \varphi\psi", r"(X)\\<NL> \varphi\psi",
           "Independent of the mod. entry of the same line (no common text). " + R2 + "has the comma."))
L.append(F(674, "(4.4), second line: 'øψ(x) = (-1)^{i-1}(i-1)! x  mod. torsion  pour x ∈ Gr^i_top (X),'",
           "'mod. torsion' with a full stop (both scans)", "\\bmod \\text{ torsion}", "punctuation", "high",
           r"\bmod \text{ torsion}\quad \text{pour } x\in \Gtop^i", r"\text{mod. torsion}\quad \text{pour } x\in \Gtop^i",
           "As the first line."))
L.append(F(674, "(4.4), second line, end: 'pour x ∈ Gr^i_top (X),'",
           "a comma after (X) (both scans)", "\\Gtop^i(X); (semicolon)", "punctuation", "high",
           r"(X);<NL>\end{aligned}", r"(X),<NL>\end{aligned}",
           "Independent of the mod. entry of the same line. " + R2 + "has the comma: the print agrees with it."))

# ---------------- page 675 ----------------
L.append(F(675, "start of page",
           "p. 674 ends '... auquel cas la formule équivaut à'; p. 675 begins with the display '(4.5) c_i(O̲_Y) = (-1)^{i-1}(i-1)! cl(Y) mod torsion ,' (both scans)",
           "\\begin{equation}\\tag{4.5} and its first line ending '\\bmod' stand at the end of page_674.tex; the folio-675 marker stands inside the equation, before '\\text{ torsion},'",
           "marker", "high",
           note="Page 675 really begins with the display (4.5). Move the folio-675 marker above it: python -I move_marker.py 6 675 \"\\begin{equation}\\tag{4.5}\" --before (the line starts with the anchor, so the marker gets its own line after 'auquel cas la formule équivaut à'; same text in both layers)."))
L.append(F(675, "4.2: 'et dans le deuxième membre cℓ(Y) désigne la classe de Y dans A^i(Y)'",
           "A^i(Y) (both scans; " + CR + "c675_AiY.png, w675_top.png)", "A^i(X) (silently corrected)", "misprint_in_print", "high",
           r"dans $A^i(X)$. Comme", r"dans $A^i(Y)$. Comme",
           "cl(Y) is the class of Y in A^i(X) (next sentence: 'Comme A^i(X) ne change pas'). " + R2 + "A^i(X) (also corrected).",
           corrected=r"dans $A^i(X)$. Comme"))
L.append(F(675, "4.2: 'le noyau de l'application naturelle A(X) --f_*--> A(X⊗_k k')', label of the arrow",
           "the label is f with the typed asterisk below and to the right, no X (both scans; " + CR + "c675_arrow.png, w675_top.png)",
           "\\xrightarrow{f_X^*}: an index X the print does not have", "extra", "high",
           r"\xrightarrow{f_X^*}", r"\xrightarrow{f^*}",
           "Apply before the next entry (misprint fix of the same label). " + R2 + "f_X^* as well; the print agrees with neither."))
L.append(F(675, "4.2: arrow label A(X) --f_*--> A(X⊗_k k')",
           "f_* (lower asterisk) on the arrow of the pull-back (both scans)", "f^* after the previous fix (the TeX silently corrects to an upper star)", "misprint_in_print", "medium",
           r"\xrightarrow{f^*}", r"\xrightarrow{f_*}",
           "The natural map A(X) -> A(X⊗_k k') is the pull-back f^* (the same sentence writes f_* f^* = n id, f_* being the trace). Old taken from the text after the previous entry's fix (apply in this order).",
           corrected=r"\xrightarrow{f^*}", after=-1))
L.append(F(675, "4.2: '(comme on voit un utilisant l'homomorphisme trace'",
           "'un utilisant' (both scans; " + CR + "c675_trace.png, w675_bot.png)", "en utilisant (silently corrected)", "misprint_in_print", "high",
           r"comme on voit en utilisant", r"comme on voit un utilisant",
           "Typing error. " + R2 + "'comme on le voit en utilisant' (corrected, with an added le).",
           corrected=r"comme on voit en utilisant"))
L.append(F(675, "4.2: 'l'homomorphisme trace f_* : A(X⊗_k k') ⟶ A(X)'",
           "f_* with the asterisk alone as index, no X (both scans; " + CR + "c675_trace.png)", "$f_{X*}:A(X\\otimes_k k')$", "extra", "high",
           r"$f_{X*}:A(X\otimes_k k')", r"$f_*:A(X\otimes_k k')",
           R2 + "f_{X*} as well; the print agrees with neither."))
L.append(F(675, "4.2: 'satisfaisant f_* f^* = n id)'",
           "f_* f^* without X (both scans)", "$f_{X*}f_X^*=n\\,\\id$", "extra", "high",
           r"$f_{X*}f_X^*=n\,\id$", r"$f_*f^*=n\,\id$",
           R2 + "f_{X*}f_X^* as well."))
L.append(F(675, "footnote (*) 'Elle est donc établie grâce à P. JOUANOLOU ...': its call mark",
           "no call mark (*) anywhere in the text of the page, only the note at its foot (both scans; w675_top.png, w675_bot.png)",
           "\\footnote{...} after 'n\\,\\id$).' (end of 4.2): a mark the print does not have, at an editorial place", "misprint_in_print", "low",
           r"\footnote{Elle est donc", r"\sgastandalonefootnotetext{xiv-jouanolou}{Elle est donc",
           "The typist left out the call mark (the note's 'Elle' is the exact formula (4.5), cf. note p. 5). The fix sets the note without a mark with the file's own macro (main.tex line 66); that macro gives the note the number of the previous footnote, so the volume's footnote-mark decision (findings_016_020, p. 20) may prefer to leave the \\footnote. The corrected layer keeps the \\footnote. " + R2 + "puts its marked footnote at the same place.",
           corrected=r"\footnote{Elle est donc"))
L.append(F(675, "footnote (*): 'grâce à P. JOUANOLOU pour X lisse'",
           "JOUANOLOU in capitals (both scans)", "P. Jouanolou", "word", "high",
           r"P. Jouanolou pour", r"P. JOUANOLOU pour",
           "As p. 671. " + R2 + "P. JOUANOLOU: the print agrees with it."))
L.append(F(675, "4.3: 'ou ce qui revient au même, que la formule 4.5. soit vraie non seulement modulo torsion'",
           "'formule 4.5.' without parentheses, with a full stop after 5 (both scans; " + CR + "c675_45.png, w675_bot.png)",
           "la formule (4.5) soit (silently corrected)", "misprint_in_print", "medium",
           r"la formule (4.5) soit", r"la formule 4.5. soit",
           "Elsewhere the print writes the formula (4.5). " + R2 + "(4.5) (also corrected).",
           corrected=r"la formule (4.5) soit"))
L.append(F(675, "4.3: 'nous avons signalé déjà au n° 3 que lorsque'",
           "n° 3 (both scans)", "au no. 3", "symbol", "high",
           r"au no. 3", r"au n\textsuperscript{o} 3", R2 + "n\\textsuperscript{o}~3: the print agrees with it."))
L.append(F(675, "4.3: 'ont même image dans Gr˙_top(X), ou ce qui revient au même, que la deuxième des formules (4.4)'",
           "no comma after 'ou' (both scans; " + CR + "c675_ou.png)", "ou, ce qui revient au même, (comma added)", "extra", "high",
           r"(X)$, ou, ce qui", r"(X)$, ou ce qui", R2 + "'ou ce qui revient': the print agrees with it."))
L.append(F(675, "end of page",
           "p. 675 ends '... au cas de la caractéristique quelconque, une fois'; p. 676 begins 'résolu de façon satisfaisante la question soulevée au n° 1' (witness p. 676, " + CR + "w676_top.png)",
           "'résolu de' ends the last line of page_675.tex (under the folio-675 marker); the folio-676 text begins 'façon satisfaisante'",
           "marker", "high",
           note="Page 676 really begins with 'résolu de'. Move the folio-676 marker before it: python -I move_marker.py 6 676 \"résolu de\" --before (gives '... une fois', the marker, 'résolu de', 'façon satisfaisante ...' in both layers)."))

# ---------------- checks ----------------
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(671, 676)}
work = dict(pages)
ok = True
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    t = work[d["page"]] if "_after" in d else pages[d["page"]]
    n = t.count(fx["old"])
    if "_after" not in d and work[d["page"]].count(fx["old"]) != 1:
        ok = False
        print("OVERLAP with an earlier fix", i, d["page"], repr(fx["old"][:60]))
    if n != 1 or fx["old"] == fx["new"]:
        ok = False
        print("PROBLEM", i, d["page"], repr(fx["old"][:60]), n)
    for line in fx["old"].split("\n"):
        if "%%%%%%%%%%  scan idx" in line:
            ok = False
            print("MARKER IN OLD", i)
    # apply to the sequential text so that dependent fixes can be checked
    if work[d["page"]].count(fx["old"]) == 1:
        work[d["page"]] = work[d["page"]].replace(fx["old"], fx["new"])
for d in L:
    d.pop("_after", None)
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
counts = {}
for d in L:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "NOT OK", len(L), "entries;", counts)
