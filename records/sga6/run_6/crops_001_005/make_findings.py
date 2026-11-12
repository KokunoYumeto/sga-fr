"""Write run_6/findings_001_005.json (SGA 6, pp. 1-5) and check that every fix's old occurs exactly once on its page."""
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


# ---------------- page 1 ----------------
add(1, "heading 'Exposé 0'", "Exposé 0 (underlined)", r"\section*{Exposé 0}", "underline", "low",
    fx(r"\section*{Exposé 0}", r"\section*{\underline{Exposé 0}}"),
    "The typescript underlines the exposé heading (single line, both scans); the TeX sets it as a plain \\section*. "
    "Apply only if the exposé headings are to keep the print's underline.")
add(1, "title, first line", "ESQUISSE D'UN PROGRAMME POUR UNE THEORIE DES INTERSECTIONS (double underline)",
    r"\underline{ESQUISSE D'UN PROGRAMME POUR UNE THÉORIE DES INTERSECTIONS}", "underline", "high",
    fx(r"\underline{ESQUISSE D'UN PROGRAMME POUR UNE THÉORIE DES INTERSECTIONS}",
       r"\underline{\underline{ESQUISSE D'UN PROGRAMME POUR UNE THÉORIE DES INTERSECTIONS}}"),
    "Both title lines carry two parallel underlines in both scans ('par A. Grothendieck' one); same form as the "
    "SGA 7 I title fix.")
add(1, "title, second line", "SUR LES SCHEMAS GENERAUX (double underline)", r"\underline{SUR LES SCHÉMAS GÉNÉRAUX}",
    "underline", "high",
    fx(r"\underline{SUR LES SCHÉMAS GÉNÉRAUX}", r"\underline{\underline{SUR LES SCHÉMAS GÉNÉRAUX}}"),
    "Double underline, as the first title line.")
add(1, "first paragraph, line 1", "de nature introductif", "de nature introductif (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Agreement slip of the print (nature is feminine). The TeX keeps the printed reading; the corrected layer "
    "already reads 'introductive'.", corrected="de nature introductive")
add(1, "throughout (here: first paragraph and §1)", "Riemann-Roch, Borel-Serre, Euler-Poincaré (typewriter hyphen)",
    "Riemann--Roch, Borel--Serre, Euler--Poincaré", "punctuation", "medium", None,
    "Convention of the transcription, not a page fix: joint names are written with an en dash (--) where the "
    "typescript has a hyphen. On p. 1: Riemann--Roch (twice), Borel--Serre, Euler--Poincaré; the diplomatic "
    "main.tex has 68 Riemann--Roch. One pass in the diplomatic layer (as SGA 7 II global issue 74).")
add(1, "§1, display after 'morphisme propre'", "f: X.⟶Y (a typed full stop after X)", r"f:X\longrightarrow Y",
    "misprint_in_print", "medium", fx(r"f:X\longrightarrow Y", r"f:X.\longrightarrow Y"),
    "A typed full stop (same dot as the colon's) stands between X and the arrow in both scans; the TeX silently "
    "drops it.", corrected=r"f:X\longrightarrow Y")
add(1, "throughout (here: 'l'homomorphisme \"image directe de cycles\"')",
    "\"image directe de cycles\" (straight typewriter double quotes)", "«~image directe de cycles~»", "punctuation",
    "high", None,
    "Convention of the transcription, not covered by the known ``...''/\"...\" rule: the print's straight quotes "
    "are written as French guillemets «~...~» (192 « in the diplomatic main.tex). In this batch: «~image directe "
    "de cycles~» (pp. 1 and 5), «~régularité locale~» (p. 2), «~\\underline{filtration topologique}~» and «~moving "
    "lemma~» (p. 3), «~moving lemma~» (p. 4). One global replacement.")
add(1, "'polynômes universels à coéfficients dans Q'", "coéfficients", "coéfficients (printed reading kept)",
    "misprint_in_print", "high", None, "The print has the accent on the first e; the TeX keeps it.",
    corrected="coefficients")
add(1, "line before (1.2)", "plus commode pour notre propos (no comma, both scans)", "notre propos,", "punctuation",
    "high", fx("notre propos,", "notre propos"), "The TeX adds a comma before the display (1.2).")
add(1, "(1.2), left side", "ch_Y(f_*(cl(F)) = f_*(Todd(T_f).ch_X(F)) ,",
    r"\ch_Y\bigl(f_*(\cl(F))=f_*\bigl(...\bigr), (printed reading kept: \bigl( never closed)", "misprint_in_print",
    "high", None,
    "The left side opens three parentheses and closes two (both scans); the TeX keeps the unbalanced form.",
    corrected=r"\ch_Y\bigl(f_*(\cl(F))\bigr)=f_*\bigl(\Todd(T_f)\cdot\ch_X(F)\bigr)")

# ---------------- page 2 ----------------
add(2, "start of page", "p. 2 begins 'de sorte que T_f joue le rôle d'un fibré tangent relatif virtuel'",
    "'de' is the last line of page_001.tex (under the folio-1 marker); page_002.tex begins 'sorte que'", "marker",
    "high", None,
    "Page 2 really begins with 'de'. Move the folio-2 marker up one line, above 'de' (right after \\end{equation} "
    "of (1.3)): python -I move_marker.py 6 2 \"de\" --before (simulated on both layers: gives the marker, then "
    "'de', then 'sorte que').")
add(2, "a)", "Se débarasser de l'hypothèse", "débarasser (printed reading kept)", "misprint_in_print", "high", None,
    "Single r in both scans; the TeX keeps it.", corrected="débarrasser")

# ---------------- page 3 ----------------
add(3, "start of page", "p. 3 begins '2.1 Pour ce qui est de cette dernière'",
    "\\subsubsection*{2.1} is the last line of page_002.tex (under the folio-2 marker)", "marker", "high", None,
    "Page 3 really begins with the heading 2.1. Move the folio-3 marker above \\subsubsection*{2.1}: python -I "
    "move_marker.py 6 3 \"\\subsubsection*{2.1}\" --before (simulated on both layers).")
add(3, "§2.1, 'définissant le sous-schémas fermé X'", "le sous-schémas fermé X", "sous-schémas (printed reading kept)",
    "misprint_in_print", "high", None, "Plural s on 'sous-schéma' in the print; the TeX keeps it.",
    corrected="le sous-schéma fermé")
add(3, "heading 2.2", "2 2. (first full stop lost in both scans; the trailing full stop is printed, faint)",
    r"\subsubsection*{2.2}", "punctuation", "medium",
    fx(r"\subsubsection*{2.2}", r"\subsubsection*{2.2.}"),
    "The print closes this paragraph number with a full stop, as 2.3. and 2.4. (2.1 and 3.1 have none); the TeX "
    "has none.")
add(3, "§2.2, 'lisses et quasi-porjectifs'", "quasi-porjectifs", "quasi-porjectifs (printed reading kept)",
    "misprint_in_print", "high", None, "Transposed letters in the print; the TeX keeps them.",
    corrected="quasi-projectifs")
add(3, "§2.2, 'dont le produit tensoriel par Q'", "par Q est effectivement (plain typed Q, no overstrike, both scans)",
    r"par $\mathbb Q$ est effectivement", "font", "low",
    fx(r"par $\mathbb Q$ est effectivement", r"par $Q$ est effectivement"),
    "The other Q of pp. 1-5 are drawn or typed with an overstruck bar (p. 1 'dans Q', p. 5 'par Q'); this one is "
    "an ordinary typewriter Q. Same open question as the typist's plain Q of SGA 7 II (global issue 61): apply "
    "only if the diplomatic layer reproduces it.")
add(3, "§2.2, 'Une première filtration naturelle'",
    "'Une première filtration ...' continues the paragraph: no indent, after a full line (both scans)",
    "blank line (new paragraph) before 'Une première filtration'", "other", "low",
    fx("cet anneau.\n\nUne première", "cet anneau. Une première"),
    "The typescript indents its new paragraphs (p. 2 'La définition', p. 4 'Ceci montre'); this line starts at the "
    "margin, so the print runs on.")
add(3, "§2.2, 'dans le cas X lisse sur un coprs k'", "coprs", "coprs (printed reading kept)", "misprint_in_print",
    "high", None, "Transposed letters in the print; the TeX keeps them.", corrected="corps")
add(3, "throughout pp. 3-5 (here: 'que nous noterons ici Gr_top(X)')",
    "Gr˙_top(X), Gr˙(X): the degree mark is a typed full stop raised to superscript",
    r"\Gr^{\bullet}_{\mathrm{top}}(X), \Gr^\bullet(X)", "symbol", "low", None,
    "Convention for one decision, not a page fix: the TeX writes \\bullet for the print's raised dot: "
    "\\Gr^{\\bullet}_{\\mathrm{top}}(X) (p. 3), \\Gr^\\bullet(X) (p. 4), \\Gr^\\bullet(Y)_{\\mathbb Q} (p. 5). A "
    "diplomatic reading would be \\Gr^{\\cdot}; compare SGA 7 global issues 15 and 70.")
add(3, "display after 'homomorphisme d'anneaux surjectif'",
    "ϕ: A(X) ⟶ Gr_top(X) (hand-drawn closed phi: a loop crossed by a stroke)", r"\varphi:A(X)", "symbol", "medium",
    fx(r"\varphi:A(X)", r"\phi:A(X)"),
    "The drawn letter is the closed form that TeX sets as \\phi, not the open \\varphi (as treated in SGA 7 I pp. "
    "13-14).")

# ---------------- page 4 ----------------
add(4, "start of page", "p. 4 begins '(tranformant la classe d'un cycle premier Z'",
    "the opening '(' stands alone on the last line of page_003.tex (under the folio-3 marker)", "marker", "high", None,
    "Page 4 really begins with '('. Move the folio-4 marker above that line: python -I move_marker.py 6 4 \"(\" "
    "--before (simulated on both layers). The lone '(' line makes the output read '( tranformant': join it to the "
    "next line when moving.")
add(4, "first line, '(tranformant la classe'", "tranformant", "tranformant (printed reading kept)",
    "misprint_in_print", "high", None, "Missing s in the print; the TeX keeps it.", corrected="transformant")
add(4, "'formules qui même pour X projectif et lisse sur un corps'",
    "sur un corpa ne sont pas (last letter an a, heavily inked, both scans)", "sur un corps ne sont",
    "misprint_in_print", "medium", fx("un corps ne sont", "un corpa ne sont"),
    "The last letter has the a's right-hand stem and lower bowl (unlike the s of 'sont' beside it); the TeX "
    "silently corrects.", corrected="un corps ne sont")
add(4, "'(Exp. XIV, 4 3 et 4.4)'", "4 3 (no full stop visible in either scan; its character cell is there)",
    "XIV, 4 3 et", "punctuation", "low", fx("XIV, 4 3 et", "XIV, 4.3 et"),
    "Full stops of this typescript often vanish (p. 3: the TeX restores those of (Exp. VIII), (2.1), T_f.). If the "
    "stop was never typed, this is instead a misprint the TeX keeps, correct reading 4.3.")
add(4, "'le problème signalé plus haut'", "plus baut (b with a closed bowl, both scans)", "plus haut",
    "misprint_in_print", "high", fx("plus haut de la", "plus baut de la"),
    "The print has b for h; the TeX silently corrects.", corrected="plus haut de la")
add(4, "heading 2.3", "2.3. (trailing full stop)", r"\subsubsection*{2.3}", "punctuation", "high",
    fx(r"\subsubsection*{2.3}", r"\subsubsection*{2.3.}"), "The printed paragraph number ends with a full stop.")
add(4, "(2.3) and the following lines (throughout the volume)",
    "ε drawn in the open form (like a reversed 3)", r"\epsilon (lunate) five times on this page", "symbol", "low",
    None,
    "Glyph convention for one decision, not a page fix: the print's augmentation epsilon is the open form "
    "(\\varepsilon), the TeX writes the lunate \\epsilon: (2.3) \\gamma^i(x-\\epsilon(x)), '$\\epsilon$ étant "
    "l'augmentation', \\epsilon(x_1) ... \\epsilon(x_k); the diplomatic main.tex has 68 \\epsilon and 26 "
    "\\varepsilon. Compare SGA 7 global issues 9 and 24.")
add(4, "after (2.3), 'des λ^j (j=i) explicitée'", "(j=i) explicitée (no comma, both scans)",
    "($j=i$), explicitée", "punctuation", "high", fx("($j=i$), explicitée", "($j=i$) explicitée"),
    "The TeX adds a comma after the parenthesis.")
add(4, "after (2.3), 'combinaison linéaire des λ^j (j=i)'", "(j=i)", "($j=i$) (printed reading kept)",
    "misprint_in_print", "medium", None,
    "gamma^i is a combination of the lambda^j with j at most i (gamma^i(x) = lambda^i(x+i-1)); the typed = lacks "
    "the < of the inequality. The TeX keeps the printed reading; the corrected layer already reads $j\\leq i$.",
    corrected=r"($j\leq i$)")

# ---------------- page 5 ----------------
add(5, "start of page", "p. 5 begins 'est un isomorphisme modulo torsion'",
    "'est un' is the last line of page_004.tex (under the folio-4 marker)", "marker", "high", None,
    "Page 5 really begins with 'est un'. Move the folio-5 marker above that line: python -I move_marker.py 6 5 "
    "\"est un\" --before (simulated on both layers).")
add(5, "heading 2.4", "2.4. (trailing full stop)", r"\subsubsection*{2.4}", "punctuation", "high",
    fx(r"\subsubsection*{2.4}", r"\subsubsection*{2.4.}"), "The printed paragraph number ends with a full stop.")
add(5, "§2.4, 'que celles de ses deux concurents'", "concurents", "concurents (printed reading kept)",
    "misprint_in_print", "high", None, "Single r in the print; the TeX keeps it.", corrected="concurrents")
add(5, "§2.4, 'est un morphisme propre de schémas noethériens'",
    "propre (a thin stray stroke stands high above, between r and o, in both scans)", "morphisme própre", "accent",
    "medium", fx("morphisme própre", "morphisme propre"),
    "The stroke is long, thin and well above the x-height, unlike the typed acute accents of the same line "
    "(schémas, noethériens), which are short wedges touching the e: a stray mark, not an accent.")
add(5, "end of page", "p. 5 ends '... admettant des Modules inversibles amples.'; p. 6 begins '3. Montrons "
    "maintenant comment' (DjVu witness p. 17)",
    "page_005.tex ends with \\subsection*{3.}, which belongs to p. 6", "marker", "high", None,
    "Move the folio-6 marker above \\subsection*{3.}: python -I move_marker.py 6 6 \"\\subsection*{3.}\" --before "
    "(simulated on both layers).")

# ---------------- checks ----------------
bad = 0
for d in F:
    fix = d["fix"]
    if not fix:
        continue
    t = (RUN / "b001_005" / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    body = t.split("\n", 2)[2]  # drop '% from main.tex' and the marker line
    n = body.count(fix["old"])
    if n != 1 or "%%%%%%%%%%" in fix["old"] or "%%%%%%%%%%" in fix["new"]:
        bad += 1
        print("PROBLEM", d["page"], repr(fix["old"]), n)
out = RUN / "findings_001_005.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(1, 6):
    print(f"p. {p}: {c[(p, False)]}/{c[(p, True)]}")
print("findings", len(F), "fixes", sum(1 for d in F if d["fix"]), "problems", bad)
