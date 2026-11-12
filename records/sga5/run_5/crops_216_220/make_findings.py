"""Build findings_216_220.json and check every fix's 'old' (sequentially, in listed order) against page_NNN.tex.
In the strings below, the character ¶ stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
batch = run / "b216_220"
out = run / "findings_216_220.json"


def nl(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


U = "Exposé V has no underline markup; \\emph is this file's command for the print's underline (\\emph{Preuve}; III B p. 146). "

# ---------------- page 216 ----------------
add(216, "first paragraph: 'notons Hom'_AR(X,Y) l'ensemble des isomorphismes de X dans Y dans P'_AR'",
    "l'ensemble des isomorphismes de X dans Y dans P'_AR", "l'ensemble des isomorphismes (keeps the printed reading)",
    "misprint_in_print", "medium", None, None,
    "Hom'_AR(X,Y) must be the set of all morphisms of X to Y in P'_AR = P(AR^{-1}): it is the target of m_XY, which is a bijection from Hom_AR(X,Y), and m is a functor that is an isomorphism of categories (2.4.3). 'isomorphismes' is a slip for 'morphismes'. The TeX keeps the print.",
    corrected="l'ensemble des morphismes")
add(216, "Proposition 2.4.3, statement",
    "underlined: 'Le foncteur' | 'est un isomorphisme de catégories'; m not underlined",
    "Le foncteur $m$ est un isomorphisme de catégories.  (no underline)", "underline", "high",
    r"Le foncteur $m$ est un isomorphisme de catégories.",
    r"\emph{Le foncteur} $m$ \emph{est un isomorphisme de catégories}.",
    U + "Formula letters and the final full stop are left out of the underline.")
add(216, "Preuve, first sentence", "Il s'agit de voir que pour tout couple (X,Y) d'objets de P ,",
    "Il s'agit de voir que, pour tout couple", "punctuation", "high",
    r"voir que, pour tout couple", r"voir que pour tout couple", "Comma added by the TeX.")
add(216, "Preuve, 'on se ramène immédiatement à voir que pour tout diagramme'",
    "à voir que pour tout diagramme commutatif", "à voir que, pour tout diagramme", "punctuation", "high",
    r"voir que, pour tout diagramme", r"voir que pour tout diagramme", "Comma added by the TeX.")
add(216, "end of the sentence before the first diagram", "le morphisme canonique de X[t] dans X[r] .",
    "dans $X[r]$:", "punctuation", "high",
    r"dans $X[r]$:", r"dans $X[r]$.", "The print ends the sentence with a full stop, not a colon.")
add(216, "'tous les morphismes canoniques entrant en jeu', before the second diagram",
    "entrant en jeu.", "entrant en jeu:", "punctuation", "high",
    r"entrant en jeu:", r"entrant en jeu.", "Full stop in the print, not a colon.")
add(216, "second diagram, after X[s] (bottom right)", "X[r] <--rho-- X[s] .  (full stop after the diagram)",
    "no full stop after the diagram", "punctuation", "high",
    "X[s] \\arrow[l,\"\\rho\"]¶\\end{tikzcd}", "X[s] \\arrow[l,\"\\rho\"]¶\\end{tikzcd}.",
    "The file's form for a stop after a diagram is '\\end{tikzcd}.' (as on p. 105).")

# ---------------- page 217 ----------------
add(217, "Proposition 2.4.4 (i)", "underlined: 'La catégorie' | 'est abélienne'",
    "La catégorie $P_{AR}$ est abélienne.  (no underline)", "underline", "high",
    r"\item La catégorie $P_{AR}$ est abélienne.", r"\item \emph{La catégorie} $P_{AR}$ \emph{est abélienne}.",
    U)
add(217, "Proposition 2.4.4 (ii)", "underlined: 'Le foncteur' | 'est exact'",
    "Le foncteur $p_{AR}:P\\to P_{AR}$ est exact.  (no underline)", "underline", "high",
    r"\item Le foncteur $p_{AR}:P\to P_{AR}$ est exact.", r"\item \emph{Le foncteur} $p_{AR}:P\to P_{AR}$ \emph{est exact}.",
    U)
add(217, "Proposition 2.4.4 (iii)",
    "underlined: 'Pour qu'un objet' | 'de' | 'soit' | 'nul' (not 'AR-') | 'il faut et il suffit que'",
    "(no underline)", "underline", "high",
    r"\item Pour qu'un objet $X$ de $P$ soit AR-nul, il faut et il suffit que $p_{AR}(X)=0$.",
    r"\item \emph{Pour qu'un objet} $X$ \emph{de} $P$ \emph{soit} AR-\emph{nul}, \emph{il faut et il suffit que} $p_{AR}(X)=0$.",
    U)
add(217, "Proposition 2.4.4 (iv)",
    "underlined: 'Le couple' | 'est un quotient de la catégorie abélienne' | 'par la sous catégorie abélienne épaisse des objets' | 'nuls'",
    "(no underline)", "underline", "high",
    r"\item Le couple $(p_{AR},P_{AR})$ est un quotient de la catégorie abélienne $P$ par la sous-catégorie abélienne épaisse des objets AR-nuls.",
    r"\item \emph{Le couple} $(p_{AR},P_{AR})$ \emph{est un quotient de la catégorie abélienne} $P$ \emph{par la sous-catégorie abélienne épaisse des objets} AR-\emph{nuls}.",
    U + "Apply before the two misprint edits of this item (next two findings).")
add(217, "Proposition 2.4.4 (iv), 'sous catégorie'",
    "par la sous catégorie abélienne  (a word space, no hyphen)", "sous-catégorie", "misprint_in_print", "high",
    r"sous-catégorie", r"sous catégorie",
    "The typist left out the hyphen (the print has 'sous-catégorie' on p. 219); the TeX silently corrects it. Diplomatic fix restores the printed reading.",
    corrected="sous-catégorie")
add(217, "Proposition 2.4.4 (iv), 'des objets AR nuls'",
    "des objets AR nuls.  (no hyphen: a plain space, whereas (iii) on the same page has AR-nul with a clear hyphen)",
    "AR-nuls", "misprint_in_print", "high",
    r"objets} AR-\emph{nuls}", r"objets} AR \emph{nuls}",
    "Missing hyphen in the print; the TeX silently corrects it. 'old' is taken from the text after the underline edit of (iv) (two findings above), which must be applied first.",
    corrected="AR-nuls")
add(217, "Preuve of 2.4.4, second sentence", "Il résulte de (2.3.4) que pour qu'un objet X de P soit AR-nul,",
    "(2.3.4) que, pour", "punctuation", "high",
    r"(2.3.4) que, pour", r"(2.3.4) que pour", "Comma added by the TeX.")
add(217, "Corollaire 2.4.5, first sentences",
    "underlined: 'Soit' | 'de la catégorie' | 'Les assertions suivantes sont équivalentes'",
    "(no underline)", "underline", "high",
    r"Soit $u:X\to Y$ de la catégorie $P$. Les assertions suivantes sont équivalentes:",
    r"\emph{Soit} $u:X\to Y$ \emph{de la catégorie} $P$. \emph{Les assertions suivantes sont équivalentes}:",
    U)
add(217, "Corollaire 2.4.5 (i)", "underlined: 'est un isomorphisme'", "(no underline)", "underline", "high",
    r"\item $p_{AR}(u)$ est un isomorphisme.", r"\item $p_{AR}(u)$ \emph{est un isomorphisme}.", U)
add(217, "Corollaire 2.4.5 (ii)", "underlined: 'Le noyau et le conoyau de' | 'sont' | 'nuls' (not 'AR-')",
    "(no underline)", "underline", "high",
    r"\item Le noyau et le conoyau de $u$ sont AR-nuls.",
    r"\item \emph{Le noyau et le conoyau de} $u$ \emph{sont} AR-\emph{nuls}.", U)
add(217, "after Corollaire 2.4.5 (ii): 'Un morphisme u : X → Y de la catégorie P ...'",
    "a new, indented paragraph (not underlined)", "runs on after \\end{enumerate} (no blank line: not indented)",
    "other", "medium",
    r"\end{enumerate}¶Un morphisme", r"\end{enumerate}¶¶Un morphisme",
    "Paragraph break of the print.")
add(217, "'sera appelé un AR-isomorphisme.'", "the defined term: 'isomorphisme' underlined, 'AR-' not",
    "AR-isomorphisme (no underline)", "underline", "high",
    r"appelé un AR-isomorphisme.", r"appelé un AR-\emph{isomorphisme}.", U)
add(217, "Définition 2.4.6, statement",
    "underlined: 'Deux objets' | 'et' | 'de la catégorie' | 'sont dits' | 'isomorphes si' (not 'AR-') | 'et' | 'sont isomorphes dans la catégorie'",
    "(no underline)", "underline", "high",
    r"Deux objets $X$ et $Y$ de la catégorie $P$ sont dits AR-isomorphes si $p_{AR}(X)$ et $p_{AR}(Y)$ sont isomorphes dans la catégorie",
    r"\emph{Deux objets} $X$ \emph{et} $Y$ \emph{de la catégorie} $P$ \emph{sont dits} AR-\emph{isomorphes si} $p_{AR}(X)$ \emph{et} $p_{AR}(Y)$ \emph{sont isomorphes dans la catégorie}",
    U)
add(217, "Définition 2.4.6, 'Si X et Y sont deux objets AR-isomorphes ...'",
    "a new, indented paragraph after '... dans la catégorie P_AR .' (not underlined: not part of the definition)",
    "same paragraph as the definition", "other", "high",
    r"$P_{AR}$. Si $X$ et $Y$", r"$P_{AR}$.¶¶Si $X$ et $Y$", "Paragraph break of the print.")
add(217, "heading 2.5", "2.5. Caractérisation ... de Mittag-Leffler-Artin-Rees.  (underlined title with a full stop)",
    "\\subsubsection*{2.5. ... Mittag-Leffler-Artin-Rees}", "punctuation", "high",
    r"Mittag-Leffler-Artin-Rees}", r"Mittag-Leffler-Artin-Rees.}", "Full stop of the underlined title.")
add(217, "Proposition 2.5.1, first sentence",
    "underlined: 'Les assertions suivantes pour un objet' | 'de' | 'sont équivalentes'",
    "(no underline)", "underline", "high",
    r"Les assertions suivantes pour un objet $X$ de $P$ sont équivalentes:",
    r"\emph{Les assertions suivantes pour un objet} $X$ \emph{de} $P$ \emph{sont équivalentes}:", U)
add(217, "Proposition 2.5.1 (i) (printed at the top of p. 218; the TeX has it above the folio-218 marker)",
    "(i) X vérifie (MLAR) (2.1.1) .  with 'vérifie (MLAR)' underlined in one stroke",
    "(no underline)", "underline", "high",
    r"\item $X$ vérifie (MLAR) (2.1.1).", r"\item $X$ \emph{vérifie (MLAR)} (2.1.1).",
    U + "The first stop of (2.1.1) looks like a comma under magnification: a smudged full stop, not reported.")
add(217, "Proposition 2.5.1 (ii), its first word 'Il' (printed on p. 218; the marker splits the item)",
    "'Il existe un système projectif strict' underlined in one stroke", "\\item Il  (no underline)",
    "underline", "high",
    r"\item Il", r"\item \emph{Il}",
    U + "The rest of the item is under the folio-218 marker: see the p. 218 finding for (ii). Both edits are balanced and can be applied separately.")

# ---------------- page 218 ----------------
add(218, "top of the page",
    "p. 218 begins with Proposition 2.5.1 (i) 'X vérifie (MLAR) (2.1.1) .'; p. 217 ends with 'sont équivalentes :' (the rest of p. 217 is blank)",
    "'\\item $X$ vérifie (MLAR) (2.1.1).' and '\\item Il' are the last two lines of page_217.tex; the folio-218 marker splits item (ii) between 'Il' and 'existe'",
    "marker", "high", None, None,
    "Page 218 really begins at '\\item $X$ vérifie (MLAR) (2.1.1).'. Exact fix, after the text edits: python -I move_marker.py 5 218 '\\item $X$' --before  (anchor without the words, so that it also finds the line after the underline edit filed under p. 217; simulated in memory on both layers: '\\begin{enumerate}[label=(\\roman*)]' / marker / '\\item $X$ ...' / '\\item Il' / 'existe un système ...'). Text not moved.")
add(218, "Proposition 2.5.1 (ii), after the marker",
    "underlined: '(Il) existe un système projectif strict' | 'et un' | 'isomorphisme' (not 'AR-')",
    "(no underline)", "underline", "high",
    r"existe un système projectif strict $Y$ et un AR-isomorphisme $u:Y\to X$ (2.4.5).",
    r"\emph{existe un système projectif strict} $Y$ \emph{et un} AR-\emph{isomorphisme} $u:Y\to X$ (2.4.5).",
    U + "Goes with the p. 217 edit '\\item \\emph{Il}' (same underline, split by the marker).")
add(218, "Proposition 2.5.1 (iii)",
    "underlined: 'Il existe un système projectif strict' | 'tel que' | 'et' | 'soient isomorphes dans la catégorie'",
    "(no underline)", "underline", "high",
    r"\item Il existe un système projectif strict $Y$ tel que $X$ et $Y$ soient isomorphes dans la catégorie $P_{AR}$.",
    r"\item \emph{Il existe un système projectif strict} $Y$ \emph{tel que} $X$ \emph{et} $Y$ \emph{soient isomorphes dans la catégorie} $P_{AR}$.",
    U)
add(218, "Proposition 2.5.1 (iv)",
    "underlined: 'vérifie la condition de Mittag-Leffler et, désignant par' | 'le système projectif des images universelles de' | 'le système projectif' | 'est' | 'nul' (not 'AR-')",
    "(no underline)", "underline", "high",
    r"\item $X$ vérifie la condition de Mittag-Leffler et, désignant par $X'$ le système projectif des images universelles de $X$, le système projectif $X/X'$ est AR-nul.",
    r"\item $X$ \emph{vérifie la condition de Mittag-Leffler et, désignant par} $X'$ \emph{le système projectif des images universelles de} $X$, \emph{le système projectif} $X/X'$ \emph{est} AR-\emph{nul}.",
    U)
add(218, "Preuve of 2.5.1, first sentence", "Nous allons prouver la suite d'implications :",
    "la suite d'implications  (no colon)", "punctuation", "high",
    r"prouver la suite d'implications", r"prouver la suite d'implications:",
    "Colon of the print (written without a space, as the file's other colons).")
add(218, "'(i) ⇒ (iv) . Il existe un entier m' after the display", "a new, indented paragraph",
    "runs on after \\] (no blank line)", "other", "high",
    "\\]¶$(i)\\Rightarrow(iv)$.", "\\]¶¶$(i)\\Rightarrow(iv)$.",
    "Paragraph break of the print; the three other steps already start new paragraphs in the TeX.")
add(218, "(i) ⇒ (iv): 'le morphisme canonique w_mX de X[m] dans X'",
    "w_mX  (a clear w)", "$w_{mX}$ (keeps the printed reading)", "misprint_in_print", "low",
    None, None,
    "The canonical morphism X[r] → X is v_{rX} in this exposé (its definition on p. 211; v_{rX}, v_{sX} on p. 216); w here is probably a slip for v. The TeX keeps the print.",
    corrected="$v_{mX}$")
add(218, "(i) ⇒ (iv): 'est un épimorphisme (direct) donc ,'",
    "p_AR(i) est un épimorphisme (direct) donc , puisque", "épimorphisme direct, donc, puisque",
    "punctuation", "high",
    r"épimorphisme direct, donc,", r"épimorphisme (direct) donc,",
    "The print has 'direct' in parentheses and no comma before 'donc'.")
add(218, "(i) ⇒ (iv), last sentence", "On conclut par (2.4.4 (iii)) .", "On conclut par (2.4.4) (iii).",
    "punctuation", "high",
    r"On conclut par (2.4.4) (iii).", r"On conclut par (2.4.4 (iii)).",
    "The print nests the parentheses.")
add(218, "(iv) ⇒ (iii), first sentence", "La condition de (iv) signifie,", "La condition (iv) signifie,",
    "missing", "high",
    r"La condition (iv) signifie", r"La condition de (iv) signifie", "Word 'de' missing in the TeX.")
add(218, "(ii) ⇒ (i): 'tel que pour tout s supérieur ou égal à r le morphisme canonique'",
    "tel que pour tout s supérieur ou égal à r le morphisme  (no commas)",
    "tel que, pour tout $s$ supérieur ou égal à $r$, le morphisme", "punctuation", "high",
    r"tel que, pour tout $s$ supérieur ou égal à $r$, le morphisme",
    r"tel que pour tout $s$ supérieur ou égal à $r$ le morphisme", "Two commas added by the TeX.")
add(218, "(ii) ⇒ (i): 'On en conclut que pour s ≥ r l'image'", "On en conclut que pour s≥r l'image  (no commas)",
    "On en conclut que, pour $s\\ge r$, l'image", "punctuation", "high",
    r"On en conclut que, pour $s\ge r$, l'image", r"On en conclut que pour $s\ge r$ l'image",
    "Two commas added by the TeX.")
add(218, "last line of page_218.tex (printed at the top of p. 219): 'donc que X vérifie (MLAR) et que Y est le'",
    "donc que X vérifie (MLAR) et que Y est le  (no comma)", "vérifie (MLAR), et que", "punctuation", "high",
    r"vérifie (MLAR), et que", r"vérifie (MLAR) et que", "Comma added by the TeX.")

# ---------------- page 219 ----------------
add(219, "top of the page",
    "p. 219 begins 'pour s suffisamment grand, donc que X vérifie (MLAR) et que Y est le'; p. 218 ends '... On en conclut que Y est l'image de X[s]' (the rest of p. 218 is blank)",
    "'pour $s$ suffisamment grand, donc que $X$ vérifie (MLAR), et que $Y$ est le' ends the last line of page_218.tex, above the folio-219 marker",
    "marker", "high", None, None,
    "Page 219 really begins at 'pour $s$ suffisamment grand'. Exact fix: python -I move_marker.py 5 219 'pour $s$ suffisamment grand' --before  (simulated in memory on both layers: '... l'image de $X[s]$' / marker / 'pour $s$ suffisamment grand, ... est le' / 'système projectif ...'; the comma edit of that line, filed under p. 218, does not touch the anchor). Text not moved.")
add(219, "Corollaire 2.5.2, statement",
    "underlined: 'Soit' | 'un' | 'isomorphisme' (not 'AR-') | 'étant strict' | 'Dans ces conditions' | 'vérifie la condition' | 'et' | 'est le système projectif des images universelles de'",
    "(no underline)", "underline", "high",
    r"Soit $u:Y\to X$ un AR-isomorphisme, $Y$ étant strict. Dans ces conditions, $X$ vérifie la condition (MLAR) et $u(Y)$ est le système projectif des images universelles de $X$.",
    r"\emph{Soit} $u:Y\to X$ \emph{un} AR-\emph{isomorphisme}, $Y$ \emph{étant strict}. \emph{Dans ces conditions}, $X$ \emph{vérifie la condition} (MLAR) \emph{et} $u(Y)$ \emph{est le système projectif des images universelles de} $X$.",
    U + "(MLAR), u(Y), X, Y not underlined.")
add(219, "heading 3", "3. Systèmes projectifs J-adiques et AR-J-adiques.  (underlined title with a full stop)",
    "\\subsection*{3. ... AR-$J$-adiques}", "punctuation", "high",
    r"AR-$J$-adiques}", r"AR-$J$-adiques.}", "Full stop of the underlined title.")
add(219, "§3, first paragraph: 'les symboles P et P_AR désignent, respectivement les catégories'",
    "a hand-drawn comma-shaped ink stroke below the line between 'désignent' and 'respectivement'",
    "désignent respectivement", "punctuation", "low",
    r"désignent respectivement", r"désignent, respectivement",
    "Probably a handwritten comma (a deliberate slanted stroke at the comma position, not a speck); the comma of Hom_AR(N°,C) on the same line is also retouched by pen. Drop if judged an ink mark.")
add(219, "§3, first paragraph: 'les catégories Hom(N°,C)'", "Hom underlined (the category of projective systems)",
    "$\\Hom(\\NN^\\circ,\\cC)$", "underline", "high",
    r"les catégories $\Hom(\NN^\circ,\cC)$", r"les catégories $\underline{\Hom}(\NN^\circ,\cC)$",
    "Only 'Hom' is underlined. The hom-sets Hom_AR(X,Y), Hom'_AR(X,Y) on p. 216 are not underlined.")
add(219, "§3, first paragraph: 'et Hom_AR(N°,C)'", "Hom underlined, not the index AR",
    "$\\Hom_{AR}(\\NN^\\circ,\\cC)$", "underline", "high",
    r"$\Hom_{AR}(\NN^\circ,\cC)$", r"$\underline{\Hom}_{AR}(\NN^\circ,\cC)$", "As the previous finding.")
add(219, "heading 3.1", "3.1. Systèmes projectifs J-adiques.  (underlined title with a full stop)",
    "\\subsubsection*{3.1. Systèmes projectifs $J$-adiques}", "punctuation", "high",
    r"{3.1. Systèmes projectifs $J$-adiques}", r"{3.1. Systèmes projectifs $J$-adiques.}",
    "Full stop of the underlined title.")
add(219, "Définition 3.1.1, first sentences",
    "underlined: 'Soit' | 'un objet de' | 'On dit que' | 'est' | 'adique' (not 'J-') + 's'il vérifie les conditions suivantes'",
    "(no underline)", "underline", "high",
    r"Soit $X$ un objet de $P$. On dit que $X$ est $J$-adique s'il vérifie les conditions suivantes:",
    r"\emph{Soit} $X$ \emph{un objet de} $P$. \emph{On dit que} $X$ \emph{est} $J$-\emph{adique s'il vérifie les conditions suivantes}:",
    U)
add(219, "Définition 3.1.1 (i), first word", "(i) Pour tout entier  (capital P)", "pour tout entier",
    "word", "high",
    r"\item pour tout entier", r"\item Pour tout entier", "Capital in the print. Apply before the underline edit of (i).")
add(219, "Définition 3.1.1 (i), end", "J^{n+1}X_n = 0 .  (full stop)", "$J^{n+1}X_n=0$;", "punctuation", "high",
    r"$J^{n+1}X_n=0$;", r"$J^{n+1}X_n=0$.", "Full stop in the print, not a semicolon.")
add(219, "Définition 3.1.1 (i)", "underlined: 'Pour tout entier'", "(no underline)", "underline", "high",
    r"\item Pour tout entier", r"\item \emph{Pour tout entier}",
    U + "'old' is taken from the text after the capital-P edit (two findings above), which must be applied first.")
add(219, "Définition 3.1.1 (ii), first word", "(ii) Pour tout couple  (capital P)", "pour tout couple",
    "word", "high",
    r"\item pour tout couple", r"\item Pour tout couple", "Capital in the print. Apply before the underline edit of (ii).")
add(219, "Définition 3.1.1 (ii)",
    "underlined: 'Pour tout couple' | 'd'entiers avec' | 'le morphisme' | 'déduit du morphisme de transition' | 'est un isomorphisme'",
    "(no underline)", "underline", "high",
    "\\item Pour tout couple $(m,n)$ d'entiers avec $m\\ge n\\ge0$, le morphisme¶\\[¶A/J^{n+1}\\otimes_A X_m\\longrightarrow X_n¶\\]¶déduit du morphisme de transition $X_m\\to X_n$ est un isomorphisme.",
    "\\item \\emph{Pour tout couple} $(m,n)$ \\emph{d'entiers avec} $m\\ge n\\ge0$, \\emph{le morphisme}¶\\[¶A/J^{n+1}\\otimes_A X_m\\longrightarrow X_n¶\\]¶\\emph{déduit du morphisme de transition} $X_m\\to X_n$ \\emph{est un isomorphisme}.",
    U + "'old' is taken from the text after the capital-P edit (previous finding), which must be applied first. The print runs A/J^{n+1} ⊗_A X_m → X_n into the text (layout, not reported).")
add(219, "Remarque 3.1.2: 'Alors on peut montrer que si I et J définissent'",
    "on peut montrer que si I et J  (no comma)", "on peut montrer que, si", "punctuation", "high",
    r"montrer que, si", r"montrer que si", "Comma added by the TeX.")

# ---------------- page 220 ----------------
add(220, "label of Proposition 3.1.3", "PROPOSITION 3.1.3. (Stabilités par suites exactes) .",
    "\\begin{statement}{Proposition 3.1.3 (Stabilités par suites exactes)}  (renders 'Proposition 3.1.3 (Stabilités ...).')",
    "punctuation", "medium",
    r"{Proposition 3.1.3 (Stabilités", r"{Proposition 3.1.3. (Stabilités",
    "The print has a full stop after the number as well as after the parenthesis; the environment supplies only the final one.")
add(220, "Proposition 3.1.3, statement around the display", "underlined: 'Soit' | 'une suite exacte de'",
    "(no underline)", "underline", "high",
    "Soit¶\\[¶0\\longrightarrow X\\stackrel{u}{\\longrightarrow}Y\\stackrel{v}{\\longrightarrow}Z\\longrightarrow0¶\\]¶une suite exacte de $P$.",
    "\\emph{Soit}¶\\[¶0\\longrightarrow X\\stackrel{u}{\\longrightarrow}Y\\stackrel{v}{\\longrightarrow}Z\\longrightarrow0¶\\]¶\\emph{une suite exacte de} $P$.",
    U)
add(220, "Proposition 3.1.3 (i)",
    "underlined: 'Si' | 'est strict et' | 'est' | 'adique, alors' | 'est' | 'adique' (the 'J-' not)",
    "(no underline)", "underline", "high",
    r"\item Si $X$ est strict et $Y$ est $J$-adique, alors $Z$ est $J$-adique.",
    r"\item \emph{Si} $X$ \emph{est strict et} $Y$ \emph{est} $J$-\emph{adique, alors} $Z$ \emph{est} $J$-\emph{adique}.",
    U)
add(220, "Proposition 3.1.3 (ii)",
    "underlined: 'Si' | 'est strict et' | 'est' | 'adique, alors' | 'est strict'",
    "(no underline)", "underline", "high",
    r"\item Si $Y$ est strict et $Z$ est $J$-adique, alors $X$ est strict.",
    r"\item \emph{Si} $Y$ \emph{est strict et} $Z$ \emph{est} $J$-\emph{adique, alors} $X$ \emph{est strict}.",
    U)
add(220, "Proposition 3.1.3 (iii)", "underlined: 'Si' | 'et' | 'sont' | 'adiques' | 'est' | 'adique'",
    "(no underline)", "underline", "high",
    r"\item Si $X$ et $Z$ sont $J$-adiques, $Y$ est $J$-adique.",
    r"\item \emph{Si} $X$ \emph{et} $Z$ \emph{sont} $J$-\emph{adiques}, $Y$ \emph{est} $J$-\emph{adique}.",
    U)
add(220, "diagram (T) in the proof of 3.1.3", "the diagram carries the label (T) at its left",
    "no label in the display (the text refers to 'le diagramme $(T)$' twice)", "missing", "high",
    "Z_n \\arrow[r] & 0 .¶\\end{tikzcd}", "Z_n \\arrow[r] & 0 .¶\\end{tikzcd}¶\\tag{T}",
    "\\tag works in \\[ \\] with amsmath (the file gives the display (S) of Exposé V a \\tag{S}); the print sets the label on the left (position not reported).")
add(220, "heading 3.2", "3.2. Systèmes projectifs AR-J-adiques.  (underlined title with a full stop)",
    "\\subsubsection*{3.2. Systèmes projectifs AR-$J$-adiques}", "punctuation", "high",
    r"AR-$J$-adiques}", r"AR-$J$-adiques.}", "Full stop of the underlined title.")
add(220, "Proposition 3.2.1, first sentence", "pour tout n ≥ 0 sont équivalentes :  (no comma)",
    "pour tout $n\\ge0$, sont équivalentes:", "punctuation", "high",
    r"pour tout $n\ge0$, sont", r"pour tout $n\ge0$ sont",
    "Comma added by the TeX. Apply before the underline edit of this sentence (next finding).")
add(220, "Proposition 3.2.1, first sentence",
    "underlined: 'Les assertions suivantes, pour un objet' | 'de' | 'tel' + 'que' | 'pour tout' | 'sont équivalentes'",
    "(no underline)", "underline", "high",
    r"Les assertions suivantes, pour un objet $X$ de $P$ tel que $J^{n+1}X_n=0$ pour tout $n\ge0$ sont équivalentes:",
    r"\emph{Les assertions suivantes, pour un objet} $X$ \emph{de} $P$ \emph{tel que} $J^{n+1}X_n=0$ \emph{pour tout} $n\ge0$ \emph{sont équivalentes}:",
    U + "'old' is taken from the text after the comma edit (previous finding), which must be applied first.")
add(220, "Proposition 3.2.1 (i)",
    "underlined: 'Il existe un système projectif' | 'adique' | 'et un' | 'isomorphisme' (not 'AR-')",
    "(no underline)", "underline", "high",
    r"\item Il existe un système projectif $J$-adique $Y$ et un AR-isomorphisme $u:Y\to X$ (2.4.5).",
    r"\item \emph{Il existe un système projectif} $J$-\emph{adique} $Y$ \emph{et un} AR-\emph{isomorphisme} $u:Y\to X$ (2.4.5).",
    U)
add(220, "Proposition 3.2.1 (ii)",
    "underlined: 'Il existe un système projectif' | 'adique' | 'isomorphe à' | 'dans la catégorie'",
    "(no underline)", "underline", "high",
    r"\item Il existe un système projectif $J$-adique $Y$, isomorphe à $X$ dans la catégorie $P_{AR}$.",
    r"\item \emph{Il existe un système projectif} $J$-\emph{adique} $Y$, \emph{isomorphe à} $X$ \emph{dans la catégorie} $P_{AR}$.",
    U)
add(220, "foot of the page / top of p. 221",
    "p. 220 ends with Proposition 3.2.1 (ii) '... dans la catégorie P_AR .' (the rest of the page is blank); the proof begins p. 221",
    "'\\begin{prooftext}[' is the last line of page_220.tex; the folio-221 marker splits it from its argument 'Preuve]'",
    "marker", "high", None, None,
    "Page 221 really begins at '\\begin{prooftext}[Preuve]'. Exact fix: python -I marker_split_word.py 5 221 pull '\\begin{prooftext}['  (simulated in memory on both layers: '\\end{statement}' / marker / '\\begin{prooftext}[Preuve]' / 'Il nous faut montrer ...'; move_marker.py would leave the bracket split across a line, giving the label a leading space). Text not moved.")

# ---------------- checks ----------------
ok = True
texts = {p: (batch / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(216, 221)}
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    t = texts[f["page"]]
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, f["page"], n, repr(fx["old"][:80]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("MARKER IN FIX", i)
    texts[f["page"]] = t.replace(fx["old"], fx["new"], 1)
# independent check against the original files: which olds need an earlier edit
orig = {p: (batch / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(216, 221)}
for i, f in enumerate(F):
    fx = f["fix"]
    if fx and orig[f["page"]].count(fx["old"]) != 1:
        print("depends on an earlier edit:", f["page"], repr(fx["old"][:60]), "count in original:",
              orig[f["page"]].count(fx["old"]))
# brace balance of every new vs old
for i, f in enumerate(F):
    fx = f["fix"]
    if fx:
        d_old = fx["old"].count("{") - fx["old"].count("}")
        d_new = fx["new"].count("{") - fx["new"].count("}")
        if d_old != d_new:
            print("BRACE BALANCE CHANGES", i, f["page"], repr(fx["old"][:60]))
out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(216, 221):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(F), "all unique in sequence" if ok else "PROBLEMS")
