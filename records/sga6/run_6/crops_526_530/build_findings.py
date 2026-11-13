import json, pathlib, re, sys, datetime
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b526_530"
OUT = RUN / "findings_526_530.json"
MAIN = {l: pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{l}\main.tex")
        for l in ("diplomatic", "current")}
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M526 = "%%%%%%%%%%  scan idx 539  |  folio 526  %%%%%%%%%%"
M529 = "%%%%%%%%%%  scan idx 542  |  folio 529  %%%%%%%%%%"
D529 = ("\\[\nD_Y(x)-D_Y(y)=\\dimdot\\mathcal O_{S,y'}-\\dimdot\\mathcal O_{S,x'}"
        "+\\degtr_{k(x')}k(x)-\\degtr_{k(y')}k(y).\n\\]\n")
MOVE526 = ("de $D$ sur $k(e)$, car ces\n" + M526 + "\npoints sont",
           "de $D$\n" + M526 + "\nsur $k(e)$, car ces points sont")
MOVE529 = ("On déduit\n" + M529 + "\nalors de (1.5.2) et (1.5.1) :\n" + D529 + "Puisque $S$ est caténaire, on a\n\\[\n",
           "On déduit\nalors de (1.5.2) et (1.5.1) :\n" + D529 + "Puisque $S$ est caténaire, on a\n" + M529 + "\n\\[\n")

# check the marker moves on both layers (in memory only)
stamp = datetime.datetime.fromtimestamp(MAIN["diplomatic"].stat().st_mtime).strftime("%H:%M:%S")
lines = {}
for layer, p in MAIN.items():
    t = p.read_text(encoding="utf-8")
    for key, (old, new) in (("526", MOVE526), ("529", MOVE529)):
        n = t.count(old)
        assert n == 1, (layer, key, n)
        k = t.find(old)
        lines[(layer, key)] = (t.count("\n", 0, k) + 1, t.count("\n", 0, k + len(old)) + 1)
        t = t.replace(old, new)
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) in (526, 529):
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            print(layer, m.group(2), "begins", repr(t[m.end():m.end() + 70]))


def L(layer, key):
    a, b = lines[(layer, key)]
    return f"{a}-{b}"


def js(s):
    """show a TeX string with \\n for line breaks, as in the notes of earlier batches"""
    return s.replace("\n", "\\n")


F = []
# ---------------------------------------------------------------- page 526
F.append(dict(
    page=526, where="start of page (folio-526 marker)",
    scan="p. 525 ends '... on peut trouver un point rationnel u de la fibre générique D_e de D'; p. 526 begins 'sur k(e), car ces points sont en correspondance biunivoque avec les' (both scans; b521_525/page_525_s4.png, b526_530/page_526_s1.png, crops_526_530/wit_526_half.png)",
    tex="page_525.tex ends '... de la fibre générique $D_e$ de $D$ sur $k(e)$, car ces' above the folio-526 marker; page_526.tex begins 'points sont en correspondance'",
    kind="marker", confidence="high", fix=None,
    note=("Page 526 really begins at 'sur $k(e)$, car ces'. Exact edit in main.tex, both layers (diplomatic lines "
          f"{L('diplomatic', '526')}, current {L('current', '526')}, main.tex as of {stamp}): replace '{js(MOVE526[0])}' by "
          f"'{js(MOVE526[1])}' (old string once per layer; simulated in memory: crops_526_530/build_findings.py). "
          "The sentence runs on, so no blank line. python -I move_marker.py 6 526 'sur $k(e)$, car ces' --before gives "
          "the same page split (it keeps the line break before 'points').")))
F.append(dict(
    page=526, where="'(EGA IV 5.4.1 (ii)).' / 'Les hypothèses du cas I'",
    scan="'Les hypothèses du cas I sont donc satisfaites' begins an indented new paragraph (both scans)",
    tex="the same paragraph: '(EGA IV 5.4.1(ii)). Les hypothèses'",
    kind="other", confidence="high",
    fix={"old": "(EGA IV 5.4.1(ii)). Les hypothèses", "new": "(EGA IV 5.4.1(ii)).\n\nLes hypothèses"},
    note="Paragraph break, as the p. 446 and p. 451-455 entries of earlier batches."))
F.append(dict(
    page=526, where="after (1.3.8): 'D'autre part l'homomorphisme canonique'",
    scan="indented new paragraph (both scans; 'On en conclut' and 'est un isomorphisme' after the other displays stand at the margin)",
    tex="\\end{equation} then 'D'autre part' on the next line (no blank line)",
    kind="other", confidence="high",
    fix={"old": "\\end{equation}\nD'autre part", "new": "\\end{equation}\n\nD'autre part"},
    note=""))
F.append(dict(
    page=526, where="letters the print underlines on pp. 526 and 529 (k of the residue field, E)",
    scan="underlined in the print (both scans; crops_526_530/p526_ke.png, p526_Ee.png, p529_154.png, w529_k.png): p. 526 both k of 'sur k(e)' and the E of 'l'espace vectoriel E_e'; p. 529 the k of 'deg.tr_{k(x')}' and of 'k(x)' in the second bracket of (1.5.4). Plain in the print: the k of (1.5.2), (1.5.3), of the display 'D_Y(x)-D_Y(y)= ...' at the foot of p. 528 and of the first bracket of (1.5.4); X, X', U, D, Y, Z, S, f, g, s",
    tex="all plain",
    kind="underline", confidence="high", fix=None,
    note=("Convention of the Exposé X transcription, as the Exposé VII entries (findings_451_455, findings_461_465): not itemized. "
          "p. 525 has the same (E, L_1, ..., L_n, k(e) underlined in the print, plain in the TeX). The underlined O of O_X, O_{X'}, "
          "O_{S,x}, O_{Z,y'}, O_{Y,y} (written \\mathcal O) falls under the pending structure-sheaf decision. "
          "The edits, in the form to use if the diplomatic layer reproduces the print: "
          "'sur $k(e)$, car ces' -> 'sur $\\underline{k}(e)$, car ces' (at present the end of page_525.tex, p. 526 after the marker move); "
          "page_526.tex 'sur $k(e)$. D'autre part' -> 'sur $\\underline{k}(e)$. D'autre part' and '$E_e$' -> '$\\underline{E}_e$'; "
          "page_529.tex '\\degtr_{k(x')}k(x)]' -> '\\degtr_{\\underline{k}(x')}\\underline{k}(x)]'. "
          "If adopted, edit 'sur $k(e)$, car ces' only after the folio-526 marker move, whose old string contains it.")))
# ---------------------------------------------------------------- page 527
F.append(dict(
    page=527, where="Remarque 1.4: 'des seules propriétés suivantes'",
    scan="'seules' underlined (both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix={"old": "des seules propriétés", "new": "des \\emph{seules} propriétés"},
    note="\\emph is the command of the Exposé X TeX for underlined words (\\emph{Démonstration :}, \\emph{nombre de Chern})."))
F.append(dict(
    page=527, where="Remarque 1.4: 'D(x) = D_Y(x) = dim({x})'",
    scan="dim({x}) without a bar over {x} (both scans; crops_526_530/p527_dim.png, w527_dim.png); the bars of s(U) on p. 526 and of {x} in (1.5.1) and 'Y = {x}' on p. 528 are clearly printed",
    tex="\\dim(\\overline{\\{x\\}})",
    kind="misprint_in_print", confidence="high",
    fix={"old": "\\dim(\\overline{\\{x\\}})", "new": "\\dim(\\{x\\})"},
    corrected="\\dim(\\overline{\\{x\\}})",
    note="The TeX silently corrects: the dimension function is the dimension of the closure of {x} (the print draws the bar in (1.5.1) and in 'Y = {x}' on p. 528); here it omits it."))
F.append(dict(
    page=527, where="after the list (i)-(iv): 'Cela signifie que tous les résultats'",
    scan="indented new paragraph (both scans)",
    tex="\\end{enumerate} then 'Cela signifie' on the next line (no blank line)",
    kind="other", confidence="high",
    fix={"old": "\\end{enumerate}\nCela signifie", "new": "\\end{enumerate}\n\nCela signifie"},
    note=""))
F.append(dict(
    page=527, where="Remarque 1.4, last paragraph 'Cela signifie que ... suivant une telle fonction D.'",
    scan=("underlined word group by word group (both scans): 'Cela signifie que tous les résultats de cette section', 'en particulier', "
          "'et', 'restent valables tels quels', 'si l'on y remplace la', 'dimension', 'par une fonction', 'satisfaisant aux conditions', "
          "'ci-dessus et si l'on définit la filtration de', 'suivant une telle fonction'; the references (1.3.2), (1.3.3), (i)à(iv), "
          "the letters D, K.(X), the quotes and the punctuation plain"),
    tex="the paragraph in roman",
    kind="underline", confidence="high", fix=None,
    note=("Exposé X follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision; Définition 2.1.1 on p. 531 is underlined "
          "the same way): not itemized. In the form to use if the diplomatic layer reproduces it: '\\emph{Cela signifie que tous les "
          "résultats de cette section}, \\emph{en particulier} (1.3.2) \\emph{et} (1.3.3), \\emph{restent valables tels quels}, "
          "\\emph{si l'on y remplace la} « \\emph{dimension} » \\emph{par une fonction} $D$ \\emph{satisfaisant aux conditions} "
          "(i)à(iv) \\emph{ci-dessus et si l'on définit la filtration de} $K_\\bullet(X)$ \\emph{suivant une telle fonction} $D$.'")))
# ---------------------------------------------------------------- page 528
F.append(dict(
    page=528, where="'Si f : Y_1 → Y_2 est un S-morphisme' after (1.5.2)",
    scan="indented new paragraph (both scans)",
    tex="\\end{equation} then 'Si $f:Y_1\\to Y_2$' on the next line (no blank line)",
    kind="other", confidence="high",
    fix={"old": "\\end{equation}\nSi $f:Y_1\\to Y_2$", "new": "\\end{equation}\n\nSi $f:Y_1\\to Y_2$"},
    note=""))
F.append(dict(
    page=528, where="'satisfont aux conditions (i)-(iv) de 1.4'",
    scan="(i)-(iv) with the typed hyphen (both scans)",
    tex="(i)--(iv)",
    kind="punctuation", confidence="high",
    fix={"old": "(i)--(iv)", "new": "(i)-(iv)"},
    note="En dash added by the TeX (watch list of 10 Nov)."))
# ---------------------------------------------------------------- page 529
F.append(dict(
    page=529, where="start of page (folio-529 marker)",
    scan=("p. 528 ends 'On déduit alors de (1.5.2) et (1.5.1) :', the display 'D_Y(x)-D_Y(y)= dim.O_{S,y'} - dim.O_{S,x'} + "
          "deg.tr_{k(x')}k(x)- deg.tr_{k(y')}k(y) .' and 'Puisque S est caténaire, on a'; p. 529 begins with the display "
          "'dim.O_{S,y'}-dim.O_{S,x'} = dim.O_{Z,y'} - dim.O_{Z,x'}' (both scans; b526_530/page_528_s3.png, page_528_s4.png, "
          "page_529_s1.png, crops_526_530/wit_529_half.png)"),
    tex="page_529.tex begins with 'alors de (1.5.2) et (1.5.1) :', the D_Y(x)-D_Y(y) display and 'Puisque $S$ est caténaire, on a' (five TeX lines that p. 528 prints); page_528.tex ends 'On déduit'",
    kind="marker", confidence="high", fix=None,
    note=("Page 529 really begins at the '\\[' of the display '\\dimdot\\mathcal O_{S,y'}-\\dimdot\\mathcal O_{S,x'}=...'. Exact edit "
          f"in main.tex, both layers (diplomatic lines {L('diplomatic', '529')}, current {L('current', '529')}, main.tex as of {stamp}): "
          f"replace '{js(MOVE529[0])}' by '{js(MOVE529[1])}' (the text itself unchanged; old string once per layer; simulated in "
          "memory: crops_526_530/build_findings.py).")))
F.append(dict(
    page=529, where="'On voit donc que (1.3.2) et (1.3.3) restent valables'",
    scan="indented new paragraph (both scans)",
    tex="\\] then 'On voit donc' on the next line (no blank line)",
    kind="other", confidence="high",
    fix={"old": "\\]\nOn voit donc", "new": "\\]\n\nOn voit donc"},
    note=""))
F.append(dict(
    page=529, where="'suivant la codimension des supports'",
    scan="'codimension' underlined (both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix={"old": "suivant la codimension des supports", "new": "suivant la \\emph{codimension} des supports"},
    note=""))
F.append(dict(
    page=529, where="'lorsque de plus X est biéqui-dimensionnel.'",
    scan="'biéqui-dimensionnel' underlined, the full stop plain (both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix={"old": "est biéqui-dimensionnel.", "new": "est \\emph{biéqui-dimensionnel}."},
    note=""))
F.append(dict(
    page=529, where="heading 1.6",
    scan="'1.6.' with its full stop, run into the text (both scans; crops_526_530/p529_head.png)",
    tex="\\subsection*{1.6}",
    kind="punctuation", confidence="high",
    fix={"old": "\\subsection*{1.6}", "new": "\\subsection*{1.6.}"},
    note=("As the p. 456 entry for 4.7 (findings_456_460). The whole Exposé X writes its headings without the print's full stop "
          "(\\subsection*{1.2} for the print's '1.2.' on p. 522, \\subsection*{1.3} for '1.3.' on p. 523, \\subsection*{2.1} for '2.1.' on p. 531; "
          "the other headings 1.1 to 5.3 are written the same way): a convention for one decision.")))
F.append(dict(
    page=529, where="1.6: 'une fonction D possédant la propriété (i)'",
    scan="'possè-dant' with a grave accent (both scans; crops_526_530/p529_possede.png, w529_possede.png; the acute accents of 'définir', 'propriété' on the same lines slope the other way)",
    tex="possédant",
    kind="misprint_in_print", confidence="high",
    fix={"old": "possédant", "new": "possèdant"},
    corrected="possédant",
    note="The TeX silently corrects."))
# ---------------------------------------------------------------- page 530
F.append(dict(
    page=530, where="start of page: 'Il est évidemment nécessaire'",
    scan="indented new paragraph after the (ii bis) clause that ends p. 529 (both scans)",
    tex="\\end{quote} (end of page_529.tex), the marker, then 'Il est' with no blank line",
    kind="other", confidence="high",
    fix={"old": "Il est\névidemment", "new": "\nIl est\névidemment"},
    note="The blank line then stands directly after the marker line; the marker itself is right (p. 530 begins with 'Il est')."))
F.append(dict(
    page=530, where="'que X soit biéquidimensionne (EGA 0_IV 14.3.3)'",
    scan="'biéquidimensionne' without the final l (both scans; crops_526_530/p530_bieq.png, wit_530_half.png)",
    tex="biéquidimensionne",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="biéquidimensionnel",
    note="The TeX keeps the printed reading; the current layer already has 'biéquidimensionnel'."))
F.append(dict(
    page=530, where="'idéaux maximaux m resp. m' de E' and 'les corps résiduels de m et m''",
    scan="m and m' typed with the m underlined (the prime outside), four times (both scans; crops_526_530/p530_m.png)",
    tex="\\mathfrak m, \\mathfrak m'",
    kind="font", confidence="high",
    fix={"old": "$\\mathfrak m$ resp. $\\mathfrak m'$ de $E$", "new": "$\\underline{m}$ resp. $\\underline{m}'$ de $E$"},
    note="As the SGA 6 entries for p_i and m_s (findings_176_180, findings_181_185, findings_186_190): the print's underlined letter, not Fraktur. Second edit in the next entry."))
F.append(dict(
    page=530, where="'Rappelons que les corps résiduels de m et m' sont isomorphes'",
    scan="m and m' with the m underlined (both scans)",
    tex="\\mathfrak m, \\mathfrak m'",
    kind="font", confidence="high",
    fix={"old": "de $\\mathfrak m$ et $\\mathfrak m'$ sont", "new": "de $\\underline{m}$ et $\\underline{m}'$ sont"},
    note="Same as the previous entry; the two edits do not overlap."))
F.append(dict(
    page=530, where="'et alors dans Z, Y_1 ∩ Y_2 = {y_1,y_2} est de dimension zéro'",
    scan="'dans Z,' (both scans; crops_526_530/p530_dansZ.png, wit_530_half.png)",
    tex="dans $Z$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="dans $X$",
    note="The TeX keeps the printed reading. No Z is defined in this example: Y_1 and Y_2 are the two irreducible components of the glued scheme X, and their intersection in X is {y_1, y_2}."))
F.append(dict(
    page=530, where="display 'D(y_1) = D(z_1) - 1 = D(y_2) - 1'",
    scan="no punctuation after the display (both scans; crops_526_530/p530_disp1.png, wit_530_half.png); the second display ends with its comma",
    tex="D(y_1)=D(z_1)-1=D(y_2)-1,",
    kind="punctuation", confidence="high",
    fix={"old": "D(y_1)=D(z_1)-1=D(y_2)-1,", "new": "D(y_1)=D(z_1)-1=D(y_2)-1"},
    note="Comma added at the end of the display (watch list of 10 Nov)."))

# validation: every fix's old occurs exactly once in its page file
ok = True
for f in F:
    fx = f.get("fix")
    if fx:
        t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
        n = t.count(fx["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", f["page"], n, repr(fx["old"]))
        if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
            ok = False
            print("MARKER IN FIX", f["page"])
    if f["kind"] != "misprint_in_print":
        f.pop("corrected", None)
    else:
        assert "corrected" in f
# order the keys as in the task
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
F = [{k: f[k] for k in order if k in f} for f in F]
assert ok
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(526, 531):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("written", OUT, len(F))
