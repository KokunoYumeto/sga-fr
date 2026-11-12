"""Build findings_296_300.json and check that every fix's old occurs exactly once in its page file."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b296_300\page_%d.tex"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_296_300.json"
N = "\n"

OC_NOTE = ("The subscript is a small c (x-height 15-17 px like the typed small letters; the typed capitals measure "
           "21-22 px, the double-struck C of X(C) 24-25 px): O_c is 'le faisceau des fonctions continues à valeurs "
           "complexes sur X(C)' (p. 295), c for continu, not the field C. The TeX writes \\mathcal O_\\mathbb C, a "
           "wrong letter, in all eight places of pp. 296-297 (each itemized) and in the two of p. 295.")


def f(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


F = []

# ---------------- page 296 ----------------
F.append(f(296, "display (3.8.1)",
           "'c_i(ℰ) ∈ H ^i(X(C), Z/ν Z).': superscript i only, with one blank character slot between H and i "
           "(no trace of a 2 at any threshold)",
           r"c_i(\mathcal E)\in H^i(X(\mathbb C),\mathbb Z/\nu\mathbb Z).",
           "misprint_in_print", "medium", None, None,
           "c_i lies in H^{2i} (the integral classes of p. 295, the statement of 3.8.5). The TeX keeps the printed "
           "reading; the current layer already reads H^{2i}.",
           corrected=r"H^{2i}(X(\mathbb C),\mathbb Z/\nu\mathbb Z)"))
F.append(f(296, "3.8, 'de son faisceau structural O_a en X(C) de l'Anneau O_c'",
           "'en X(C)': the typescript has en where et is meant",
           r"$\mathcal O_a$ et $X(\mathbb C)$",
           "misprint_in_print", "high",
           r"$\mathcal O_a$ et $X", r"$\mathcal O_a$ en $X",
           "Typing error (munir X_ét de O_a et X(C) de l'Anneau O_c); the TeX silently corrects it.",
           corrected=r"$\mathcal O_a$ et $X"))
F.append(f(296, "3.8, 'de l'Anneau O_c'",
           "Anneau with a capital A (sheaf of rings)",
           "l'anneau", "word", "high",
           "l'anneau", "l'Anneau",
           "As the print's Module and Idéal (sheaves)."))
F.append(f(296, "3.8, 'de l'Anneau O_c , on a'",
           "O_c: hand-drawn script O with a small c",
           r"$\mathcal O_\mathbb C$", "symbol", "high",
           r"$\mathcal O_\mathbb C$, on a", r"$\mathcal O_c$, on a",
           OC_NOTE))
F.append(f(296, "'le morphisme d'Anneaux structural'",
           "Anneaux with a capital A",
           "d'anneaux structural", "word", "high",
           "d'anneaux structural", "d'Anneaux structural"))
F.append(f(296, "display (3.8.2), source ε•(O_a)",
           "ε followed by a small raised ring (8 x 9 px, hollow centre): the typewriter's raised dot of A•(S) "
           "(pp. 290-295) and C•(X), A•(X) (p. 298), not the star (17 x 16 px) of (3.8.3) and (3.8.6)",
           r"\varepsilon^*(\mathcal O_a)",
           "misprint_in_print", "medium",
           r"\varepsilon^*(\mathcal O_a)", r"\varepsilon^{\bullet}(\mathcal O_a)",
           "The inverse image is ε* everywhere else on pp. 296-297 ((3.8.3), 3.8.5, (3.8.6), (3.8.7)); the raised "
           "dot is a typing slip and the TeX silently corrects it. Drop this item if the dot is read as intended.",
           corrected=r"\varepsilon^*(\mathcal O_a)"))
F.append(f(296, "display (3.8.2), target O_c",
           "O_c: hand-drawn script O with a small c",
           r"\to\mathcal O_\mathbb C", "symbol", "high",
           r"\to\mathcal O_\mathbb C" + N + r"\tag{3.8.2}", r"\to\mathcal O_c" + N + r"\tag{3.8.2}",
           "As the first O_c of the page."))
F.append(f(296, "'provenant de ce que \"toute fonction algébrique est continue\".'",
           "the clause in straight typewriter quotation marks, the full stop after the closing quote",
           "ce que toute fonction algébrique est continue.", "punctuation", "high",
           "ce que toute fonction algébrique est continue.",
           "ce que ``toute fonction algébrique est continue''.",
           "The TeX drops the quotation marks."))
F.append(f(296, "'la lettre μ désignant dans chacun des deux contextes le faisceau'",
           "no commas",
           "désignant, dans chacun des deux contextes, le", "punctuation", "high",
           "désignant, dans chacun des deux contextes, le",
           "désignant dans chacun des deux contextes le",
           "The TeX adds two commas."))
F.append(f(296, "'le faisceau des racines ν^èmes de l'unité'",
           "'èmes' raised as a superscript after ν, no hyphen",
           r"$\nu$-èmes", "other", "high",
           r"$\nu$-èmes", r"$\nu$\textsuperscript{èmes}",
           r"Written with \textsuperscript, as the file's '\(n\)\textsuperscript{ème} composant'."))
F.append(f(296, "after (3.8.4), 'envoyant la section 1 sur la section \"e^(2iπ/ν)\" .'",
           "the exponential in straight quotation marks; the exponent a built-up fraction, 2iπ over ν",
           r"$e^{2i\pi/\nu}$.", "punctuation", "high",
           r"la section $e^{2i\pi/\nu}$.", r"la section ``$e^{\frac{2i\pi}{\nu}}$''.",
           "The TeX drops the quotation marks. One edit: it also gives the print's built-up fraction in the "
           "exponent (formula)."))
F.append(f(296, "Proposition 3.8.5, first sentence",
           "underlined: 'Soit' | 'un' | 'Module localement libre. Notant pour tout entier' (E, O_X- and i ≥ 0 "
           "not); Module with a capital M; no comma after 'Notant' or after 'i ≥ 0'",
           r"Soit $E$ un $\mathcal O_X$-module localement libre. Notant, pour tout entier $i\ge0$, (no underline "
           "markup)", "underline", "high",
           r"Soit $E$ un $\mathcal O_X$-module localement libre. Notant, pour tout entier $i\ge0$,",
           r"\emph{Soit} $E$ \emph{un} $\mathcal O_X$-\emph{Module localement libre. Notant pour tout entier} "
           r"$i\ge0$",
           "One edit: it also gives the capital M (word) and drops the two commas the TeX adds (punctuation). "
           "Exposé VII: the TeX has no underline markup for statements; \\emph as in the applied statements of "
           "pp. 283-295."))
F.append(f(296, "Proposition 3.8.5, after the display",
           "underlined: 'le morphisme image réciproque déduit de' | 'et' | 'on a l'égalité' (3.8.3 and '3.8.4,' "
           "not)",
           "le morphisme image réciproque déduit de 3.8.3 et 3.8.4, on a l'égalité (no underline markup)",
           "underline", "high",
           "le morphisme image réciproque déduit de 3.8.3 et 3.8.4, on a l'égalité",
           r"\emph{le morphisme image réciproque déduit de} 3.8.3 \emph{et} 3.8.4, \emph{on a l'égalité}"))
F.append(f(296, "display (3.8.6), target H^1(X(C), O_c^*)",
           "O_c^*: hand-drawn script O with a small c",
           r"\mathcal O_\mathbb C^*", "symbol", "high",
           r"\mathcal O_\mathbb C^*)," + N + r"\tag{3.8.6}", r"\mathcal O_c^*)," + N + r"\tag{3.8.6}",
           "As the first O_c of the page."))
F.append(f(296, "diagram (3.8.7), top right H^1(X(C), O_c^*)",
           "O_c^*: hand-drawn script O with a small c",
           r"\mathcal O_\mathbb C^*", "symbol", "high",
           r"\mathcal O_\mathbb C^*) \arrow[d", r"\mathcal O_c^*) \arrow[d",
           "Printed on p. 297; filed under p. 296, where the diagram stands until the marker move of p. 297. "
           "As the first O_c of p. 296."))
F.append(f(296, "diagram (3.8.7), bottom arrow H^2(X, μ_X) → H^2(X(C), Z/νZ)",
           "label ε* above the arrow, as on the top arrow",
           r'''\arrow[r,"\varepsilon^*"'] (label below)''', "other", "medium",
           r"""\arrow[r,"\varepsilon^*"']""", r"""\arrow[r,"\varepsilon^*"]""",
           "Printed on p. 297; filed under p. 296 until the marker move. Label position as in the print (as the "
           "logged label fixes of pp. 265, 277-278)."))
F.append(f(296, "end of the diagram (3.8.7)",
           "a comma after the diagram, at the right of the bottom row",
           r"\end{tikzcd} (no punctuation)", "punctuation", "high",
           r"\end{tikzcd}" + N + r"\tag{3.8.7}", r"\end{tikzcd}," + N + r"\tag{3.8.7}",
           "Printed on p. 297; filed under p. 296 until the marker move. The TeX leaves out the comma."))

# ---------------- page 297 ----------------
F.append(f(297, "top of the page / folio-297 marker",
           "p. 297 begins with 'et il s'agit de voir que le diagramme' and the diagram (3.8.7); p. 296 ends with "
           "the display (3.8.6) (rest of the page blank)",
           "'et il s'agit de voir que le diagramme' and the tikzcd diagram with \\tag{3.8.7} stand at the end of "
           "page_296.tex; the folio-297 marker stands before 'dans lequel'",
           "marker", "high", None, None,
           "Page 297 really begins at the line 'et il s'agit de voir que le diagramme' (right after the \\] that "
           "closes (3.8.6)). Exact fix (bash): python -I move_marker.py 5 297 \"et il s'agit de voir\" --before "
           "(simulated in memory on both layers: the anchor is the last occurrence before the marker; the marker "
           "then stands on its own line between '\\]' and 'et il s'agit de voir que le diagramme'). Text not "
           "moved; the three fixes of the moved diagram are filed under p. 296."))
F.append(f(297, "'en utilisant que le morphisme \"première classe de Chern\"'",
           "straight typewriter quotation marks",
           "« première classe de Chern »", "punctuation", "high",
           "« première classe de Chern »", "``première classe de Chern''",
           "The TeX writes guillemets for the print's straight quotes (``...'' as elsewhere in the file)."))
F.append(f(297, "display H^1(X(C), O_c^*) → H^2(X, Z)",
           "O_c^*: hand-drawn script O with a small c",
           r"\mathcal O_\mathbb C^*", "symbol", "high",
           r"\mathcal O_\mathbb C^*)\to H^2(X,\mathbb Z)", r"\mathcal O_c^*)\to H^2(X,\mathbb Z)",
           "As p. 296 (O_c, the sheaf of continuous functions of p. 295)."))
F.append(f(297, "display 0 → Z → O_c --exp--> O_c^* → 0",
           "O_c and O_c^*: small c, twice",
           r"\mathcal O_\mathbb C\xrightarrow{\exp}\mathcal O_\mathbb C^*", "symbol", "high",
           r"\mathcal O_\mathbb C\xrightarrow{\exp}\mathcal O_\mathbb C^*",
           r"\mathcal O_c\xrightarrow{\exp}\mathcal O_c^*",
           "As p. 296."))
F.append(f(297, "display 0 → Z → O_c → O_c^* → 0 , with t ↦ 2iπ t below",
           "the comma stands after the sequence only; none after 't ↦ 2iπ t' (set under the sequence)",
           r"t\mapsto 2i\pi t,", "punctuation", "high",
           r"t\mapsto 2i\pi t,", r"t\mapsto 2i\pi t",
           "The TeX adds a comma after the map."))
F.append(f(297, "display 0 → Z/νZ → O_c^* --ν--> O_c^* → 0",
           "O_c^*: small c, twice",
           r"\mathcal O_\mathbb C^*\xrightarrow{\nu}\mathcal O_\mathbb C^*", "symbol", "high",
           r"\mathcal O_\mathbb C^*\xrightarrow{\nu}\mathcal O_\mathbb C^*",
           r"\mathcal O_c^*\xrightarrow{\nu}\mathcal O_c^*",
           "As p. 296."))
F.append(f(297, "the map t ↦ e^(2iπt/ν) under the second sequence",
           "no comma after the map (the comma stands after the sequence)",
           r"t\mapsto e^{2i\pi t/\nu},", "punctuation", "high",
           "}," + N + r"\]" + N + "qui, compte tenu", "}" + N + r"\]" + N + "qui, compte tenu",
           "The TeX adds a comma after the map. Independent of the fraction item (the olds do not overlap)."))
F.append(f(297, "the map t ↦ e^(2iπt/ν) under the second sequence",
           "the exponent a built-up fraction, 2iπt over ν",
           r"e^{2i\pi t/\nu}", "formula", "medium",
           r"2i\pi t/\nu", r"\frac{2i\pi t}{\nu}",
           "As e^(2iπ/ν) after (3.8.4) (p. 296)."))
F.append(f(297, "3.9, 'E un O_X-Module localement libre'",
           "Module with a capital M",
           r"$\mathcal O_X$-module", "word", "high",
           r"$\mathcal O_X$-module", r"$\mathcal O_X$-Module"))
F.append(f(297, "3.9, 'permet de définir pour tout nombre premier ℓ'",
           "no comma after 'définir'",
           "permet de définir, pour tout", "punctuation", "high",
           "permet de définir, pour tout", "permet de définir pour tout",
           "The TeX adds a comma."))
F.append(f(297, "3.9, 'des classes de Chern ℓ-adiques'",
           "underlined: 'classes de Chern' | 'adiques' (ℓ not): the defined term",
           r"des classes de Chern $\ell$-adiques (no underline markup)", "underline", "high",
           r"des classes de Chern $\ell$-adiques",
           r"des \emph{classes de Chern} $\ell$-\emph{adiques}"))
F.append(f(297, "3.9, display, the sign of definition",
           "'déf' (with the accent) over the long equals sign",
           r"\stackrel{\mathrm{def}}{=}", "accent", "high",
           r"\stackrel{\mathrm{def}}{=}", r"\stackrel{\mathrm{d\acute{e}f}}{=}",
           r"é written as in the file's \et (\mathrm{\acute{e}t})."))

# ---------------- page 298 ----------------
F.append(f(298, "first sentence, 'et qui dans le contexte de 3.8 sont manifestement compatibles'",
           "no commas",
           "et qui, dans le contexte de 3.8, sont", "punctuation", "high",
           "et qui, dans le contexte de 3.8, sont", "et qui dans le contexte de 3.8 sont",
           "The TeX adds two commas."))
F.append(f(298, "first sentence, 'compatibles (dans un sens évident) avec'",
           "the phrase in parentheses",
           "compatibles, dans un sens évident, avec", "punctuation", "high",
           "compatibles, dans un sens évident, avec", "compatibles (dans un sens évident) avec",
           "The TeX turns the parentheses into commas."))
F.append(f(298, "end of the display c_i(E) ∈ H^{2i}(X, Q_ℓ(i)) = H^{2i}(X, Z_ℓ(i)) ⊗_{Z_ℓ} Q_ℓ",
           "no punctuation after Q_ℓ",
           r"\otimes_{\mathbb Z_\ell}\mathbb Q_\ell,", "punctuation", "high",
           r"\otimes_{\mathbb Z_\ell}\mathbb Q_\ell,", r"\otimes_{\mathbb Z_\ell}\mathbb Q_\ell",
           "The TeX adds a comma at the end of the display."))
F.append(f(298, "'lisse sur un corps k et notons ici C•(X)'",
           "no comma after k",
           "corps $k$, et notons", "punctuation", "high",
           "corps $k$, et notons", "corps $k$ et notons",
           "The TeX adds a comma."))
F.append(f(298, "'et notons ici C•(X) son anneau de Chow'",
           "C with the typewriter's raised dot (C•), as A•",
           "$C^*(X)$", "symbol", "high",
           "notons ici $C^*(X)$", r"notons ici $C^{\bullet}(X)$",
           "The TeX has a star (as the A• items of pp. 290-295)."))
F.append(f(298, "display φ_X : C•(X) → A•(X)",
           "C• and A• with raised dots",
           r"C^*(X)\to A^*(X)", "symbol", "high",
           r"C^*(X)\to A^*(X)", r"C^{\bullet}(X)\to A^{\bullet}(X)",
           "The TeX has stars."))
F.append(f(298, "'associant à tout O_X-Module inversible L'",
           "Module with a capital M",
           r"$\mathcal O_X$-module inversible", "word", "high",
           r"$\mathcal O_X$-module inversible", r"$\mathcal O_X$-Module inversible"))
F.append(f(298, "'sur le modèle de l'article précité de GROTHENDIECK'",
           "the name in capitals",
           "de Grothendieck", "word", "high",
           "de Grothendieck", "de GROTHENDIECK",
           "As the logged GYSIN (p. 285) and the bylines."))
F.append(f(298, "'(où k était supposé algébriquement clos), à une théorie'",
           "the clause in parentheses, the comma after the closing parenthesis",
           ", où $k$ était supposé algébriquement clos, à", "punctuation", "high",
           ", où $k$ était supposé algébriquement clos, à", " (où $k$ était supposé algébriquement clos), à",
           "The TeX turns the parentheses into commas. Independent of the GROTHENDIECK item."))
F.append(f(298, "'à valeurs dans C•(X).'",
           "C with the raised dot (C•)",
           "$C^*(X)$", "symbol", "high",
           "valeurs dans $C^*(X)$", r"valeurs dans $C^{\bullet}(X)$",
           "The TeX has a star."))
F.append(f(298, "'avec J un Idéal inversible de O_X'",
           "Idéal with a capital I",
           "un idéal inversible", "word", "high",
           "un idéal inversible", "un Idéal inversible"))
F.append(f(298, "last sentence, 'le morphisme φ_X transforme classes de Chern en classes de Chern.'",
           "underlined: 'le morphisme' | 'transforme classes de Chern en' / 'classes de Chern' (φ_X and the full "
           "stop not)",
           r"le morphisme $\varphi_X$ transforme classes de Chern en classes de Chern. (no underline markup)",
           "underline", "high",
           r"le morphisme $\varphi_X$ transforme classes de Chern en classes de Chern.",
           r"\emph{le morphisme} $\varphi_X$ \emph{transforme classes de Chern en classes de Chern}."))

# ---------------- page 299 ----------------
F.append(f(299, "section title 4",
           "'4. FORMULE DE SELF-INTERSECTION ET APPLICATIONS': hand-drawn capitals, underlined, no full stop",
           r"\section*{4. Formule de self-intersection et applications}", "word", "high",
           r"\section*{4. Formule de self-intersection et applications}",
           r"\section*{4. FORMULE DE SELF-INTERSECTION ET APPLICATIONS}",
           "Capitals as printed, as the logged titles 1-3 of the exposé (pp. 282, 285, 290)."))
F.append(f(299, "'J l'Idéal de O_X définissant Y'",
           "Idéal with a capital I",
           "l'idéal de", "word", "high",
           "l'idéal de", "l'Idéal de"))
F.append(f(299, "'qu'on dispose dans ce cas d'isomorphismes de Gysin'",
           "'isomorphismes' underlined (d' not)",
           "d'isomorphismes de Gysin", "underline", "high",
           "d'isomorphismes de Gysin", r"d'\emph{isomorphismes} de Gysin"))
F.append(f(299, "Théorème 4.1, 'Dans la situation précédente, notant'",
           "underlined (the comma inside the underline)",
           "Dans la situation précédente, notant (no underline markup)", "underline", "high",
           "Dans la situation précédente, notant", r"\emph{Dans la situation précédente, notant}"))
F.append(f(299, "Théorème 4.1, 'le faisceau normal de i , on a pour tout'",
           "underlined: 'le faisceau normal de' | 'on a pour tout' (i and the comma not)",
           r"le faisceau normal de $i$, on a pour tout (no underline markup)", "underline", "high",
           r"le faisceau normal de $i$, on a pour tout",
           r"\emph{le faisceau normal de} $i$, \emph{on a pour tout}",
           "List before the low-confidence 'conormal' item (whose old lies inside this one)."))
F.append(f(299, "Théorème 4.1, 'y ∈ A•(Y)'",
           "A with the raised dot (A•)",
           "A^*(Y)", "symbol", "high",
           "A^*(Y)", r"A^{\bullet}(Y)",
           "The TeX has a star (as pp. 290-295)."))
F.append(f(299, "Théorème 4.1, 'l'égalité'",
           "underlined",
           "l'égalité (no underline markup)", "underline", "high",
           "l'égalité", r"\emph{l'égalité}"))
F.append(f(299, "Théorème 4.1, 'le faisceau normal de i'",
           "a thin handwritten 'co' above the line, with a slanted stroke down to the space between 'faisceau' "
           "and 'normal' and a dotted vertical tick before it: 'faisceau conormal'",
           "le faisceau normal de $i$", "missing", "low",
           "faisceau normal", "faisceau conormal",
           "N = J/J^2 is the conormal sheaf (the formula uses its dual Ň), so the insertion fits the sense. Low: "
           "the strokes are thinner and lighter than the print's hand-drawn symbols, and the same words in "
           "Théorème 9.2 (p. 337) carry no mark, so it may be a reader's annotation in the scanned copy rather "
           "than part of the print; apply only if judged part of the print. Apply after the underline item of "
           "the same line."))
F.append(f(299, "b), 'Si par exemple T est un fermé de Y'",
           "no commas",
           "Si, par exemple, $T$", "punctuation", "high",
           "Si, par exemple, $T$", "Si par exemple $T$",
           "The TeX adds two commas."))
F.append(f(299, "b), 'Bien entendu i_* désigne alors'",
           "no comma after 'Bien entendu'",
           "Bien entendu, $i_*$", "punctuation", "high",
           "Bien entendu, $i_*$", "Bien entendu $i_*$",
           "The TeX adds a comma."))
F.append(f(299, "end of the last display H_T^{2p}(Y, μ_Y^{⊗p}) → H_T^{2p+2d}(X, μ_X^{⊗(p+d)})",
           "no punctuation (p. 300 goes on 'qui est encore un isomorphisme')",
           r"\to H_T^{2p+2d}(X,\mu_X^{\otimes(p+d)}),", "punctuation", "high",
           r"\to H_T^{2p+2d}(X,\mu_X^{\otimes(p+d)}),", r"\to H_T^{2p+2d}(X,\mu_X^{\otimes(p+d)})",
           "The TeX adds a comma at the end of the display."))

# ---------------- page 300 ----------------
F.append(f(300, "cartesian square, bottom arrow Y → X",
           "label i above the arrow, as j above the top arrow",
           r"""Y \arrow[r,"i"'] (label below)""", "other", "medium",
           r"""Y \arrow[r,"i"']""", r"""Y \arrow[r,"i"]""",
           "Label position as in the print (as the logged label fixes of pp. 265, 277-278)."))
F.append(f(300, "'On rappelle (cf. SGA 6 VII,3.1, dont on adopte les notations)'",
           "a comma between VII and 3.1",
           "SGA 6 VII 3.1,", "punctuation", "high",
           "SGA 6 VII 3.1,", "SGA 6 VII,3.1,",
           "The TeX drops the comma ('(SGA 6 VII 1.8)' in the proof has none, as the TeX)."))
F.append(f(300, "'définie par un Idéal'",
           "Idéal with a capital I",
           "par un idéal", "word", "high",
           "par un idéal", "par un Idéal"))
F.append(f(300, "'une suite exacte de O_Y'-Modules'",
           "Modules with a capital M",
           r"$\mathcal O_{Y'}$-modules", "word", "high",
           r"$\mathcal O_{Y'}$-modules", r"$\mathcal O_{Y'}$-Modules"))
F.append(f(300, "Lemme 4.2, first line",
           "underlined: 'Pour tout' | 'Module' | 'les homomorphismes' (A_X-, M and the comma not); Module with a "
           "capital M",
           r"Pour tout $A_X$-module $M$, les homomorphismes (no underline markup)", "underline", "high",
           r"Pour tout $A_X$-module $M$, les homomorphismes",
           r"\emph{Pour tout} $A_X$-\emph{Module} $M$, \emph{les homomorphismes}",
           "One edit: it also gives the capital M (word)."))
F.append(f(300, "Lemme 4.2, 'et' between the two displays",
           "'et' underlined",
           "et (no underline markup)", "underline", "high",
           r"\]" + N + "et" + N + r"\[", r"\]" + N + r"\emph{et}" + N + r"\[",
           ""))
F.append(f(300, "Lemme 4.2, last sentence",
           "underlined: 'sont liés par la relation' | 'De plus' | 'est de degré' (f_*f^* = id., f_* and '0 .' "
           "not); no comma after 'De plus'",
           r"sont liés par la relation $f_*f^*=\mathrm{id}$. De plus, $f_*$ est de degré $0$. (no underline "
           "markup)", "underline", "high",
           r"sont liés par la relation $f_*f^*=\mathrm{id}$. De plus, $f_*$ est de degré $0$.",
           r"\emph{sont liés par la relation} $f_*f^*=\mathrm{id}$. \emph{De plus} $f_*$ \emph{est de degré} $0$.",
           "One edit: it also drops the comma the TeX adds after 'De plus' (punctuation)."))
F.append(f(300, "proof of 4.2, projection formula f_*(x.f^*(x')) = f_*(x).x' ,",
           "the typewriter's full stop as product dot, twice",
           r"f_*(x\,f^*(x'))=f_*(x)x',", "symbol", "high",
           r"f_*(x\,f^*(x'))=f_*(x)x',", r"f_*(x\cdot f^*(x'))=f_*(x)\cdot x',",
           "The TeX has a thin space for the first dot and drops the second (written \\cdot by the volume's rule, "
           "as p. 294)."))

# ---------------- checks ----------------
ok = True
texts = {p: open(B % p, encoding="utf-8").read() for p in range(296, 301)}
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    t = texts[d["page"]]
    old = d["fix"]["old"]
    c = t.count(old)
    if c != 1:
        ok = False
        print("COUNT", c, "item", i, d["page"], repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER in fix", i)
print("all olds unique:", ok)

# simulate applying the fixes in order on each page (each old must be found when its turn comes)
for p in range(296, 301):
    t = texts[p]
    for i, d in enumerate(F):
        if d["page"] != p or d["fix"] is None:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        if t.count(old) != 1:
            print("SEQUENTIAL FAIL page", p, "item", i, repr(old))
            ok = False
        t = t.replace(old, new, 1)
    open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_296_300\page_%d_applied_preview.tex" % p,
         "w", encoding="utf-8", newline="\n").write(t)
print("sequential application ok:", ok)

counts = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(d["page"], {"normal": 0, "misprint": 0})[k] += 1
print(counts, "total", len(F))
if ok:
    json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("written", OUT)
