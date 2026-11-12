"""Write run_6/findings_006_010.json (SGA 6, pp. 6-10) and check that every fix's old occurs exactly once on its page."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------- page 6 ----------------
add(6, "§3.1, line 1, 'l'observation qui avait servie de point de départ'", "qui avait servie de point de départ",
    "servie (printed reading kept)", "misprint_in_print", "medium", None,
    "Agreement slip of the print: with avoir and no preceding direct object the participle stays invariable. The TeX "
    "keeps the printed reading; the corrected layer already reads 'servi'.",
    corrected="servi")
add(6, "§3.1, 'L'homomorphisme x -> x cl.(O_X)'",
    "x →x cl.(O_X): a plain typed arrow, no bar at its tail (both scans)",
    r"$x\mapsto x\,\cl_\bullet(\underline O_X)$", "symbol", "medium",
    fx(r"x\mapsto x", r"x\to x"),
    "The arrow has no tail bar in either scan; the TeX writes \\mapsto.")
add(6, "§3.1, 'Comme nous avons signalé dans 2.3., ces λ-anneaux'",
    "dans 2.3., ces (full stop after the paragraph number, then the comma; both scans)",
    "dans 2.3, ces", "punctuation", "high",
    fx("dans 2.3, ces", "dans 2.3., ces"),
    "The reference repeats the printed paragraph number with its full stop (heading 2.3. on p. 4).")
add(6, "display after 'qui ne peut plus être définie par la formule naïve'",
    "f_*(cl˙(E)) = Σ_i (-1)^i cl˙(R^i f_*(F)) (underlined E on the left, F on the right; both scans)",
    r"f_*(\cl^\bullet(\underline E))=\sum_i(-1)^i\cl^\bullet\bigl(R^if_*(\underline F)\bigr) (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The naive formula is about one locally free F (next line: 'car même si F est localement libre'); the E on the "
    "left is a slip of the print. The TeX keeps it; the corrected layer still reads \\underline E.",
    corrected=r"f_*(\cl^\bullet(\underline F))=\sum_i(-1)^i\cl^\bullet\bigl(R^if_*(\underline F)\bigr)")
add(6, "throughout (here: §3.1 'Pour notre formulation ...'; p. 9 §3.3 'dans le cas d'un morphisme ...'; "
       "p. 10 §4.1 'pour un schéma ...')",
    "the typescript underlines word groups only: the formulas, the commas after them, parentheses and quotes stay "
    "outside the underline (p. 6: the comma after 'généralisé', K˙(X), K˙(Y), K.(X), K.(Y); p. 9: X,Y; p. 10: X, "
    "the parentheses, K(X), [RRR], K˙(X), K(Parf(X)), '3 1. ,', the quotes around 'bon')",
    r"one \uline{...} over the whole statement, formulas and punctuation included", "underline", "medium", None,
    "Convention for one decision, not a page fix (as SGA 7 II items 48 and 73): \\uline{Pour notre formulation du "
    "théorème de Riemann--Roch généralisé, nous travaillerons exclusivement avec $K^\\bullet(X)$, $K^\\bullet(Y)$, à "
    "l'exclusion de $K_\\bullet(X)$, $K_\\bullet(Y)$} (p. 6), \\uline{... noeth\\'eriens $X,Y$ admettant tous deux ...} "
    "(p. 9), \\uline{pour un sch\\'ema $X$ (ou plus ...} (p. 10). On p. 10 the \\uline also covers words that the print "
    "leaves plain: separate findings with fixes.")

# ---------------- page 7 ----------------
add(7, "'le complexe Rf_*(F) est \"parfait\"'", "\"parfait\" with the word underlined inside the quotes (both scans)",
    "«~parfait~»", "underline", "high",
    fx("«~parfait~»", r"«~\underline{parfait}~»"),
    "Same form as «~\\underline{localement d'insersection complète}~» on p. 8.")
add(7, "triangle after 'pour tout triangle distingué'",
    "a full stop to the right of the diagram, on the line of K' → K (both scans)",
    "tikzcd without punctuation", "punctuation", "high",
    fx(r"& K \arrow[ul]", r"& K \arrow[ul] ."),
    "Punctuation printed after a diagram that the TeX leaves out; set in the last cell, as elsewhere in main.tex "
    "('&H .').")
add(7, "'isomorphe dans D(Y) à un complexe L! à degrés bornés'",
    "L!: a prime over a baseline full stop in one character cell (both scans), the typescript's L'. as L. is L_•",
    "$L'$", "symbol", "medium",
    fx("complexe $L'$", r"complexe $L'_\bullet$"),
    "First of four: the print writes this second complex L! here, on p. 8 ('où L! est comme ci-dessus') and on "
    "p. 10 ('Si L. et L! sont', 'L.⊗L!'); the TeX drops the dot each time. Apply all four or none. The components "
    "L!_i (p. 8, twice: same glyph with the index i below) are left as L'_i.")
add(7, "display after 'l'homomorphisme canonique'", "K˙(X) ⟶ K(Parf(Y)) , (both scans)",
    r"K^\bullet(X)\longrightarrow K(\Parf(Y)), (printed reading kept)", "misprint_in_print", "high", None,
    "The canonical map goes from K˙(Y): the sentence is about perfect complexes on Y, with an ample invertible "
    "Module on Y. The TeX keeps the X; the corrected layer still reads K^\\bullet(X).",
    corrected=r"K^\bullet(Y)\longrightarrow K(\Parf(Y))")

# ---------------- page 8 ----------------
add(8, "first line, 'qui n'est d'ailleurs autre que'", "d'ailleurs",
    "d'<line break>ailleurs (TeX sets d' ailleurs)", "other", "medium",
    fx("d'\nailleurs", "d'ailleurs"),
    "A source line break inside the word renders as a space after the apostrophe; the current layer has the same "
    "break.")
add(8, "display 'cl(L.) = Σ_i (-1)^i cl˙(L!_i)'", "a full stop to the right of the display (both scans)",
    r"\cl(L_\bullet)=\sum_i(-1)^i\cl^\bullet(L'_i) (no punctuation)", "punctuation", "medium",
    fx("\\cl^\\bullet(L'_i)\n\\]", "\\cl^\\bullet(L'_i).\n\\]"),
    "The mark stands where the typescript puts the full stop after its displays (as after T_f ∈ K˙(X) and Rf_* on "
    "this page) and is in the witness too; it is a little less round than the other stops.")
add(8, "'où L! est comme ci-dessus'", "L! (prime over a baseline full stop), as on p. 7", "$L'$", "symbol", "medium",
    fx("où $L'$ est", r"où $L'_\bullet$ est"),
    "Second of the four L! (see p. 7); apply all or none. In the display and in 'les L!_i' the same glyph carries "
    "the index i: left as L'_i.")
add(8, "heading 3.2", "3.2. (trailing full stop)", r"\subsubsection*{3.2}", "punctuation", "high",
    fx(r"\subsubsection*{3.2}", r"\subsubsection*{3.2.}"),
    "The printed paragraph number ends with a full stop (as 2.3., 2.4. on pp. 4-5).")
add(8, "§3.2, 'identifie X à un sous-schémas de X''", "sous-schémas", "sous-schémas (printed reading kept)",
    "misprint_in_print", "high", None,
    "Plural s in the print, as on p. 3; the TeX keeps it; the corrected layer already reads 'sous-schéma'.",
    corrected="sous-schéma")
add(8, "§3.2, 'il en est de même pour la classe T_f défini par la formule (2.1)'", "la classe T_f défini",
    "$T_f$ défini (printed reading kept)", "misprint_in_print", "medium", None,
    "Agreement slip (la classe ... définie); the TeX keeps it; the corrected layer already reads 'définie'.",
    corrected="définie")
add(8, "§3.2, 'un morphisme \"localement d'insersection complète\"'", "insersection",
    "insersection (printed reading kept)", "misprint_in_print", "high", None,
    "The TeX keeps it; the corrected layer already reads 'intersection'.",
    corrected="intersection")
add(8, "footnote, 'ce qui ne risque d'entrainer aucune confusion'", "d'entrainer (no circumflex)",
    "d'entrainer (printed reading kept)", "misprint_in_print", "low", None,
    "The spelling of the time is entraîner; the typist types the circumflex elsewhere (disparaîtra, p. 9). The TeX "
    "keeps the printed reading.",
    corrected="d'entraîner")

# ---------------- page 9 ----------------
add(9, "heading 3.3", "3.3. (trailing full stop)", r"\subsubsection*{3.3}", "punctuation", "high",
    fx(r"\subsubsection*{3.3}", r"\subsubsection*{3.3.}"),
    "The printed paragraph number ends with a full stop.")
add(9, "equation number (3 4)", "(3 4): the full stop between the digits prints in neither scan (its cell is there)",
    r"\tag{3 4}", "punctuation", "low",
    fx(r"\tag{3 4}", r"\tag{3.4}"),
    "The typewriter's full stop is faint throughout (4.3 and (3.4) on p. 10 barely print) and is lost here, as "
    "'4 3' on p. 4. The TeX itself writes the stop at the same kind of gap in (3 1) p. 6 and 4 2 p. 10. If the stop "
    "was never typed, this is instead a misprint the TeX keeps (correct reading (3.4)): one decision for the volume.")

# ---------------- page 10 ----------------
add(10, "start of page",
    "p. 10 begins 'de Modules inversibles amples sur X et Y.'; p. 9 ends '... d'une hypothèse d'existence' (both "
    "scans)",
    "'de' is the last word of the last line of page_009.tex (under the folio-9 marker); page_010.tex begins "
    "'Modules inversibles'", "marker", "high", None,
    "Page 10 really begins with 'de'. Move the folio-10 marker before it: python -I move_marker.py 6 10 \"de\" "
    "--before (simulated on both layers: '... d'existence', the marker, then 'de', then 'Modules inversibles').")
add(10, "heading 4.1", "4.1. (trailing full stop)", r"\subsubsection*{4.1}", "punctuation", "high",
    fx(r"\subsubsection*{4.1}", r"\subsubsection*{4.1.}"),
    "The printed paragraph number ends with a full stop.")
add(10, "§4.1, 'de [RRR] n'est pas l'anneau K˙(X)'",
    "'n'est pas' is not underlined: the underline stops after 'de' and starts again at 'l'anneau' (both scans)",
    r"inside \uline{...}", "underline", "high",
    fx("de [RRR] n'est pas l'anneau", r"de [RRR]} n'est pas \uline{l'anneau"),
    "Words the print leaves plain inside the TeX's single underline (beyond the formula convention). Independent of "
    "the next fix.")
add(10, "§4.1, end of the underlined statement",
    "the underline ends with 'groupe que nous noterons ici'; 'K˙(X), et que nous distinguerons du groupe \"naif\" de "
    "3.1, que nous notons K˙_naif(X)' is not underlined (both scans)",
    r"\uline{...} runs to $K^\bullet_{\mathrm{naif}}(X)$}", "underline", "high",
    fx(r"ici $K^\bullet(X)$, et que nous distinguerons du groupe ``naif'' de 3.1, que nous notons "
       r"$K^\bullet_{\mathrm{naif}}(X)$}",
       r"ici} $K^\bullet(X)$, et que nous distinguerons du groupe ``naif'' de 3.1, que nous notons "
       r"$K^\bullet_{\mathrm{naif}}(X)$"),
    "One edit, so that the braces stay balanced.")
add(10, "§4.1, 'envisagé dans 3 1. ,'", "3 1. , (no ink between the digits in either scan)", r"dans 3 1., d\'efini",
    "punctuation", "low",
    fx("dans 3 1.,", "dans 3.1.,"),
    "Lost full stop between digits, as (3 4) on p. 9: same decision.")
add(10, "§4.1, 'Avec la définition de K˙(X) adopté maintenant'", "adopté",
    r"adopt\'e (printed reading kept)", "misprint_in_print", "medium", None,
    "Agreement slip (la définition ... adoptée); the TeX keeps it; the corrected layer already reads 'adoptée'.",
    corrected=r"adopt\'ee")
add(10, "§4.1, 'par la formule (3 2)'", "(3 2) (no ink between the digits in either scan)", "(3 2)",
    "punctuation", "low",
    fx("formule (3 2)", "formule (3.2)"),
    "Lost full stop between digits, as (3 4) on p. 9: same decision.")
add(10, "§4.1, 'du groupe \"naif\" de 3.1, que nous notons K˙_naif(X)'", "naif (twice, no diaeresis)",
    r"``naif'' and \mathrm{naif} (printed reading kept)", "misprint_in_print", "low", None,
    "naïf without its diaeresis (twice); the typist elsewhere writes the i-diaeresis as i-circumflex (naîve, p. 6). "
    "The TeX keeps the printed reading.",
    corrected=r"na\"{\i}f")
add(10, "§4.2, 'un nouveau problème d'algébre homologique'", "algébre (acute accent)",
    r"alg\'ebre (printed reading kept)", "misprint_in_print", "high", None,
    "Wrong accent in the print; the TeX keeps it.",
    corrected=r"alg\`ebre")
add(10, "§4.2, '(NB Si L. et L! sont deux complexes parfaits'", "L! (prime over a baseline full stop), as on p. 7",
    "$L'$", "symbol", "medium",
    fx(r"Si $L_\bullet$ et $L'$ sont", r"Si $L_\bullet$ et $L'_\bullet$ sont"),
    "Third of the four L! (see p. 7); apply all or none.")
add(10, "§4.2, 'leur produit tensoriel total L.⊗L! )'", "L.⊗L! (the second factor again L!)", r"\otimes^{\mathbf L}L'$",
    "symbol", "medium",
    fx(r"\otimes^{\mathbf L}L'$", r"\otimes^{\mathbf L}L'_\bullet$"),
    "Fourth of the four L! (see p. 7); apply all or none.")
add(10, "§4.2, 'Plus précisement, il y aurait lieu'", "précisement (no accent on the second e)",
    r"pr\'ecisement (printed reading kept)", "misprint_in_print", "medium", None,
    "Missing accent in the print; the TeX keeps it.",
    corrected=r"pr\'ecis\'ement")
add(10, "§4.2, 'Cette question n'a pas encore été tiré au clair'", "tiré au clair",
    r"tir\'e au clair (printed reading kept)", "misprint_in_print", "medium", None,
    "Agreement slip (cette question ... tirée); the TeX keeps it; the corrected layer already reads 'tirée'.",
    corrected=r"tir\'ee au clair")
add(10, "§4.2, 'Un fois cette question résolue'", "Un fois", "Un fois (printed reading kept)",
    "misprint_in_print", "high", None,
    "Missing e in the print; the TeX keeps it; the corrected layer still reads 'Un fois'.",
    corrected="Une fois")
add(10, "end of page",
    "p. 10 ends '... et de définir enfin la classe tangente relative virtuelle'; p. 11 begins with the display "
    "'T_f ∈ K˙(X) .' (DjVu witness p. 22)",
    r"page_010.tex ends with \[ T_f\in K^\bullet(X). \], which belongs to p. 11", "marker", "high", None,
    "Move the folio-11 marker above that display: python -I move_marker.py 6 11 \"\\[\" --before (simulated on both "
    "layers: the marker, then \\[ T_f\\in K^\\bullet(X). \\], then 'Lorsque $f$ admet une factorisation').")

# ---------------- write and check ----------------
out = RUN / "findings_006_010.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    t = (RUN / "b006_010" / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1 or "%%%%%%%%%%" in d["fix"]["old"] or "%%%%%%%%%%" in d["fix"]["new"]:
        bad += 1
        print("BAD", d["page"], n, repr(d["fix"]["old"]))
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print(len(F), "findings;", "bad fixes:", bad)
print(" ".join(f"p{p} {c[0]}/{c[1]}" for p, c in sorted(counts.items())))
