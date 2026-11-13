import io, json, os

RUN = r'C:/Users/user/Documents/sga_scan_check_20261105/run_6'
B = os.path.join(RUN, 'b416_420')
OUT = os.path.join(RUN, 'findings_416_420.json')

M417 = '%%%%%%%%%%  scan idx 430  |  folio 417  %%%%%%%%%%'
M418 = '%%%%%%%%%%  scan idx 431  |  folio 418  %%%%%%%%%%'

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 416 ----------------
add(page=416,
    where="Exposé title: « CALCUL DU K˙ D'UN SCHEMA ECLATE »",
    scan="K with a raised filled dot (K˙), the K˙ of Exposé VI (both scans; crops_416_420/p416_title_K.png)",
    tex=r"\texorpdfstring{$K^\circ$}{K0}",
    kind="symbol", confidence="high",
    fix={"old": r"\texorpdfstring{$K^\circ$}{K0}", "new": r"\texorpdfstring{$K^{\bullet}$}{K0}"},
    note=r"Exposé VII writes the print's K˙ as K^\circ throughout: 174 in main.tex, folios 416-465 (only the title on pp. 416-420; the witness of p. 435 also prints K˙ where the TeX has K^\circ: 'x ∈ K˙(Y)', 'i_* : K˙(Y) → K˙(X)'). The form Exposé VI §1 had before the 10 Nov pass: one script for VII (K^\circ -> K^{\bullet}, both layers).")

add(page=416,
    where="display (1.2.2), end",
    scan="'Tor_i^A(J^n/J^{n+1},A') = 0 pour i ≥ 1;' with a semicolon (both scans)",
    tex=r"\text{pour }i\geq1, \tag{1.2.2}",
    kind="punctuation", confidence="high",
    fix={"old": r"i\geq1, \tag{1.2.2}", "new": r"i\geq1; \tag{1.2.2}"},
    note="(1.2.1) and (1.2.3) end with a comma, (1.2.4) with a full stop, as in the TeX.")

add(page=416,
    where="proof of Lemme 1.2, first words",
    scan="the indented paragraph 'a) On suppose d'abord que les J^n/J^{n+1} sont projectifs ...' follows the displays directly; no 'Démonstration' label (both scans)",
    tex=r"\emph{Démonstration.} a) On suppose",
    kind="extra", confidence="high",
    fix={"old": r"\emph{Démonstration.} a) On suppose", "new": "a) On suppose"},
    note=r"The transcription adds proof labels the print does not have: here, p. 418 (\emph{Démonstration.}) and p. 420 (\emph{Preuve.}). Exposé VII has four more such labels (diplomatic main.tex lines 10613, 10813, 10893, 11745; folios 422, 432, 435, 460) to check against the print.")

add(page=416,
    where="statements of pp. 416-420: Définition 1.1, Lemme 1.2, Proposition 1.3, Définition 1.4 (with its paragraph 'Soit i : Y → X une immersion ...' on p. 419), Proposition 1.5",
    scan="underlined word group by word group, e.g. Déf. 1.1 'Soient', 'un anneau commutatif', 'un', 'module projectif de', 'type fini', 'un homomorphisme', 'linéaire', 'On dit que', 'est régulier', 'si le complexe de Koszul', 'défini par', 'est acyclique en dimension', 'donc est une résolution de'; 'pour' in (1.2.2) and (1.2.4); Prop. 1.5 'Comparer', 'Soit', 'une immersion', 'Si', 'est régulière', ...; formulas, letters and punctuation plain; the labels underline only the word (both scans)",
    tex=r"the statements in roman (Exposé VII has no \underline at all)",
    kind="underline", confidence="high", fix=None,
    note="Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision): not itemized. The TeX adds no emphasis on defined terms here, and these pages have no category letter.")

# ---------------- page 417 ----------------
add(page=417,
    where="start of page (folio-417 marker)",
    scan="p. 416 ends '... ils sont localement libres de type fini sur B.'; p. 417 begins 'Les relations à prouver se vérifiant ponctuellement sur Spec(A), ...' (both scans)",
    tex="page_416.tex ends '... de type fini sur $B$. Les' above the folio-417 marker; page_417.tex begins 'relations à prouver'",
    kind="marker", confidence="high", fix=None,
    note="Page 417 really begins at 'Les relations'. Exact edit in main.tex, both layers (diplomatic lines 10516-10518, current 10522-10524): replace 'sur $B$. Les\\n" + M417 + "\\nrelations à prouver' by 'sur $B$.\\n" + M417 + "\\nLes relations à prouver' (no blank line, so the paragraph stays whole).")

add(page=417,
    where="'grâce à la suite exacte des Tor associé à la suite exacte :'",
    scan="'associé' (both scans; crops_416_420/p417_associe.png)",
    tex="des Tor associé à la suite exacte (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="associée",
    note="The participle goes with 'la suite exacte'; the same phrase later on the page reads 'associée'. The current layer also has 'associé'.")

add(page=417,
    where="'on déduit les relations J^n⊗_A A' ≃ J'^n.' (proof of (1.2.3))",
    scan="a plain bar with a tilde above and no arrowhead at either end, in both scans (crops_416_420/c417_arrow.png, w417_arrow.png); the other isomorphism arrows of pp. 416-418 have heads",
    tex=r"J^n\otimes_AA'\xrightarrow{\sim}J'^n",
    kind="misprint_in_print", confidence="low",
    fix={"old": r"\xrightarrow{\sim}J'^n$. Enfin", "new": r"\simeq J'^n$. Enfin"},
    corrected=r"\xrightarrow{\sim}",
    note="(1.2.3), which this proves, prints the arrow. Low: the head may be a faint hand-drawn stroke lost in both scans (on p. 418 the main scan almost loses a head that the witness shows).")

# ---------------- page 418 ----------------
add(page=418,
    where="start of page (folio-418 marker)",
    scan="p. 417 ends '... et soit A_o → A l'homomorphisme qui applique'; p. 418 begins 'T_i sur f_i ; notons u_o : E_o = (A_o)^d → A_o ...' (both scans)",
    tex="page_417.tex ends 'qui applique $T_i$ sur $f_i$;' above the folio-418 marker; page_418.tex begins 'notons'",
    kind="marker", confidence="high", fix=None,
    note="Page 418 really begins at '$T_i$ sur $f_i$;'. Exact edit in main.tex, both layers (diplomatic lines 10534-10536, current 10540-10542): replace 'qui applique $T_i$ sur $f_i$;\\n" + M418 + "\\nnotons' by 'qui applique\\n" + M418 + "\\n$T_i$ sur $f_i$; notons'.")

add(page=418,
    where="'Or les J_o^n/J_o^{n+1} sont libres de type fini sur ℤ, donc on peut appliquer'",
    scan="a typed comma after the handwritten ℤ; between them a speck far smaller than typed punctuation (both scans; crops_416_420/c418_Z.png, w418_Z.png)",
    tex=r"sur $\mathbb Z$; donc",
    kind="punctuation", confidence="medium",
    fix={"old": r"$\mathbb Z$; donc", "new": r"$\mathbb Z$, donc"},
    note="")

add(page=418,
    where="'Par suite J^n/J^{n+1} ← J_o^n/J_o^{n+1}⊗_{A_o} A'",
    scan="a left-pointing arrow with a tilde above: the head at the left end is clear in the witness (crops_416_420/w418_arrow.png) and almost lost in the main scan (c418_arrow.png)",
    tex=r"J^n/J^{n+1}\xrightarrow{\sim}J_0^n/J_0^{n+1}\otimes_{A_0}A",
    kind="symbol", confidence="high",
    fix={"old": r"J^n/J^{n+1}\xrightarrow{\sim}J_0^n", "new": r"J^n/J^{n+1}\xleftarrow{\sim}J_0^n"},
    note="The canonical map goes from J_o^n/J_o^{n+1}⊗A to J^n/J^{n+1}; the print's direction is right.")

add(page=418,
    where="proof of Proposition 1.3, first words",
    scan="the indented paragraph 'On a vu dans la démonstration de 1.2 b), que J/J^2 ...' follows 'est un isomorphisme.' directly; no label (both scans)",
    tex=r"\emph{Démonstration.} On a vu",
    kind="extra", confidence="high",
    fix={"old": r"\emph{Démonstration.} On a vu", "new": "On a vu"},
    note="As on p. 416.")

add(page=418,
    where="letters of sheaves on pp. 418-420",
    scan="underlined in the print: in Définition 1.4 the A of (X,A), E, the A of A-Module, E and A of u : E → A, the A of A-linéaire, the K of K.(u), and J, A, J of 'Soit J un Idéal de A ; on dit que J est'; on p. 419 A, E of 'un A-Module libre de type fini E', E and J of E → J, and every J and J_x of 1.4.1-1.4.2 (also the J of O_X/J); on p. 420 every J and J_y and both letters of each J/J^2 (43 letters in all, O not counted). Plain in the print: X, Y, U, V, x, y, u, i, f_i, g_j, and the ideal J = u(E) of a ring on pp. 416-418 (both scans)",
    tex="all plain",
    kind="underline", confidence="high", fix=None,
    note=r"Convention of the Exposé VII transcription, as reported for Exposé VI (findings_401_405): not itemized; no blind script (the ring-case J of pp. 416-418 stays plain). The underlined O of O_U, O_X written \cO falls under the pending volume decision.")

# ---------------- page 419 ----------------
add(page=419,
    where="Définition 1.4, second paragraph: 'il est donc nécéssaire et suffisant'",
    scan="'nécéssaire' (both scans; crops_416_420/c419_necessaire.png)",
    tex="nécéssaire (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="nécessaire",
    note="The current layer already reads 'nécessaire'.")

add(page=419,
    where="'Cette définition est en conflit avec EGA IV 16.9.2, et remplace cette dernière.'",
    scan="'Cette définition est en conflit avec' and 'et remplace cette dernière' underlined; 'EGA IV 16.9.2,' and the rest of the paragraph plain (both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix={"old": "Cette définition est en conflit avec EGA IV 16.9.2, et remplace cette dernière.",
         "new": r"\emph{Cette définition est en conflit avec} EGA IV 16.9.2, \emph{et remplace cette dernière}."},
    note=r"Emphasis in the running text after Définition 1.4, not a statement; \emph is the file's command for underlined words in running text (Exposés V-VI).")

add(page=419,
    where="1.4.1: 'forme un système minimum de générateurs de J au voisinage de x'",
    scan="'système minimum de générateurs de', 'J', 'au voisinage', 'de' underlined (the term defined); x plain; the later uses in 1.4.2-1.4.3 are plain (both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix={"old": r"forme un système minimum de générateurs de $J$ au voisinage de $x$",
         "new": r"forme un \emph{système minimum de générateurs de $J$ au voisinage de} $x$"},
    note="")

# ---------------- page 420 ----------------
add(page=420,
    where="'il existe un voisinage de x sur lequel J peut être engendré soit les f_i, soit par les g_j'",
    scan="'engendré soit les f_i, soit par les' (both scans; crops_416_420/c420_soitles.png)",
    tex=r"engendré soit les $f_i$ (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"engendré soit par les $f_i$",
    note="The current layer already reads 'soit par les'.")

add(page=420,
    where="'Elle permet donc de définir un isomorphime du complexe de Koszul'",
    scan="'isomorphime': no s before the m, the final e struck over another letter (both scans; crops_416_420/c420_isomorphime.png, w420_isom.png)",
    tex="isomorphime (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="isomorphisme",
    note="The current layer already reads 'isomorphisme'.")

add(page=420,
    where="1.4.3: 'donc J dans un voisinage de y puisque J est de type fini'",
    scan="the y carries a diaeresis: two dots, clear in the witness (crops_416_420/w420_ybar.png), joined into a short bar in the main scan (c420_ybar.png)",
    tex=r"voisinage de $y$ puisque (silently corrected)",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"voisinage de $y$ puisque", "new": r"voisinage de $\ddot y$ puisque"},
    corrected="y",
    note="A stray typewriter tréma over the point y; the corrected edition keeps $y$.")

add(page=420,
    where="1.4.3, end: 'puisqu'ils donnent un base de J/J^2.'",
    scan="'un base' (both scans; crops_416_420/c420_unbase.png)",
    tex="donnent un base (printed reading kept)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="une base",
    note="The current layer already reads 'une base'.")

add(page=420,
    where="proof of Proposition 1.5, first words",
    scan="the indented line 'La stabilité par changement de base plat est évidente.' follows the statement directly; no label (both scans)",
    tex=r"\emph{Preuve.} La stabilité",
    kind="extra", confidence="high",
    fix={"old": r"\emph{Preuve.} La stabilité", "new": "La stabilité"},
    note="As on pp. 416 and 418.")

# ---------------- checks ----------------
ok = True
for x in F:
    fx = x.get('fix')
    if fx:
        t = io.open(os.path.join(B, 'page_%d.tex' % x['page']), encoding='utf-8', newline='').read()
        n = t.count(fx['old'])
        if n != 1:
            ok = False
            print('NOT UNIQUE', x['page'], n, fx['old'])
        if '%%%%%%%%%%' in fx['old'] or '%%%%%%%%%%' in fx['new']:
            ok = False
            print('MARKER IN FIX', x['page'])
    if x['kind'] == 'misprint_in_print' and 'corrected' not in x:
        ok = False
        print('NO CORRECTED', x['page'], x['where'])
    if x['kind'] != 'misprint_in_print' and 'corrected' in x:
        ok = False
        print('CORRECTED ON NON-MISPRINT', x['page'])

order = ['page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'corrected', 'note']
F2 = [{k: x[k] for k in order if k in x} for x in F]
with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(F2, f, ensure_ascii=False, indent=1)
    f.write('\n')
json.load(io.open(OUT, encoding='utf-8'))
from collections import Counter
c = Counter((x['page'], x['kind'] == 'misprint_in_print') for x in F2)
for p in range(416, 421):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
print('all fixes unique' if ok else 'PROBLEMS', len(F2))
