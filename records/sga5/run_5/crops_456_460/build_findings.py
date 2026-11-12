"""Build findings_456_460.json. Checks: every fix's old occurs once in this batch's page file (the lines printed at
the top of p. 456: in b451_455/page_455.tex, where the batch files have them) and once in the live span of its page
(both layers); the fixes of each page applied in listed order to the live spans (corrected layer without the
misprint fixes); and after the simulated moves of the folio-457 and folio-460 markers each old is still once on its
page or, for the diagram printed on p. 460, once on p. 460."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
RUN = W / "run_5"
OUT = RUN / "findings_456_460.json"
sys.path.insert(0, str(HERE))
from sim_markers import MARK, move  # noqa: E402


def pfile(n):
    d = "b451_455" if n <= 455 else "b456_460" if n <= 460 else "b461_465"
    return RUN / d / f"page_{n:03d}.tex"


F = []
MOVED = []  # indices of findings whose old sits in b451_455/page_455.tex in the batch files


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None, moved=False):
    x = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        x["corrected"] = corrected
    x["note"] = note
    if moved:
        MOVED.append(len(F))
    F.append(x)


MV457 = "python -I move_marker.py 5 457 '\\item' --before"
MV460 = "python -I move_marker.py 5 460 \"$(printf '%s\\n%s' '\\[' '\\resizebox')\" --before"
P456 = ("Printed at the top of p. 456. In this batch's page files the line is still the end of page_455.tex; in the "
        "live s5.tex (folio-456 marker moved by batch 451-455) it stands under the folio-456 marker, where the old "
        "occurs once (both layers).")
P460 = ("Printed on p. 460; filed under p. 459 because the diagram stands in page_459.tex until the folio-460 marker "
        "is moved (marker finding of p. 460): apply before the move. The old is also once on p. 460 after the move.")

# ---------------------------------------------------------------- p. 456
add(456, "top of the page / folio-456 marker",
    "p. 456 begins 'et φ_F(U) : F(U) --> F(U) à l'application : s ~~> φ_{F|U} o s = s o φ_U (s ∈ Hom_U(U,F|U)) ; "
    "comme le faisceau final U de Ũ_ét ...'; p. 455 ends '... on sait que F(U) s'identifie à Hom_U(U,F|U)' "
    "(b451_455/page_455_s4.png)",
    "batch files: 'et $\\varphi_F(U):F(U)\\to F(U)$ à l'application', the display s\\longmapsto ..., 'où "
    "$s\\in\\Hom_U(U,F|U)$; comme le' end page_455.tex; page_456.tex begins 'faisceau final $U$'",
    "marker", "high", None, None,
    "Page 456 really begins at 'et $\\varphi_F(U)'. Already done in both live layers (reported by batch 451-455; "
    "the marker now stands on its own line before 'et $\\varphi_F(U)', diplomatic line 15294, current 15290): "
    "nothing to run. Batch 451-455 left the moved lines unchecked; their four differences follow, filed under "
    "p. 456 where the live file has them.")
add(456, "first line: 'à l'application :'",
    "et φ_F(U) : F(U) --> F(U) à l'application : s ~~> φ_{F|U} o s = s o φ_U",
    "'à l'application' with no colon before the display", "punctuation", "high",
    r"F(U)$ à l'application", r"F(U)$ à l'application :", "The TeX drops the colon. " + P456, moved=True)
add(456, "first line: the arrow of s ~~> φ_{F|U} o s",
    "a wavy arrow (~~>) after s", r"s\longmapsto \varphi_{F|U}", "symbol", "high",
    r"s\longmapsto \varphi_{F|U}", r"s\rightsquigarrow \varphi_{F|U}",
    "The print's maps-to sign is the wavy arrow, as on pp. 365-369, 444 and 462 (\\rightsquigarrow, amssymb). "
    + P456, moved=True)
add(456, "first line: end of the formula s ~~> φ_{F|U} o s = s o φ_U",
    "no punctuation after s o φ_U; the parenthesis (s ∈ Hom_U(U,F|U)) follows",
    r"s\circ\varphi_U, at the end of the display", "extra", "high",
    r"=s\circ\varphi_U,", r"=s\circ\varphi_U", "Comma added at the end of the display. " + P456, moved=True)
add(456, "second line: '(s ∈ Hom_U(U,F|U)) ; comme le faisceau final'",
    "(s ∈ Hom_U(U,F|U)) ; comme ...: the condition in parentheses, no 'où'",
    r"où $s\in\Hom_U(U,F|U)$; comme le", "word", "high",
    r"où $s\in\Hom_U(U,F|U)$;", r"($s\in\Hom_U(U,F|U)$);",
    "The TeX adds 'où' and drops the parentheses. " + P456, moved=True)
add(456, "'sur le préschéma X (de caractéristique p),'",
    "X (de caractéristique p), Fr*_{F/X} est un isomorphisme de faisceaux de groupes",
    r"préschéma $X$ de caractéristique $p$, $\Fr^*_{F/X}$ (no parentheses)", "punctuation", "high",
    r"préschéma $X$ de caractéristique $p$, $\Fr", r"préschéma $X$ (de caractéristique $p$), $\Fr",
    "The TeX drops the parentheses.")
add(456, "'... de faisceaux de Λ-modules ; plus généralement, si F˙ est un complexe'",
    "Λ-modu-/les ; plus généralement (semicolon, small p)", r"$\Lambda$-modules. Plus généralement", "punctuation",
    "high", r"$\Lambda$-modules. Plus généralement", r"$\Lambda$-modules; plus généralement",
    "Full stop and capital for the print's semicolon and small letter.")
add(456, "Fr*_{F˙/X} : fr*_X(F˙) --- F˙ égal à ...: the arrow",
    "three typed dashes and no arrowhead (pixel check, strip 2: dashes at x = 1289-1345, clean paper at 1346-1367, "
    "then the F; the other arrows of the page, H^0(X,F) --> ..., have their head)", r"\longrightarrow F^\bullet",
    "misprint_in_print", "medium",
    r"\longrightarrow F^\bullet", r"\relbar\joinrel\relbar F^\bullet",
    "The typist left out the head of the isomorphism arrow. The TeX silently supplies it; the fix restores the "
    "printed headless line (diplomatic layer only).", corrected=r"\longrightarrow F^\bullet")
add(456, "heading n°2",
    "n°2. Effet sur la cohomologie. (underlined, full stop)",
    r"\subsubsection*{n\textsuperscript{o} 2. Effet sur la cohomologie}", "punctuation", "high",
    r"Effet sur la cohomologie}", r"Effet sur la cohomologie.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")
add(456, "Proposition 2, 'Soit X un préschéma de caractéristique p .'",
    "underlined: 'Soit', 'un préschéma de caractéristique'; X, p and the full stop not",
    "no underline markup", "underline", "high",
    r"Soit $X$ un préschéma de caractéristique $p$.",
    r"\emph{Soit} $X$ \emph{un préschéma de caractéristique} $p$.",
    "The print underlines the statement word group by word group; Exposé XV of the TeX has no underline markup. "
    "\\emph as for the underlined statements of Exposés III B, V and XII and on pp. 442-445 and 461-465.")
add(456, "Proposition 2 a), up to 'c'est-à-dire le composé'",
    "underlined: 'Pour tout faisceau d'ensembles', 'sur', 'l'endomorphisme / de', 'défini par', 'c'est-à-dire le "
    "composé'; F, X_ét, H^0(X,F), (fr_X,Fr*_{F/X}) and the commas not", "no underline markup", "underline", "high",
    r"Pour tout faisceau d'ensembles $F$ sur $X_{\et}$, l'endomorphisme de $H^0(X,F)$ défini par $(\fr_X,\Fr^*_{F/X})$, c'est-à-dire le composé",
    r"\emph{Pour tout faisceau d'ensembles} $F$ \emph{sur} $X_{\et}$, \emph{l'endomorphisme de} $H^0(X,F)$ \emph{défini par} $(\fr_X,\Fr^*_{F/X})$, \emph{c'est-à-dire le composé}",
    "Underlined statement. The old ends before the display (comma edit below): no overlap.")
add(456, "Proposition 2 a), the composite H^0(X,F) --> H^0(X,fr*_X(F)) --> H^0(X,F)",
    "no punctuation after the last H^0(X,F); 'où la première flèche' follows",
    r"H^0(X,F)\longrightarrow H^0(X,\fr_X^*(F))\longrightarrow H^0(X,F),", "extra", "high",
    r"\longrightarrow H^0(X,F),", r"\longrightarrow H^0(X,F)", "Comma added at the end of the display.")
add(456, "Proposition 2 a), 'où la première flèche ... est l'identité de H^0(X,F) .'",
    "underlined: 'où la première flèche est l'ap-/plication canonique', 'caractère contravariant de' (not the "
    "parenthesis), 'par rapport / à', 'et la seconde', 'est l'identité de'; the formulas, X), the comma and the "
    "full stop not", "no underline markup", "underline", "high",
    r"où la première flèche est l'application canonique (caractère contravariant de $H^0(X,F)$ par rapport à $X$) et la seconde $H^0(X,\Fr^*_{F/X})$, est l'identité de $H^0(X,F)$.",
    r"\emph{où la première flèche est l'application canonique} (\emph{caractère contravariant de} $H^0(X,F)$ \emph{par rapport à} $X$) \emph{et la seconde} $H^0(X,\Fr^*_{F/X})$, \emph{est l'identité de} $H^0(X,F)$.",
    "Underlined statement.")

# ---------------------------------------------------------------- p. 457
add(457, "top of the page / folio-457 marker: the item label b)",
    "p. 457 begins with 'b) Pour tout faisceau de groupes F ...'; p. 456 ends with '... est l'identité de H^0(X,F) .'",
    "the '\\item' that prints 'b)' is the last line of page_456.tex; the folio-457 marker follows it",
    "marker", "high", None, None,
    "Page 457 really begins at that '\\item' (live s5.tex at the check: diplomatic line 15318, marker at 15319; "
    "current 15314/15315). Exact fix: " + MV457 + " (simulated in memory on both layers: the marker then stands on "
    "its own line between '... est l'identité de $H^0(X,F)$.' and '\\item'; the anchor matches before and after the "
    "edits of pp. 456-457). Run it once only: a second run would move the marker back to the '\\item' of a). "
    "Text not moved.")
add(457, "Proposition 2 b), 'Pour tout faisceau de groupes F sur'",
    "underlined: 'Pour tout faisceau de groupes', 'sur'; F not", "no underline markup", "underline", "high",
    r"Pour tout faisceau de groupes $F$ sur $", r"\emph{Pour tout faisceau de groupes} $F$ \emph{sur} $",
    "Underlined statement.")
add(457, "Proposition 2 b), 'sur X_ét l'endomorphisme / de H^1(X,F)'",
    "no comma after X_ét (clean paper); 'l'endomorphisme / de' underlined",
    r"$X_{\et}$, l'endomorphisme de $H^1(X,F)$", "extra", "high",
    r"{\et}$, l'endomorphisme de $H^1(X,F)$", r"{\et}$ \emph{l'endomorphisme de} $H^1(X,F)$",
    "The TeX adds the comma (a) on p. 456 has one, b) has none). The new text also carries the underline of the "
    "statement (adjacent); no shared characters with the edits before and after it.")
add(457, "Proposition 2 b), 'défini par (fr_X,Fr*_{F/X}) , c'est-à-dire'",
    "underlined: 'défini par', 'c'est-à-dire'; the formula and the comma not", "no underline markup", "underline",
    "high", "défini par $(\\fr_X,\\Fr^*_{F/X})$, c'est-à-dire\n\\[",
    "\\emph{défini par} $(\\fr_X,\\Fr^*_{F/X})$, \\emph{c'est-à-dire}\n\\[", "Underlined statement.")
add(457, "Proposition 2 b), display: H^1(X,fr*_X(F))",
    "H^1(X,F) --> H^1(X,fr*_X(F)) --> H^1(X,F): parentheses around F", r"H^1(X,\fr_X^*F)", "formula", "high",
    r"H^1(X,\fr_X^*F)", r"H^1(X,\fr_X^*(F))", "The TeX drops the parentheses around F.")
add(457, "Proposition 2 b), ', est l'identité.'",
    "'est l'identité' underlined; comma and full stop not", "no underline markup", "underline", "high",
    "\\]\nest l'identité.\n\\item", "\\]\n\\emph{est l'identité}.\n\\item", "Underlined statement.")
add(457, "Proposition 2 c), 'Pour tout complexe limité à gauche F de'",
    "underlined: 'Pour tout complexe limité à gauche', 'de'; F and Λ not", "no underline markup", "underline",
    "high", r"Pour tout complexe limité à gauche $F$ de $",
    r"\emph{Pour tout complexe limité à gauche} $F$ \emph{de} $", "Underlined statement.")
add(457, "Proposition 2 c), 'Λ-Modules sur'",
    "Λ-Modules with a capital M; 'Modules sur' underlined", r"$\Lambda$-modules sur", "word", "high",
    r"-modules sur $X", r"-\emph{Modules sur} $X",
    "Small m for the print's capital (as 'complexe de Λ-Modules' on p. 456, which the TeX has right). The new text "
    "also carries the underline of the statement (same words).")
add(457, "Proposition 2 c), 'l'endomorphisme de RΓ_X(F) défini par'",
    "underlined: 'l'endomorphisme de', 'défini par'; the formulas and the comma not", "no underline markup",
    "underline", "high", r"{\et}$, l'endomorphisme de $\RGamma_X(F)$ défini par $(",
    r"{\et}$, \emph{l'endomorphisme de} $\RGamma_X(F)$ \emph{défini par} $(", "Underlined statement.")
add(457, "Proposition 2 c), 'c'est-/à-dire le composé :'",
    "'c'est-à-dire le composé' underlined, then a colon (not underlined) before RΓ_X(F) --> ...",
    "'c'est-à-dire le composé' and the display, no colon", "punctuation", "high",
    "c'est-à-dire le composé\n\\[\n\\RGamma", "\\emph{c'est-à-dire le composé} :\n\\[\n\\RGamma",
    "The TeX drops the colon. The new text also carries the underline of the statement (adjacent).")
add(457, "Proposition 2 c), display: RΓ_X(fr*_X(F))",
    "RΓ_X(F) --> RΓ_X(fr*_X(F)) --> RΓ_X(F): parentheses around F", r"\RGamma_X(\fr_X^*F)", "formula", "high",
    r"\RGamma_X(\fr_X^*F)", r"\RGamma_X(\fr_X^*(F))", "The TeX drops the parentheses around F.")
add(457, "Proposition 2 c), ', est / l'identité.'",
    "'est' and 'l'identité' underlined; comma and full stop not", "no underline markup", "underline", "high",
    "est l'identité.\n\\end{enumerate}", "\\emph{est l'identité}.\n\\end{enumerate}", "Underlined statement.")
add(457, "'Etablissons d'abord a) : nous en déduirons b) et c).'",
    "a colon after a)", r"a); nous", "punctuation", "high",
    r"d'abord a); nous", r"d'abord a) : nous", "Semicolon for the print's colon.")
add(457, "'s'identifie à un morphisme de faisceaux : s : X --> F'",
    "a colon after 'faisceaux'", r"de faisceaux $s:X\to F$", "punctuation", "high",
    r"de faisceaux $s:X\to F$", r"de faisceaux : $s:X\to F$", "The TeX drops the colon.")
add(457, "φ_F o H^0(X,s) = H^0(X,s) o φ_X = H^0(X,s) d'après ...",
    "no punctuation after the last H^0(X,s)", r"=H^0(X,s), at the end of the display", "extra", "high",
    "=H^0(X,s),\n\\]", "=H^0(X,s)\n\\]", "Comma added at the end of the display.")
add(457, "'Notons que φ_F est encore le composé :'",
    "a colon after 'le composé'", "'le composé' and the display, no colon", "punctuation", "high",
    "encore le composé\n\\[", "encore le composé :\n\\[", "The TeX drops the colon.")
add(457, "H^0(X,F) --> H^0(X,fr_{X*}(F)) --> H^0(X,F)",
    "parentheses around F in fr_{X*}(F)", r"H^0(X,\fr_{X*}F)", "formula", "high",
    r"H^0(X,\fr_{X*}F)", r"H^0(X,\fr_{X*}(F))", "The TeX drops the parentheses (also in the next displays).")
add(457, "end of that display, before 'où la première flèche est'",
    "no punctuation after H^0(X,F)", r"H^0(X,F), at the end of the display", "extra", "high",
    "H^0(X,F),\n\\]\noù", "H^0(X,F)\n\\]\noù", "Comma added at the end of the display.")
add(457, "'l'application canonique (qui n'est autre que l'identité) ; de même les endomorphismes'",
    "the clause in parentheses, then a semicolon and a small d", r"canonique, qui n'est autre que l'identité. De même",
    "punctuation", "high",
    r"l'application canonique, qui n'est autre que l'identité. De même",
    r"l'application canonique (qui n'est autre que l'identité); de même",
    "Comma, full stop and capital for the print's parentheses, semicolon and small letter.")
add(457, "H^1(X,F) --> H^1(X,fr_{X*}(F)) --> H^1(X,F)",
    "parentheses around F", r"H^1(X,\fr_{X*}F)", "formula", "high",
    r"H^1(X,\fr_{X*}F)", r"H^1(X,\fr_{X*}(F))", "The TeX drops the parentheses.")
add(457, "end of that display, before 'et'",
    "no punctuation after H^1(X,F)", r"H^1(X,F), at the end of the display", "extra", "high",
    "H^1(X,F),\n\\]\net", "H^1(X,F)\n\\]\net", "Comma added at the end of the display.")
add(457, "RΓ_X(F) --> RΓ_X(fr_{X*}(F)) --> RΓ_X(F) .",
    "parentheses around F", r"\RGamma_X(\fr_{X*}F)", "formula", "high",
    r"\RGamma_X(\fr_{X*}F)", r"\RGamma_X(\fr_{X*}(F))", "The TeX drops the parentheses.")
add(457, "'Pour établir b) nous utiliserons'",
    "no comma after b)", r"Pour établir b), nous", "extra", "high",
    r"Pour établir b), nous", r"Pour établir b) nous", "The TeX adds a comma.")
add(457, "fr_{X*}(F) --> fr_{X*}(G) est un monomorphisme",
    "parentheses around F and G", r"$\fr_{X*}F\to\fr_{X*}G$", "formula", "high",
    r"$\fr_{X*}F\to\fr_{X*}G$", r"$\fr_{X*}(F)\to\fr_{X*}(G)$", "The TeX drops the parentheses.")
add(457, "H^1(X,fr_{X*}(G)) = 0",
    "parentheses around G", r"$H^1(X,\fr_{X*}G)=0$", "formula", "high",
    r"$H^1(X,\fr_{X*}G)=0$", r"$H^1(X,\fr_{X*}(G))=0$", "The TeX drops the parentheses.")
add(457, "last line: 'quotient C = G/F ;'",
    "a semicolon after C = G/F; the sentence runs on at the top of p. 458 with a small 'comme'",
    r"$C=G/F$. (full stop)", "punctuation", "high",
    r"quotient $C=G/F$.", r"quotient $C=G/F$;",
    "Apply together with the p. 458 edit 'Comme' -> 'comme' (one sentence across the page break).")

# ---------------------------------------------------------------- p. 458
add(458, "first word of the page: 'comme fr_X est entier'",
    "small c: the sentence continues from p. 457 ('C = G/F ; comme ...')", r"Comme $\fr_X$ est", "word", "high",
    r"Comme $\fr_X$ est", r"comme $\fr_X$ est",
    "Apply together with the p. 457 edit '$C=G/F$.' -> '$C=G/F$;'.")
add(458, "'entier surjectif et radiciel les foncteurs'",
    "no commas", r"entier, surjectif et radiciel, les", "extra", "high",
    r"entier, surjectif et radiciel, les", r"entier surjectif et radiciel les", "The TeX adds two commas.")
add(458, "φ_C : H^0(X,C) --> H^0(X,C) qui est l'identité",
    "no punctuation after the formula", r"H^0(X,C), at the end of the display", "extra", "high",
    "H^0(X,C)\\longrightarrow H^0(X,C),\n\\]", "H^0(X,C)\\longrightarrow H^0(X,C)\n\\]",
    "Comma added at the end of the display.")
add(458, "'construite sur les Λ-Modules ;'",
    "Λ-Modules with a capital M", r"$\Lambda$-modules;", "word", "high",
    r"$\Lambda$-modules; le complexe", r"$\Lambda$-Modules; le complexe", "Small m for the print's capital.")
add(458, "'RΓ_X(fr_{X*}(F)) à H^0(X,fr_{X*}(I))'",
    "parentheses around F", r"$\RGamma_X(\fr_{X*}F)$", "formula", "high",
    r"$\RGamma_X(\fr_{X*}F)$", r"$\RGamma_X(\fr_{X*}(F))$",
    "The TeX drops the parentheses (the comment FIX #52 under this paragraph is not printed text).")
add(458, "'à H^0(X,fr_{X*}(I))'",
    "parentheses around I", r"$H^0(X,\fr_{X*}I)$", "formula", "high",
    r"$H^0(X,\fr_{X*}I)$", r"$H^0(X,\fr_{X*}(I))$", "The TeX drops the parentheses.")
add(458, "'s'identifie à φ_I qui est l'identité'",
    "no comma after φ_I (end of the line, clean paper)", r"$\varphi_I$, qui", "extra", "high",
    r"$\varphi_I$, qui", r"$\varphi_I$ qui", "The TeX adds a comma.")
add(458, "heading n°3",
    "n°3. Comportement des produits. (underlined, full stop)",
    r"\subsubsection*{n\textsuperscript{o} 3. Comportement des produits}", "punctuation", "high",
    r"Comportement des produits}", r"Comportement des produits.}",
    "The underlined title ends with a full stop in the print; the TeX drops it.")
add(458, "'au produit fibré X x_e X' où e = Spec(F_p)'",
    "no comma before 'où'", r"$X\times_eX'$, où", "extra", "high",
    r"$X\times_eX'$, où", r"$X\times_eX'$ où", "The TeX adds a comma.")
add(458, "'On en déduit immédiatement que pour tout X-préschéma Y'",
    "no comma after 'que'", r"que, pour tout", "extra", "high",
    r"immédiatement que, pour tout", r"immédiatement que pour tout", "The TeX adds a comma.")
add(458, "(Y x Y')^{(p/XxX')} ≃ Y^{(p/X)} x Y'^{(p/X')} ; modulo cet isomorphisme",
    "a semicolon after the formula", r"Y'{}^{(p/X')}, (comma)", "punctuation", "high",
    "Y'{}^{(p/X')},\n\\]", "Y'{}^{(p/X')};\n\\]", "Comma for the print's semicolon.")

# ---------------------------------------------------------------- p. 459
add(459, "first line: 'peut écrire Fr_{YxY'/XxX'} = Fr_{Y/X} x Fr_{Y'/X'} .'",
    "no colon after 'écrire'", r"peut écrire:", "extra", "high",
    r"peut écrire:", r"peut écrire", "The TeX adds a colon.")
add(459, "Proposition 3, statement up to the second 'Λ-modules sur'",
    "underlined: 'Soient', 'et', 'des préschémas de caractéristique', 'un anneau commutatif', 'un faisceau de', "
    "'-modules sur', 'et', 'un faisceau de', '-modules sur'; the letters, Λ, the commas not",
    "no underline markup", "underline", "high",
    r"Soient $X$ et $X'$ des préschémas de caractéristique $p$, $\Lambda$ un anneau commutatif, $F$ un faisceau de $\Lambda$-modules sur $X_{\et}$ et $F'$ un faisceau de $\Lambda$-modules sur $",
    r"\emph{Soient} $X$ \emph{et} $X'$ \emph{des préschémas de caractéristique} $p$, $\Lambda$ \emph{un anneau commutatif}, $F$ \emph{un faisceau de} $\Lambda$-\emph{modules sur} $X_{\et}$ \emph{et} $F'$ \emph{un faisceau de} $\Lambda$-\emph{modules sur} $",
    "Underlined statement. The old stops at the $ before X'_{\\et} (misprint item below): the same edit fits the "
    "corrected layer.")
add(459, "Proposition 3, '. On a'",
    "'On a' underlined", "no underline markup", "underline", "high",
    r"{\et}$. On a", r"{\et}$. \emph{On a}", "Underlined statement.")
add(459, "Proposition 3: 'F' un faisceau de Λ-modules sur X_ét'",
    "X_ét without a prime (clean paper at the top right of the X; the prime of F' in the same line is plain)",
    r"$X'_{\et}$", "misprint_in_print", "high",
    r"$X'_{\et}$", r"$X_{\et}$",
    "F' is a sheaf on X'_ét (the X' of the statement). The TeX silently corrects; the fix restores the printed X "
    "(diplomatic layer only). Listed after the two underline edits of Proposition 3; its old is unique before and "
    "after them.", corrected=r"$X'_{\et}$")
add(459, "Proposition 3, first line of the formula: Fr*_{F ⊗_Λ F'/XxX'}",
    "the typed tensor sign (an O overstruck with x), the same sign as in Fr*_{F/X} ⊗ Fr*_{F'/X'}",
    r"F\boxt_\Lambda F' (box-times)", "symbol", "high",
    r"F\boxt_\Lambda F'/X", r"F\otimes_\Lambda F'/X",
    "\\boxt is \\boxtimes; the print has the same ⊗ for every tensor product on pp. 459-460. All 11 uses of \\boxt in "
    "s5.tex are on these two pages (itemized here).")
add(459, "Proposition 3: id_{fr*_{X'}(F')}",
    "parentheses around F'", r"\id_{\fr_{X'}^*F'}", "formula", "high",
    r"\id_{\fr_{X'}^*F'}", r"\id_{\fr_{X'}^*(F')}", "The TeX drops the parentheses.")
add(459, "Proposition 3, second line: id_{fr*_X(F)}",
    "parentheses around F", r"\id_{\fr_X^*F}", "formula", "high",
    r"\id_{\fr_X^*F}", r"\id_{\fr_X^*(F)}", "The TeX drops the parentheses.")
add(459, "Proposition 3, end of the second line of the formula",
    "no full stop after (Fr*_{F/X} ⊗ id_{F'})", r"\id_{F'}). at the end of the display", "extra", "high",
    "\\otimes\\id_{F'}).\n\\]", "\\otimes\\id_{F'})\n\\]", "Full stop added at the end of the display.")
add(459, "'on a identifié fr*_{XxX'}(F ⊗_Λ F')'",
    "the typed tensor sign ⊗", r"(F\boxt_\Lambda F')", "symbol", "high",
    r"(F\boxt_\Lambda F')", r"(F\otimes_\Lambda F')", "As in Proposition 3.")
add(459, "'au cas où F = Λ_X et F' = Λ_{X'} ; alors'",
    "a semicolon before 'alors'", r"$F'=\Lambda_{X'}$, alors", "punctuation", "high",
    r"$F'=\Lambda_{X'}$, alors", r"$F'=\Lambda_{X'}$; alors", "Comma for the print's semicolon.")
add(459, "'au cas où F = _X' (end of the line)",
    "F = , then blank paper where the hand-drawn Λ belongs, then the lowered X (pixel check: pure white between "
    "'=' and 'X', x = 1446-1498 of strip 3); the Λ of 'F' = Λ_{X'}' just below is drawn",
    r"$F=\Lambda_X$", "misprint_in_print", "high",
    r"$F=\Lambda_X$", r"$F={}_X$",
    "The space left for the hand-drawn Λ was never filled (not a faint stroke). The TeX silently supplies \\Lambda; "
    "the fix restores the printed reading (diplomatic layer only).", corrected=r"$F=\Lambda_X$")
add(459, "Corollaire, 'Avec les données de la proposition 3, les endomorphismes / de'",
    "underlined: 'Avec les données de la proposition 3' (the 3 included), 'les endomorphismes', 'de'; the comma not",
    "no underline markup", "underline", "high",
    r"Avec les données de la proposition 3, les endomorphismes de $",
    r"\emph{Avec les données de la proposition 3}, \emph{les endomorphismes de} $", "Underlined statement.")
add(459, "Corollaire: RΓ_{XxX'}(F ⊗ F')",
    "the typed tensor sign ⊗", r"(F\boxt F')", "symbol", "high",
    "(F\\boxt F')$ ", "(F\\otimes F')$ ",
    "As in Proposition 3. The old ends with the space before 'définis' (unique; it does not touch the underline "
    "edits around it).")
add(459, "Corollaire, 'définis respectivement par'",
    "underlined", "no underline markup", "underline", "high",
    r"définis respectivement par", r"\emph{définis respectivement par}", "Underlined statement.")
add(459, "Corollaire, 'et par'",
    "underlined", "no underline markup", "underline", "high",
    "\\]\net par\n\\[", "\\]\n\\emph{et par}\n\\[", "Underlined statement.")
add(459, "Corollaire, 'sont des isomorphismes réciproques / l'un de l'autre.'",
    "underlined; the full stop not", "no underline markup", "underline", "high",
    r"sont des isomorphismes réciproques l'un de l'autre.",
    r"\emph{sont des isomorphismes réciproques l'un de l'autre}.", "Underlined statement.")
add(459, "last line of the page: 'cela résulte du diagramme'",
    "p. 459 ends '... ; cela résulte du diagramme' and blank paper; p. 460 begins with the diagram, followed by "
    "', qui est commutatif à cause de ...': no 'commutatif suivant :' anywhere",
    r"cela résulte du diagramme commutatif suivant:", "extra", "high",
    r"du diagramme commutatif suivant:", r"du diagramme",
    "Words added by the TeX (the print says 'commutatif' only after the diagram). The folio-460 move (anchor '\\[' "
    "+ '\\resizebox') is not affected.")
add(459, "the diagram (printed on p. 460): the tensor signs of the nodes",
    "every node has the typed ⊗: RΓ_{XxX'}(F⊗F'), RΓ_{XxX'}(F⊗fr*_{X'}(F')), RΓ_{XxX'}(fr*_{XxX'}(F⊗F')), "
    "RΓ_{XxX'}(fr*_X(F)⊗F'), RΓ(Fr*_{F⊗F'/XxX'})", r"\boxt in the seven nodes A-G", "symbol", "high",
    "\\node (A) at (0,3.6) {$\\RGamma_{X\\times X'}(F\\boxt F')$};\n"
    "\\node (B) at (4.7,3.6) {$\\RGamma_{X\\times X'}(F\\boxt\\fr_{X'}^*(F'))$};\n"
    "\\node (C) at (9.4,3.6) {$\\RGamma_{X\\times X'}(F\\boxt F')$};\n"
    "\\node (D) at (3.3,1.9) {$\\RGamma_{X\\times X'}(\\fr^*_{X\\times X'}(F\\boxt F'))$};\n"
    "\\node (E) at (9.4,1.9) {$\\RGamma_{X\\times X'}(\\fr_X^*(F)\\boxt F')$};\n"
    "\\node (F) at (4.4,0.25) {$\\RGamma(\\Fr^*_{F\\boxt F'/X\\times X'})$};\n"
    "\\node (G) at (9.4,0.25) {$\\RGamma_{X\\times X'}(F\\boxt",
    "\\node (A) at (0,3.6) {$\\RGamma_{X\\times X'}(F\\otimes F')$};\n"
    "\\node (B) at (4.7,3.6) {$\\RGamma_{X\\times X'}(F\\otimes\\fr_{X'}^*(F'))$};\n"
    "\\node (C) at (9.4,3.6) {$\\RGamma_{X\\times X'}(F\\otimes F')$};\n"
    "\\node (D) at (3.3,1.9) {$\\RGamma_{X\\times X'}(\\fr^*_{X\\times X'}(F\\otimes F'))$};\n"
    "\\node (E) at (9.4,1.9) {$\\RGamma_{X\\times X'}(\\fr_X^*(F)\\otimes F')$};\n"
    "\\node (F) at (4.4,0.25) {$\\RGamma(\\Fr^*_{F\\otimes F'/X\\times X'})$};\n"
    "\\node (G) at (9.4,0.25) {$\\RGamma_{X\\times X'}(F\\otimes",
    "One edit for the seven nodes (\\boxt -> \\otimes only). Its old ends inside node G, before the comma edit "
    "below (no overlap). Nodes, arrows and labels otherwise agree with the print (label sides are layout). " + P460)
add(459, "the diagram (printed on p. 460): after the bottom right node",
    "a comma after RΓ_{XxX'}(F⊗F') (bottom right), then 'qui est commutatif à cause de'",
    r"node G ends ...(F\boxt F')$}; no comma", "punctuation", "high",
    " F')$};\n\\draw[->] (A)", " F')$\\ ,};\n\\draw[->] (A)",
    "The TeX drops the comma that ends the diagram. Independent of the node edit above. " + P460)

# ---------------------------------------------------------------- p. 460
add(460, "top of the page / folio-460 marker: the diagram",
    "p. 460 begins with the diagram RΓ_{XxX'}(F⊗F') --> ... (no text above it); p. 459 ends with '... ; cela "
    "résulte du diagramme' and blank paper",
    "the display '\\[', '\\resizebox{\\textwidth}{!}{%', the tikzpicture with all its nodes and arrows stand in "
    "page_459.tex; the folio-460 marker splits the display before '\\end{tikzpicture}%'",
    "marker", "high", None, None,
    "Page 460 really begins at the '\\[' that opens the diagram (live s5.tex at the check: diplomatic line 15427, "
    "marker at 15445; current 15423/15441). Exact fix (bash): " + MV460 + " (simulated in memory on both layers: "
    "the marker then stands on its own line between '... cela résulte du diagramme commutatif suivant:' (or '... du "
    "diagramme' after the p. 459 edit) and '\\['; the anchor occurs once in s5.tex, so a second run prints 'anchor "
    "not found'). Text not moved; the two diagram edits filed under p. 459 go first.")
add(460, "'(pour le triangle du haut) et de'",
    "the words in parentheses", "'pour le triangle du haut' without parentheses", "punctuation", "high",
    "\\]\npour le triangle du haut et de", "\\]\n(pour le triangle du haut) et de",
    "The TeX drops the parentheses.")
add(460, "Fr*_{F⊗F'/XxX'} = (...) o (id_{fr*_X(F)} ⊗ Fr*_{F'/X'})",
    "parentheses around F in id_{fr*_X(F)}", r"\id_{\fr_X^*F}", "formula", "high",
    r"\id_{\fr_X^*F}", r"\id_{\fr_X^*(F)}", "The TeX drops the parentheses.")
add(460, "Fr*_{F⊗F'/XxX'}: the tensor sign",
    "the typed tensor sign ⊗", r"\Fr^*_{F\boxt F'/X\times X'}", "symbol", "high",
    r"\Fr^*_{F\boxt F'/X\times X'}=", r"\Fr^*_{F\otimes F'/X\times X'}=", "As on p. 459.")
add(460, "'(pour le triangle du bas), et dans lequel'",
    "the words in parentheses, then the comma", "'pour le triangle du bas,' without parentheses", "punctuation",
    "high", "\\]\npour le triangle du bas,", "\\]\n(pour le triangle du bas),", "The TeX drops the parentheses.")
add(460, "'les rôles de (X,F) et (X',F') on obtient : φ' o φ = id .'",
    "no comma after (X',F'); a colon after 'obtient'", r"$(X',F')$, on obtient $\varphi'", "punctuation", "high",
    r"$(X',F')$, on obtient $\varphi'", r"$(X',F')$ on obtient : $\varphi'",
    "The TeX adds the comma and drops the colon.")
add(460, "'Dans ce cas nous poserons : X̄ = ...'",
    "a colon after 'poserons'", "'nous poserons' and the display, no colon", "punctuation", "high",
    "nous poserons\n\\[", "nous poserons :\n\\[", "The TeX drops the colon.")
add(460, "X̄ = X x ē = X ⊗_{F_p} F̄_p",
    "a plain x between X and ē, no subscript e under it", r"X\times_e\bar e", "formula", "high",
    r"X\times_e\bar e", r"X\times\bar e", "The TeX adds the subscript e.")
add(460, "'X̄ = ... = X ⊗_{F_p} F̄_p et F̄ = F ⊗_Λ Λ_ē'",
    "'et' between the two formulas, no comma", r"\overline{\mathbb F}_p, \qquad \overline F", "word", "high",
    "\\overline{\\mathbb F}_p,\n\\qquad\n\\overline F", "\\overline{\\mathbb F}_p\\quad\\text{et}\\quad\n\\overline F",
    "The TeX drops 'et' and adds a comma (written as the p. 461 fix '\\quad\\text{et}\\quad').")
add(460, "'F̄ = F ⊗_Λ Λ_ē = image réciproque de F par la projection'",
    "'=' before 'image réciproque'", r"\Lambda_{\bar e}, at the end of the display", "punctuation", "high",
    "\\Lambda_{\\bar e},\n\\]\nimage", "\\Lambda_{\\bar e}=\n\\]\nimage",
    "Comma for the print's '=' (as the p. 461 lines, fixed there the same way).")
add(460, "'f : λ ~~> λ^p'",
    "a wavy arrow (~~>)", r"f:\lambda\longmapsto\lambda^p", "symbol", "high",
    r"f:\lambda\longmapsto\lambda^p", r"f:\lambda\rightsquigarrow\lambda^p",
    "As the wavy arrow at the top of p. 456 (and p. 462).")
add(460, "π_e = Gal(F̄_p/F_p) (f détermine ...",
    "no comma after Gal(F̄_p/F_p); a parenthesis opens",
    r"\Gal(\overline{\mathbb F}_p/\mathbb F_p), at the end of the display", "extra", "high",
    "/\\mathbb F_p),\n\\]", "/\\mathbb F_p)\n\\]", "Comma added at the end of the display.")
add(460, "'(f détermine un iso-/morphisme: Ẑ ⥲ π_e), et'",
    "an opening parenthesis, the verb 'détermine', a colon after 'isomorphisme'",
    r"$f$ déterminant un isomorphisme $\widehat{\mathbb Z}", "word", "high",
    r"$f$ déterminant un isomorphisme $", r"($f$ détermine un isomorphisme: $",
    "The TeX writes the participle and drops the parenthesis and the colon (closing parenthesis: edit after next).")
add(460, "Ẑ ⥲ π_e: the sign",
    "a hand-drawn tilde over a typed arrow with its head (-->)", r"\simeq", "symbol", "high",
    r"\simeq\pi_e$", r"\xrightarrow{\sim}\pi_e$",
    "An isomorphism arrow, not the headless ≃ (the two ≃ of p. 458 have no head).")
add(460, "'π_e), et Fr*...'",
    "the closing parenthesis before ', et'", r"\pi_e$, et", "punctuation", "high",
    r"\pi_e$, et", r"\pi_e$), et", "Closes the parenthesis opened before 'f' (two edits above).")
add(460, "'car Λ_ē est un faisceau constant. Posons :'",
    "a colon after 'Posons' (the last word of the page)", r"Posons (no colon)", "punctuation", "high",
    r"faisceau constant. Posons", r"faisceau constant. Posons :", "The TeX drops the colon.")

# ---------------------------------------------------------------- checks
batch = {n: pfile(n).read_text(encoding="utf-8") for n in range(455, 461)}
bad = 0
for i, x in enumerate(F):
    f = x["fix"]
    if f is None:
        continue
    src = 455 if i in MOVED else x["page"]
    c = batch[src].count(f["old"])
    if c != 1:
        bad += 1
        print("NOT ONCE IN BATCH FILE", i, src, c, repr(f["old"][:60]))
    if MARK.search(f["old"]) or MARK.search(f["new"]):
        bad += 1
        print("MARKER IN FIX", i)
    if f["old"] == f["new"]:
        bad += 1
        print("NO CHANGE", i)
for layer in ("diplomatic", "current"):
    t = (W / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")

    def spans(text):
        ms = list(MARK.finditer(text))
        out = {}
        for j, m in enumerate(ms):
            end = ms[j + 1].start() if j + 1 < len(ms) else len(text)
            out[int(m.group(2))] = text[m.start():end]
        return out

    sp = spans(t)
    # live spans: each old once on its page; then all edits of the page in listed order
    for n in range(456, 461):
        s = sp[n]
        for i, x in enumerate(F):
            if x["page"] != n or x["fix"] is None:
                continue
            if layer == "current" and x["kind"] == "misprint_in_print":
                continue
            o, nw = x["fix"]["old"], x["fix"]["new"]
            if sp[n].count(o) != 1:
                bad += 1
                print("NOT ONCE IN LIVE SPAN", layer, n, i, sp[n].count(o), repr(o[:60]))
            if s.count(o) != 1:
                bad += 1
                print("SEQUENCE FAIL", layer, n, i, s.count(o), repr(o[:60]))
                continue
            s = s.replace(o, nw)
    # remaining marker moves (456 is already done in the live file)
    t2 = t
    for folio, anchor in ((457, "\\item"), (460, "\\[\n\\resizebox")):
        r = move(t2, folio, anchor, True)
        if r is None:
            bad += 1
            print("MOVE FAILED", layer, folio)
            continue
        t2 = r
    sp2 = spans(t2)
    for i, x in enumerate(F):
        f = x["fix"]
        if f is None:
            continue
        o, n0 = f["old"], x["page"]
        if sp2[n0].count(o) == 1:
            continue
        if sp2[n0].count(o) == 0 and sp2[n0 + 1].count(o) == 1:
            print(f"  {layer}: finding {i} (p. {n0}) lies once on p. {n0 + 1} after the moves")
            continue
        bad += 1
        print("AFTER MOVES", layer, i, n0, sp2[n0].count(o), sp2[n0 + 1].count(o), repr(o[:60]))
    # the moves after the edits too (anchors unchanged by the edits)
    t3 = t
    for i, x in enumerate(F):
        if x["fix"] is None or (layer == "current" and x["kind"] == "misprint_in_print"):
            continue
        n0 = x["page"]
        s3 = spans(t3)[n0]
        k = t3.find(s3)
        t3 = t3[:k] + s3.replace(x["fix"]["old"], x["fix"]["new"], 1) + t3[k + len(s3):]
    for folio, anchor in ((457, "\\item"), (460, "\\[\n\\resizebox")):
        r = move(t3, folio, anchor, True)
        if r is None:
            bad += 1
            print("MOVE FAILED AFTER EDITS", layer, folio)
            continue
        t3 = r
        m = next(m for m in MARK.finditer(t3) if int(m.group(2)) == folio)
        print(f"  {layer} after edits, folio {folio}: ...{t3[max(0, m.start() - 70):m.start()]!r} | "
              f"{t3[m.end():m.end() + 40]!r}")
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("problems:", bad, "| findings:", len(F), "| per page (normal, misprint):", counts)
if bad == 0:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
