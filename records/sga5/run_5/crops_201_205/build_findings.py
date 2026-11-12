"""Build findings_201_205.json and check that every fix's old occurs exactly once in its page_NNN.tex."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b201_205"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_201_205.json"
N = "\n"
F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 201 ----------------
add(201, "label of Lemme 6.23.3",
    "'Lemme 6.23.3 - (cf. ...': the label is followed by ' -' ('Lemme' underlined)",
    r"\begin{statement}{Lemme 6.23.3}", "punctuation", "high",
    r"\begin{statement}{Lemme 6.23.3}", r"\begin{statement}{Lemme 6.23.3 -}",
    "Exposé III B keeps Exposé III's run-in labels with ' -' (the environment adds no stop there).")
add(201, "Lemme 6.23.3, the reference before 'Soient'",
    "'(cf. (SGA 4^{1/2} Rapport 4.7).': two opening parentheses, one closing (clear at 2x)",
    r"(cf. SGA $4^{1/2}$ Rapport 4.7).", "misprint_in_print", "high",
    r"(cf. SGA", r"(cf. (SGA",
    "The parentheses of the print do not balance; the TeX silently corrects. The fix restores the printed reading "
    "(diplomatic layer only).", corrected=r"(cf. SGA")
add(201, "Lemme 6.23.3, statement before the diagram (*)",
    "underlined: 'Soient', 'un', '-module localement / facteur direct d'un module libre de type fini', 'et', "
    "'un complexe de', '-modules, parfait sur', 'Alors', 'considéré comme objet de', 'par l'action diagonale de', "
    "'est parfait sur', 'et l'on a un carré commu-/tatif'; the math letters, the reference and the commas between "
    "are not underlined",
    "no underline markup", "underline", "high",
    r"Soient $P$ un $G_V$-module localement facteur direct d'un module libre de type fini, $P'=i_!P$, et $Q$ un "
    r"complexe de $\Lambda[G]$-modules, parfait sur $\Lambda$. Alors $P\lten_{\Lambda}Q$, considéré comme objet "
    r"de $D({}_{\Lambda[G]}V)$ par l'action diagonale de $G$, est parfait sur $\Lambda[G]$, et l'on a un carré "
    r"commutatif",
    r"\emph{Soient} $P$ \emph{un} $G_V$-\emph{module localement facteur direct d'un module libre de type fini}, "
    r"$P'=i_!P$, \emph{et} $Q$ \emph{un complexe de} $\Lambda[G]$-\emph{modules, parfait sur} $\Lambda$. "
    r"\emph{Alors} $P\lten_{\Lambda}Q$, \emph{considéré comme objet de} $D({}_{\Lambda[G]}V)$ \emph{par l'action "
    r"diagonale de} $G$, \emph{est parfait sur} $\Lambda[G]$, \emph{et l'on a un carré commutatif}",
    "Exposé III B statement underline, \\emph as in the logged III B fixes (pp. 142-175). The misprint fix "
    "'(cf. (SGA' does not overlap this edit.")
add(201, "diagram (*), top row, the tensor sign between the two RHom",
    "'... p_2^!P') ⊗^L RHom_Λ[G](Q,Q)': L above the sign, no subscript Λ (clear at 2x; the Λ under ⊗ in "
    "the statement and the proof is crisp)",
    r"p_2^!P')\lten_{\Lambda}", "formula", "high",
    r"p_2^!P')\lten_{\Lambda}", r"p_2^!P')\lten",
    "The TeX adds the subscript.")
add(201, "diagram (*), top row, second RHom",
    "'⊗ RHom_Λ[G](Q,Q)': RHom typed without any underline (the first RHom of the row has Hom underlined)",
    r"\uRHom_{\Lambda[G]}(Q,Q) \arrow[r", "underline", "high",
    r"\uRHom_{\Lambda[G]}(Q,Q) \arrow[r", r"\mathrm{R}\mathrm{Hom}_{\Lambda[G]}(Q,Q) \arrow[r",
    "\\mathrm{R}\\mathrm{Hom} is the file's form for a plain RHom in Exposé III. The same RHom in the display "
    "after 'et' below and in the bottom row has Hom underlined, as in the TeX.")
add(201, "diagram (*), bottom row",
    "'δ*RHom_Λ[G](p_1^*P' ⊗^L Q, p_2^!P' ⊗^L Q)': both tensor signs with L above and no subscript Λ",
    r"(p_1^*P'\lten_{\Lambda}Q,p_2^!P'\lten_{\Lambda}Q)", "formula", "high",
    r"(p_1^*P'\lten_{\Lambda}Q,p_2^!P'\lten_{\Lambda}Q)", r"(p_1^*P'\lten Q,p_2^!P'\lten Q)",
    "The TeX adds both subscripts.")
add(201, "Lemme 6.23.3, 'où δ : Y → Y ×_S Y est la diagonale, (1) est produit tensoriel des flèches'",
    "underlined: 'où', 'est la diagonale', 'est produit tensoriel des flèches'; not the formula, the comma, '(1)'",
    "no underline markup", "underline", "high",
    r"où $\delta:Y\to Y\times_SY$ est la diagonale, (1) est produit tensoriel des flèches",
    r"\emph{où} $\delta:Y\to Y\times_SY$ \emph{est la diagonale}, (1) \emph{est produit tensoriel des flèches}",
    "Exposé III B statement underline.")
add(201, "Lemme 6.23.3, the 'et' between the two displays",
    "'et' underlined", "no underline markup", "underline", "high",
    r"\]" + N + "et" + N + r"\[", r"\]" + N + r"\emph{et}" + N + r"\[",
    "Exposé III B statement underline.")
add(201, "Lemme 6.23.3, '(2) est la flèche déduite ... selon la diagonale'",
    "'est la flèche déduite du produit tensoriel externe par restriction selon la / diagonale' underlined; '(2)' not",
    "no underline markup", "underline", "high",
    r"(2) est la flèche déduite du produit tensoriel externe par restriction selon la diagonale",
    r"(2) \emph{est la flèche déduite du produit tensoriel externe par restriction selon la diagonale}",
    "Exposé III B statement underline.")
add(201, "Lemme 6.23.3, ', et (3) est composé de 6.5.3 (définie car'",
    "underlined: 'et', 'est composé de', 'définie car'; not '(3)', '6.5.3', the parenthesis, nor 'et de' further on",
    "no underline markup", "underline", "high",
    r"et (3) est composé de 6.5.3 (définie car", r"\emph{et} (3) \emph{est composé de} 6.5.3 (\emph{définie car}",
    "Exposé III B statement underline; the subscript fix of the same line (next finding) does not overlap.")
add(201, "Lemme 6.23.3, '(définie car P' ⊗^L Q ∈ ob D_ctf(Λ[G]Y))'",
    "P' ⊗^L Q: L above the sign, no subscript Λ",
    r"P'\lten_{\Lambda}Q\in", "formula", "high",
    r"P'\lten_{\Lambda}Q\in", r"P'\lten Q\in",
    "The TeX adds the subscript.")
add(201, "proof, display after 'on a', first sign",
    "δ*RHom(...) ≃ D_Λ[G](i_!P) ⊗^L i_!P: a tilde over a plain typed bar, no arrowhead (zoomed 5x: the bar ends "
    "flat)",
    r"\xrightarrow{\sim} (after p_2^!P')", "symbol", "high",
    "p_2^!P')" + N + r"\xrightarrow{\sim}", "p_2^!P')" + N + r"\simeq",
    "As the logged findings of pp. 10 and 17-20 (bar without head written \\simeq).")
add(201, "proof, display after 'on a', second sign",
    "... ⊗^L i_!P ≃ i_!(D_Λ[G]P ⊗^L P): a tilde over a plain typed bar, no arrowhead",
    r"\xrightarrow{\sim} (after i_!P)", "symbol", "high",
    r"i_!P" + N + r"\xrightarrow{\sim}", r"i_!P" + N + r"\simeq",
    "")
add(201, "diagram (**), top row, second RHom (printed at the top of p. 202; in page_201.tex as the files stand)",
    "'RHom_Λ[G](P, K_Y ⊗^L P) ⊗^L RHom_Λ[G](Q,Q)': the second RHom without any underline (the first and the "
    "bottom-row RHom have Hom underlined)",
    r"\lten\uRHom_{\Lambda[G]}(Q,Q)", "underline", "high",
    r"\lten\uRHom_{\Lambda[G]}(Q,Q)", r"\lten\mathrm{R}\mathrm{Hom}_{\Lambda[G]}(Q,Q)",
    "Filed under p. 201 because its TeX stands there until the folio-202 marker move; the old is unique in s5.tex.")

# ---------------- page 202 ----------------
add(202, "top of the page: diagram (**)",
    "p. 202 begins with the whole diagram (**); p. 201 ends with 'Le carré (*) s'écrit alors' and the footnote",
    "'\\begin{equation}', '\\tag{**}', the tikzcd's first row and '& K_Y \\arrow[d,' (s5.tex lines 6813-6818 in "
    "the diplomatic layer) end page_201.tex; the folio-202 marker (line 6819) stands inside the tikzcd, before "
    "'equal]\\\\'",
    "marker", "high", None, None,
    "Page 202 really begins at s5.tex line 6813 '\\begin{equation}' (the diagram (**)). Exact fix: python -I "
    "move_marker.py 5 202 '\\begin{equation}' --before (simulated in memory on both layers: the marker then "
    "stands after 'Le carré (*) s'écrit alors', just before '\\begin{equation}' and '\\tag{**}'). Text not moved.")
add(202, "'(1) est donné par Tr_Λ[G](-)(e) ⊗ Tr_Λ (traces au sens du n° 5)'",
    "the formula runs into the text; no comma after Tr_Λ (clean paper before the line break)",
    r"\Tr_{\Lambda[G]}(-)(e)\otimes\Tr_{\Lambda}, (end of the display)", "punctuation", "high",
    r"\otimes\Tr_{\Lambda},", r"\otimes\Tr_{\Lambda}",
    "The TeX adds punctuation at the end of the display.")
add(202, "paragraph number 6.24",
    "'6.24.' with a full stop", r"\subsection*{6.24}", "punctuation", "high",
    r"\subsection*{6.24}", r"\subsection*{6.24.}",
    "As the logged fixes '\\subsection*{6.2.}' etc. of pp. 183-185.")
add(202, "6.24, 'est l'identité (mais, ... n'est pas sérieuse). Si Y est'",
    "'l'identité (mais, comme on l'a déjà observé, cette restriction n'est pas sérieuse). Si'",
    r"l'identité; mais, comme on l'a déjà observé, cette restriction n'est pas sérieuse. Si", "punctuation", "high",
    r"l'identité; mais, comme on l'a déjà observé, cette restriction n'est pas sérieuse.",
    r"l'identité (mais, comme on l'a déjà observé, cette restriction n'est pas sérieuse).",
    "The TeX replaces the printed parenthesis by a semicolon.")
add(202, "heading of the bibliography (printed at the top of p. 203; in page_202.tex as the files stand)",
    "'BIBLIOGRAPHIE.': capitals, underlined, then a full stop", r"\section*{Bibliographie}", "word", "high",
    r"\section*{Bibliographie}", r"\section*{BIBLIOGRAPHIE.}",
    "Capitals and full stop as printed (as the logged BIBLIOGRAPHIE. fix of p. 135/136); the underline is the "
    "accepted \\section* setting. Filed under p. 202: the anchor of the folio-203 marker move ('\\section*{B') "
    "matches either spelling.")

# ---------------- page 203 ----------------
add(203, "top of the page: the heading BIBLIOGRAPHIE. and the start of the list",
    "p. 203 begins with 'BIBLIOGRAPHIE.' and '[1] Cartan, H. et Eilenberg, S.'; p. 202 ends '... et la partie I "
    "du présent exposé).'",
    "'\\section*{Bibliographie}' and '\\begin{enumerate}[' (s5.tex lines 6840-6842, diplomatic) end page_202.tex; "
    "the folio-203 marker (line 6843) splits the enumerate option before 'label={[\\arabic*]}]'",
    "marker", "high", None, None,
    "Page 203 really begins at s5.tex line 6840 '\\section*{Bibliographie}'. Exact fix: python -I move_marker.py "
    "5 203 '\\section*{B' --before (simulated in memory on both layers; run it once only: an earlier "
    "'\\section*{B' would catch a second run). Text not moved.")
for num, who in [("[1] Cartan-Eilenberg", r"Eilenberg, S. --"), ("[2] Grothendieck", r"Grothendieck, A. --"),
                 ("[3] Illusie", r"Illusie, L. --"), ("[6] Verdier", r"Verdier, J.-L. --")]:
    add(203, num + ", between author and title",
        "' - ' (typewriter hyphen between spaces)", who, "punctuation", "high",
        who, who[:-1], "The TeX writes an en dash.")
add(203, "[4] Langlands, between author and title",
    "'Langlands, R.P.- Modular': the hyphen right after 'R.P.' (no space before it, none between the initials)",
    r"Langlands, R. P. --", "punctuation", "high",
    r"Langlands, R. P. --", r"Langlands, R.P.-",
    "The TeX writes an en dash; the edit also closes up 'R. P.' as printed.")
add(203, "[5] Stallings, between author and title",
    "' - ' (typewriter hyphen)", r"Stallings, J. --", "punctuation", "high",
    r"Stallings, J. --", r"Stallings, J. -", "The TeX writes an en dash.")
add(203, "[5] Stallings, title 'Centerless groups - an algebraic formulation'",
    "' - ' (typewriter hyphen)", r"Centerless groups --", "punctuation", "high",
    r"Centerless groups --", r"Centerless groups -", "The TeX writes an en dash.")
add(203, "[5] Stallings, 'p. 129-134'",
    "p. 129-134 (typewriter hyphen)", r"129--134", "punctuation", "high",
    r"129--134", r"129-134", "As the logged page ranges of p. 136.")
for title in ["Homological Algebra", "Dix exposés sur la cohomologie des schémas",
              "Modular Functions of One Variable II", "Proceedings of a conference on local fields",
              "Cohomologie étale"]:
    add(203, "title '" + title + "'",
        "typed plain (no italic, no underline)", r"\textit{" + title + "}", "font", "high",
        r"\textit{" + title + "}", title, "The TeX adds italics the typescript does not have.")
add(203, "[5] Stallings, 'Topology, 4, p. 129-134'",
    "'Topology, 4,': plain, with a comma after Topology", r"\textit{Topology} 4,", "punctuation", "high",
    r"\textit{Topology} 4,", r"Topology, 4,",
    "The TeX drops the comma and adds italics (one edit: the two changes touch).")
add(203, "SGA 4^{1/2} entry, 'Springer-Verlag 1977.'",
    "no comma between Springer-Verlag and 1977", r"Springer-Verlag, 1977.", "punctuation", "high",
    r"Springer-Verlag, 1977.", r"Springer-Verlag 1977.", "The TeX adds a comma.")
add(203, "'(Dans SGA 4^{1/2} : Th. Finitude : ...'",
    "the three lines are in parentheses: '(Dans SGA 4^{1/2} : ...' ... 'formule des traces).'",
    r"Dans SGA $4^{1/2}$:", "punctuation", "high",
    r"Dans SGA $4^{1/2}$:", r"(Dans SGA $4^{1/2}$:",
    "Apply together with the closing parenthesis after 'traces' (below).")
add(203, "'Théorèmes de finitude en cohomologie ℓ-adique.'",
    "full stop after 'ℓ-adique'", r"\ell\text{-adique;}", "punctuation", "high",
    r"-adique;}", r"-adique.}", "The TeX has a semicolon.")
add(203, "'Cycle : La classe de cohomologie associée à un cycle.'",
    "full stop after 'cycle'", r"\text{Cycle: La classe de cohomologie associée à un cycle;}", "punctuation", "high",
    r"un cycle;}", r"un cycle.}", "The TeX has a semicolon.")
add(203, "'Rapport : Rapport sur la formule des traces).'",
    "closing parenthesis before the full stop", r"\text{Rapport: Rapport sur la formule des traces.}",
    "punctuation", "high",
    r"des traces.}", r"des traces).}",
    "Closes the parenthesis opened before 'Dans'; apply together with that edit.")

# ---------------- page 204 ----------------
add(204, "exposé heading, first line",
    "'E X P O S E  V' (capitals, letter-spaced, dashed underline) on a line of its own; no full stop (the speck "
    "to the right of V is a tiny mark at mid-height, not a typed stop)",
    r"\section*{Exposé V. Systèmes projectifs $J$-adiques}", "word", "medium",
    r"{Exposé V. ", r"{EXPOSÉ V\\",
    "Capitals as printed (the typescript's capital E has no accent: the accented capital stands); the title on "
    "a line of its own as in '\\section*{Exposé III B\\\\CALCULS DE TERMES LOCAUX}'. Medium only for the full stop.")
add(204, "exposé heading, title",
    "'SYSTEMES PROJECTIFS J- ADIQUES' in capitals, underlined, centred",
    r"Systèmes projectifs $J$-adiques", "word", "high",
    r"Systèmes projectifs $J$-adiques}", r"SYSTÈMES PROJECTIFS $J$-ADIQUES}",
    "Capitals as printed, as the titles of Exposés I, III and III B; accented capital as the volume's rule.")
add(204, "author line",
    "'par' / 'J.P. JOUANOLOU': no hyphen between the initials, surname in capitals",
    r"par J.-P. Jouanolou", "word", "high",
    r"par J.-P. Jouanolou", r"par J.P. JOUANOLOU",
    "As 'A.~GROTHENDIECK' on p. 1. The TeX adds the hyphen.")
add(204, "section heading 1",
    "'1. Généralités sur les A-catégories abéliennes.' with a full stop (words underlined)",
    r"\subsection*{1. Généralités sur les $A$-catégories abéliennes}", "punctuation", "high",
    r"$A$-catégories abéliennes}", r"$A$-catégories abéliennes.}",
    "Underlined title: the print's full stop.")
add(204, "label of Définition 1.1",
    "'DEFINITION 1.1. - On appelle': capitals, not underlined, then '. -'",
    r"\begin{statement}{Définition 1.1} (the Exposé V environment prints 'Définition 1.1.')", "word", "high",
    r"{Définition 1.1}" + N, r"{DÉFINITION 1.1}" + N + "- ",
    "With the environment as restored at p. 204 (it adds the stop) this prints 'DÉFINITION 1.1. - On appelle'. "
    "Exposé V's labels differ from the volume's 'Définition 1.1. :' form: see the coordinator message.")
add(204, "Définition 1.1, first sentence up to 'd'anneaux'",
    "underlined: 'On appelle', 'catégorie (resp.', 'catégorie abélienne)', 'un couple', 'formé d'une catégorie "
    "additive (resp. abélienne)', 'et / d'un homomorphisme d'anneaux'; not A-, (C,ρ), C, nor the colon",
    "no underline markup", "underline", "high",
    r"On appelle $A$-catégorie (resp. $A$-catégorie abélienne) un couple $(\cC,\rho)$ formé d'une catégorie "
    r"additive (resp. abélienne) $\cC$ et d'un homomorphisme d'anneaux",
    r"\emph{On appelle} $A$-\emph{catégorie (resp.} $A$-\emph{catégorie abélienne)} \emph{un couple} "
    r"$(\cC,\rho)$ \emph{formé d'une catégorie additive (resp. abélienne)} $\cC$ \emph{et d'un homomorphisme "
    r"d'anneaux}",
    "The TeX of Exposé V has no underline markup; \\emph as in III B. Does not overlap the label edit before it "
    "or the colon edit after it.")
add(204, "Définition 1.1, 'd'un homomorphisme d'anneaux :'",
    "a colon before the display", "no colon", "punctuation", "high",
    N + r"\[" + N + r"\rho:A\longrightarrow", ":" + N + r"\[" + N + r"\rho:A\longrightarrow",
    "The colon follows the underlined words directly.")
add(204, "Définition 1.1, 'de A dans l'anneau des endomorphismes ... de C dans C .'",
    "underlined: 'de', 'dans l'anneau des endomorphismes du foncteur identique de', 'dans'; not A, C, the stop",
    "no underline markup", "underline", "high",
    r"de $A$ dans l'anneau des endomorphismes du foncteur identique de $\cC$ dans $\cC$.",
    r"\emph{de} $A$ \emph{dans l'anneau des endomorphismes du foncteur identique de} $\cC$ \emph{dans} $\cC$.",
    "")
add(204, "'(resp. de A-catégories abéliennes de (C,ρ) dans (C',ρ')'",
    "no closing parenthesis after 'abéliennes': '(resp. de A - / catégories abéliennes de (C,ρ) dans (C',ρ') un "
    "foncteur' (clean paper after 'abéliennes')",
    r"(resp. de $A$-catégories abéliennes) de $(\cC,\rho)$", "misprint_in_print", "high",
    r"abéliennes) de $(\cC,\rho)$", r"abéliennes de $(\cC,\rho)$",
    "The '(resp.' is never closed in the print; the TeX silently corrects. The fix restores the printed reading "
    "(diplomatic layer only).", corrected=r"abéliennes) de $(\cC,\rho)$")
add(204, "'tel que pour tout objet M de C et tout élément a de A l'égalité ci-dessous soit vérifiée :'",
    "no comma after 'que' nor after 'de A'", r"tel que, pour tout objet ... de $A$, l'égalité", "punctuation", "high",
    r"tel que, pour tout objet $M$ de $\cC$ et tout élément $a$ de $A$, l'égalité",
    r"tel que pour tout objet $M$ de $\cC$ et tout élément $a$ de $A$ l'égalité",
    "The TeX adds two commas.")
add(204, "Exemple 1.1.1, 'des (A,C)-modules (à gauche) et qu'on note'",
    "'(à gauche)' in parentheses, no comma before 'et'", r"$(A,\cC)$-modules à gauche, et", "punctuation", "high",
    r"-modules à gauche, et", r"-modules (à gauche) et", "")
add(204, "Exemple 1.1.1, '(A,C)-mod la catégorie décrite comme suit :'",
    "no comma after 'mod'", r"$(A,\cC)$-mod, la catégorie", "punctuation", "high",
    r"-mod, la catégorie", r"-mod la catégorie", "The TeX adds a comma.")

# ---------------- page 205 ----------------
add(205, "top of the page: '(i) Ses objets sont les couples'",
    "p. 205 begins with '(i) Ses objets sont les couples (X,α)'; p. 204 ends 'la catégorie décrite comme suit :'",
    "'\\begin{enumerate}[label=(\\roman*)]' and '\\item Ses' (s5.tex lines 6895-6896, diplomatic) end "
    "page_204.tex; the folio-205 marker (line 6897) stands between 'Ses' and 'objets'",
    "marker", "high", None, None,
    "Page 205 really begins at s5.tex line 6895 '\\begin{enumerate}[label=(\\roman*)]'. Exact fix: python -I "
    "move_marker.py 5 205 '\\begin{enumerate}[label=(\\roman*)]' --before (simulated in memory on both layers). "
    "Text not moved; it agrees with the print.")
add(205, "(ii), 'tel que pour tout élément a de A la diagramme'",
    "no comma after 'que' nor after 'de A'", r"tel que, pour tout élément $a$ de $A$, le diagramme",
    "punctuation", "high",
    r"tel que, pour tout élément $a$ de $A$,", r"tel que pour tout élément $a$ de $A$",
    "The TeX adds two commas. Listed before the misprint fix of the next word, which it does not overlap.")
add(205, "(ii), 'la diagramme ci-dessous soit commutatif'",
    "'la diagramme' (clear: l-a)", r"le diagramme ci-dessous", "misprint_in_print", "high",
    r"le diagramme ci-dessous", r"la diagramme ci-dessous",
    "Wrong article ('diagramme' is masculine); the TeX silently corrects. The fix restores the printed reading "
    "(diplomatic layer only).", corrected=r"le diagramme ci-dessous")
add(205, "(ii), the square, bottom row",
    "'X ——> Y' with nothing after Y (clean paper)", r"X \arrow[r] & Y .", "punctuation", "high",
    r"X \arrow[r] & Y .", r"X \arrow[r] & Y",
    "The TeX adds a full stop at the end of the display.")
add(205, "property (a)",
    "underlined: 'Le foncteur', 'mod', 'obtenu en oubliant la structure de', 'module commute aux limites "
    "inductives et projectives'; not (A,C)-, → C, A-, the stop",
    "no underline markup", "underline", "high",
    r"Le foncteur $(A,\cC)$-mod $\to\cC$ obtenu en oubliant la structure de $A$-module commute aux limites "
    r"inductives et projectives.",
    r"\emph{Le foncteur} $(A,\cC)$-\emph{mod} $\to\cC$ \emph{obtenu en oubliant la structure de} "
    r"$A$-\emph{module commute aux limites inductives et projectives}.",
    "Exposé V: no underline markup in the TeX; \\emph as in III B.")
add(205, "property (b)",
    "underlined: 'Soit', 'une catégorie', 'Pour que les', 'limites inductives', '(resp. / projectives)', 'de', "
    "'mod soient représentables, il suffit qu'il en soit / ainsi pour les', 'limites inductives (resp. "
    "projectives) de'; not I, I-, (A,C)-, C, the stops",
    "no underline markup", "underline", "high",
    r"Soit $I$ une catégorie. Pour que les $I$-limites inductives (resp. projectives) de $(A,\cC)$-mod soient "
    r"représentables, il suffit qu'il en soit ainsi pour les $I$-limites inductives (resp. projectives) de $\cC$.",
    r"\emph{Soit} $I$ \emph{une catégorie}. \emph{Pour que les} $I$-\emph{limites inductives} \emph{(resp. "
    r"projectives)} \emph{de} $(A,\cC)$-\emph{mod soient représentables, il suffit qu'il en soit ainsi pour les} "
    r"$I$-\emph{limites inductives (resp. projectives) de} $\cC$.",
    "")
add(205, "heading 1.2",
    "'1.2. Produit tensoriel externe.' with a full stop (title underlined)",
    r"\subsubsection*{1.2. Produit tensoriel externe}", "punctuation", "high",
    r"\subsubsection*{1.2. Produit tensoriel externe}", r"\subsubsection*{1.2. Produit tensoriel externe.}",
    "Underlined title: the print's full stop.")
add(205, "1.2, 'on appelle produit tensoriel externe de X par M'",
    "underlined: 'produit / tensoriel externe de', 'par'; not X, M", "no underline markup", "underline", "high",
    r"on appelle produit tensoriel externe de $X$ par $M$",
    r"on appelle \emph{produit tensoriel externe de} $X$ \emph{par} $M$",
    "The term being defined.")
add(205, "1.2, 'un A-module à droite grâce à l'action'",
    "'à droite' underlined (the earlier 'A-module à droite et X' is not)", "no underline markup", "underline",
    "high",
    r"un $A$-module à droite grâce", r"un $A$-module \emph{à droite} grâce", "")
add(205, "1.2, 'Ĉ = Hom(C,Ens)°'",
    "Hom underlined", r"\widehat{\cC}=\Hom(\cC,\Ens)^{\circ}", "underline", "high",
    r"=\Hom(\cC,\Ens)", r"=\uHom(\cC,\Ens)",
    "\\uHom (\\underline{\\Hom}) is defined in the preamble.")
add(205, "end of the page: 'l'allure plus familière suivante :'",
    "p. 205 ends with 'suivante :'; the display Hom_Ĉ(M ⊗_A X, Y) = ... is not on this page",
    "'suivante:' (s5.tex line 6923, diplomatic) is the first line of page 206: the folio-206 marker (line 6922) "
    "stands between 'familière' and 'suivante:'",
    "marker", "high", None, None,
    "Page 206 really begins at the display '\\[' after 'suivante:' (s5.tex line 6924). Exact fix: python -I "
    "move_marker.py 5 206 '\\[' (forward, no --before; simulated in memory on both layers: the marker then "
    "stands between 'suivante:' and '\\['). Text not moved.")

# ---------------- checks ----------------
pages = {p: open(rf"{B}\page_{p}.tex", encoding="utf-8", newline="").read() for p in range(201, 206)}
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    c = pages[d["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], c, repr(fx["old"][:80]))
    if "%%%%%%%%%%" in fx["old"]:
        bad += 1
        print("MARKER IN OLD", d["page"])
# overlapping olds on one page
for p in range(201, 206):
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = pages[p].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"][:30]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
cnt = {}
for d in F:
    k = "m" if d["kind"] == "misprint_in_print" else "n"
    cnt.setdefault(d["page"], {"n": 0, "m": 0})[k] += 1
print(cnt, "total", len(F), "problems", bad)
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("written", OUT)
