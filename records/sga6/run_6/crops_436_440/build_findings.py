"""Build findings_436_440.json; check every fix (old once in its page file; all fixes of a page apply in any order)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
B = RUN / "b436_440"
OUT = RUN / "findings_436_440.json"
NL = "<NL>"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


TOR_NOTE = r"Sheaf Tor underlined in the print, \Tor (= \operatorname{Tor}) plain; \underline{\Tor} as applied on pp. 431-435 (findings_431_435)."

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 436 ----------------
add(436, "conventions of pp. 436-440: K with a raised dot",
    "K˙ (K with a raised filled dot) in all 11 places of pp. 436-440: p. 436 'la classe dans K˙(Y)', 'soient x, y ∈ K˙(Y)', the §3 title 'Calcul du K˙ d'un schéma éclaté'; p. 440 the eight K˙ of the display i_*, j_*, f_*, g_* (both scans)",
    r"K^\circ (11 places)", "symbol", "high", None,
    r"The Exposé VII convention reported in findings_416_420 and findings_431_435 (one script K^\circ -> K^{\bullet} for VII, both layers): not itemized. Three examples: p. 436 'soient \(x,y\in K^\circ(Y)\)' -> 'soient \(x,y\in K^{\bullet}(Y)\)'; p. 440 'i_*:K^\circ(Y)\to K^\circ(X);' -> 'i_*:K^{\bullet}(Y)\to K^{\bullet}(X);'; p. 440 'g_*:K^\circ(Y')\to K^\circ(Y).' -> 'g_*:K^{\bullet}(Y')\to K^{\bullet}(Y).'.")

add(436, "conventions of pp. 436-440: letters of sheaves",
    "underlined in the print (both scans): every M of p. 436 (M, Ri_*(M), i_*(M), (M,O_Y), M⊗, 10 letters) and the N of ∧^i N in the second display; p. 437 J, J', every J of J.O_X', ⊕J^n, O_X/J, J^n/J^{n+1}, J/J^2, J'/J'^2, the S of Proj(S), S = ⊕J^n, i^*(S), the N of 'On note N', P(N), g^*(N), the F of (3.1.2) and of Lemme 3.2 ii), the L of 'on le notera L'; p. 438 the first J of 'J étant défini par un idéal J de A'; p. 439 J' ('l'idéal inversible J'') and the J of 0 → J → O_X; p. 440 every J of J⊗O_X' and J.O_X', the N of both g^*(N) and of P(N), the F of Tor_1 = F. Plain in the print: the N of x.λ^i(N) and λ_{-1}(N) (p. 436, classes in K), the ideal J of A, J^n, J^p (p. 438), E, E', E'', A, A', the K of K.(u) (pp. 438-439)",
    "all plain", "underline", "high", None,
    r"Convention of the Exposé VII transcription (findings_416_420 to findings_431_435): not itemized; no blind script (the ring-case J and the class N stay plain). The underlined O written \cO falls under the pending volume decision. Three examples, in the form to use if the diplomatic layer reproduces the underline: p. 436 'de type fini \(M\). L'élément' -> 'de type fini \(\underline{M}\). L'élément'; p. 437 'On note \(J\) l'idéal' -> 'On note \(\underline{J}\) l'idéal'; p. 437 'on le notera \(L\).' -> 'on le notera \(\underline{L}\).'.")

add(436, "statements of pp. 436-437: Corollaire 2.8 (p. 436), Lemme 3.2 (p. 437)",
    "underlined word group by word group (both scans): Cor. 2.8 'Sous les hypothèses de', 'soient', 'on a la relation'; Lemme 3.2 'Avec les hypothèses et les notations de', 'on a les isomorphismes suivants'; '2.7,', '3.1,', 'x, y ∈ K˙(Y) ;', the colons and the items i), ii) plain; the labels underline only the word",
    r"the statements in roman (no \underline, no \emph)", "underline", "high", None,
    "Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as reported for pp. 416-435: not itemized. No emphasized defined terms and no category letter on pp. 436-440.")

add(436, "first paragraph: 'L'élément i^*(i_*(x)) est alors la classe du complexe Li^*(Ri_*(M)), obtenu'",
    "L and R each with a double underline (the derived functors), M with a single underline (both scans; crops_436_440/c436_LR1.png)",
    r"\(\mathrm L i^*(Ri_*(M))\)", "font", "high",
    fx(r"complexe \(\mathrm L i^*(Ri_*(M))\), obtenu", r"complexe \(\mathbb L i^*(\mathbb Ri_*(M))\), obtenu"),
    r"Double-struck L and R written plain (reported singly, as asked); \mathbb R as in the applied fix of p. 435 (\mathbb Ri_*(L^\bullet)), \mathbb L as the \mathbb L f^* of Exposé I. The underlined M is in the sheaf-letter entry.")

add(436, "first paragraph: 'une résolution projective du complexe Ri_*(M) = i_*(M)'",
    "R with a double underline (both scans; crops_436_440/c436_LR1.png)",
    r"\(Ri_*(M)=i_*(M)\)", "font", "high",
    fx(r"du complexe \(Ri_*(M)=i_*(M)\)", r"du complexe \(\mathbb Ri_*(M)=i_*(M)\)"),
    "As the entry above.")

add(436, "first paragraph: 'Les faisceaux d'homologie de ce complexe sont donc les Tor_i^{O_X}(M,O_Y)'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"donc les \(\Tor_i", r"donc les \(\underline{\Tor}_i"), TOR_NOTE)

add(436, "first display, left member Tor_i^{O_X}(M,O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\[<NL>\Tor_i^{\cO_X}(M,\cO_Y)", r"\[<NL>\underline{\Tor}_i^{\cO_X}(M,\cO_Y)"), TOR_NOTE)

add(436, "first display, right member M⊗_{O_Y} Tor_i^{O_X}(O_Y,O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"M\otimes_{\cO_Y}\Tor_i^{\cO_X}(\cO_Y,\cO_Y).", r"M\otimes_{\cO_Y}\underline{\Tor}_i^{\cO_X}(\cO_Y,\cO_Y)."), TOR_NOTE)

add(436, "second display (after 'D'après 2.5'), left member Tor_i^{O_X}(O_Y,O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\[<NL>\Tor_i^{\cO_X}(\cO_Y,\cO_Y)", r"\[<NL>\underline{\Tor}_i^{\cO_X}(\cO_Y,\cO_Y)"), TOR_NOTE)

add(436, "'Les Tor_i^{O_X}(M,O_Y) sont donc des O_Y-Modules localement libres', after the second display",
    "begins a new, indented paragraph (both scans)",
    r"'\]' followed directly by 'Les' (the paragraph runs on)", "other", "high",
    fx(r"\]<NL>Les", r"\]<NL><NL>Les"), "Missing paragraph break; independent of the Tor entry of the same line (no common text).")

add(436, "'Les Tor_i^{O_X}(M,O_Y) sont donc des O_Y-Modules'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\(\Tor_i^{\cO_X}(M,\cO_Y)\) sont donc", r"\(\underline{\Tor}_i^{\cO_X}(M,\cO_Y)\) sont donc"), TOR_NOTE)

add(436, "'et la classe dans K˙(Y) du complexe Li^*(Ri_*(M)) est la somme alternée'",
    "L and R each with a double underline (both scans; crops_436_440/c436_LR2.png)",
    r"\(\mathrm L i^*(Ri_*(M))\)", "font", "high",
    fx(r"complexe \(\mathrm L i^*(Ri_*(M))\) est la somme", r"complexe \(\mathbb L i^*(\mathbb Ri_*(M))\) est la somme"),
    "As the first L/R entry.")

add(436, "third display: 'cl(M⊗_{O_Y} Tor_i^{O_X}(O_Y,O_Y))'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\operatorname{cl}\bigl(M\otimes_{\cO_Y}\Tor_i", r"\operatorname{cl}\bigl(M\otimes_{\cO_Y}\underline{\Tor}_i"), TOR_NOTE)

add(436, "Corollaire 2.8, the display i_*(xyλ_{-1}(N)) = i_*(x).i_*(y)",
    "no equation number at either margin (both scans)",
    r"\begin{equation}\tag{2.8.1}", "extra", "high",
    fx(r"\begin{equation}\tag{2.8.1}", r"\begin{equation}\notag"),
    r"The number is the TeX's addition; main.tex has (2.8.1) only as this tag. \notag as for (2.4.1), (2.7.1) (findings_431_435).")

add(436, "'D'après 2.7, yλ_{-1}(N) = i^*(i_*(y)).' after the display of Corollaire 2.8",
    "begins a new, indented paragraph (both scans)",
    r"'\end{equation}' followed directly by 'D'après 2.7' (the paragraph runs on)", "other", "high",
    fx(r"\end{equation}<NL>D'après 2.7", r"\end{equation}<NL><NL>D'après 2.7"), "Missing paragraph break; independent of the (2.8.1) entry.")

add(436, "'Par application de la formule de projection, on trouve donc :'",
    "begins a new, indented line-paragraph after the one-line paragraph 'D'après 2.7, ... = i^*(i_*(y)).' (both scans)",
    "one paragraph with 'D'après 2.7, ...'", "other", "high",
    fx(r". Par application", r".<NL><NL>Par application"), "Missing paragraph break.")

# ---------------- page 437 ----------------
add(437, "start of page (folio-437 marker)",
    "p. 436 ends '... faisant éclater Y, et Y' = Y×_X X'.'; p. 437 begins 'On sait (EGA II 8.1.8) que Y' est un sous-schéma fermé ...' (both scans)",
    "page_436.tex ends 'et \\(Y'=Y\\times_X X'\\). On' above the folio-437 marker; page_437.tex begins 'sait (EGA II 8.1.8)'",
    "marker", "high", None,
    r"Page 437 really begins at 'On sait'. Exact edit in main.tex, both layers (diplomatic lines 10940-10942, current 10946-10948): replace '\(Y'=Y\times_X X'\). On\n%%%%%%%%%%  scan idx 450  |  folio 437  %%%%%%%%%%\nsait (EGA II 8.1.8)' by '\(Y'=Y\times_X X'\).\n%%%%%%%%%%  scan idx 450  |  folio 437  %%%%%%%%%%\nOn sait (EGA II 8.1.8)' (old string once in each layer; simulated in memory: crops_436_440/sim_marker.py). The sentence runs on, so no blank line. python -I move_marker.py 6 437 On --before gives the same split (it leaves a space at the end of the line before the marker).")

add(437, "first lines: 'Y' est un sous-schéma fermé de X' défini par un idéal de O_X, canoniquement isomorphe à O_X'(1)'",
    "O_X with an unprimed X, then a comma (both scans; crops_436_440/c437_OX.png, w437_OX.png)",
    r"un idéal de \(\cO_X\) (printed reading kept)", "misprint_in_print", "high", None,
    "Y' is a closed subscheme of X', so the ideal is one of O_X' (as 'J' l'idéal de O_X' qui définit Y'' below). The current layer already reads \\cO_{X'}.",
    corrected=r"un idéal de \(\cO_{X'}\)")

add(437, "'l'immersion j : Y' ⟶ X étant définie par un idéal inversible'",
    "target X without a prime (both scans; crops_436_440/c437_jYX.png, w437_jYX.png)",
    r"\(j:Y'\to X\) (printed reading kept)", "misprint_in_print", "high", None,
    "j is the immersion of Y' in X' (diagram (3.1.1): Y' → X' labelled j); Y' → X is not an immersion. The current layer already reads X'.",
    corrected=r"\(j:Y'\to X'\)")

add(437, "'Par définition, X' = Proj(S), où S = ⊕ J^n. Par suite, on a :' after (3.1.1)",
    "begins a new, indented paragraph (both scans)",
    r"'\end{equation}' followed directly by 'Par définition' (the paragraph runs on)", "other", "high",
    fx(r"\end{equation}<NL>Par définition", r"\end{equation}<NL><NL>Par définition"), "Missing paragraph break.")

add(437, "'Or, i étant régulière, ⊕ J^n/J^{n+1} ≃ Sym_{O_Y}(J/J^2) (1.3)'",
    "Sym underlined with a single line, the sheaf Sym (both scans; crops_436_440/c437_Sym.png, w437_Sym.png)",
    r"\Sym_{\cO_Y}(J/J^2) (\Sym is \operatorname{Sym} in Exposé VII, main.tex line 10496)", "underline", "high",
    fx(r"\Sym_{\cO_Y}(J/J^2)", r"\underline{\Sym}_{\cO_Y}(J/J^2)"),
    "Underlined like the sheaf Tor; the only other \\Sym of Exposé VII is the ring case Sym_{A/J}(J/J^2) of p. 418.")

add(437, "'Sur Y', on peut écrire la suite exacte :'",
    "begins a new, indented paragraph after the display Y' = P(N) (both scans)",
    r"'\]' followed directly by 'Sur \(Y'\)' (the paragraph runs on)", "other", "high",
    fx(r"\]<NL>Sur \(Y'\)", r"\]<NL><NL>Sur \(Y'\)"), "Missing paragraph break.")

add(437, "'On remarque que O_Y'(1) = j^*(O_X'(1)) = J'/J'^2' after (3.1.2)",
    "begins a new, indented paragraph (both scans)",
    r"'\end{equation}' followed directly by 'On remarque' (the paragraph runs on)", "other", "high",
    fx(r"\end{equation}<NL>On remarque", r"\end{equation}<NL><NL>On remarque"), "Missing paragraph break.")

add(437, "Lemme 3.2 i), left member Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\Tor_i^{\cO_X}(\cO_{X'},\cO_Y)<NL>\simeq", r"\underline{\Tor}_i^{\cO_X}(\cO_{X'},\cO_Y)<NL>\simeq"), TOR_NOTE)

add(437, "Lemme 3.2 i), right member ∧^i Tor_1^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigwedge^i\Tor_1", r"\bigwedge^i\underline{\Tor}_1"), TOR_NOTE + " Independent of the punctuation entry of the same line.")

add(437, "Lemme 3.2 i), end: '∧^i Tor_1^{O_X}(O_X',O_Y) ;'",
    "a semicolon (both scans)", "a comma", "punctuation", "high",
    fx(r"(\cO_{X'},\cO_Y),\\[4pt]", r"(\cO_{X'},\cO_Y);\\[4pt]"), "")

add(437, "Lemme 3.2 ii), Tor_1^{O_X}(O_X',O_Y) ≃ F",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\Tor_1^{\cO_X}(\cO_{X'},\cO_Y)\simeq F.", r"\underline{\Tor}_1^{\cO_X}(\cO_{X'},\cO_Y)\simeq F."), TOR_NOTE)

add(437, "end of page: the proof label of Lemme 3.2",
    "p. 437 ends with item ii) of Lemme 3.2; p. 438 begins with the indented paragraph 'i) Comme O_Y peut se résoudre localement ...'; no label on either page (both scans)",
    r"\textit{Démonstration.} (last line of page_437.tex)", "extra", "high",
    fx(r"\textit{Démonstration.}", ""),
    "The transcription's proof label (diplomatic main.tex line 10978, current 10984), as on pp. 416, 418, 420, 422, 432, 435. Removing it leaves a blank line before the folio-438 marker, so 'i) Comme' stays a new paragraph, as printed.")

# ---------------- page 438 ----------------
add(438, "i): 'l'algèbre graduée ⊕_{i≥0} Tor_i^{O_X}(O_X',O_Y) est alternée (2.2)'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"graduée \(\bigoplus_{i\ge0}\Tor_i", r"graduée \(\bigoplus_{i\ge0}\underline{\Tor}_i"), TOR_NOTE)

add(438, "(3.2.1), left member ∧ Tor_1^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigwedge \Tor_1", r"\bigwedge \underline{\Tor}_1"), TOR_NOTE)

add(438, "(3.2.1), right member ⊕_{i≥0} Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigoplus_{i\ge0}\Tor_i^{\cO_X}(\cO_{X'},\cO_Y),", r"\bigoplus_{i\ge0}\underline{\Tor}_i^{\cO_X}(\cO_{X'},\cO_Y),"), TOR_NOTE)

add(438, "'prolongeant l'injection de Tor_1^{O_X}(O_X',O_Y)'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"l'injection de \(\Tor_1", r"l'injection de \(\underline{\Tor}_1"), TOR_NOTE)

add(438, "'dans ⊕_{i≥0} Tor_i^{O_X}(O_X',O_Y). Il suffit'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\Tor_i^{\cO_X}(\cO_{X'},\cO_Y)\). Il suffit", r"\underline{\Tor}_i^{\cO_X}(\cO_{X'},\cO_Y)\). Il suffit"), TOR_NOTE)

add(438, "'un homomorphisme régulier u : E ⟶ A, définissant J, avec E = (A)^n. Soient f_1,...,f_d les images d'une base de E.'",
    "exponent n (both scans; crops_436_440/w438_An.png)",
    r"\(E=(A)^n\) (printed reading kept)", "misprint_in_print", "high", None,
    "The basis of E is e_1,...,e_d (same page) and its images are f_1,...,f_d; p. 439 has (O_X')^{d-1}. The current layer already reads (A)^d.",
    corrected=r"\(E=(A)^d\)")

add(438, "'Dans ⊕_{n≥0} J^n, nous noterons, pour m ≤ p, x^{(m)} ...'",
    "begins a new, indented paragraph after '... les images d'une base de E.' (both scans)",
    "one paragraph with 'On peut donc se placer ...'", "other", "high",
    fx(r"base de \(E\). Dans", r"base de \(E\).<NL><NL>Dans"), "Missing paragraph break.")

add(438, "'Les Tor_i^{O_X}(O_X',O_Y) sont les faisceaux d'homologie du complexe K.(u)⊗O_X''",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"Les \(\Tor_i", r"Les \(\underline{\Tor}_i"), TOR_NOTE)

add(438, "'si e_1,...,e_d est la base donnée de E, on pose :'",
    "colon after 'pose', the same glyph as the colons of 'un seul :' and 'trouve donc :' (both scans; crops_436_440/c438_pose.png, w438_pose.png)",
    "on pose (no colon)", "punctuation", "high",
    fx(r"on pose<NL>\[", r"on pose:<NL>\["), "")

add(438, "display 'e'_1 = e_1 ; pour i ≠ 1, e'_i = e_i - (f_i^{(1)}/f_1^{(1)})e_1 .'",
    "a full stop at the end (both scans; crops_436_440/c438_e1dot.png, w438_e1dot.png); the next sentence begins with a capital ('Posons')",
    "a comma", "punctuation", "high",
    fx(r"e_1,<NL>\]", r"e_1.<NL>\]"), "")

add(438, "'En prenant pour base de ∧^k(E') les éléments'",
    "a typed k above the ∧, as the i above ∧ in ∧^i N (p. 436) (both scans; crops_436_440/c438_wedgek.png, w438_wedgek.png)",
    r"\(\bigwedge(E')\)", "formula", "high",
    fx(r"\(\bigwedge(E')\)", r"\(\bigwedge^k(E')\)"), "The exponent k is missing in the TeX.")

add(438, "'avec i_1<..<i_k on trouve donc :'",
    "two dots between the < signs (both scans; crops_436_440/c438_wedgek.png, w438_wedgek.png); the products e'_{i_1}∧...∧e'_{i_k} of the same line have three",
    r"\(i_1<\cdots<i_k\) (silently corrected)", "misprint_in_print", "medium",
    fx(r"i_1<\cdots<i_k", r"i_1<..<i_k"),
    "Typist's two-dot ellipsis; the corrected edition keeps \\cdots.",
    corrected=r"i_1<\cdots<i_k")

# ---------------- page 439 ----------------
add(439, "(3.2.2), left member Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\tag{3.2.2}<NL>\Tor_i", r"\tag{3.2.2}<NL>\underline{\Tor}_i"), TOR_NOTE)

add(439, "display for i = 1: Tor_1^{O_X}(O_X',O_Y) ≃ (O_Y')^{d-1}",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\[<NL>\Tor_1", r"\[<NL>\underline{\Tor}_1"), TOR_NOTE)

add(439, "(3.2.3), left member Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\tag{3.2.3}<NL>\Tor_i", r"\tag{3.2.3}<NL>\underline{\Tor}_i"), TOR_NOTE)

add(439, "(3.2.3), right member ∧^i Tor_1^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigwedge^i\Tor_1", r"\bigwedge^i\underline{\Tor}_1"), TOR_NOTE + " Independent of the punctuation entry of (3.2.3).")

add(439, "(3.2.3), end",
    "no punctuation after the display (both scans; crops_436_440/c439_323end.png, w439_323.png); (3.2.2) and the display for i = 1 end with a full stop, as in the TeX",
    r"(\cO_{X'},\cO_Y). (full stop added)", "punctuation", "high",
    fx(r"(\cO_{X'},\cO_Y).", r"(\cO_{X'},\cO_Y)"), "Punctuation the TeX adds at the end of a display.")

add(439, "'Or d'après 2.2, l'isomorphisme :' after (3.2.3)",
    "begins a new, indented paragraph (both scans)",
    r"'\end{equation}' followed directly by 'Or d'après 2.2' (the paragraph runs on)", "other", "high",
    fx(r"\end{equation}<NL>Or d'après 2.2", r"\end{equation}<NL><NL>Or d'après 2.2"), "Missing paragraph break.")

add(439, "first isomorphism after 'Or d'après 2.2', right member ⊕_{i≥0} Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigoplus_{i\ge0}\Tor_i^{\cO_X}(\cO_{X'},\cO_Y)<NL>\]<NL>défini par les isomorphismes (3.2.2)",
       r"\bigoplus_{i\ge0}\underline{\Tor}_i^{\cO_X}(\cO_{X'},\cO_Y)<NL>\]<NL>défini par les isomorphismes (3.2.2)"), TOR_NOTE)

add(439, "second isomorphism, left member ∧ Tor_1^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigwedge\Tor_1", r"\bigwedge\underline{\Tor}_1"), TOR_NOTE)

add(439, "second isomorphism, right member ⊕_{i≥0} Tor_i^{O_X}(O_X',O_Y)",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\bigoplus_{i\ge0}\Tor_i^{\cO_X}(\cO_{X'},\cO_Y)<NL>\]<NL>défini par les isomorphismes (3.2.3)",
       r"\bigoplus_{i\ge0}\underline{\Tor}_i^{\cO_X}(\cO_{X'},\cO_Y)<NL>\]<NL>défini par les isomorphismes (3.2.3)"), TOR_NOTE)

# ---------------- page 440 ----------------
add(440, "first line: 'et la suite exacte des Tor obtenue par tensorisation avec O_X' :'",
    "Tor underlined (both scans)", "des Tor (plain text)", "underline", "high",
    fx(r"des Tor obtenue", r"des \(\underline{\Tor}\) obtenue"),
    "The sheaf Tor in running text, as 'la suite exacte des Tor' on p. 434 (findings_431_435).")

add(440, "second display, 0 → Tor_1^{O_X}(O_X',O_Y) → J⊗O_X' → O_X'(1) → 0",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"Par suite, on obtient la suite exacte:<NL>\[<NL>0\longrightarrow<NL>\Tor_1",
       r"Par suite, on obtient la suite exacte:<NL>\[<NL>0\longrightarrow<NL>\underline{\Tor}_1"),
    TOR_NOTE + " The Tor of the first display of the page (0 → Tor_1 → J⊗O_X' → O_X' → O_Y' → 0) is plain in both scans (crops_436_440/c440_tor1.png, w440_tor1.png), as in the TeX: leave it.")

add(440, "'On fait alors son produit tensoriel par O_Y' ; comme ...'",
    "begins a new, indented paragraph after the second display (both scans)",
    r"'\]' followed directly by 'On fait alors' (the paragraph runs on)", "other", "high",
    fx(r"\]<NL>On fait alors", r"\]<NL><NL>On fait alors"), "Missing paragraph break.")

add(440, "'comme Tor_1^{O_X}(O_X',O_Y) est un O_Y'-Module'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"comme<NL>\(\Tor_1", r"comme<NL>\(\underline{\Tor}_1"), TOR_NOTE)

add(440, "third display, 0 → Tor_1^{O_X}(O_X',O_Y) → g^*(N) → O_Y'(1) → 0",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\Tor_1^{\cO_X}(\cO_{X'},\cO_Y)<NL>\longrightarrow<NL>g^*(N)", r"\underline{\Tor}_1^{\cO_X}(\cO_{X'},\cO_Y)<NL>\longrightarrow<NL>g^*(N)"), TOR_NOTE)

add(440, "display 'Tor_1^{O_X}(O_X',O_Y) = F .'",
    "Tor underlined (both scans)", r"\Tor plain", "underline", "high",
    fx(r"\Tor_1^{\cO_X}(\cO_{X'},\cO_Y)=F.", r"\underline{\Tor}_1^{\cO_X}(\cO_{X'},\cO_Y)=F."), TOR_NOTE)

add(440, "3.3, end of the paragraph: 'on peut définir les homomorphismes additifs (IV' before the display of i_*, j_*, f_*, g_*",
    "'(IV' with no number and no closing parenthesis, at the end of a short line; nothing after the display, and p. 441 begins with Proposition 3.4 (both scans; crops_436_440/w440_IV.png)",
    "additifs (IV (printed reading kept)", "misprint_in_print", "medium", None,
    "Unfinished reference of the typescript. p. 435 cites (IV 2.12) for the same i_* (IV 2.12, 'Variances inhabituelles de K˙ et K˙'); elsewhere Exposé VII leaves blanks '(IV\\qquad)' (main.tex lines 11901, 11917). The current layer also reads '(IV': the corrected edition needs the completed reference.",
    corrected=r"(IV 2.12)")

# ---------------- checks ----------------
ok = True
for p in range(436, 441):
    text = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    fixes = [f["fix"] for f in F if f["page"] == p and f["fix"]]
    for fx_ in fixes:
        n = text.count(fx_["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", p, n, repr(fx_["old"]))
        if "%%%%%%%%%%" in fx_["old"]:
            ok = False
            print("MARKER IN OLD", p, repr(fx_["old"]))
    # positions must not overlap
    spans = sorted((text.find(fx_["old"]), text.find(fx_["old"]) + len(fx_["old"]), fx_["old"]) for fx_ in fixes)
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
    results = []
    for order in (fixes, list(reversed(fixes))):
        t = text
        for fx_ in order:
            if t.count(fx_["old"]) != 1:
                ok = False
                print("ORDER FAIL", p, repr(fx_["old"]))
            t = t.replace(fx_["old"], fx_["new"], 1)
        results.append(t)
    if results[0] != results[1]:
        ok = False
        print("ORDER-DEPENDENT RESULT", p)
    nm = sum(1 for f in F if f["page"] == p and f["kind"] == "misprint_in_print")
    print(p, "entries:", sum(1 for f in F if f["page"] == p), "normal:", sum(1 for f in F if f["page"] == p) - nm, "misprint:", nm, "fixes:", len(fixes))
print("ALL CHECKS OK" if ok else "CHECKS FAILED")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(F))
