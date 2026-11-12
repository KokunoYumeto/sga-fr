import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
PAGES = BASE / "b336_340"
OUT = BASE / "findings_336_340.json"
NL = "\u23ce"  # placeholder for a line break in old/new


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 336 ----------------
L.append(F(336, "top of the page: item (b) of Lemme 9.1",
           "p. 336 begins with '(b) Pour tout z ∈ C•(N̂), on a :'; p. 335 ends with the display (9.1.3)",
           r"the '\item' that prints '(b)' is the last line of page_335.tex, just above the folio-336 marker",
           "marker", "high",
           note=r"Page 336 really begins at the '\item' on the line above the marker (s5.tex diplomatic line 11418, current line 11414). Exact fix: python -I move_marker.py 5 336 '\item' --before (simulated in memory on both layers: the marker moves 6 characters and then stands on its own line between '\]' (end of (9.1.3)) and '\item'). Text not moved."))
L.append(F(336, "Lemme 9.1 (ii)(b), first words",
           "'(b) Pour tout': capital P; 'Pour tout' underlined (z and C•(N̂) not)",
           r"pour tout $z\in C^*(\widehat N)$", "word", "high",
           r"pour tout $z\in", r"\emph{Pour tout} $z\in",
           note="One edit: the capital P and the underline of the statement."))
L.append(F(336, "Lemme 9.1 (ii)(b), 'on a :' before (9.1.4)",
           "', on a :': a colon; 'on a' underlined, the colon not",
           r"$, on a (no colon, no underline)", "punctuation", "high",
           r"(\widehat N)$, on a⏎\[", r"(\widehat N)$, \emph{on a} :⏎\[",
           note="One edit: the colon and the underline."))
L.append(F(336, "display (9.1.4)",
           "'s*(z) = p_*(z c_r(F̌))  , dans  C•(S).': a comma before 'dans'",
           r"p_*(z\,c_r(\check F))\quad\text{dans }C^*(S).", "punctuation", "high",
           r"(z\,c_r(\check F))\quad", r"(z\,c_r(\check F)),\quad",
           note="The TeX drops the comma."))
L.append(F(336, "display (9.1.4), 'dans'",
           "'dans' underlined (end of the statement)",
           r"\text{dans }", "underline", "high",
           r"\text{dans }C^*(S).", r"\text{\emph{dans} }C^*(S).",
           note=""))
L.append(F(336, "proof, 'L'égalité du 1e et du 3e membre de (9.1.2)'",
           "'du 1e et du 3e membre': the numerals with a raised e",
           "du premier et du troisième membre", "word", "high",
           "du premier et du troisième membre", r"du 1\textsuperscript{e} et du 3\textsuperscript{e} membre",
           note="The TeX writes the abbreviations out."))
L.append(F(336, "number of the display after 'on voit que'",
           "'(9.1.2) bis': 'bis' outside the parentheses",
           r"\tag{9.1.2 bis} (prints '(9.1.2 bis)')", "number", "high",
           r"\tag{9.1.2 bis}", r"\tag*{(9.1.2) bis}",
           note=r"\tag* as in the file's \tag*{(4.2.4)'}. Same form for (9.3.7) bis on p. 340."))
L.append(F(336, "'et à fortiori des égalités'",
           "'à fortiori' with a grave accent on the a",
           "et a fortiori", "accent", "high",
           "et a fortiori", "et à fortiori",
           note="The print's spelling (a current French spelling, not a misprint)."))
L.append(F(336, "'Notant α : V(N) → N̂ l'inclusion canonique'",
           "a plain arrow, no hook (the hooks of 'i : Y ↪ X' and 's : Y ↪ N̂' on p. 337 are clear)",
           r"\alpha:V(N)\hookrightarrow\widehat N", "symbol", "high",
           r"V(N)\hookrightarrow\widehat N$ l'inclusion", r"V(N)\to\widehat N$ l'inclusion",
           note=""))
L.append(F(336, "'on a évidemment α*(O_p(1)) ≃ O_V(N) , d'où'",
           "O_p(1): the subscript is a small typed p (bowl at x-height, descender)",
           r"\mathcal O_P(1) (silently corrected)", "misprint_in_print", "medium",
           r"\alpha^*(\mathcal O_P(1))\simeq", r"\alpha^*(\mathcal O_p(1))\simeq",
           corrected=r"\mathcal O_P(1)",
           note="The bundle is P; (9.1.6) on the same page prints O_P with a capital P. Same series as the small p of A_p, mu_p, O_p(1) on pp. 286-288 (all or none)."))
L.append(F(336, "display α*(ξ) = α*(c_1(O_p(1))) = c_1(O_V(N)) = 0",
           "O_p(1): small typed p as subscript",
           r"c_1(\mathcal O_P(1)) (silently corrected)", "misprint_in_print", "medium",
           r"c_1(\mathcal O_P(1))", r"c_1(\mathcal O_p(1))",
           corrected=r"c_1(\mathcal O_P(1))",
           note="As the line above."))
L.append(F(336, "display (9.1.6), c_{r+1}(p*(Ň) ⊕ O_P)",
           "O_P without a prime: the stroke at the upper right is the tail of the hand-drawn script O (the same tail on O_p(1) and O_V(N) above); the subscript is a capital P",
           r"\mathcal O'_P", "symbol", "high",
           r"\mathcal O'_P", r"\mathcal O_P",
           note="The TeX adds a prime."))
L.append(F(336, "display z = Σ p*(a_i)ξ^i , avec a_i ∈ C•(S)",
           "', avec  a_i ∈ C•(S),': the word 'avec' between the two formulas",
           r",\qquad a_i\in C^*(S),", "missing", "high",
           r",\qquad a_i\in C^*(S),", r",\quad\text{avec }a_i\in C^*(S),",
           note="The TeX drops 'avec'."))
L.append(F(336, "'([CH] 4 Th 1)'",
           "'Th 1': no full stop after Th",
           "Th. 1", "punctuation", "high",
           "Th. 1)", "Th 1)",
           note="The TeX adds a full stop."))
L.append(F(336, "the Chow ring C•(-) throughout pp. 336-340 (convention, reported once)",
           "C with a small raised dot (C•): e.g. p. 336 'Pour tout z ∈ C•(N̂)' (Lemme 9.1 (b)), p. 337 'y ∈ C•(Y)' (Théorème 9.2), p. 340 'Pour tout y ∈ C•(N̂)' (Lemme 9.4); C^1(Y) on p. 340 has the numeral",
           r"C^* (a star) in all 13 places on pp. 336-340: C^*(\widehat N), C^*(S), C^*(Y), C^*(Z')", "symbol", "high",
           note=r"Convention of the transcription, not itemized: one global pass C^* -> C^{\bullet} over section 9 (from p. 335, 'on note $C^*(X)$ l'anneau de Chow'), as A^* -> A^{\bullet} for the print's A• earlier in the exposé."))

# ---------------- page 337 ----------------
L.append(F(337, "'la \"formule de self-intersection\" dans l'anneau de Chow'",
           "straight typewriter double quotes",
           "«formule de self-intersection»", "punctuation", "high",
           "«formule de self-intersection»", "``formule de self-intersection''",
           note="Guillemets for the print's straight quotes (the accepted forms are ``...'' and \"...\")."))
L.append(F(337, "Théorème 9.2, first sentence",
           "underlined: 'Soient' | 'un corps séparablement clos et' | 'une' / 'immersion fermée, purement de codimension' | 'de' | 'schémas quasiprojectifs et lisses' (k, i : Y ↪ X, d, 'k-' and the full stop not)",
           "no underline markup", "underline", "high",
           r"Soient $k$ un corps séparablement clos et $i:Y\hookrightarrow X$ une immersion fermée, purement de codimension $d$, de $k$-schémas quasiprojectifs et lisses.",
           r"\emph{Soient} $k$ \emph{un corps séparablement clos et} $i:Y\hookrightarrow X$ \emph{une immersion fermée, purement de codimension} $d$, \emph{de} $k$-\emph{schémas quasiprojectifs et lisses}.",
           note=""))
L.append(F(337, "Théorème 9.2, second sentence",
           "underlined: 'Alors, notant' | 'le faisceau normal de' | 'on a pour tout' | 'l'égalité' (N, i, y ∈ C•(Y) not)",
           "no underline markup", "underline", "high",
           r"Alors, notant $N$ le faisceau normal de $i$, on a pour tout $y\in C^*(Y)$ l'égalité",
           r"\emph{Alors, notant} $N$ \emph{le faisceau normal de} $i$, \emph{on a pour tout} $y\in C^*(Y)$ \emph{l'égalité}",
           note=""))
L.append(F(337, "Théorème 9.2, 'dans C•(Y).' after the display",
           "'dans' underlined",
           r"dans $C^*(Y)$.", "underline", "high",
           r"dans $C^*(Y)$.", r"\emph{dans} $C^*(Y)$.",
           note=""))
L.append(F(337, "'Plongeons X dans Z = X ×_k P^1_k ...'",
           "'Plongeons' opens a new, indented paragraph after '... et de schémas auxiliaires.'",
           "runs on in the paragraph 'Pour la preuve, ...'", "other", "high",
           "auxiliaires. Plongeons", "auxiliaires.⏎⏎Plongeons",
           note="Paragraph break of the print."))
L.append(F(337, "cartesian square N̂ → Z' over Y → Z",
           "both horizontal arrows are hooked (j_1 and i_1, the hook at the source)",
           r'''plain arrows \arrow[r,"j_1"] and \arrow[r,"i_1"']''', "symbol", "high",
           r'''\widehat N \arrow[r,"j_1"] \arrow[d,"g_1"'] & Z' \arrow[d,"f_1"]\\⏎Y \arrow[r,"i_1"']''',
           r'''\widehat N \arrow[r,hook,"j_1"] \arrow[d,"g_1"'] & Z' \arrow[d,"f_1"]\\⏎Y \arrow[r,hook,"i_1"']''',
           note=r'''tikz-cd 'hook', as elsewhere in the file (\arrow[r,hook,"i_1"']).'''))
L.append(F(337, "cartesian square, vertex Z",
           "'Z' with no comma after it",
           "Z ,", "punctuation", "high",
           r"& Z ,⏎\end{tikzcd}", r"& Z⏎\end{tikzcd}",
           note="The TeX adds punctuation to the diagram."))
L.append(F(337, "'L'inclusion Y ⊂ X permet d'identifier Y × P^1 = W à un sous-schéma fermé'",
           "'Y×P^1 = W'",
           r"$Y\times\mathbb P^1$", "missing", "high",
           r"d'identifier $Y\times\mathbb P^1$ à", r"d'identifier $Y\times\mathbb P^1=W$ à",
           note="The TeX drops '= W'."))
L.append(F(337, "'On note W' le \"transformé pur de Y × P^1 par f_1\" , i.e.'",
           "straight typewriter double quotes",
           r"«transformé pur de $Y\times\mathbb P^1$ par $f_1$»", "punctuation", "high",
           r"«transformé pur de $Y\times\mathbb P^1$ par $f_1$»", r"``transformé pur de $Y\times\mathbb P^1$ par $f_1$''",
           note="Guillemets for the print's straight quotes."))
L.append(F(337, "last line of p. 337, 'sont fixées par le diagramme canonique'",
           "the sentence ends with 'canonique' (no '(D_1).'); the label (D_1) stands only at the left of the diagram, at the top of p. 338",
           r"le diagramme canonique $(D_1)$.", "extra", "high",
           r"le diagramme canonique $(D_1)$.", "le diagramme canonique",
           note="The TeX adds the label and a full stop."))
L.append(F(337, "diagram (D_1) (printed at the top of p. 338), arrow j_1 : N̂ → Z'",
           "hooked arrow",
           r'''\arrow[rr,"j_1"] (plain)''', "symbol", "high",
           r'''\widehat N \arrow[rr,"j_1"]''', r'''\widehat N \arrow[rr,hook,"j_1"]''',
           note="Filed under p. 337, where the TeX of (D_1) stands until the folio-338 marker is moved."))
L.append(F(337, "diagram (D_1) (printed on p. 338), arrows s : Y → N̂ and δ : Y → W'",
           "both hooked (the hook at Y)",
           r'''\arrow[ur,"s"], \arrow[rr,"\delta"'] (plain)''', "symbol", "high",
           r'''Y \arrow[ur,"s"] \arrow[rr,"\delta"']''', r'''Y \arrow[ur,hook,"s"] \arrow[rr,hook,"\delta"']''',
           note="Printed on p. 338 (see the j_1 entry)."))
L.append(F(337, "diagram (D_1) (printed on p. 338), arrow β : W' → Z'",
           "hooked arrow",
           r'''\arrow[ur,"\beta"'] (plain)''', "symbol", "high",
           r'''W' \arrow[ur,"\beta"']''', r'''W' \arrow[ur,hook,"\beta"']''',
           note="Printed on p. 338."))
L.append(F(337, "diagram (D_1) (printed on p. 338), arrows γ : Y → Y × P^1 and α : Y × P^1 → X × P^1",
           "both hooked",
           r'''\arrow[rr,"\gamma"'], \arrow[ur,"\alpha"'] (plain)''', "symbol", "high",
           r'''Y \arrow[rr,"\gamma"'] & & Y\times\mathbb P^1 \arrow[ur,"\alpha"']''',
           r'''Y \arrow[rr,hook,"\gamma"'] & & Y\times\mathbb P^1 \arrow[ur,hook,"\alpha"']''',
           note="Printed on p. 338. g_1, id, f_1 and f_2 are plain in the print, as in the TeX."))
L.append(F(337, "diagram (D_1) (printed on p. 338), arrow f_2 : W' → Y × P^1",
           "the isomorphism sign ≀ at the left of the arrow, f_2 at the right",
           r'''\arrow[ddd,"f_2"'] (no ≀; f_2 at the left)''', "missing", "high",
           r'''\arrow[ddd,"f_2"']''', r'''\arrow[ddd,"\wr"',"f_2"]''',
           note=r'''Written like the file's \arrow[d,"f'"',"\wr"]. Printed on p. 338.'''))
L.append(F(337, "diagram (D_1) (printed on p. 338), vertex X × P^1",
           "'X × P^1' alone (no '= Z'; it is diagram (D_2) that has 'X × P^1 = Z')",
           r"X\times\mathbb P^1=Z", "extra", "high",
           r"X\times\mathbb P^1=Z", r"X\times\mathbb P^1",
           note="Printed on p. 338."))
L.append(F(337, "'De même, notant X' ...' after diagram (D_1) (printed on p. 338)",
           "'De même' at the left margin: the sentence continues the paragraph (the typescript indents new paragraphs, e.g. 'L'inclusion', 'Plongeons')",
           "a blank line before 'De même' (new paragraph)", "other", "medium",
           r"\]⏎⏎De même,", r"\]⏎De même,",
           note="Printed on p. 338."))
L.append(F(337, "'De même, notant X' le ous-schéma fermé de Z'' (printed on p. 338)",
           "'ous-schéma' (no s)",
           "sous-schéma (silently corrected)", "misprint_in_print", "high",
           "le sous-schéma fermé de $Z'$", "le ous-schéma fermé de $Z'$",
           corrected="le sous-schéma fermé de $Z'$",
           note="Printed on p. 338; the TeX silently corrects."))
L.append(F(337, "statement labels of pp. 337-340 (convention, reported once)",
           "'THEOREME 9.2 (MUMFORD).-' (p. 337), 'Lemme 9.3.-' (p. 339, typed in small letters), 'LEMME 9.4.-' (p. 340): not underlined, ending '.-'",
           r"\begin{statement}{Théorème 9.2 (Mumford)}, {Lemme 9.3}, {Lemme 9.4}: bold mixed case, the environment adds a full stop, no dash",
           "word", "high",
           note="Convention for the exposé's labels, not itemized. If the closing pass sets the print's capitals, Lemme 9.3 on p. 339 stays in small letters ('Lemme 9.3.-')."))
L.append(F(337, "the projective line and bundles, pp. 337-338 (convention, reported once)",
           "a plain typed P: 'Z = X ×_k P^1_k', 'N̂ = P_Y(N ⊕ O_Y)' (p. 337), 'P(N) = X' ∩ N̂' (p. 338)",
           r"\mathbb P everywhere: X\times_k\mathbb P^1_k, \mathbb P_Y(N\oplus\mathcal O_Y), \mathbb P(N), Y\times\mathbb P^1, X\times\mathbb P^1=Z",
           "font", "high",
           note="Convention, not itemized: the plain P of the print written \\mathbb P (as P^r, E^r on pp. 288-289)."))

# ---------------- page 338 ----------------
L.append(F(338, "top of the page: diagram (D_1)",
           "p. 338 begins with the diagram (D_1); p. 337 ends with '... sont fixées par le diagramme canonique' (the rest of p. 337 is blank)",
           r"page_337.tex goes on with the (D_1) diagram and 'De même, notant $X'$ ... il est'; the folio-338 marker stands before 'clair que'",
           "marker", "high",
           note=r"Page 338 really begins at the '\[' that opens the (D_1) diagram (the line after 'le diagramme canonique $(D_1)$.'). Exact fix: python -I move_marker.py 5 338 '\[' --before (simulated in memory on both layers: the marker moves back 536 characters to its own line between '... canonique $(D_1)$.' and '\['). The anchor is the last '\[' above the marker, so run the command once only. The (D_1) and 'De même' findings are filed under p. 337."))
L.append(F(338, "'sont fixées par le diagramme canonique' before (D_2)",
           "the sentence ends with 'canonique' (no '(D_2).'); the label (D_2) stands only at the left of the diagram",
           r"le diagramme canonique $(D_2)$.", "extra", "high",
           r"le diagramme canonique $(D_2)$.", "le diagramme canonique",
           note="The TeX adds the label and a full stop."))
L.append(F(338, "diagram (D_2), arrow j_1 : N̂ → Z'",
           "hooked arrow",
           r'''\arrow[rr,"j_1"] (plain)''', "symbol", "high",
           r'''\widehat N \arrow[rr,"j_1"]''', r'''\widehat N \arrow[rr,hook,"j_1"]''',
           note=""))
L.append(F(338, "diagram (D_2), arrows k : H → N̂ and j : H → X'",
           "both hooked (the hook at H)",
           r'''\arrow[ur,"k"], \arrow[rr,"j"'] (plain)''', "symbol", "high",
           r'''H \arrow[ur,"k"] \arrow[rr,"j"']''', r'''H \arrow[ur,hook,"k"] \arrow[rr,hook,"j"']''',
           note=""))
L.append(F(338, "diagram (D_2), arrow v : X' → Z'",
           "hooked arrow",
           r'''\arrow[ur,"v"'] (plain)''', "symbol", "high",
           r'''X' \arrow[ur,"v"']''', r'''X' \arrow[ur,hook,"v"']''',
           note=""))
L.append(F(338, "diagram (D_2), arrow i : Y → X",
           "hooked arrow",
           r'''\arrow[rr,"i"'] (plain)''', "symbol", "high",
           r'''Y \arrow[rr,"i"']''', r'''Y \arrow[rr,hook,"i"']''',
           note="u : X → X × P^1 = Z, g, g_1, f and f_1 are plain in the print, as in the TeX."))
L.append(F(338, "'Nous allons maintenant donner ...' after diagram (D_2)",
           "'Nous allons' at the left margin: no new paragraph (the typescript indents new paragraphs)",
           "a blank line before 'Nous allons' (new paragraph)", "other", "medium",
           r"\]⏎⏎Nous allons", r"\]⏎Nous allons",
           note=""))
L.append(F(338, "'On note le O_N̂ - Module localement libre défini par la suite exacte canonique'",
           "'On note le O_N̂-Module': the name E of the Module is missing (it first appears in (9.3.0))",
           r"On note le $\mathcal O_{\widehat N}$-Module (the printed reading)", "misprint_in_print", "medium",
           corrected=r"On note $E$ le $\mathcal O_{\widehat N}$-Module",
           note="The TeX keeps the printed reading."))

# ---------------- page 339 ----------------
L.append(F(339, "top of the page: 'et on pose' and (9.3.1)",
           "p. 339 begins with 'et on pose' and the display (9.3.1) ξ̄ = c_1(O_N̂(1)).; p. 338 ends with (9.3.0)",
           "'et on pose' and the display (9.3.1) end page_338.tex", "marker", "high",
           note="Page 339 really begins at 'et on pose' (the line after the display (9.3.0)). Exact fix: python -I move_marker.py 5 339 'et on pose' --before (simulated in memory on both layers: the marker moves back 71 characters to its own line between '\\]' (end of (9.3.0)) and 'et on pose'). Text not moved."))
L.append(F(339, "Lemme 9.3, statement",
           "'Avec les notations précédentes, on a les relations' underlined (the full stop not)",
           "no underline markup", "underline", "high",
           "Avec les notations précédentes, on a les relations", r"\emph{Avec les notations précédentes, on a les relations}",
           note=""))
L.append(F(339, "Lemme 9.3, end of the sentence",
           "'on a les relations.': a full stop",
           "relations:", "punctuation", "high",
           r":⏎\[⏎j_1^*(\beta", r".⏎\[⏎j_1^*(\beta",
           note=""))
L.append(F(339, "display (9.3.2)",
           "'j_1*(β_*(1)) = c_d(Ě) , dans C•(N̂) .': a comma before 'dans', 'dans' underlined, a full stop at the end",
           r"=c_d(\check E)\quad\text{dans }C^*(\widehat N), (no comma before dans, no underline, a comma at the end)",
           "punctuation", "high",
           r"=c_d(\check E)\quad\text{dans }C^*(\widehat N),⏎\tag{9.3.2}",
           r"=c_d(\check E),\quad\text{\emph{dans} }C^*(\widehat N).⏎\tag{9.3.2}",
           note="One edit: both punctuation marks and the underline."))
L.append(F(339, "display (9.3.3)",
           "'j_1*(v_*(1)) = ξ̄ , dans C•(N̂) .': a comma before 'dans', 'dans' underlined, a full stop at the end",
           r"=\bar\xi\quad\text{dans }C^*(\widehat N), (no comma before dans, no underline, a comma at the end)",
           "punctuation", "high",
           r"=\bar\xi\quad\text{dans }C^*(\widehat N),⏎\tag{9.3.3}",
           r"=\bar\xi,\quad\text{\emph{dans} }C^*(\widehat N).⏎\tag{9.3.3}",
           note="One edit: both punctuation marks and the underline."))
L.append(F(339, "display (9.3.4)",
           "'... + v_*(1), dans C•(Z').': a comma before 'dans', 'dans' underlined",
           r"+v_*(1)\quad\text{dans }C^*(Z').", "punctuation", "high",
           r"+v_*(1)\quad\text{dans }C^*(Z').", r"+v_*(1),\quad\text{\emph{dans} }C^*(Z').",
           note="One edit: the comma and the underline."))
L.append(F(339, "proof, the pair of equalities j_1*β_*(1) = s_*(1), j_1*v_*(1) = k_*(1)",
           "no comma after s_*(1) (only the full stop after k_*(1))",
           r"s_*(1),\\", "punctuation", "high",
           r"=s_*(1),\\", r"=s_*(1)\\",
           note="The TeX adds a comma."))
L.append(F(339, "'normalisation des classes de Chern ([CH] 4-18)'",
           "'4-18': a hyphen",
           "4--18", "punctuation", "high",
           "([CH] 4--18)", "([CH] 4-18)",
           note="En dash for the print's hyphen."))
L.append(F(339, "display (9.3.7)",
           "'0 = j_1*(j_1)_* g*(μ) + ξ̄ .': g* without the index 1 (clear in the scan)",
           r"g^*(\mu) (the printed reading)", "misprint_in_print", "high",
           corrected=r"g_1^*(\mu)",
           note="(9.3.6) has g_1*(μ), and (j_1)_* g*(μ) needs a class on N̂, so g_1. The TeX keeps the printed reading."))

# ---------------- page 340 ----------------
L.append(F(340, "display (9.3.7) bis",
           "'0 = μ j_1*(j_1)_*(1) + ξ̄ , avec μ ∈ N .': the word 'avec'",
           r",\qquad \mu\in\mathbb N.", "missing", "high",
           r",\qquad \mu\in\mathbb N.", r",\quad\text{avec }\mu\in\mathbb N.",
           note="The TeX drops 'avec'."))
L.append(F(340, "number of the display (9.3.7) bis",
           "'(9.3.7) bis': 'bis' outside the parentheses",
           r"\tag{9.3.7 bis} (prints '(9.3.7 bis)')", "number", "high",
           r"\tag{9.3.7 bis}", r"\tag*{(9.3.7) bis}",
           note="As (9.1.2) bis on p. 336."))
L.append(F(340, "'Portant cette expression dans (9.3.7) bis,'",
           "'(9.3.7) bis'", "(9.3.7 bis)", "number", "high",
           "dans (9.3.7 bis),", "dans (9.3.7) bis,",
           note=""))
L.append(F(340, "'du lemme suivant (qui serait évident ... pour tout y ∈ C•(N̂)).'",
           "the clause is in parentheses: '(qui serait ... y ∈ C•(N̂)).'; no comma after 'suivant'",
           r"suivant, qui serait ... pour tout $y\in C^*(\widehat N)$.", "punctuation", "high",
           r"suivant, qui serait évident si on savait, comme c'est le cas en cohomologie, que⏎\[⏎j_1^*(j_1)_*(y)=-y\bar\xi⏎\]⏎pour tout $y\in C^*(\widehat N)$.",
           r"suivant (qui serait évident si on savait, comme c'est le cas en cohomologie, que⏎\[⏎j_1^*(j_1)_*(y)=-y\bar\xi⏎\]⏎pour tout $y\in C^*(\widehat N)$).",
           note="One edit for both parentheses. The print runs the formula into the text (layout, not reported)."))
L.append(F(340, "Lemme 9.4, 'Pour tout'",
           "'Pour tout' underlined",
           "no underline markup", "underline", "high",
           r"Pour tout $y", r"\emph{Pour tout} $y",
           note=""))
L.append(F(340, "Lemme 9.4, 'on a :'",
           "', on a :': a colon; 'on a' underlined, the colon not",
           "$, on a (no colon, no underline)", "punctuation", "high",
           r"(\widehat N)$, on a⏎\[", r"(\widehat N)$, \emph{on a} :⏎\[",
           note="One edit: the colon and the underline."))
L.append(F(340, "display (9.4.1)",
           "'[j_1* v_*(1)]^p': square brackets",
           r"\bigl(j_1^*v_*(1)\bigr)^p", "formula", "high",
           r"\bigl(j_1^*v_*(1)\bigr)^p", r"[j_1^*v_*(1)]^p",
           note=""))
L.append(F(340, "display c_d(Ě) j_1*(j_1)_*(y) = c_d(E) j_1*(j_1)_* g_1*(a_o) ;",
           "right-hand side 'c_d(E)': no check over E (the check over the E on the left is clear; no trace of one on the right)",
           r"c_d(E) (the printed reading)", "misprint_in_print", "medium",
           corrected=r"c_d(\check E)",
           note="Lemme 9.4 and (9.1.6) concern c_d(Ě). The TeX keeps the printed reading."))

# ---------------- checks ----------------
pages = {p: (PAGES / f"page_{p}.tex").read_bytes().decode("utf-8") for p in range(336, 341)}
ok = True
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        if d["kind"] == "misprint_in_print" and "corrected" not in d:
            print("misprint without corrected", i)
            ok = False
        continue
    t = pages[d["page"]]
    n = t.count(fx["old"])
    if n != 1:
        print("COUNT", n, d["page"], repr(fx["old"]))
        ok = False
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        print("marker in fix", i)
        ok = False
    for s in (fx["old"], fx["new"]):
        if any(ord(c) < 32 and c != "\n" for c in s):
            print("control char", i, repr(s))
            ok = False
# overlapping olds on the same page
for p in range(336, 341):
    spans = []
    for d in L:
        if d["page"] == p and d["fix"]:
            k = pages[p].find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP", p, a[2], "|", b[2])
            ok = False
# apply all fixes in memory, to be sure they apply in sequence
for p in range(336, 341):
    t = pages[p]
    for d in L:
        if d["page"] == p and d["fix"]:
            assert t.count(d["fix"]["old"]) == 1, (p, d["fix"]["old"])
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in L)
for p in range(336, 341):
    print(p, c[(p, False)], "/", c[(p, True)])
print("total", len(L), "ok", ok)
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(L, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("written", OUT)
