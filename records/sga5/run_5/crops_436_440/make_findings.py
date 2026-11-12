import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
BATCH = os.path.join(RUN, "b436_440")
OUT = os.path.join(RUN, "findings_436_440.json")

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- p. 436 ----------------
add(436, "label of Lemme 6.4.5 (first line of the page)",
    "Lemma 6.4.5. (underlined; 'Lemma' with a final a)",
    r"\subsection*{Lemme 6.4.5}",
    "misprint_in_print", "high",
    {"old": r"Lemme 6.4.5", "new": r"Lemma 6.4.5"},
    "The typescript spells the label 'Lemma'; the TeX silently corrects it to 'Lemme'. The fix restores the printed word (diplomatic layer only).",
    corrected=r"Lemme 6.4.5")

add(436, "Lemme 6.4.5, last line of the statement",
    "sur l'espace vectorial m_{x'}/m^2_{x'} .",
    r"sur l'espace vectoriel $\fm_{x'}/\fm_{x'}^2$",
    "misprint_in_print", "high",
    {"old": r"vectoriel", "new": r"vectorial"},
    "Spelling slip of the print ('vectorial'); the TeX silently corrects it.",
    corrected=r"vectoriel")

add(436, "Démonstration, display 'g^{-1}T = ε(g^{-1})T mod m^2 ,'",
    "mod m^2 : a plain typed m, not underlined (every other m of the page, m_{x'}/m^2_{x'}, m/m^2 and 'où m est l'idéal maximal', is underlined)",
    r"\mod \fm^2",
    "misprint_in_print", "medium",
    {"old": r"\mod \fm^2", "new": r"\mod m^2"},
    "The maximal ideal of k[[T]] (the underlined m of the next line); the typist left out the underline in the display, and the TeX silently gives \\fm. Diplomatic layer only, as the missing underlines of H^i_c in SGA 7 II (global issue 79).",
    corrected=r"\mod \fm^2")

add(436, "Démonstration, before the second display",
    "Par conséquence",
    r"Par conséquent",
    "misprint_in_print", "high",
    {"old": r"Par conséquent", "new": r"Par conséquence"},
    "The print has 'Par conséquence' (for 'Par conséquent'); the TeX silently corrects it.",
    corrected=r"Par conséquent")

add(436, "Démonstration, display 'g^{-1}f'(T) = ε(g^{-1})T + b_ν T^ν + ...'",
    "g^{-1}f^1(T): after the f a raised digit 1 (flag and foot serif, the same glyph as the 1 of g^{-1}), not the typed apostrophe of f'(T) two lines above",
    r"g^{-1}f^{\prime}(T)",
    "misprint_in_print", "high",
    {"old": r"f^{\prime}(T)", "new": r"f^{1}(T)"},
    "The typist typed a superscript 1 for the prime; the TeX silently gives the prime. Diplomatic layer only.",
    corrected=r"f^{\prime}(T)")

add(436, "Démonstration, last line: 'et l'hypothèse ε(g^{-1}f') > 1 implique ...'",
    "ε(g^{-1}f^1) > 1 : the typed ε of ε(g^{-1}), no index",
    r"\varepsilon(g^{-1}f^{\prime}) > 1",
    "misprint_in_print", "high",
    None,
    "The hypothesis of the lemma is ν_{x'}(g^{-1}f') > 1 (second line of the statement); ε(g^{-1}f') is meaningless. The TeX keeps the printed ε; the corrected layer (current/s5.tex) reads \\nu(g^{-1}f^{\\prime}) > 1, without the index x'. The f^1 of the same expression is the next finding (diplomatic layer); the two edits touch different layers.",
    corrected=r"\nu_{x'}(g^{-1}f^{\prime}) > 1")

add(436, "Démonstration, last line: 'et l'hypothèse ε(g^{-1}f') > 1'",
    "ε(g^{-1}f^1) > 1 : a raised digit 1 after the f, as in the display above",
    r"\varepsilon(g^{-1}f^{\prime}) > 1",
    "misprint_in_print", "high",
    {"old": r"f^{\prime}) > 1", "new": r"f^{1}) > 1"},
    "Same typing slip as in the display (superscript 1 for the prime); the TeX silently gives the prime. Diplomatic layer only.",
    corrected=r"f^{\prime}) > 1")

# ---------------- p. 437 ----------------
add(437, "(6.4.7), first case of the brace",
    "O si il existe x' ∈ X' tel qu'on a ...",
    r"\text{si il existe }",
    "misprint_in_print", "low",
    None,
    "Elision slip of the typescript ('si il' for 's'il'; the exposé prints 's'il existe' in (3.1), p. 414). The TeX keeps the printed reading, as does the corrected layer; list it for the corrected edition only if such slips are corrected there (as the agreement slip of p. 381).",
    corrected=r"\text{s'il existe }")

# ---------------- p. 438 ----------------
add(438, "title of section 7",
    "7. Commentaires sur les conditions de validité de la formule de Lefschetz. (underlined, ends with a full stop)",
    r"\section*{7. Commentaires sur les conditions de validité de la formule de Lefschetz}",
    "punctuation", "high",
    {"old": r"formule de Lefschetz}", "new": r"formule de Lefschetz.}"},
    "The TeX drops the full stop that ends the underlined title.")

add(438, "heading 7.1",
    "7.1. Bien entendu, ... (full stop after 7.1)",
    r"\subsection*{7.1}",
    "punctuation", "high",
    {"old": r"\subsection*{7.1}", "new": r"\subsection*{7.1.}"},
    "As the '6.1.' of p. 393 and '1.1.' of p. 140.")

add(438, "the two conditions after 'tel que :'",
    "- F est un faisceau constructible ... / - l'ensemble X^f ... : the items are labelled with typewriter hyphens",
    r"\begin{itemize} (bullets)",
    "symbol", "high",
    {"old": r"\begin{itemize}", "new": r"\begin{itemize}[label=-]"},
    "The TeX's itemize prints bullets; enumitem is loaded and the file already uses [label=-] (s5.tex line 7101, as on p. 211).")

add(438, "paragraph 'En utilisant ...', line 5",
    "semble dificile,",
    r"semble difficile,",
    "misprint_in_print", "high",
    {"old": r"difficile", "new": r"dificile"},
    "Spelling slip of the print; the TeX silently corrects it.",
    corrected=r"difficile")

add(438, "paragraph 'En utilisant ...', last line",
    "d'ou l'intérêt (no grave accent on the u)",
    r"d'où l'intérêt",
    "misprint_in_print", "high",
    {"old": r"d'où", "new": r"d'ou"},
    "The accent of 'où' is missing in the print (checked on a crop; the typewriter's ù is printed in 'Où' on p. 439); the TeX silently corrects.",
    corrected=r"d'où")

add(438, "paragraph 'En revanche ...'",
    "des hypothèses suplémentaires",
    r"des hypothèses supplémentaires",
    "misprint_in_print", "high",
    {"old": r"supplémentaires", "new": r"suplémentaires"},
    "Spelling slip of the print; the TeX silently corrects it.",
    corrected=r"supplémentaires")

add(438, "paragraph 'En utilisant ...', line 2",
    "définir les termes τ_x(u,f) tel que la formule (*) soit vraie",
    r"tel que la formule (*) soit vraie",
    "misprint_in_print", "low",
    None,
    "Agreement slip ('les termes ... tel que'). The TeX keeps the printed reading, as does the corrected layer; list it for the corrected edition only if agreement slips are corrected there (as p. 381). Compare p. 440, where the TeX silently corrects 'tel que'.",
    corrected=r"tels que la formule (*) soit vraie")

# ---------------- p. 439 ----------------
add(439, "Proposition 7.2, first sentence",
    "Soient X un schéma lisse de dimension 1, F cons-tructible et : one continuous underline (also under X, 1 and F)",
    r"Soient $X$ un schéma lisse de dimension $1$, $F$ constructible et (no underline markup)",
    "underline", "high",
    {"old": r"Soient $X$ un schéma lisse de dimension $1$, $F$ constructible et",
     "new": r"\emph{Soient $X$ un schéma lisse de dimension $1$, $F$ constructible et}"},
    "The print underlines the statement; the statement environment sets an upright body. \\emph is this exposé's markup for underlined statements (Lemme 6.4.5, p. 436; p. 416).")

add(439, "Proposition 7.2, line after the first display",
    "un endomorphisme tel que le morphisme de faisceaux (underlined)",
    r"un endomorphisme tel que le morphisme de faisceaux",
    "underline", "high",
    {"old": r"un endomorphisme tel que le morphisme de faisceaux",
     "new": r"\emph{un endomorphisme tel que le morphisme de faisceaux}"},
    "As the first sentence of the statement.")

add(439, "Proposition 7.2, line after the second display",
    "soit un isomorphisme. (underlined)",
    r"soit un isomorphisme.",
    "underline", "high",
    {"old": r"soit un isomorphisme.", "new": r"\emph{soit un isomorphisme}."},
    "As the first sentence; the full stop is kept outside the group, as the volume's punctuation-out-of-underline rule.")

add(439, "Proposition 7.2, before 'Sous ces conditions'",
    "'soit un isomorphisme.' ends a short line; 'Sous ces conditions il existe' starts a new line at the margin after extra space (1.5 line pitches, as before 'Si f est constant' below, where the TeX has a paragraph break)",
    r"soit un isomorphisme. Sous ces conditions (one paragraph)",
    "other", "medium",
    {"old": " Sous ces", "new": "\n\nSous ces"},
    "Paragraph break inside the statement. Apply this edit before the next one (the underline of 'Sous ces conditions ...'), whose old begins at 'Sous': both olds share 'Sous ces'.")

add(439, "Proposition 7.2, last sentence",
    "Sous ces conditions il existe (underlined)  U,U',G,f',φ (not underlined)  satisfaisant aux conditions de 5.1, 6.1, 6.2. (underlined, numbers included)",
    r"Sous ces conditions il existe $U,U',G,f',\varphi$ satisfaisant aux conditions de 5.1, 6.1, 6.2.",
    "underline", "high",
    {"old": r"Sous ces conditions il existe $U,U',G,f',\varphi$ satisfaisant aux conditions de 5.1, 6.1, 6.2.",
     "new": r"\emph{Sous ces conditions il existe} $U,U',G,f',\varphi$ \emph{satisfaisant aux conditions de 5.1, 6.1, 6.2}."},
    "Apply after the paragraph-break edit above (its old ' Sous ces' overlaps this old); after it this old is still unchanged.")

add(439, "Démonstration, 'En effet supposons par l'absurde'",
    "En effet supposons par l'absurde (no comma; 'par' typed into a narrow space, a typist's insertion)",
    r"En effet, supposons",
    "punctuation", "high",
    {"old": r"En effet, supposons", "new": r"En effet supposons"},
    "The TeX adds a comma.")

add(439, "Démonstration, 'au voisinage de y et en utilisant l'isomorphisme u il résulte'",
    "de y et en utilisant l'isomorphisme u il résulte que F (no commas)",
    r"et, en utilisant l'isomorphisme $u$, il",
    "punctuation", "high",
    {"old": r"et, en utilisant l'isomorphisme $u$, il", "new": r"et en utilisant l'isomorphisme $u$ il"},
    "The TeX adds two commas.")

add(439, "Démonstration, 'au voisinage de y ce qui est absurde'",
    "au voisinage de y ce qui est absurde. (no comma)",
    r"de $y$, ce qui",
    "punctuation", "high",
    {"old": r"de $y$, ce qui", "new": r"de $y$ ce qui"},
    "The TeX adds a comma.")

add(439, "Démonstration, 'Si f est constant la démonstration'",
    "Si f est constant la démonstration (no comma)",
    r"est constant, la",
    "punctuation", "high",
    {"old": r"est constant, la", "new": r"est constant la"},
    "The TeX adds a comma.")

add(439, "Démonstration, 'Où va donc supposer'",
    "Où va donc supposer (O, u with a grave accent; checked at 4x)",
    r"Où va donc supposer",
    "misprint_in_print", "high",
    None,
    "'Où' for 'On'. The TeX keeps the printed reading; the corrected layer (current/s5.tex) already reads 'On va donc'.",
    corrected=r"On va donc supposer")

add(439, "Démonstration, 'que f n'est pas constant'",
    "n'est pas constant (underlined)",
    r"n'est pas constant",
    "underline", "high",
    {"old": r"n'est pas constant", "new": r"\emph{n'est pas constant}"},
    "Emphasis by underlining; \\emph as in the rest of the exposé.")

add(439, "Démonstration, 'de X on aura donc f(η) = η'",
    "point générique de X on aura donc (no comma)",
    r"de $X$, on aura",
    "punctuation", "high",
    {"old": r"de $X$, on aura", "new": r"de $X$ on aura"},
    "The TeX adds a comma.")

# ---------------- p. 440 ----------------
add(440, "first paragraph, 'le morphisme (en fait l'isomorphisme) de faisceaux'",
    "le morphisme (en fait l'isomorphisme) de faisceaux (parentheses)",
    r"le morphisme, en fait l'isomorphisme, de faisceaux",
    "punctuation", "high",
    {"old": r"le morphisme, en fait l'isomorphisme, de faisceaux",
     "new": r"le morphisme (en fait l'isomorphisme) de faisceaux"},
    "The TeX has commas for the print's parentheses. (u_η : f_η^*(F_η) → F_η runs in the text in the print; the TeX's display is layout, not reported.)")

add(440, "the two isomorphisms H → H, F_η̄ → F_η̄",
    "F_η̄ --u_η̄--> F_η̄ with nothing after the target",
    r"& F_{\bar\eta},",
    "punctuation", "high",
    {"old": r"& F_{\bar\eta},", "new": r"& F_{\bar\eta}"},
    "The TeX adds a comma at the end of the second arrow. (The print stacks the two arrows; side by side in the TeX is layout.)")

add(440, "paragraph 'Soit K ⊃ k(η) ...'",
    "correspondante au sous-groupe H_1 et X' la normalisée (no comma)",
    r"$H_1$, et $X'$",
    "punctuation", "high",
    {"old": r"$H_1$, et $X'$", "new": r"$H_1$ et $X'$"},
    "The TeX adds a comma.")

add(440, "paragraph 'Soit K ⊃ k(η) ...', line 3",
    "Evidement on peut définir (one m)",
    r"Évidemment",
    "misprint_in_print", "high",
    {"old": r"Évidemment", "new": r"Évidement"},
    "Spelling slip of the print (one m missing); the TeX silently corrects it. The fix keeps the TeX's accented capital (global rule for 'Evidemment').",
    corrected=r"Évidemment")

add(440, "last line of the page",
    "tel que le système U,U',f',G,φ (singular 'tel')",
    r"tels que le système",
    "misprint_in_print", "medium",
    {"old": r"tels que le système", "new": r"tel que le système"},
    "Agreement slip: the condition bears on both endomorphisms f' and φ. The TeX silently corrects it ('tels'); the fix restores the printed reading (diplomatic layer only). Independent of the next finding.",
    corrected=r"tels que le système")

add(440, "last line of the page",
    "U,U',f',G,φ satisfassent aux conditions voulues. (plural verb)",
    r"satisfasse aux conditions voulues.",
    "misprint_in_print", "medium",
    {"old": r"satisfasse aux", "new": r"satisfassent aux"},
    "Agreement slip (the subject is 'le système'); the TeX silently corrects it. Diplomatic layer only.",
    corrected=r"satisfasse aux")

# ---------------- checks ----------------
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    path = os.path.join(BATCH, "page_%03d.tex" % d["page"])
    txt = open(path, encoding="utf-8", newline="").read()
    n = txt.count(fx["old"])
    marker_lines = [l for l in fx["old"].split("\n") if "%%%%%%%%%%" in l]
    if n != 1 or marker_lines:
        ok = False
        print("BAD", d["page"], repr(fx["old"]), n)
    if "\r" in txt:
        print("CR in", path)

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(436, 441):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(F), "all olds unique:", ok)
