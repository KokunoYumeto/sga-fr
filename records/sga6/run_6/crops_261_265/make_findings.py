"""Build findings_261_265.json and check that every fix's old text occurs exactly once in its page file
(and, as an extra check, once in that folio's span of the present main.tex, both layers)."""
import json
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b261_265"
C = "crops_261_265/"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---- p. 261
add(261, "start of page",
    "p. 261 begins 'du type O_{U,X}, où U est un objet de X.'; p. 260 ends '... où M^0 et M^1 sont sommes directes "
    "de faisceaux' (both scans; " + C + "w_272.png)",
    "'du' is the last word of page_260.tex ('sont sommes directes de faisceaux du', under the folio-260 marker); "
    "page_261.tex begins 'type'",
    "marker", "high", None,
    "Page 261 really begins with 'du'. Move the folio-261 marker before it: python -I move_marker.py 6 261 \"du\" "
    "--before (simulated in memory on both layers of the present main.tex with " + C + "sim_all.py: '... sommes "
    "directes de faisceaux', the marker, 'du', 'type \\(\\mathcal O_{U,X}\\) ...'). The checker of p. 260 may report "
    "the same boundary: apply once.")

add(261, "'Supposons E pseuso-cohérent, et prouvons b) ⟹ b')'",
    "pseuso-cohérent (both scans; " + C + "w_272.png)",
    "Supposons \\(E\\) pseudo-cohérent (silent correction)",
    "misprint_in_print", "high",
    (r"Supposons \(E\) pseudo-cohérent", r"Supposons \(E\) pseuso-cohérent"),
    "Typing error of the print (s for d). The TeX silently corrects it; the diplomatic layer restores the printed "
    "reading. Only the d changes.",
    corrected="pseudo-cohérent")

add(261, "Preuve de (5.1.1): '(resp. RHom(F^∨, M))'",
    "R Hom(F^∨, M): a plain typed R, 'Hom' underlined (the sheaf Hom), the R not underlined (both scans; "
    + C + "c261_RHom.png, w261_RHom.png)",
    "\\RHom(F^{\\vee},M) (\\RHom = \\mathrm R\\!\\operatorname{Hom}: Hom not underlined)",
    "underline", "high",
    (r"\RHom(F^{\vee},M)", r"\mathrm R\underline{\Hom}(F^{\vee},M)"),
    "\\underline{\\Hom} is the file's form for the underlined Hom (pp. 116-118, 148; p. 263 writes "
    "\\underline{\\mathrm{Hom}}); the R stays plain, as printed.")

add(261, "'des foncteurs H^p(E) ⊗ . et H^p(E ⊗^L .)', first place-holder",
    "a typed full stop on the baseline after ⊗, level with the foot of 'et' (both scans; " + C
    + "c261_dots.png, w261_dots.png)",
    "\\otimes\\,\\cdot\\, (centred dot)",
    "symbol", "low",
    (r"\otimes\,\cdot\,\)", r"\otimes\,.\,\)"),
    "As the baseline place-holders reported on pp. 89 and 117 (p. 236 has the converse case, a raised dot).")

add(261, "'et H^p(E ⊗^L .), on se ramène', second place-holder",
    "a typed full stop on the baseline after the derived tensor sign (both scans; " + C
    + "c261_dots.png, w261_dots.png)",
    "\\,\\cdot\\,) (centred dot)",
    "symbol", "low",
    (r"\,\cdot\,)", r"\,.\,)"),
    "As the previous entry (disjoint texts). The old text leaves out the L, which is now \\mathrm L in main.tex.")

# ---- p. 262
add(262, "start of page, first word",
    "p. 262 begins 'tion a) (resp. a'), etc.) relative à E_x', the second half of 'condi-tion' divided at the page "
    "break; p. 261 ends '(ii) Si x est un point de X, notons a_x) (resp. a'_x), etc.) la condi-' (both scans)",
    "the folio-262 marker stands before the whole word 'condition'; page_261.tex ends 'etc.) la'",
    "marker", "high", None,
    "Page 262 really begins with 'tion'. Split the word at the marker as at folios 18, 36, 46, 54, 161, 185 and 206: "
    "python -I marker_split_word.py 6 262 split condi tion (simulated in memory on both layers with " + C
    + "sim_all.py: '... etc.) la', 'condi%', the marker, 'tion a) (resp. a'), etc.) relative à ...').")

add(262, "Remarques 5.2 (iv), 'Soient X un schéma quasi-séparé, O_X le faisceau structural'",
    "'quasi-séparé' underlined, the comma not (both scans; " + C + "w_273.png)",
    "un schéma quasi-séparé, (no emphasis)",
    "underline", "high",
    ("schéma quasi-séparé,", r"schéma \emph{quasi-séparé},"),
    "\\emph is this exposé's command for the typescript's underline (\\emph{Preuve.}); a remark, not a statement.")

add(262, "Remarques 5.2 (iv), 'la condition analogue à a) (resp. a'), etc). où l'on remplace Mod(X)'",
    "etc). où: the full stop after the closing parenthesis (both scans; " + C + "w_273.png)",
    "etc). où (printed reading kept)",
    "misprint_in_print", "high", None,
    "Stop and parenthesis transposed: the sentence goes on with 'où', and the line above has 'etc.) la condition'. "
    "The TeX keeps the printed reading.",
    corrected="etc.) où")

# ---- p. 263
add(263, "Proposition 5.3 b'), '(composée de l'isomorphisme (3.7) R^{p+1}f_*(E ⊗^L_Y M) ≃ H^{p+1}(Rf_*(E) ⊗^L M)'",
    "≃: a typed tilde over a straight line, no arrowhead (both scans; " + C
    + "c263_bprime_arrow.png, w263_bprime_arrow.png); the isomorphism of a') on the same page has its arrowhead",
    "\\xrightarrow{\\sim}H^{p+1}",
    "symbol", "high",
    (r"\xrightarrow{\sim}H^{p+1}", r"\simeq H^{p+1}"),
    "As the headless ≃ fixed on pp. 223, 238 and 239. The a') sign '(3.7) H^p(...) ⥲ R^pf_*(...)' has its head "
    "and stays \\xrightarrow{\\sim}.")

# ---- p. 264
add(264, "start of page",
    "p. 264 begins 'c) Pour tout changement de base Y' ⟶ Y , la flèche canonique'; p. 263 ends with b') '... est un "
    "isomorphisme pour tout M ∈ ob Qcoh(Y).' and the two footnotes (both scans; " + C + "w_274.png, w_275.png)",
    "'\\item[c)]' is the last line of page_263.tex (under the folio-263 marker); page_264.tex begins 'Pour tout "
    "changement de base'",
    "marker", "high", None,
    "Page 264 really begins with the item label c). Move the folio-264 marker above it: python -I move_marker.py "
    "6 264 '\\item[c)]' --before (single quotes; simulated in memory on both layers with " + C + "sim_all.py: "
    "'... pour tout \\(M\\in\\Ob\\Qcoh(Y)\\).', the marker, '\\item[c)]', 'Pour tout changement de base ...').")

# ---- p. 265
add(265, "display (5.3.1.1), last line of printed p. 264",
    "the comma stands on the display line after the formula ('... H^{-p-1}((E ⊗^L_X O_{X'})^∨)   ,'); p. 265 "
    "begins 'composée de' (both scans; " + C + "w_275.png, w_276.png)",
    "the comma begins the line after \\end{equation} (', composée de'), so it prints at the head of the following "
    "text line",
    "punctuation", "high",
    ("\\tag{5.3.1.1}\n\\end{equation}\n, composée", ",\\tag{5.3.1.1}\n\\end{equation}\ncomposée"),
    "Apply before the marker entry below (it then puts the folio-265 marker at the start of the 'composée de' "
    "line). Same case as GLOBAL_ISSUES 49.")

add(265, "start of page",
    "p. 265 begins 'composée de H^{-p-1}(E^∨) ⊗_X O_{X'} ⟶ H^{-p-1}(E^∨ ⊗^L_X O_{X'})'; p. 264 ends '... la "
    "condition (5.1 a)) implique que, pour tout morphisme X' ⟶ X, la flèche canonique' and the display (5.3.1.1) "
    "with its comma (both scans; " + C + "w_275.png)",
    "page_264.tex ends 'implique que, pour tout'; page_265.tex begins 'morphisme \\(X'\\to X\\), la flèche "
    "canonique' and the (5.3.1.1) equation, which belong to p. 264",
    "marker", "high", None,
    "Page 265 really begins with 'composée de'. After the comma entry above: python -I move_marker.py 6 265 "
    "'composée de \\(H^{-p-1}(E^{\\vee})' (single quotes; no --before: the anchor follows the marker's present "
    "place). Simulated in memory on both layers in this order with " + C + "sim_all.py: '...)^{\\vee}),"
    "\\tag{5.3.1.1}', '\\end{equation}', the marker, 'composée de ...'. Run without the comma entry, the same "
    "command leaves ', ' alone on the line above the marker.")

# ---- checks
ok = True
spans = {}
for edition in ("diplomatic", "current"):
    t = files("6", edition)[0].read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        fo = int(m.group(2))
        if 260 <= fo <= 266:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            spans[(edition, fo)] = t[m.start():end]
for d in F:
    if d["fix"] is None:
        continue
    page = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = page.count(old)
    nm = [spans[(e, d["page"])].count(old) for e in ("diplomatic", "current")]
    flag = "OK" if n == 1 and nm == [1, 1] else "CHECK"
    if n != 1:
        ok = False
    print(flag, d["page"], n, nm, repr(old)[:70])
out = RUN / "findings_261_265.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", out, len(F), "findings; all page checks pass" if ok else "PAGE CHECK FAILED")
for p in range(261, 266):
    n = sum(1 for d in F if d["page"] == p and d["kind"] != "misprint_in_print")
    m = sum(1 for d in F if d["page"] == p and d["kind"] == "misprint_in_print")
    print(p, f"{n}/{m}")
