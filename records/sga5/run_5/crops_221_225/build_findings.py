"""Build findings_221_225.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b221_225"
OUT = RUN / "findings_221_225.json"
NL = "\n"


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------------------------------------------------------- page 221
L.append(F(221, "top of the page: label of the proof of Proposition 3.2.1",
           "the page begins with the proof label 'Preuve :' (Preuve underlined)",
           "the marker splits \\begin{prooftext}[Preuve]: '\\begin{prooftext}[' is the last line of folio 220's text, 'Preuve]' the first line under the folio 221 marker",
           "marker", "high", None, None,
           "The page really begins with this proof label. Resolved without moving the marker when the two label fixes below are applied together with deleting the line '\\begin{prooftext}[' just above the marker (s5.tex line 7381, folio 220's text). If the environment is kept instead, move the marker before '\\begin{prooftext}[' (move_marker.py 5 221 \"\\begin{prooftext}[\" --before)."))
L.append(F(221, "proof of Proposition 3.2.1, label",
           "Preuve : Il nous faut montrer",
           "\\begin{prooftext}[Preuve] (renders 'Preuve.' with a full stop)",
           "punctuation", "high",
           "Preuve]" + NL + "Il nous faut",
           r"\emph{Preuve} : Il nous faut",
           "Another form of the proof label: the prooftext environment of Expose V prints 'Preuve.'; the print has 'Preuve :', the file's form \\emph{Preuve} :. Must be applied together with the next fix and with deleting '\\begin{prooftext}[' at the end of folio 220's text (s5.tex line 7381); applied alone it leaves that opening unclosed."))
L.append(F(221, "end of the proof of Proposition 3.2.1",
           "d'où l'assertion. (no environment)",
           "d'où l'assertion. \\end{prooftext}",
           "other", "high",
           "d'où l'assertion." + NL + r"\end{prooftext}",
           "d'où l'assertion.",
           "Goes with the previous fix (the environment is replaced by the run-in label \\emph{Preuve} :)."))
L.append(F(221, "proof of 3.2.1, second sentence",
           "est représenté pour un certain entier r par un AR-isomorphisme",
           "est représenté, pour un certain entier $r$, par un AR-isomorphisme",
           "punctuation", "high",
           r"est représenté, pour un certain entier $r$, par",
           r"est représenté pour un certain entier $r$ par",
           "Two commas added by the TeX."))
L.append(F(221, "Définition 3.2.2, first sentence",
           "underlined: 'Un système projectif indexé par' | 'à valeurs dans' | 'est appelé' | 'adique si'; not underlined: N, C, 'AR-J-', ' :'",
           "no underline markup",
           "underline", "high",
           r"Un système projectif indexé par $\NN$ à valeurs dans $\cC$ est appelé AR-$J$-adique si:",
           r"\emph{Un système projectif indexé par} $\NN$ \emph{à valeurs dans} $\cC$ \emph{est appelé} AR-$J$-\emph{adique si}:",
           "Expose V statements have no underline markup in the TeX; \\emph is the file's command for the print's underline (as on the first Expose V pages, s5.tex lines 6870-6902)."))
L.append(F(221, "Définition 3.2.2 (a)",
           "J^{n+1}X_n = 0 pour tout n >= 0 ('pour tout' underlined)",
           "no underline",
           "underline", "high",
           r"\item $J^{n+1}X_n=0$ pour tout",
           r"\item $J^{n+1}X_n=0$ \emph{pour tout}",
           ""))
L.append(F(221, "Définition 3.2.2 (a), end",
           "n >= 0 ,",
           "$n\\ge0$;",
           "punctuation", "high",
           r"$n\ge0$;",
           r"$n\ge0$,",
           "The print ends item (a) with a comma, not a semicolon."))
L.append(F(221, "Définition 3.2.2 (b)",
           "underlined: 'il vérifie les conditions équivalentes' | 'et' | 'de la propo-sition'; (i), (ii) not",
           "no underline",
           "underline", "high",
           r"il vérifie les conditions équivalentes (i) et (ii) de la proposition",
           r"\emph{il vérifie les conditions équivalentes} (i) \emph{et} (ii) \emph{de la proposition}",
           ""))
L.append(F(221, "Définition 3.2.2 (b), reference",
           "de la proposition (3.2.1) .",
           "de la proposition 3.2.1.",
           "punctuation", "high",
           "3.2.1." + NL + r"\end{enumerate}",
           "(3.2.1)." + NL + r"\end{enumerate}",
           "The print writes the reference in parentheses."))
L.append(F(221, "Proposition 3.2.3, first two sentences",
           "underlined: 'Soit' | 'un système projectif indexé par' | 'à valeurs' 'dans' | 'On suppose que' | 'pour tout'; X, N, C, the formula and n >= 0 not",
           "no underline markup",
           "underline", "high",
           r"Soit $X$ un système projectif indexé par $\NN$ à valeurs dans $\cC$. On suppose que $J^{n+1}X_n=0$ pour tout",
           r"\emph{Soit} $X$ \emph{un système projectif indexé par} $\NN$ \emph{à valeurs dans} $\cC$. \emph{On suppose que} $J^{n+1}X_n=0$ \emph{pour tout}",
           ""))
L.append(F(221, "Proposition 3.2.3, 'Alors pour que'",
           "Alors pour que X (no comma; 'Alors pour que' underlined)",
           "Alors, pour que $X$",
           "punctuation", "high",
           "Alors, pour que",
           r"\emph{Alors pour que}",
           "Comma added by the TeX; the fix also gives the print's underline of these words (part of the statement's underline)."))
L.append(F(221, "Proposition 3.2.3, rest of the statement",
           "underlined: 'soit' | 'adique, il faut et il suffit qu'il vérifie la propriété' | 'et que, désignant par' | 'son système projectif des images universelles,' 'il existe un entier' | 'tel que, pour tout couple' | 'd'entiers avec' | 'le \"morphisme de transition\" ci-dessous soit un isomorphisme'; AR-J-, (MLAR), X', r >= 0, (m,n), m >= n+r and ' :' not",
           "no underline markup",
           "underline", "high",
           r"soit AR-$J$-adique, il faut et il suffit qu'il vérifie la propriété (MLAR) et que, désignant par $X'$ son système projectif des images universelles, il existe un entier $r\ge0$ tel que, pour tout couple $(m,n)$ d'entiers avec $m\ge n+r$, le ``morphisme de transition'' ci-dessous soit un isomorphisme:",
           r"\emph{soit} AR-$J$-\emph{adique, il faut et il suffit qu'il vérifie la propriété} (MLAR) \emph{et que, désignant par} $X'$ \emph{son système projectif des images universelles, il existe un entier} $r\ge0$ \emph{tel que, pour tout couple} $(m,n)$ \emph{d'entiers avec} $m\ge n+r$, \emph{le ``morphisme de transition'' ci-dessous soit un isomorphisme}:",
           "The underline runs on across the line break after 'universelles,'."))
L.append(F(221, "proof of 3.2.3 (a)",
           "(a) Les conditions de l'énoncé sont suffisantes : / [new paragraph] Si X vérifie (MLAR) ,",
           "suffisantes: si $X$ vérifie (MLAR),",
           "word", "high",
           r"suffisantes: si $X$ vérifie",
           "suffisantes:" + NL + NL + r"Si $X$ vérifie",
           "The print starts a new indented paragraph with a capital 'Si' (in (b) the 'si' runs on, as in the TeX)."))
L.append(F(221, "proof of 3.2.3 (a), 'Par ailleurs'",
           "Par ailleurs l'hypothèse faite sur X'",
           "Par ailleurs, l'hypothèse",
           "punctuation", "high",
           "Par ailleurs, l'hypothèse",
           "Par ailleurs l'hypothèse",
           "Comma added by the TeX."))
L.append(F(221, "proof of 3.2.3 (a), the system (X'_{n+r}/J^{n+1}X'_{n+r})_{n>=0}",
           "(X'_{n+r}/J^{n+1}X'_{n+r})_{n>=0} (les morphismes de transition étant évidents) est J-adique.",
           "display ending with a comma, then ', les morphismes de transition étant évidents, est'",
           "punctuation", "high",
           r"_{n\ge0}," + NL + r"\]" + NL + "les morphismes de transition étant évidents, est",
           r"_{n\ge0}" + NL + r"\]" + NL + "(les morphismes de transition étant évidents) est",
           "The print has the phrase in parentheses and no comma after the formula (which it runs into the text; the display is kept)."))

# ---------------------------------------------------------------- page 222
L.append(F(222, "top of the page",
           "the page begins 'Le système projectif X' des images universelles de X ...'",
           "'Le' is the last word of folio 221's text (above the marker); folio 222's TeX begins 'système projectif'",
           "marker", "high", None, None,
           "Move the folio 222 marker before that 'Le' (move_marker.py 5 222 \"Le\" --before)."))
L.append(F(222, "first paragraph, 'les deuxième point'",
           "Pour prouver les deuxième point",
           "Pour prouver le deuxième point",
           "misprint_in_print", "high",
           "prouver le deuxième",
           "prouver les deuxième",
           "The typescript has 'les' for 'le'; the TeX silently corrects it.",
           corrected="prouver le deuxième"))
L.append(F(222, "first paragraph, 'ra-mané'",
           "on est donc ra-mané à voir",
           "on est donc ramené à voir",
           "misprint_in_print", "high",
           "ramené",
           "ramané",
           "The typescript has 'ramané' (a for e, across the hyphenation); the TeX silently corrects it.",
           corrected="ramené"))
L.append(F(222, "first paragraph, 'à voir que si'",
           "à voir que si X est un système projectif",
           "à voir que, si $X$ est",
           "punctuation", "high",
           r"voir que, si $X$",
           r"voir que si $X$",
           "Comma added by the TeX."))
L.append(F(222, "first paragraph, 'Soit pour cela u = Y --> X'",
           "Soit pour cela u = Y --> X un AR-isomorphisme (an equals sign)",
           "$u:Y\\to X$",
           "misprint_in_print", "high",
           r"$u:Y\to X$ un AR",
           r"$u=Y\to X$ un AR",
           "The typescript types '=' for ':'; the TeX silently corrects it.",
           corrected=r"$u:Y\to X$ un AR"))
L.append(F(222, "Proposition 3.2.4, title and first word",
           "(Stabilités par suites exactes) . Soit — title inside the parentheses and 'Soit' underlined",
           "label argument 'Proposition 3.2.4 (Stabilités par suites exactes)' and 'Soit' without underline",
           "underline", "high",
           r"(Stabilités par suites exactes)}" + NL + "Soit",
           r"(\emph{Stabilités par suites exactes})}" + NL + r"\emph{Soit}",
           ""))
L.append(F(222, "Proposition 3.2.4, after the exact sequence",
           "underlined: 'une suite exacte de' | 'les systèmes projectifs' | 'et' | 'étant tels que'; P, X, Y, Z not",
           "no underline",
           "underline", "high",
           r"une suite exacte de $P$, les systèmes projectifs $X$, $Y$ et $Z$ étant tels que",
           r"\emph{une suite exacte de} $P$, \emph{les systèmes projectifs} $X$, $Y$ \emph{et} $Z$ \emph{étant tels que}",
           ""))
L.append(F(222, "Proposition 3.2.4 (i) and (ii)",
           "underlined: 'Si', 'vérifie', 'et', 'est', 'adique' (after AR-J-), 'est', 'adique' / 'Si', 'vérifie', 'et', 'est', 'adique', 'vérifie'; letters, (MLAR) and 'AR-J-' not",
           "no underline",
           "underline", "high",
           r"\item Si $X$ vérifie (MLAR) et $Y$ est AR-$J$-adique, $Z$ est AR-$J$-adique." + NL + r"\item Si $Y$ vérifie (MLAR) et $Z$ est AR-$J$-adique, $X$ vérifie (MLAR).",
           r"\item \emph{Si} $X$ \emph{vérifie} (MLAR) \emph{et} $Y$ \emph{est} AR-$J$-\emph{adique}, $Z$ \emph{est} AR-$J$-\emph{adique}." + NL + r"\item \emph{Si} $Y$ \emph{vérifie} (MLAR) \emph{et} $Z$ \emph{est} AR-$J$-\emph{adique}, $X$ \emph{vérifie} (MLAR).",
           ""))
L.append(F(222, "proof of 3.2.4, label of part (i)",
           "Preuve de (i) : Si X' et Y' ('Preuve de' underlined)",
           "Preuve de (i). Si",
           "punctuation", "high",
           "Preuve de (i). Si",
           r"\emph{Preuve de} (i) : Si",
           "Another form of the proof label: the print has ' :' after (i), not a full stop, and underlines 'Preuve de'."))
L.append(F(222, "diagram of the proof of (i), vertical arrows X' -> X and Y' -> Y",
           "hooked arrows (inclusions); the third vertical arrow is plain",
           "\\arrow[d] (plain) for all three",
           "symbol", "high",
           r"X' \arrow[r] \arrow[d] & Y' \arrow[r] \arrow[d]",
           r"X' \arrow[r] \arrow[d,hook] & Y' \arrow[r] \arrow[d,hook]",
           "The file writes hooked arrows as \\arrow[d,hook] elsewhere."))
L.append(F(222, "diagram of the proof of (i), top row",
           "Z~' (tilde Z with a prime); p. 223 then writes 'le morphisme Z~ --> Z' without the prime",
           "\\widetilde{Z'} here and \\widetilde Z on p. 223, as printed",
           "misprint_in_print", "low",
           None, None,
           "Inconsistent notation in the print: the same object is Z~' in the diagram and Z~ in the text (the parallel part (ii) on p. 223 uses X~ without a prime). The TeX keeps both printed readings; the corrected edition should use one name (Z~ assumed here).",
           corrected=r"\widetilde{Z}"))

# ---------------------------------------------------------------- page 223
L.append(F(223, "top of the page",
           "the page begins with the displayed functor 'P_AR : P --> P_AR', then 'est exact, il résulte de ce diagramme'",
           "'$P_{AR}\\colon P\\to P_{AR}$ est' is at the end of folio 222's text (above the marker); folio 223's TeX begins 'exact, il résulte'",
           "marker", "high", None, None,
           "Move the folio 223 marker before '$P_{AR}\\colon P\\to P_{AR}$' (move_marker.py 5 223 \"$P_{AR}\\colon P\\to P_{AR}$\" --before). The print sets the functor as a display (layout, not reported)."))
L.append(F(223, "first diagram of (ii), vertical arrows Y' -> Y and Z' -> Z",
           "hooked arrows (the two inclusions); X~ -> X plain",
           "\\arrow[d] (plain) for all three",
           "symbol", "high",
           r"Y' \arrow[r] \arrow[d] & Z' \arrow[r] \arrow[d]",
           r"Y' \arrow[r] \arrow[d,hook] & Z' \arrow[r] \arrow[d,hook]",
           "The text calls them 'les inclusions canoniques'."))
L.append(F(223, "first diagram of (ii), bottom row labels",
           "u and v above the arrows X --> Y --> Z",
           "\"u\"' and \"v\"' (swapped: set below the arrows)",
           "other", "medium",
           r'''X \arrow[r,"u"'] & Y \arrow[r,"v"'] & Z \arrow[r] & 0 .''',
           r'''X \arrow[r,"u"] & Y \arrow[r,"v"] & Z \arrow[r] & 0 .''',
           "Label position in the diagram."))
L.append(F(223, "second diagram of (ii), bottom row labels",
           "u and v above the arrows X --> Y --> Z",
           "\"u\"' and \"v\"' (swapped: set below the arrows)",
           "other", "medium",
           r'''X \arrow[r,"u"'] & Y \arrow[r,"v"'] & Z \arrow[r] & 0,''',
           r'''X \arrow[r,"u"] & Y \arrow[r,"v"] & Z \arrow[r] & 0,''',
           "Label position in the diagram."))
L.append(F(223, "after the second diagram",
           "dans lequel comme précédemment X~~ --> X est un AR-isomorphisme",
           "dans lequel, comme précédemment, $\\widetilde{\\widetilde X}\\to X$",
           "punctuation", "high",
           r"dans lequel, comme précédemment, $",
           r"dans lequel comme précédemment $",
           "Two commas added by the TeX."))
L.append(F(223, "last line, 'et ou Z est J-adique'",
           "au cas où Y est strict et ou Z est J-adique (no grave accent on the second 'ou')",
           "et où $Z$",
           "misprint_in_print", "medium",
           r"et où $Z$",
           r"et ou $Z$",
           "The accent of 'où' is absent in the print (the 'où' earlier on the line is clear); the TeX silently corrects it.",
           corrected=r"et où $Z$"))

# ---------------------------------------------------------------- page 224
L.append(F(224, "top of the page",
           "the page begins '(3.1.3 (ii)) permet de conclure.'",
           "'(3.1.3 (ii))' is the last item of folio 223's text ('Alors (3.1.3 (ii))', above the marker); folio 224's TeX begins 'permet de conclure.'",
           "marker", "high", None, None,
           "Move the folio 224 marker before '(3.1.3 (ii))' (move_marker.py 5 224 \"(3.1.3 (ii))\" --before)."))
L.append(F(224, "heading 4",
           "4. Filtrations et graduations. (title underlined, with a full stop)",
           "\\subsection*{4. Filtrations et graduations}",
           "punctuation", "high",
           r"\subsection*{4. Filtrations et graduations}",
           r"\subsection*{4. Filtrations et graduations.}",
           "Underlined title ending with a full stop in the print."))
L.append(F(224, "heading 4.1",
           "4.1. Généralités. (title underlined, with a full stop)",
           "\\subsubsection*{4.1. Généralités}",
           "punctuation", "high",
           r"\subsubsection*{4.1. Généralités}",
           r"\subsubsection*{4.1. Généralités.}",
           "Underlined title ending with a full stop in the print."))
L.append(F(224, "4.1.1, before the definition of F^pX",
           "dans la catégorie P_1 = Hom(Z°,C) en posant :",
           "en posant (no colon)",
           "punctuation", "high",
           "en posant" + NL + r"\[",
           "en posant:" + NL + r"\[",
           ""))
L.append(F(224, "4.1.1, definition of (F^pX)_n",
           "{ Ker(X_n --> X_{p-1})  si n >= p-1  /  0  si n < p-1 ,",
           "\\Ker(X_n\\to X_{p-1}),& n\\ge p-1,\\\\ 0,& n<p-1,",
           "formula", "high",
           r"\Ker(X_n\to X_{p-1}),& n\ge p-1,\\" + NL + r"0,& n<p-1,",
           r"\Ker(X_n\to X_{p-1})& \text{si } n\ge p-1\\" + NL + r"0& \text{si } n<p-1,",
           "The print writes 'si' before both conditions and has no comma after Ker(...), after 'n >= p-1' or after 0; the final comma is printed."))
L.append(F(224, "paragraph 'Par ailleurs'",
           "ci-dessous prouve que dès que n >= p ,",
           "prouve que, dès que $n\\ge p$,",
           "punctuation", "high",
           "prouve que, dès que",
           "prouve que dès que",
           "Comma added by the TeX."))
L.append(F(224, "paragraph 'Par ailleurs', before the display",
           "le morphisme canonique :",
           "le morphisme canonique (no colon)",
           "punctuation", "high",
           "le morphisme canonique" + NL + r"\[",
           "le morphisme canonique:" + NL + r"\[",
           ""))
L.append(F(224, "after the display F^pX_n/F^{p+1}X_n --> ...",
           "est un isomorphisme.",
           "est un isomorphisme:",
           "punctuation", "high",
           "est un isomorphisme:",
           "est un isomorphisme.",
           "The print ends the sentence with a full stop before the diagram (D)."))
L.append(F(224, "diagram (D), bottom row",
           "the tilde (~) above the arrow X_{p-1} --> X_{p-1}",
           "\"\\sim\"' (swapped: set below the arrow)",
           "other", "medium",
           r'''X_{p-1} \arrow[r,"\sim"'] & X_{p-1}''',
           r'''X_{p-1} \arrow[r,"\sim"] & X_{p-1}''',
           "Label position in the diagram."))

# ---------------------------------------------------------------- page 225
L.append(F(225, "display P = Hom(N°, C)",
           "P = Hom(N°,C) with Hom underlined",
           "P=\\Hom(\\NN^\\circ,\\cC)",
           "underline", "high",
           r"P=\Hom(\NN^\circ,\cC)",
           r"P=\uHom(\NN^\circ,\cC)",
           "The file's macro for the underlined Hom is \\uHom (used in Expose V at s5.tex line 6910). On p. 224 'P_1 = Hom(Z°,C)' is not underlined, as in the TeX."))
L.append(F(225, "Définition 4.1.2",
           "underlined: 'Soit' | 'un système projectif indexé par' | 'On dit que' | 'est essentiellement constant s'il existe un entier' | 'tel que, pour tout' 'couple' | 'd'entiers supérieurs ou égaux à' | 'et vérifiant l'inégalité' | 'le morphisme de transition'; X, Z, p, (r,s), s >= r not",
           "no underline markup",
           "underline", "high",
           r"Soit $X$ un système projectif indexé par $\ZZ$. On dit que $X$ est essentiellement constant s'il existe un entier $p$ tel que, pour tout couple $(r,s)$ d'entiers supérieurs ou égaux à $p$ et vérifiant l'inégalité $s\ge r$, le morphisme de transition",
           r"\emph{Soit} $X$ \emph{un système projectif indexé par} $\ZZ$. \emph{On dit que} $X$ \emph{est essentiellement constant s'il existe un entier} $p$ \emph{tel que, pour tout couple} $(r,s)$ \emph{d'entiers supérieurs ou égaux à} $p$ \emph{et vérifiant l'inégalité} $s\ge r$, \emph{le morphisme de transition}",
           ""))
L.append(F(225, "Définition 4.1.2, after the display",
           "'soit un isomorphisme.' underlined; then a new paragraph 'Il est clair qu'il suffit ...' not underlined",
           "no underline",
           "underline", "high",
           "soit un isomorphisme. Il est clair",
           r"\emph{soit un isomorphisme}. Il est clair",
           ""))
L.append(F(225, "Proposition 4.1.3, title",
           "(Propriété (MLAR) et gradués) — 'Propriété' and 'et gradués' underlined, (MLAR) not",
           "label argument without underline",
           "underline", "high",
           r"(Propriété (MLAR) et gradués)}",
           r"(\emph{Propriété} (MLAR) \emph{et gradués})}",
           ""))
L.append(F(225, "Proposition 4.1.3, first sentence",
           "underlined: 'Les assertions suivantes' 'pour un objet' | 'de la catégorie' | 'sont équivalentes'; X, P and ' :' not",
           "no underline",
           "underline", "high",
           r"Les assertions suivantes pour un objet $X$ de la catégorie $P$ sont équivalentes:",
           r"\emph{Les assertions suivantes pour un objet} $X$ \emph{de la catégorie} $P$ \emph{sont équivalentes}:",
           ""))
L.append(F(225, "Proposition 4.1.3 (i) and the first line of (ii)",
           "(i) X vérifie (MLAR) . ('vérifie' underlined); (ii) 'Le système projectif à valeurs dans la catégorie des objets gradués' 'par' | 'de' underlined, N not",
           "no underline",
           "underline", "high",
           r"\item $X$ vérifie (MLAR)." + NL + r"\item Le système projectif à valeurs dans la catégorie des objets gradués par $\NN$ de",
           r"\item $X$ \emph{vérifie} (MLAR)." + NL + r"\item \emph{Le système projectif à valeurs dans la catégorie des objets gradués par} $\NN$ \emph{de}",
           ""))
L.append(F(225, "Proposition 4.1.3 (ii), before the display",
           "par N de C :",
           "de $\\cC$ (no colon)",
           "punctuation", "high",
           r" $\cC$" + NL + r"\[" + NL + r"r\longmapsto",
           r" $\cC$:" + NL + r"\[" + NL + r"r\longmapsto",
           ""))
L.append(F(225, "Proposition 4.1.3, end of (ii) and first line of (iii)",
           "'où les morphismes de transition sont évidents, est essentiellement constant' underlined; (iii) as (ii)",
           "no underline",
           "underline", "high",
           "où les morphismes de transition sont évidents, est essentiellement constant." + NL + r"\item Le système projectif à valeurs dans la catégorie des objets gradués par $\NN$ de",
           r"\emph{où les morphismes de transition sont évidents, est essentiellement constant}." + NL + r"\item \emph{Le système projectif à valeurs dans la catégorie des objets gradués par} $\NN$ \emph{de}",
           ""))
L.append(F(225, "Proposition 4.1.3 (iii), before the display",
           "par N de C :",
           "de $\\cC$ (no colon)",
           "punctuation", "high",
           r" $\cC$" + NL + r"\[" + NL + r"n\longmapsto",
           r" $\cC$:" + NL + r"\[" + NL + r"n\longmapsto",
           ""))
L.append(F(225, "Proposition 4.1.3, end of (iii)",
           "'où les morphismes de transition sont évidents, vérifie' underlined, (MLAR) not",
           "no underline",
           "underline", "high",
           "où les morphismes de transition sont évidents, vérifie (MLAR).",
           r"\emph{où les morphismes de transition sont évidents, vérifie} (MLAR).",
           ""))
L.append(F(225, "proof of 4.1.3, (i) => (ii)",
           "Preuve : (i) => (ii) : résulte de",
           "$(i)\\Rightarrow(ii)$ résulte (no colon)",
           "punctuation", "high",
           r"$(i)\Rightarrow(ii)$ résulte",
           r"$(i)\Rightarrow(ii)$ : résulte",
           ""))
L.append(F(225, "proof of 4.1.3, (i) => (ii), reference",
           "donnée en (4.1.1) .",
           "donnée en 4.1.1.",
           "punctuation", "high",
           "donnée en 4.1.1.",
           "donnée en (4.1.1).",
           "The print writes the reference in parentheses."))
L.append(F(225, "proof of 4.1.3, (ii) => (iii)",
           "(ii) => (iii) : Soit r",
           "$(ii)\\Rightarrow(iii)$. Soit",
           "punctuation", "high",
           r"$(ii)\Rightarrow(iii)$. Soit",
           r"$(ii)\Rightarrow(iii)$ : Soit",
           "The print has ' :' after the implication, not a full stop."))
L.append(F(225, "proof of 4.1.3, (ii) => (iii), last line",
           "tel que pour tout s > r et tout p le morphisme canonique",
           "tel que, pour tout $s>r$ et tout $p$, le morphisme canonique",
           "punctuation", "high",
           r"tel que, pour tout $s>r$ et tout $p$, le morphisme",
           r"tel que pour tout $s>r$ et tout $p$ le morphisme",
           "Two commas added by the TeX."))

# ---------------------------------------------------------------- checks
texts = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(221, 226)}
bad = 0
for i, x in enumerate(L):
    fx = x["fix"]
    if fx is None:
        continue
    t = texts[x["page"]]
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", i, x["page"], n, repr(fx["old"][:80]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        bad += 1
        print("MARKER IN FIX", i)
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO CHANGE", i)
# overlapping olds on one page
for p in range(221, 226):
    spans = []
    for i, x in enumerate(L):
        if x["page"] == p and x["fix"]:
            k = texts[p].find(x["fix"]["old"])
            spans.append((k, k + len(x["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP on page", p, a, b)
counts = {}
for x in L:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("counts", counts, "bad", bad)
if bad == 0 or "--force" in sys.argv:
    OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT, len(L))
