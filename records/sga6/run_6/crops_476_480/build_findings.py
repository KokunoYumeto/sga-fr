"""Build and check findings_476_480.json.
Checks: every fix's old string occurs exactly once in its page file (also after the earlier fixes of the page, in
order), no old/new touches a marker line; the main.tex marker edits quoted in the p. 478 marker note occur once in
each layer, and after them (and after the p. 477 diagram-rows fix) each page starts and ends where the print does."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
SGA6 = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = "\u23ce"  # placeholder for a line break inside raw strings


def T(s):
    return s.replace(NL, "\n")


pages = {n: open(RUN + rf"\b476_480\page_{n}.tex", encoding="utf-8", newline="").read() for n in range(476, 481)}

# the three rows of the p. 478 diagram, as they stand in page_477.tex
p477 = pages[477]
r0 = p477.index(r'B\otimes_A B \arrow[r,"p\otimes p"]')
r1 = p477.index("{} & C & {}") + len("{} & C & {}")
OLD_ROWS = p477[r0:r1]
NEW_ROWS = T(r'''B\otimes_A B \arrow[r,"p\otimes p"] \arrow[d,"\Delta"'] \arrow[dr,phantom,"(1)"] & B'\otimes_A B' \arrow[d,"\Delta"]\\⏎B \arrow[r,"p"] \arrow[dr,"i"'] & B' \arrow[d,"j"'] \arrow[dr,"i'","(2)"' near start] & B'\otimes_B B' \arrow[l,"\Delta"'] \arrow[d]\\⏎{} & C \arrow[r,shift right=.7ex,"p'"'] & B'\otimes_B C = B'/IB'. \arrow[l,shift right=.7ex,"j'"']''')

MARK478 = "%%%%%%%%%%  scan idx 491  |  folio 478  %%%%%%%%%%"
MEDIT = [
    (MARK478 + "\n" + r"\end{tikzcd}", r"\end{tikzcd}"),
    ("les idéaux correspondants. On a le diagramme :\n" + "\\[\n",
     "les idéaux correspondants. On a le diagramme :\n" + MARK478 + "\n" + "\\[\n"),
]


def q(s):
    """quote an edit string for a note: line breaks as \\n"""
    return s.replace("\n", "\\n")


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 476
add(476,
    "statements of pp. 476-480: Proposition 2.2 (p. 476), Définition 2.3 and Proposition 2.4 (p. 478; 2.4 ends on p. 479), Corollaire 2.5 (p. 479), Proposition 2.6 with its condition (G) and its conclusion (pp. 479-480)",
    "underlined word group by word group (both scans): Prop. 2.2 'Le complexe', 'ne dépend pas', 'à un isomorphisme canonique près dans la catégorie dérivée', 'de la factorisation choisie par un', 'schéma lisse'; Déf. 2.3 'Soit', 'un morphisme lissifiable', 'Le complexe', 'défini à isomorphisme canonique près dans la catégorie dérivée', 'est appelé', 'de', 'sur', 'ou de' (the defined term 'complexe cotangent relatif' is left plain); Prop. 2.4 'Soit', 'un morphisme d'intersection complète', 'lissifiable', 'Alors', 'est parfait', 'Plus précisément', 'pour toute', p. 479 'factorisation de', 'comme composé d'une immersion et d'un morphisme lisse', 'le complexe', 'défini en', 'est strictement parfait'; Cor. 2.5 'Soit', 'un morphisme d'intersection complète', 'lissifiable', 'et', 'une factorisation de', 'par un', 'schéma lisse', 'Soit', 'l'idéal de', 'définissant', 'Alors', 'si', 'désigne le groupe de', 'Grothendieck des', '-Modules localement libres de type fini', 'resp', 'des complexes parfaits sur', 'l'élément', 'défini par', 'ne dépend pas de la factorisation de', 'choisie', 'La valeur en un point', 'de', 'de l'augmentation de', 'n'est autre que la dimension relative virtuelle', 'de', 'sur', 'au point'; Prop. 2.6 'Soient', 'et', 'deux morphismes d'intersection complète lissifiables', 'et supposons de plus la condition suivante remplie', p. 480 (G) 'Il existe un', 'schéma lisse', 'factorisant', 'tel que pour toute', 'immersion fermée', 'on puisse trouver un', 'schéma lisse', 'avec', 'cette condition est en particulier remplie si', 'est quasi-projectif et si', 'a un faisceau ample', 'en prenant pour', 'un', then 'Alors', 'est d'intersection complète', 'lissifiable', 'et on a un triangle distingué'; formulas, numbers and punctuation plain; the labels underline only the word",
    "the statements in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé VIII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as Exposés VI and VII do (findings_401_405, findings_416_420, findings_431_435): not itemized; the word groups are listed for the scripted pass. The TeX adds no emphasis on defined terms here (Déf. 2.3's 'complexe cotangent relatif' is plain in the print and in the TeX). No category letter on pp. 476-480.")

add(476,
    "letters of sheaves and complexes on pp. 476-480",
    "underlined in the print (both scans): the L of every cotangent complex L.^{X/Y}, L.^{Y/Z}, L.^{X/Z} (11 places: Prop. 2.2 and 'les complexes L.' on p. 476; a) twice on p. 477; Déf. 2.3 and Prop. 2.4 on p. 478; Prop. 2.4 and 'resp. T_f = cl(L.)' on p. 479; the three vertices of the triangle on p. 480); the ideal sheaves I, J, J', K: I/I^2 → J/J^2 and the (2.2.1) square (p. 476), 'Soient I, J, K', p^*(I), i'^*(p^*(I)) = p'^*(I/I^2), (2.2.3) and the K/K^2 of b) (p. 477), I/I^2 → J/J^2 and K/K^2 of the two 'L'homomorphisme' (p. 478), 'Si J est l'Idéal', J/J^2, 'Soit J l'idéal', cl(J/J^2) (p. 479), every I, J, J', K of p. 480; the Ω of every sheaf of differentials Ω^1_{V/Y}, Ω^1_{V'/Y}, Ω^1_{V'/V}, Ω^1_{V'/Z}, Ω^1_{V''/Z}, Ω^1_{V''/V'} (pp. 476-480). Plain in the print: the ring-level letters of p. 478 (IB' → J, p : I → J, the K/K^2 of 'soit x̄ ∈ K/K^2', J, K = J/IB', H, H/H^2, the K/K^2 of H/H^2⊗C → K/K^2, Ω_{B'/A}, Ω^1_{B'/B})",
    "all plain",
    "underline", "high", None,
    "Convention of the Exposé VIII transcription (no \\underline at all in folios 466-480), as the sheaf letters of Exposés VI and VII (findings_411_415, findings_431_435): not itemized; no blind script (the ring-level letters of p. 478 are plain in the print). The volume's notation index writes this complex underlined (main.tex: '\\(\\underline L_{\\cdot}^{X/Y}\\) & VIII & 2.1'). Three examples, in the form to use if the diplomatic layer reproduces the underline: p. 476 'p^*(\\Omega^1_{V/Y})\\longrightarrow\\Omega^1_{V'/Y},' -> 'p^*(\\underline{\\Omega}^1_{V/Y})\\longrightarrow\\underline{\\Omega}^1_{V'/Y},'; p. 477 'Soient $I,J,K$ les idéaux' -> 'Soient $\\underline{I},\\underline{J},\\underline{K}$ les idéaux'; p. 479 'le complexe $L^{X/Y}_\\bullet$ défini en 2.1' -> 'le complexe $\\underline{L}^{X/Y}_\\bullet$ défini en 2.1'. The underlined O of O_V, O_X written \\mathcal O falls under the pending volume decision.")

add(476,
    "after 'et p un morphisme lisse.': 'Par fonctorialité, on obtient alors des homomorphismes :'",
    "'Par fonctorialité' begins a new, indented paragraph (both scans)",
    "'... un morphisme lisse. Par fonctorialité, ...' in one paragraph",
    "other", "medium",
    ("morphisme lisse. Par fonctorialité", T("morphisme lisse.⏎⏎Par fonctorialité")),
    "")

add(476,
    "after the diagram (2.2.1): 'Comme V et V' sont lisses sur Y, on obtient la suite exacte :'",
    "indented: a new paragraph (both scans); the later 'Comme les Modules de différentielles ...' is not indented",
    "'\\end{equation}' followed directly by 'Comme $V$ et $V'$' (no blank line)",
    "other", "medium",
    (T(r"\end{equation}⏎Comme $V$ et $V'$"), T(r"\end{equation}⏎⏎Comme $V$ et $V'$")),
    "")

add(476,
    "triangle after 'au-dessus de Y :', label i of X → V",
    "i stands above the arrow X → V, inside the triangle, under the diagonal j (both scans; crops_476_480/m476_triangle.png)",
    "\\arrow[r,\"i\"'] (label below the arrow)",
    "formula", "medium",
    (r'\arrow[r,"i"'+"'"+r'] & V,', r'\arrow[r,"i"] & V,'),
    "")

add(476,
    "'Comme les Modules de différentielles considérés sont localement libres sur O_V'",
    "O_V: underlined O, index V without prime (both scans; crops_476_480/w476_b.png)",
    "$\\mathcal O_V$ (the printed reading)",
    "misprint_in_print", "medium", None,
    "The Modules of the sequence, p^*(Ω^1_{V/Y}), Ω^1_{V'/Y}, Ω^1_{V'/V}, are O_{V'}-Modules, and j^* is applied to them (j : X → V'): the print drops the prime. The diplomatic TeX keeps the printed reading; the current layer already reads \\mathcal O_{V'}.",
    corrected="$\\mathcal O_{V'}$")

# ---------------------------------------------------------------- p. 477
add(477,
    "start of p. 477: 'Par ailleurs, j définit une section j' de X' = V'x_VX :'",
    "indented: a new paragraph after the display (2.2.2) that ends p. 476 (both scans)",
    "page_476.tex ends '\\end{equation}' and page_477.tex begins 'Par' with no blank line between, so 'Par ailleurs' continues the paragraph",
    "other", "medium",
    (T("Par⏎ailleurs, $j$"), T("⏎Par⏎ailleurs, $j$")),
    "The blank line goes after the marker line (a comment), so the edit leaves the marker alone.")

add(477,
    "diagram after 'X' = V'x_VX :', label i of X → V",
    "i stands above the arrow X → V, inside the triangle under the diagonal j (both scans; crops_476_480/m477_square.png)",
    "\\arrow[r,\"i\"'] (label below the arrow)",
    "formula", "medium",
    (r'X \arrow[r,"i"'+"'"+r'] \arrow[ur,"j"]', r'X \arrow[r,"i"] \arrow[ur,"j"]'),
    "")

add(477,
    "same diagram, label of the curved section arrow j' : X → X'",
    "j' stands to the right of the curved arrow, which bulges to the right of p' (both scans; crops_476_480/m477_square.png)",
    "\\arrow[u,\"j'\",bend right]: the label sits on the inner (left) side of the curve, between it and p'",
    "formula", "medium",
    (r'''\arrow[u,"j'",bend right]''', r'''\arrow[u,"j'"',bend right]'''),
    "")

add(477,
    "'Nous allons montrer : a) que le diagramme (2.2.1) est commutatif'",
    "'Nous allons montrer :' ends its line; 'a) que le diagramme ...' begins a new, indented paragraph (both scans)",
    "'Nous allons montrer : a) que' run on in one paragraph",
    "other", "medium",
    ("Nous allons montrer : a) que", T("Nous allons montrer :⏎⏎a) que")),
    "")

add(477,
    "'... défini par V' ; b) que l'homomorphisme : K/K^2 → j^*(Ω^1_{V'/V})'",
    "'b) que l'homomorphisme ...' begins a new, indented paragraph (both scans)",
    "run on after 'défini par $V'$ ;'",
    "other", "medium",
    ("défini par $V'$ ; b) que", T("défini par $V'$ ;⏎⏎b) que")),
    "")

add(477,
    "b): 'cela entrainera que le mapping cylinder de θ est acyclique'",
    "'entrainera', the i without circumflex (both scans; crops_476_480/m477_entrainera.png, w477_bottom.png)",
    "entrainera (the printed reading)",
    "misprint_in_print", "medium", None,
    "The spelling of 1971 is 'entraînera' (the typewriter has î: 'coîncide', p. 478). The diplomatic TeX keeps the printed reading; the current layer already reads 'entraînera'.",
    corrected="entraînera")

add(477,
    "the diagram after 'On a le diagramme :' (printed at the top of p. 478; its three rows stand in page_477.tex, above the misplaced folio-478 marker)",
    "rows: B⊗_A B --p⊗p--> B'⊗_A B' / B --p--> B' <--Δ-- B'⊗_B B' / C and B'⊗_B C = B'/IB'. Arrows: Δ : B⊗_A B → B (label left) and Δ : B'⊗_A B' → B' (label right), '(1)' inside the square they make with p⊗p and p; i : B → C (label below left); j : B' → C (label left); i' : B' → B'⊗_B C (label above right), '(2)' between j and i'; the unlabelled B'⊗_B B' → B'⊗_B C; two parallel arrows between C and B'⊗_B C: j' above, pointing to C, labelled above, and p' below, pointing to B'⊗_B C, labelled below; a full stop after B'/IB' (both scans; crops_476_480/m478_diag_a.png, w478_tophalf.png, w478_bottomarrows.png)",
    "B'⊗_B B' in the top row with its Δ arrow pointing to B'⊗_A B'; B'⊗_B C = B'/IB' in the middle row with one arrow p' to C; no arrow i', no arrow j', no '(1)' or '(2)', no full stop; j labelled on the right",
    "formula", "high",
    (OLD_ROWS, NEW_ROWS),
    "The text cites both squares ('se déduit du carré commutatif (1)', 'le carré commutatif (2) donne un homomorphisme : H → K', p. 478); p' : C → B'⊗_B C and j' : B'⊗_B C → C are the ring maps of p' : X' → X and of the section j' of p. 477. The edit rewrites the three rows only (\\[, \\begin{tikzcd}[...] and \\end{tikzcd} stay). Apply it to page 477's text before the folio-478 marker is moved (marker entry of p. 478); after the move these rows belong to p. 478. 'shift right=.7ex' is the form main.tex uses for parallel arrows (folio 611); phantom and near start are tikz-cd options.")

# ---------------------------------------------------------------- p. 478
add(478,
    "start of page (folio-478 marker)",
    "p. 477 ends with 'On a le diagramme :' and blank space below it; p. 478 begins with that diagram (B⊗_A B --p⊗p--> B'⊗_A B' ...), then 'L'homomorphisme I/I^2 → J/J^2 se déduit ...' (both scans; crops_476_480/w477_bottom.png, w478_tophalf.png)",
    "the folio-478 marker stands inside the tikzcd, after the row '{} & C & {}' and before '\\end{tikzcd}'; page_478.tex begins '\\end{tikzcd}' and '\\]'",
    "marker", "high", None,
    "Page 478 really begins at the '\\[' that opens the diagram after 'On a le diagramme :'. Exact edits in main.tex, both layers (at 16:15: diplomatic lines 12245-12251, current 12251-12257; the files were changing): replace '"
    + q(MEDIT[0][0]) + "' by '" + q(MEDIT[0][1]) + "', and replace '" + q(MEDIT[1][0]) + "' by '" + q(MEDIT[1][1])
    + "' (each old string once per layer; simulated: crops_476_480/build_findings.py). Apply the p. 477 diagram-rows entry first: its old string lies in page 477's text until the marker moves.")

add(478,
    "after the diagram: 'L'homomorphisme I/I^2 → J/J^2 se déduit de l'homomorphisme : IB' → J'",
    "indented: a new paragraph (both scans)",
    "'\\]' followed directly by 'L'homomorphisme' (no blank line)",
    "other", "medium",
    (T(r"\]⏎L'homomorphisme $I/I^2"), T(r"\]⏎⏎L'homomorphisme $I/I^2")),
    "")

add(478,
    "'l'homomorphisme composé : J --d--> Ω_{B'/A}⊗_{B'}C → Ω^1_{B'/B}⊗_{B'}C'",
    "the first Ω has no superscript 1 (Ω_{B'/A}⊗_{B'}C); the second has it (Ω^1_{B'/B}) (both scans; crops_476_480/w478_omega.png)",
    "\\Omega^1_{B'/A}",
    "formula", "high",
    (r"J\xrightarrow{d}\Omega^1_{B'/A}", r"J\xrightarrow{d}\Omega_{B'/A}"),
    "The TeX adds the index; Ω_{B'/A} = Ω^1_{B'/A}, so the print is not wrong here.")

add(478,
    "'L'homomorphisme : K/K^2 → j^*(Ω^1_{V'/V}) considéré dans b) peut-être défini comme suit'",
    "'peut-être' with a hyphen (both scans)",
    "peut-être (the printed reading)",
    "misprint_in_print", "medium", None,
    "The verb 'peut' with 'être défini' is meant, not the adverb 'peut-être'. The diplomatic TeX keeps the printed reading; the current layer already reads 'peut être'.",
    corrected="peut être")

# ---------------------------------------------------------------- p. 479
add(479,
    "Corollaire 2.5, second display '(resp. T_f = cl(L.^{X/Y}) )'",
    "one centred display line '(resp. T_f = cl(L.^{X/Y}) )', the parenthesis and 'resp.' inside it, under the display T_f = cl(i^*(Ω^1_{V/Y})) - cl(J/J^2); then 'ne dépend pas ...' at the margin (both scans; crops_476_480/w479_a.png)",
    "'(resp.' as a text line before the display T_f=\\operatorname{cl}(L^{X/Y}_\\bullet) and ')' as a text line after it",
    "other", "medium",
    (T(r"(resp.⏎\[⏎T_f=\operatorname{cl}(L^{X/Y}_\bullet)⏎\]⏎)"),
     T(r"\[⏎(\text{resp. }T_f=\operatorname{cl}(L^{X/Y}_\bullet))⏎\]")),
    "")

# ---------------------------------------------------------------- p. 480
add(480,
    "triangle of Proposition 2.6, lower left vertex Lf^*(L.^{Y/Z})",
    "the L of Lf^* is doubly underlined, the derived functor's double-struck L (both scans; crops_476_480/w480_a.png)",
    "plain L",
    "font", "high",
    (r"Lf^*(L^{Y/Z}_\bullet)", r"\mathbb Lf^*(L^{Y/Z}_\bullet)"),
    "The form of the same triangle in Exposé VII (main.tex '\\mathbb Lf^*(\\mathbb Rf_*(M^\\bullet))') and of the doubly underlined P on this page (\\mathbb P^r_Y).")

add(480,
    "the same triangle, after L.^{X/Z}",
    "a full stop after L.^{X/Z} (both scans)",
    "no full stop",
    "punctuation", "high",
    (r"L^{X/Z}_\bullet \arrow[ul]", r"L^{X/Z}_\bullet . \arrow[ul]"),
    "")

add(480,
    "after the triangle: 'Soit V' un Z-schéma lisse factorisant g.'",
    "indented: a new paragraph (both scans)",
    "'\\]' followed directly by 'Soit $V'$' (no blank line)",
    "other", "medium",
    (T(r"\]⏎Soit $V'$"), T(r"\]⏎⏎Soit $V'$")),
    "")

add(480,
    "after the diagram X → V → V'': 'Alors l'immersion j' est régulière'",
    "indented: a new paragraph (both scans)",
    "'\\]' followed directly by 'Alors l'immersion' (no blank line)",
    "other", "medium",
    (T(r"\]⏎Alors l'immersion"), T(r"\]⏎⏎Alors l'immersion")),
    "")

add(480,
    "after (2.6.1): 'Par ailleurs, V' et V'' étant lisses sur Z, on a la suite exacte :'",
    "indented: a new paragraph (both scans)",
    "'\\end{equation}' followed directly by 'Par ailleurs' (no blank line)",
    "other", "medium",
    (T(r"\end{equation}⏎Par ailleurs"), T(r"\end{equation}⏎⏎Par ailleurs")),
    "")

# ---------------------------------------------------------------- checks
ok = True
counts = {}
for i, x in enumerate(F):
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
    if (x["kind"] == "misprint_in_print") != ("corrected" in x):
        print("corrected key wrong", i); ok = False
    f = x["fix"]
    if f is None:
        continue
    k = pages[x["page"]].count(f["old"])
    if k != 1:
        print("entry", i, "page", x["page"], "old occurs", k, repr(f["old"][:80])); ok = False
    if MARK.search(f["old"]) or MARK.search(f["new"]):
        print("entry", i, "touches a marker"); ok = False
work = dict(pages)
for i, x in enumerate(F):
    f = x["fix"]
    if f is None:
        continue
    t = work[x["page"]]
    if t.count(f["old"]) != 1:
        print("sequential: entry", i, "old occurs", t.count(f["old"])); ok = False
        continue
    work[x["page"]] = t.replace(f["old"], f["new"])
print("page fixes:", "OK" if ok else "PROBLEMS")
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})

for layer in ("diplomatic", "current"):
    t = open(SGA6 + "\\" + layer + r"\main.tex", encoding="utf-8", newline="").read()
    # the p. 477 rows fix first (it lies in page 477's region now)
    k = t.count(OLD_ROWS)
    print(layer, "rows old occurs", k)
    if k == 1:
        t = t.replace(OLD_ROWS, NEW_ROWS)
    else:
        ok = False
    for o, nw in MEDIT:
        k = t.count(o)
        print(layer, "marker edit old occurs", k)
        if k != 1:
            ok = False
            continue
        t = t.replace(o, nw)
    ms = list(MARK.finditer(t))
    for j, m in enumerate(ms):
        fo = int(m.group(2))
        if 476 <= fo <= 481:
            body = t[m.end():ms[j + 1].start()] if j + 1 < len(ms) else t[m.end():]
            body = body.strip("\n")
            print("  ", layer, fo, "starts", repr(body[:60]), "| ends", repr(body[-60:]))
print("ALL OK" if ok else "PROBLEMS FOUND")

json.dump(F, open(RUN + r"\findings_476_480.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("written", len(F), "entries")
