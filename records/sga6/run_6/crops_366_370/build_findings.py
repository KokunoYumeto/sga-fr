"""Build findings_366_370.json and check that every fix's old string occurs exactly once in its page file."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
NL = chr(10)
B = 'C:/Users/user/Documents/sga_scan_check_20261105/run_6/'
OUT = B + 'findings_366_370.json'
F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


M366 = '%%%%%%%%%%  scan idx 379  |  folio 366  %%%%%%%%%%'
M370 = '%%%%%%%%%%  scan idx 383  |  folio 370  %%%%%%%%%%'

# ---------------- p. 366
add(366, "start of page (folio-366 marker)",
    "p. 366 begins '2°) 1,...,ξ^{r+1} sont linéairement dépendants sur K˙(S).' (both scans)",
    r"the line '\(2^\circ\)) \(1,\ldots,\xi^{r+1}\)' is the last line of page_365.tex, above the folio-366 marker; page_366.tex begins 'sont linéairement dépendants'",
    "marker", "high", None,
    r"Page 366 really begins with '\(2^\circ\)) \(1,\ldots,\xi^{r+1}\)' (a whole TeX line, not a heading). Move the folio-366 marker up one line, above that line: python -I move_marker.py 6 366 '\(2^\circ\))' --before. Equivalent exact fix in main.tex (both layers; diplomatic line 9185, current 9184): replace '\(2^\circ\)) \(1,\ldots,\xi^{r+1}\)\n" + M366 + r"\n' by '" + M366 + r"\n\(2^\circ\)) \(1,\ldots,\xi^{r+1}\)\n' (simulated in memory on both layers, crops_366_370/sim_markers.py: '\end{enumerate}', blank line, marker, '\(2^\circ\)) ...', 'sont linéairement dépendants ...').")

add(366, "'linéairement dépendants sur K˙(S)' and 'linéairement indépendants sur K˙(S)' (2°) and 3°) of the plan of proof)",
    "K followed by a raised dot (K˙, the K^• of the exposé), not the small ring of '2°)', '3°)' on the same lines (both scans; crops_366_370/c366_Kdot.png, w366_top.png)",
    r"\(K^\circ(S)\) twice",
    "symbol", "high", None,
    r"Convention of the Exposé VI transcription, reported once: K^\circ for the print's K with a raised dot in § 1 (46 times in main.tex, folios 365-379, the exposé title and § 1 heading included) and K' in §§ 2-3 (193 times, folios 380-415, not on these pages), as Exposé IV before the 10 Nov script (GLOBAL_ISSUES 86). Examples in that script's form: p. 366 'dépendants sur \(K^\circ(S)\)' -> 'dépendants sur \(K^{\bullet}(S)\)'; p. 366 'indépendants sur \(K^\circ(S)\)' -> 'indépendants sur \(K^{\bullet}(S)\)'; p. 365 title 'Le \(K^\circ\) d'un fibré projectif' -> 'Le \(K^{\bullet}\) d'un fibré projectif' (that page's print not checked here). The three K_i^{\bullet} of § 2 are complexes, not this K.")

add(366, "sheaf letters and Proj on pp. 366-370",
    "the typescript underlines the letters of sheaves and Modules: B, M, N, N(n), M_n, B_{k-n}, M_k, P, Q, B|U (p. 366); M, B, M^{(n)} (p. 367); M, F, E, M', F(n) (p. 368); F, E, E_o, F_o, E_λ, E_μ (p. 369); F_{λ'}, F_μ, F_{λ''}, M, F (p. 370); and the 'Proj' of Proj_o (pp. 368, 370). Plain in the print: S, X, U, the integers, and A, B, M, B̃, M̃ of Lemme 1.5.1 (modules over a ring) (both scans)",
    r"plain \(B\), \(M\), \(N\), \(P\), \(Q\), \(E\), \(F\), \(M'\); \Projz prints Proj_0 without the underline; Exposé VI has no \underline at all (main.tex lines 9154-10479)",
    "underline", "high", None,
    r"Convention of the Exposé VI transcription (no underline markup, as Exposé V: findings_326_330 p. 330), reported once. Three examples, in the form to use if the diplomatic layer reproduces them: p. 366 'Soient \(S\) un schéma, \(B\) une' -> 'Soient \(S\) un schéma, \(\underline{B}\) une'; p. 367 '\[\n  M\simeq \bigoplus_{n=n_0}^{n_1}M^{(n)},' -> '\[\n  \underline{M}\simeq \bigoplus_{n=n_0}^{n_1}\underline{M}^{(n)},'; p. 369 'soit \(F_0\) un' -> 'soit \(\underline{F}_0\) un'. Not for a blind script: S, X, U and the ring-theoretic A, B, M of Lemme 1.5.1 are plain in the print. Proj: \Projz is defined only in the Exposé VI macro block (main.tex line 9132); \underline{\operatorname{Proj}}_0 there gives the printed form (check its uses on folios 365, 373-374 first). The underlined O of O_S, O_X is \mathcal O on these pages (pending volume decision).")

# ---------------- p. 367
add(367, "statements of pp. 367-370: Proposition 1.2.3 (p. 367), Proposition 1.3 (p. 368), Corollaire 1.4 and Lemme 1.5.1 (p. 370)",
    "underlined word groups: Prop. 1.2.3 'Les entiers', 'intervenant dans la décomposition', 'ne dépendent pas de la décomposition choisie' (k_n, (1.2.2) and the full stop plain); Prop. 1.3 'Soient', 'un schéma quasi-compact', 'un', '-Module localement libre de type fini', 'le fibré projectif associé', 'Soit', 'un', '-Module de présentation finie', 'plat sur', 'Il existe un entier', 'tel que pour', 'on ait', i) 'pour', ii) 'est localement libre de type fini sur', iii) 'est un', '-Module gradué de présentation finie' (S, X, n_o, n ⩾ n_o, the formulas and (1.2) plain; the sheaf letters E, O_S, F, O_X, M and S(E) carry their own underlines); Cor. 1.4 'Avec les hypothèses de', 'il existe un', '-Module gradué', 'de présentation finie', 'et plat sur', 'tel que' (1.3 plain); Lemme 1.5.1 'Soient', 'un anneau', 'une', 'algèbre graduée à degrés positifs', 'telle que', 'un', 'module gradué', 'On suppose que', 'est projectif de type fini', 'en tant que', 'module non gradué', 'Soient', 'le faisceau d'algèbres sur', 'défini par', 'le', 'Module associé à', 'alors', 'est localement sur', 'libre de type fini sur', 'comme', 'Module gradué' (A, B, M, B̃, M̃, A-, B-, Spec(A), B_o = A and (1.2) plain) (both scans)",
    r"the four statements in roman (no \underline, no \emph)",
    "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (as Exposé V, findings_336_340): not itemized, for the per-exposé decision; the word groups are listed for a scripted fix. No emphasized defined terms and no category L on these pages.")

add(367, "after (1.2.2): 'On obtient ainsi une décomposition de M'",
    "'On obtient ainsi' begins a new, indented paragraph (both scans)",
    r"\end{equation} followed directly by 'On obtient ainsi' (the paragraph runs on)",
    "other", "high",
    {"old": r"\end{equation}" + NL + "On obtient ainsi", "new": r"\end{equation}" + NL + NL + "On obtient ainsi"},
    "Missing paragraph break.")

add(367, "proof of 1.2.3, the display of the two decompositions",
    "⊕(B(-n))^{k_n} ⥲ ⊕(B(-n))^{k'_n} : a tilde over an arrow, unlike the ≃ (tilde over a bar) of (1.2.2) and of the display after it (both scans; crops_366_370/c367_iso2.png, w367_iso2.png, c367_iso1.png)",
    r"\simeq",
    "symbol", "high",
    {"old": r"\bigr)^{k_n}\simeq", "new": r"\bigr)^{k_n}\xrightarrow{\sim}"},
    r"\xrightarrow{\sim} is the file's form for the printed ⥲ (82 uses in main.tex).")

# ---------------- p. 368
add(368, "end of the first paragraph: '... ne dépendent pas de la décomposition'",
    "no full stop after 'décomposition' at the end of the paragraph, before Proposition 1.3 (both scans; crops_366_370/c368_decomp_end.png, w368_top.png)",
    "ne dépendent pas de la décomposition. (silently corrected)",
    "misprint_in_print", "high",
    {"old": "pas de la décomposition.", "new": "pas de la décomposition"},
    "The typist left out the final full stop.", corrected="pas de la décomposition.")

add(368, "'Par ailleurs, Γ_*(F) = Γ_*(Proj_o M') = ⊕ f_*(F(n))'",
    "Γ_*(Proj_o M') : one pair of parentheses, M' directly after Proj_o (both scans; crops_366_370/c368_gamma.png)",
    r"\Gamma_*(\Projz(M'))",
    "formula", "high",
    {"old": r"\Gamma_*(\Projz(M'))", "new": r"\Gamma_*(\Projz M')"},
    r"The TeX adds the parentheses around M' (the print has Proj_o(M') in the line above, but not here).")

add(368, "'est TN-isomorphe à M' d'après EGA III 2.3.1'",
    "EGA: the G's crossbar and stem are weak in the main scan but present in both scans (the witness shows crossbar and stem; crops_366_370/c368_ECA_z.png, w368_ECA_z.png; compare 'EGA III 7.9.10' on the same page, c368_EGA_known.png)",
    "d'après ECA III 2.3.1",
    "word", "medium",
    {"old": "d'après ECA III", "new": "d'après EGA III"},
    "A weakly struck G read as C; not a misprint of the typescript.")

add(368, "symmetric algebra S(E): p. 368 Prop. 1.3 iii) and 'il existe un S(E)-Module gradué quasi-cohérent', p. 369 'soit un S(E)-Module de type fini', p. 370 Corollaire 1.4",
    "S(E) with a doubly underlined S (the typescript's bold, as the doubly underlined P of P(E_o), P(E_μ), p. 369) and an underlined E (both scans; crops_366_370/c368_SE.png, c368_SE2.png)",
    r"\Sym(E), which prints Sym(E) (\Sym = \operatorname{Sym}, main.tex line 80)",
    "symbol", "high", None,
    r"Convention of the Exposé VI transcription, reported once (20 \Sym in the exposé: folios 365, 368-370, 372, 377, 415). Three examples, in the print's form (\mathbf for the double underline, as \mathbf P(E_0) on p. 369): p. 368 '\text{ est un }\Sym(E)\text{-Module' -> '\text{ est un }\mathbf S(E)\text{-Module'; p. 369 'soit un \(\Sym(E)\)-Module' -> 'soit un \(\mathbf S(E)\)-Module'; p. 370 'il existe un \(\Sym(E)\)-Module gradué' -> 'il existe un \(\mathbf S(E)\)-Module gradué'. A \renewcommand{\Sym}{\mathbf S} scoped to Exposé VI would do it (the \providecommand{\Sym} of line 9131 has no effect), after the other folios are checked.")

# ---------------- p. 369
add(369, "'donc de présentation finie d'après les hypothèses noethériennnes'",
    "noethériennnes, with three n (both scans; crops_366_370/c369_noeth.png, w369_top.png)",
    "noethériennnes (printed reading kept)",
    "misprint_in_print", "high", None,
    "Typing error; the diplomatic layer is right.", corrected="noethériennes")

add(369, "'La proposition est donc montrée dans le cas ou S est noethérien.'",
    "'ou' without the grave accent (both scans; crops_366_370/c369_ou.png, w369_top.png); the typewriter has ù ('cas où S est affine', p. 368)",
    r"dans le cas ou \(S\) (printed reading kept)",
    "misprint_in_print", "high", None,
    "Missing accent; the diplomatic layer is right.", corrected=r"dans le cas où \(S\)")

add(369, "carré cartésien, bottom arrow S → S_o",
    "label g_o above the bottom arrow, as g above the top arrow (both scans; w369_top.png)",
    r'''\arrow[r,"g_0"'] (the ' sets the label below the arrow)''',
    "formula", "medium",
    {"old": r'''\arrow[r,"g_0"']''', "new": r'''\arrow[r,"g_0"]'''},
    "Label on the wrong side of the arrow (as reported on pp. 41, 59, 74); the other three labels stand as printed (g above, f left, f_o right).")

# ---------------- p. 370
add(370, "start of page (folio-370 marker)",
    "p. 370 begins 'et un faisceau F_{λ'} de présentation finie sur X_{λ'}'; p. 369 ends '... Par suite, il existe un indice λ' ⩾ λ' (both scans)",
    r"'et un' ends the last line of page_369.tex ('... il existe un indice \(\lambda'\geq\lambda\) et un'), above the folio-370 marker; page_370.tex begins 'faisceau'",
    "marker", "high", None,
    r"The folio-370 marker stands two words late. Page 370 really begins at 'et un faisceau'. Exact fix in main.tex (both layers; diplomatic line 9270, current 9269): replace '\(\lambda'\geq\lambda\) et un\n" + M370 + r"\nfaisceau' by '\(\lambda'\geq\lambda\)\n" + M370 + r"\net un faisceau' (each old string occurs once; simulated in memory on both layers, crops_366_370/sim_markers.py). marker_split_word.py pull 'et un' would give 'et unfaisceau' without a space.")

add(370, "'tel que F = u'^*_{λ'}(F_{λ'})'",
    "u with a prime: the prime after the u, the asterisk above, λ' below (both scans; crops_366_370/c370_ustar.png, w370_top.png)",
    r"F=u_{\lambda'}^*(F_{\lambda'})",
    "symbol", "high",
    {"old": r"F=u_{\lambda'}^*(F_{\lambda'})", "new": r"F=u'^*_{\lambda'}(F_{\lambda'})"},
    r"u'_{λ'} : X → X_{λ'} is the morphism of the X's, distinct from u_{λ'} : S → S_{λ'} (p. 369).")

add(370, "'(u'_{λ'} étant le morphisme X → X_{λ'})'",
    "u with a prime (both scans; crops_366_370/c370_ulam.png, w370_top.png)",
    r"(\(u_{\lambda'}\) étant",
    "symbol", "high",
    {"old": r"(\(u_{\lambda'}\) étant", "new": r"(\(u'_{\lambda'}\) étant"},
    "As the entry above; the two edits do not overlap.")

add(370, "'Toutes les hypothèses de 1.3 sont donc vérifiée,'",
    "vérifiée, singular (both scans; w370_top.png)",
    "sont donc vérifiée, (printed reading kept)",
    "misprint_in_print", "high", None,
    "Agreement error; the diplomatic layer is right.", corrected="sont donc vérifiées,")

add(370, "after '... sont localement libres sur S.': 'Par ailleurs, F = Proj_o(M) d'après EGA II 3.4.'",
    "'Par ailleurs' begins a new, indented paragraph (both scans)",
    r"'... sur \(S\). Par ailleurs, \(F=\Projz(M)\) ...' in one paragraph",
    "other", "high",
    {"old": r"sur \(S\). Par ailleurs", "new": r"sur \(S\)." + NL + NL + "Par ailleurs"},
    "Missing paragraph break.")

add(370, "'Passons à la partie b) de la démonstration.'",
    "'Passons' begins a new, indented paragraph of its own (both scans)",
    "'... d'après EGA II 3.4. Passons à la partie b) ...' in one paragraph",
    "other", "high",
    {"old": "EGA II 3.4. Passons", "new": "EGA II 3.4." + NL + NL + "Passons"},
    "Missing paragraph break; independent of the entry above (no common text).")

# ---------------- checks
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = open(B + 'b366_370/page_%03d.tex' % d["page"], encoding='utf-8').read()
    n = t.count(d["fix"]["old"])
    if n != 1 or '%%%%%%%%%%' in d["fix"]["old"]:
        ok = False
    print(d["page"], n, repr(d["fix"]["old"]))
with open(OUT, 'w', encoding='utf-8', newline=NL) as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print('written', len(F), 'ok' if ok else 'PROBLEM')
