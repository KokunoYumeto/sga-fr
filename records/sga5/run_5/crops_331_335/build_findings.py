"""Build findings_331_335.json and check every fix: its "old" must occur exactly once in the page file as it stands,
and exactly once at its turn when the page's fixes are applied in the listed order."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b331_335"
OUT = RUN / "findings_331_335.json"

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


NL = "\n"

# ---------------------------------------------------------------- page 331
add(331, "Proposition 8.5 a), first line of the page", "et la matrice inverse de (8.3.2) est (words underlined, the number not)",
    "et la matrice inverse de (8.3.2) est (no underline)", "underline", "high",
    r"et la" + NL + r"matrice inverse de (8.3.2) est",
    r"\emph{et la matrice inverse de} (8.3.2) \emph{est}",
    "Exposé VII: the TeX has no underline markup for statements; \\emph is the file's command (as the applied statements of pp. 283-295).")
add(331, "matrix (8.5.3), lower right entry", "g*(.)c_{d-1}(F), F without the check",
    r"g^*(\cdot)c_{d-1}(\check F)", "misprint_in_print", "medium",
    r"c_{d-1}(\check F)" + NL + r"\end{pmatrix}.", r"c_{d-1}(F)" + NL + r"\end{pmatrix}.",
    "No trace of a check above F at high zoom, where the hand-drawn checks of the lambda display and of (8.5.4) on the same page are sharp; the same F without check in the first matrix of the proof and in the display at the top of p. 332. The TeX silently corrects (F-check as in Lemme 8.4.3 and the lambda display).",
    r"c_{d-1}(\check F)")
add(331, "Proposition 8.5 b), first line", "b) Pour tout entier  p >= 0, la suite ('Pour tout entier' and 'la suite' underlined)",
    "no underline", "underline", "high",
    r"\item Pour tout entier $p\ge0$, la suite", r"\item \emph{Pour tout entier} $p\ge0$, \emph{la suite}")
add(331, "Proposition 8.5 b), 'dans laquelle lambda et mu désignent les flèches'", "the words underlined, lambda and mu not",
    "no underline", "underline", "high",
    r"dans laquelle $\lambda$ et $\mu$ désignent les flèches",
    r"\emph{dans laquelle} $\lambda$ \emph{et} $\mu$ \emph{désignent les flèches}")
add(331, "Proposition 8.5 b), display of lambda and mu",
    "lambda : x |--> [g*(x)c_{d-1}(F-check), -i_*(x)] / mu : (x,y) |-> j_*(x) + f*(y) (two lines, no punctuation)",
    r"\lambda(x)=\bigl(g^*(x)c_{d-1}(\check F),-i_*(x)\bigr), \qquad \mu(x,y)=j_*(x)+f^*(y),",
    "formula", "high",
    r"\lambda(x)=\bigl(g^*(x)c_{d-1}(\check F),-i_*(x)\bigr)," + NL + r"\qquad" + NL + r"\mu(x,y)=j_*(x)+f^*(y),",
    r"\lambda : x\longmapsto [g^*(x)c_{d-1}(\check F),-i_*(x)]" + NL + r"\qquad" + NL + r"\mu : (x,y)\mapsto j_*(x)+f^*(y)",
    "The print gives the maps with colon and mapsto arrows (long for lambda, short for mu) and square brackets; the TeX rewrites them as equations with parentheses and adds a comma after each.")
add(331, "Proposition 8.5 b), 'est exacte. De plus, l'application lambda a pour inverse à gauche'",
    "'est exacte. De plus, l'application' and 'a pour inverse à gauche' underlined", "no underline", "underline", "high",
    r"est exacte. De plus, l'application $\lambda$ a pour inverse à gauche",
    r"\emph{est exacte. De plus, l'application} $\lambda$ \emph{a pour inverse à gauche}")
add(331, "Proposition 8.5 b), display of lambda'", "lambda' : (x,y) |--> g_*(x) .", r"\lambda'(x,y)=g_*(x).",
    "formula", "high", r"\lambda'(x,y)=g_*(x).", r"\lambda' : (x,y)\longmapsto g_*(x).")
add(331, "proof of 8.5 a), first matrix, upper left entry", "f* (asterisk raised)", "f_*", "misprint_in_print", "high",
    r"pour voir que" + NL + r"\[" + NL + r"\begin{pmatrix}" + NL + r"f_*",
    r"pour voir que" + NL + r"\[" + NL + r"\begin{pmatrix}" + NL + r"f^*",
    "The first matrix of the proof is (8.5.3), whose upper left entry is f_*; the argument uses f_*f* = id (4.2) for that entry. The asterisk is clearly raised (as in the second matrix's f*). The TeX silently corrects.",
    r"f_*")
add(331, "proof of 8.5 a), first matrix, lower right entry", "g*(.)c_{d-1}(F), F without the check",
    r"g^*(\cdot)c_{d-1}(\check F)", "misprint_in_print", "medium",
    r"c_{d-1}(\check F)" + NL + r"\end{pmatrix}" + NL + r"\circ", r"c_{d-1}(F)" + NL + r"\end{pmatrix}" + NL + r"\circ",
    "As in (8.5.3): no trace of a check above F; the TeX silently corrects.", r"c_{d-1}(\check F)")
add(331, "display (8.5.4)", "gamma j_* + id = g*[g_*(.)c_{d-1}(F-check)],  (square brackets)",
    r"g^*(g_*(\cdot)c_{d-1}(\check F)),", "formula", "high",
    r"g^*(g_*(\cdot)c_{d-1}(\check F)),", r"g^*[g_*(\cdot)c_{d-1}(\check F)],",
    "Square brackets of the print. In the current layer, which already corrects the bracket's place (next item), the same change reads g^*[g_*(\\cdot)]c_{d-1}(\\check F).")
add(331, "display (8.5.4), place of the closing bracket", "g*[g_*(.)c_{d-1}(F-check)]",
    r"g^*(g_*(\cdot)c_{d-1}(\check F)) (printed placement kept)", "misprint_in_print", "medium", None, None,
    "The bracket closes after c_{d-1}(F-check), so g* would act on a class of Y'; the product of the matrices (8.5.3) and (8.3.2) gives in the lower right gamma j_* + id = g*[g_*(.)] c_{d-1}(F-check). The same placement in the display at the top of p. 332. The TeX keeps the printed placement; the current layer already reads g^*(g_*(\\cdot))c_{d-1}(\\check F).",
    r"g^*[g_*(\cdot)]c_{d-1}(\check F)")
add(331, "'d'où par (4.2)  j_* gamma f* = 0'", "d'où par (4.2)  j_*gamma f* = 0, (no commas around 'par (4.2)')",
    "d'où, par (4.2), $j_*\\gamma f^*=0$,", "punctuation", "high",
    r"d'où, par (4.2), $j", r"d'où par (4.2) $j", "The TeX adds two commas.")

# ---------------------------------------------------------------- page 332
add(332, "top of the page / folio-332 marker", "p. 332 begins with the display f*f_*j_* = j_* gamma j_* + j_* ,",
    "the display stands at the end of page_331.tex, under the folio-331 marker", "marker", "high", None, None,
    "Page 331 ends with '... Montrons (8.5.4). De (8.5.1) résulte que' and a blank lower half. Page 332 really begins at the '\\[' that opens the display 'f^*f_*j_*=j_*\\gamma j_*+j_*,' (the last three lines of page_331.tex). Exact fix: python -I move_marker.py 5 332 '\\[' --before (simulated in memory on both layers: the marker then stands between '... De (8.5.1) résulte que' and that '\\['; diplomatic s5.tex line 11266, current 11262 at the time of the check). No edit of this batch touches the three lines.")
add(332, "display after 'compte tenu de (8.4.3),'", "j_*g*(g_*(.)c_{d-1}(F))=j_* gamma j_* + j_* . (F without the check)",
    r"c_{d-1}(\check F)", "misprint_in_print", "medium",
    r"c_{d-1}(\check F))=j_*", r"c_{d-1}(F))=j_*",
    "No trace of a check above F at high zoom (as the two matrices of p. 331); the display applies Lemme 8.4.3, which has F-check. The TeX silently corrects.",
    r"c_{d-1}(\check F))=j_*")
add(332, "same display, place of the parentheses", "j_*g*(g_*(.)c_{d-1}(F))",
    r"j_*g^*(g_*(\cdot)c_{d-1}(\check F)) (printed placement kept)", "misprint_in_print", "medium", None, None,
    "As (8.5.4) on p. 331: by f_*j_* = i_*g_* and Lemme 8.4.3, f*i_*g_*(x) = j_*(g*(g_*(x)) c_{d-1}(F-check)). The TeX keeps the printed placement; the current layer already reads j_*(g^*(g_*(\\cdot))c_{d-1}(\\check F)).",
    r"j_*(g^*(g_*(\cdot))c_{d-1}(\check F))")
add(332, "'... dans l'autre sens est l'identité. Montrons b).'", "one paragraph: 'est l'identité. Montrons b). De 8.4.3 ...' on one line",
    "paragraph break before 'Montrons b).'", "other", "high",
    r"est l'identité." + NL + NL + r"Montrons b).", r"est l'identité. Montrons b).",
    "Paragraph break the print does not have.")
add(332, "'lambda'o(lambda o lambda') = id'", "lambda' o (lambda o lambda') = id",
    r"\lambda'\circ(\lambda\circ\lambda')=\operatorname{id}", "misprint_in_print", "high", None, None,
    "From lambda' o lambda = id one gets lambda' o (lambda o lambda') = lambda', which is what the next step uses ((mu + lambda')(lambda o lambda'(x)) = (mu + lambda')(x) when mu(x) = 0). The TeX keeps the printed reading; the current layer already reads \\lambda'.",
    r"\lambda'\circ(\lambda\circ\lambda')=\lambda'")
add(332, "'= id  de sorte que'", "no comma after 'id'", "$, de sorte que", "punctuation", "high",
    r"$, de sorte que", r"$ de sorte que", "The TeX adds a comma. The old also matches the current layer.")
add(332, "'mu(x) = 0  implique que'", "implique que", "implique", "missing", "high",
    r"implique" + NL + r"\[", r"implique que" + NL + r"\[", "The TeX drops 'que'.")
add(332, "paragraph number 8.6.", "8.6.", r"\subsection*{8.6}", "punctuation", "high",
    r"\subsection*{8.6}", r"\subsection*{8.6.}", "As the logged 3.3., 3.8. of pp. 291-295.")
add(332, "8.6, 'la structure multiplicative de'", "'structure multiplicative' underlined", "no underline", "underline", "high",
    r"la structure multiplicative de", r"la \emph{structure multiplicative} de")
add(332, "8.6, 'tout A_X-Module M'", "A_X-Module (capital M)", "$A_X$-module", "word", "high",
    r"$A_X$-module $M$", r"$A_X$-Module $M$", "The typescript's capital M (sheaf of modules), as the applied 'Module' of pp. 282-295.")
add(332, "8.6, 'deux A_X-Modules localement constants'", "A_X-Modules (capital M)", "$A_X$-modules", "word", "high",
    r"deux $A_X$-modules", r"deux $A_X$-Modules")
add(332, "end of display (8.6.2)", "no punctuation after the display", r"\bigr).", "punctuation", "high",
    r"x_1x_2\bigr).", r"x_1x_2\bigr)", "The TeX adds a full stop.")
add(332, "'clairement anticommutative'", "'anticommutative' underlined", "no underline", "underline", "high",
    r"clairement anticommutative,", r"clairement \emph{anticommutative},")
add(332, "'qu'elle est associative'", "'associative' underlined", "no underline", "underline", "high",
    r"est associative.", r"est \emph{associative}.")

# ---------------------------------------------------------------- page 333
add(333, "Proposition 8.6.3 a), first sentence",
    "Pour tout couple (M,N) de A_X-Modules localement constants constructibles au voisinage de Y , le diagramme (words underlined; (M,N), A_X and Y not)",
    "no underline; A_X-modules", "underline", "high",
    r"Pour tout couple $(M,N)$ de $A_X$-modules localement constants constructibles au voisinage de $Y$, le diagramme",
    r"\emph{Pour tout couple} $(M,N)$ \emph{de} $A_X$-\emph{Modules localement constants constructibles au voisinage de} $Y$, \emph{le diagramme}",
    "One edit: it also gives the print's capital M (word). The underline starts at the M, not at the hyphen.")
add(333, "Proposition 8.6.3 a), 'est commutatif. En particulier, l'application surjective'", "underlined", "no underline",
    "underline", "high",
    r"est commutatif. En particulier, l'application surjective",
    r"\emph{est commutatif. En particulier, l'application surjective}")
add(333, "Proposition 8.6.3 a), 'est un morphisme d'anneaux, et l'application'", "underlined", "no underline",
    "underline", "high",
    r"est un morphisme d'anneaux, et l'application", r"\emph{est un morphisme d'anneaux, et l'application}")
add(333, "Proposition 8.6.3 a), 'est un morphismes de modules sur anneaux variables.'", "underlined (the full stop not)",
    "no underline", "underline", "high",
    r"est un morphisme de modules sur anneaux variables.", r"\emph{est un morphisme de modules sur anneaux variables}.",
    "Apply before the next item (misprint 'morphismes').")
add(333, "Proposition 8.6.3 a), 'est un morphismes de modules'", "morphismes", "morphisme", "misprint_in_print", "high",
    r"un morphisme de modules", r"un morphismes de modules",
    "Typing error (plural after 'un'); the TeX silently corrects. The old also matches after the underline edit before it.",
    r"un morphisme de modules")
add(333, "Proposition 8.6.3 b), first sentence",
    "Si l'on fait opérer ... sur ... au moyen de l'application ('Si l'on fait opérer', 'sur', 'au moyen de l'application' underlined)",
    "no underline", "underline", "high",
    r"Si l'on fait opérer $\nabla^*(X',A)$ sur $H^*(Y,M(-d))(-2d)$ au moyen de l'application",
    r"\emph{Si l'on fait opérer} $\nabla^*(X',A)$ \emph{sur} $H^*(Y,M(-d))(-2d)$ \emph{au moyen de l'application}")
add(333, "Proposition 8.6.3 b), display, end of the first line", "...-> H^{p+q-2d}(Y,M(-d))  (no comma)", "(Y,M(-d)),",
    "punctuation", "high", r"(Y,M(-d))," + NL + r"\qquad", r"(Y,M(-d))" + NL + r"\qquad", "The TeX adds a comma.")
add(333, "Proposition 8.6.3 b), display, second line", "(y',x) (x) y |---> i*(x).y   ,", r"i^*(x)y,", "symbol", "high",
    r"i^*(x)y,", r"i^*(x)\cdot y,", "The TeX drops the product dot (the typewriter's full stop, written \\cdot by the volume's rule).")
add(333, "Proposition 8.6.3 b), last sentence",
    "'alors l'application', 'de', 'devient un morphisme de' and 'modules' underlined; lambda, 8.5 b), Nabla*(X',A) and the hyphen not",
    "no underline", "underline", "high",
    r"alors l'application $\lambda$ de 8.5 b) devient un morphisme de $\nabla^*(X',A)$-modules.",
    r"\emph{alors l'application} $\lambda$ \emph{de} 8.5 b) \emph{devient un morphisme de} $\nabla^*(X',A)$-\emph{modules}.")
add(333, "proof, 'Avec les notations de 8.6.2., il s'agit'", "8.6.2., (full stop and comma)", "8.6.2,", "punctuation", "high",
    r"de 8.6.2, il", r"de 8.6.2., il", "The TeX drops the full stop of the number.")
add(333, "proof, first display, last term", "f*(x,x_2)", r"f^*(x_1x_2)", "misprint_in_print", "high",
    r"+f^*(x_1x_2)", r"+f^*(x,x_2)",
    "The first x has no index and is followed by a comma (as the commas of the line); the second component of (8.6.2) is x_1x_2 and the right side gives f*(x_1)f*(x_2). The TeX silently corrects.",
    r"+f^*(x_1x_2)")

# ---------------------------------------------------------------- page 334
add(334, "braced display, first line", "f*(x_1)f*(x_2) = f*(x_1x_2)   (multiplicativité de f*)",
    r"f^*(x_1x_2),&\text{multiplicativité de }f^*,\\", "punctuation", "high",
    r"f^*(x_1x_2),&\text{multiplicativité de }f^*,\\", r"f^*(x_1x_2)&\text{(multiplicativité de }f^*\text{)}\\",
    "The TeX drops the parentheses of the gloss and adds two commas.")
add(334, "braced display, second line", "j_*(-y'_1y'_2 xi) = j_*(y')j_*(y')  (no indices on the right)",
    r"j_*(y_1')j_*(y_2')", "misprint_in_print", "high",
    r"=j_*(y_1')j_*(y_2')", r"=j_*(y')j_*(y')",
    "No index under either y' (the indices of the left side are clear); the TeX silently corrects.",
    r"=j_*(y_1')j_*(y_2')")
add(334, "braced display, second line, gloss", "(4.5)  (no commas)", r",&\text{(4.5)},\\", "punctuation", "high",
    r",&\text{(4.5)},\\", r"&\text{(4.5)}\\", "The TeX adds two commas.")
add(334, "braced display, third line", "... = j_*(y')f*(x) (formule de projection).",
    r"f^*(x),&\text{formule de projection}.", "punctuation", "high",
    r"f^*(x),&\text{formule de projection}.", r"f^*(x)&\text{(formule de projection)}.",
    "The TeX drops the parentheses of the gloss and adds a comma.")
add(334, "display lambda(i*(x).y) = (y',x).lambda(y)", "no punctuation after the display", r"\cdot\lambda(y),",
    "punctuation", "high", r"\cdot\lambda(y),", r"\cdot\lambda(y)", "The TeX adds a comma.")
add(334, "'se décompose en les deux suivantes.'", "suivantes.", "suivantes:", "punctuation", "high",
    r"deux suivantes:", r"deux suivantes.")
add(334, "display g*(i*(x).y)c_{d-1}(F-check) = ...", "the two lines of the right side stand in a left brace",
    "no brace", "formula", "medium",
    r"=" + NL + r"-y'g^*(y)c_{d-1}(\check F)\xi" + NL + r"+y'g^*i^*(-i_*(y))" + NL + r"+g^*(i^*x)g^*(y)c_{d-1}(\check F)",
    r"=" + NL + r"\begin{cases}" + NL + r"-y'g^*(y)c_{d-1}(\check F)\xi+y'g^*i^*(-i_*(y))\\" + NL
    + r"+g^*(i^*x)g^*(y)c_{d-1}(\check F)" + NL + r"\end{cases}",
    "The print's brace (as the braced display above, which the TeX gives with cases). Independent of the next item.")
add(334, "end of the same display", "no punctuation after the display", r"c_{d-1}(\check F),", "punctuation", "high",
    r"," + NL + r"\]" + NL + r"et" + NL + r"\[" + NL + r"-i_*", NL + r"\]" + NL + r"et" + NL + r"\[" + NL + r"-i_*",
    "The TeX adds a comma.")
add(334, "'La seconde n'est autre que la formule de projection'", "new paragraph (the line is indented)",
    "runs on after the display", "other", "medium",
    r"\]" + NL + r"La seconde", r"\]" + NL + NL + r"La seconde", "Paragraph break of the print left out.")
add(334, "the two relations after 'découle immédiatement des relations'",
    "one display: a left brace over -xi c_{d-1}(F-check) = g*[c_d(N-check)] (suite exacte de 8.4.3) and i*i_*(y) = y c_d(N-check) (4.1); no 'et', no final stop",
    "two displays joined by 'et'; '(4.1).'", "extra", "high",
    r"\[" + NL + r"-\xi\,c_{d-1}(\check F)=g^*[c_d(\check N)]" + NL + r"\quad\text{(suite exacte de 8.4.3)}" + NL + r"\]" + NL
    + r"et" + NL + r"\[" + NL + r"i^*i_*(y)=y\,c_d(\check N)\qquad\text{(4.1)}." + NL + r"\]",
    r"\[" + NL + r"\begin{cases}" + NL + r"-\xi\,c_{d-1}(\check F)=g^*[c_d(\check N)]&\text{(suite exacte de 8.4.3)}\\" + NL
    + r"i^*i_*(y)=y\,c_d(\check N)&\text{(4.1)}" + NL + r"\end{cases}" + NL + r"\]",
    "The TeX adds the word 'et', drops the brace and adds a full stop after (4.1).")

# ---------------------------------------------------------------- page 335
add(335, "title of section 9", "9. ANNEAU DE CHOW D'UNE VARIETE ECLATEE ET FORMULE DE SELF-INTERSECTION DANS L'ANNEAU DE CHOW.",
    "9. Anneau de Chow d'une variété éclatée et formule de self-intersection dans l'anneau de Chow", "word", "high",
    r"9. Anneau de Chow d'une variété éclatée et formule de self-intersection dans l'anneau de Chow",
    r"9. ANNEAU DE CHOW D'UNE VARIÉTÉ ÉCLATÉE ET FORMULE DE SELF-INTERSECTION DANS L'ANNEAU DE CHOW",
    "Capitals as printed, as the applied titles 1.-3. (FIBRES VECTORIELS, SCHÉMAS PROJECTIFS, CLASSES DE CHERN); accented capitals as the volume's rule. Independent of the next item.")
add(335, "title of section 9, end", "full stop after CHOW", "no full stop", "punctuation", "high",
    r"}" + NL + NL + r"On se propose", r".}" + NL + NL + r"On se propose", "Underlined title: the TeX drops the print's final full stop.")
add(335, "'la démonstration, dûe à MUMFORD'", "dûe", "due", "misprint_in_print", "high",
    r"démonstration, due", r"démonstration, dûe", "Spelling error of the typescript (circumflex clear); the TeX silently corrects.",
    r"démonstration, due")
add(335, "'dûe à MUMFORD'", "MUMFORD", "Mumford", "word", "high", r"Mumford", r"MUMFORD",
    "The name in capitals, as the restored LERAY (pp. 275-276) and SERRE (p. 259).")
add(335, "'la \"formule-clef\" (8.4.3)'", "straight typewriter double quotes", "«formule-clef»", "punctuation", "high",
    r"«formule-clef»", r"``formule-clef''", "The TeX adds guillemets; the file writes the typescript's quotes as ``...''.")
add(335, "'On se servira plusieurs fois du lemme suivant.'", "a paragraph of its own (indented, after a blank line)",
    "runs on after 'celle de [1].'", "other", "high",
    r"celle de [1]. On se servira", r"celle de [1]." + NL + NL + r"On se servira", "Paragraph break of the print left out.")
add(335, "Lemme 9.1, first two sentences",
    "underlined: 'Soient', 'un schéma quasi-projectif et lisse sur un corps séparablement clos', 'un', 'Module localement libre de rang constant', 'et', 'le fibré projectif associé. On désigne par', 'le', 'Module défini par la suite exacte canonique'; O_S-Module, O_p-Module",
    "no underline; -module twice", "underline", "high",
    r"Soient $S$ un schéma quasi-projectif et lisse sur un corps séparablement clos $k$, $E$ un $\mathcal O_S$-module localement libre de rang constant $r+1$, et $p:P=\mathbb P_S(E)\to S$ le fibré projectif associé. On désigne par $F$ le $\mathcal O_P$-module défini par la suite exacte canonique",
    r"\emph{Soient} $S$ \emph{un schéma quasi-projectif et lisse sur un corps séparablement clos} $k$, $E$ \emph{un} $\mathcal O_S$-\emph{Module localement libre de rang constant} $r+1$, \emph{et} $p:P=\mathbb P_S(E)\to S$ \emph{le fibré projectif associé. On désigne par} $F$ \emph{le} $\mathcal O_P$-\emph{Module défini par la suite exacte canonique}",
    "One edit: it also gives the print's capital M twice (word). Apply before the next item (O_p).")
add(335, "Lemme 9.1, 'le O_p-Module défini par la suite exacte canonique'", "O_p (small p)", r"\mathcal O_P",
    "misprint_in_print", "medium", r"$\mathcal O_P$-", r"$\mathcal O_p$-",
    "The subscript is a small p: its bowl takes 14 of the letter's 21 pixel rows and its top sits 5 px below the foot of the O; the capital P of 'P = P_S(E)' on this page has its bowl in 12 of 21 rows. As the O_p items of pp. 286-295 (global issue 89(h): all or none). The TeX silently corrects. The old also matches after the underline edit before it.",
    r"$\mathcal O_P$-")
add(335, "display (9.1.0)", "0 -> F -> p*(E) -> O_p(1) -> 0,  (small p)", r"\mathcal O_P(1)", "misprint_in_print", "medium",
    r"\to\mathcal O_P(1)\to0,", r"\to\mathcal O_p(1)\to0,",
    "Small p as measured: bowl 15 of 22 rows, top 5 px below the foot of the O. The TeX silently corrects.",
    r"\to\mathcal O_P(1)\to0,")
add(335, "Lemme 9.1, 'et on pose xi = c_1(O_p(1)). Alors :'", "'et on pose' and 'Alors' underlined", "no underline",
    "underline", "high",
    r"et on pose $\xi=c_1(\mathcal O_P(1))$. Alors:", r"\emph{et on pose} $\xi=c_1(\mathcal O_P(1))$. \emph{Alors} :",
    "Apply before the next item (O_p).")
add(335, "Lemme 9.1, xi = c_1(O_p(1))", "O_p (small p)", r"\mathcal O_P", "misprint_in_print", "medium",
    r"c_1(\mathcal O_P(1))", r"c_1(\mathcal O_p(1))",
    "Small p as measured: bowl 15 of 22 rows, top 5 px below the foot of the O. The TeX silently corrects. The old also matches after the underline edit before it.",
    r"c_1(\mathcal O_P(1))")
add(335, "Lemme 9.1 (i), 'Pour tout'", "(i) Pour tout (capital P, underlined)", "pour tout", "word", "high",
    r"(\roman*)]" + NL + r"\item pour tout", r"(\roman*)]" + NL + r"\item \emph{Pour tout}",
    "One edit: capital P and underline.")
add(335, "Lemme 9.1 (i), 'on a'", "'on a' underlined", "no underline", "underline", "high",
    r"$, on a" + NL + r"\[" + NL + r"y=p_*", r"$, \emph{on a}" + NL + r"\[" + NL + r"y=p_*")
add(335, "end of display (9.1.1)", "y = p_*(p*(y)c_r(F-check)).", r"\bigr);", "punctuation", "high",
    r"c_r(\check F)\bigr);", r"c_r(\check F)\bigr).", "Full stop of the print; the TeX has a semicolon.")
add(335, "Lemme 9.1 (ii), first sentence",
    "(ii) Supposons que ... et notons (capital S; underlined: 'Supposons que', 'avec', 'un', 'Module localement libre de rang', 'de sorte que', 's'identifie à la complétion projective', 'de', 'et notons')",
    "supposons; no underline; -module", "word", "high",
    r"\item supposons que $E=N\oplus\mathcal O_S$, avec $N$ un $\mathcal O_S$-module localement libre de rang $r$, de sorte que $P$ s'identifie à la complétion projective $\widehat N$ de $V(N)$, et notons",
    r"\item \emph{Supposons que} $E=N\oplus\mathcal O_S$, \emph{avec} $N$ \emph{un} $\mathcal O_S$-\emph{Module localement libre de rang} $r$, \emph{de sorte que} $P$ \emph{s'identifie à la complétion projective} $\widehat N$ \emph{de} $V(N)$, \emph{et notons}",
    "One edit: capital S, the underlines and the capital M of Module.")
add(335, "Lemme 9.1 (ii), after the display s : S -> P_S(E)",
    "'la section composée de la section nulle de', 'et de l'inclusion canonique' and 'Alors' underlined", "no underline",
    "underline", "high",
    r"la section composée de la section nulle de $V(N)$ et de l'inclusion canonique $V(N)\hookrightarrow\widehat N$. Alors:",
    r"\emph{la section composée de la section nulle de} $V(N)$ \emph{et de l'inclusion canonique} $V(N)\hookrightarrow\widehat N$. \emph{Alors} :")
add(335, "Lemme 9.1 (ii)(a), 'Pour tout'", "(a) Pour tout (capital P, underlined)", "pour tout", "word", "high",
    r"(\alph*)]" + NL + r"\item pour tout", r"(\alph*)]" + NL + r"\item \emph{Pour tout}",
    "One edit: capital P and underline.")
add(335, "Lemme 9.1 (ii)(a), 'on a les relations :'", "'on a les relations' underlined, followed by ' :'",
    "no underline, no colon", "missing", "high",
    r"$, on a les relations", r"$, \emph{on a les relations} :", "The TeX drops the colon; one edit with the underline.")
add(335, "display (9.1.2), before 'dans'", "..., dans C°(N^).  (comma before 'dans'; 'dans' underlined)",
    r"\quad\text{dans }", "punctuation", "high",
    r"\right)" + NL + r"\quad\text{dans }", r"\right)," + NL + r"\quad\text{\emph{dans} }",
    "The TeX drops the comma; one edit with the underline of 'dans'.")
add(335, "end of display (9.1.2)", "full stop", "comma", "punctuation", "high",
    r"(\widehat N)," + NL + r"\tag{9.1.2}", r"(\widehat N)." + NL + r"\tag{9.1.2}")
add(335, "display (9.1.3), before 'dans'", "y c_r(N-check) , dans C°(S).  (comma; 'dans' underlined)", r"\quad\text{dans }",
    "punctuation", "high",
    r"c_r(\check N)\quad\text{dans }", r"c_r(\check N),\quad\text{\emph{dans} }",
    "The TeX drops the comma; one edit with the underline of 'dans'.")
add(335, "end of display (9.1.3)", "full stop", "semicolon", "punctuation", "high",
    r"(S);" + NL + r"\tag{9.1.3}", r"(S)." + NL + r"\tag{9.1.3}")
add(335, "end of the page / folio-336 marker", "p. 335 ends with (9.1.3) and a blank lower part; (b) is printed on p. 336",
    "the \\item of (b) is the last line of page_335.tex, before the folio-336 marker", "marker", "high", None, None,
    "Page 336 really begins at the '\\item' that sets the label (b) (the last line of page_335.tex). Exact fix: python -I move_marker.py 5 336 '\\item' --before (simulated in memory on both layers: the marker then stands between the '\\]' that closes (9.1.3) and '\\item'; diplomatic s5.tex line 11419, current 11415 at the time of the check). No edit of this batch touches that line.")

# ---------------------------------------------------------------- checks
ok = True
for page in (331, 332, 333, 334, 335):
    t0 = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    assert "\r" not in t0
    t = t0
    for d in F:
        if d["page"] != page or d["fix"] is None:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        n0 = t0.count(old)
        n1 = t.count(old)
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
            print("MARKER LINE IN EDIT", page, d["where"])
            ok = False
        if n0 != 1 or n1 != 1:
            print("COUNT PROBLEM page", page, "orig", n0, "in sequence", n1, "|", d["where"], "|", repr(old))
            ok = False
        else:
            t = t.replace(old, new, 1)
    # the marker line must be unchanged
    if t0.splitlines()[1] != t.splitlines()[1]:
        print("marker line changed on", page)
        ok = False

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", {k: "%d/%d" % tuple(v) for k, v in sorted(counts.items())})
print("total", len(F), "all olds unique:", ok)
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
