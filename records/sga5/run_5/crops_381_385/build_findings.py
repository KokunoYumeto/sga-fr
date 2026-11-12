"""Build findings_381_385.json and check every fix's old string.

Checks: each old occurs exactly once in its page_NNN.tex; olds of one page do not overlap; each old is also looked up
in the same page span of the current layer (reported, not required).
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
BATCH = RUN / "b381_385"
OUT = RUN / "findings_381_385.json"
CUR = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\current\s5.tex")
DIP = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex")
NL = "\u23ce"  # stands for a line break inside old/new

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def mp(page, where, scan, tex, conf, corrected, note, old=None, new=None):
    add(page, where, scan, tex, "misprint_in_print", conf, old, new, note, corrected)


# ---------------------------------------------------------------- p. 381
add(381, "top of the page (folio-381 marker)",
    "p. 381 begins with 'K°(Λ[G]) et K°(Γ[G]) .' (end of the sentence of p. 380), then 'Soit A un algèbre sur Λ et'; "
    "p. 380 ends '... commute aux involutions x ⟶ x̌ sur'",
    "the last line of page_380.tex is 'commute aux involutions $x\\longmapsto \\check x$ sur $K^{\\bullet}(\\Lambda[G])$ "
    "et $K^{\\bullet}(\\Gamma[G])$.'; page_381.tex begins with 'Soit $A$'",
    "marker", "high",
    note="Page 381 really begins at '$K^{\\bullet}(\\Lambda[G])$ et $K^{\\bullet}(\\Gamma[G])$.' in the last line of "
         "page_380.tex (diplomatic s5.tex line 12937, current 12933 at the batch extraction). Exact fix: python -I move_marker.py 5 381 "
         "'$K^{\\bullet}(\\Lambda[G])$ et $K^{\\bullet}(\\Gamma[G])$' --before (single quotes keep $ and backslashes; "
         "simulated in memory on both layers: the line is split after 'sur ' and the marker stands on its own line "
         "before '$K^{\\bullet}(\\Lambda[G])$ et ...'). Text not moved; the moving words read as the print. Live layers (s5.tex as modified 12 Nov "
         "16:17): the marker already stands there (diplomatic line 12952, current 12948); the command then prints "
         "'anchor not found' and changes nothing.")

mp(381, "'Soit A un algèbre sur Λ et'", "un algèbre", "Soit $A$ un algèbre sur $\\Lambda$ et (as printed)",
   "high", "Soit $A$ une algèbre sur $\\Lambda$",
   "Gender slip of the typescript (algèbre is feminine). The TeX keeps the printed reading; the current layer has "
   "'une algèbre'.")

add(381, "'Un complexe X° de A[G]-modules étant donné, ...' after the display A[G] = Λ[G] ⊗_Λ A .",
    "a new, indented paragraph (as 'Soit A un algèbre' above it)", "runs on after the display (no blank line)",
    "other", "high", "\\]" + NL + "Un complexe", "\\]" + NL + NL + "Un complexe",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

mp(381, "'qui associe à chaque A[G]-module X de module sur A formé par ...'", "X de module sur A",
   "$X$ de module sur $A$ (as printed)", "high", "$X$ le module sur $A$",
   "'de' for 'le'. The TeX keeps the printed reading; the current layer has 'le module'.")

add(381, "statement of Proposition 3.8 (first part, up to 'et M')",
    "underlined: 'Soient' | 'un groupe fini' | 'un complexe borné de' | '-modules dont toutes les composantes sont "
    "projectives de type fini' | 'et'; not underlined: G, P°, Λ[G], the commas, M",
    "Soient $G$ un groupe fini, $P^\\bullet$ un complexe borné de ... de type fini, et $M (statement environment, no "
    "underline)",
    "underline", "high",
    "Soient $G$ un groupe fini, $P^\\bullet$ un complexe borné de $\\Lambda[G]$-modules dont toutes les composantes "
    "sont projectives de type fini, et $M",
    "\\emph{Soient} $G$ \\emph{un groupe fini}, $P^\\bullet$ \\emph{un complexe borné de} $\\Lambda[G]$-\\emph{modules "
    "dont toutes les composantes sont projectives de type fini}, \\emph{et} $M",
    "Exposé X's statement environment sets the text upright with no underline markup; the print underlines the "
    "statement word group by word group (as Exposé III B and V; \\emph is this exposé's command for the print's "
    "underline, e.g. \\emph{l'invariant local de Nielsen-Wecken}). Split at '$M' so that the edit also matches the "
    "current layer ('$M^\\bullet$'); the next item continues the statement.")

mp(381, "statement of Proposition 3.8, 'et M un complexe de A[G]-modules'", "M without the raised dot",
   "et $M$ un complexe (as printed)", "medium", "et $M^\\bullet$ un complexe",
   "M is the complex M° everywhere else (P̌° ⊗ M° in (3.8.1), Hom°(P°,M°) and M° in the remark). The TeX keeps the "
   "printed reading; the current layer has $M^\\bullet$.")

add(381, "statement of Proposition 3.8 (second part)",
    "underlined: 'un complexe de' | 'modules' | 'Sous ces conditions il existe des isomorphismes canoniques de "
    "complexes de' | 'modules'; not underlined: A[G], A, the hyphens, the full stop, the colon",
    "un complexe de $A[G]$-modules. Sous ces conditions ... de $A$-modules: (no underline)",
    "underline", "high",
    "un complexe de $A[G]$-modules. Sous ces conditions il existe des isomorphismes canoniques de complexes de "
    "$A$-modules:",
    "\\emph{un complexe de} $A[G]$-\\emph{modules}. \\emph{Sous ces conditions il existe des isomorphismes canoniques "
    "de complexes de} $A$-\\emph{modules}:",
    "Continues the previous item (independent edits).")

mp(381, "display (3.8.1), first two terms", "Hom°_{Λ[G]}(P°,M) ≃ Hom°_Λ(P°,M)^G : M without the raised dot "
   "(the last two terms have M°)",
   "\\Hom_{\\Lambda[G]}^\\bullet(P^\\bullet,M) \\simeq \\Hom_\\Lambda^\\bullet(P^\\bullet,M)^G (as printed)",
   "medium", "\\Hom_{\\Lambda[G]}^\\bullet(P^\\bullet,M^\\bullet)\n\\simeq \\Hom_\\Lambda^\\bullet(P^\\bullet,M^\\bullet)^G",
   "Missing raised dots. The TeX keeps the printed reading; the current layer has M^\\bullet in both.")

add(381, "'La démonstration utilise les isomorphismes bien-connus'", "bien-connus (hyphenated, on one line)",
    "bien connus", "punctuation", "high", "bien connus", "bien-connus", "")

mp(381, "'Noter que dans les deuxième et troisième terme'", "troisième terme, (singular)",
   "deuxième et troisième terme (as printed)", "low", "deuxième et troisième termes",
   "Agreement slip (two terms). The TeX keeps the printed reading, as does the current layer; list only if the "
   "corrected edition fixes grammar slips.")

mp(381, "'à partir do ses opérations'", "do ses", "à partir do ses (as printed)", "high", "à partir de ses",
   "The TeX keeps the printed reading; the current layer has 'de ses'.")

mp(381, "'resp. P̌° et M̌° .' (end of the remark)", "P̌° et M̌° : a hand-drawn check over M as well",
   "resp. $\\check P^\\bullet$ et $\\check M^\\bullet$ (as printed)", "medium",
   "resp. $\\check P^\\bullet$ et $M^\\bullet$",
   "The operations on P̌° ⊗_Λ M° come from those on P̌° and M°; M is not dualized. The TeX keeps the printed "
   "reading; the current layer has $M^\\bullet$.")

add(381, "statement of Corollaire 3.9",
    "underlined: 'Si' | 'et' | 'alors on a dans la catégorie dérivée' | 'les isomorphismes suivants'; not "
    "underlined: the formulas, D(A), the colon",
    "Si $P^\\bullet\\in ...$ et $M^\\bullet\\in D^+(A[G])$ alors on a ... suivants: (no underline)",
    "underline", "high",
    "Si $P^\\bullet\\in \\operatorname{Ob}(D(\\Lambda[G])_{\\parf})$ et $M^\\bullet\\in D^+(A[G])$ alors on a dans la "
    "catégorie dérivée $D(A)$ les isomorphismes suivants:",
    "\\emph{Si} $P^\\bullet\\in \\operatorname{Ob}(D(\\Lambda[G])_{\\parf})$ \\emph{et} $M^\\bullet\\in D^+(A[G])$ "
    "\\emph{alors on a dans la catégorie dérivée} $D(A)$ \\emph{les isomorphismes suivants}:",
    "As Proposition 3.8.")

add(381, "display (3.9.1), the L over the tensor sign of ℝΓ^G(P̌° ⊗^L_Λ M)",
    "a hand-drawn L, blotted: an ink blot with white flecks inside the stem, as the hand-drawn double-struck L of "
    "p. 382",
    "\\otimes_\\Lambda^{\\mathbf L} (bold L)", "font", "low",
    "=\\R\\Gamma^G(\\check P^\\bullet\\otimes_\\Lambda^{\\mathbf L}",
    "=\\R\\Gamma^G(\\check P^\\bullet\\otimes_\\Lambda^{\\mathbb{L}}",
    "The two R of (3.9.1) are double-struck as \\RHom and \\R (= \\mathbb{R}) render; the L is too blotted to be "
    "sure, but the same hand's L on p. 382 is clearly double-struck (three places, itemized there).")

mp(381, "display (3.9.1), ℝΓ^G(P̌° ⊗^L_Λ M)", "M without the raised dot",
   "\\otimes_\\Lambda^{\\mathbf L}M) (as printed)", "medium",
   "\\R\\Gamma^G(\\check P^\\bullet\\otimes_\\Lambda^{\\mathbb{L}}M^\\bullet)",
   "The TeX keeps the printed reading; the current layer has M^\\bullet.")

mp(381, "'En effet grâce à l'hypothèse P° ∈ D(Λ[G]_parf on peut supposer'",
   "D(Λ[G]_parf : no closing parenthesis after [G] (magnified: the subscript parf follows the bracket directly)",
   "D(\\Lambda[G])_{\\parf} (silently corrected)", "high", "D(\\Lambda[G])_{\\parf}",
   "Restores the printed reading in the diplomatic layer; the corrected layer keeps D(\\Lambda[G])_{\\parf} "
   "(Corollaire 3.9 prints Ob(D(Λ[G])_parf) with both parentheses).",
   old="D(\\Lambda[G])_{\\parf}$ on peut", new="D(\\Lambda[G]_{\\parf}$ on peut")

add(381, "display 'R Hom_{Λ[G]}(P°,M°) = Hom°_{Λ[G]}(P°,M°)' (printed at the top of p. 382)",
    "a plain typed R (the R of (3.9.1) just above is a hand-drawn double-struck R)",
    "\\RHom (= \\mathbb{R}\\mathrm{Hom} in this part of s5.tex)", "font", "high",
    "\\RHom_{\\Lambda[G]}(P^\\bullet,M^\\bullet)=\\Hom", "\\mathrm{R}\\Hom_{\\Lambda[G]}(P^\\bullet,M^\\bullet)=\\Hom",
    "Printed on p. 382; filed under p. 381, where the display stands until the folio-382 marker move (the edit does "
    "not touch the move's anchor).")

# ---------------------------------------------------------------- p. 382
add(382, "top of the page (folio-382 marker)",
    "p. 382 begins with 'fini. On a donc', then the display 'R Hom_{Λ[G]}(P°,M°) = Hom°_{Λ[G]}(P°,M°)' and 'et on "
    "peut utiliser ...'; p. 381 ends '... sont projectives de type'",
    "page_381.tex goes on with 'fini. On a donc', the display and 'et on'; page_382.tex begins with 'peut utiliser'",
    "marker", "high",
    note="Page 382 really begins at 'fini. On a donc' (end of the line 'En effet grâce à l'hypothèse ...'; "
         "diplomatic s5.tex line 12984, current 12980 in the live files of 16:17). Exact fix: python -I move_marker.py 5 382 'fini. On a donc' "
         "--before (simulated in memory on both layers: the line is split after 'projectives de type ' and the "
         "marker stands on its own line before 'fini. On a donc'). Text not moved. The plain-R fix of the display is "
         "filed under p. 381.")

mp(382, "'et on peut utiliser les isomorphismes (4.3.4)'", "(4.3.4)", "(4.3.4) (as printed)", "medium", "(3.8.1)",
   "The isomorphisms used are those of Proposition 3.8; there is no (4.3.4) before this point. The TeX keeps the "
   "printed reading (s5.tex comment: 'scan p382 prints reference (4.3.4) exactly'); the current layer has (3.8.1).")

add(382, "first formula 'P̌° ⊗_{Λ[G]} M° ≅ P̌° ⊗^L_{Λ[G]} M°'",
    "≅: a hand-drawn tilde over a typed '=' (two bars; magnified), unlike the ≃ (tilde over one bar) of (3.8.1), "
    "(3.9.1) and the RΓ display",
    "\\simeq", "symbol", "medium", "M^\\bullet\\simeq \\check P", "M^\\bullet\\cong \\check P", "")

add(382, "first formula, the L over the second tensor sign", "a hand-drawn double-struck L (doubled stem)",
    "\\otimes_{\\Lambda[G]}^{\\mathbf L} (bold L)", "font", "high",
    "\\otimes_{\\Lambda[G]}^{\\mathbf L}", "\\otimes_{\\Lambda[G]}^{\\mathbb{L}}", "")

mp(382, "'De même P̌° ⊗_Λ M° – P̌° ⊗^L_Λ M°'",
   "a single short dash between the two tensor products, no second bar and no tilde (magnified)",
   "= (silently corrected)", "medium", "M^\\bullet=\\check P^\\bullet",
   "The typist's '-' was never completed to '=' (or to ≃ with a hand-drawn tilde, as in the formula before it). "
   "Restores the printed reading in the diplomatic layer; the corrected layer keeps '='.",
   old="M^\\bullet=\\check P^\\bullet", new="M^\\bullet-\\check P^\\bullet")

add(382, "'De même ...', the L over the second tensor sign", "a hand-drawn double-struck L (doubled stem)",
    "\\otimes_\\Lambda^{\\mathbf L}", "font", "high",
    "\\otimes_\\Lambda^{\\mathbf L}M^\\bullet$", "\\otimes_\\Lambda^{\\mathbb{L}}M^\\bullet$", "")

add(382, "'les composantes du complexe P̌° ⊗ M° sont cohomologiquement triviales'",
    "P̌° ⊗ M° : no index under the tensor sign (clean paper below it)",
    "\\check P^\\bullet\\otimes_\\Lambda M^\\bullet", "extra", "high",
    "complexe $\\check P^\\bullet\\otimes_\\Lambda M^\\bullet$ sont", "complexe $\\check P^\\bullet\\otimes M^\\bullet$ sont",
    "The TeX adds the index Λ.")

add(382, "display 'R Γ^G(P̌° ⊗^L_Λ M°) ≃ (P̌° ⊗_Λ M°)^G .', the R", "a plain typed R",
    "\\R (= \\mathbb{R})", "font", "high", "\\[" + NL + "\\R\\Gamma^G(\\check P",
    "\\[" + NL + "\\mathrm{R}\\Gamma^G(\\check P", "")

add(382, "same display, the L over the first tensor sign",
    "a hand-drawn L with a doubled stem (white flecks inside the heavy stem), as the two L above", "\\mathbf L",
    "font", "medium", "\\otimes_\\Lambda^{\\mathbf L}M^\\bullet)", "\\otimes_\\Lambda^{\\mathbb{L}}M^\\bullet)", "")

add(382, "heading '4. La représentation de Swan.'", "a full stop after the underlined title",
    "\\subsection*{4. La représentation de Swan}", "punctuation", "high",
    "\\subsection*{4. La représentation de Swan}", "\\subsection*{4. La représentation de Swan.}", "")

add(382, "'son anneau local O_{E,x} (ou simplement O_x) est un anneau'", "parentheses, no commas",
    ", ou simplement $\\mathcal O_x$,", "punctuation", "high",
    "$\\mathcal O_{E,x}$, ou simplement $\\mathcal O_x$, est", "$\\mathcal O_{E,x}$ (ou simplement $\\mathcal O_x$) est",
    "")

add(382, "statement of Lemme 4.1, up to 'alors la multiplicité'",
    "underlined: 'Soient' | 'une courbe algébrique lisse sur le corps' | 'algébriquement clos et' | 'un endomorphisme "
    "de' | 'différent de l'identité' | 'Supposons que' | 'est un point fixe isolé de' | 'et soit' | 'une "
    "uniformisante de' | 'Si' | 'est la valuation de' | 'correspondante' | 'alors la multiplicité'; letters, "
    "formulas, full stops and the comma after 'correspondante' not underlined",
    "no underline (statement environment)", "underline", "high",
    "Soient $E$ une courbe algébrique lisse sur le corps $k$ algébriquement clos et $g:E\\to E$ un endomorphisme de $E$ "
    "différent de l'identité. Supposons que $x\\in E$ est un point fixe isolé de $g$ et soit $\\pi$ une uniformisante "
    "de $\\mathcal O_{E,x}$. Si $v_x$ est la valuation de $\\mathcal O_{E,x}$ correspondante, alors la multiplicité",
    "\\emph{Soient} $E$ \\emph{une courbe algébrique lisse sur le corps} $k$ \\emph{algébriquement clos et} $g:E\\to E$ "
    "\\emph{un endomorphisme de} $E$ \\emph{différent de l'identité}. \\emph{Supposons que} $x\\in E$ \\emph{est un point "
    "fixe isolé de} $g$ \\emph{et soit} $\\pi$ \\emph{une uniformisante de} $\\mathcal O_{E,x}$. \\emph{Si} $v_x$ \\emph{est "
    "la valuation de} $\\mathcal O_{E,x}$ \\emph{correspondante}, \\emph{alors la multiplicité}",
    "As Proposition 3.8. This edit, the ν edit and the end of the statement (next two items) touch adjacent, "
    "non-overlapping text.")

add(382, "Lemme 4.1, 'la multiplicité ν_x(g) du point fixe'",
    "ν_x(g): a hand-drawn Greek nu (the valuation v_x of the same statement is the typed Latin v)",
    "$v_x(g)$", "symbol", "high", "$v_x(g)$", "$\\nu_x(g)$",
    "The print writes the multiplicity ν and the valuation v (Lemme 4.1: ν_x(g) = v_x(g(π)-π)); the TeX writes v for "
    "both. Same on pp. 383-385, itemized there.")

add(382, "statement of Lemme 4.1, end", "underlined: 'du point fixe' | 'de l'application' | 'est égale à'; x, g, "
    "'(IV )' and the formula not underlined",
    "no underline", "underline", "high",
    " du point fixe $x$ de l'application $g$ (IV) est égale à $v_x(g(\\pi)-\\pi)$.",
    " \\emph{du point fixe} $x$ \\emph{de l'application} $g$ (IV) \\emph{est égale à} $v_x(g(\\pi)-\\pi)$.", "")

# ---------------------------------------------------------------- p. 383
add(383, "'Dans le produit E x E la diagonale et le graphe'", "no comma after E x E", "$E\\times E$, la diagonale",
    "punctuation", "high", "$E\\times E$, la diagonale", "$E\\times E$ la diagonale", "")

mp(383, "displayed immersions 'γ : E ⟶ E x E' (two lines)", "γ in both lines (magnified)",
   "\\gamma:E\\longrightarrow E\\times E,\\qquad \\gamma:E\\longrightarrow E\\times E (as printed)", "high",
   "\\delta:E\\longrightarrow E\\times E,\\qquad\n\\gamma:E\\longrightarrow E\\times E",
   "The first map is the diagonal immersion δ (δ(x) below). The TeX keeps the printed reading; the current layer "
   "has \\delta.")

add(383, "displayed immersions, between the two maps", "the two maps stand on two lines with no punctuation",
    "a comma after the first map (,\\qquad)", "punctuation", "high", "E\\times E,\\qquad", "E\\times E\\qquad",
    "The TeX adds the comma.")

mp(383, "display 'γ*, ν* : A ⊗̂ A ⟶ A ( A = Ô_x) ,'", "γ*, ν* (a stray dot mark above the γ*)",
   "\\gamma^*,\\nu^* (as printed)", "high", "\\delta^*,\\gamma^*",
   "The homomorphisms of δ and γ (next display). The TeX keeps the printed reading; the current layer has "
   "\\delta^*,\\gamma^*.")

mp(383, "display 'γ*(a ⊗ b) = ab'", "γ* in the first line", "\\gamma^*(a\\otimes b)=ab (as printed)", "high",
   "\\delta^*(a\\otimes b)=ab",
   "The product map is δ*; γ*(a ⊗ b) = ag*(b) is the second line. The TeX keeps the printed reading; the current "
   "layer has \\delta^*.")

add(383, "display 'γ*(a ⊗ b) = ab / γ*(a ⊗ b) = ag*(b) .'", "no comma after 'ab' (two lines; the full stop after "
    "the second is printed)", "ab,\\qquad", "punctuation", "high", "ab,\\qquad", "ab\\qquad", "The TeX adds the comma.")

add(383, "'Il s'agit d'évaluer la multiplicité ν_x(g) du point δ(x)'", "ν_x(g): Greek nu", "$v_x(g)$", "symbol",
    "high", "multiplicité $v_x(g)$ du point $\\delta(x)$", "multiplicité $\\nu_x(g)$ du point $\\delta(x)$",
    "As Lemme 4.1.")

add(383, "display 'ν_x(g) = v_x(γ*(1 ⊗ π - π ⊗ 1)) = v_x(g(π)-π) , cqfd.'", "left side ν_x(g) (Greek nu); "
    "the two v_x are Latin", "v_x(g)=v_x\\bigl(", "symbol", "high", "v_x(g)=v_x\\bigl(", "\\nu_x(g)=v_x\\bigl(", "")

add(383, "numbered paragraph '4.2.'", "4.2. (with a full stop)", "\\subsubsection*{4.2}", "punctuation", "high",
    "\\subsubsection*{4.2}", "\\subsubsection*{4.2.}", "As the logged '4.10.' of p. 304.")

mp(383, "'désignons par K = k(η son corps de fonctions rationnelles'",
   "k( η with no closing parenthesis: only two small specks at the top right of the hand-drawn η, nothing at the "
   "baseline where a typed ')' would stand", "$K=k(\\eta)$ (silently corrected)", "low", "$K=k(\\eta)$",
   "Low: the η is written by hand in a gap and a ')' hidden by its long right stroke cannot be excluded. Restores "
   "the printed reading in the diplomatic layer only.",
   old="$K=k(\\eta)$", new="$K=k(\\eta$")

add(383, "'Soit' before the display K' ⊃ K", "'Soit' stands flush left on the line after '... rationnelles.' "
    "(new paragraphs of this typescript are indented)", "a blank line before 'Soit' (new paragraph)", "other", "low",
    "rationnelles." + NL + NL + "Soit", "rationnelles." + NL + "Soit",
    "The print continues the paragraph of 4.2 on a new line; low because a flush-left line before a display may be "
    "the typist's layout only. Drop it if paragraphing is left to a global pass.")

mp(383, "display 'K' ⊃ K , [K':K] == n'",
   "two equals signs side by side after the bracket (the first lighter; magnified)", "[K':K]=n (silently corrected)",
   "medium", "[K':K]=n", "A doubled typed '='. Restores the printed reading in the diplomatic layer only.",
   old="[K':K]=n", new="[K':K]==n")

# ---------------------------------------------------------------- p. 384
add(384, "top of the page (folio-384 marker)",
    "p. 384 begins with the display 'p : C' ⟶ C', then 'la projection canonique .'; p. 383 ends '... Désignons par "
    "C' la normalisée de C dans K' et soit'",
    "the display '\\[ p:C'\\longrightarrow C \\]' and 'la' end page_383.tex; page_384.tex begins with 'projection "
    "canonique'", "marker", "high",
    note="Page 384 really begins at the '\\[' that opens 'p:C'\\longrightarrow C' (diplomatic s5.tex line 13041, "
         "current 13037 in the live files of 16:17). Exact fix (bash): python -I move_marker.py 5 384 $'\\\\[\\np:C' --before (simulated in "
         "memory on both layers: the marker then stands on its own line between '... dans $K'$ et soit' and '\\['). "
         "Text not moved.")

add(384, "'et si s ∈ G_{y'} s ≠ e posons'", "no comma after G_{y'} and none after s ≠ e",
    "$s\\in G_{y'}$, $s\\ne e$, posons", "punctuation", "high", "$s\\in G_{y'}$, $s\\ne e$, posons",
    "$s\\in G_{y'}$ $s\\ne e$ posons", "The TeX adds both commas.")

add(384, "(4.2.1) 'v_{y'}(s(π)-π) = ν_{y'}(s)'", "right side ν_{y'}(s) (Greek nu)", "=v_{y'}(s)", "symbol", "high",
    "=v_{y'}(s)" + NL + "\\tag{4.2.1}", "=\\nu_{y'}(s)" + NL + "\\tag{4.2.1}", "As Lemme 4.1.")

mp(384, "'(la multiplicité du point fixe y' pour l'application s : C' ⟶ C' (lemme 5.1)).'", "(lemme 5.1)",
   "(lemme 5.1) (as printed)", "high", "(lemme 4.1)",
   "The fixed-point multiplicity is Lemme 4.1 (p. 382). The TeX keeps the printed reading (its comment says so); "
   "the current layer has (lemme 4.1).")

add(384, "'La représentation de Swan associée à y' est définie'", "'La représentation de Swan' underlined (defined term)",
    "no underline", "underline", "high", "La représentation de Swan associée",
    "\\emph{La représentation de Swan} associée", "")

add(384, "'... caractère σ_{y'} , qui est donné par la formule :'", "a colon after 'formule'", "formule (no colon)",
    "punctuation", "high", "qui est donné par la formule", "qui est donné par la formule:",
    "The file writes such colons without a space (p. 380 'par la formule:').")

add(384, "(4.2.2), first row '1 - ν_{y'}(s) si s ≠ e'",
    "ν (Greek nu); the word 'si' before the condition; no commas",
    "1-v_{y'}(s),& s\\ne e,\\\\[0.4em]", "formula", "high",
    "\\sigma_{y'}(s)=" + NL + "\\begin{cases}" + NL + "1-v_{y'}(s),& s\\ne e,\\\\[0.4em]",
    "\\sigma_{y'}(s)=" + NL + "\\begin{cases}" + NL + "1-\\nu_{y'}(s)& \\text{si } s\\ne e\\\\[0.4em]",
    "Three differences in one row: v for ν, 'si' missing, two commas added. \\text{si } as at s5.tex line 13651.")

add(384, "(4.2.2), second row 'Σ_{s≠e} (ν_{y'}(s)-1) si s = e .'",
    "ν (Greek nu); 'si' before s = e; no comma; the full stop is printed",
    "\\bigl(v_{y'}(s)-1\\bigr),& s=e.", "formula", "high",
    "\\bigl(v_{y'}(s)-1\\bigr),& s=e.", "\\bigl(\\nu_{y'}(s)-1\\bigr)& \\text{si } s=e.",
    "A small stroke after the e (e´) is a stray mark, not a prime.")

add(384, "'Les résultats de Artin-Serre-Swan ...' after (4.2.2)", "a new, indented paragraph",
    "runs on after the display (no blank line)", "other", "high", "\\tag{4.2.2}" + NL + "\\]" + NL + "Les ",
    "\\tag{4.2.2}" + NL + "\\]" + NL + NL + "Les ",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

mp(384, "'Les résultats de Artin-Serre-Swan'", "de Artin (no elision)", "d'Artin (silently corrected)", "medium",
   "Les résultats d'Artin",
   "p. 385 prints 'la représentation d'Artin'. Restores the printed reading in the diplomatic layer only; the en "
   "dashes are the next item.",
   old="résultats d'", new="résultats de ")

add(384, "'Artin-Serre-Swan'", "hyphens", "Artin--Serre--Swan (en dashes)", "punctuation", "high",
    "Artin--Serre--Swan", "Artin-Serre-Swan", "The typescript's hyphens (as the joint names elsewhere).")

add(384, "'(IX Th 4)'", "Th without a full stop", "(IX Th. 4)", "punctuation", "high", "(IX Th. 4)", "(IX Th 4)",
    "The TeX adds the abbreviation's full stop.")

mp(384, "(4.2.3) 'Sw'_{y'} = Sw_{y'} ⊗ Z_ℓ [G_{y'}]'", "⊗ (a cross in the circle; magnified)",
   "Sw_{y'}\\otimes\\mathbb Z_\\ell[G_{y'}] (as printed)", "high", "Sw_{y'}\\oplus\\mathbb Z_\\ell[G_{y'}]",
   "Direct sum: σ' = σ + the regular character gives (4.2.4) (s ≠ e: 1 - ν; s = e: Σ(ν-1) + |G| = 1 + Σν). The TeX "
   "keeps the printed reading; the current layer has \\oplus.")

add(384, "(4.2.3), end of the display", "no punctuation after Z_ℓ[G_{y'}]", "a full stop", "punctuation", "high",
    "\\mathbb Z_\\ell[G_{y'}]." + NL + "\\tag{4.2.3}", "\\mathbb Z_\\ell[G_{y'}]" + NL + "\\tag{4.2.3}",
    "The TeX adds the full stop.")

add(384, "'Le caractère σ'_{y'} de Sw'_{y'} ...' after (4.2.3)", "a new, indented paragraph",
    "runs on after the display (no blank line)", "other", "high", "\\]" + NL + "Le caractère $\\sigma'_{y'}$",
    "\\]" + NL + NL + "Le caractère $\\sigma'_{y'}$", "Paragraph break; drop it if paragraphing is left to a global pass.")

add(384, "'Le caractère σ'_{y'} de Sw'_{y'} est donné par la formule :'", "a colon after 'formule'",
    "formule (no colon)", "punctuation", "high", "$Sw'_{y'}$ est donné par la formule",
    "$Sw'_{y'}$ est donné par la formule:", "Last line of p. 384.")

add(384, "(4.2.4) (printed on p. 385), first row '1 - ν_{y'}(s) si s ≠ e'",
    "ν (Greek nu); 'si' before the condition; no commas", "1-v_{y'}(s),& s\\ne e,\\\\[0.4em]", "formula", "high",
    "\\sigma'_{y'}(s)=" + NL + "\\begin{cases}" + NL + "1-v_{y'}(s),& s\\ne e,\\\\[0.4em]",
    "\\sigma'_{y'}(s)=" + NL + "\\begin{cases}" + NL + "1-\\nu_{y'}(s)& \\text{si } s\\ne e\\\\[0.4em]",
    "Printed on p. 385; filed under p. 384, where (4.2.4) stands until the folio-385 marker move (no edit of (4.2.4) "
    "touches the move's anchor '\\[' + line break + '\\sigma').")

add(384, "(4.2.4) (printed on p. 385), second row, 'Σ_{s≠e} ν_{y'}(s)'", "ν (Greek nu) after the sum",
    "\\sum_{s\\ne e}v_{y'}(s)", "symbol", "high",
    "\\sum_{s\\ne e}v_{y'}(s)" + NL + "=", "\\sum_{s\\ne e}\\nu_{y'}(s)" + NL + "=",
    "The v of '1 + v_{y'}(D)' is the Latin v of the valuation, as the TeX.")

add(384, "(4.2.4) (printed on p. 385), second row, '1 + v_{y'}(D_{C'/C})'", "D_{C'/C} (C' first; magnified)",
    "\\mathfrak D_{C/C'}", "formula", "high",
    "1+v_{y'}(\\mathfrak D_{C/C'}", "1+v_{y'}(\\mathfrak D_{C'/C}",
    "Diplomatic layer only: the current layer already reads C'/C here. The print has C/C' in (4.2.6) (misprint "
    "item under p. 385).")

add(384, "(4.2.4) (printed on p. 385), end of the second row 'si s = e'",
    "'si' before s = e; no comma and no punctuation at the end of the display",
    "),& s=e,", "missing", "high",
    "),& s=e," + NL + "\\end{cases}", ")& \\text{si } s=e" + NL + "\\end{cases}",
    "Also removes the two commas the TeX adds.")

# ---------------------------------------------------------------- p. 385
add(385, "top of the page (folio-385 marker)",
    "p. 385 begins with the display (4.2.4) 'σ'_{y'}(s) = { 1 - ν_{y'}(s) si s ≠ e ...'; p. 384 ends 'Le caractère "
    "σ'_{y'} de Sw'_{y'} est donné par la formule :'",
    "(4.2.4) ends page_384.tex; page_385.tex begins with 'où $\\mathfrak D_{C/C'}$'", "marker", "high",
    note="Page 385 really begins at the '\\[' that opens (4.2.4) (diplomatic s5.tex line 13072, current 13068 in the live files of 16:17). "
         "Exact fix (bash): python -I move_marker.py 5 385 $'\\\\[\\n\\\\sigma' --before. Do not use the bare anchor "
         "'\\[': the last '\\[' before the marker is the one inside '\\\\[0.4em]' of (4.2.4) and the marker would "
         "land inside the cases environment (checked). Simulated in memory on both layers: the marker then stands on "
         "its own line between '... donné par la formule' and '\\['. Text not moved; the (4.2.4) edits are filed "
         "under p. 384.")

add(385, "'où D_{C'/C} est la différente du revêtement C'/C'", "D_{C'/C} (C' first)", "$\\mathfrak D_{C/C'}$",
    "formula", "high", "où $\\mathfrak D_{C/C'}$ est", "où $\\mathfrak D_{C'/C}$ est",
    "Diplomatic layer only: the current layer already reads C'/C.")

mp(385, "'l'idéal d'augmentation de Z_ℓ [G] ,'", "Z_ℓ [G] (magnified: G without index)",
   "\\mathbb Z_\\ell[G_{y'}] (silently corrected)", "high", "\\mathbb Z_\\ell[G_{y'}]",
   "u_{G_{y'}} is the character of the augmentation ideal of Z_ℓ[G_{y'}]. Restores the printed reading in the "
   "diplomatic layer only.",
   old="\\mathbb Z_\\ell[G_{y'}]$, est aussi", new="\\mathbb Z_\\ell[G]$, est aussi")

add(385, "'d'un Q_ℓ[G_{y'}]-module,- la représentation d'Artin'", "a dash right after the comma",
    "-module, la (no dash)", "punctuation", "high", "\\mathbb Q_\\ell[G_{y'}]$-module, ",
    "\\mathbb Q_\\ell[G_{y'}]$-module,- ",
    "A short typed dash; written as the typescript's hyphen (no en dash).")

add(385, "'la représentation d'Artin de G_{y'}'", "'la représentation d'Artin' and 'de' (next line) underlined",
    "no underline", "underline", "high", "la représentation d'Artin de $G_{y'}$",
    "\\emph{la représentation d'Artin de} $G_{y'}$", "")

mp(385, "'qui sera désigné part Art_{y'}'", "part", "part (as printed)", "high", "par",
   "The TeX keeps the printed reading; the current layer keeps 'part' too.")

add(385, "'On a donc :' after '... qui sera désigné part Art_{y'} .'", "'On a donc :' stands flush left on the "
    "next line (not indented)", "a blank line before 'On a donc' (new paragraph)", "other", "low",
    "$Art_{y'}$." + NL + NL, "$Art_{y'}$." + NL,
    "As 'Soit' on p. 383: the print does not indent it. Drop it if paragraphing is left to a global pass.")

add(385, "'On a donc :'", "a colon", "On a donc (no colon)", "punctuation", "high",
    "On a donc" + NL + "\\[" + NL + "a_{y'}(s)=", "On a donc:" + NL + "\\[" + NL + "a_{y'}(s)=", "")

add(385, "(4.2.6), first row '- ν_{y'}(s) si s ≠ e'", "ν (Greek nu); 'si'; no commas",
    "-v_{y'}(s),& s\\ne e,\\\\[0.4em]", "formula", "high",
    "\\begin{cases}" + NL + "-v_{y'}(s),& s\\ne e,\\\\[0.4em]",
    "\\begin{cases}" + NL + "-\\nu_{y'}(s)& \\text{si } s\\ne e\\\\[0.4em]",
    "v for ν, 'si' missing, two commas added.")

add(385, "(4.2.6), second row, 'Σ_{s≠e} ν_{y'}(s)'", "ν (Greek nu) after the sum", "\\sum_{s\\ne e}v_{y'}(s)",
    "symbol", "high", "\\sum_{s\\ne e}v_{y'}(s)=v_{y'}(", "\\sum_{s\\ne e}\\nu_{y'}(s)=v_{y'}(",
    "The v of 'v_{y'}(D_{C/C'})' is the Latin v, as the TeX.")

mp(385, "(4.2.6), second row, 'v_{y'}(D_{C/C'})'", "D_{C/C'} (here C first; (4.2.4) and the text print C'/C)",
   "\\mathfrak D_{C/C'} (as printed)", "high", "\\mathfrak D_{C'/C}",
   "The different of C'/C, as in (4.2.4). The TeX keeps the printed reading; the current layer has C'/C.")

add(385, "(4.2.6), end of the second row 'si s = e .'", "'si' before s = e; no comma; the full stop is printed",
    "),& s=e.", "missing", "high",
    "),& s=e." + NL + "\\end{cases}" + NL + "\\tag{4.2.6}", ")& \\text{si } s=e." + NL + "\\end{cases}" + NL + "\\tag{4.2.6}",
    "Also removes the comma the TeX adds.")

add(385, "'Les caractères des représentations précédentes ...' after (4.2.8)", "a new, indented paragraph",
    "runs on after the display (no blank line)", "other", "high", "\\]" + NL + "Les caractères",
    "\\]" + NL + NL + "Les caractères", "Paragraph break; drop it if paragraphing is left to a global pass.")

mp(385, "'Les caractères ... sont notés σ_{y'} , σ'_y , a_y .'", "σ_{y'} (the first, with a typed prime)",
   "$\\sigma_{y'}$ (as printed)", "medium", "$\\sigma_y$",
   "The characters of Sw_y, Sw'_y, Art_y are σ_y, σ'_y, a_y (the current layer has these). The second is printed "
   "σ'_y followed by a faint tick that may be a lightly struck prime, so the TeX's $\\sigma'_{y'}$ is left as it is.")

add(385, "same line, the third character 'a_y'", "a_y (no prime)", "$a_{y'}$", "formula", "high", "$a_{y'}$.",
    "$a_y$.", "Diplomatic layer only: the current layer already reads $a_y$.")

add(385, "numbered paragraph '4.3.' (printed at the top of p. 386)", "4.3. (with a full stop)",
    "\\subsubsection*{4.3}", "punctuation", "high", "\\subsubsection*{4.3}", "\\subsubsection*{4.3.}",
    "Printed on p. 386; filed under p. 385, where the line stands until the folio-386 marker move (the edit keeps "
    "the move's anchor '\\subsubsection*{4.3', so either order works). Already applied in both live "
    "layers (16:17: '\\subsubsection*{4.3.}' under the folio-386 marker).")

add(385, "end of the page (folio-386 marker)",
    "p. 385 ends with 'σ_{y'} , σ'_y , a_y .' and blank space; p. 386 begins '4.3. Notons que les modules ainsi "
    "obtenus ...'",
    "'\\subsubsection*{4.3}' is the last line of page_385.tex; the folio-386 marker follows it, before 'Notons'",
    "marker", "high",
    note="Page 386 really begins at '\\subsubsection*{4.3}' (diplomatic s5.tex line 13116, current 13112 before the move). Exact "
         "fix: python -I move_marker.py 5 386 '\\subsubsection*{4.3' --before (simulated in memory on both layers: "
         "the marker then stands on its own line after the blank line that ends p. 385, directly before "
         "'\\subsubsection*{4.3}'). Already done in both live layers (s5.tex as modified 12 Nov 16:17: the marker "
         "stands directly before '\\subsubsection*{4.3.}', diplomatic line 13115, current 13111); the command then "
         "prints 'anchor not found' and changes nothing. Text not moved.")


# ---------------------------------------------------------------- checks
def page_span(text, folio):
    marks = [(m.start(), int(m.group(2))) for m in
             re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", text)]
    for i, (pos, f) in enumerate(marks):
        if f == folio:
            end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
            return text[pos:end]
    return ""


cur = CUR.read_text(encoding="utf-8")
ok = True
spans = {}
for d in F:
    if d["fix"] is None:
        continue
    p = d["page"]
    t = (BATCH / f"page_{p}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = t.count(old)
    k = t.find(old)
    spans.setdefault(p, []).append((k, k + len(old), old[:40]))
    c = page_span(cur, p).count(old)
    live = DIP.read_text(encoding="utf-8").count(old)
    flag = "" if n == 1 else "   <-- NOT UNIQUE/ABSENT"
    if n != 1:
        ok = False
    print(f"p{p} n={n} cur={c} live_dipl_file={live} {d['kind']:<18} {old[:50]!r}{flag}")
for p, s in spans.items():
    s.sort()
    for a, b in zip(s, s[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP on page", p, a, b)
print("all olds unique and non-overlapping:", ok)
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT)
