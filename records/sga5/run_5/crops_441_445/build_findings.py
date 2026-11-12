# Build findings_441_445.json and check that every fix's old occurs exactly once in its page file.
# Strings are raw; the character NL stands for a line break (the page files use LF).
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b441_445"
OUT = RUN / "findings_441_445.json"
NL = "\u23ce"


def s(x):
    return x.replace(NL, "\n") if isinstance(x, str) else x


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 441 ----------------
L.append(F(441, "Exemple 7.3, line 3: '(cf.XIV) et un faisceau de Λ-modules sur X'",
           "(cf.XIV)  et un faisceau de Λ-modules sur X  .  (no F between 'et' and 'un'; checked on a crop)",
           r"(cf. XIV) et $F$ un faisceau de $\Lambda$-modules sur $X$.",
           "misprint_in_print", "high",
           r"et $F$ un faisceau", r"et un faisceau",
           "The typist left out the name F of the sheaf (used in the rest of the example). The TeX silently supplies it; "
           "the fix restores the printed reading (diplomatic layer only).",
           corrected=r"et $F$ un faisceau"))
L.append(F(441, "Exemple 7.3, 'Si Y,S sont des schémas sur F_p et si Y est un schéma sur S'",
           "sur 𝔽_p   et si  Y  (no comma)", r"sur $\mathbb F_p$, et si $Y$",
           "punctuation", "high",
           r"$\mathbb F_p$, et si", r"$\mathbb F_p$ et si",
           "The TeX adds a comma."))
L.append(F(441, "Exemple 7.3, 'nous désignons par Fr_{Y/S} : Y -> Y^{(p/S)}'",
           "the F of Fr_{Y/S} is the typist's double-struck F (the same overstruck glyph as in 𝔽_p two lines above), "
           "underlined; the other three Fr of the page have a plain F",
           r"\Fr_{Y/S}", "misprint_in_print", "medium",
           r"\Fr_{Y/S}", r"\operatorname{\mathbb{F}r}_{Y/S}",
           "Typing slip (the 𝔽 of 𝔽_p for the F of Fr); the TeX silently gives a plain Fr. A glyph question of the kind "
           "held in GLOBAL_ISSUES 61 (plain Q for double-struck Q): apply only if the diplomatic layer reproduces such "
           "glyphs. If \\Fr gets the underline of the convention entry below, write "
           "\\underline{\\operatorname{\\mathbb{F}r}}_{Y/S}.",
           corrected=r"\Fr_{Y/S}"))
L.append(F(441, "'On obtient un morphisme de faisceaux sur X_et'",
           "X_et (subscript 'et' without accent)", r"$X_{\et}$ (\et is \mathrm{\acute{e}t}, s5.tex line 77)",
           "accent", "high",
           r"X_{\et}", r"X_{\mathrm{et}}",
           "The typescript's subscript has no accent; written as the logged fixes of pp. 372-373 (findings_371_375)."))
L.append(F(441, "end of the sentence 'On obtient un morphisme de faisceaux sur X_et :', before the display",
           "sur  X_et  :", r"sur $X_{\et}$ followed by the display, no colon",
           "punctuation", "high",
           r"$⏎\[⏎(\fr_X)_*(F)\longrightarrow F", r"$ :⏎\[⏎(\fr_X)_*(F)\longrightarrow F",
           "The TeX drops the colon before the display. The old starts at the $ that closes X_{\\et}: independent of the "
           "accent edit."))
L.append(F(441, "'en posant pour tout X-préschéma étale U :'",
           "en posant pour tout  X-préschéma étale  U  :", r"en posant, pour tout $X$-préschéma étale $U$,",
           "punctuation", "high",
           r"en posant, pour tout $X$-préschéma étale $U$,", r"en posant pour tout $X$-préschéma étale $U$ :",
           "The TeX adds a comma after 'posant' and writes a comma for the print's colon."))
L.append(F(441, "'Son inverse :' before the display",
           "Son inverse :", "Son inverse",
           "punctuation", "high",
           r"Son inverse", r"Son inverse :",
           "The TeX drops the colon."))
L.append(F(441, "display F(Fr_{/X})^{-1} : F -> (fr_X)_*(F) ,",
           "... ⟶ (fr_X)_* (F)   ,", r"F(\Fr_{/X})^{-1}:F\longrightarrow (\fr_X)_*(F)",
           "punctuation", "high",
           r"(\fr_X)_*(F)⏎\]", r"(\fr_X)_*(F),⏎\]",
           "The TeX drops the comma that ends the display."))
L.append(F(441, "display (Fr^*_{F/X}, fr_X) : (X,F) -> (X,F) ,",
           "... : (X,F) ⟶ (X,F)    ,", r"(\Fr_{F/X}^*,\fr_X):(X,F)\longrightarrow (X,F)",
           "punctuation", "high",
           r"(X,F)\longrightarrow (X,F)", r"(X,F)\longrightarrow (X,F),",
           "The TeX drops the comma that ends the display."))
L.append(F(441, "reference [1]: 'Math. Ann. 117 (1941) p. 659-671,'",
           "117 (1941) p. 659-671,", r"117 (1941), p. 659--671;",
           "punctuation", "high",
           r"(1941), p.", r"(1941) p.",
           "The TeX adds a comma after the year."))
L.append(F(441, "reference [1]: page range 659-671",
           "659-671 (hyphen)", r"659--671",
           "punctuation", "high",
           r"659--", r"659-",
           "En dash for the print's hyphen."))
L.append(F(441, "reference [1]: punctuation after 659-671",
           "659-671,  (comma; the next line begins 'Fixpunktklassen II, III')", r"659--671;",
           "punctuation", "high",
           r"671; Fix", r"671, Fix",
           "Semicolon for the print's comma. Independent of the en-dash edit before it (no shared characters)."))
L.append(F(441, "reference [1]: (1942-1943)",
           "(1942-1943)", r"(1942--1943)",
           "punctuation", "high",
           r"1942--1943", r"1942-1943",
           "En dash for the print's hyphen."))
L.append(F(441, "reference [1]: p. 216-234",
           "216-234", r"216--234",
           "punctuation", "high",
           r"216--234", r"216-234",
           "En dash for the print's hyphen."))
L.append(F(441, "reference [1]: p. 544-577",
           "544-577", r"544--577",
           "punctuation", "high",
           r"544--577", r"544-577",
           "En dash for the print's hyphen."))
L.append(F(441, "heading of Exposé XV (printed at the top of p. 442; the line stands under the folio-441 marker)",
           "E X P O S E  XV (letter-spaced capitals, underlined)", r"\section*{Exposé XV}",
           "word", "high",
           r"\section*{Exposé XV}", r"\section*{EXPOSÉ XV}",
           "Capitals as printed, as the logged EXPOSÉ V, VI, VII (pp. 204, 250, 281); accented capital per the volume's "
           "rule. Filed under p. 441, where the line stands now; independent of the marker move of p. 442 (its anchor "
           "'\\section*{E' matches before and after this edit)."))
L.append(F(441, "fr and Fr throughout Exemple 7.3 (convention entry; e.g. 'fr_X : X -> X', '(fr_X)_*(F)', "
                "'F(Fr_{U/X})', 'Fr^*_{F/X}')",
           "fr and Fr singly underlined (all six fr and five Fr of the page)",
           r"\fr, \Fr = \operatorname{fr}, \operatorname{Fr} (s5.tex preamble): no underline",
           "underline", "high",
           r"$\fr_X:X\to X$", r"$\underline{\fr}_X:X\to X$",
           "Convention: the print underlines the Frobenius symbols, the macros print them plain. Reported once, not "
           "itemized: decide globally (single underline here in Exposé XIV 7.3; double underline in Exposé XV, entry "
           "on p. 442). Fix given for the first occurrence only."))

# ---------------- page 442 ----------------
L.append(F(442, "top of the page: the heading 'E X P O S E  XV' and the title block",
           "p. 442 begins with 'E X P O S E  XV', then the title 'MORPHISME DE FROBENIUS ET RATIONALITE DES FONCTIONS "
           "L .', 'par C. HOUZEL', '§ 1. MORPHISME DE FROBENIUS'; p. 441 ends with reference [1] (Wecken).",
           "'\\section*{Exposé XV}', '\\begin{center}' and '\\Large\\bfseries' are the last lines of page_441.tex, "
           "above the folio-442 marker",
           "marker", "high", None, None,
           "Page 442 really begins at '\\section*{Exposé XV}' (diplomatic s5.tex line 14839, current 14835 at the time "
           "of the check; the file is being edited, line numbers move). Exact fix: python -I move_marker.py 5 442 "
           "'\\section*{E' --before (simulated in memory on both layers: the marker moves back three lines, to its own "
           "line between the blank line after reference [1] and '\\section*{Exposé XV}'; the anchor matches before "
           "and after the EXPOSÉ capitals edit filed under p. 441). Text not moved."))
L.append(F(442, "title of the exposé",
           "MORPHISME DE FROBENIUS ET RATIONALITE DES FONCTIONS  L  .  (underlined)",
           r"MORPHISME DE FROBENIUS ET RATIONALITÉ DES FONCTIONS $L$",
           "punctuation", "high",
           r"FONCTIONS $L$", r"FONCTIONS $L$.",
           "The underlined title ends with a full stop in the print; the TeX drops it. (The broken T of 'ET' is a "
           "defect of the type; RATIONALITE without accent: the accented capital stands.)"))
L.append(F(442, "author line",
           "par C. HOUZEL", "par C. Houzel",
           "word", "high",
           r"par C. Houzel", r"par C. HOUZEL",
           "The name in capitals, as printed."))
L.append(F(442, "heading § 1",
           "§ 1. MORPHISME DE FROBENIUS (capitals, centred, underlined)", r"\subsection*{§ 1. Morphisme de Frobenius}",
           "word", "high",
           r"§ 1. Morphisme de Frobenius", r"§ 1. MORPHISME DE FROBENIUS",
           "Capitals as printed."))
L.append(F(442, "heading n° 1",
           "n° 1. Endomorphisme de Frobenius.  (underlined)",
           r"\subsubsection*{n\textsuperscript{o} 1. Endomorphisme de Frobenius}",
           "punctuation", "high",
           r"Endomorphisme de Frobenius}", r"Endomorphisme de Frobenius.}",
           "The underlined title ends with a full stop in the print; the TeX drops it."))
L.append(F(442, "Définition 1, 'Soit p un nombre premier'",
           "Soit (underlined)  p  un nombre premier (underlined)", r"Soit $p$ un nombre premier",
           "underline", "high",
           r"Soit $p$ un nombre premier", r"\emph{Soit} $p$ \emph{un nombre premier}",
           "The print underlines the statement word group by word group, leaving out the letters and the punctuation; "
           "the TeX has no underline markup in Exposé XV. Written with \\emph, as the underlined statements of Exposés "
           "III B, V, XII and XIV."))
L.append(F(442, "Définition 1, 'premier, on dit qu'un préschéma'",
           "premier, on dit qu'un préschéma  (comma, small 'on'; 'on dit qu'un préschéma' underlined)",
           r"premier. On dit qu'un préschéma",
           "punctuation", "high",
           r". On dit qu'un préschéma", r", \emph{on dit qu'un préschéma}",
           "The print runs one sentence: a comma and 'on' where the TeX has a full stop and 'On'. The new text also "
           "carries the underline of the statement. No shared characters with the underline edits before and after."))
L.append(F(442, "Définition 1, 'est de caractéristique p si'",
           "est de caractéristique (underlined; 'caractéristique' has a second underline, the defined term)  p  si "
           "(underlined)",
           r"est de caractéristique $p$ si $p\cdot 1_{\OO_X}=0$",
           "underline", "high",
           r"est de caractéristique $p$ si $p", r"\emph{est de \underline{caractéristique}} $p$ \emph{si} $p",
           "The single underline as \\emph (as above); the second line under the defined term written \\underline "
           "inside the run (\\underline{\\underline{caractéristique}} if the volume renders underlines literally)."))
L.append(F(442, "'le morphisme (unique) X -> Spec(Z)'",
           "le morphisme (uni-que)", "le morphisme unique",
           "punctuation", "high",
           r"le morphisme unique", r"le morphisme (unique)",
           "The TeX drops the parentheses."))
L.append(F(442, "'notons de plus qu'une telle factorisation est unique.'",
           "unique (underlined)", "est unique.",
           "underline", "high",
           r"factorisation est unique.", r"factorisation est \emph{unique}.",
           "Emphasis by underlining; \\emph as above."))
L.append(F(442, "'le couple fr_X = (id_{|X|}, φ)' (convention entry for Exposé XV; the same on pp. 443-445)",
           "fr with a double underline",
           r"$\fr_X=(\id_{|X|},\varphi)$ (\fr = \operatorname{fr}: no underline)",
           "underline", "high",
           r"$\fr_X=(\id", r"$\underline{\underline{\fr}}_X=(\id",
           "Convention: in Exposé XV the print underlines fr and Fr twice (pp. 442-445: fr_X, fr_Y, fr_S, fr, "
           "Fr_{X/S}, Fr_{X/Y}, Fr_{Y/S}, Fr_{X'/S'}, also in the diagrams), written as the double-underlined L of "
           "p. 37; the TeX's \\fr and \\Fr are plain. Reported once, not itemized: decide globally (Exposé XIV 7.3 has "
           "a single underline, p. 441). Exception: p. 443 'L'endomorphisme de Frobenius fr_X dépend "
           "fonctoriellement' prints fr_X without underline; keep it plain there if the macros are redefined."))

# ---------------- page 443 ----------------
L.append(F(443, "Définition 2, first sentence",
           "Soit (u.)  X  un préschéma de caractéristique (u.)  p ;  on appelle endomorphisme de Frobénius de (u.)  X",
           r"Soit $X$ un préschéma de caractéristique $p$; on appelle endomorphisme de Frobenius de $X$",
           "underline", "high",
           r"Soit $X$ un préschéma de caractéristique $p$; on appelle endomorphisme de Frobenius de $X$",
           r"\emph{Soit} $X$ \emph{un préschéma de caractéristique} $p$; \emph{on appelle endomorphisme de Frobenius de} $X$",
           "Underlined statement (\\emph as on p. 442). Apply before the misprint fix 'Frobénius' below; that fix's "
           "old 'Frobenius de' occurs once before and after this edit."))
L.append(F(443, "Définition 2, 'l'endomorphisme fr_X ainsi défini.'",
           "l'endomorphisme (u.)  fr_X (double underline)  ainsi défini (u.) .",
           r"l'endomorphisme $\fr_X$ ainsi défini.",
           "underline", "high",
           r"l'endomorphisme $\fr_X$ ainsi défini.", r"\emph{l'endomorphisme} $\fr_X$ \emph{ainsi défini}.",
           "Underlined statement; the double underline of fr is the convention entry of p. 442."))
L.append(F(443, "Définition 2, 'endomorphisme de Frobénius de X'",
           "Frobénius (with é; checked on a crop)", "Frobenius",
           "misprint_in_print", "medium",
           r"Frobenius de", r"Frobénius de",
           "The print accents the name here only ('Frobenius' everywhere else on these pages, also two lines below); "
           "the TeX silently gives 'Frobenius'. Listed after the underline edit of Définition 2: its old occurs once "
           "before and after that edit.",
           corrected=r"Frobenius de"))
L.append(F(443, "'dépend fonctoriellement du préschéma X'",
           "fonctoriellement (underlined); the fr_X before it has no underline here",
           "dépend fonctoriellement du préschéma",
           "underline", "high",
           r"fonctoriellement du préschéma", r"\emph{fonctoriellement} du préschéma",
           "Emphasis by underlining."))
L.append(F(443, "'c'est-à-dire que pour tout morphisme'",
           "c'est-à-dire que pour tout", "c'est-à-dire que, pour tout",
           "punctuation", "high",
           r"que, pour tout", r"que pour tout",
           "The TeX adds a comma."))
L.append(F(443, "heading n° 2",
           "n°2. Morphisme de Frobenius relatif.  (underlined)",
           r"\subsubsection*{n\textsuperscript{o} 2. Morphisme de Frobenius relatif}",
           "punctuation", "high",
           r"Frobenius relatif}", r"Frobenius relatif.}",
           "The underlined title ends with a full stop in the print; the TeX drops it."))
L.append(F(443, "'Soit S un préschéma de caractéristique p , tous les S-préschémas'",
           "p  , tous les", r"$p$; tous les",
           "punctuation", "high",
           r"$p$; tous les", r"$p$, tous les",
           "Semicolon for the print's comma."))
L.append(F(443, "formula π_{X/S} : X x_S (S,fr_S) -> X",
           "... ⟶ X  où (S,fr_S) désigne  (no comma; the formula runs in the text)",
           r"\pi_{X/S}:X\times_S(S,\fr_S)\longrightarrow X,",
           "punctuation", "high",
           r"\longrightarrow X,⏎\]", r"\longrightarrow X⏎\]",
           "The TeX adds a comma at the end of the display (display for the print's run-in formula: layout, not "
           "reported)."))
L.append(F(443, "'par X^{(p/S)} ou même par X^{(p)}'",
           "par  X^{(p/S)}  ou même par", r"par $X^{(p/S)}$, ou même par",
           "punctuation", "high",
           r"$X^{(p/S)}$, ou même", r"$X^{(p/S)}$ ou même",
           "The TeX adds a comma."))
L.append(F(443, "'qui composé avec π_{X/S} donne fr_X'",
           "qui composé avec π_{X/S} donne", r"qui, composé avec $\pi_{X/S}$, donne",
           "punctuation", "high",
           r"qui, composé avec $\pi_{X/S}$, donne", r"qui composé avec $\pi_{X/S}$ donne",
           "The TeX adds two commas."))
L.append(F(443, "diagram of n° 2, middle node of the top row (printed at the top of p. 444; the diagram stands under "
                "the folio-443 marker)",
           "X^{(p)}  (X <- X^{(p)} <- X)", r"\node (XM) at (3.0,2.0) {$X^{(p/S)}$};",
           "formula", "high",
           r"(3.0,2.0) {$X^{(p/S)}$}", r"(3.0,2.0) {$X^{(p)}$}",
           "The diagram prints the short form X^{(p)} (which the text allows: 'ou même par X^{(p)}'). Filed under p. "
           "443, where the diagram stands now: apply before the marker move of p. 444."))
L.append(F(443, "diagram of n° 2, full stop after it (printed on p. 444)",
           "a full stop to the right of the bottom row (S <- S)", r"\end{tikzpicture} with no full stop",
           "punctuation", "high",
           r"\end{tikzpicture}", r"\end{tikzpicture}.",
           "The TeX drops the full stop that ends the diagram. Filed under p. 443, where the diagram stands now: apply "
           "before the marker move of p. 444."))

# ---------------- page 444 ----------------
L.append(F(444, "top of the page: the diagram of n° 2 (X <- X^{(p)} <- X over S <- S, with fr_X, g, g^{(p)})",
           "p. 444 begins with the diagram, then 'Il est clair que X^{(p/S)} dépend fonctoriellement'; p. 443 ends with "
           "'... où le carré est cartésien :' and the rest of p. 443 is blank",
           "the display '\\[ \\begin{tikzpicture} ... \\end{tikzpicture} \\]' is the end of page_443.tex; the folio-444 "
           "marker stands before 'Il est'",
           "marker", "high", None, None,
           "Page 444 really begins at the '\\[' that opens the tikzpicture (diplomatic s5.tex line 14884, current 14880 "
           "at the time of the check). Exact fix: python -I move_marker.py 5 444 '\\[' --before (simulated in memory on "
           "both layers: the last '\\[' before the marker is the tikzpicture's; the marker moves to its own line between "
           "'cartésien:' and '\\['). Apply the two diagram edits filed under p. 443 first. Text not moved."))
L.append(F(444, "display p_S : X ~> X^{(p/S)}",
           "a wavy arrow (hand-drawn squiggle with an arrowhead)", r"p_S:X\longmapsto X^{(p/S)}",
           "symbol", "high",
           r"\longmapsto", r"\rightsquigarrow",
           "The functor arrow is the wavy arrow; s5.tex writes it \\rightsquigarrow elsewhere (Exposé VIII)."))
L.append(F(444, "'montre que si X est muni'",
           "montre que si  X", r"montre que, si $X$",
           "punctuation", "high",
           r"montre que, si", r"montre que si",
           "The TeX adds a comma."))
L.append(F(444, "'structure algébrique (par exemple : groupe, algèbre, etc.), X^{(p/S)}'",
           "algébrique (par exemple : groupe, algèbre, etc.),  X^{(p/S)}",
           r"algébrique, par exemple groupe, algèbre, etc., $X^{(p/S)}$",
           "punctuation", "high",
           r"algébrique, par exemple groupe, algèbre, etc., $X", r"algébrique (par exemple : groupe, algèbre, etc.), $X",
           "The TeX writes commas for the print's parentheses and drops the colon after 'exemple'."))
L.append(F(444, "Définition 3, first two lines",
           "Soient (u.)  S  un préschéma de caractéristique (u.)  p  et (u.)  X  un (u.)  S -préschéma (u., from the p). "
           "On dit que le (u.)  S -morphisme (u.)",
           r"Soient $S$ un préschéma de caractéristique $p$ et $X$ un $S$-préschéma. On dit que le $S$-morphisme",
           "underline", "high",
           r"Soient $S$ un préschéma de caractéristique $p$ et $X$ un $S$-préschéma. On dit que le $S$-morphisme",
           r"\emph{Soient} $S$ \emph{un préschéma de caractéristique} $p$ \emph{et} $X$ \emph{un} $S$-\emph{préschéma}. \emph{On dit que le} $S$-\emph{morphisme}",
           "Underlined statement; the underline leaves out the letters, the hyphens and the full stop."))
L.append(F(444, "Définition 3, last line",
           "est le morphisme de Frobenius de (u.)  X  relativement à (u.)  S  .",
           r"est le morphisme de Frobenius de $X$ relativement à $S$.",
           "underline", "high",
           r"est le morphisme de Frobenius de $X$ relativement à $S$.",
           r"\emph{est le morphisme de Frobenius de} $X$ \emph{relativement à} $S$.",
           "Underlined statement."))
L.append(F(444, "last line of the page: 'sont énoncées dans la proposition suivante :'",
           "suivante :", "suivante.",
           "punctuation", "high",
           r"proposition suivante.", r"proposition suivante :",
           "Full stop for the print's colon."))

# ---------------- page 445 ----------------
L.append(F(445, "top of the page: 'Proposition 1.'",
           "p. 445 begins with 'Proposition 1.' (underlined), then 'a) (transitivité) Soient S ...'; p. 444 ends with "
           "'dans la proposition suivante :'",
           "'\\begin{statement}{Proposition 1}', '\\begin{enumerate}[label=\\alph*)]' and '\\item' are the last lines "
           "of page_444.tex, above the folio-445 marker",
           "marker", "high", None, None,
           "Page 445 really begins at '\\begin{statement}{Proposition 1}' (diplomatic s5.tex line 14924, current 14920 "
           "at the time of the check). Exact fix: python -I move_marker.py 5 445 '\\begin{statement}{Proposition 1}' "
           "--before (simulated in memory on both layers: the marker moves back three lines). Text not moved."))
L.append(F(445, "Proposition 1 a), the label of the item",
           "(transitivité)  (small t, no full stop, not underlined)", r"\emph{(Transitivité.)}",
           "word", "high",
           r"\emph{(Transitivité.)}", r"(transitivité)",
           "The TeX capitalizes, adds a full stop and sets the label with \\emph (this file's mark for underlining); the "
           "print has a plain '(transitivité)'."))
L.append(F(445, "Proposition 1 a), statement",
           "Soient (u.)  S  un préschéma de caractéristique (u.)  p  et (u.)  g : X -> Y  un (u.)  S -morphisme de (u.)  "
           "S -préschémas (u.).  Le diagramme suivant est commutatif et ses trois carrés sont cartésiens (u.)  :",
           r"Soient $S$ un préschéma de caractéristique $p$ et $g:X\to Y$ un $S$-morphisme de $S$-préschémas. Le diagramme suivant est commutatif et ses trois carrés sont cartésiens:",
           "underline", "high",
           r"Soient $S$ un préschéma de caractéristique $p$ et $g:X\to Y$ un $S$-morphisme de $S$-préschémas. Le diagramme suivant est commutatif et ses trois carrés sont cartésiens",
           r"\emph{Soient} $S$ \emph{un préschéma de caractéristique} $p$ \emph{et} $g:X\to Y$ \emph{un} $S$-\emph{morphisme de} $S$-\emph{préschémas}. \emph{Le diagramme suivant est commutatif et ses trois carrés sont cartésiens}",
           "Underlined statement."))
L.append(F(445, "diagram of Proposition 1 a), full stop after it",
           "a full stop to the right of the bottom row (S <- S)", r"\end{tikzcd} with no full stop",
           "punctuation", "high",
           r"\end{tikzcd}", r"\end{tikzcd}.",
           "The TeX drops the full stop that ends the diagram. (Label sides of the lower horizontal arrows: volume "
           "decision, GLOBAL_ISSUES 85, not itemized.)"))
L.append(F(445, "Proposition 1 b), the label of the item",
           "(changement de base)  (small c, no full stop, not underlined)", r"\emph{(Changement de base.)}",
           "word", "high",
           r"\emph{(Changement de base.)}", r"(changement de base)",
           "As '(transitivité)': capital, full stop and \\emph added by the TeX."))
L.append(F(445, "Proposition 1 b), first line",
           "Soient (u.)  g : S' -> S  un morphisme de / préschémas de caractéristique (u.)  p  et (u.)",
           r"Soient $g:S'\to S$ un morphisme de préschémas de caractéristique $p$ et",
           "underline", "high",
           r"Soient $g:S'\to S$ un morphisme de préschémas de caractéristique $p$ et",
           r"\emph{Soient} $g:S'\to S$ \emph{un morphisme de préschémas de caractéristique} $p$ \emph{et}",
           "Underlined statement. The old stops before '$C$' (misprint item below), so the same edit fits the corrected "
           "layer."))
L.append(F(445, "Proposition 1 b), 'et C un S-préschéma'",
           "C", r"$C$",
           "misprint_in_print", "high", None, None,
           "C for X (the S-préschéma is X in the rest of b)). The TeX keeps the printed reading; the corrected layer "
           "(current/s5.tex) already reads $X$.",
           corrected=r"$X$"))
L.append(F(445, "Proposition 1 b), 'un S-préschéma. On a un isomorphisme canonique'",
           "un (u.)  S -préschéma (u.).  On a un / isomorphisme canonique (u.)",
           r"un $S$-préschéma. On a un isomorphisme canonique",
           "underline", "high",
           r"un $S$-préschéma. On a un isomorphisme canonique",
           r"\emph{un} $S$-\emph{préschéma}. \emph{On a un isomorphisme canonique}",
           "Underlined statement."))
L.append(F(445, "Proposition 1 b), colon after 'isomorphisme canonique'",
           "isomorphisme canonique :  X^{(p/S)} x_S S' ≃ ...", "isomorphisme canonique, then the display, no colon",
           "punctuation", "high",
           r"⏎\[⏎X^{(p/S)}\times_S S'", r" :⏎\[⏎X^{(p/S)}\times_S S'",
           "The TeX drops the colon. Independent of the underline edit before it (the old starts at the line break after "
           "'canonique')."))
L.append(F(445, "Proposition 1 b), after the first display",
           "fonctoriel / en (u.)  X , soit (u.)  (X^{(p/S)})' ≃ X'^{(p/S')}  en affectant d'un (u.)  '  le résultat du "
           "changement de base par (u.)  g ;  de plus (u.)",
           r"fonctoriel en $X$, soit $(X^{(p/S)})'\simeq X'{}^{(p/S')}$ en affectant d'un $'$ le résultat du changement de base par $g$; de plus",
           "underline", "high",
           r"fonctoriel en $X$, soit $(X^{(p/S)})'\simeq X'{}^{(p/S')}$ en affectant d'un $'$ le résultat du changement de base par $g$; de plus",
           r"\emph{fonctoriel en} $X$, \emph{soit} $(X^{(p/S)})'\simeq X'{}^{(p/S')}$ \emph{en affectant d'un} $'$ \emph{le résultat du changement de base par} $g$; \emph{de plus}",
           "Underlined statement."))
L.append(F(445, "Proposition 1 b), last line",
           "modulo l'identification permise par l'isomorphisme précédent (u.) .",
           r"modulo l'identification permise par l'isomorphisme précédent.",
           "underline", "high",
           r"modulo l'identification permise par l'isomorphisme précédent.",
           r"\emph{modulo l'identification permise par l'isomorphisme précédent}.",
           "Underlined statement."))
L.append(F(445, "Proposition 2, first sentence",
           "Soient (u.)  S  un préschéma de caractéristique (u.)  p  et (u.)  X / un  S -préschéma.  (the second line "
           "is not underlined)",
           r"Soient $S$ un préschéma de caractéristique $p$ et $X$ un $S$-préschéma.",
           "underline", "high",
           r"Soient $S$ un préschéma de caractéristique $p$ et $X$ un $S$-préschéma.",
           r"\emph{Soient} $S$ \emph{un préschéma de caractéristique} $p$ \emph{et} $X$ un $S$-préschéma.",
           "Underlined statement; the typist left 'un S-préschéma.' on the second line without underline."))
L.append(F(445, "Proposition 2 a), first words",
           "Le morphisme de Frobenius relatif (u.)", r"\item Le morphisme de Frobenius relatif",
           "underline", "high",
           r"\item Le morphisme de Frobenius relatif", r"\item \emph{Le morphisme de Frobenius relatif}",
           "Underlined statement."))
L.append(F(445, "Proposition 2 a), after the display",
           "est / entier surjectif et radiciel (u.)  (donc c'est un homéomorphisme universel (u.)).",
           r"est entier, surjectif et radiciel, donc c'est un homéomorphisme universel.",
           "punctuation", "high",
           r"est entier, surjectif et radiciel, donc c'est un homéomorphisme universel.",
           r"\emph{est entier surjectif et radiciel} (\emph{donc c'est un homéomorphisme universel}).",
           "The TeX adds a comma after 'entier' and writes a comma for the print's parentheses. The new text also "
           "carries the underline of the statement (parentheses and full stop outside it)."))

# ---------------- checks ----------------
ok = True
texts = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(441, 446)}
spans = {}
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    t = texts[d["page"]]
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", n, d["page"], repr(fx["old"]))
        continue
    k = t.find(fx["old"])
    if "%%%%%%%%%%" in fx["old"]:
        ok = False
        print("MARKER IN OLD", d["page"], repr(fx["old"]))
    spans.setdefault(d["page"], []).append((k, k + len(fx["old"]), i))
# overlapping olds on the same page
for p, sp in spans.items():
    sp.sort()
    for a, b in zip(sp, sp[1:]):
        if b[0] < a[1]:
            print("OVERLAP p.", p, repr(L[a[2]]["fix"]["old"][:40]), "|", repr(L[b[2]]["fix"]["old"][:40]))
# apply the fixes in listed order: each old must be unique in the text at its turn
for pg in range(441, 446):
    t2 = texts[pg]
    for d in L:
        if d["page"] != pg or d["fix"] is None:
            continue
        n = t2.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL NOT UNIQUE", n, pg, repr(d["fix"]["old"][:50]))
            continue
        t2 = t2.replace(d["fix"]["old"], d["fix"]["new"], 1)
print("all olds unique:", ok)
counts = {}
for d in L:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print(counts, len(L))
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
