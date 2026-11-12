"""Write findings_011_015.json for the SGA 6 pp. 11-15 check and verify every fix's "old" (once per page file).

usage: python -I make_findings.py
"""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
OUT = RUN / "findings_011_015.json"


def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 11 ----------------
    # The folio-11 marker (display T_f in K(X) printed at the top of p. 11, left at the end of p. 10) was reported in
    # findings_006_010.json and is already moved in both layers of main.tex: not repeated here (a second run of the move
    # would take the c_i display of p. 10 as anchor).
    F(11, "equation number (4 1)",
      "(4 1): no full stop between the digits in either scan; its blank character cell is there, where (4.2) and (4.3) have their stop",
      "\\tag{4 1}", "punctuation", "medium", ("\\tag{4 1}", "\\tag{4.1}"),
      "Lost stop, the same case as (3 4) p. 9 and '3 1.', '(3 2)' p. 10 of findings_006_010.json, which main.tex now reads with "
      "the stop. If the stop was never typed, this is instead a misprint the TeX keeps (correct reading (4.1))."),
    F(11, "display after 'induit par la différentielle extérieure'",
      "d_{X'/X} : J ⊂ O_{X'} → Ω^1_{X'/Y} (index X'/X, both scans)",
      "d_{X'/X}:\\underline J (printed reading kept)", "misprint_in_print", "medium", None,
      "The exterior differential of X' relative to Y: its target is Ω^1_{X'/Y}, and X' is smooth over Y, not a scheme over X. "
      "The TeX keeps the printed index; the corrected layer also reads d_{X'/X}.",
      corrected="d_{X'/Y}"),
    F(11, "heading 4.4", "4.4. (trailing full stop)", "\\subsubsection*{4.4}", "punctuation", "high",
      ("\\subsubsection*{4.4}", "\\subsubsection*{4.4.}"),
      "The printed paragraph number ends with a full stop (as 4.1. on p. 10)."),
    F(11, "'et le complexe de chaines'", "chaines (no circumflex)", "chaines (printed reading kept)",
      "misprint_in_print", "low", None,
      "Missing circumflex, as d'entrainer (p. 8, findings_006_010.json); again on p. 12. The TeX keeps the printed reading, "
      "and so does the corrected layer.",
      corrected="cha\\^{\\i}nes"),
    F(11, "§4.4, 'toute algèbre B sur un anneau A apparait comme quotient'", "apparait (no circumflex)",
      "apparait (printed reading kept)", "misprint_in_print", "low", None,
      "Missing circumflex; the TeX and the corrected layer keep it.",
      corrected="appara\\^{\\i}t"),
    # ---------------- page 12 ----------------
    F(12, "first line, 'non recollables. Voici une construction'",
      "'tiellement non recollables  Voici une construction générale de L^{X/Y} , vala-': the next sentence follows on the same "
      "line (both scans)",
      "blank line (new paragraph) before 'Voici'", "other", "high", ("recollables.\n\nVoici", "recollables. Voici"),
      "The print runs on. Its full stop after 'recollables' prints in neither scan, but the blank cell for it is there (spacing as "
      "in 'A-Algèbre. Soit' below): a lost stop, so the TeX's full stop stands."),
    F(12, "display 'ϕ:C = A[T] → B'", "closed phi: an o crossed by a slanted stroke (both scans)",
      "\\varphi:C=A[T]", "symbol", "medium", ("\\varphi:C=A[T]", "\\phi:C=A[T]"),
      "Closed form, like the p. 3 phi already changed to \\phi (findings_001_005.json); Exposé 0 otherwise writes \\phi. "
      "Apply together with the next fix."),
    F(12, "'Soit J le noyau de ϕ'", "the same closed phi", "noyau de $\\varphi$", "symbol", "medium",
      ("noyau de $\\varphi$", "noyau de $\\phi$"),
      "Same letter as in the display above: both or neither."),
    F(12, "'= A(U)-algèbre commutative libre engendré par T(U)'", "engendré",
      "engendr\\'e par $T(U)$ (printed reading kept)", "misprint_in_print", "medium", None,
      "Agreement slip (algèbre ... engendrée, as 'la A-Algèbre commutative libre engendrée par T' in the same sentence). "
      "The TeX keeps it; the corrected layer also reads engendr\\'e.",
      corrected="engendr\\'ee par $T(U)$"),
    F(12, "'défini par l'homomorphisme naturelle'", "naturelle", "naturelle (printed reading kept)",
      "misprint_in_print", "high", None,
      "Agreement slip (homomorphisme is masculine); the TeX keeps it; the corrected layer already reads 'naturel'.",
      corrected="naturel"),
    F(12, "'le complexe de chaines de longueur 1'", "chaines (no circumflex)", "chaines (printed reading kept)",
      "misprint_in_print", "low", None,
      "As on p. 11; the TeX and the corrected layer keep it.",
      corrected="cha\\^{\\i}nes"),
    F(12, "'la désignation de complexe cotangent relatif L^{X/Y} de X sur Y'",
      "underlined: 'complexe cotangent', 'relatif', 'de', 'sur'; L^{X/Y}, X and Y stand outside the underline (both scans)",
      "\\uline{complexe cotangent relatif $L^{X/Y}_\\bullet$ de $X$ sur $Y$}", "underline", "medium", None,
      "Instance of the convention reported in findings_006_010.json (formulas inside the TeX's underline); no word is left plain, "
      "so no page fix. If the volume follows the print: \\uline{complexe cotangent relatif} $L^{X/Y}_\\bullet$ \\uline{de} $X$ "
      "\\uline{sur} $Y$."),
    F(12, "'de définir T_f comme un élément de K˙_naif(X)' and 'de préférence à K˙_naif(X)'",
      "naif (twice, no diaeresis)", "K^\\bullet_{\\mathrm{naif}}(X), twice (printed reading kept)",
      "misprint_in_print", "low", None,
      "As naif on p. 10 (findings_006_010.json); the TeX and the corrected layer keep it.",
      corrected="K^\\bullet_{\\text{na\\\"{\\i}f}}(X)"),
    F(12, "heading 4.5", "4.5. (trailing full stop)", "\\subsubsection*{4.5}", "punctuation", "high",
      ("\\subsubsection*{4.5}", "\\subsubsection*{4.5.}"),
      "The printed paragraph number ends with a full stop."),
    F(12, "§4.5, 'faite implicitement dans les sections qui précédent'", "précédent (two acute accents)",
      "pr\\'ec\\'edent (printed reading kept)", "misprint_in_print", "medium", None,
      "Verb (les sections qui précèdent); the TeX keeps the print's accent; the corrected layer already reads pr\\'ec\\`edent.",
      corrected="pr\\'ec\\`edent"),
    # ---------------- page 13 ----------------
    F(13, "start of page",
      "p. 12 ends '... le spectre d'un corps'; p. 13 begins 'algébrique clos de caractéristique p > 0' (both scans)",
      "page_012.tex ends 'd'un corps alg\\'' and page_013.tex begins 'ebrique clos': the folio-13 marker stands inside the word",
      "marker", "high", None,
      "Page 13 really begins with alg\\'ebrique. Move the folio-13 marker before it: python -I move_marker.py 6 13 \"alg\\'\" --before "
      "(simulated on both layers: '... d'un corps', the marker, then alg\\' alone on a line, then 'ebrique clos'). Then join that "
      "line to the next ('alg\\'ebrique clos') in both layers."),
    F(13, "first line, 'd'un corps algébrique clos de caractéristique p > 0'", "algébrique clos",
      "alg\\' + ebrique clos (printed reading kept; the word is split by the marker)", "misprint_in_print", "high", None,
      "The print drops -ment; the TeX keeps it, and so does the corrected layer.",
      corrected="alg\\'ebriquement clos"),
    # ---------------- page 14 ----------------
    F(14, "start of page",
      "p. 13 ends '... on sait lui associer grâce à Atiyah-Hirzebruch'; p. 14 begins '[1] un homomorphisme groupes' (both scans)",
      "'[1] un' ends the last line of page_013.tex (under the folio-13 marker); page_014.tex begins 'homomorphisme groupes'",
      "marker", "high", None,
      "Page 14 really begins with '[1] un'. Move the folio-14 marker before it: python -I move_marker.py 6 14 \"[1] un\" --before "
      "(simulated on both layers: '... Atiyah--Hirzebruch', the marker, then '[1] un', then 'homomorphisme ...')."),
    F(14, "first line, '[1] un homomorphisme groupes'", "homomorphisme groupes",
      "homomorphisme groupes (printed reading kept)", "misprint_in_print", "high", None,
      "The print drops 'de'; the TeX keeps it; the corrected layer already reads 'homomorphisme de groupes'.",
      corrected="homomorphisme de groupes"),
    F(14, "'le théorème de finitude de Grauert [4]'", "Grauert [4]", "Grauert [4] (printed reading kept)",
      "misprint_in_print", "high", None,
      "Wrong reference number: in the exposé's bibliography (p. 19, read in the witness) Grauert is [3]; [4] is [RRR]. "
      "The TeX and the corrected layer keep [4].",
      corrected="Grauert [3]"),
    F(14, "diagram (5.3), left vertical arrow", "f_* to the left of the left arrow (f^top_* to the right of the right arrow)",
      "\\downarrow f_* (label to the right of the arrow)", "formula", "medium", ("\\downarrow f_* &&", "f_*\\downarrow &&"),
      "Label on the wrong side of the arrow."),
    F(14, "'de ses généralisations dues à Shih [7] et Atiyah'", "Shih [7]", "Shih [7] (printed reading kept)",
      "misprint_in_print", "medium", None,
      "Wrong reference number: Shih is [6] in the bibliography (p. 19); [7] is Atiyah-Hirzebruch, Riemann-Roch for analytic "
      "embeddings, rightly cited for the projective case three lines above. The TeX and the corrected layer keep [7].",
      corrected="Shih [6]"),
    F(14, "'où les flèches horizontales'", "flêches (circumflex, both scans; 'première' on p. 15 has its grave)",
      "fl\\`eches", "misprint_in_print", "high", ("fl\\`eches", "fl\\^eches"),
      "Wrong accent in the print; the TeX silently corrects. Same on p. 15 (flêche): both or neither.",
      corrected="fl\\`eches"),
    # ---------------- page 15 ----------------
    F(15, "first line, 'la première flêche verticale'", "flêche (circumflex, both scans)", "fl\\`eche",
      "misprint_in_print", "high", ("fl\\`eche", "fl\\^eche"),
      "As flêches on p. 14; the TeX silently corrects.",
      corrected="fl\\`eche"),
    F(15, "'l'homomorphisme de Gysin en cohomologie rationelle'", "rationelle", "rationelle (printed reading kept)",
      "misprint_in_print", "high", None,
      "Single n in the print; the TeX keeps it; the corrected layer already reads 'rationnelle'.",
      corrected="rationnelle"),
    F(15, "§6, 'dont l'existence a été signalé dans 3.1'", "signalé", "signal\\'e (printed reading kept)",
      "misprint_in_print", "medium", None,
      "Agreement slip (l'existence ... signalée); the TeX keeps it; the corrected layer already reads signal\\'ee.",
      corrected="signal\\'ee"),
    F(15, "'Filt_i K.(X) étant engendré par des classes'", "Filt_i K.(X)",
      "$\\Fil_iK_\\bullet(X)$ (the preamble's \\Fil is \\operatorname{Fil}: it prints Fil)", "word", "high",
      ("$\\Fil_iK_\\bullet(X)$", "$\\operatorname{Filt}_iK_\\bullet(X)$"),
      "The print writes Filt, as in (2.3) p. 4 and (3.4) p. 9, where the TeX has \\operatorname{Filt}. One of three Filt fixes on "
      "this page (with the two in (6.1)): apply all; the same strings stand in the corrected layer."),
    F(15, "'tel que dim supp.F ≤ i'", "dim supp.F (a full stop after supp, both scans)", "\\dim \\operatorname{supp}F\\le i",
      "punctuation", "high", ("\\operatorname{supp}F", "\\operatorname{supp}.F"),
      "The abbreviation's full stop is printed; the TeX drops it."),
    F(15, "(6.1), left side", "Filt^i K˙(X) . Filt_j(K.(X)", "\\Fil^iK^\\bullet(X)\\cdot \\Fil_j(K_\\bullet(X)", "word", "high",
      ("\\Fil^iK^\\bullet(X)\\cdot \\Fil_j", "\\operatorname{Filt}^iK^\\bullet(X)\\cdot \\operatorname{Filt}_j"),
      "Filt, as above; the edit leaves the misprinted parenthesis alone (separate finding)."),
    F(15, "(6.1), right side", "⊂ Filt_{j-i} K.(X)", "\\subset \\Fil_{j-i}K_\\bullet(X)", "word", "high",
      ("\\subset \\Fil_{j-i}", "\\subset \\operatorname{Filt}_{j-i}"),
      "Filt, as above."),
    F(15, "(6.1), 'Filt_j(K.(X)'", "Filt_j(K.(X): a parenthesis opened and never closed (both scans)",
      "\\Fil_j(K_\\bullet(X) (printed reading kept)", "misprint_in_print", "high", None,
      "Stray parenthesis; the TeX keeps it; the corrected layer already reads \\Fil_j K_\\bullet(X) (its \\Fil to change with "
      "the Filt fixes).",
      corrected="\\operatorname{Filt}_jK_\\bullet(X)"),
    F(15, "'moins fine que l'équivalence rationelle, lorsque X'", "rationelle", "rationelle (printed reading kept)",
      "misprint_in_print", "high", None,
      "As in the first line of the page; the corrected layer already reads 'rationnelle'.",
      corrected="rationnelle"),
]

ok = True
for f in findings:
    if f["fix"] is None:
        continue
    t = (RUN / "b011_015" / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], repr(f["fix"]["old"]), n)
    if "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False
        print("touches marker", f["page"])
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("all olds unique" if ok else "PROBLEMS")
print(len(findings), {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})
