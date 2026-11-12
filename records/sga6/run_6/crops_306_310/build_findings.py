"""Build findings_306_310.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6')
B = RUN / 'b306_310'
NL = '\n'


def M(folio, idx):
    return '%%%%%%%%%%  scan idx ' + str(idx) + '  |  folio ' + str(folio) + '  %%%%%%%%%%'


F = []

# ---------------------------------------------------------------- page 306
F.append(dict(
    page=306, where='start of page',
    scan=r"p. 306 begins '(1+X^{(j)}t)_{j=1,..,k} de (Ĝ(K[(X^{(j)})_j]))^k; un élément θ de H(K[(X^{(j)})_j]) déter-mine'; p. 305 ends '... ils sont déterminés par leur valeur pour l'élément' (both scans)",
    tex=r"in the batch file the line '\((1+X^{(j)}t)_{j=1,\ldots,k}\) de \(\bigl(\Ghat(K[(X^{(j)})_j])\bigr)^k\)~; un' is the last line under the folio-305 marker; page_306.tex begins 'élément \(\theta\)'",
    kind='marker', confidence='high', fix=None,
    note=r"ALREADY DONE, no action: reported by findings_301_305.json (p. 305, page end) and applied; the live main.tex has the folio-306 marker above that line in both layers (checked 21:16). The moved line differs from the print once: see the next entry."))
F.append(dict(
    page=306, where=r"first line (the line moved above), index 'j=1,..,k' of (1+X^{(j)}t)",
    scan=r"'j=1,..,k': two typed stops between the commas (both scans; crops_306_310/c306_dots.png, w306_dots2.png)",
    tex=r"_{j=1,\ldots,k} (silently corrected)",
    kind='misprint_in_print', confidence='medium', fix=None,
    corrected=r"_{j=1,\ldots,k}",
    note=r"Two stops for the ellipsis, as the misprints recorded on pp. 37 and 50 (x^1,..,x^j; F,..,F). fix is null only because this line is not in page_306.tex of the batch (it now stands under the folio-306 marker of the live main.tex): apply by hand in the diplomatic layer only: '_{j=1,\ldots,k}\) de \(\bigl(\Ghat' -> '_{j=1,..,k}\) de \(\bigl(\Ghat' (once in main.tex). The rest of the line agrees with the print (findings_301_305 checked it)."))
F.append(dict(
    page=306, where="relations after 'Ces foncteurs vérifient les relations suivantes'",
    scan=r"'g∘i = Id ; Ĝ∘i∘g = Ĝ_g ; Ĝ_g∘i∘g = Ĝ_g (cf. 1.3,ex.2)' on one line, no full stop after the reference (both scans; crops_306_310/c306_cf.png)",
    tex=r"(cf. 1.3, ex. 2).",
    kind='punctuation', confidence='high',
    fix={'old': r'(cf. 1.3, ex. 2).', 'new': r'(cf. 1.3, ex. 2)'},
    note="The TeX adds a full stop. The reference set on the line after the display is left as layout."))
F.append(dict(
    page=306, where=r"Lemme 1.9 (pp. 306-307) and the other statements of pp. 306-310",
    scan=r"the typescript underlines the statements word group by word group: Lemme 1.9 'Soit', 'un foncteur sur', 'alors l'homomorphisme canonique', 'est un isomorphisme' (top of p. 307); Théorème 1.10 (pp. 307-308), Lemme 1.12 (p. 309) and Théorème 1.13 (p. 310) the same; formulas, label numbers and the final punctuation are not underlined",
    tex="the statements in roman (Exposé V has no underline markup)",
    kind='underline', confidence='high', fix=None,
    note=r"Exposé V follows the Exposé II pattern of GLOBAL_ISSUES 82 (also reported for p. 298 in findings_296_300.json): not itemized, for the scripted per-exposé decision. No \emph on defined terms and no category L on pp. 306-310."))
F.append(dict(
    page=306, where=r"Lemme 1.9, 'H : C_o → Ab fil', and the display Hom_{Ab fil}(Ĝ,H∘g) → Hom_{Ab fil}(Ĝ∘i,H)",
    scan=r"'Ab' and 'fil' each underlined, without stops, in all nine places of pp. 306-310 (p. 306 three, p. 307 one, p. 308 one, p. 309 three, p. 310 one; both scans)",
    tex=r"\Abfil, defined in the Exposé V macro block as \mathrm{Ab\,fil}: no underline",
    kind='underline', confidence='high', fix=None,
    note=r"Convention of the Exposé V transcription, reported once (p. 299 was fixed in the text by findings_296_300.json). Three examples: p. 306 '\(H:\mathcal C_0\to\Abfil\)'; p. 307 '\Hom_{\Abfil}(\Ghat\circ i,H)'; p. 309 '\(H:\mathcal C_g\to\Abfil\)'. Global fix, both layers: \providecommand{\Abfil}{\underline{\mathrm{Ab}}\,\underline{\mathrm{fil}}} (13 uses left: folios 301, 306-311; spot-check 301 and 311)."))

# ---------------------------------------------------------------- page 307
F.append(dict(
    page=307, where=r"diagram of the proof of 1.9, bottom arrow Ĝ(A_g) → H∘g(A_g)",
    scan=r"the label Φ_{A_g} stands above the bottom arrow, as Φ_A above the top one (both scans; crops_306_310/c307_diag.png)",
    tex=r"""\arrow[r,"\Phi_{A_g}"'] (the ' sets the label below the arrow)""",
    kind='formula', confidence='medium',
    fix={'old': r"""\arrow[r,"\Phi_{A_g}"']""", 'new': r"""\arrow[r,"\Phi_{A_g}"]"""},
    note="Label on the wrong side of the arrow (as reported on pp. 41, 59, 74, 304)."))

# ---------------------------------------------------------------- page 308
F.append(dict(
    page=308, where='start of page',
    scan=r"p. 308 begins 'sa valeur sur l'élément 1+Xt de Ĝ∘i(K[X]), est injective'; p. 307 ends '... qui, à un morphisme de foncteurs, associe' (both scans)",
    tex=r"'sa' ends the last line of page_307.tex ('... associe sa'), above the folio-308 marker; page_308.tex begins 'valeur sur l'élément'",
    kind='marker', confidence='high', fix=None,
    note=r"The folio-308 marker stands one word late. Page 308 really begins at 'sa valeur'. Exact fix in main.tex (both layers): replace 'associe sa\n" + M(308, 321) + r"\nvaleur sur' by 'associe\n" + M(308, 321) + r"\nsa valeur sur' (simulated on both layers of the live main.tex: once in each). marker_split_word.py pull 'sa' would give 'savaleur' without a space; move_marker.py 6 308 sa --before also works but leaves 'sa' on a line of its own."))
F.append(dict(
    page=308, where=r"last line, 'en associant à la série 1+...+a_nt^n+...,'",
    scan=r"typed stops on the baseline: '1+...+a_nt^n+...,' (both scans)",
    tex=r"\(1+\cdots+a_nt^n+\cdots\)",
    kind='symbol', confidence='medium',
    fix={'old': r'\(1+\cdots+a_nt^n+\cdots\)', 'new': r'\(1+\ldots+a_nt^n+\ldots\)'},
    note=r"\cdots sets the dots at mid-height; the typescript has baseline stops (same fix as pp. 298-299, findings_296_300.json)."))
F.append(dict(
    page=308, where=r"'la série 1+...+ā_n+..., où ā_n est la classe de a_n dans Gr^nA' (printed as the first line of p. 309)",
    scan=r"baseline stops '1+...+ā_n+...,' (both scans)",
    tex=r"\(1+\cdots+\bar a_n+\cdots\) (still under the folio-308 marker: see the p. 309 marker entry)",
    kind='symbol', confidence='medium',
    fix={'old': r'\(1+\cdots+\bar a_n+\cdots\)', 'new': r'\(1+\ldots+\bar a_n+\ldots\)'},
    note=r"As the previous entry. Printed on p. 309; listed under page 308 because the text stands there in the batch files. If the folio-309 marker is moved before this batch is processed, apply it on page 309 (the old text is unique there too)."))
F.append(dict(
    page=308, where=r"before 'Soit B ∈ Ob(G) ; on notera 1+B̂^+'",
    scan=r"'Soit' is indented: a new paragraph after 'Il existe un isomorphisme de foncteurs ε : Id ⥲ Gr∘j.' (both scans)",
    tex=r"'... \operatorname{Gr}\circ j\).' and 'Soit \(B\in ...' on consecutive lines: one paragraph",
    kind='other', confidence='medium',
    fix={'old': r'\circ j\).' + NL + 'Soit', 'new': r'\circ j\).' + NL + NL + 'Soit'},
    note="Paragraph break of the print missing."))
F.append(dict(
    page=308, where=r"before 'Par ailleurs, on définit pour tout A ∈ Ob(C)'",
    scan=r"'Par ailleurs' is indented: a new paragraph after '... un foncteur : G → Ab fil.' (both scans)",
    tex=r"'... \(\mathcal C_g\to\Abfil\). Par ailleurs, on définit' in one paragraph",
    kind='other', confidence='medium',
    fix={'old': '. Par ailleurs, on définit', 'new': '.' + NL + NL + 'Par ailleurs, on définit'},
    note="Paragraph break of the print missing."))
F.append(dict(
    page=308, where=r"1.11 and after: the category of graded K-algebras",
    scan=r"a hand-drawn script G: a C-like letter whose stroke runs into a long descender, the whole letter drawn by hand, distinct from the C beside it in 'C → G' (both scans; crops_306_310/c308_teur.png, w308_id.png, w308_notera.png): 'On notera G la catégorie des K-algèbres graduées', 'le foncteur de G dans C', 'C → G', 'Id_G', 'Ob(G)', 'G → Ab fil' (p. 308), Lemme 1.12 twice (p. 309, the descenders faint), Théorème 1.13 (p. 310)",
    tex=r"\mathcal C_g (C with an index g) in all nine places of pp. 308-310",
    kind='symbol', confidence='high', fix=None,
    note=r"Convention of the Exposé V transcription, reported once: 16 \mathcal C_g in main.tex (both layers), folios 308 (6), 309 (2), 310 (1), 311 (3), 313 (1), 345 (2), 347 (1); the exposé has no \mathcal G (its macro block defines \cG = \mathcal G, unused). Not C with an index: the C_o of K-algebras carries a typed o, while here nothing is typed, and the small letter of Id_G has the same shape. Three examples: p. 308 'On notera \(\mathcal C_g\) la catégorie des \(K\)-algèbres graduées'; p. 308 '\operatorname{Id}_{\mathcal C_g}'; p. 309 Lemme 1.12 '\(H:\mathcal C_g\to\Abfil\)'. Global fix, both layers: \mathcal C_g -> \mathcal G in Exposé V (look at folios 345 and 347 first)."))

# ---------------------------------------------------------------- page 309
F.append(dict(
    page=309, where='start of page',
    scan=r"p. 309 begins 'la série 1+...+ā_n+..., où ā_n est la classe de a_n dans Gr^nA. Son noyau est le groupe Ĝ'(A)'; p. 308 ends '... en associant à la série 1+...+a_nt^n+...,' (both scans)",
    tex=r"page_308.tex ends ', la série \(1+\cdots+\bar a_n+\cdots\), où \(\bar a_n\) est la classe de \(a_n\) dans \(\operatorname{Gr}^nA\). Son' above the folio-309 marker; page_309.tex begins 'noyau est le groupe'",
    kind='marker', confidence='high', fix=None,
    note=r"Page 309 really begins at 'la série \(1+\cdots+\bar a_n'. python -I move_marker.py 6 309 'la série' --before (the last 'la série' before the marker; simulated on both layers of the live main.tex: '... en associant à la série \(1+\cdots+a_nt^n+\cdots\), ', the marker, 'la série \(1+\cdots+\bar a_n+\cdots\), où ... Son', 'noyau est ...'). The command does not depend on the \ldots entries of p. 308; an exact replacement written now would (it contains the \cdots of the moved text)."))
F.append(dict(
    page=309, where=r"display of the composite that defines ρ, middle term",
    scan=r"'Hom(1+\widehat{Gr.}^+,H∘Gr)': the hat covers 'Gr.', no parentheses around the dot (both scans; crops_306_310/c309_compose.png)",
    tex=r"\Hom(1+\widehat{\operatorname{Gr}(\,\cdot\,)}^{+},H\circ\operatorname{Gr})",
    kind='extra', confidence='high',
    fix={'old': r'1+\widehat{\operatorname{Gr}(\,\cdot\,)}^{+},H', 'new': r'1+\widehat{\operatorname{Gr}\,\cdot\,}^{+},H'},
    note=r"The TeX adds parentheses Gr(·); the print has Gr followed by the dot, here and in the three places below (pp. 309, 310). The dot itself is a typed stop on the baseline, written \,\cdot\, in all 17 placeholder places of folios 309-313: left as the transcription's form."))
F.append(dict(
    page=309, where=r"'la dernière flèche étant définie par l'homomorphisme Ĝ → 1+\widehat{Gr.}^+'",
    scan=r"'1+\widehat{Gr.}^+', no parentheses (both scans; crops_306_310/c309_derniere.png)",
    tex=r"\widehat{\operatorname{Gr}(\,\cdot\,)}^{+}",
    kind='extra', confidence='high',
    fix={'old': r"l'homomorphisme \(\Ghat\longrightarrow1+\widehat{\operatorname{Gr}(\,\cdot\,)}", 'new': r"l'homomorphisme \(\Ghat\longrightarrow1+\widehat{\operatorname{Gr}\,\cdot\,}"},
    note="As the previous entry."))
F.append(dict(
    page=309, where=r"end of the same sentence, before 'On va construire'",
    scan=r"no full stop after 1+\widehat{Gr.}^+ (the stop under the hat is the placeholder dot); the line ends there (both scans; crops_306_310/c309_derniere.png)",
    tex=r"...\widehat{\operatorname{Gr}(\,\cdot\,)}^{+}\).",
    kind='punctuation', confidence='high',
    fix={'old': r'^{+}\).' + NL, 'new': r'^{+}\)' + NL},
    note="The TeX adds a full stop. Independent of the previous and the next entry (any order)."))
F.append(dict(
    page=309, where=r"before 'On va construire un morphisme en sens inverse'",
    scan=r"'On va construire' is indented: a new paragraph (both scans)",
    tex="the line follows 'la dernière flèche ...' with no blank line: one paragraph",
    kind='other', confidence='medium',
    fix={'old': NL + 'On va construire', 'new': NL + NL + 'On va construire'},
    note="Paragraph break of the print missing."))
F.append(dict(
    page=309, where=r"'se factorise par le morphisme canonique Ĝ → 1+\widehat{Gr.}^+, ce qui équivaut'",
    scan=r"'1+\widehat{Gr.}^+,' no parentheses (both scans)",
    tex=r"\widehat{\operatorname{Gr}(\,\cdot\,)}^{+}",
    kind='extra', confidence='high',
    fix={'old': r"canonique \(\Ghat\longrightarrow1+\widehat{\operatorname{Gr}(\,\cdot\,)}", 'new': r"canonique \(\Ghat\longrightarrow1+\widehat{\operatorname{Gr}\,\cdot\,}"},
    note="As the first Gr entry of the page."))
F.append(dict(
    page=309, where=r"before 'Soient A ∈ Ob(C), χ ∈ Ĝ'(A)'",
    scan=r"'Soient' is indented: a new paragraph after 'd'après 1.11.' (both scans)",
    tex=r"'... d'après 1.11. Soient \(A\in ...' in one paragraph",
    kind='other', confidence='medium',
    fix={'old': "d'après 1.11. Soient", 'new': "d'après 1.11." + NL + NL + 'Soient'},
    note="Paragraph break of the print missing."))

# ---------------------------------------------------------------- page 310
F.append(dict(
    page=310, where='start of page',
    scan=r"p. 310 begins 'K-algèbres filtrées K[X_i]_{i≥1} → A en envoyant X_1 sur 0'; p. 309 ends '... ; on définit un homomorphisme de' (both scans)",
    tex=r"'\(K\)-' ends the last line of page_309.tex ('on définit un homomorphisme de \(K\)-'), above the folio-310 marker; page_310.tex begins 'algèbres filtrées'",
    kind='marker', confidence='high', fix=None,
    note=r"Page 310 really begins with '\(K\)-algèbres'. python -I marker_split_word.py 6 310 pull '\(K\)-' (simulated on both layers of the live main.tex: '... un homomorphisme de', the marker, '\(K\)-algèbres filtrées ...'). Exact replacement (both layers): 'homomorphisme de \(K\)-\n" + M(310, 323) + r"\nalgèbres filtrées' -> 'homomorphisme de\n" + M(310, 323) + r"\n\(K\)-algèbres filtrées'. This also removes the space that the line end now puts between 'K-' and 'algèbres'."))
F.append(dict(
    page=310, where=r"'s'annule pour l'élément 1+X_2t+...+X_{n+1}t^n+... .'",
    scan=r"baseline stops '1+X_2t+...+X_{n+1}t^n+...' (both scans)",
    tex=r"\(1+X_2t+\cdots+X_{n+1}t^n+\cdots\)",
    kind='symbol', confidence='medium',
    fix={'old': r'\(1+X_2t+\cdots+X_{n+1}t^n+\cdots\)', 'new': r'\(1+X_2t+\ldots+X_{n+1}t^n+\ldots\)'},
    note=r"\cdots for baseline stops, as on p. 308."))
F.append(dict(
    page=310, where=r"'un morphisme de foncteurs : 1+\widehat{Gr.}^+ → H∘Gr'",
    scan=r"'1+\widehat{Gr.}^+', no parentheses (both scans)",
    tex=r"\widehat{\operatorname{Gr}(\,\cdot\,)}^{+}",
    kind='extra', confidence='high',
    fix={'old': r'\widehat{\operatorname{Gr}(\,\cdot\,)}', 'new': r'\widehat{\operatorname{Gr}\,\cdot\,}'},
    note="As on p. 309 (the TeX adds the parentheses)."))
F.append(dict(
    page=310, where='end of page',
    scan=r"p. 310 ends '... qui, à un morphisme de foncteurs, associe sa valeur sur l'élément'; p. 311 begins '1+X de 1+\widehat{K[X]}^+ est injective ; son image' (main scan of p. 310; witness of p. 311, crops_306_310/w_322_small.png)",
    tex=r"page_310.tex ends 'associe sa valeur sur l'élément \(1+X\) de \(1+\widehat{K[X]}^+\) est': '\(1+X\) de \(1+\widehat{K[X]}^+\) est' stands under the folio-310 marker",
    kind='marker', confidence='high', fix=None,
    note=r"Page 311 really begins with '\(1+X\) de'. python -I move_marker.py 6 311 '\(1+X\) de' --before (simulated on both layers of the live main.tex: '... associe sa valeur sur l'élément ', the marker, '\(1+X\) de \(1+\widehat{K[X]}^+\) est', 'injective; ...'). Exact replacement (both layers): 'l'élément \(1+X\) de \(1+\widehat{K[X]}^+\) est\n" + M(311, 324) + r"\n' -> 'l'élément\n" + M(311, 324) + r"\n\(1+X\) de \(1+\widehat{K[X]}^+\) est\n'. The checker of p. 311 may report the same boundary: apply once."))

# ---------------------------------------------------------------- checks
ok = True
order = ['page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'corrected', 'note']
out = []
for x in F:
    if x['kind'] != 'misprint_in_print':
        x.pop('corrected', None)
    out.append({k: x[k] for k in order if k in x})
    fx = x.get('fix')
    if fx:
        t = (B / f"page_{x['page']}.tex").read_text(encoding='utf-8')
        n = t.count(fx['old'])
        if n != 1 or '%%%%%%%%%%  scan idx' in fx['old'] or '%%%%%%%%%%  scan idx' in fx['new']:
            ok = False
        print(x['page'], x['kind'], 'old count', n, repr(fx['old'])[:70])
        if any(ord(c) < 32 and c != '\n' for c in fx['old'] + fx['new']):
            ok = False
            print('   CONTROL CHARACTER')
for x in out:
    for k in ('scan', 'tex', 'note', 'where'):
        if any(ord(c) < 32 for c in x[k]):
            ok = False
            print('control char in', x['page'], k)
print('all fixes unique:', ok, '| entries:', len(out))
from collections import Counter
c = Counter((x['page'], x['kind'] == 'misprint_in_print') for x in out)
print({p: (c[(p, False)], c[(p, True)]) for p in range(306, 311)})
if ok:
    (RUN / 'findings_306_310.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')
    print('written')
