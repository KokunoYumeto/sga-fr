import json
import os

B = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b031_035'
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_031_035.json'

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
         'confidence': confidence, 'fix': fix}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


# ---------------- page 31 ----------------
add(31,
    "Bibliographie, [1] (Abhyankar)",
    "Local uniformization of algebraic surfaces over ground field of characteristic  p = 0 , Amer. J. of Math., t.63, 1956.",
    r"Local uniformization of algebraic surfaces over ground field of characteristic  $p = 0$ , Amer. J. of Math., t.63, 1956.",
    'misprint_in_print', 'high', None,
    "The cited paper is S. Abhyankar, 'Local uniformization on algebraic surfaces over ground fields of characteristic p ≠ 0', "
    "Ann. of Math. 63 (1956), no. 3, 491–526: surfaces in positive characteristic, which is why Théorème 2.3.1 (p. 27) cites [1] "
    "for dim X = 2 and [2] (Hironaka) for characteristic zero. The print has 'of' for 'on', 'field' for 'fields', 'p = 0' "
    "(no stroke through the = in the scan or in the DjVu witness) and the wrong journal (the volume and year are the Annals ones). "
    "The TeX keeps the printed reading; the corrected layer (expose_II_body.tex) already reads 'Local uniformization on algebraic "
    "surfaces over ground fields of characteristic  $p \\neq 0$ , Ann. of Math., t. 63, no. 3, 1956, p. 491--526.' "
    "'corrected' replaces the 'tex' substring.",
    corrected=r"Local uniformization on algebraic surfaces over ground fields of characteristic  $p \neq 0$ , Ann. of Math., t. 63, no. 3, 1956, p. 491--526.")

# ---------------- page 32 ----------------
add(32,
    "Ax.2.",
    "A composit of cocartesian morphism in A is again cocartesian.",
    "A composit of",
    'misprint_in_print', 'medium', None,
    "Misspelling of 'composite' (the exposé has 'composite' 11 times and 'composit' 6 times). The TeX keeps the printed "
    "reading, as does the corrected layer. 'corrected' replaces the 'tex' substring.",
    corrected="A composite of")

add(32,
    "Ax.2.",
    "A composit of cocartesian morphism in A is again cocartesian.",
    "cocartesian morphism in",
    'misprint_in_print', 'medium', None,
    "Plural needed: a composite of cocartesian morphisms. The TeX keeps the printed reading, as does the corrected layer. "
    "'corrected' replaces the 'tex' substring.",
    corrected="cocartesian morphisms in")

# ---------------- page 33 ----------------
add(33,
    "second paragraph, last sentence, 'A map a' --α--> a on A will be called surjective'",
    "A map a' --α--> a on A will be called surjective, by abuse of language,",
    r"on  $\underline{A}$  will be called surjective",
    'misprint_in_print', 'low', None,
    "The parallel sentence just before reads 'A map a' --α--> a in A will be called simply a C_Λ-map'. Low: a preposition "
    "slip that does not change the sense. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    corrected=r"in  $\underline{A}$  will be called surjective")

# ---------------- page 34 ----------------
add(34,
    "Ex.1.1.(c), 'the functor P : M_{X_0} → C_Λ given by (R,X) ↦ R'",
    "(R,X) ⊢∿∿→ R: a hand-drawn arrow with a vertical bar at its tail and a wavy shaft (two waves); clear in the scan and in the DjVu witness",
    r"(R,X) \longmapsto R",
    'symbol', 'medium',
    {'old': r"(R,X) \longmapsto R", 'new': r"(R,X) \mathrel{\mapstochar\rightsquigarrow} R"},
    "Not the straight maps-to arrow of the neighbouring pages ('(S,a) ↦ S' on p. 33 and 'W ⟼ k[W]' on p. 36 are drawn "
    "straight). \\mapstochar is the bar of LaTeX's own \\mapsto; \\rightsquigarrow is from amssymb, which the preamble loads. "
    "A plain \\rightsquigarrow would drop the printed bar.")

add(34,
    "Definition 1.2 (2), 'Let R ×_k k[ε] (π_1 to R, π_2 to k[ε]) be the projection maps'",
    "R ×_k k[ε] is printed once, right after 'Let', as the source of the two arrows π_1 (to R) and π_2 (to k[ε])",
    r"(2) \underline{Let}  $R \underset{k}{\times} k[\varepsilon]$   (then a centred tikzcd whose left node is again R \underset{k}{\times} k[\varepsilon])",
    'extra', 'high',
    {'old': r"(2) \underline{Let}  $R \underset{k}{\times} k[\varepsilon]$", 'new': r"(2) \underline{Let}"},
    "The output shows R ×_k k[ε] twice: inline after 'Let' and again as the source node of the diagram. The fix keeps the "
    "diagram (which carries the arrows and the labels π_1, π_2) and drops the inline copy.")

add(34,
    "Remark 1.3.(a), 'We note that if A is semi-homogeneous. Then so is [A]'",
    "We note that if A is semi-homogeneous. Then so is [A] ,",
    "semi-homogeneous. Then so is",
    'misprint_in_print', 'medium', None,
    "One conditional sentence ('if A is semi-homogeneous, then so is [A]'); the full stop and the capital T are a slip. "
    "Same in the DjVu witness. The TeX keeps the printed reading, as does the corrected layer. 'corrected' replaces the "
    "'tex' substring.",
    corrected="semi-homogeneous, then so is")

# ---------------- page 35 ----------------
LAMBDA_NOTE = ("The index is the base ring Λ ('a complete noetherian local ring Λ', p. 33), typed with the same Λ as on "
               "pp. 33–34, where the TeX writes \\underline{C}_{\\Lambda}; \\wedge is a misreading of the typewriter Λ. "
               "The same misreading runs through the rest of Exposé VI (see the coordinator note).")
add(35,
    "Remark 1.3.(b), 'in a cofibered category A over C_Λ . Set'",
    "over C_Λ . Set R = P(a) , R' = P(a') and",
    r"over  $\underline{C}_{\wedge}$ . Set",
    'symbol', 'high',
    {'old': r"over  $\underline{C}_{\wedge}$ . Set", 'new': r"over  $\underline{C}_{\Lambda}$ . Set"},
    LAMBDA_NOTE)

add(35,
    "(1)', 'in A above (R_1 → R ← R_2) in C_Λ , where'",
    "in C_Λ , where",
    r"in  $\underline{C}_{\wedge}$ , where",
    'symbol', 'high',
    {'old': r"in  $\underline{C}_{\wedge}$ , where", 'new': r"in  $\underline{C}_{\Lambda}$ , where"},
    LAMBDA_NOTE)

add(35,
    "Remark 1.3.(c), 'a semi-homogeneous cofibered groupoid over C_Λ , then'",
    "cofibered groupoid over C_Λ , then",
    r"over  $\underline{C}_{\wedge}$ , then",
    'symbol', 'high',
    {'old': r"over  $\underline{C}_{\wedge}$ , then", 'new': r"over  $\underline{C}_{\Lambda}$ , then"},
    LAMBDA_NOTE)

add(35,
    "Remark 1.3.(c), '[A(k[ε])] is canonically provided with a vector space structure over k'",
    "A(k[ε])] is canonically provided ... (closing bracket printed, no opening bracket before A)",
    r"$\underline{A}(k [\epsilon])]$",
    'misprint_in_print', 'high', None,
    "No opening bracket before A in the scan or in the DjVu witness; the vector-space structure is on the set of "
    "isomorphism classes [A(k[ε])] (as in the display at the top of the page). The TeX keeps the printed reading, as does "
    "the corrected layer. 'corrected' replaces the 'tex' substring.",
    corrected=r"$[\underline{A}(k [\epsilon])]$")

# ---------------- checks ----------------
pages = {}
for p in sorted({d['page'] for d in F}):
    with open(os.path.join(B, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        pages[p] = fh.read()

ok = True
for d in F:
    txt = pages[d['page']]
    if d['fix'] is not None:
        old = d['fix']['old']
        n = txt.count(old)
        marker_hit = any(line.startswith('%%%%%%%%%%') for line in old.split('\n'))
        print('FIX  p%d count=%d %s' % (d['page'], n, old[:70].encode('ascii', 'replace').decode()))
        if n != 1 or marker_hit:
            ok = False
    if d['kind'] == 'misprint_in_print':
        n = txt.count(d['tex'])
        print('MIS  p%d count=%d %s' % (d['page'], n, d['tex'][:70].encode('ascii', 'replace').decode()))
        if n != 1:
            ok = False

# overlapping fixes on the same page?
for p in pages:
    spans = []
    for d in F:
        if d['page'] == p and d['fix'] is not None:
            i = pages[p].find(d['fix']['old'])
            spans.append((i, i + len(d['fix']['old'])))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print('OVERLAP on page', p, a, b)
            ok = False

print('ALL OK' if ok else 'PROBLEM')
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print('written', OUT, len(F))
    from collections import Counter
    c = Counter((d['page'], d['kind'] == 'misprint_in_print') for d in F)
    for p in (31, 32, 33, 34, 35):
        print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
