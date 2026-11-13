"""Build findings_636_640.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b636_640"
OUT = RUN / "findings_636_640.json"

MARK637 = "%%%%%%%%%%  scan idx 650  |  folio 637  %%%%%%%%%%"
M_OLD = "le morphisme d'inclusion.}\n" + MARK637 + "\n\\emph{On suppose que"
M_NEW = "le morphisme d'inclusion. On}\n" + MARK637 + "\n\\emph{suppose que"

F = []

F.append(dict(
    page=636,
    where="'L un faisceau inversible sur un X_T avec T de type fini sur S, qui limite L'",
    scan="'sur un X_T avec T de type fini sur S, qui limite' with no comma after X_T (both scans; crops_636_640/p636_XT.png, w636_XT_OX.png)",
    tex="'sur un \\(X_T\\), avec \\(T\\) de type fini sur \\(S\\), qui limite'",
    kind="punctuation", confidence="high",
    fix={"old": r"\(X_T\), avec", "new": r"\(X_T\) avec"},
    note="The TeX adds a comma the print does not have (the comma after 'sur S' is printed)."))

F.append(dict(
    page=636,
    where="the structure sheaf O_X, O_Y, O_{Y_s} on pp. 636-639 (convention of the Exposé XIII transcription, reported once for these pages; 8 places: p. 636 three, p. 638 one, p. 639 four)",
    scan="a plain typed capital O, not underlined, in every place: p. 636 'très ample O_X(1).', Théorème 3.8 'relativement ample O_Y(1)' and 'section φ de O_Y(1)'; p. 638 'φ_s est O_{Y_s}-régulier'; p. 639 'H=O_Y(m) un multiple de O_Y(1)', Lemme 3.11 'faisceau ample O_Y(1)' and 'section φ de O_Y(1)' (both scans; crops_636_640/p636_OX.png, w636_XT_OX.png; the underlines of the statements stop before the O)",
    tex="\\mathcal O in all 8 places",
    kind="font", confidence="medium",
    fix=None,
    note="CONVENTION, not itemized, as already reported for pp. 616-619 (findings_616_620.json, page 616): the TeX writes \\mathcal O for the print's plain typed O, as in SGA 5 Exposé VII (GLOBAL_ISSUES 89 (f)); not the pending underlined-O decision, since these O carry no underline. Three examples in the plain form: p. 636 'tr\\`es ample \\(\\mathcal O_X(1)\\)' -> 'tr\\`es ample \\(O_X(1)\\)'; p. 638 '\\(\\mathcal O_{Y_s}\\)-r\\'egulier' -> '\\(O_{Y_s}\\)-r\\'egulier'; p. 639 '\\(H=\\mathcal O_Y(m)\\)' -> '\\(H=O_Y(m)\\)'."))

F.append(dict(
    page=637,
    where="start of page (folio-637 marker)",
    scan="p. 636 ends with Théorème 3.8 '... et f : X → Y le morphisme d'inclusion. On' ('On' underlined, last word of the page); p. 637 begins 'suppose que pour tout point s ∈ S, et toute composante irréductible' (both scans: b636_640/page_636_s4.png, page_637_s1.png; crops_636_640/w_636_full.png, w_637_full.png)",
    tex="page_636.tex ends '... le morphisme d'inclusion.}'; the word 'On' stands under the folio-637 marker: page_637.tex begins '\\emph{On suppose que pour tout point'",
    kind="marker", confidence="high",
    fix=None,
    note="The folio-637 marker stands one word early: page 637 really begins at 'suppose que pour tout point'; 'On' belongs to p. 636. Exact edit in main.tex, both layers (the string occurs once in each; at the time of the check diplomatic and current lines 16162-16164, but the files are being edited, so find it by the string; simulated in memory on both layers): replace "
         + "\"" + M_OLD.replace("\n", "\\n") + "\" by \"" + M_NEW.replace("\n", "\\n") + "\""
         + ". The statement's \\emph stays split in two groups, as now, so each page's span keeps its braces balanced; the output is unchanged ('d'inclusion. On suppose que'). Do not use move_marker.py with the anchor 'suppose' here: it would put the marker inside the \\emph group."))

F.append(dict(
    page=637,
    where="Théorème 3.8, after the display f* : Pic_Y/S → Pic_X/S: 'est de type fini. / De plus, si S est intègre'",
    scan="'est de type fini.' stands on its own line; 'De plus, si S est intègre, il existe un ouvert non-vide U de' begins a new, indented paragraph (indented as 'Démontrons d'abord' on the same page; both scans: b636_640/page_637_s2.png, crops_636_640/w_637_full.png)",
    tex="'\\emph{est de type fini. De plus, si \\(S\\) est int\\`egre, ...' in one paragraph",
    kind="other", confidence="high",
    fix={"old": r"\emph{est de type fini. De plus, si", "new": "\\emph{est de type fini.}\n\n\\emph{De plus, si"},
    note="Missing paragraph break inside the statement; the continuation lines after the two displays ('est de type fini.', 'soit quasi-affine') start flush left and stay in their paragraphs."))

F.append(dict(
    page=637,
    where="Lemme 3.9, first line: 'Soient S un schema noethérien intègre'",
    scan="'un schema noethérien intègre': 'schema' without the acute accent (both scans; crops_636_640/p637_schema.png, w637_schema.png); the 'S-schéma' and 'un schéma intègre' of the same statement have it",
    tex="'un sch\\'ema noeth\\'erien int\\`egre': the TeX silently corrects",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"un sch\'ema noeth\'erien int\`egre", "new": r"un schema noeth\'erien int\`egre"},
    corrected=r"sch\'ema",
    note="Typing error of the print (accent left out). The fix restores the printed reading in the diplomatic layer."))

F.append(dict(
    page=638,
    where="'le morphisme fini et surjectif X'_K → X_K d'un S'_α-morphisme fini et surjectif X' → X_{S_α}'",
    scan="'d'un S'_α-morphisme': S with a prime and the index α (both scans; crops_636_640/p638_Salpha.png, w638_Salpha.png)",
    tex="'d'un \\(S'_\\alpha\\)-morphisme': the TeX keeps the printed reading",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"S_\alpha",
    note="X' is an S_α-schéma (previous line) and the morphism goes to X_{S_α}, so it is an S_α-morphisme; no S'_α is defined (S' is introduced later as an open subset of S_α). The current layer also has S'_\\alpha."))

F.append(dict(
    page=638,
    where="Remarque 3.10: '(par exemple si dim (X_K) ≤2, d'après Abhyankhar)'",
    scan="'d'après Abhyankhar)' (both scans; crops_636_640/p638_abhy.png, w638_abhy.png)",
    tex="'d'apr\\`es Abhyankhar)': the TeX keeps the printed reading",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected="Abhyankar",
    note="Misspelled name (S. Abhyankar, resolution of singularities in dimension 2); the TeX of the exposé's bibliography (folio 666) writes 'Abhyankar'. The current layer also has 'Abhyankhar'."))

F.append(dict(
    page=639,
    where="'restent bornés grâce à 2.10. Par conséquent'",
    scan="'graĉe': the circumflex stands over the c, not over the a (both scans; crops_636_640/p639_grace.png, w639_grace.png); the 'grâce à 1.13' four lines above has it over the a (w639_grace1.png)",
    tex="'born\\'es gr\\^ace \\`a 2.10': the TeX silently corrects",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"born\'es gr\^ace \`a 2.10", "new": r"born\'es gra\^ce \`a 2.10"},
    corrected=r"gr\^ace",
    note="Typing error of the print: the accent struck one letter late. The fix restores the printed reading in the diplomatic layer (as 'envoyè', GLOBAL_ISSUES 16)."))

F.append(dict(
    page=639,
    where="Lemme 3.11: 'Alors le morphisme Pic_Y/k → Pic_X/k (resp. le morphisme ...'",
    scan="the formula Pic_{Y/k} ⟶ Pic_{X/k} stands in the line, between 'Alors le morphisme' and '(resp. le morphisme', not displayed (both scans: b636_640/page_639_s3.png, crops_636_640/w_639_full.png)",
    tex="the statement's \\emph is closed after 'Alors le morphisme', the formula is a display \\[ ... \\], and '\\emph{(resp. le morphisme' reopens it",
    kind="other", confidence="medium",
    fix={"old": "Alors le morphisme}\n\\[\n\\Pic_{Y/k}\\longrightarrow\\Pic_{X/k}\n\\]\n\\emph{(resp. le morphisme",
         "new": "Alors le morphisme \\(\\Pic_{Y/k}\\longrightarrow\\Pic_{X/k}\\) (resp. le morphisme"},
    note="Display the print does not have. Independent of the Pic^τ fix that follows (no overlap)."))

F.append(dict(
    page=639,
    where="Lemme 3.11: '(resp. le morphisme Pic^τ_Y/k → Pic^τ_X/k (voir 4.1))'",
    scan="the superscript of both Pic is a typed Greek tau (a small T whose bar curls down at the left), the glyph of G^τ in 4.1 and of 'Pic^τ_X/S' in the title of § 4 (p. 643), not a capital T (both scans; crops_636_640/p639_pictau.png, w_639_full.png, w_643_full.png)",
    tex="'\\Pic^T_{Y/k}\\to\\Pic^T_{X/k}'",
    kind="symbol", confidence="high",
    fix={"old": r"\Pic^T_{Y/k}\to\Pic^T_{X/k}", "new": r"\Pic^\tau_{Y/k}\to\Pic^\tau_{X/k}"},
    note="Capital T for the print's τ; § 4 of the exposé writes \\Pic^\\tau (main.tex: \\Pic^\\tau_{X/S} in the § 4 title, \\underline{\\Pic}^\\tau further on in the section). These and the next two are the only \\Pic^T in main.tex (3 lines)."))

F.append(dict(
    page=639,
    where="last line: 'donc contenu dans Pic^τ_Y/k, donc est le même'",
    scan="Pic with the typed tau as superscript (both scans; crops_636_640/p639_pictau2.png, w_639_full.png)",
    tex="'contenu dans \\(\\Pic^T_{Y/k}\\)'",
    kind="symbol", confidence="high",
    fix={"old": r"contenu dans \(\Pic^T_{Y/k}\)", "new": r"contenu dans \(\Pic^\tau_{Y/k}\)"},
    note="As in Lemme 3.11 above."))

F.append(dict(
    page=640,
    where="first line: 'Comme Pic^τ_Y/k est propre, Y étant normal'",
    scan="Pic with the typed tau as superscript (both scans; crops_636_640/p640_pictau.png, w_640_full.png)",
    tex="'Comme \\(\\Pic^T_{Y/k}\\) est propre'",
    kind="symbol", confidence="high",
    fix={"old": r"Comme \(\Pic^T_{Y/k}\)", "new": r"Comme \(\Pic^\tau_{Y/k}\)"},
    note="As in Lemme 3.11 (p. 639): capital T for the print's τ."))

# checks
ok = True
for x in F:
    fx = x.get("fix")
    if fx is None:
        continue
    t = (B / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", x["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", x["page"])
    # simulate
    t2 = t.replace(fx["old"], fx["new"], 1)
    assert t2 != t
# marker edit simulated on both layers of main.tex
for layer in ("diplomatic", "current"):
    m = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6") / layer / "main.tex"
    t = m.read_text(encoding="utf-8")
    print(layer, "marker old count", t.count(M_OLD))
for x in F:
    if x["kind"] != "misprint_in_print":
        assert "corrected" not in x
    else:
        assert "corrected" in x
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print("written", OUT, len(F), "ok" if ok else "CHECK FAILED")
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
for p in range(636, 641):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
