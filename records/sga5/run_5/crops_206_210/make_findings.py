"""Builds findings_206_210.json for SGA 5 pp. 206-210 and checks every fix's old string against its page file."""
import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'run_5')
OUT = os.path.join(RUN, 'findings_206_210.json')
NL = '\n'


def F(page, where, scan, tex, kind, conf, old=None, new=None, note='', corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind, 'confidence': conf,
         'fix': None if old is None else {'old': old, 'new': new}}
    if corrected is not None:
        d['corrected'] = corrected
    d['note'] = note
    return d


L = []

# ---------------- page 206 ----------------
L.append(F(206, "top of the page: 'suivante:' before the first display",
           "p. 206 begins with the display Hom_Ĉ(M ⊗_A X, Y) = Hom_A(M,Hom_C(X,Y) .; p. 205 ends with "
           "'l'égalité précédente prend l'allure plus familière / suivante :'",
           "'suivante:' is the first line under the folio-206 marker",
           'marker', 'high',
           note=r"Page 206 really begins at the '\[' of the display, after 'suivante:'. Exact fix: "
                r"python -I move_marker.py 5 206 '\[' . Text not moved. Already done in both live layers of s5.tex "
                r"(state of 20:52): the marker stands after 'suivante:' there, and the command, simulated in memory, "
                r"moves it by 0 characters; nothing left to do."))
L.append(F(206, "after the first display: 'Si le foncteur M ⊗_A X est représentable'",
           "a new, indented paragraph",
           r"runs on from the display (no blank line after \])",
           'other', 'high', r"\]" + NL + "Si le foncteur", r"\]" + NL + NL + "Si le foncteur",
           note="Paragraph break of the print left out."))
L.append(F(206, "first display, right-hand side 'Hom_A(M, ...'",
           "Hom_A is not underlined (as in the display of p. 205)",
           r"\uHom_A(M,",
           'underline', 'high', r"\uHom_A(M,", r"\Hom_A(M,",
           note=r"\uHom is \underline{\Hom}; the print has a plain Hom here."))
L.append(F(206, "first display, end: 'Hom_A(M,Hom_C(X,Y) .'",
           "one closing parenthesis only: the parenthesis opened after Hom_A is never closed",
           r"\Hom_{\cC}(X,Y)).",
           'misprint_in_print', 'high', "(X,Y)).", "(X,Y).",
           corrected="(X,Y)).",
           note="The TeX silently adds the missing parenthesis; the fix restores the print. "
                r"Independent of the \uHom_A fix (no overlap)."))
L.append(F(206, "'ce qui nous permettra de parler du bifoncteur (deux fois covariant) produit tensoriel externe'",
           "'(deux fois covariant)' in parentheses",
           "'bifoncteur, deux fois covariant, produit'",
           'punctuation', 'high', "bifoncteur, deux fois covariant, produit",
           "bifoncteur (deux fois covariant) produit"))
L.append(F(206, "label of Proposition 1.2.2",
           "'PROPOSITION 1.2.2. (Critères de représentabilité).': a full stop after the number",
           r"\begin{statement}{Proposition 1.2.2 (Critères de représentabilité)}, which prints "
           "'Proposition 1.2.2 (Critères de représentabilité).'",
           'punctuation', 'high', "{Proposition 1.2.2 (Critères", "{Proposition 1.2.2. (Critères",
           note="The environment adds the final full stop after the parenthesis, as in the print."))
L.append(F(206, "Proposition 1.2.2 (c): 'possède des sommes directes \"quelconques\"'",
           "\"quelconques\" in typewriter double quotes",
           "sommes directes quelconques",
           'punctuation', 'high', "sommes directes quelconques", "sommes directes ``quelconques''",
           note="Quotation marks missing in the TeX (the file writes ``...'' for them in this exposé, p. 208)."))
L.append(F(206, "Proposition 1.2.2 (c): 'représentable pour \"tout\" couple (M,X)'",
           "\"tout\" in typewriter double quotes",
           "pour tout couple",
           'punctuation', 'high', "pour tout couple", "pour ``tout'' couple",
           note="Quotation marks missing in the TeX."))
L.append(F(206, "proof of Proposition 1.2.2",
           "'Démonstration : L'assertion (a) est claire.' (Démonstration underlined, then a colon)",
           r"\begin{prooftext}[Démonstration] ... \end{prooftext}; Exposé V's prooftext prints 'Démonstration.'",
           'punctuation', 'high',
           r"\begin{prooftext}[Démonstration]" + NL + "L'assertion (a) est claire. Les deux autres assertions "
           "résultent alors du lemme ci-dessous, dont la démonstration est immédiate." + NL + r"\end{prooftext}",
           r"\emph{Démonstration} : L'assertion (a) est claire. Les deux autres assertions résultent alors du "
           "lemme ci-dessous, dont la démonstration est immédiate.",
           note=r"Proof label of the print, set like the '\emph{Preuve} :' paragraphs of this exposé; one edit "
                r"for the whole environment, so that \begin and \end go together."))

# ---------------- page 207 ----------------
L.append(F(207, "Remarque 1.2.4: 'mais C possède des sommes directes'",
           "'mais C possède' (no 'que')",
           r"mais que $\cC$ possède",
           'extra', 'high', r"mais que $\cC$ possède", r"mais $\cC$ possède"))
L.append(F(207, "Remarque 1.2.4: 'des sommes directes \"quelconques\" . On pose'",
           "\"quelconques\" in typewriter double quotes",
           "directes quelconques.",
           'punctuation', 'high', "directes quelconques.", "directes ``quelconques''.",
           note="Quotation marks missing in the TeX."))
L.append(F(207, "heading '2. Condition de Mittag-Leffler-Artin-Rees.'",
           "the underlined title ends with a full stop",
           r"\subsection*{2. Condition de Mittag-Leffler-Artin-Rees}",
           'punctuation', 'high', "{2. Condition de Mittag-Leffler-Artin-Rees}",
           "{2. Condition de Mittag-Leffler-Artin-Rees.}"))
L.append(F(207, "'on pose P = Hom(ℕ°, C) , catégorie des systèmes projectifs'",
           "Hom underlined",
           r"P=\Hom(\NN^\circ,\cC)",
           'underline', 'high', r"P=\Hom(\NN^\circ,\cC)", r"P=\uHom(\NN^\circ,\cC)",
           note="The functor category Hom(ℕ°,C) has its Hom underlined in the print, as Ĉ = Hom(C,Ens)° on p. 205."))
L.append(F(207, "heading '2.1. Condition de Mittag-Leffler-Artin-Rees.' (run into the text)",
           "the underlined title ends with a full stop",
           r"\subsubsection*{2.1. Condition de Mittag-Leffler-Artin-Rees}",
           'punctuation', 'high', "{2.1. Condition de Mittag-Leffler-Artin-Rees}",
           "{2.1. Condition de Mittag-Leffler-Artin-Rees.}"))
L.append(F(207, "'un morphisme noté h[r] de X[r] dans Y[r] et cela de façon fonctorielle'",
           "no comma after Y[r]",
           r"dans $Y[r]$, et cela",
           'punctuation', 'high', r"dans $Y[r]$, et cela", r"dans $Y[r]$ et cela",
           note="Comma added by the TeX."))
L.append(F(207, "'les \"morphismes de transition\" X_{n+s} ⟶ X_{n+r} (n ≥ 0)'",
           "\"morphismes de transition\" in typewriter double quotes",
           "les morphismes de transition",
           'punctuation', 'high', "les morphismes de transition", "les ``morphismes de transition''",
           note="Quotation marks missing (the TeX has them for the same words on p. 208)."))
L.append(F(207, "'définissent un morphisme w_sr de X[s] dans X[r] ,'",
           "in the line and in words: 'un morphisme w_sr de X[s] dans X[r] ,'",
           r"a display 'w_{sr}:X[s]\longrightarrow X[r],'",
           'word', 'high',
           "un morphisme" + NL + r"\[" + NL + r"w_{sr}:X[s]\longrightarrow X[r]," + NL + r"\]",
           r"un morphisme $w_{sr}$ de $X[s]$ dans $X[r]$,",
           note="The print has no colon and no arrow here; 'de ... dans' are its words."))
L.append(F(207, "'et il est clair que si t est un troisième entier avec t ≥ s ≥ r'",
           "no comma after 'que'",
           r"clair que, si $t$",
           'punctuation', 'high', r"clair que, si $t$", r"clair que si $t$",
           note="Comma added by the TeX."))

# ---------------- page 208 ----------------
L.append(F(208, "top of the page: 'vérifiée:' before the display w_ts ∘ w_sr = w_tr",
           "p. 208 begins with the display 'w_ts ∘ w_sr = w_tr .'; p. 207 ends with 'l'égalité ci-dessous est vérifiée :'",
           "'vérifiée:' is the first line under the folio-208 marker",
           'marker', 'high',
           note=r"Page 208 really begins at the '\[' of that display. Exact fix: python -I move_marker.py 5 208 '\[' "
                r"(simulated in memory on both live layers: the marker moves 10 characters, to just after "
                r"'vérifiée:'). Text not moved."))
L.append(F(208, "first display",
           "'w_ts ∘ w_sr = w_tr .'",
           r"w_{ts}\circ w_{sr}=w_{tr}.",
           'misprint_in_print', 'high',
           corrected=r"w_{sr}\circ w_{ts}=w_{tr}.",
           note="The TeX keeps the printed reading. w_ts : X[t] → X[s] and w_sr : X[s] → X[r] compose to "
                "w_sr ∘ w_ts; the exposé writes composites in the usual order ('le composé v∘u' for u : X → Y, "
                r"v : Y → Z, p. 210). The current layer of s5.tex already reads w_{sr}\circ w_{ts}."))
L.append(F(208, "'Enfin, si 0 ⟶ X ⟶ Y ⟶ Z ⟶ 0 est une suite exacte de P'",
           "a new, indented paragraph",
           "runs on after 'et cela de façon fonctorielle.'",
           'other', 'high', "fonctorielle. Enfin, si", "fonctorielle." + NL + NL + "Enfin, si",
           note="Paragraph break of the print left out."))
L.append(F(208, "'la suite correspondante ci-dessous dans P̄ = Hom(ℕ°, P) est exacte :'",
           "Hom underlined",
           r"\overline P=\Hom(\NN^\circ,P)",
           'underline', 'high', r"\overline P=\Hom(\NN^\circ,P)", r"\overline P=\uHom(\NN^\circ,P)",
           note=r"In 'de la catégorie Hom(ℕ°,P).' higher on the page the print does not underline Hom; the "
                r"TeX's \Hom there is right."))
L.append(F(208, "Définition 2.1.1, first sentence",
           "'Soit un objet de la catégorie P .' (no letter X)",
           "Soit un objet de la catégorie $P$.",
           'misprint_in_print', 'medium',
           corrected="Soit $X$ un objet de la catégorie $P$.",
           note="The TeX keeps the printed reading. The display of the definition uses X, which the print "
                "never introduces: the letter has dropped out."))
L.append(F(208, "Définition 2.1.1: 'tel que pour tout entier s ≥ r l'égalité ci-dessous soit vérifiée'",
           "no commas around 'pour tout entier s ≥ r'",
           r"tel que, pour tout entier $s\ge r$, l'égalité",
           'punctuation', 'high', r"tel que, pour tout entier $s\ge r$, l'égalité",
           r"tel que pour tout entier $s\ge r$ l'égalité",
           note="Two commas added by the TeX."))
L.append(F(208, "'Il revient au même de dire que pour tout entier n ≥ 0 les images'",
           "no commas around 'pour tout entier n ≥ 0'",
           r"dire que, pour tout entier $n\ge0$, les images",
           'punctuation', 'high', r"dire que, pour tout entier $n\ge0$, les images",
           r"dire que pour tout entier $n\ge0$ les images",
           note="Two commas added by the TeX."))
L.append(F(208, "heading '2.2. Systèmes projectifs AR-nuls.'",
           "the underlined title ends with a full stop",
           r"\subsubsection*{2.2. Systèmes projectifs AR-nuls}",
           'punctuation', 'high', "{2.2. Systèmes projectifs AR-nuls}", "{2.2. Systèmes projectifs AR-nuls.}"))

# ---------------- page 209 ----------------
L.append(F(209, "Proposition 2.2.2 (i)",
           "'(i) Y est AR-nul,' (comma)",
           r"\item $Y$ est AR-nul;",
           'punctuation', 'high', r"\item $Y$ est AR-nul;", r"\item $Y$ est AR-nul,"))
L.append(F(209, "proof of 2.2.2: 'à la condition de la définition (2.2.1) pour X et Z'",
           "'(2.2.1)' in parentheses",
           "la définition 2.2.1 pour $X$",
           'punctuation', 'high', "condition de la définition 2.2.1 pour $X$",
           "condition de la définition (2.2.1) pour $X$"))
L.append(F(209, "proof of 2.2.2: 'aux conditions de la définition (2.2.1) pour Y'",
           "'(2.2.1)' in parentheses",
           "la définition 2.2.1 pour $Y$",
           'punctuation', 'high', "conditions de la définition 2.2.1 pour $Y$",
           "conditions de la définition (2.2.1) pour $Y$"))
L.append(F(209, "proof of 2.2.2: 'l'entier s + t répond aux conditions'",
           "'s + t'",
           "$s+t$",
           'misprint_in_print', 'high',
           corrected="$r+t$",
           note="The TeX keeps the printed reading. The integers chosen are r (for X) and t (for Z); s does not "
                "occur in the proof."))
L.append(F(209, "heading '2.3. Rappels sur le calcul de fractions et applications.'",
           "the underlined title ends with a full stop",
           r"\subsubsection*{2.3. Rappels sur le calcul de fractions et applications}",
           'punctuation', 'high', "{2.3. Rappels sur le calcul de fractions et applications}",
           "{2.3. Rappels sur le calcul de fractions et applications.}"))
L.append(F(209, "'S une partie de FL(E)'",
           "'FL(E)' with a capital L (p. 210 types 'Fl(E)' twice)",
           r"$\Fl(\cE)$",
           'misprint_in_print', 'high', r"$\Fl(\cE)$", r"$\operatorname{FL}(\cE)$",
           corrected=r"$\Fl(\cE)$",
           note=r"The TeX silently normalizes to \Fl (\operatorname{Fl}); the fix restores the print."))
L.append(F(209, "'vérifiant la propriété universelle suivante : / Pour qu'un foncteur u de E'",
           "'suivante :' ends the paragraph; 'Pour qu'un foncteur' begins a new, indented paragraph with a capital P",
           "suivante: pour qu'un foncteur (same paragraph, small p)",
           'other', 'high', "suivante: pour qu'un foncteur", "suivante:" + NL + NL + "Pour qu'un foncteur",
           note="Paragraph break and capital P of the print."))
L.append(F(209, "'L'unicité d'un tel couple modulo isomorphisme est claire.'",
           "a new, indented paragraph",
           "runs on after 'et alors la factorisation est unique.'",
           'other', 'high', "est unique. L'unicité", "est unique." + NL + NL + "L'unicité",
           note="Paragraph break of the print left out."))
L.append(F(209, "end of the page: '(Voir aussi : P. Gabriel et M. Zisman, ... 1967.)'",
           "'(Voir aussi : P. Gabriel et M. Zisman, Calculus of fractions and homotopy theory, Erg. der Math., 35, "
           "Springer-Verlag, 1967.)': in parentheses, a colon after 'aussi', the title neither underlined nor in "
           "another style; p. 210 goes on unindented ('Certaines propriétés ...'), so the paragraph continues",
           r"'Voir aussi P. Gabriel et M. Zisman, \emph{Calculus of fractions and homotopy theory}, Erg. der Math., "
           "35, Springer-Verlag, 1967.' and a blank line before the folio-210 marker",
           'punctuation', 'high',
           r"Voir aussi P. Gabriel et M. Zisman, \emph{Calculus of fractions and homotopy theory}, Erg. der Math., "
           "35, Springer-Verlag, 1967." + NL + NL,
           "(Voir aussi : P. Gabriel et M. Zisman, Calculus of fractions and homotopy theory, Erg. der Math., 35, "
           "Springer-Verlag, 1967.)" + NL,
           note=r"One edit: the parentheses and colon of the print; no \emph; and the blank line before the "
                "folio-210 marker goes, since 'Certaines propriétés' at the top of p. 210 starts at the left margin "
                "(x 181 px, as the other lines of p. 210; the paragraph indent there is x 365) while this typist "
                "indents a new paragraph at the top of a page ('Il est clair', p. 209). 'Voir aussi :' is typed in "
                "a heavier (bold) face and the reference in another typeface (a typed insertion): not marked."))

# ---------------- page 210 ----------------
L.append(F(210, "first sentence: 'une description simple de la catégorie E(S^{-1}) :'",
           "ends with a colon",
           r"catégorie $\cE(S^{-1})$.",
           'punctuation', 'high', r"catégorie $\cE(S^{-1})$.", r"catégorie $\cE(S^{-1})$:"))
L.append(F(210, "Définition 2.3.1 (c), end: 'dans lequel s appartient à S .'",
           "a full stop before the diagrams (D_1), (D_2)",
           "dans lequel $s$ appartient à $S$:",
           'punctuation', 'high', "appartient à $S$:" + NL + r"\[", "appartient à $S$." + NL + r"\["))
L.append(F(210, "diagram (D_1): the arrow X —u→ Y",
           "u above the arrow",
           r"""\arrow[r,"u"'] (label below the arrow)""",
           'symbol', 'high',
           r"""& X \arrow[r,"u"'] & Y""" + NL + r"\end{tikzcd}" + NL + r"\qquad",
           r"""& X \arrow[r,"u"] & Y""" + NL + r"\end{tikzcd}" + NL + r"\qquad",
           note="Label position in the diagram."))
L.append(F(210, "diagram (D_2): the bottom arrow X —u→ Y",
           "u above the arrow",
           r"""\arrow[r,"u"'] (label below the arrow)""",
           'symbol', 'high',
           r"""\arrow[d,"s"'] & Y' \arrow[d,"t"]""" + "\\\\" + NL + r"""& X \arrow[r,"u"']""",
           r"""\arrow[d,"s"'] & Y' \arrow[d,"t"]""" + "\\\\" + NL + r"""& X \arrow[r,"u"]""",
           note="Label position in the diagram (u' on the top arrow stands above, as in the print)."))
L.append(F(210, "diagram (D_2), after Y",
           "no full stop after the diagram",
           "& Y .",
           'punctuation', 'high', "& Y .", "& Y",
           note="Full stop added by the TeX at the end of the display."))
L.append(F(210, "Définition 2.3.1 (d): 'Pour tout diagramme commutatif :'",
           "a colon after 'commutatif'",
           "Pour tout diagramme commutatif (no colon)",
           'punctuation', 'high', "Pour tout diagramme commutatif" + NL, "Pour tout diagramme commutatif:" + NL))
L.append(F(210, "(d), second diagram: the arrow T —t→ X",
           "the hand-written t stands above the arrow",
           r"""T \arrow[r,"t"'] (label below the arrow)""",
           'symbol', 'high', r"""T \arrow[r,"t"']""", r"""T \arrow[r,"t"]""",
           note="Label position in the diagram."))
L.append(F(210, "(d), second diagram, after Y",
           "no punctuation after the diagram",
           "& Y,",
           'punctuation', 'high', "& Y,", "& Y",
           note="Comma added by the TeX at the end of the display (the first diagram's 'Z ,' is in the print)."))
L.append(F(210, "'Dualement on définit la notion suivante :'",
           "ends with a colon",
           "la notion suivante.",
           'punctuation', 'high', "la notion suivante.", "la notion suivante:"))
for x in 'abc':
    L.append(F(210, "Définition 2.3.2, item (%s)'" % x,
               "'(%s)'': the prime after the closing parenthesis" % x,
               r"\item[(%s')]" % x,
               'symbol', 'high', r"\item[(%s')]" % x, r"\item[(%s)']" % x))
L.append(F(210, "end of the page: 'à $S$,' at the end of the (c') line",
           "p. 210 ends with '(c)' Tout diagramme du type (D_1)' ci-dessous, dans lequel s appartient'; p. 211 begins "
           "'à S , peut se compléter en un diagramme du type (D_2)' ...'",
           "'à $S$,' ends the last line of page_210.tex; the folio-211 marker follows",
           'marker', 'high',
           note=r"Page 211 really begins at 'à $S$,'. Exact fix: python -I move_marker.py 5 211 'à $S$,' --before "
                r"(simulated in memory on both live layers: the marker goes on its own line between "
                r"'dans lequel $s$ appartient ' and 'à $S$,'). Text not moved."))

# ---------------- checks ----------------
ok = True
pages = {}
for p in sorted({d['page'] for d in L}):
    pages[p] = open(os.path.join(RUN, 'b206_210', 'page_%d.tex' % p), encoding='utf-8', newline='').read()
work = dict(pages)
for i, d in enumerate(L):
    if d['fix'] is None:
        continue
    old, new = d['fix']['old'], d['fix']['new']
    n = pages[d['page']].count(old)
    if n != 1:
        ok = False
        print('NOT UNIQUE', n, d['page'], repr(old))
    if '%%%%%%%%%%' in old:
        ok = False
        print('MARKER IN OLD', d['page'], repr(old))
    # sequential application
    m = work[d['page']].count(old)
    if m != 1:
        ok = False
        print('SEQUENTIAL PROBLEM', m, d['page'], repr(old))
    else:
        work[d['page']] = work[d['page']].replace(old, new)
print('findings:', len(L), 'all unique:', ok)
for p in sorted(pages):
    nm = sum(1 for d in L if d['page'] == p and d['kind'] == 'misprint_in_print')
    nn = sum(1 for d in L if d['page'] == p and d['kind'] != 'misprint_in_print')
    print(p, '%d/%d' % (nn, nm))
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(L, f, ensure_ascii=False, indent=1)
    print('written', OUT)
