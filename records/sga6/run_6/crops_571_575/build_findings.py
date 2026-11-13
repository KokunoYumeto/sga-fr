"""Build findings_571_575.json; '§' stands for a TeX backslash (so '§n' in a note is a written line break).
Checks that every fix's old string occurs exactly once in its page_NNN.tex and that a page's fixes apply in sequence."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b571_575"
OUT = RUN / "findings_571_575.json"

M571 = "%%%%%%%%%%  scan idx 584  |  folio 571  %%%%%%%%%%"
M572 = "%%%%%%%%%%  scan idx 585  |  folio 572  %%%%%%%%%%"
M575 = "%%%%%%%%%%  scan idx 588  |  folio 575  %%%%%%%%%%"

def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d

L = []
# ---------------- page 571
L.append(F(571, "start of page (folio-571 marker)",
  "p. 571 begins with the heading line '7.11. On peut, pour un schéma T sur un corps k algébriquement clos, définir' "
  "(both scans: b571_575/page_571_s1.png; crops_571_575/wit_571_half.png)",
  "'§textbf{7.11.} On' stands above the folio-571 marker (end of page_570.tex); page_571.tex begins 'peut, pour un schéma'",
  "marker", "high", None,
  "Page 571 really begins at '§textbf{7.11.} On peut,'. A heading at the top of the page, so the 10 Nov script left it. "
  "Exact edit in main.tex, both layers (diplomatic about line 14833, current about line 14838 at 16:27 on 13 Nov; the file is being edited, "
  "use the string; it occurs once per layer): replace '§textbf{7.11.} On§n" + M571 + "§npeut, pour un schéma' by '"
  + M571 + "§n§textbf{7.11.} On peut, pour un schéma' (simulated in memory: crops_571_575/sim_markers.py). "
  "The blank line before the heading stays above the marker (new paragraph in the print)."))
L.append(F(571, "7.11, second line: 'des éléments algébriquement équivalents à zéro comme'",
  "'algébriquement équivalents à zéro' underlined (both scans), the term being defined",
  "plain 'algébriquement équivalents à zéro'",
  "underline", "high",
  ("éléments algébriquement équivalents à zéro comme", "éléments §emph{algébriquement équivalents à zéro} comme"),
  "The file writes the typescript's underline as §emph in this exposé (7.12 on p. 573)."))
# ---------------- page 572
L.append(F(572, "start of page (folio-572 marker)",
  "p. 571 ends '... en prenant ci-dessus E dans K.(Tx_kC), et'; p. 572 begins 'en notant que i_x: T ⟶ Tx_kC est un morphisme parfait' "
  "(both scans: page_571_s4.png, page_572_s1.png; crops_571_575/wit_571_half.png, wit_572_half.png)",
  "page_571.tex ends 'et en' above the folio-572 marker; page_572.tex begins 'notant que'",
  "marker", "high", None,
  "Page 572 really begins at 'en notant que'. Exact edit in main.tex, both layers (diplomatic about line 14849, current about line 14854 "
  "at 16:27 on 13 Nov; use the string, it occurs once per layer): replace 'et en§n" + M572 + "§nnotant que' by 'et§n" + M572
  + "§nen notant que' (simulated in memory: crops_571_575/sim_markers.py). The sentence runs on, so no blank line."))
L.append(F(572, "first line: 'est un morphisme parfait, car déduit'",
  "'parfait' underlined (both scans)",
  "plain 'parfait'",
  "underline", "high",
  ("morphisme parfait, car", "morphisme §emph{parfait}, car"),
  "Only the first 'parfait' of the sentence is underlined; 'qui est parfait grâce à' is plain in the print."))
L.append(F(572, "7.11.6: 'en prenant ci-dessus C géométriquement connexe sur k'",
  "'géométriquement' underlined (both scans)",
  "plain 'géométriquement'",
  "underline", "high",
  ("§(C§) géométriquement connexe", "§(C§) §emph{géométriquement} connexe"),
  ""))
L.append(F(572, "'le produit d'un éléments de K˙(T)'",
  "'le produit d'un éléments de K˙(T) par un élément de K.(T)' (both scans)",
  "'le produit d'un éléments de §(K^§bullet(T)§)': the TeX keeps the printed reading",
  "misprint_in_print", "high", None,
  "Typing error (plural after 'un'). The current layer already reads 'd'un élément'.",
  corrected="d'un élément"))
# ---------------- page 574
L.append(F(574, "first line: 'les immersions x_i : S ⟶ X (i=0,1)'",
  "'suite les immersions x_i : S ⟶ X (i=0,1) sont régulières' (both scans; crops_571_575/m574_SX.png, wit_574_half.png)",
  "'§(x_i:S§to X§)': the TeX keeps the printed reading",
  "misprint_in_print", "high", None,
  "The x_i are the sections of C over S (C lisse sur S en les points de x_0(S), x_1(S)), so the regular immersions are S → C, "
  "and they become x_i: s → C_s after the base change s → S. The current layer already reads '§(x_i:S§to C§)'.",
  corrected="§(x_i:S§to C§)"))
L.append(F(574, "'provient de l'élément E(x_1)-E(x_o) de K.(Xx_SC)'",
  "'K.(X_t) provient de l'élément E(x_1)-E(x_o) de K.(Xx_SC), et par suite son image' (both scans; crops_571_575/m574_KXSC.png)",
  "'de §(K_§bullet(X§times_SC)§)' after '§(E(x_1)-E(x_0)§)': the TeX keeps the printed reading",
  "misprint_in_print", "medium", None,
  "E(x) = i_x^*(E) with i_x: X → X×_S C (next display), so E(x_1)-E(x_0) lies in K.(X); (*) applies i^* (i: X_s → X) to it. "
  "The 'K.(Xx_SC)' repeats the group of E from the line above. The current layer still has the printed reading.",
  corrected="de §(K_§bullet(X)§)"))
L.append(F(574, "after the display (*): 'Bien entendu, pour une section x de C sur S, on pose'",
  "'Bien entendu' continues flush left after (*), not indented (both scans), like 'on trouve que' and 'Comme k(s)' after the next two displays; "
  "the typescript indents its new paragraphs ('Pour le voir' p. 573, 'Lorsqu'on suppose' p. 575)",
  "blank line between '§]' and 'Bien entendu' (a new, indented paragraph)",
  "other", "medium",
  ("§]\n\nBien entendu", "§]\nBien entendu"),
  "Extra paragraph break."))
L.append(F(574, "diagram, lower right corner: 'X_s x_{k(x)} C_s'",
  "'X_s x_{k(x)} C_s' (both scans; crops_571_575/m574_diag.png)",
  "'X_s§times_{k(x)}C_s': the TeX keeps the printed reading",
  "misprint_in_print", "high", None,
  "The fibre product over the residue field of s, k(s). The current layer already reads 'X_s§times_{k(s)}C_s'.",
  corrected="X_s§times_{k(s)}C_s"))
L.append(F(574, "'leurs points d'intersections rationnelles sur k(s)'",
  "'et leurs points d'intersections / rationnelles sur k(s)' (both scans; crops_571_575/m574_inters.png)",
  "'leurs points d'intersections rationnelles': the TeX keeps the printed reading",
  "misprint_in_print", "medium", None,
  "'rationnelles' should agree with 'points'. The current layer already reads 'd'intersection rationnels'.",
  corrected="d'intersection rationnels"))
# ---------------- page 575
L.append(F(575, "start of page (folio-575 marker)",
  "p. 574 ends '... dans K.(X_s), en utilisant la connexité'; p. 575 begins 'de C_s, qui résulte de la connexité géométrique de C_t.' "
  "(both scans: page_574_s4.png, page_575_s1.png; crops_571_575/wit_574_half.png, wit_575_half.png)",
  "page_574.tex ends 'en utilisant la connexité de §(C_s§), qui' above the folio-575 marker; page_575.tex begins 'résulte de'",
  "marker", "high", None,
  "Page 575 really begins at 'de §(C_s§), qui'. Exact edit in main.tex, both layers (diplomatic about line 14903, current about line 14908 "
  "at 16:27 on 13 Nov; use the string, it occurs once per layer): replace 'la connexité de §(C_s§), qui§n" + M575
  + "§nrésulte de' by 'la connexité§n" + M575 + "§nde §(C_s§), qui résulte de' (simulated in memory: crops_571_575/sim_markers.py). "
  "The sentence runs on, so no blank line."))
L.append(F(575, "after (7.12.2): 'Lorsqu'on suppose de plus X_s et X_t réguliers'",
  "'Lorsqu'on suppose' begins a new, indented paragraph after (7.12.2) (both scans; crops_571_575/wit_575_half.png)",
  "'§end{equation}' followed directly by 'Lorsqu'on suppose' (the paragraph runs on)",
  "other", "high",
  ("§end{equation}\nLorsqu'on suppose", "§end{equation}\n\nLorsqu'on suppose"),
  "Missing paragraph break."))
L.append(F(575, "7.12.5: 'On vérifie facilement qu'un élément de K˙(T), tel qu'il existe un entier n ≥ 1 avec nx'",
  "'qu'un élément de K˙(T), tel qu'il existe un entier n ≥ 1 / avec nx algébriquement équivalent à zéro' (both scans; crops_571_575/m575_nx.png): "
  "the element is never named x ('nx' typed in a tighter spacing, as if filled in afterwards)",
  "'qu'un élément de §(K^§bullet(T)§)': the TeX keeps the printed reading",
  "misprint_in_print", "medium", None,
  "Omitted letter: the x of 'nx' is the element just introduced. The current layer still has the printed reading.",
  corrected="qu'un élément §(x§) de §(K^§bullet(T)§)"))

def subst(o):
    if isinstance(o, str):
        return o.replace("§", BS)
    if isinstance(o, dict):
        return {k: subst(v) for k, v in o.items()}
    if isinstance(o, list):
        return [subst(v) for v in o]
    return o
L = subst(L)

ok = True
texts = {}
for f in L:
    p = f["page"]
    if p not in texts:
        texts[p] = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = texts[p].count(old)
        crosses = "%%%%%%%%%%" in old
        print(p, f["kind"], "count", n, "crosses-marker" if crosses else "", repr(old[:70]))
        if n != 1 or crosses:
            ok = False
# apply each page's fixes in order to make sure they do not interfere
for p, t in texts.items():
    for f in L:
        if f["page"] == p and f["fix"] is not None:
            if t.count(f["fix"]["old"]) != 1:
                ok = False; print("sequential failure", p, repr(f["fix"]["old"]))
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
print("all fixes unique and sequential:", ok)
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT, len(L), "findings")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in L)
for p in range(571, 576):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
