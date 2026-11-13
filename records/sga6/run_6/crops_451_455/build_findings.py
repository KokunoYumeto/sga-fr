"""Build findings_451_455.json; check that every fix's old occurs exactly once in its page file, never contains or
crosses a marker line, and that the fixes of a page apply one after the other (no edit destroys another's old)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b451_455"
OUT = RUN / "findings_451_455.json"
M451 = "%%%%%%%%%%  scan idx 464  |  folio 451  %%%%%%%%%%"
M456 = "%%%%%%%%%%  scan idx 469  |  folio 456  %%%%%%%%%%"


def L(s):
    """raw LaTeX with the pilcrow standing for a line break"""
    return s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": L(old), "new": L(new)}


MOD = r"\quad\text{mod.\ torsion}"
PMOD_NOTE = ("The print's plain 'mod.' after a wide space, no parentheses; the transcription's \\pmod reported singly, "
             "as asked (ten displays on pp. 451-453, all written \\pmod{\\text{torsion}}).")

# ---------------------------------------------------------------- page 451
add(451, "start of page (folio-451 marker)",
    "p. 450 ends '... La relation à vérifier s'écrit donc finalement, en appliquant la formule de projection :' "
    "(b446_450/page_450_s4.png); p. 451 begins with the display 'λ^p(J',u')(1-J') = λ^p(u'(1-J')) .' "
    "(both scans; crops_451_455/wit_451_half.png)",
    "page_451.tex begins 'projection :' under the folio-451 marker; page_450.tex ends 'en appliquant la formule de'",
    "marker", "high", None,
    "Page 451 really begins at the display '\\[ \\lambda^p(J',u')(1-J')=\\lambda^p(u'(1-J')).'. Exact edit in main.tex, "
    "both layers: replace 'en appliquant la formule de\\n" + M451 + "\\nprojection :\\n\\[' by "
    "'en appliquant la formule de\\nprojection :\\n" + M451 + "\\n\\['. ALREADY APPLIED: main.tex as of 13 Nov "
    "16:06 reads 'projection :' above the marker in both layers (diplomatic lines 11447-11450, current 11453-11456; "
    "checked in memory: crops_451_455/sim_markers.py); nothing left to do but regenerate the page files.")

add(451, "ii), first sentence: '... vérifie la condition de 4.1. (voir 4.2).'",
    "'4.1.' with a full stop before '(voir 4.2)' (both scans; crops_451_455/c451_41.png, wit_451_half.png)",
    "condition de 4.1 (voir 4.2)", "punctuation", "high",
    fx(r"condition de 4.1 (voir 4.2)", r"condition de 4.1. (voir 4.2)"), "")

add(451, "(4.3.3), end: 'mod. torsion.'",
    "'λ^p((s∘i)_*(y))  mod. torsion.' (both scans)", r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"_*(y)\bigr)¶ \pmod{\text{torsion}}.", r"_*(y)\bigr)¶ " + MOD + "."), PMOD_NOTE)

add(451, "'La section s est définie par un idéal isomorphe à O_p(-1) (4.2)'",
    "underlined O with a lowercase p as index, the p not underlined: the glyph of the p of 'p ≥ 1' (bowl, descender, "
    "narrow foot serif), not the capital P of 'J.P.' (both scans; crops_451_455/c451_OP.png, w451_OP.png, "
    "c451_pcompare.png)",
    r"\mathcal O_{\mathbf P}(-1) (silently corrected)", "misprint_in_print", "medium",
    fx(r"O_{\mathbf P}(-1)", r"O_p(-1)"),
    "The sheaf is O(-1) of P = P^1_X (s : X → P^1_X); p is the structural morphism P^1_X → X, named three lines "
    "below. The typist writes the same lowercase index in 4.2, p. 449 ('l'idéal correspondant de O_p à (O_X)^r', "
    "TeX \\cO_P), for that batch. The current layer reads \\mathcal O_{\\mathbf P}(-1), the corrected reading. The "
    "underlined O as \\mathcal O falls under the pending volume decision.",
    corrected=r"\mathcal O_{\mathbf P}(-1)")

add(451, "'La section s est définie par un idéal ...' after (4.3.3)",
    "indented new paragraph (both scans; it starts 150 px right of the margin, as 'Si on suppose' above)",
    "\\end{equation} then 'La section' on the next line (no blank line)", "other", "high",
    fx(r"\end{equation}¶La section", r"\end{equation}¶¶La section"), "Missing paragraph break.")

add(451, "'... comme s_*(1) = 1-ξ, on a la relation voulue :' and 'La relation (4.3.3) s'écrit alors :'",
    "'voulue :' with a colon; 'La relation (4.3.3) s'écrit alors :' begins an indented new paragraph (both scans; "
    "crops_451_455/c451_voulue.png)",
    "on a la relation voulue. La relation (4.3.3) s'écrit alors :", "punctuation", "high",
    fx(r"on a la relation voulue. La relation (4.3.3)", r"on a la relation voulue :¶¶La relation (4.3.3)"),
    "Colon for the TeX's full stop, with the printed paragraph break.")

add(451, "display after 'La relation (4.3.3) s'écrit alors :', first line, end: 'mod. torsion'",
    "plain 'mod. torsion', no punctuation (both scans)", r"\pmod{\text{torsion}}\\", "formula", "high",
    fx(r"(1-\xi)\bigr)\pmod{\text{torsion}}\\", r"(1-\xi)\bigr)" + MOD + r"\\"), "As (4.3.3).")

add(451, "same display, second line, end: 'mod. torsion .'",
    "plain 'mod. torsion .' (both scans)", r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"(1-\xi)\pmod{\text{torsion}}.", r"(1-\xi)" + MOD + "."), "As (4.3.3).")

add(451, "K˙ on pp. 451-455 (21 places: p. 451 3, p. 452 1, p. 453 1, p. 454 9, p. 455 7)",
    "K with a raised dot everywhere (both scans)", "K^\\circ (21 places)", "symbol", "high", None,
    "The Exposé VII convention reported in findings_416_420 (K^\\circ for the print's K˙, one script K^\\circ -> "
    "K^{\\bullet} for VII, both layers): not itemized. Three examples: p. 451 'et tout \\(y\\in K^\\circ(Y)\\) :' -> "
    "'et tout \\(y\\in K^{\\bullet}(Y)\\) :'; p. 454 '(le \\(K^\\circ\\) commutant' -> '(le \\(K^{\\bullet}\\) "
    "commutant'; p. 455 '\\Fil^{i+d}(K^\\circ(X)_{\\mathbb Q})' -> '\\Fil^{i+d}(K^{\\bullet}(X)_{\\mathbb Q})'. "
    "One fix of p. 455 (inline formula) has K^\\circ in its old: run the script after it, or read K^{\\bullet} there.")

add(451, "statements of pp. 451-455: Lemme (p. 451), Corollaire 4.4 (p. 453), Théorème 4.6 (p. 454)",
    "underlined word group by word group: Lemme 'Dans les conditions de', 'soit', 'la section définie' / 'en', "
    "'Si la proposition', 'est vraie pour', 'elle est vraie pour'; Cor. 4.4 'Avec les notations et les hypothèses "
    "de', 'on a pour tout', 'et tout'; Thm 4.6 'Soient', 'un schéma quasi-compact ayant un faisceau ample', "
    "'un entier', 'et', 'une immersion régulière de codimension', 'Alors', 'pour tout', 'on a'; formulas, letters, "
    "numbers and punctuation plain; the labels (and those of Remarques 4.5, 4.6.1) underline only the word "
    "(both scans)",
    "the statements in roman", "underline", "high", None,
    "Exposé VII follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as findings_416_420 "
    "to findings_431_435 report: not itemized; the word groups are listed for the scripted pass. No emphasized "
    "defined terms and no category letter on pp. 451-455.")

# ---------------------------------------------------------------- page 452
add(452, "first display, first line, end: 'mod. torsion'",
    "plain 'mod. torsion' (both scans)", r"\pmod{\text{torsion}}\\", "formula", "high",
    fx(r"(1-\xi) \pmod{\text{torsion}}\\", r"(1-\xi) " + MOD + r"\\"), "As (4.3.3), p. 451.")

add(452, "first display, second line, end: 'mod. torsion.'",
    "plain 'mod. torsion.' (both scans)", r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"(1-\xi) \pmod{\text{torsion}}.", r"(1-\xi) " + MOD + "."), "As (4.3.3), p. 451.")

add(452, "(4.3.4), end: 'mod. torsion,'",
    "plain 'mod. torsion,' (both scans)", r"\pmod{\text{torsion}},", "formula", "high",
    fx(r"\lambda^p(1,i_*(y)) \pmod{\text{torsion}},", r"\lambda^p(1,i_*(y)) " + MOD + ","),
    "As (4.3.3), p. 451.")

add(452, "'De même, la même formule appliquée à N = 0 et L = 1 ...'",
    "indented new paragraph (both scans; 'D'après la formule' above is indented the same)",
    "\\] then 'De même,' on the next line (no blank line)", "other", "high",
    fx(r"\]¶De même,", r"\]¶¶De même,"), "Missing paragraph break.")

add(452, "'Les congruences (4.3.4) peuvent donc s'écrire :'",
    "indented new paragraph (both scans)",
    "\\] then 'Les congruences' on the next line (no blank line)", "other", "high",
    fx(r"\]¶Les congruences", r"\]¶¶Les congruences"), "Missing paragraph break.")

add(452, "last display (the congruence of the series), end: 'mod. torsion'",
    "plain 'mod. torsion' and no full stop after it (both scans; crops_451_455/c452_torsion_end.png, "
    "w452_bottom_half.png)",
    r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"\pmod{\text{torsion}}.¶\]", MOD + r"¶\]"),
    "As (4.3.3), p. 451; the TeX also adds the full stop at the end of the display (p. 453 continues 'En appliquant "
    "la formule 2.8').")

# ---------------------------------------------------------------- page 453
add(453, "first display (after 'En appliquant la formule 2.8, on obtient :'), end: 'mod. torsion'",
    "plain 'mod. torsion' and no full stop after it (both scans; crops_451_455/c453_tors1.png, "
    "w453_half_top.png)",
    r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"\pmod{\text{torsion}}.¶\]¶Si on pose", MOD + r"¶\]¶Si on pose"),
    "As (4.3.3), p. 451; the TeX also adds the full stop at the end of the display.")

add(453, "display d/dt(u(t)/v(t)) ≡ 0, end: 'mod. torsion.'",
    "plain 'mod. torsion.' (both scans)", r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"\equiv0¶  \pmod{\text{torsion}}.", r"\equiv0¶  " + MOD + "."), "As (4.3.3), p. 451.")

add(453, "Corollaire 4.4, display, end: 'mod. torsion.'",
    "plain 'mod. torsion.' (both scans; the speck before 'mod' is in the main scan only)",
    r"\pmod{\text{torsion}}.", "formula", "high",
    fx(r"(y))¶  \pmod{\text{torsion}}.", r"(y))¶  " + MOD + "."),
    "As (4.3.3), p. 451. The old stops after the misprinted i' of the next entry, so it also matches the current "
    "layer.")

add(453, "Corollaire 4.4, display: 'i_*(γ^p(N,y)) ≡ γ^p(i'_*(y))'",
    "a thin prime after the i of the right member, in both scans (crops_451_455/c453_iprime.png; witness: a "
    "separate stroke right of the dot of the i)",
    r"\gamma^p(i'_*(y)) (printed reading kept)", "misprint_in_print", "medium", None,
    "Corollary 4.4 is 4.3 with γ for λ: the right member is γ^p(i_*(y)), as λ^p(i_*(y)) in (4.3.1) and (4.3.4); "
    "4.3-4.4 have no i'. The current layer already reads \\gamma^p(i_*(y)) (main.tex current line 11547).",
    corrected=r"\gamma^p(i_*(y))")

add(453, "'Le corollaire résulte immédiatement de 4.3, ...' after the display of Cor. 4.4",
    "indented new paragraph (both scans)",
    "\\] then 'Le corollaire' on the next line (no blank line)", "other", "high",
    fx(r"\]¶Le corollaire", r"\]¶¶Le corollaire"), "Missing paragraph break.")

add(453, "'Le corollaire résulte immédiatement de 4.3, et utilisant l'expression des γ^p ...'",
    "'et utilisant' (both scans; crops_451_455/c453_etutil.png)",
    "et utilisant (printed reading kept)", "misprint_in_print", "medium", None,
    "Typist's 'et' for 'en': the gerund needs 'en' ('résulte de 4.3, en utilisant l'expression ...'). The current "
    "layer also reads 'et utilisant' (main.tex current line 11550): the corrected edition needs 'en utilisant'.",
    corrected="en utilisant")

# ---------------------------------------------------------------- page 454
add(454, "'Par ailleurs, la filtration de λ-anneau de R est discrète' after the display 'x ∈ Fil^k R .'",
    "starts at the left margin, not indented (both scans): the paragraph goes on after the display, as 'Comme le "
    "terme constant' on p. 453; the indented paragraphs of the page ('Remarquons', 'Pour tout groupe') start "
    "about 140 px further right",
    "blank line (new paragraph) before 'Par ailleurs'", "other", "medium",
    fx(r"\]¶¶Par ailleurs", r"\]¶Par ailleurs"), "Added paragraph break.")

add(454, "letters of sheaves on p. 454",
    "underlined in the print (both scans; crops_451_455/c454_letters.png): J of 'l'idéal J définissant Y', both J of "
    "J^n/J^{n+1}, the E_α of 'de type fini E_α.' and of 'supposer les E_α de rang constant'; plain in the print: "
    "the classes E_α ('des classes E_α', 'par les E_α'), N, R, A",
    "all plain", "underline", "high", None,
    "Convention of the Exposé VII transcription (findings_416_420 to findings_431_435): not itemized; the print "
    "distinguishes the Modules E_α (underlined) from their classes (plain). The underlined O of O_Y, O_p written "
    "\\mathcal O falls under the pending volume decision. Three examples, in the form to use if the diplomatic "
    "layer reproduces it: 'l'idéal \\(J\\) définissant' -> 'l'idéal \\(\\underline{J}\\) définissant'; 'les "
    "\\(J^n/J^{n+1}\\) sont' -> 'les \\(\\underline{J}^n/\\underline{J}^{n+1}\\) sont'; 'de type fini "
    "\\(E_\\alpha\\). Soit' -> 'de type fini \\(\\underline{E}_\\alpha\\). Soit'.")

# ---------------------------------------------------------------- page 455
add(455, "'On peut donc appliquer l'hypothèse de récurrence, supposant que :'",
    "indented new paragraph (both scans)",
    "\\] then 'On peut donc appliquer' on the next line (no blank line)", "other", "high",
    fx(r"\]¶On peut donc appliquer", r"\]¶¶On peut donc appliquer"), "Missing paragraph break.")

add(455, "'Comme i_*(y) est d'augmentation nulle, γ^{d+i}(i_*(y)) ∈ Fil^{d+i}K˙(X) .'",
    "the formula in the running line, after 'nulle,', with its spaced full stop; 'Comme on fait des calculs' "
    "follows at the left margin (both scans)",
    "a display \\[ \\gamma^{d+i}\\bigl(i_*(y)\\bigr)\\in\\Fil^{d+i}K^\\circ(X). \\]", "other", "medium",
    fx(r"nulle,¶\[¶  \gamma^{d+i}\bigl(i_*(y)\bigr)\in\Fil^{d+i}K^\circ(X).¶\]",
       r"nulle, \(\gamma^{d+i}\bigl(i_*(y)\bigr)\in\Fil^{d+i}K^\circ(X)\)."),
    "The TeX makes an inline formula a display (same kind of fix as pp. 21, 34, 42, 80, 105, 426). The old has "
    "K^\\circ: if the Exposé VII K^{\\bullet} script runs first, read K^{\\bullet} in old and new.")

add(455, "end of page (folio-456 marker)",
    "p. 455 ends '... Pour un contre-exemple, voir XIV 4.6.'; p. 456 begins '4.7. On revient à la situation de "
    "3.7, ...' (both scans; b456_460/page_456_s1.png)",
    "page_455.tex ends '\\subsection*{4.7}', a blank line and 'On' above the folio-456 marker; page_456.tex begins "
    "'revient à la situation'",
    "marker", "high", None,
    "Page 456 really begins at the heading '\\subsection*{4.7}' (a heading at the top of a page, which the 10 Nov "
    "script did not move). Exact edit in main.tex, both layers (diplomatic lines 11615-11619, current 11621-11625 "
    "as of 13 Nov 16:06): replace '\\subsection*{4.7}\\n\\nOn\\n" + M456 + "\\nrevient à la situation' by '" + M456
    + "\\n\\subsection*{4.7}\\n\\nOn\\nrevient à la situation' (old string once per layer; simulated in memory: "
    "crops_451_455/sim_markers.py). The blank line before the heading stays above the marker. Apply it before the "
    "heading entry below, or read \\subsection*{4.7.} in both strings; the batch of pp. 456-460 may report the same "
    "move.")

add(455, "heading 4.7 (printed at the top of p. 456; its TeX stands in page_455.tex above the folio-456 marker)",
    "'4.7.' with a full stop (both scans; b456_460/page_456_s1.png)", r"\subsection*{4.7}", "punctuation", "high",
    fx(r"\subsection*{4.7}", r"\subsection*{4.7.}"),
    "As headings 2.1, 2.2 (findings_426_430): the printed paragraph number ends with a full stop; the run-in "
    "heading set as its own paragraph is accepted. See the marker entry above for the order of the two edits.")

# ---------------------------------------------------------------- checks
ok = True
for p in range(451, 456):
    text = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    assert "\r" not in text
    cur = text
    for d in F:
        if d["page"] != p or not d["fix"]:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        n = text.count(old)
        if n != 1:
            ok = False
            print("NOT UNIQUE", p, n, repr(old))
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
            ok = False
            print("MARKER IN FIX", p, repr(old))
        if cur.count(old) != 1:
            ok = False
            print("DESTROYED BY AN EARLIER EDIT", p, repr(old))
        cur = cur.replace(old, new, 1)
    # every edit applied in reverse order too
    cur = text
    for d in reversed([d for d in F if d["page"] == p and d["fix"]]):
        old, new = d["fix"]["old"], d["fix"]["new"]
        if cur.count(old) != 1:
            ok = False
            print("ORDER-DEPENDENT", p, repr(old))
        cur = cur.replace(old, new, 1)
    (pathlib.Path(__file__).parent / f"patched_{p}.tex").write_text(cur, encoding="utf-8", newline="\n")
for d in F:
    if d["kind"] == "misprint_in_print":
        assert d.get("corrected"), d["where"]
    else:
        assert "corrected" not in d
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("entries", len(F), "checks ok" if ok else "CHECKS FAILED")
print(" ".join(f"{p}: {c[0]}/{c[1]}" for p, c in sorted(counts.items())))
