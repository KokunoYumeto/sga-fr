import io, json, os, re

RUN = r'C:/Users/user/Documents/sga_scan_check_20261105/run_6'
B = os.path.join(RUN, 'b421_425')
OUT = os.path.join(RUN, 'findings_421_425.json')
DIP = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex'
CUR = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/current/main.tex'
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

M425 = '%%%%%%%%%%  scan idx 438  |  folio 425  %%%%%%%%%%'
M426 = '%%%%%%%%%%  scan idx 439  |  folio 426  %%%%%%%%%%'

F = []


def add(**kw):
    F.append(kw)


# ---------------- page 421 ----------------
add(page=421,
    where="statements of pp. 421-425: Définition 1.6 (p. 421), Proposition 1.7 (p. 422), Proposition 1.8 (pp. 424-425)",
    scan="underlined word group by word group, e.g. Déf. 1.6 'Soit', 'une immersion définie dans un ouvert', 'de', 'par un Idéal', 'de', 'le', '-Module', '(indépendant de', 'est appelé', 'et noté', 'Si', 'est régulière', 'est', 'localement libre de type fini', 'et son rang s'appelle', 'ou encore codimension de' (the defined terms 'faisceau conormal de Y dans X' and 'codimension de Y dans X' left plain); Prop. 1.7 'Comparer', 'Soient', 'et', 'deux immersions', 'Si', 'sont régulières', 'est régulière', 'et la suite', 'est exacte', 'en particulier', ...; Prop. 1.8 'Soient', 'un schéma', 'un', '-Module localement libre de type fini', 'un homomorphisme régulier', 'On note', 'le sous-schéma fermé de', ..., 'Alors', 'i.e.'; letters and formulas plain; the labels underline only the word (both scans)",
    tex=r"the statements in roman (Exposé VII has no \underline)",
    kind="underline", confidence="high", fix=None,
    note="Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_416_420 reported for pp. 416-420: not itemized. The TeX adds no emphasis on the defined terms; these pages have no category letter.")

add(page=421,
    where="letters of sheaves on pp. 421-425",
    scan="underlined in the print: J and both letters of each J/J^2 of p. 421 (proof of 1.5 and Déf. 1.6); I, J, K, I/I^2 in the proof of (1.6.1); every N of N_{X/Y}, N_{X/Z}, N_{Y/Z} (pp. 421-424); in Prop. 1.8 (pp. 424-425) E, J of 'E un O_X-Module', 'u : E → O_X', 'J = u(E)', 'défini par J', 'associé à E', p^*(E), S(E), every J of ⊕J^n, and F of the two displays of p. 425; E of 'E libre sur X' (p. 425). Plain in the print: X, Y, Z, U, P, T, i, j, u, v, p, f_i, g_j, the ideals I, J, K of the rings A, B, C in the proof of 1.7 (pp. 422-424) and the E of 'E étant muni d'une base' (p. 425) (both scans)",
    tex="all plain",
    kind="underline", confidence="high", fix=None,
    note=r"Convention of the Exposé VII transcription, as findings_416_420 reported for pp. 418-420: not itemized; no blind script (the ring ideals of pp. 422-424 stay plain). The underlined O written \cO falls under the pending volume decision.")

add(page=421,
    where="'Si f_1,...,f_d est une suite de sections de J relevant une base de J/J^2, le complexe de Koszul ...'",
    scan="continues the paragraph: no indent, after the full line '... par morphismes fidèlement plats quasi-compacts.' (both scans); the typescript indents its new paragraphs ('Si on a deux immersions fermées' on this page)",
    tex=r"blank line (new paragraph) before 'Si $f_1,\ldots,f_d$'",
    kind="other", confidence="low",
    fix={"old": "quasi-compacts.\n\nSi $f_1", "new": "quasi-compacts. Si $f_1"},
    note="Added paragraph break.")

add(page=421,
    where="'de Z dans Y. On a la suite exacte :' before the display 0 → I → J → K → 0 ;",
    scan="'On a la suite exacte :' with a colon (both scans)",
    tex="On a la suite exacte (no colon)",
    kind="punctuation", confidence="high",
    fix={"old": "On a la suite exacte", "new": "On a la suite exacte:"},
    note="The TeX has the colon in 'forment une suite exacte:' before (1.6.1).")

add(page=421,
    where="'d'où par tensorisation par O_X/I = O_Y, la suite exacte :'",
    scan="no comma after 'd'où' (both scans; the speck above the line before 'tensorisation' in the main scan is not punctuation)",
    tex="d'où, par tensorisation",
    kind="punctuation", confidence="high",
    fix={"old": "d'où, par", "new": "d'où par"},
    note="Added comma.")

add(page=421,
    where="same line, end: '... = O_Y, la suite exacte :'",
    scan="colon after 'la suite exacte' (both scans)",
    tex=r"$\cO_X/I=\cO_Y$, la suite exacte (no colon)",
    kind="punctuation", confidence="high",
    fix={"old": r"=\cO_Y$, la suite exacte", "new": r"=\cO_Y$, la suite exacte:"},
    note="")

add(page=421,
    where="'en tensorisant par O_Z = O_X/J = O_Y/K, on obtient la suite exacte :'",
    scan="colon after 'la suite exacte' (both scans)",
    tex="on obtient la suite exacte (no colon)",
    kind="punctuation", confidence="high",
    fix={"old": "on obtient la suite exacte", "new": "on obtient la suite exacte:"},
    note="")

# ---------------- page 422 ----------------
add(page=422,
    where="Proposition 1.7, first line: 'Soient i : Y → X, et j : Z → Y deux immersions :'",
    scan="comma after the X of i : Y → X (both scans)",
    tex=r"Soient $i:Y\longrightarrow X$ et $j:Z\longrightarrow Y$",
    kind="punctuation", confidence="high",
    fix={"old": r"Y\longrightarrow X$ et", "new": r"Y\longrightarrow X$, et"},
    note="")

add(page=422,
    where="proof of Proposition 1.7, first words",
    scan="the indented paragraph 'La question étant locale sur X, on peut supposer X affine ...' follows the statement directly; no label (both scans)",
    tex=r"\emph{Preuve.} La question",
    kind="extra", confidence="high",
    fix={"old": r"\emph{Preuve.} La question", "new": "La question"},
    note="As pp. 416, 418, 420 (findings_416_420; diplomatic main.tex line 10613).")

# ---------------- page 423 ----------------
add(page=423,
    where="'... et (ḡ_1,...,ḡ_m), sont respectivement les Tor ...'",
    scan="comma after (ḡ_1,...,ḡ_m) (both scans)",
    tex=r"$(\bar g_1,\ldots,\bar g_m)$ sont respectivement",
    kind="punctuation", confidence="high",
    fix={"old": r"\bar g_m)$ sont respectivement", "new": r"\bar g_m)$, sont respectivement"},
    note="")

add(page=423,
    where="'sont respectivement les Tor_i^{A_o}(B_o,A), Tor_i^{A_o}(C_o,A), Tor_i^{A_o}(C_o,B).'",
    scan="the third Tor has the superscript A_o (both scans; crops_421_425/c423_tor3.png, w423_tor3.png)",
    tex=r"$\Tor_i^{A_0}(C_0,B)$ (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\Tor_i^{B_0}(C_0,B)",
    note="The Koszul complex of (ḡ_1,...,ḡ_m) on B is the Koszul resolution of C_o over B_o tensored with B, so its homology is Tor^{B_o}(C_o,B); the third line of (1.7.2) prints Tor_i^{B_o}(C_o,B). The current layer also has A_0.")

add(page=423,
    where="(1.7.2), end of the first line 'i régulière ⟺ ∀i ≥ 1, Tor_i^{A_o}(B_o,A) = 0 ;'",
    scan="semicolon (both scans); the second line also ends with ';', the third with '.'",
    tex=r"\Tor_i^{A_0}(B_0,A)=0,\\",
    kind="punctuation", confidence="high",
    fix={"old": r"(B_0,A)=0,\\", "new": r"(B_0,A)=0;\\"},
    note="")

add(page=423,
    where="(1.7.2), end of the second line 'i∘j régulière ⟺ ∀i ≥ 1, Tor_i^{A_o}(C_o,A) = 0 ;'",
    scan="semicolon (both scans)",
    tex=r"\Tor_i^{A_0}(C_0,A)=0,\\",
    kind="punctuation", confidence="high",
    fix={"old": r"(C_0,A)=0,\\", "new": r"(C_0,A)=0;\\"},
    note="")

add(page=423,
    where="'On utilise alors la suite spectrale de transitivité ([1], XVI 5)', after (1.7.2)",
    scan="starts an indented new paragraph (both scans)",
    tex=r"\end{equation} then 'On utilise alors' on the next line (no blank line: no new paragraph)",
    kind="other", confidence="medium",
    fix={"old": "\\end{equation}\nOn utilise alors", "new": "\\end{equation}\n\nOn utilise alors"},
    note="Missing paragraph break.")

add(page=423,
    where="'D'après les hypothèses de i), E^2_{pq} = 0 pour p ou q ≠ 0.', after (1.7.3)",
    scan="starts an indented new paragraph (both scans)",
    tex=r"\end{equation} then 'D'après les hypothèses' on the next line (no blank line: no new paragraph)",
    kind="other", confidence="medium",
    fix={"old": "\\end{equation}\nD'après les hypothèses", "new": "\\end{equation}\n\nD'après les hypothèses"},
    note="Missing paragraph break.")

# ---------------- page 424 ----------------
add(page=424,
    where="'Il en résulte que le noyau de j^*(N_{X/Y}) → N_{X/Z} est localement libre de rang nul, donc que la suite (1.8.1) est exacte.'",
    scan="'(1.8.1)' (both scans)",
    tex="la suite (1.8.1) (printed reading kept)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="(1.6.1)",
    note="The sequence meant is the conormal sequence of 1.7 i), i.e. (1.6.1) completed by 0 on the left; the print numbers no display (1.8.1) (the canonical sequence of Prop. 1.8 on p. 425 has no number, see p. 425). The current layer reads (1.6.1).")

add(page=424,
    where="'on obtient donc des edge-isomorphismes : E^2_{p,0} ≃ Tor_p^{A_o}(C_o,A).'",
    scan="a tilde over a short plain bar, no head at either end, in both scans (crops_421_425/c424_iso.png, w424_iso.png); the arrows of this page have heads",
    tex=r"E^2_{p,0}\xrightarrow{\sim}\Tor_p^{A_0}(C_0,A)",
    kind="symbol", confidence="medium",
    fix={"old": r"E^2_{p,0}\xrightarrow{\sim}", "new": r"E^2_{p,0}\simeq"},
    note="Same glyph as p. 417 'J^n⊗_A A' ≃ J'^n' (findings_416_420, filed there as a low misprint because (1.2.3) prints the arrow). Here no printed arrow states the same map, and ≃ is a correct reading: symbol, not misprint.")

# ---------------- page 425 ----------------
add(page=425,
    where="start of page (folio-425 marker)",
    scan="p. 424 ends '... un homomorphisme régulier, J = u(E). On note Y'; p. 425 begins 'le sous-schéma fermé de X défini par J, ...' (both scans)",
    tex=r"page_424.tex ends 'On note \(Y\) le' above the folio-425 marker; page_425.tex begins 'sous-schéma fermé'",
    kind="marker", confidence="high", fix=None,
    note=("Page 425 really begins at 'le sous-schéma'. Exact edit in main.tex, both layers (diplomatic lines 10672-10674, current 10678-10680): replace 'On note \\(Y\\) le\\n" + M425 + "\\nsous-schéma fermé' by 'On note \\(Y\\)\\n" + M425 + "\\nle sous-schéma fermé'. Or python -I move_marker.py 6 425 \"le\" --before (the last 'le' before the marker is this one; simulated on both layers: 'On note \\(Y\\) ', the marker, 'le', 'sous-schéma'); marker_split_word.py pull would glue 'lesous-schéma'."))

add(page=425,
    where="end of page (folio-426 marker)",
    scan="p. 425 ends '... il suffit de le faire localement sur P, donc sur les'; 'ouverts D_+(X_i) ; plaçons-nous par exemple ...' is the first line of p. 426 (both scans)",
    tex=r"page_425.tex ends 'donc sur les ouverts \(D_+(X_i)\); plaçons-' above the folio-426 marker; page_426.tex begins 'nous par exemple'",
    kind="marker", confidence="high", fix=None,
    note=("Page 426 really begins at 'ouverts'. Exact edit in main.tex, both layers (diplomatic lines 10691-10693, current 10697-10699): replace 'donc sur les ouverts \\(D_+(X_i)\\); plaçons-\\n" + M426 + "\\nnous par exemple' by 'donc sur les\\n" + M426 + "\\nouverts \\(D_+(X_i)\\); plaçons-nous par exemple'. This also removes the space the line end now prints in 'plaçons- nous'. With python -I move_marker.py 6 426 \"ouverts \\(D_+(X_i)\\)\" --before, join 'plaçons-' and 'nous' afterwards (they end up on adjacent lines)."))

add(page=425,
    where="display '0 → F → p^*(E) → O_P(1) → 0 ,' (the canonical exact sequence of Prop. 1.8)",
    scan="no formula number at either margin (both scans)",
    tex=r"\begin{equation}\tag{1.8.1} ... \end{equation}",
    kind="extra", confidence="high",
    fix={"old": "\\begin{equation}\\tag{1.8.1}\n0\\to F\\to p^*(E)\\to\\cO_P(1)\\to0,\n\\end{equation}",
         "new": "\\[\n0\\to F\\to p^*(E)\\to\\cO_P(1)\\to0,\n\\]"},
    note="No text cites this sequence as (1.8.1); the one citation of (1.8.1), on p. 424, means the conormal sequence (misprint, see p. 424). The current layer has the same tag.")

SNOTE = (r"The print's doubly underlined S, as the S(E) of Exposé VI, which the volume prints bold (\renewcommand{\Sym}{\mathbf{S}}, main.tex line 9131); "
         r"in Exposé VII \Sym prints the typed 'Sym' of (1.3.1), p. 418, so it cannot be used here. \cS is \mathcal S (script S).")
add(page=425,
    where="Prop. 1.8 ii): 'l'homomorphisme surjectif S(E) → ⊕_{n≥0} J^n'",
    scan="a typed S underlined twice (the E underlined once), both scans",
    tex=r"\cS(E)",
    kind="font", confidence="high",
    fix={"old": r"\(\cS(E)\longrightarrow", "new": r"\(\mathbf{S}(E)\longrightarrow"},
    note=SNOTE + " The other three of the page follow; p. 427 has the same \\cS (main.tex lines 10720-10724) to check.")

add(page=425,
    where="Prop. 1.8 iii): 'Le S(E)-Module ⊕_{n≥0} J^n'",
    scan="doubly underlined S (both scans)",
    tex=r"\cS(E)",
    kind="font", confidence="high",
    fix={"old": r"Le \(\cS(E)\)-Module", "new": r"Le \(\mathbf{S}(E)\)-Module"},
    note="As the entry before.")

add(page=425,
    where="Prop. 1.8 iii): 'est parfait en tant que S(E)-Module gradué'",
    scan="doubly underlined S (both scans)",
    tex=r"\cS(E)",
    kind="font", confidence="high",
    fix={"old": r"en tant que \(\cS(E)\)-Module", "new": r"en tant que \(\mathbf{S}(E)\)-Module"},
    note="As the entry before.")

add(page=425,
    where="Prop. 1.8 iii): 'par des S(E)-Modules gradués localement libres de type fini'",
    scan="doubly underlined S (both scans)",
    tex=r"\cS(E)",
    kind="font", confidence="high",
    fix={"old": r"par des \(\cS(E)\)-Modules", "new": r"par des \(\mathbf{S}(E)\)-Modules"},
    note="As the entry before.")

add(page=425,
    where="Prop. 1.8: 'Alors :' after the display v : F → p^*(E) → O_P.",
    scan="'Alors :' starts an indented new paragraph, like the items i)-iii) after it (both scans)",
    tex=r"\] then 'Alors :' on the next line (no blank line: no new paragraph)",
    kind="other", confidence="medium",
    fix={"old": "\\]\nAlors :", "new": "\\]\n\nAlors :"},
    note="Missing paragraph break.")

add(page=425,
    where="proof of 1.8 ii): 'On fait d'abord la démonstration dans le cas standard'",
    scan="starts an indented new paragraph after the short line '... On pose X = Spec(A).' (both scans)",
    tex=r"'On pose \(X=\Spec(A)\). On fait d'abord' in one paragraph",
    kind="other", confidence="medium",
    fix={"old": r"On pose \(X=\Spec(A)\). On fait", "new": "On pose \\(X=\\Spec(A)\\).\n\nOn fait"},
    note="Missing paragraph break.")

# ---------------- checks ----------------
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = []
ok = True
for f in F:
    page = f["page"]
    t = io.open(os.path.join(B, 'page_%03d.tex' % page), encoding='utf-8', newline='').read()
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = t.count(old)
        if n != 1:
            ok = False
            print('NOT UNIQUE', page, n, repr(old))
        if MARK.search(old) or MARK.search(f["fix"]["new"]):
            ok = False
            print('MARKER IN FIX', page, repr(old))
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
    else:
        assert "corrected" not in f
    out.append({k: f[k] for k in order if k in f})

# marker edits: literal replacements and move_marker simulation on both layers
def sim_move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, k

lit = [
    ("On note \\(Y\\) le\n" + M425 + "\nsous-schéma fermé", "On note \\(Y\\)\n" + M425 + "\nle sous-schéma fermé"),
    ("donc sur les ouverts \\(D_+(X_i)\\); plaçons-\n" + M426 + "\nnous par exemple",
     "donc sur les\n" + M426 + "\nouverts \\(D_+(X_i)\\); plaçons-nous par exemple"),
]
for name, p in (('dip', DIP), ('cur', CUR)):
    t = io.open(p, encoding='utf-8', newline='').read()
    for o, nw in lit:
        print(name, 'literal count', t.count(o))
    t2, k = sim_move(t, 425, "le", True)
    i = t2.find(M425)
    print(name, 'move 425 ->', repr(t2[i - 40:i + len(M425) + 30]))
    t3, k = sim_move(t, 426, "ouverts \\(D_+(X_i)\\)", True)
    i = t3.find(M426)
    print(name, 'move 426 ->', repr(t3[i - 40:i + len(M426) + 50]))

io.open(OUT, 'w', encoding='utf-8', newline='\n').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
print('written', OUT, len(out), 'findings; all fixes unique:', ok)
from collections import Counter
c = Counter((f['page'], f['kind'] == 'misprint_in_print') for f in out)
for pg in (421, 422, 423, 424, 425):
    print(pg, c[(pg, False)], '/', c[(pg, True)])
