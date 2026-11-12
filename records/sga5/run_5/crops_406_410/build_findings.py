"""Build findings_406_410.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b406_410"
OUT = RUN / "findings_406_410.json"
pages = {n: (B / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(406, 411)}
assert all("\r" not in t for t in pages.values())

# p. 408: the editorial comment that swallows the end of the paragraph
t408 = pages[408]
i = t408.index("-modules% [faithful]")
j = t408.index("brûlé) et plus") + len("brûlé) et plus")
old408 = t408[i:j]
new408 = old408.replace("-modules% [faithful]", "-modules\n% [faithful]", 1).replace("brûlé) et plus", "brûlé)\net plus", 1)

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 406 ----------------
add(406, "top of the page: heading 'Références' and the start of [1]",
    "p. 406 begins (under the folio) with the underlined heading 'Références', then '[1] M. Raynaud   Caractéristique d'Euler-Poincaré ...'; p. 405 ends with 'd'où la formule (7.13).' and blank paper (b401_405/page_405_s3.png, s4.png)",
    r"'\section*{Références}', a blank line, '\begin{enumerate}' and '\item[{[1]}] M.' are the last lines of page_405.tex (s5.tex diplomatic lines 13765-13768, current 13761-13764); the folio-406 marker (diplomatic 13769, current 13765) stands between 'M.' and 'Raynaud'",
    "marker", "high", None,
    r"Page 406 really begins at '\section*{Références}'. Exact fix: python -I move_marker.py 5 406 '\section*{Références}' --before (simulated in memory on both layers: the marker moves back 57 characters to its own line between the blank line after 'd'où la formule (7.13).' and '\section*{Références}'; the anchor occurs once in s5.tex, so a second run prints 'anchor not found' and changes nothing). Text not moved; the heading, '\begin{enumerate}' and '[1] M.' agree with the print (the underlined title as \section* is the accepted setting; the print has no full stop after it).")
add(406, "[1], between the author and the title",
    "M. Raynaud in the left column, the title 'Caractéristique d'Euler-Poincaré ...' in the right column; no comma between them",
    "Raynaud, Caractéristique", "punctuation", "high",
    {"old": "Raynaud, Caractéristique", "new": "Raynaud Caractéristique"},
    "The print sets author and title in two columns with no comma (as the bibliography of p. 350 and 'VERDIER, J-L.' on p. 72); the TeX adds one.")
add(406, "[2], between the author and the title",
    "A. Grothendieck in the left column, 'Sur quelques points ...' in the right column; no comma",
    "Grothendieck, Sur", "punctuation", "high",
    {"old": "Grothendieck, Sur", "new": "Grothendieck Sur"},
    "As [1].")
add(406, "[2], the journal: 'Toh. Math. Journal'",
    "'... homologique, Toh.' at the end of the line, 'Math. Journal, vol. 9(1957)' on the next (checked at 1.2x)",
    "Tohoku Math. Journal", "word", "high",
    {"old": "Tohoku Math.", "new": "Toh. Math."},
    "Abbreviation written out by the transcription.")
add(406, "[2], pages 'p.119 - 221'",
    "a typewriter hyphen between spaces: 'p.119 - 221,'",
    "p. 119--221", "punctuation", "high",
    {"old": "119--221", "new": "119 - 221"},
    "En dash for the print's hyphen (as 137-154 on p. 350 and 491-526 on p. 54).")
add(406, "[3], author 'Serre,J-P.'",
    "'Serre,J-P.' (no full stop after J), then the title in the right column with no comma (checked at 1.6x)",
    "Serre, J.-P., Corps", "punctuation", "high",
    {"old": "Serre, J.-P., Corps", "new": "Serre, J-P. Corps"},
    "The initial's full stop and the column comma in one edit (adjacent); as 'Serre, J-P.' on p. 54. The comma after Serre is printed (no space after it: spacing, not changed).")
add(406, "[3], 'Act. Sci. Ind, 1296(1962)'",
    "'Ind,' with no full stop after Ind (clear at 1.6x; 'Act.' and 'Sci.' have theirs)",
    "Act. Sci. Ind., 1296", "misprint_in_print", "high",
    {"old": "Ind., 1296", "new": "Ind, 1296"},
    "The TeX silently supplies the abbreviation's full stop; the fix restores the printed reading (diplomatic layer only), as 'Math,' and 'vol 63' on p. 54.",
    corrected="Ind., 1296")
add(406, "[3], 'Hermann Paris.'",
    "'Hermann' ends the line, 'Paris.' begins the next; no comma",
    "Hermann, Paris.", "punctuation", "high",
    {"old": "Hermann, Paris.", "new": "Hermann Paris."},
    "The TeX adds a comma (as 'n° 20 / Springer' on p. 54).")
add(406, "[4], author 'Serre,J-P.'",
    "'Serre,J-P.' (no full stop after J), then the title in the right column with no comma",
    "Serre, J.-P., Cohomologie", "punctuation", "high",
    {"old": "Serre, J.-P., Cohomologie", "new": "Serre, J-P. Cohomologie"},
    "As [3].")
add(406, "[5], author 'Verdier, J-L.'",
    "'Verdier, J-L.' (no full stop after J), then the title in the right column with no comma",
    "Verdier, J.-L., Catégories", "punctuation", "high",
    {"old": "Verdier, J.-L., Catégories", "new": "Verdier, J-L. Catégories"},
    "As [3] (and 'VERDIER, J-L.' on p. 72).")

# ---------------- p. 407 ----------------
add(407, "top of the page: the heading 'Exposé XII'",
    "p. 407 (title page, no folio printed) begins with 'Exposé XII' at the left, then the title FORMULES DE NIELSEN-WECKEN ET DE LEFSCHETZ EN GEOMETRIE ALGEBRIQUE, 'par A. Grothendieck', 'rédigé par I. BUCUR'; p. 406 ends with '[5] ... dans SGA 4^{1/2}).'",
    r"'\section*{Exposé XII}', a blank line, '\begin{center}' and '\Large\bf' are the last lines of page_406.tex (s5.tex diplomatic lines 13777-13780, current 13773-13776); the folio-407 marker stands inside the center block of the title",
    "marker", "high", None,
    r"Page 407 really begins at '\section*{Exposé XII}'. Exact fix: python -I move_marker.py 5 407 '\section*{Exposé XII}' --before (simulated in memory on both layers: the marker moves back 48 characters to its own line between the blank line after '\end{enumerate}' and '\section*{Exposé XII}', and the whole title block is on p. 407; the anchor occurs once in s5.tex, a second run prints 'anchor not found'). Text not moved; the heading and the title block agree with the print (the bold title is the accepted setting).")

# ---------------- p. 408 ----------------
add(408, "top of the page: paragraph number '1.'",
    "p. 408 begins with '1. Soient X' un schéma propre ...'; p. 407 (title page) ends with 'rédigé par I. BUCUR'",
    r"'\section*{1.}' is the last line of page_407.tex (s5.tex diplomatic line 13793, current 13789); the folio-408 marker follows it, before 'Soient'",
    "marker", "high", None,
    r"Page 408 really begins at '\section*{1.}'. Exact fix: python -I move_marker.py 5 408 '\section*{1.}' --before (simulated in memory on both layers: the marker moves back 14 characters to its own line between '\bigskip' plus the blank line and '\section*{1.}'; the anchor occurs once in s5.tex, a second run prints 'anchor not found'). Text not moved. The number run into the text is not reported (rule).")
add(408, "end of the paragraph 'Désignons par ...': 'et plus précisément un complexe parfait (VIII,7) de Λ_n[G] - modules (IX,2).'",
    "'... est un complexe de Λ_n[G] - modules et plus précisément un complexe parfait (VIII,7) de Λ_n[G] - modules (IX,2).' (the second accent of 'précisément' is a hand-written correction)",
    r"the editorial comment '% [faithful] le livre imprime « Par conséquence » ... brûlé)' stands right after '$\La_n[G]$-modules' on the same line, so the printed words after it ('et plus précisément ... (IX, 2).') are inside the comment and are lost in the output, which reads '... complexe de Λ_n[G]-modules' and ends the paragraph without its full stop",
    "missing", "high",
    {"old": old408, "new": new408},
    r"The edit keeps the comment but puts it on a line of its own, so that '-modules', the comment line and 'et plus précisément ...' join with one space in the output; one edit (two separate edits would print 'moduleset' if only the second were applied). Both layers have the comment (current line 13797). 'Par conséquence' is the printed wording, as the comment says.")
add(408, "Exposé XII: the complex H_{n,U',X'} and its dual (pp. 408 and 410, every occurrence)",
    "a script capital H (curved strokes, a loop at the foot of the left stem; not the plain typed H of 'Hom' in the display of p. 408): ℋ_{n,U',X'}, ℋ^∨_{n,U',X'}, and in the subscripts f'_{ℋ_{n,U',X'}}, g_{ℋ_{n,U',X'}}, f'_{ℋ_{n,U'}} of p. 410",
    r"plain H: '$H_{n,U',X'} = \R\Gamma_{X'}(\La_{n,U',X'})$' and 'son dual $H_{n,U',X'}^\vee$' (p. 408), the display 'H_{n,U',X'}^\vee = \R\Gamma_{X'}(...)^\vee' (p. 408), '(1.4) g_{H_{n,U',X'}} \circ f'_{H_{n,U',X'}}' (p. 410)",
    "font", "high", None,
    r"Convention of the TeX in Exposé XII, not itemized: one decision for the exposé (for example \mathcal{H}, as the file writes the print's script F of ℱ_! on p. 410 as \mathcal{F}). The diplomatic s5.tex has 37 such H_{n,U'...}/H_{m,U'...} in Exposé XII (lines 13777-14826); pages after 410 not checked here.")
add(408, "'... un endomorphisme φ : G → G du groupe G tel que les deux conditions suivantes soient remplies :'",
    "tel que (singular)",
    "du groupe $G$ tel que les deux conditions", "misprint_in_print", "medium", None,
    "Agreement slip of the redaction: 'tel' refers to the two endomorphisms f' and φ. The TeX keeps the printed reading (both layers). The same 'tel que' for 'tels que' on pp. 409 and 410 (three times); list only if the corrected edition fixes grammar slips (as 'troisième terme', p. 381).",
    corrected="tels que")

# ---------------- p. 409 ----------------
add(409, "diagram (1.3), label of the left vertical arrow",
    "f'_{Λ_{n,U',X'}} stands to the right of the arrow, as the labels f'_{Λ_{n,X'}} and f'_{Λ_{n,Y'}} of the other two vertical arrows",
    r"""\arrow[d, "f'_{\La_{n,U',X'}}"'] (the swap mark sets the label to the left)""",
    "other", "high",
    {"old": r"""\arrow[d, "f'_{\La_{n,U',X'}}"']""", "new": r"""\arrow[d, "f'_{\La_{n,U',X'}}"]"""},
    "tikz-cd sets an unswapped label to the right of a downward arrow (as on p. 86). The other two labels and the full stop after the lower row are right.")
add(409, "'On obtient donc les homomorphismes de faisceaux : ... tel que le diagramme suivant ... soit commutatif :'",
    "tel que (singular)",
    "tel que le diagramme suivant", "misprint_in_print", "medium", None,
    "Agreement slip ('les homomorphismes ... tels que'); the TeX keeps the printed reading (both layers). See p. 408.",
    corrected="tels que")

# ---------------- p. 410 ----------------
add(410, "first display, second line: (f'_{H_{n,U'}})^∨",
    "the inner subscript is 'n,U'' only (no X'; clear at 2x), while the left side and both ends of the arrow have n,U',X'",
    r"(f'_{H_{n,U'}})^\vee", "misprint_in_print", "high", None,
    r"The definition is f'^\vee_{H_{n,U',X'}} = (f'_{H_{n,U',X'}})^\vee (line 1 defines f'_{H_{n,U',X'}}; line 4 has (g_{H_{n,U',X'}})^\vee). The diplomatic TeX keeps the printed reading; the current layer already reads (f'_{H_{n,U',X'}})^\vee.",
    corrected=r"(f'_{H_{n,U',X'}})^\vee")
add(410, "first display, third line (g_{H} = RΓ_{X'}(g_{Λ_{n,U',X'}}) : H -> H)",
    "no comma at the end of the line (clean paper; lines 1, 2 and 4 end with a comma; checked at 1.5x)",
    r"H_{n,U',X'} \longrightarrow H_{n,U',X'} \quad , \\ (line 3)", "punctuation", "high",
    {"old": r"(g_{\La_{n,U',X'}}) : H_{n,U',X'} \longrightarrow H_{n,U',X'} \quad , \\",
     "new": r"(g_{\La_{n,U',X'}}) : H_{n,U',X'} \longrightarrow H_{n,U',X'} \\"},
    "The TeX adds punctuation at the end of a display line.")
add(410, "relation (1.5), last term",
    "'∘ f'_{ℋ_{n,U',X'}} .': no ∨ on the last f' (clean paper where the ∨ stands on the other three terms; checked at 4x)",
    r"\circ f'^\vee_{H_{n,U',X'}} \quad .", "misprint_in_print", "high",
    {"old": r"\circ f'^\vee", "new": r"\circ f'"},
    r"(1.5) is the dual of (1.4), so the last term is f'^\vee_{H_{n,U',X'}} (the text below takes the trace of f'^\vee). The TeX silently corrects (both layers); the fix restores the printed reading (diplomatic layer only).",
    corrected=r"\circ f'^\vee")
add(410, "'en térmes d'invariants locaux'",
    "térmes, with an acute accent on the first e (clear at 4x); 'termes que nous allons définir' in the same sentence has none",
    "en térmes d'invariants", "misprint_in_print", "high", None,
    "Typing error. The diplomatic TeX keeps the printed reading; the current layer already reads 'termes'.",
    corrected="termes")
add(410, "'... des homomorphismes de complexes de Λ_n-modules : [display] tel que les relations suivantes soient vraies :'",
    "tel que (singular)",
    "tel que les\nrelations suivantes", "misprint_in_print", "medium", None,
    "Agreement slip ('des homomorphismes ... tels que'); the TeX keeps the printed reading (both layers). See p. 408.",
    corrected="tels que")
add(410, "§2, 'Soient pour cela n,m deux entiers positifs tel que m ≥ n'",
    "tel que (singular)",
    "deux entiers positifs tel que $m \\geq n$", "misprint_in_print", "medium", None,
    "Agreement slip ('deux entiers positifs tels que'); the TeX keeps the printed reading (both layers). See p. 408.",
    corrected="tels que")
add(410, "end of the page / folio-411 marker: the display α_{m,n} : Λ_m ⟶ Λ_n",
    "p. 410 ends with 'tel que m ≥ n . Les homomorphismes d'anneaux :' and the footnote '(*) cf. III B 5.12 .'; p. 411 begins with the display 'α_{m,n} : Λ_m ⟶ Λ_n', then 'engendrent les homomorphismes ...' (b411_415/page_411_s1.png)",
    r"the display '\[ \alpha_{m,n} : \La_m \longrightarrow \La_n \]' ends page_410.tex (s5.tex diplomatic lines 13867-13869, current 13863-13865); the folio-411 marker follows it",
    "marker", "high", None,
    r"Page 411 really begins at the '\[' of that display. Exact fix: python -I move_marker.py 5 411 '\[' --before (simulated in memory on both layers: the marker moves back 49 characters to its own line between '... Les homomorphismes d'anneaux :' and '\['). Run it once only: the anchor is the last '\[' above the marker, and a second run would move the marker 555 characters further back, to the trace display of p. 410. Batch 411-415 may report the same move. Text not moved; the display agrees with the print of p. 411.")

# ---------------- checks ----------------
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    n = pages[d["page"]].count(fx["old"])
    assert n == 1, (d["page"], fx["old"][:60], n)
    assert "%%%%%%%%%%" not in fx["old"]
    for c in fx["old"] + fx["new"]:
        assert c == "\n" or ord(c) >= 32, repr(c)
# misprint fixes change only the misprinted characters; null-fix misprints: check the tex excerpt exists
for d in F:
    if d["kind"] == "misprint_in_print" and d["fix"] is None:
        probe = d["tex"].replace("\\n", "\n")
        assert pages[d["page"]].count(probe) >= 1, (d["page"], probe)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
cnt = {}
for d in F:
    k = "m" if d["kind"] == "misprint_in_print" else "n"
    cnt.setdefault(d["page"], {"n": 0, "m": 0})[k] += 1
print(len(F), "findings;", cnt)
print("old408 =", repr(old408))
print("new408 =", repr(new408))
