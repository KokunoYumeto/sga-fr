"""Build findings_361_365.json: '¶' in old/new stands for a line feed. Checks every old against its page file."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = 'C:/Users/user/Documents/sga_scan_check_20261105/run_6/'
OUT = RUN + 'findings_361_365.json'
NL = chr(10)


def fx(old, new):
    return {"old": old.replace('¶', NL), "new": new.replace('¶', NL)}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected.replace('¶', NL)
    d["note"] = note
    F.append(d)


# ---------------- p. 361 ----------------
add(361, "7.3, 'il est nécéssaire et suffisant'",
    "nécéssaire, with an acute accent on the second e as well (both scans; crops_361_365/p361_necessaire.png, wit_361_bot.png)",
    "nécéssaire (printed reading kept)", "misprint_in_print", "high", None,
    "Spelling slip of the typescript; the diplomatic layer is right (main.tex has the same spelling once more, line 10546, outside these pages).",
    corrected="nécessaire")
add(361, "Exemples 7.4 i), display 'd/dt(λ_t(n))/λ_t(n) = n(1+t)^{n-1}/(1+t)^n = n.Σ_{k=1}(-1)^{k-1}t^{k-1} .'",
    "the Σ has only k=1 under it, no ∞ above it (both scans; crops_361_365/p361_sigma.png, wit_361_bot.png), unlike (7.2.1) on the same page",
    r"n.\sum_{k=1}^{\infty}", "extra", "high",
    fx(r"n.\sum_{k=1}^{\infty}", r"n.\sum_{k=1}"),
    "Upper limit of the sum added by the transcription.")
add(361, "before 'D'après (7.1.1), les ψ^k sont des polynomes isobares'",
    "'D'après (7.1.1)' begins a new, indented paragraph after the display ψ^k(x+y) = ψ^k(x) + ψ^k(y). (both scans; wit_361_top.png)",
    r"\] followed directly by 'D'après (7.1.1)' (same paragraph)", "other", "high",
    fx(r"D'après (7.1.1),", r"¶D'après (7.1.1),"),
    "Missing paragraph break.")

# ---------------- p. 362 ----------------
add(362, "start of page (folio-362 marker)",
    "p. 362 begins 'opérations ψ^k définissent d'après 7.3 des endomorphismes additifs du'; p. 361 ends '... des Z-algèbres (1.8). Les' (both scans)",
    r"'opérations \(\psi^k\)' ends the last line of page_361.tex, above the folio-362 marker; page_362.tex begins 'définissent'",
    "marker", "high", None,
    r"The folio-362 marker stands two words late. Page 362 really begins at 'opérations \(\psi^k\)'. Exact fix in main.tex (both layers, once each): replace '(1.8). Les opérations \(\psi^k\)\n%%%%%%%%%%  scan idx 375  |  folio 362  %%%%%%%%%%\ndéfinissent' by '(1.8). Les\n%%%%%%%%%%  scan idx 375  |  folio 362  %%%%%%%%%%\nopérations \(\psi^k\)\ndéfinissent'. Equivalent: python -I move_marker.py 6 362 'opérations \(\psi^k\)' --before (the nearest match before the marker is the right one; it leaves a trailing space after 'Les'). Both simulated in memory on both layers with crops_361_365/sim_markers.py (one match each). Independent of the folio-363 move.")
add(362, "'du foncteur en λ-anneaux Ĝ ; d'après 1.10'",
    "Ĝ with its hat (both scans; crops_361_365/p362_Ghat.png, wit_362_top.png)",
    r"anneaux \(G\)~;", "symbol", "high",
    fx(r"anneaux \(G\)~;", r"anneaux \(\widehat G\)~;"),
    r"The hat is dropped; \widehat G is the file's form for this functor (diagram (7.5.2), 'source \widehat G\times\widehat G' p. 363).")
add(362, "first display, left member 'd/dt(λ_u(1+Xt))/λ_u(1+Xt))='",
    "after the second λ_u(1+Xt) a further, hand-drawn closing parenthesis before '=': three opening, four closing (both scans; crops_361_365/p362_disp1.png, w362_disp1.png)",
    r"\frac{d}{dt}(\lambda_u(1+Xt))/\lambda_u(1+Xt) (silently corrected)", "misprint_in_print", "high",
    fx(r"/\lambda_u(1+Xt)", r"/\lambda_u(1+Xt))"),
    "Unbalanced parenthesis of the print; the TeX silently drops it, the fix restores the printed reading. Independent of the d/dt and underline entries below.",
    corrected=r"/\lambda_u(1+Xt)")
add(362, "same display, 'd/dt' in front of (λ_u(1+Xt))",
    "d/dt (both scans), as in the definition (7.1.1)",
    r"\frac{d}{dt}(\lambda_u(1+Xt)) (printed reading kept)", "misprint_in_print", "medium", None,
    "The λ-structure of Ĝ is written in the variable u (λ_u(1+Xt) = 1̲ + {1+Xt}u), and the right member is the series in u whose coefficients give ψ^k(1+Xt) = {1+Xt}^{∘k}: the logarithmic derivative is taken with respect to u; the d/dt of (7.1.1) was carried over. The TeX keeps the printed reading.",
    corrected=r"\frac{d}{du}(\lambda_u(1+Xt))/\lambda_u(1+Xt)")
add(362, "same display, denominator '1̲ + {1+Xt}u'",
    "the 1 is underlined: the unit of Ĝ (both scans; crops_361_365/p362_disp1.png, w362_disp1.png)",
    r"\frac{1+Xt}{1+\{1+Xt\}u}", "underline", "high",
    fx(r"{1+\{1+Xt\}u}", r"{\underline{1}+\{1+Xt\}u}"),
    r"\underline{1} is the file's form for this unit (21 times in Exposé V, e.g. '\(\lambda_u\) est \(\underline{1}+\{1+Xt\}u\)').")
add(362, "Proposition 7.5 ii), 'si les ψ^t vérifient ces identités'",
    "ψ^t: the exponent is a t (both scans; crops_361_365/p362_psit.png, wit_362_top.png)",
    r"\(\psi^k\) (silently corrected)", "misprint_in_print", "high",
    fx(r"si les \(\psi^k\) vérifient", r"si les \(\psi^t\) vérifient"),
    "Typing slip: the operations are the ψ^k of i). The fix restores the printed reading.",
    corrected=r"si les \(\psi^k\) vérifient")
add(362, "Proposition 7.5 (the statement)",
    "underlined word groups: i) 'Si', 'est un', 'anneau' (λ- plain), 'les opérations', 'vérifient', 'les identités'; ii) 'Réciproquement', 'si les', 'vérifient ces identités', 'et si', 'est de', 'caractéristique nulle', 'est un', 'anneau' (λ- plain); K, ψ^k, ψ^t, (7.5.1) and the punctuation plain (both scans)",
    r"the statement in roman (no \underline, no \emph)", "underline", "high", None,
    "Exposé V continues the GLOBAL_ISSUES 82 pattern (as reported for pp. 330 and 351-355): not itemized, for the scripted per-exposé decision; the word groups are listed for that script.")
add(362, "proof of 7.5 i): 'd'où : d/dt(λ_t(1))/λ_t(1) = 1/1+t = Σ_{k=1}^∞(-1)^{k-1}t^{k-1}, et par suite :'",
    "the formula stands at the left margin of the next text line and the sentence goes on in the same line ', et par suite :' (both scans; wit_362_bot.png)",
    r"d'où : \[ ... \] et par suite : (a display)", "other", "medium",
    fx(r"d'où :¶\[¶  \frac{d}{dt}(\lambda_t(1))/\lambda_t(1)¶  =¶  \frac1{1+t}¶  =¶  \sum_{k=1}^{\infty}(-1)^{k-1}t^{k-1},¶\]¶et par suite :",
       r"d'où : \(\frac{d}{dt}(\lambda_t(1))/\lambda_t(1)=\frac1{1+t}=\sum_{k=1}^{\infty}(-1)^{k-1}t^{k-1}\), et par suite :"),
    r"Inline formula made a display (same kind of fix as pp. 351-352). Apply before the next entry: this edit keeps \frac1{1+t}, which the next entry then replaces (the next entry alone also works).")
add(362, "same formula, '1/1+t'",
    "1/1+t typed on the line with a solidus, no fraction bar, no parentheses (both scans; wit_362_bot.png)",
    r"\frac1{1+t}", "formula", "high",
    fx(r"\frac1{1+t}", r"1/1+t"),
    r"The typescript's notation (as 'X/1+Xt' on p. 363, which the TeX keeps); the TeX builds a fraction. The old string is unique before and after the inline entry above.")
add(362, "diagram (7.5.2), label of the middle vertical arrow",
    "the small circle ∘ stands to the left of the arrow Ĝ(K) x Ĝ(K) → Ĝ(K) (both scans; wit_362_bot.png)",
    r"\arrow[d,\"\circ\"] (label set to the right of the arrow)".replace('\\"', '"'), "formula", "medium",
    fx(r'\arrow[d,"\circ"]', r'\arrow[d,"\circ"' + "']"),
    "Label on the wrong side of the arrow.")
add(362, "diagram (7.5.2), labels of the two lower arrows",
    "λ_t and Φ^k above the lower arrows K → Ĝ(K) → K (both scans; wit_362_bot.png)",
    r'\arrow[r,"\lambda_t"' + "'] and " + r'\arrow[r,"\Phi^k"' + "'] (the ' sets the labels below the arrows)", "formula", "medium",
    fx(r'K \arrow[r,"\lambda_t"' + "'] &¶" + r'\widehat G(K) \arrow[r,"\Phi^k"' + "'] &",
       r'K \arrow[r,"\lambda_t"] &¶\widehat G(K) \arrow[r,"\Phi^k"] &'),
    "Labels on the wrong side of the arrows (as reported on pp. 41, 59, 74, 354, 369); the labels of the upper arrows stand as printed.")

# ---------------- p. 363 ----------------
add(363, "start of page (folio-363 marker)",
    "p. 363 begins 'un homomorphisme de groupes de Ĝ(K) dans K[[t]]'; p. 362 ends '... l'application \"dérivée logarithmique\" est' (both scans)",
    "'un' ends the last line of page_362.tex ('... « dérivée logarithmique » est un'), above the folio-363 marker; page_363.tex begins 'homomorphisme'",
    "marker", "high", None,
    r"The folio-363 marker stands one word late. Page 363 really begins at 'un homomorphisme'. Exact fix in main.tex (both layers, once each): replace '« dérivée logarithmique » est un\n%%%%%%%%%%  scan idx 376  |  folio 363  %%%%%%%%%%\nhomomorphisme de groupes' by '« dérivée logarithmique » est\n%%%%%%%%%%  scan idx 376  |  folio 363  %%%%%%%%%%\nun homomorphisme de groupes'. Simulated in memory on both layers with crops_361_365/sim_markers.py (one match each). Independent of the folio-362 move.")
add(363, "'Φ^k(1+Xt) = X^k ( (k-1)-ième coefficient de X/1+Xt ) ; Φ(1+Yt) = Y^k ;'",
    "Φ(1+Yt) = Y^k: no exponent k on this Φ (both scans; crops_361_365/p363_PhiY.png, wit_363_top.png)",
    r"\Phi^k(1+Yt)=Y^k (silently corrected)", "misprint_in_print", "high",
    fx(r"\Phi^k(1+Yt)=Y^k", r"\Phi(1+Yt)=Y^k"),
    "The k was not typed (Φ^k(1+Xt) = X^k just before it). The fix restores the printed reading.",
    corrected=r"\Phi^k(1+Yt)=Y^k")
add(363, "'Φ^k((1+Xt)∘(1+Yt)) = Φ^k(1+XYt) = (XY)^k = Φ^k(1+Xt)Φ^k(1+Yt), ce qui donne le résultat.'",
    "the formula stands at the left margin at ordinary line spacing and the sentence goes on in the same line ', ce qui donne' (both scans; wit_363_top.png)",
    r"\[ ... \Phi^k(1+Xt)\Phi^k(1+Yt), \] ce qui donne le résultat. (a display)", "other", "medium",
    fx(r"\[¶  \Phi^k\bigl((1+Xt)\circ(1+Yt)\bigr)¶  =¶  \Phi^k(1+XYt)¶  =¶  (XY)^k¶  =¶  \Phi^k(1+Xt)\Phi^k(1+Yt),¶\]¶ce qui donne",
       r"\(\Phi^k\bigl((1+Xt)\circ(1+Yt)\bigr)=\Phi^k(1+XYt)=(XY)^k=\Phi^k(1+Xt)\Phi^k(1+Yt)\), ce qui donne"),
    "Inline formula made a display (as p. 352). The line before (Φ^k(1+Xt) = X^k ... ; Φ(1+Yt) = Y^k ;) stands on a line of its own and is left as a display. Independent of the misprint entry above.")
add(363, "diagram (7.5.3), label of the lower arrow",
    "Φ^k above the lower arrow (both scans; crops_361_365/m363_bottomarrow.png, wit_363_bot.png)",
    r'K \arrow[r,"\Phi^k"' + "'] (the ' sets the label below the arrow)", "formula", "medium",
    fx(r'K \arrow[r,"\Phi^k"' + "']", r'K \arrow[r,"\Phi^k"]'),
    "Label on the wrong side of the arrow, as in (7.5.2); the other three labels stand as printed (λ_u above, Φ^{kk'} left, Φ^{k'}_u right). Independent of the arrow-direction entry below (fix null).")
add(363, "diagram (7.5.3), direction of the lower arrow K — Ĝ^t(K)",
    "the lower arrow points from K to Ĝ^t(K), arrowhead at the right (both scans; crops_361_365/m363_bottomarrow.png, wit_363_bot.png)",
    r'K \arrow[r,"\Phi^k"' + "'] &" + r" \widehat G^t(K), (printed direction kept)", "misprint_in_print", "high", None,
    "Φ^k is a map Ĝ(K) → K (the composite described on pp. 362-363), and the square states Φ^{kk'} = Φ^k∘Φ^{k'}_u∘λ_u, as the text then checks on 1+Xt: the lower arrow must point from Ĝ^t(K) to K. The TeX keeps the printed direction. For the corrected layer, replace the lower row 'K \\arrow[r,...] &' / '\\widehat G^t(K),' by the corrected reading (the ' keeps the label above a leftward arrow).",
    corrected=r'K &¶\widehat G^t(K), \arrow[l,"\Phi^k"' + "']")
add(363, "between '... = 1+X^{k'}t ;' and 'Φ^k(1+X^{k'}t) = X^{kk'} = Φ^{kk'}(1+Xt).'",
    "nothing between the two formula lines (both scans; wit_363_bot.png)",
    r"\]¶puis¶\[".replace('¶', ' / '), "extra", "high",
    fx(r"\]¶puis¶\[", r"\]¶\["),
    "Word added by the transcription.")
add(363, "before 'Par suite, ψ^{kk'} = ...'",
    "'Par suite,' begins a new, indented paragraph (both scans; wit_363_bot.png)",
    r"'Par suite,' follows the \] of the display before (same paragraph)", "other", "high",
    fx(r"Par suite,", r"¶Par suite,"),
    "Missing paragraph break. Order-free with the next entry (each old survives the other edit).")
add(363, "'Par suite, ψ^{kk'} = Φ^k∘Φ^{k'}_u∘λ_u∘λ_t = Φ^k∘ψ^{k'}∘λ_t .'",
    "the formula follows 'Par suite,' in the same line, then the full stop (both scans; crops_361_365/p363_parsuite_start.png)",
    r"Par suite, \[ \psi^{kk'} = ... \] (a display)", "other", "medium",
    fx(r"Par suite,¶\[¶  \psi^{kk'}¶  =¶  \Phi^k\circ\Phi^{k'}_u\circ\lambda_u\circ\lambda_t¶  =¶  \Phi^k\circ\psi^{k'}\circ\lambda_t.¶\]",
       r"Par suite, \(\psi^{kk'}=\Phi^k\circ\Phi^{k'}_u\circ\lambda_u\circ\lambda_t=\Phi^k\circ\psi^{k'}\circ\lambda_t\)."),
    "Inline in the print, display in the TeX (as 'Enfin,' p. 351).")
add(363, "before 'Par ailleurs, ψ^k∘ψ^{k'} = ...'",
    "'Par ailleurs,' begins a new, indented paragraph (both scans; crops_361_365/p363_parailleurs.png)",
    r"'Par ailleurs,' follows the \] of the display before (same paragraph)", "other", "high",
    fx(r"Par ailleurs,", r"¶Par ailleurs,"),
    "Missing paragraph break. Order-free with the next entry and with the 'Par suite' entries.")
add(363, "'Par ailleurs, ψ^k∘ψ^{k'} = Φ^k∘λ_t∘Φ^{k'}∘λ_t = Φ^k∘λ_t∘ψ^{k'}.'",
    "the formula follows 'Par ailleurs,' in the same line, then the full stop (both scans; crops_361_365/p363_parailleurs.png)",
    r"Par ailleurs, \[ \psi^k\circ\psi^{k'} = ... \] (a display)", "other", "medium",
    fx(r"Par ailleurs,¶\[¶  \psi^k\circ\psi^{k'}¶  =¶  \Phi^k\circ\lambda_t\circ\Phi^{k'}\circ\lambda_t¶  =¶  \Phi^k\circ\lambda_t\circ\psi^{k'}.¶\]",
       r"Par ailleurs, \(\psi^k\circ\psi^{k'}=\Phi^k\circ\lambda_t\circ\Phi^{k'}\circ\lambda_t=\Phi^k\circ\lambda_t\circ\psi^{k'}\)."),
    "Inline in the print, display in the TeX.")

# ---------------- p. 364 ----------------
add(364, "start of page, 'Or si K est un λ-anneau, le diagramme :'",
    "'Or si' is indented: a new paragraph after the display that ends p. 363 (both scans; wit_364_top.png)",
    r"'Or si' follows the last \] of p. 363 with only the marker line between", "other", "high",
    fx(r"Or si \(K\) est un", r"¶Or si \(K\) est un"),
    "Paragraph break of the print missing; the blank line comes after the marker line (as p. 349). Independent of the next entry.")
add(364, "same line, 'λ-anneau'",
    "λ-anneau in one piece (both scans)",
    r"'\(\lambda\)-' at the end of a line, 'anneau' on the next: prints 'λ- anneau' with a space", "other", "high",
    fx(r"\(\lambda\)-¶anneau", r"\(\lambda\)-anneau"),
    "A line end left inside the word (probably by an earlier marker split) becomes a space.")
add(364, "diagram (7.5.4), label of the lower arrow",
    "λ_t above the lower arrow K → Ĝ(K), as above the upper one (both scans; wit_364_top.png)",
    r'K \arrow[r,"\lambda_t"' + "'] (the ' sets the label below the arrow)", "formula", "medium",
    fx(r'K \arrow[r,"\lambda_t"' + "']", r'K \arrow[r,"\lambda_t"]'),
    "Label on the wrong side of the arrow, as in (7.5.2) and (7.5.3); the other three labels stand as printed.")
add(364, "before 'Enfin, la relation λ_t(1) = 1+t s'obtient par intégration'",
    "'Enfin,' begins a new, indented paragraph (both scans; wit_364_bot.png)",
    r"'... \(\psi^{kk'}=\psi^k\circ\psi^{k'}\). Enfin, ...' in one paragraph", "other", "high",
    fx(r" Enfin, la relation", r"¶¶Enfin, la relation"),
    "Missing paragraph break.")
add(364, "heading of the bibliography",
    "BIBLIOGRAPHIE: typed capitals, underlined (both scans)",
    r"\subsection*{Bibliographie}", "word", "medium",
    fx(r"\subsection*{Bibliographie}", r"\subsection*{BIBLIOGRAPHIE}"),
    "As the headings fixed on pp. 19, 159, 220, 273 and 296; the missing underline of a section title is accepted.")
add(364, "bibliography [1] Grothendieck, title",
    "'La théorie des classes de Chern,' typed plain, not underlined (both scans; crops_361_365/m364_items.png, wit_364_bot.png)",
    r"\emph{La théorie des classes de Chern}", "font", "high",
    fx(r"\emph{La théorie des classes de Chern}", r"La théorie des classes de Chern"),
    "The typescript neither underlines nor italicizes the titles of this bibliography; same fix as pp. 19, 159, 273, 296.")
add(364, "bibliography [2] Hirzebruch, title",
    "'Neue topologische Methoden in der algebraischen Geometrie.' typed plain, not underlined (both scans)",
    r"\emph{Neue topologische Methoden in der algebraischen Geometrie}", "font", "high",
    fx(r"\emph{Neue topologische Methoden in der algebraischen Geometrie}", r"Neue topologische Methoden in der algebraischen Geometrie"),
    "As [1].")

# ---------------- p. 365 ----------------
add(365, "heading of Exposé VI",
    "three blocks: 'Exposé VI' (small letters, underlined, no full stop) at the left; the title on two centred lines 'LE K˙ D'UN FIBRE PROJECTIF :' / 'CALCULS ET CONSEQUENCES', typed capitals with a double underline (both scans; wit_365_top.png)",
    r"\section*{Exposé VI. Le \(K^{\bullet}\) d'un fibré projectif : calculs et conséquences}", "word", "medium",
    fx(r"\section*{Exposé VI. Le \(K^{\bullet}\) d'un fibré projectif : calculs et conséquences}",
       r"\section*{\underline{Exposé VI}\\[3pt] \underline{\underline{LE \(K^{\bullet}\) D'UN FIBRÉ PROJECTIF :}}\\[3pt] \underline{\underline{CALCULS ET CONSÉQUENCES}}}"),
    "The TeX joins the lines with an added full stop and sets the title in small letters. Same form as the applied headings of Exposés II-V and the two-line title of Exposé I (main.tex line 1774); É keeps the TeX's accents (rule for typed capitals).")
add(365, "author line of the heading",
    "'par Pierre BERTHELOT': the name in capitals, the line underlined (both scans)",
    "par Pierre Berthelot", "word", "medium",
    fx("par Pierre Berthelot", r"\underline{par Pierre BERTHELOT}"),
    r"As the applied author lines of Exposés I-V (\underline{par P. BERTHELOT}, p. 297); here the first name is written out.")
add(365, "Théorème 1.1, 'définit un homomorphisme d'anneaux : K˙(S) →^{f*} K˙(X) munissant'",
    "the formula follows 'd'anneaux :' in the same text line; 'munissant' begins the next line at the margin (both scans; wit_365_top.png)",
    r"d'anneaux : \[ K^{\bullet}(S) \xrightarrow{f^*} K^{\bullet}(X) \] munissant (a display)", "other", "medium",
    fx(r"d'anneaux :¶\[¶  K^{\bullet}(S) \xrightarrow{f^*} K^{\bullet}(X)¶\]¶munissant",
       r"d'anneaux : \(K^{\bullet}(S) \xrightarrow{f^*} K^{\bullet}(X)\) munissant"),
    "Inline formula made a display (as pp. 351-352).")
add(365, "Plan b), '0 → L_{r+1} →... → L_o → M → 0'",
    "typed baseline dots between the arrows (both scans; wit_365_bot.png)",
    r"\longrightarrow\cdots\longrightarrow", "symbol", "low",
    fx(r"\longrightarrow\cdots\longrightarrow", r"\longrightarrow\ldots\longrightarrow"),
    r"GLOBAL_ISSUES 87 leaves the \cdots for the typed baseline dots to a volume decision (Exposé V, itemized on pp. 298-299); this is the same case in Exposé VI. Drop if that decision keeps \cdots.")
add(365, "Plan a), 'il existe un S(E)-Module module gradué M'",
    "'Module module': the word typed twice (both scans; wit_365_bot.png)",
    r"\(\Sym(E)\)-Module module gradué (printed reading kept)", "misprint_in_print", "high", None,
    "Doubled word of the typescript; the diplomatic layer is right.",
    corrected=r"il existe un \(\Sym(E)\)-Module gradué \(M\)")
add(365, "Plan a), '(S(E) étant l'algèbre symétrique de E ; pour la notation Proj_o, voir EGA II 8.12.1 .'",
    "no closing parenthesis before the final full stop (both scans; crops_361_365/m365_ega.png, wit_365_bot.png)",
    r"voir EGA II 8.12.1. (printed reading kept)", "misprint_in_print", "medium", None,
    "The parenthesis opened at '(S(E) étant' is never closed; the TeX keeps the printed reading.",
    corrected=r"voir EGA II 8.12.1).")
add(365, "Théorème 1.1 (the statement)",
    "underlined word groups: 'Soient', 'un schéma quasi-compact', 'un', '-Module localement libre de rang', 'le fibré projectif associé', 'le morphisme structural', 'définit un homomorphisme d'anneaux', 'munissant', 'd'une structure de', 'algèbre', 'Soit', 'la classe du faisceau', 'Alors', 'est un', 'module libre admettant pour base'; S, r+1, X, the formulas, K˙(X), K˙(S)-, ξ ∈ K˙(X), 1,...,ξ^r and the punctuation plain (the letters E, O_S, P(E), O_X carry their own underlines) (both scans)",
    r"the statement in roman (no \underline, no \emph)", "underline", "high", None,
    "Exposé VI follows the GLOBAL_ISSUES 82 pattern from its first statement (as findings_366_370 for pp. 367-370): not itemized, for the scripted per-exposé decision; the word groups are listed for that script.")
add(365, "sheaf letters of pp. 365 (Théorème 1.1 and the plan a)-c))",
    "underlined: E (7 times: 'E un', P(E), S(E) four times, 'de E'), F (twice), M (4 times), L_i (twice), L_{r+1}, L_o, N_j (twice); the S of S(E) and the P of P(E) doubly underlined; S, X, r, j plain (both scans)",
    r"plain \(E\), \(F\), \(M\), \(L_i\), \(L_{r+1}\), \(L_0\), \(N_j\); \Sym and \mathbf P give the bold S and P as printed", "underline", "high", None,
    "Convention of the Exposé VI transcription, reported once in findings_366_370 (p. 366 entry, with three example edits); the p. 365 letters listed for the same script. The underlined O of O_S, O_X is the pending structure-sheaf decision (not itemized).")

# ---------------- checks ----------------
pages = {}
for p in sorted({d['page'] for d in F}):
    pages[p] = open(RUN + 'b361_365/page_%03d.tex' % p, encoding='utf-8').read()
ok = True
cur = dict(pages)
for d in F:
    fix = d['fix']
    if not fix:
        continue
    p = d['page']
    n0 = pages[p].count(fix['old'])
    n1 = cur[p].count(fix['old'])
    if '%%%%%%%%%%' in fix['old'] or '%%%%%%%%%%' in fix['new']:
        print('MARKER IN FIX', p, d['where']); ok = False
    if n0 != 1 or n1 != 1:
        print('COUNT', p, n0, n1, repr(fix['old'][:60])); ok = False
    cur[p] = cur[p].replace(fix['old'], fix['new'], 1)
for d in F:
    if d['kind'] == 'misprint_in_print' and 'corrected' not in d:
        print('NO CORRECTED', d['page'], d['where']); ok = False
    if d['kind'] != 'misprint_in_print' and 'corrected' in d:
        print('CORRECTED ON NON-MISPRINT', d['page']); ok = False
print('all olds unique (original and in order):', ok, ' findings:', len(F))
from collections import Counter
c = Counter((d['page'], d['kind'] == 'misprint_in_print') for d in F)
for p in sorted(pages):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
if ok and '--write' in sys.argv:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('written', OUT)
