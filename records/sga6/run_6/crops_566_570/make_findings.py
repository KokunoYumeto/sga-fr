"""Write findings_566_570.json and check that every fix's old string occurs exactly once in its page file,
and that the main.tex strings named in the marker notes occur once in each layer."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b566_570"
OUT = RUN / "findings_566_570.json"
SGA6 = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")

M568 = "%%%%%%%%%%  scan idx 581  |  folio 568  %%%%%%%%%%"
M570 = "%%%%%%%%%%  scan idx 583  |  folio 570  %%%%%%%%%%"
M571 = "%%%%%%%%%%  scan idx 584  |  folio 571  %%%%%%%%%%"
MARKER_EDITS = [
    ("(resp. \\(i_Y,j_Y\\)) les\n" + M568 + "\nmorphismes",
     "(resp. \\(i_Y,j_Y\\))\n" + M568 + "\nles morphismes"),
    ("résulte aussitôt de\n" + M570 + "\ncelle des carrés",
     "résulte aussi%\n" + M570 + "\ntôt de celle des carrés"),
    ("\\textbf{7.11.} On\n" + M571 + "\n",
     M571 + "\n\\textbf{7.11.} On\n"),
]


def mk(old, new):
    return {"old": old, "new": new}


F = []

# ---------------------------------------------------------------- p. 566
F.append(dict(
    page=566,
    where="end of the first paragraph, 'où on pose évidemment L_s = L|X_s.'",
    scan="L_s = L|X_s, with X_s on the line after the bar (both scans)",
    tex="\\(L_s=L|_{X_s}\\)",
    kind="formula", confidence="high",
    fix=mk("L|_{X_s}", "L|X_s"),
    note="Restriction with the subscript |_U where the print writes R|U (task rule: report each). The L's are "
         "underlined in the print (convention entry below)."))
F.append(dict(
    page=566,
    where="second paragraph, 'et on se réduit aussitôt au cas X_s intègre, donc D = nX_s'",
    scan="'intègre' underlined (both scans); 'localement intègre' two lines above is plain",
    tex="au cas \\(X_s\\) intègre",
    kind="underline", confidence="high",
    fix=mk("au cas \\(X_s\\) intègre", "au cas \\(X_s\\) \\emph{intègre}"),
    note="The TeX of this exposé writes the print's underlining as \\emph."))
F.append(dict(
    page=566,
    where="the invertible Module L and its restrictions L_t, L_s: all 13 places on p. 566",
    scan="L, L_t, L_s underlined in every place (both scans)",
    tex="plain \\(L\\), \\(L_t\\), \\(L_s\\)",
    kind="underline", confidence="high",
    fix=None,
    note="CONVENTION of the Exposé X TeX, not itemized (as reported for Exposés VI, VII and IX: findings_401_405, "
         "findings_441_445, findings_501_505, findings_506_510): letters the print underlines as Modules are written "
         "plain; the exposé has one \\underline{E} (folio 576) and no \\underline{L}. Places on p. 566: 'faisceau "
         "inversible \\(L_t\\) sur', 'faisceau inversible \\(L\\) sur', '\\cl(L_t)', '\\cl(L_s)\\in', 'L_s=L|_{X_s}' "
         "(both L's), '\\(\\cl(L_s)\\) ne dépend', 'choisi \\(L\\) de \\(L_t\\)', 'si \\(L_t\\simeq', 'alors "
         "\\(L_s\\simeq', 'que \\(L\\simeq', 'fortiori \\(L_s\\simeq'. Form if the diplomatic layer reproduces the "
         "underline: 'tout faisceau inversible \\(L_t\\) sur' -> 'tout faisceau inversible \\(\\underline{L}_t\\) "
         "sur'; 'choisi \\(L\\) de \\(L_t\\)' -> 'choisi \\(\\underline{L}\\) de \\(\\underline{L}_t\\)'; 'fortiori "
         "\\(L_s\\simeq' -> 'fortiori \\(\\underline{L}_s\\simeq'. The underlined O written \\mathcal O falls under "
         "the pending volume decision."))

# ---------------------------------------------------------------- p. 567
F.append(dict(
    page=567,
    where="after (7.9.3): 'De ceci on déduit formellement que si x est un élément de Gr.(X_t) (resp. de "
          "Gr˙(X_t)) tel que σ.(x) (resp. σ˙(x)) soit numériquement équivalent à zéro (4.5.1), alors il en est de "
          "même de x.'",
    scan="underlined word group by word group: 'si', 'est un élément de', 'resp', 'de', 'tel que', 'resp', 'soit "
         "numériquement équivalent à zéro', 'alors il en est de même de' (letters, formulas, (4.5.1) and the "
         "stops after resp not underlined; both scans)",
    tex="no emphasis",
    kind="underline", confidence="high",
    fix=mk("si \\(x\\) est un élément de \\(\\Gr_\\bullet(X_t)\\) (resp. de \\(\\Gr^\\bullet(X_t)\\)) tel que "
           "\\(\\sigma_\\bullet(x)\\) (resp. \\(\\sigma^\\bullet(x)\\)) soit numériquement équivalent à zéro "
           "(4.5.1), alors il en est de même de \\(x\\)",
           "\\emph{si} \\(x\\) \\emph{est un élément de} \\(\\Gr_\\bullet(X_t)\\) (\\emph{resp}. \\emph{de} "
           "\\(\\Gr^\\bullet(X_t)\\)) \\emph{tel que} \\(\\sigma_\\bullet(x)\\) (\\emph{resp}. "
           "\\(\\sigma^\\bullet(x)\\)) \\emph{soit numériquement équivalent à zéro} (4.5.1), \\emph{alors il en est "
           "de même de} \\(x\\)"),
    note="An underlined conclusion inside running text, not a numbered statement of the Exposé II pattern "
         "(GLOBAL_ISSUES 82); the TeX of this exposé writes such underlining as \\emph (folio 573: "
         "'\\emph{transforme éléments algébriquement équivalents à zéro ...}'), so itemized."))
F.append(dict(
    page=567,
    where="'est un épimorphisme mod.torsion, - circonstance qui n'est cependant réalisée'",
    scan="typed hyphen with spaces: ', - circonstance' (both scans)",
    tex="torsion, -- circonstance",
    kind="punctuation", confidence="high",
    fix=mk("torsion, -- circonstance", "torsion, - circonstance"),
    note="The TeX writes an en dash for the typist's hyphen (as fixed on pp. 81-82: 'commode~-- et' -> "
         "'commode~- et')."))
F.append(dict(
    page=567,
    where="'qui n'est cependant réalisée qu'assez exceptionellement.'",
    scan="exceptionellement, with one n (both scans)",
    tex="exceptionellement",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected="qu'assez exceptionnellement",
    note="Spelling slip of the typescript (as 'rationelle', p. 15). The TeX keeps the printed reading."))
F.append(dict(
    page=567,
    where="7.9.4, 'du moins lorsque f est propre et lisse, que la réciproque'",
    scan="'lisse' underlined (both scans)",
    tex="propre et lisse, que",
    kind="underline", confidence="high",
    fix=mk("propre et lisse, que", "propre et \\emph{lisse}, que"),
    note=""))
F.append(dict(
    page=567,
    where="7.9.4, 'ce qui impliquerait que les homomorphismes (7.9.1) induisent des monomorphismes pour les "
          "groupes quotients'",
    scan="'monomorphismes' underlined (both scans)",
    tex="induisent des monomorphismes",
    kind="underline", confidence="high",
    fix=mk("induisent des monomorphismes", "induisent des \\emph{monomorphismes}"),
    note=""))
F.append(dict(
    page=567,
    where="7.10, 'Donnons nous un morphisme'",
    scan="'Donnons nous', without hyphen (both scans)",
    tex="Donnons nous un morphisme",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="Donnons-nous un morphisme",
    note="The imperative takes the hyphen (as 'plaçons nous', p. 426, and 'montrons la', p. 464, in "
         "MISPRINTS_6). The TeX keeps the printed reading."))
F.append(dict(
    page=567,
    where="after 'g : X -> Y': 'de schémas noethériens et plats sur S, On désigne par σ_X'",
    scan="a comma after S, then the capital 'On' (both scans; crops_566_570/m567_surS_zoom.png, "
         "w567_surS_zoom.png)",
    tex="plats sur \\(S\\). On désigne",
    kind="misprint_in_print", confidence="high",
    fix=mk("plats sur \\(S\\). On", "plats sur \\(S\\), On"),
    corrected="plats sur \\(S\\). On",
    note="Typing error: the sentence ends at S (capital 'On'). The TeX silently corrects to a full stop; the fix "
         "restores the printed comma in the diplomatic layer."))

# ---------------------------------------------------------------- p. 568
F.append(dict(
    page=568,
    where="start of page (folio-568 marker)",
    scan="p. 567 ends '... et par i_X, j_X (resp. i_Y,j_Y)'; p. 568 begins 'les morphismes i,j pour X (resp. Y) "
         "des fibres spéciales' (both scans)",
    tex="page_567.tex ends '(resp. \\(i_Y,j_Y\\)) les' above the folio-568 marker; page_568.tex begins "
        "'morphismes \\(i,j\\)'",
    kind="marker", confidence="high",
    fix=None,
    note="Page 568 really begins at 'les morphismes'. Exact edit in main.tex, both layers (at the time of "
         "checking diplomatic line 14758, current 14763): replace '(resp. \\(i_Y,j_Y\\)) les\\n" + M568 +
         "\\nmorphismes' by '(resp. \\(i_Y,j_Y\\))\\n" + M568 + "\\nles morphismes' (old string once per layer). "
         "marker_split_word.py 'pull les' would join 'lesmorphismes': edit by hand."))
F.append(dict(
    page=568,
    where="'Supposons d'abord g propre. Je dis qu'alors le diagramme suivant est commutatif :'",
    scan="'propre' underlined (both scans)",
    tex="Supposons d'abord \\(g\\) propre.",
    kind="underline", confidence="high",
    fix=mk("Supposons d'abord \\(g\\) propre.", "Supposons d'abord \\(g\\) \\emph{propre}."),
    note=""))
F.append(dict(
    page=568,
    where="diagram (7.10.1), after K.(Y_s)",
    scan="no punctuation after the diagram (both scans; crops_566_570/m568_7101.png)",
    tex="K_\\bullet(Y_s).",
    kind="punctuation", confidence="high",
    fix=mk("&\nK_\\bullet(Y_s).", "&\nK_\\bullet(Y_s)"),
    note="The TeX adds a full stop at the end of the display. The prism (*) below has its printed full stop."))
F.append(dict(
    page=568,
    where="diagram (*) (the prism): the vertical arrows K.(X_t) -> K.(X_s) and K.(Y_t) -> K.(Y_s)",
    scan="a long unlabelled vertical arrow from K.(X_t) down to K.(X_s) at the left and one from K.(Y_t) down to "
         "K.(Y_s) at the right (the right one passes behind the g_* arrow), both scans "
         "(crops_566_570/m568_prism.png, w568_bot.png)",
    tex="only the arrows g_{t*}, g_*, g_{s*}, j_X^*, i_X^*, j_Y^*, i_Y^*",
    kind="missing", confidence="high",
    fix=mk("K_\\bullet(X_t) \\arrow[rr,\"g_{t*}\"] && K_\\bullet(Y_t)\\\\",
           "K_\\bullet(X_t) \\arrow[rr,\"g_{t*}\"] \\arrow[dd] && K_\\bullet(Y_t) \\arrow[dd]\\\\"),
    note="The two missing arrows are the specialisation maps (sides of the prism)."))

# ---------------------------------------------------------------- p. 569
F.append(dict(
    page=569,
    where="start of the page, 'Or ces deux carrés sont les carrés \"de changement de base\"'",
    scan="'Or ces deux carrés' indented: a new paragraph after the prism (*) of p. 568 (both scans)",
    tex="no blank line: the marker line follows '\\]' of (*) and 'Or ces' continues the paragraph",
    kind="other", confidence="high",
    fix=mk("Or ces\ndeux carrés", "\nOr ces\ndeux carrés"),
    note="Missing paragraph break. The blank line goes right after the marker line; the marker itself is "
         "unchanged."))

# ---------------------------------------------------------------- p. 570
F.append(dict(
    page=570,
    where="start of page (folio-570 marker)",
    scan="p. 569 ends '... Or la commutativité de ces carrés résulte aussi-'; p. 570 begins 'tôt de celle des "
         "carrés correspondants (7.10.0)' (both scans)",
    tex="page_569.tex ends 'résulte aussitôt de' above the folio-570 marker; page_570.tex begins 'celle des "
        "carrés'",
    kind="marker", confidence="high",
    fix=None,
    note="Page 570 really begins at 'tôt de celle', the second half of 'aussitôt' divided at the page break. Exact "
         "edit in main.tex, both layers (at the time of checking diplomatic line 14810, current 14815): replace "
         "'résulte aussitôt de\\n" + M570 + "\\ncelle des carrés' by 'résulte aussi%\\n" + M570 +
         "\\ntôt de celle des carrés' (old string once per layer; the split form of marker_split_word.py, the % "
         "joins the halves)."))
F.append(dict(
    page=570,
    where="'On peut aussi noter que si X et Y sont quasi-projectifs sur S à fibres régulières et séparés, alors "
          "f_t et f_s sont automatiquement des morphismes d'intersection complète (VIII 1.1)'",
    scan="f_t et f_s (both scans)",
    tex="\\(f_t\\) et \\(f_s\\)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="alors \\(g_t\\) et \\(g_s\\) sont automatiquement",
    note="Slip of the letter: 7.10 concerns g : X -> Y and its fibres g_t, g_s; the diagram 'analogue à "
         "(7.10.1 bis)' with Gr˙( )_Q needs g_{t*}, g_{s*}, so g_t and g_s must be complete intersection morphisms "
         "(f is the structure morphism X -> S of 7.9). The TeX keeps the printed f_t, f_s."))
F.append(dict(
    page=570,
    where="end of page (folio-571 marker): '\\textbf{7.11.} On'",
    scan="p. 570 ends '... compte tenu du résultat de compatibilité (VIII 3.2).'; p. 571 begins '7.11. On peut, "
         "pour un schéma T sur un corps k ...' (both scans; crops_566_570/m571_top.png, w571_top.png)",
    tex="page_570.tex ends with '\\textbf{7.11.} On' above the folio-571 marker",
    kind="marker", confidence="high",
    fix=None,
    note="Page 571 really begins at '\\textbf{7.11.} On' (a heading at the top of a page, not moved by the "
         "script). ALREADY APPLIED: while this batch was checked, main.tex was changed in both layers to '" + M571 +
         "\\n\\textbf{7.11.} On peut, pour un schéma' (verified at the time of writing); nothing to do. The edit "
         "was: replace '\\textbf{7.11.} On\\n" + M571 + "\\n' by '" + M571 + "\\n\\textbf{7.11.} On\\n'."))

for f in F:
    if f["kind"] != "misprint_in_print":
        f.pop("corrected", None)
    if not f.get("note"):
        f["note"] = ""

# order the keys as the task lists them
KEYS = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
F = [{k: f[k] for k in KEYS if k in f} for f in F]

ok = True
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    old = f["fix"]["old"]
    n = t.count(old)
    marker_cross = "%%%%%%%%%%" in old
    print(i, f["page"], f["kind"], "count", n, "CROSSES MARKER" if marker_cross else "")
    if n != 1 or marker_cross:
        ok = False
    # simulate
    t2 = t.replace(old, f["fix"]["new"], 1)
    assert t2 != t

for ed in ("diplomatic", "current"):
    t = (SGA6 / ed / "main.tex").read_text(encoding="utf-8")
    for j, (old, new) in enumerate(MARKER_EDITS):
        if j < 2:
            n = t.count(old)
            print(ed, "marker edit: old count", n, "new count", t.count(new), repr(old[:40]))
            if n != 1 or t.count(new) != 0:
                ok = False
        else:
            n = t.count(M571 + chr(10) + chr(92) + "textbf{7.11.} On peut")
            print(ed, "folio-571 marker already moved:", n == 1)
            if n != 1:
                ok = False

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "entries; all checks ok" if ok else "CHECK FAILED")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(566, 571):
    print(p, c[(p, False)], "/", c[(p, True)])
