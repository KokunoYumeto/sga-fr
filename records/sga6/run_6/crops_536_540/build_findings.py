"""Build findings_536_540.json and check that every fix's 'old' occurs exactly once in its page_NNN.tex."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6')
B = RUN / 'b536_540'
OUT = RUN / 'findings_536_540.json'
NL = '\n'
C = 'crops_536_540/'

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind, 'confidence': confidence, 'fix': fix}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


# ---------------------------------------------------------------- page 536
add(536, 'start of page (folio-536 marker)',
    "p. 536 begins 'Proposition 2.3.1. Pour tout schéma propre X sur k, ...' (both scans). The line 'Poincaré χ(F) ∈ Z de F sur X. De 2.2.1 on conclut immédiatement :' is the end of p. 535 (witness p. 535 ends '... la caractéristique d'Euler-Poincaré χ(F) ∈ Z de F sur X . / De 2.2.1 on conclut immédiatement :')",
    r"page_536.tex begins 'Poincaré $\chi(F)\in\mathbb Z$ de $F$ sur $X$. De 2.2.1 on conclut immédiatement :'; page 535 ends '... la caractéristique d'Euler-' directly above the marker",
    'marker', 'high', None,
    r"Page 536 really begins at '\textbf{Proposition 2.3.1.}'. Exact fix in main.tex (both layers): move the folio-536 marker line down past the line 'Poincaré $\chi(F)\in\mathbb Z$ de $F$ sur $X$. De 2.2.1 on conclut immédiatement :' and the blank line after it, so that it stands directly above '\textbf{Proposition 2.3.1.}'; 'd'Euler-' and 'Poincaré' then meet again under folio 535. The marker stands one TeX line too early (it splits the word Euler-Poincaré).")

add(536, "end of 2.3: 'parfois appellé polynôme de Snapper pour F'",
    "'polynôme de Snapper' underlined (both scans)",
    r"plain 'polynôme de Snapper'",
    'underline', 'high',
    {'old': r'polynôme de Snapper pour $F$', 'new': r'\emph{polynôme de Snapper} pour $F$'},
    r"Defined term underlined in the print; Exposé X writes such terms with \emph (\emph{nombre de Chern}, \emph{nombre d'intersection}).")

add(536, "end of 2.3: 'parfois appellé polynôme de Snapper'",
    "'appellé' (both scans)",
    "'appellé' (keeps the printed reading)",
    'misprint_in_print', 'high', None,
    "Typing error (appeler: appelé). The TeX keeps the printed reading.",
    corrected='appelé')

add(536, "Prop. 2.3.1, second display 'cl_P(L) ⇝ g_*(cl˙(L)y) = χ(cl˙(L)y'",
    "the display ends 'χ(cl˙(L)y' with no closing parenthesis (both scans; " + C + "p536_disp2.png, w536_disp2.png)",
    r"=\chi(\cl^\circ(L)y)",
    'misprint_in_print', 'high',
    {'old': r'(L)y)' + NL + r'\]', 'new': r'(L)y' + NL + r'\]'},
    r"The TeX silently adds the closing parenthesis; the fix restores the printed reading (only the final ')' is concerned; the raised dot of cl is the separate \circ item below).",
    corrected=r"=\chi(\cl^\circ(L)y)")

add(536, "Prop. 2.3.1, first display 'S_y : Pic(X) → Z ↪ Q'",
    "capital S in S_y (both scans; " + C + "p536_Sy.png)",
    r"S_y:\Pic(X)\longrightarrow\mathbb Z\hookrightarrow\mathbb Q (keeps the printed capital)",
    'misprint_in_print', 'low', None,
    "The same map is s_y with a small s everywhere else: p. 538 'L'application polynôme s_y (2.3.1)', the diagram and 'correspondant à s_y' (" + C + "p538_sy.png); the TeX has S_y only here. Low confidence: the capital may be meant.",
    corrected=r's_y')

add(536, "2.4, 'le foncteur de Picard Pic_{X/k} de X sur k'",
    "'Pic' with a wavy underline (both scans; " + C + "p536_Picwavy.png)",
    r"$\Pic_{X/k}$ (plain)",
    'underline', 'medium',
    {'old': r'Picard $\Pic_{X/k}$', 'new': r'Picard $\mathbf{Pic}_{X/k}$'},
    r"The typescript marks the Picard functor with a wavy underline (the typist's sign for bold: here and p. 537 'on sait [4] que Pic°_{X/k}') and the Picard scheme with a straight underline (p. 537, six places); Pic(X), the Pic_{X/k}(Spec(k)) of this page and the Pic_{X/k} of Remarque 2.4.5 (p. 538) are plain. \mathbf{Pic} keeps the print's wavy/straight distinction; if the volume wants one form, use \underline{\Pic}, the form of Exp. XIII (whose print underlines its Pic_{X/S} straight, witness p. 631). The TeX has no other \Pic_{X/k} or \Pic^0_{X/k} in Exposé X than those of pp. 536-538.")

add(536, r"local macro block at the end of page_536.tex: \providecommand{\Gro}{\operatorname{Gr}^{\circ}}; \Gro is used for the print's Gr˙ on p. 538 (1), p. 539 (5), p. 540 (4)",
    "Gr with a raised filled dot in all ten places (both scans; " + C + "p538_Grdot.png, w538_Grdot.png, p539_fstar.png, p539_312.png, p540_323.png)",
    r"\Gro prints Gr with a raised circle (\operatorname{Gr}^{\circ})",
    'symbol', 'high',
    {'old': r'\providecommand{\Gro}{\operatorname{Gr}^{\circ}}', 'new': r'\providecommand{\Gro}{\operatorname{Gr}^{\bullet}}'},
    r"The raised typed dot of Gr is written \bullet in this volume (handled globally). \Gro is defined only here in main.tex and used only on pp. 538-540, so this one edit fixes all ten places (no single edits given for them). If the definition is to stay, replace \Gro by \Gr^{\bullet} in the ten places instead.")

add(536, 'statements of pp. 536-538: Proposition 2.3.1 (p. 536), Définition 2.4.1 and Lemme 2.4.3 (p. 537), Proposition 2.4.4 (p. 538)',
    "statement text underlined word group by word group, symbols and most punctuation not underlined (both scans), e.g. Prop. 2.3.1 'Pour tout schéma propre' X 'sur' k, 'et pour tout' y ∈ Filt_j(X), 'l'application' ... 'définie par' ... 'est une application polynôme de degré' ≤ j",
    r"statements set in roman (no \emph)",
    'underline', 'high', None,
    r"CONVENTION of the Exposé X TeX (its labelled statements, from Définition 1.1.1 on, are set in roman), the pattern of Exposé II (GLOBAL_ISSUES 82) and Exposé IX (findings_506_510); not itemized. Examples: p. 536 '\textbf{Proposition 2.3.1.} Pour tout schéma propre $X$ sur $k$', p. 537 '\textbf{Lemme 2.4.3.} Pour tout schéma propre \(X\)', p. 538 '\textbf{Proposition 2.4.4.} L'application polynôme \(s_y\)'.")

add(536, 'letters that name Modules, pp. 536-540 (L, L_1, ..., L_n, F)',
    "underlined (both scans): p. 536 'cl_P(L̲)', 'L̲_1,...,L̲_n sont des O_X-modules inversibles et F̲ un', 'pour F̲ et la suite L̲_1,...,L̲_n'; p. 537 'L̲ un O_X-module inversible', 'L̲^{⊗n}'; p. 540 'f^*(cl.(F̲))', 'Tor_i(F̲,O_{X'})', 'cohérent F̲'. Not every F: p. 536 'dim. supp. F' is plain",
    r"plain $L$, $L_1$, $F$",
    'underline', 'high', None,
    r"CONVENTION of the transcription (as for Exposé IX, findings_506_510), not itemized and not for a blind script. Examples: p. 536 'Lorsque $L_1,\ldots,L_n$ sont des $\mathcal O_X$-modules inversibles et $F$ un', p. 537 '\(L\) un \(\mathcal O_X\)-module inversible', p. 540 'pour tout \(\mathcal O_X\)-module cohérent \(F\)'.")

add(536, "cl with a raised dot: second display of Prop. 2.3.1 (twice)",
    "a raised filled dot after cl (both scans; " + C + "p536_disp2.png, w536_disp2.png); the same on p. 535 'j(cl˙(L))' (witness)",
    r"\cl^\circ (a raised circle)",
    'symbol', 'high', None,
    r"CONVENTION of Exposé X up to p. 564: the print's raised dot is written \circ (main.tex: \cl^\circ 28 times on pp. 522-551, K^\circ 54 times on pp. 522-564, \Gro on pp. 538-540), while pp. 564-594 write K^\bullet (66) and \Gr^\bullet (35). Examples: p. 536 'g_*(\cl^\circ(L)y)', p. 536 '=\chi(\cl^\circ(L)y)', p. 535 'j(\cl^\circ(L))'. One pass as for Exposés IV and VI (10 Nov): \cl^\circ -> \cl^{\bullet} once the batches of pp. 519-564 confirm the dot.")

# ---------------------------------------------------------------- page 537
add(537, "top of page, before 'Lorsque X est propre sur k'",
    "no heading: p. 537 begins 'Lorsque X est propre sur k, on sait [4] que ...' (both scans)",
    r"\subsection*{2.4, suite}",
    'extra', 'high',
    {'old': r'\subsection*{2.4, suite}' + NL + NL, 'new': ''},
    r"Heading added by the transcription. Also: the folio-537 marker splits the local macro definition '\providecommand{\longO}[1]' / '{\operatorname{length}_{#1}}' (harmless while markers are comments; it belongs below the macro block if markers are ever turned into commands).")

add(537, "'on sait [4] que Pic°_{X/k} est représentable'",
    "'Pic' with a wavy underline and a hand-drawn circle as exponent (both scans; " + C + "p537_Pic1.png)",
    r"\(\Pic^0_{X/k}\) (plain)",
    'underline', 'medium',
    {'old': r'[4] que \(\Pic^0_{X/k}\)', 'new': r'[4] que \(\mathbf{Pic}^0_{X/k}\)'},
    "Wavy underline (the Picard functor), as on p. 536; see that item for the form.")

add(537, "'on sait [4] que Pic°_{X/k} est représentable par un schéma en groupes localement de type fini Pic_{X/k}'",
    "the functor carries the exponent circle: 'Pic°_{X/k} est représentable par un schéma en groupes localement de type fini Pic_{X/k}' (both scans)",
    r"\(\Pic^0_{X/k}\) (keeps the printed reading)",
    'misprint_in_print', 'medium', None,
    r"What [4] gives is the representability of the Picard functor Pic_{X/k} by the group scheme Pic_{X/k} (locally of finite type); Pic° only comes in the next sentence ('La composante neutre Pic°_{X/k} de Pic_{X/k}'). The circle on the functor is a slip. The TeX keeps it; corrected layer: no exponent (written here after the wavy-underline item above; \Pic_{X/k} if that item is not taken).",
    corrected=r'[4] que \(\mathbf{Pic}_{X/k}\)')

for old, new, where in [
        (r'fini \(\Pic_{X/k}\) sur', r'fini \(\underline{\Pic}_{X/k}\) sur', "'localement de type fini Pic_{X/k} sur k'"),
        (r'neutre \(\Pic^0_{X/k}\) de', r'neutre \(\underline{\Pic}^0_{X/k}\) de', "'La composante neutre Pic°_{X/k}'"),
        (r'de \(\Pic_{X/k}\) est un groupe', r'de \(\underline{\Pic}_{X/k}\) est un groupe', "'de Pic_{X/k} est un groupe algébrique'"),
        (r'\cong \Pic^0_{X/k}(k)\)', r'\cong \underline{\Pic}^0_{X/k}(k)\)', "Preuve, 'Pic°(X) ≅ Pic°_{X/k}(k)'"),
        (r'Puisque \(\Pic^0_{X/k}\)', r'Puisque \(\underline{\Pic}^0_{X/k}\)', "Preuve, 'Puisque Pic°_{X/k} est connexe'"),
        (r'le groupe \(\Pic^0_{X/k}(k)\)', r'le groupe \(\underline{\Pic}^0_{X/k}(k)\)', "Preuve, 'sur le groupe Pic°_{X/k}(k) est surjectif'")]:
    add(537, where,
        "'Pic' of the Picard scheme underlined, straight (both scans; " + C + "p537_Pic3.png, p537_cong.png)",
        old + ' (plain)',
        'underline', 'high', {'old': old, 'new': new},
        r"Straight underline of the Picard scheme; \underline{\Pic} is the volume's form (Exp. XIII). Pic°(X) and Pic(X) are plain in the print.")

# ---------------------------------------------------------------- page 538
add(538, 'diagram of the proof of 2.4.4, label of the lower arrow Pic(X_K) → K.(Spec(K))',
    "s̲_y: a bar under the s (both scans; " + C + "p538_diag_bot.png, w538_diag_bot.png)",
    r"\bar s_y (bar over the s)",
    'symbol', 'high',
    {'old': r'\(\bar s_y\)} (KK)', 'new': r'\(\underline{s}_y\)} (KK)'},
    r"The print underlines the s; it does not overline it. The print also sets this label above the arrow (TeX node[below]); not changed in this edit. Apply together with the next item.")

add(538, "'où s̲_y est l'application polynôme correspondant à s_y'",
    "s̲_y with a bar under the s (both scans; " + C + "p538_sbar.png)",
    r"\(\bar s_y\)",
    'symbol', 'high',
    {'old': r'où \(\bar s_y\)', 'new': r'où \(\underline{s}_y\)'},
    "As the diagram label; apply together.")

add(538, 'diagram of the proof of 2.4.4, the two oblique arrows K.(Spec(k)) → Z and K.(Spec(K)) → Z',
    "each oblique arrow carries the isomorphism sign ~ (both scans; " + C + "p538_diag_top.png, p538_diag_bot.png, w538_diag_bot.png)",
    r"\draw[->] (Kk) -- (Z); and \draw[->] (KK) -- (Z); without label",
    'missing', 'high',
    {'old': r'\draw[->] (Kk) -- (Z);' + NL + r'\draw[->] (KK) -- (Z);',
     'new': r'\draw[->] (Kk) -- node[sloped,above] {\(\sim\)} (Z);' + NL + r'\draw[->] (KK) -- node[sloped,above] {\(\sim\)} (Z);'},
    "Missing isomorphism marks.")

add(538, 'end of the diagram of the proof of 2.4.4',
    "a comma to the right of the diagram, at the level of its lower row (both scans)",
    'no punctuation after the diagram',
    'punctuation', 'high',
    {'old': r'\end{tikzpicture}' + NL + r'\]', 'new': r'\end{tikzpicture},' + NL + r'\]'},
    "Missing comma.")

add(538, "K with a raised dot, pp. 538-539 (4 places): 3.1 'de K˙(X)' and the display 'K˙(X) x K.(X) → K.(X)'; (3.2.2) on p. 539 twice",
    "a raised filled dot (both scans; " + C + "p538_Kdot.png, w538_Kdot.png)",
    r"K^\circ",
    'symbol', 'high', None,
    r"CONVENTION, see the cl˙ item on p. 536 (Exposé X up to p. 564 writes the raised dot as \circ). Examples: p. 538 'de \(K^\circ(X)\)', p. 538 'K^\circ(X)\times K_\bullet(X)', p. 539 'x\in K^\circ(X)_{\mathbb Q}'. Same fix as for Exposés IV and VI: K^\circ -> K^{\bullet}.")

# ---------------------------------------------------------------- page 539
add(539, 'start of page (folio-539 marker)',
    "p. 538 ends with (3.1.1) '... (i,j ∈ Z) .'; p. 539 begins 'Gr.(X) devient ainsi un module sur l'anneau Gr˙(X) ...' (both scans)",
    r"page_538.tex ends with the line '\(\Grb(X)\)' after the \end{equation} of (3.1.1); page_539.tex begins 'devient ainsi un module ...'",
    'marker', 'high', None,
    r"Page 539 really begins at '\(\Grb(X)\)'. Exact fix in main.tex (both layers): move the folio-539 marker line up one TeX line, to between '\end{equation}' of (3.1.1) and '\(\Grb(X)\)'.")

add(539, "'... (i ∈ Z)). Considérons maintenant un morphisme propre'",
    "'Considérons maintenant' starts flush left on the line after '(i ∈ Z)).', not indented like the paragraphs of these pages (both scans)",
    "a blank line before 'Considérons maintenant' (new paragraph)",
    'other', 'low',
    {'old': r'\((i\in\mathbb Z)\)).' + NL + NL + r'Considérons', 'new': r'\((i\in\mathbb Z)\)).' + NL + r'Considérons'},
    "The print seems to continue the paragraph; low confidence (a flush-left line after a full stop can be an unindented new paragraph).")

add(539, 'end of display (3.2.1)',
    "'(k ∈ Z)' with no punctuation after it (both scans; " + C + "p539_321.png)",
    r"\qquad(k\in\mathbb Z),",
    'punctuation', 'high',
    {'old': r'\qquad(k\in\mathbb Z),', 'new': r'\qquad(k\in\mathbb Z)'},
    "The TeX adds a comma at the end of the display.")

add(539, "display (3.2.2), left side 'f_*((f^*(x).y)'",
    "two opening parentheses after f_*, one closing (both scans; " + C + "p539_322.png, w539_322eq.png)",
    r"f_*((f^*(x)\cdot y) (keeps the printed reading)",
    'misprint_in_print', 'high', None,
    "Unbalanced parenthesis. The TeX keeps the printed reading.",
    corrected=r'f_*(f^*(x)\cdot y)')

add(539, "display (3.2.2), right side 'x.f_*(Y)'",
    "capital Y (both scans)",
    r"x\cdot f_*(Y) (keeps the printed reading)",
    'misprint_in_print', 'high', None,
    "The element is y ∈ K˙(X')_Q (same display); capital Y is a typing error. The TeX keeps it.",
    corrected=r'x\cdot f_*(y)')

# ---------------------------------------------------------------- page 540
add(540, "3.3, display 'f^*(cl.(F)) = Σ_i (-1)^i cl.(Tor_i^{O_X}(F,O_{X'}))'",
    "Tor underlined (both scans; " + C + "p540_sum.png)",
    r"\Tor_i^{\mathcal O_X} (plain)",
    'underline', 'high',
    {'old': r'\cl_\bullet\bigl(\Tor_i^{\mathcal O_X}', 'new': r'\cl_\bullet\bigl(\underline{\Tor}_i^{\mathcal O_X}'},
    r"The volume writes the underlined Tor as \underline{\Tor} (69 places).")

add(540, "'Les O_X-modules Tor_i^{O_X}(F,O_{X'}) sont concentrés'",
    "Tor underlined (both scans; " + C + "p540_Les.png)",
    r"\Tor_i^{\mathcal O_X} (plain)",
    'underline', 'high',
    {'old': r'modules \(\Tor_i^{\mathcal O_X}', 'new': r'modules \(\underline{\Tor}_i^{\mathcal O_X}'},
    r"As the display above.")

add(540, "'pour tout O_X-module cohérent F . / Les O_X-modules ...'",
    "'Les O_X-modules Tor_i ...' begins a new, indented paragraph (both scans)",
    r"runs on after 'cohérent \(F\).' in the same paragraph",
    'other', 'high',
    {'old': r'cohérent \(F\). Les', 'new': r'cohérent \(F\).' + NL + NL + 'Les'},
    "Missing paragraph break.")

add(540, "display 'dim(f^{-1}(Supp(F)) ≤ dim(Supp(F)) + d .'",
    "three opening and two closing parentheses before ≤ (both scans; " + C + "p540_dim.png)",
    r"\dim(f^{-1}(\Supp(F))\leq \dim(\Supp(F))+d. (keeps the printed reading)",
    'misprint_in_print', 'high', None,
    "Unbalanced parenthesis. The TeX keeps the printed reading.",
    corrected=r'\dim(f^{-1}(\Supp(F)))\leq \dim(\Supp(F))+d.')

add(540, 'end of page (folio-541 marker)',
    "p. 540 ends 'd'où un homomorphisme de degré d de groupes abéliens gradués' (both scans); p. 541 begins with the display '(3.3.1) f^* : Gr.(X) → Gr.(X') .' (witness p. 541)",
    r"page_540.tex ends with '\begin{equation}\tag{3.3.1}' and ' f^*:\Grb(X)\longrightarrow\Grb(X').'; the folio-541 marker stands inside the equation, before '\end{equation}'",
    'marker', 'high', None,
    r"Page 541 really begins at '\begin{equation}\tag{3.3.1}'. Exact fix in main.tex (both layers): move the folio-541 marker line up two TeX lines, to between 'd'où un homomorphisme de degré \(d\) de groupes abéliens gradués' and '\begin{equation}\tag{3.3.1}'.")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    fx = d['fix']
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding='utf-8')
    n = t.count(fx['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE', d['page'], n, repr(fx['old']))
    if '%%%%%%%%%%' in fx['old'] or '%%%%%%%%%%' in fx['new']:
        ok = False
        print('MARKER IN FIX', d['page'], repr(fx['old']))
for d in F:
    assert set(d) >= {'page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'}
    assert d['kind'] in 'word formula symbol font underline missing extra number punctuation accent misprint_in_print marker other'.split()
    assert d['confidence'] in ('high', 'medium', 'low')
    assert ('corrected' in d) == (d['kind'] == 'misprint_in_print')
cnt = {}
for d in F:
    k = 'm' if d['kind'] == 'misprint_in_print' else 'n'
    cnt.setdefault(d['page'], {'n': 0, 'm': 0})[k] += 1
print('counts', cnt, 'total', len(F))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding='utf-8')
    print('written', OUT)
else:
    print('NOT WRITTEN')
