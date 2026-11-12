"""Build findings_466_470.json for batch 466-470 (SGA 5, Exposé XV, pp. 466-470). '<NL>' in old/new is a line break."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_466_470.json")
NL = "<NL>"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


RNOTE = (r"\R is \mathbb{R} after Exposé III B (\renewcommand{\R}{\mathbb{R}} at its end), so the TeX sets a "
         r"double-struck R. On pp. 466-469 the R of R^i_!, R^j_!, R^k_! is a plain typed R (no double underline); "
         r"on p. 470 both RΓ subscripts have a double-underlined R, where \R is right. Itemized (no blanket rule).")
EMNOTE = (r"The statement environment sets an upright body with no underline; \emph is this exposé's markup for "
          r"underlined text (\emph{(Transitivité.)} in § 1) and the form used for underlined statements in "
          r"Exposés III B, V and XII. Formulas, math letters and punctuation are not underlined in the print; the "
          r"underline of Ω-faisceau starts after the hyphen.")

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 465 (filed: text printed on p. 466)
add(465, "last word of page_465.tex, printed as the first word of p. 466: 'donne :'",
    "p. 466 begins 'donne :' (colon after 'donne'), then the display",
    "'(théorème du changement de base), ce qui donne' with no colon",
    "punctuation", "high", fx(r"ce qui donne", r"ce qui donne:"),
    "Printed on p. 466; filed under p. 465 because the word stands in page_465.tex until the folio-466 marker is "
    "moved (marker finding of p. 466): apply before moving the marker (the move anchor 'donne' still matches).")

# ---------------------------------------------------------------- p. 466
add(466, "top of the page: 'donne :' (folio-466 marker)",
    "p. 466 begins 'donne :', then the display L_F = ∏_i(∏_{y∈Y°} L_{R^i_!u(F)_y})^{(-1)^i} = ...; p. 465 ends "
    "'(théorème du changement de base), ce qui' (b461_465/page_465_s4.png)",
    "'donne' is the last word of page_465.tex ('(théorème du changement de base), ce qui donne'); the folio-466 "
    "marker follows it, so page_466.tex begins with the display",
    "marker", "high", None,
    "Page 466 really begins at 'donne'. Exact fix: python -I move_marker.py 5 466 'donne' --before (simulated in "
    "memory on both layers: the marker moves back 6 characters to its own line between '(théorème du changement de "
    "base), ce qui' and 'donne'). Run it once only: 'donne' occurs 60 times above the marker, and a second run would "
    "move the marker about 39,000 characters back. Apply the colon fix filed under p. 465 first. Text not moved.")

add(466, "first display, the L inside the product over y ∈ Y°",
    "L_{R^i_!u(F)_y}: no parentheses around R^i_!u(F); plain typed R",
    r"L_{(\R^i_!u(F))_y}",
    "formula", "high", fx(r"L_{(\R^i_!u(F))_y}", r"L_{\mathrm{R}^i_!u(F)_y}"),
    "The parentheses are added by the TeX. The same edit writes the print's plain R (see the font findings).")

add(466, "first display, last member ∏_i(L_{R^i_!u(F)})^{(-1)^i}",
    "plain typed R (no double underline)", r"\R^i_!u(F)",
    "font", "high", fx(r"\right)^{(-1)^i}<NL>=\prod_i\bigl(L_{\R", r"\right)^{(-1)^i}<NL>=\prod_i\bigl(L_{\mathrm{R}"),
    RNOTE)

add(466, "Corollaire (after Lemme 1)",
    "underlined: 'Soient' | 'un morphisme fini de schémas de type fini sur' | 'et' | 'un' | 'faisceau "
    "constructible sur' (after the hyphen of Ω-) | 'La propriété' | 'est vraie'",
    "the statement in upright type, no underline markup",
    "underline", "high",
    fx(r"Soient $u:X\to Y$ un morphisme fini de schémas de type fini sur $\mathbb F_p$, et $F$ un $\Omega$-faisceau "
       r"constructible sur $X$. La propriété $(P_{F,u})$ est vraie.",
       r"\emph{Soient} $u:X\to Y$ \emph{un morphisme fini de schémas de type fini sur} $\mathbb F_p$, \emph{et} $F$ "
       r"\emph{un} $\Omega$-\emph{faisceau constructible sur} $X$. \emph{La propriété} $(P_{F,u})$ \emph{est vraie}."),
    EMNOTE)

add(466, "'u_*(F) ≃ ⊕_{x∈X} u_*(F_x) ; pour établir la formule'",
    "the formula runs on in the line and is followed by ' ;' and a lower-case 'pour'",
    r"the display ends 'u_*(F_x).' and the next line begins 'Pour établir'",
    "punctuation", "high", fx(r"u_*(F_x).<NL>\]<NL>Pour", r"u_*(F_x);<NL>\]<NL>pour"),
    "Full stop for the print's semicolon, capital P for 'pour'. The display for a formula run into the line is not "
    "reported (layout).")

add(466, "'pour établir la formule (P_{F,u}) L_F = L_{u_*(F)} on est donc ramené': after (P_{F,u})",
    "no comma after (P_{F,u})", r"'la formule $(P_{F,u})$, $L_F=...'",
    "punctuation", "high", fx(r"formule $(P_{F,u})$,", r"formule $(P_{F,u})$"),
    "Comma added by the TeX. The next two findings (u_*(F), second comma) are disjoint edits of the same phrase.")

add(466, "same phrase: L_F = L_{u_*(F)}",
    "L_F = L_{u_*(F)}: u_*(F) with parentheses", r"L_F=L_{u_*F}",
    "formula", "high", fx(r"L_F=L_{u_*F}", r"L_F=L_{u_*(F)}"),
    "The TeX drops the parentheses (also in the display after '(n°1) :', next findings).")

add(466, "same phrase: after L_{u_*(F)}",
    "no comma before 'on est donc ramené'", r"'$, on est donc'",
    "punctuation", "high", fx(r"$, on est donc", r"$ on est donc"),
    "Comma added by the TeX.")

add(466, "'on a par définition (n°1) :'",
    "(n°1) followed by ' :' and the formula", r"(n\textsuperscript{o}~1) and the display, no colon",
    "punctuation", "high", fx(r"(n\textsuperscript{o}~1)<NL>", r"(n\textsuperscript{o}~1):<NL>"),
    "Colon missing in the TeX.")

add(466, "display after '(n°1) :'",
    "L_F = L_{g_*(F)} = L_{h_*u_*(F)} = L_{u_*(F)} , puisque", r"L_F=L_{g_*F}=L_{h_*u_*F}=L_{u_*F},",
    "formula", "high", fx(r"L_F=L_{g_*F}=L_{h_*u_*F}=L_{u_*F},", r"L_F=L_{g_*(F)}=L_{h_*u_*(F)}=L_{u_*(F)},"),
    "The TeX drops the parentheses around F three times. The comma before 'puisque' is printed.")

add(466, "Lemme 2, first sentence",
    "underlined: 'Soient' | 'des morphismes de schémas de type fini sur' | 'et' | 'un' | 'faisceau constructible "
    "sur' (after the hyphen)",
    "no underline markup",
    "underline", "high",
    fx(r"Soient $u:X\to Y$, $v:Y\to Z$ des morphismes de schémas de type fini sur $\mathbb F_p$ et $F$ un "
       r"$\Omega$-faisceau constructible sur $X$.",
       r"\emph{Soient} $u:X\to Y$, $v:Y\to Z$ \emph{des morphismes de schémas de type fini sur} $\mathbb F_p$ "
       r"\emph{et} $F$ \emph{un} $\Omega$-\emph{faisceau constructible sur} $X$."),
    EMNOTE)

add(466, "Lemme 2, second sentence",
    "underlined: 'Si les propriétés' | 'et' | 'pour tout' | 'sont vraies' | 'alors' | 'est vraie'; plain typed R in "
    "(P_{R^i_!u(F),v})",
    r"no underline markup; (P_{\R^i_!u(F),v})",
    "underline", "high",
    fx(r"Si les propriétés $(P_{F,u})$ et $(P_{\R^i_!u(F),v})$ pour tout $i$ sont vraies, alors "
       r"$(P_{F,v\circ u})$ est vraie.",
       r"\emph{Si les propriétés} $(P_{F,u})$ \emph{et} $(P_{\mathrm{R}^i_!u(F),v})$ \emph{pour tout} $i$ "
       r"\emph{sont vraies}, \emph{alors} $(P_{F,v\circ u})$ \emph{est vraie}."),
    "As the first sentence. The same edit writes the print's plain R in (P_{R^i_!u(F),v}) (\\R is \\mathbb{R} "
    "here; see the font findings): one edit because the old of a separate R fix could not avoid this one.")

add(466, "'En effet' before the display",
    "'En effet' with no punctuation", "En effet,",
    "punctuation", "high", fx(r"En effet,", r"En effet"),
    "Comma added by the TeX.")

add(466, "'En effet' display, first line (three R)",
    "L_F = ∏_i(L_{R^i_!u(F)})^{(-1)^i} = ∏_i(∏_j(L_{R^j_!v(R^i_!u(F))})...: plain typed R",
    r"\R three times",
    "font", "high",
    fx(r"L_F=\prod_i\bigl(L_{\R^i_!u(F)}\bigr)^{(-1)^i}<NL> =\prod_i\Bigl(\prod_j\bigl(L_{\R^j_!v(\R^i_!u(F))}",
       r"L_F=\prod_i\bigl(L_{\mathrm{R}^i_!u(F)}\bigr)^{(-1)^i}<NL> =\prod_i\Bigl(\prod_j\bigl(L_{\mathrm{R}^j_!v("
       r"\mathrm{R}^i_!u(F))}"),
    "As above (plain R). Does not touch the exponents of the misprint finding below.")

add(466, "'En effet' display, second member",
    "∏_i(∏_j(L_{R^j_!v(R^i_!u(F))})^{(-1)^i})^{(-1)^j}: inner exponent (-1)^i, outer (-1)^j",
    r"\prod_i\Bigl(\prod_j\bigl(L_{\R^j_!v(\R^i_!u(F))}\bigr)^{(-1)^i}\Bigr)^{(-1)^j} (the printed reading)",
    "misprint_in_print", "high", None,
    "The exponents are interchanged: the outer exponent (-1)^j uses the index of the inner product. By "
    "(P_{R^i_!u(F),v}), L_{R^i_!u(F)} = ∏_j(L_{R^j_!v(R^i_!u(F))})^{(-1)^j}, which gives the next line "
    "∏_{i,j}(...)^{(-1)^{i+j}}. The diplomatic TeX keeps the printed reading; the current layer already has a "
    "corrected form, '\\prod_i\\prod_j\\bigl(...\\bigr)^{(-1)^i(-1)^j}'. The corrected reading is given with the R "
    "of the font fix.",
    corrected=r"\prod_i\Bigl(\prod_j\bigl(L_{\mathrm{R}^j_!v(\mathrm{R}^i_!u(F))}\bigr)^{(-1)^j}\Bigr)^{(-1)^i}")

add(466, "'En effet' display, last line ∏_{i,j}",
    "plain typed R twice", r"\R^j_!v(\R^i_!u(F))",
    "font", "high",
    fx(r"=\prod_{i,j}\bigl(L_{\R^j_!v(\R^i_!u(F))}", r"=\prod_{i,j}\bigl(L_{\mathrm{R}^j_!v(\mathrm{R}^i_!u(F))}"),
    "As above (plain R).")

add(466, "'d'après (P_{F,u}) et (P_{R^i_!u(F),v}) . La suite spectrale'",
    "plain typed R", r"(P_{\R^i_!u(F),v})",
    "font", "high", fx(r"et $(P_{\R^i_!u(F),v})$. La", r"et $(P_{\mathrm{R}^i_!u(F),v})$. La"),
    "As above (plain R).")

add(466, "Leray spectral sequence R^j_!v(R^i_!u(F)) ⟹ R^k_!(vou)(F)",
    "plain typed R three times", r"\R^j_!v(\R^i_!u(F))\Longrightarrow \R^k_!(v\circ u)(F)",
    "font", "high",
    fx(r"\R^j_!v(\R^i_!u(F))\Longrightarrow \R^k_!(v\circ u)(F)",
       r"\mathrm{R}^j_!v(\mathrm{R}^i_!u(F))\Longrightarrow \mathrm{R}^k_!(v\circ u)(F)"),
    "As above (plain R). The display for a formula run into the line is not reported (layout).")

# ---------------------------------------------------------------- p. 467
add(467, "first display L_F = ∏_k(L_{R^k_!(vou)(F)})^{(-1)^k}",
    "plain typed R", r"L_{\R^k_!(v\circ u)(F)}",
    "font", "high", fx(r"L_{\R^k_!(v\circ u)(F)}", r"L_{\mathrm{R}^k_!(v\circ u)(F)}"),
    RNOTE)

add(467, "Lemme 3, first sentence",
    "underlined: 'Soit' | 'un schéma de type fini sur' | 'et soit' | 'son morphisme structural'",
    "no underline markup", "underline", "high",
    fx(r"Soit $X$ un schéma de type fini sur $\mathbb F_p$, et soit $g:X\to e$ son morphisme structural.",
       r"\emph{Soit} $X$ \emph{un schéma de type fini sur} $\mathbb F_p$, \emph{et soit} $g:X\to e$ "
       r"\emph{son morphisme structural}."),
    EMNOTE)

add(467, "Lemme 3 a), first sentence",
    "underlined: 'Considérons un' | 'faisceau constructible' (after the hyphen) | 'sur' | 'un' | 'sous-schéma "
    "fermé' | 'de' | 'et l'ouvert complémentaire'; 'a)' not underlined",
    "no underline markup", "underline", "high",
    fx(r"\item Considérons un $\Omega$-faisceau constructible $F$ sur $X$, un sous-schéma fermé $Y$ de $X$ et "
       r"l'ouvert complémentaire $U=X-Y$.",
       r"\item \emph{Considérons un} $\Omega$-\emph{faisceau constructible} $F$ \emph{sur} $X$, \emph{un "
       r"sous-schéma fermé} $Y$ \emph{de} $X$ \emph{et l'ouvert complémentaire} $U=X-Y$."),
    "As in Lemme 3.")

add(467, "Lemme 3 a), second sentence",
    "underlined: 'Si le théorème est vrai pour deux des couples' | 'il est vrai pour le troisième'",
    "no underline markup", "underline", "high",
    fx(r"Si le théorème est vrai pour deux des couples $(X,F)$, $(Y,F|Y)$, $(U,F|U)$, il est vrai pour le "
       r"troisième.",
       r"\emph{Si le théorème est vrai pour deux des couples} $(X,F)$, $(Y,F|Y)$, $(U,F|U)$, \emph{il est vrai "
       r"pour le troisième}."),
    "As in Lemme 3.")

add(467, "Lemme 3 b), 'Considérons une suite exacte'",
    "underlined: 'Considérons une suite exacte' (the sequence 0 --> F' --> F --> F\" --> 0 not)",
    "no underline markup", "underline", "high",
    fx(r"\item Considérons une suite exacte", r"\item \emph{Considérons une suite exacte}"),
    "As in Lemme 3.")

add(467, "Lemme 3 b), after the sequence",
    "underlined: 'de' | 'faisceaux constructibles sur' (after the hyphen) | 'si le théorème est vrai pour deux des "
    "couples' | 'il est vrai pour le troisième'",
    "no underline markup", "underline", "high",
    fx(r"de $\Omega$-faisceaux constructibles sur $X$; si le théorème est vrai pour deux des couples $(X,F')$, "
       r"$(X,F)$, $(X,F'')$, il est vrai pour le troisième.",
       r"\emph{de} $\Omega$-\emph{faisceaux constructibles sur} $X$; \emph{si le théorème est vrai pour deux des "
       r"couples} $(X,F')$, $(X,F)$, $(X,F'')$, \emph{il est vrai pour le troisième}."),
    "As in Lemme 3.")

add(467, "exact sequence after 'La suite exacte' (four R)",
    "... --> R^i_!g_U(F|U) --> R^i_!g(F) --> R^i_!g_Y(F|Y) --> R^{i+1}g_U(F|U) --> ...: all four R plain typed",
    r"\R four times",
    "font", "high",
    fx(r"\cdots\longrightarrow \R^i_!g_U(F|U)\longrightarrow \R^i_!g(F)<NL>\longrightarrow \R^i_!g_Y(F|Y)"
       r"\longrightarrow \R^{i+1}",
       r"\cdots\longrightarrow \mathrm{R}^i_!g_U(F|U)\longrightarrow \mathrm{R}^i_!g(F)<NL>\longrightarrow "
       r"\mathrm{R}^i_!g_Y(F|Y)\longrightarrow \mathrm{R}^{i+1}"),
    "As on p. 466 (plain R). Listed before the misprint fix of the same display; the two olds are disjoint.")

add(467, "same exact sequence, fourth term",
    "R^{i+1}g_U(F|U): no '!' under the R (the three other R of the sequence have it; the scan is clean there, "
    "crops_466_470/c467_ri1.png)",
    r"\R^{i+1}_!g_U(F|U) (silent correction)",
    "misprint_in_print", "high", fx(r"_!g_U(F|U)\longrightarrow\cdots", r"g_U(F|U)\longrightarrow\cdots"),
    "The exact sequence of cohomology with proper supports needs R^{i+1}_!. The fix removes only the '_!'.",
    corrected=r"\mathrm{R}^{i+1}_!g_U(F|U)")

add(467, "'et la proposition 1a) (n°1) donnent :'",
    "'donnent :' with a colon", "donnent, then the display, no colon",
    "punctuation", "high", fx(r"(n\textsuperscript{o}~1) donnent<NL>", r"(n\textsuperscript{o}~1) donnent:<NL>"),
    "Colon missing in the TeX.")

add(467, "product display, left member and first factor",
    "∏_i(L_{R^i_!g(F)})^{(-1)^i} = ∏_i(L_{R^i_!g_U(F|U)} ...: plain typed R", r"\R twice",
    "font", "high",
    fx(r"\prod_i\bigl(L_{\R^i_!g(F)}\bigr)^{(-1)^i}<NL>=\prod_i\bigl(L_{\R^i_!g_U",
       r"\prod_i\bigl(L_{\mathrm{R}^i_!g(F)}\bigr)^{(-1)^i}<NL>=\prod_i\bigl(L_{\mathrm{R}^i_!g_U"),
    "As above (plain R). The four edits of this display (two font, symbol, comma) are disjoint.")

add(467, "product display, between the two factors",
    "L_{R^i_!g_U(F|U)} · L_{R^i_!g_Y(F|Y)}: a product dot between the factors", r"\, (thin space only)",
    "symbol", "high", fx(r"(F|U)}\,L_{", r"(F|U)}\cdot L_{"),
    "The TeX drops the printed product dot (a typed dot, written \\cdot as the volume does for the typewriter's dot).")

add(467, "product display, second factor",
    "L_{R^i_!g_Y(F|Y)}: plain typed R", r"\R^i_!g_Y(F|Y)",
    "font", "high", fx(r"\R^i_!g_Y(F|Y)}", r"\mathrm{R}^i_!g_Y(F|Y)}"),
    "As above (plain R).")

add(467, "end of the product display",
    "no punctuation after (...)^{(-1)^i}; the next line is 'et la proposition 1b) (n°1) permet alors de conclure.'",
    r"\bigr)^{(-1)^i},",
    "punctuation", "high", fx(r"\bigr)^{(-1)^i},<NL>\]", r"\bigr)^{(-1)^i}<NL>\]"),
    "Comma added at the end of the display.")

# ---------------------------------------------------------------- p. 468
add(468, "top of the page: 'propres.' (folio-468 marker)",
    "p. 468 begins 'propres.', then the indented 'Utilisons maintenant les lemmes précédents ...'; p. 467 ends "
    "'... analogues à celles de la cohomologie à supports'",
    "'propres.' ends page_467.tex ('... la cohomologie à supports propres.' and a blank line); the folio-468 marker "
    "follows, and page_468.tex begins 'Utilisons maintenant'",
    "marker", "high", None,
    "Page 468 really begins at 'propres.'. Exact fix: python -I move_marker.py 5 468 'propres.' --before (simulated "
    "in memory on both layers: the marker moves back 10 characters to its own line between '... cohomologie à "
    "supports' and 'propres.'). Run it once only: a second run would move the marker to an earlier 'propres.' about "
    "452,000 characters back. Text not moved.")

add(468, "1ère Réduction: 'Il suffit donc de démontrer le théorème dans le cas où X est affine.'",
    "a new, indented paragraph after '... puisque X = ⋃_{i⩾1} U_i .'",
    "run on in the paragraph of the 1ère Réduction",
    "other", "high", fx(r"U_i$. Il suffit donc", r"U_i$.<NL><NL>Il suffit donc"),
    "Paragraph break; drop it if paragraphing is left to a global pass.")

add(468, "2ème Réduction: 'défini à partir d'un isomorphisme : E^n ≃ E^1 x E^{n-1}'",
    "'isomorphisme :' with a colon before the formula", r"'d'un isomorphisme $\mathbb E^n\simeq...' (no colon)",
    "punctuation", "high", fx(r"d'un isomorphisme $\mathbb E^n", r"d'un isomorphisme: $\mathbb E^n"),
    "Colon missing in the TeX.")

add(468, "end of page_468.tex, printed at the top of p. 469: '(E^1, R^i_!w(F))'",
    "plain typed R", r"\R^i_!w(F)",
    "font", "high", fx(r"\R^i_!w(F)", r"\mathrm{R}^i_!w(F)"),
    "As on p. 466 (plain R). Filed under p. 468 because the text stands in page_468.tex until the folio-469 marker is "
    "moved: apply before moving the marker (the old stays unique on p. 469 after the move; the move's anchor "
    "'$(\\mathbb E^1,' is not touched).")

# ---------------------------------------------------------------- p. 469
add(469, "top of the page: '(E^1, R^i_!w(F)) . On se ramène' (folio-469 marker)",
    "p. 469 begins '(E^1,R^i_!w(F)) . On se ramène ainsi au cas où X = E^1 est la droite affine.'; p. 468 ends "
    "'Grâce au lemme 2 on voit qu'il suffit d'établir le théorème pour les couples'",
    r"'$(\mathbb E^1,\R^i_!w(F))$. On se ramène' ends page_468.tex; the folio-469 marker follows, and page_469.tex "
    r"begins 'ainsi au cas où'",
    "marker", "high", None,
    "Page 469 really begins at '$(\\mathbb E^1,'. Exact fix: python -I move_marker.py 5 469 '$(\\mathbb E^1,' "
    "--before (simulated in memory on both layers: the marker moves back 41 characters to its own line between "
    "'... pour les couples' and '$(\\mathbb E^1,\\R^i_!w(F))$. On se ramène'; a second run prints 'anchor not "
    "found'). Text not moved.")

add(469, "3ème Réduction: '... au point à l'infini de P^1 ; comme le théorème est vrai'",
    "'P^1 ;' then a lower-case 'comme'", r"'de $\mathbb P^1$. Comme le théorème'",
    "punctuation", "high", fx(r"de $\mathbb P^1$. Comme", r"de $\mathbb P^1$; comme"),
    "Full stop for the print's semicolon, capital C for 'comme'.")

add(469, "3ème Réduction: '(comme i est une immersion ouverte on a : F = i_!(F)|E^1).'",
    "'on a :' with a colon", r"'on a $F=i_!(F)|\mathbb E^1$' (no colon)",
    "punctuation", "high", fx(r"ouverte on a $F", r"ouverte on a: $F"),
    "Colon missing in the TeX.")

add(469, "heading 'n°3. Démonstration du théorème.'",
    "underlined title ending with a full stop", r"\subsubsection*{n\textsuperscript{o} 3. Démonstration du théorème}",
    "punctuation", "high", fx(r"Démonstration du théorème}", r"Démonstration du théorème.}"),
    "Final full stop of an underlined title dropped (the \\subsubsection* setting is accepted).")

add(469, "display after 'Reprenons la formule (1) :'",
    "L_F = ∏_i(L_{R^i_!g(F)})^{(-1)^i}: plain typed R", r"L_{\R^i_!g(F)}",
    "font", "high", fx(r"L_{\R^i_!g(F)}", r"L_{\mathrm{R}^i_!g(F)}"),
    "As on p. 466 (plain R).")

# ---------------------------------------------------------------- p. 470
add(470, "top of the page (folio-470 marker): the display ∑_{n⩾1}(∑_i(-1)^i Tr(f^{-n}_{H^i_!(X̄,F̄)}))t^n/n",
    "p. 470 begins with the display ∑_{n⩾1}(...)t^n/n ., then 'En comparant les coefficients ...'; p. 469 ends "
    "with the display ∑_{x∈X°}∑_{n=1}^∞ Tr(...)t^{nd(x)}/n = ∑_{n=1}^∞(...)t^n/n and 'tandis que celui du second "
    "membre est :'",
    r"page_470.tex begins with the display '\sum_{x\in X^0}...' and 'tandis que celui du second membre est', both "
    r"printed on p. 469",
    "marker", "high", None,
    "Page 470 really begins at the '\\[' of the display '\\sum_{n\\ge1}...'. Exact fix (bash): python -I "
    "move_marker.py 5 470 $'\\\\[\\n\\\\sum_{n\\\\ge1}' (forward; the anchor is '\\[', a line break, "
    "'\\sum_{n\\ge1}', unique in s5.tex; simulated in memory on both layers: the marker moves forward 204 "
    "characters to its own line between 'membre est' and '\\['; a second run leaves it there). The two fixes filed "
    "under p. 470 for the moved lines (comma, colon) keep a unique old on p. 469 after the move. Text not moved.")

add(470, "display ∑_{x∈X°} ... = ∑_{n=1}^∞(∑_{d(x)|n} ...)t^n/n (printed on p. 469)",
    "no punctuation after t^n/n; the next line is 'tandis que celui du second membre est :'", r"t^n/n,",
    "punctuation", "high", fx(r"t^n/n,<NL>\]", r"t^n/n<NL>\]"),
    "Comma added at the end of the display. Printed on p. 469 (marker finding above).")

add(470, "'tandis que celui du second membre est :' (printed on p. 469)",
    "'membre est :' with a colon", "membre est (no colon)",
    "punctuation", "high", fx(r"membre est", r"membre est:"),
    "Colon missing in the TeX. Printed on p. 469 (marker finding above).")

add(470, "'les morphismes de Frobenius Fr*_{F_ν/X} définissent'",
    "Fr*_{F_ν/X} with no bar over Fr (double-underlined Fr, star above), clean scan "
    "(crops_466_470/c470_fr1.png); the bars appear only in the two pairs (f̄r̄_X, F̄r̄*_{...}) further down",
    r"\overline{\Fr}^*_{F_\nu/X}",
    "formula", "high", fx(r"\overline{\Fr}^*_{F_\nu/X}$ définissent", r"\Fr^*_{F_\nu/X}$ définissent"),
    "Bar added by the TeX. The print may intend the base change to X̄ here (its display writes fr*_X(F̄) --> F̄ with "
    "bars only on F), but the TeX's bar is not printed, and the TeX leaves fr_X without one.")

add(470, "display 'Fr*_{F/X} : fr*_X(F̄) --> F̄ , d'où une correspondance'",
    "no bar over Fr (nor over fr)", r"\overline{\Fr}^*_{F/X}:\fr_X^*(\bar F)",
    "formula", "high", fx(r"\overline{\Fr}^*_{F/X}:\fr_X^*", r"\Fr^*_{F/X}:\fr_X^*"),
    "As the previous finding. The pairs (\\bar{\\fr}_X,\\overline{\\Fr}^*_{F_\\nu/X}) and "
    "(\\bar{\\fr}_X,\\overline{\\Fr}^*_{F/X}) agree with the print.")

add(470, "'est l'inverse de f_{RΓ_X̄(F̄)} (§2, n°3, corollaire de la proposition 3)'",
    "f_{RΓ_X̄(F̄)}: F̄ without the index ν (crops_466_470/c470_fRG.png), while the endomorphism inverted is "
    "fr_{RΓ_X̄(F̄_ν)}",
    r"f_{\R\Gamma_{\bar X}(\bar F)} (the printed reading)",
    "misprint_in_print", "medium", None,
    "An endomorphism of RΓ_X̄(F̄_ν) is the inverse of f on the same object: the index ν is missing (the sentence "
    "begins 'Pour chaque entier ν'). The TeX keeps the printed reading. Both RΓ here have a double-underlined R, so "
    "\\R is right.",
    corrected=r"f_{\R\Gamma_{\bar X}(\bar F_\nu)}")

add(470, "'est l'inverse de f_{H^i(X̄,F̄)} ; ainsi :'",
    "'ainsi :' with a colon (faint but both dots visible, crops_466_470/c470_ainsi.png)",
    "'; ainsi' then the display, no colon",
    "punctuation", "medium", fx(r"$; ainsi", r"$; ainsi:"),
    "Colon missing in the TeX.")

add(470, "'pour tout n ⩾ 1 et tout i .' / 'Appliquons ce résultat ...'",
    "'Appliquons ce résultat dans le cas particulier ...' starts at the left margin after the display, not "
    "indented (new paragraphs on these pages are indented: 'Transformons encore', p. 469 'Au bout de ces "
    "réductions', 'Reprenons'): the paragraph goes on",
    "a blank line before 'Appliquons' (new paragraph)",
    "other", "medium", fx(r"et tout $i$.<NL><NL>Appliquons", r"et tout $i$.<NL>Appliquons"),
    "Paragraph break added by the TeX; drop it if paragraphing is left to a global pass.")

add(470, "end of the page (folio-471 marker): the display f^{-n}_{F_x̄} = fr^n_{F_x̄} = (Fr*_{F_x̄/x̄})^n",
    "p. 470 ends 'Nous obtenons :' and the footnote (*); p. 471 begins with the display "
    "f^{-n}_{F_x̄} = fr^n_{F_x̄} = (Fr*_{F_x̄/x̄})^n (b471_475/page_471_s1.png)",
    r"the display '\[ f^{-n}_{F_{\bar x}}=\fr^n_{F_{\bar x}}=(\Fr^*_{F_{\bar x}/\bar x})^n \]' ends page_470.tex; "
    r"the folio-471 marker follows it",
    "marker", "high", None,
    "Page 471 really begins at the '\\[' of that display. Exact fix (bash): python -I move_marker.py 5 471 "
    "$'\\\\[\\nf^{-n}_{F_{\\\\bar x}}' --before (the anchor is '\\[', a line break, 'f^{-n}_{F_{\\bar x}}', unique "
    "in s5.tex; simulated in memory on both layers: the marker moves back 75 characters to its own line between "
    "'Nous obtenons:' and '\\['; a second run prints 'anchor not found'). Batch 471-475 may report the same move: "
    "apply it once. Text not moved; the display agrees with the print of p. 471 apart from the double-underlined "
    "fr/Fr (convention, see the message).")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(len(F), "findings written to", OUT)
