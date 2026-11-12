"""Build findings_041_045.json and check that every fix's old occurs exactly once in its page file.
usage: python -I build_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b041_045"
OUT = RUN / "findings_041_045.json"
N = "\n"


def fx(old, new):
    return {"old": old, "new": new}


F = []


def add(page, where, scan, tex, kind, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 41
add(41, "top of the page: \"X' au lieu de Y, on aurait alors obtenu un isomorphisme canonique\"",
    "p. 41 begins with \"X' au lieu de Y , on aurait alors obtenu\"; p. 40 ends with 'en passant par'.",
    "page_041.tex begins with 'lieu de $Y$'; '$X'$ au' ends the last line of page_040.tex.",
    "marker", "high", None,
    "Already reported on p. 40 (findings_036_040.json) and applied: in the live s5.tex (both layers, 16:51) the "
    "folio-41 marker stands before '$X'$ au'. Nothing to do; listed only because page_041.tex predates the move.")

add(41, "display (4.5.3) after 'on peut définir (cf. 1.12 b) (ii)) une flèche canonique', right-hand part",
    "'pour F ∈ ob D^b_c(X) .': the word 'pour', no parentheses",
    r"\qquad (F\in\ob\D_c^b(X)).",
    "word", "high", fx(r"\qquad (F\in\ob\D_c^b(X)).", r"\qquad \text{pour } F\in\ob\D_c^b(X)."),
    "The corrected layer has the same display (labelled (4.5.3)^{\\mathrm{bis}} there) with the same parenthesis; "
    "the fix applies to both layers.")

add(41, "label of the same display",
    "(4.5.3), the number of the isomorphism (D_XF)_x̄ ≃ D_x̄ RΓ_x̄(F) of p. 40; no 'bis'",
    r"(4.5.3)\qquad \underline{D}_X(F)_{\ol{x}}\longrightarrow",
    "misprint_in_print", "medium", None,
    "The print numbers the canonical arrow like the isomorphism of p. 40 and cites it as (4.5.3) in Proposition "
    "4.5.4 (p. 42). The diplomatic TeX keeps the printed number here; the corrected layer already writes "
    "(4.5.3)^{\\mathrm{bis}} here and in 4.5.4. Possibly deliberate (the same arrow, now defined without assuming "
    "K_X dualisant). Goes with the p. 42 entry.",
    corrected=r"(4.5.3)^{\mathrm{bis}}\qquad \underline{D}_X(F)_{\ol{x}}\longrightarrow")

# ---------------------------------------------------------------- p. 42
add(42, "Proposition 4.5.4, 'et que la flèche canonique (4.5.3) soit un isomorphisme'",
    "(4.5.3), no 'bis'",
    r"la flèche canonique (4.5.3)$^{\mathrm{bis}}$",
    "misprint_in_print", "high", fx(r"canonique (4.5.3)$^{\mathrm{bis}}$", "canonique (4.5.3)"),
    "The diplomatic TeX gives the label of p. 41 as printed, (4.5.3), but this reference carries the corrected "
    "layer's 'bis'. The fix restores the printed reading (diplomatic layer only); the corrected layer keeps "
    "(4.5.3)^bis, matching its p. 41 label. Goes with the p. 41 entry.",
    corrected=r"canonique (4.5.3)$^{\mathrm{bis}}$")

add(42, "Remarque 4.5.5, after '(avec les notations de 1.12).'",
    "'Son exploitation pour le calcul de R_!f(F) ...' begins a new, indented paragraph",
    "(avec les notations de 1.12). Son exploitation (same paragraph)",
    "other", "high",
    fx("(avec les notations de 1.12). Son exploitation", "(avec les notations de 1.12)." + N + N + "Son exploitation"),
    "")

# ---------------------------------------------------------------- p. 43
add(43, "top of the page: the opening quotation mark of '\"conservative\"'",
    "p. 43 begins with '\"conservative\", i.e. un morphisme'; p. 42 ends with '... des points géométriques de X) est'.",
    "page_042.tex ends with 'est ``'; page_043.tex begins with 'conservative'''.",
    "marker", "high", None,
    "Page 43 really begins at the '``' that ends the last line of page_042.tex ('($i$ parcourant ... de $X$) est ``'). "
    "Exact fix: python -I move_marker.py 5 43 '``' --before (simulated in memory on both layers: the marker then "
    "splits that line after 'est '). Text not moved. The '``' then ends its own line before 'conservative''': that "
    "line end prints a space inside the quotes (as it does now through the marker line); write '``%' to join them.")

add(43, "first line, 'tel que les H^i_x̄(F) ⟶ H^i_x̄(G) soient des isomorphismes', first H",
    "H̲^i_x̄(F): the H underlined",
    r"les $\H_{\ol{x}}^i(F)",
    "underline", "high", fx(r"les $\H_{\ol{x}}^i(F)", r"les $\uH_{\ol{x}}^i(F)"),
    r"\H is the plain upright H of the preamble, \uH the underlined one, as in (4.5.3)'' (p. 41) and Exercice 4.5.6 "
    "(p. 42).")

add(43, "same line, second H: 'H^i_x̄(G)'",
    "H^i_x̄(G) without underline (no trace of a rule; the bar over the x is clear)",
    r"\H_{\ol{x}}^i(G)",
    "misprint_in_print", "medium", None,
    "The same functor as the first H (underlined in (4.5.3)'' and 4.5.6); the typist left the underline out. The TeX "
    "keeps the printed plain H.",
    corrected=r"\uH_{\ol{x}}^i(G)")

add(43, "the isomorphisms of 4.6, third line: '(induction ordinaire (1.12. b) (i)) )'",
    "(induction ordinaire (1.12. b) (i)) ): a full stop after 1.12, and a further ')' that closes '(induction'",
    r"\text{(induction ordinaire (1.12 b) (i))}",
    "punctuation", "high", fx("(1.12 b) (i))}", "(1.12. b) (i)) )}"),
    "The reference stands in its own parentheses, as (4.2.1) and (4.5.1) in the lines above; the TeX drops the outer "
    "closing one. '1.12.' is the typist's form (p. 36 '(1.12. b)', fixed there the same way).")

add(43, "same line, the first factor i'^*",
    "the prime after the first i has two strokes (a typed tick and a thinner, slanted second stroke), unlike the single "
    "tick of i'^* in the line above; it reads i''^*",
    r"&\xrightarrow{\sim}i'^*\underline{D}_{\ol{x}}",
    "misprint_in_print", "low", fx(r"\xrightarrow{\sim}i'^*\underline", r"\xrightarrow{\sim}i''^*\underline"),
    "The pull-back along i' : x̄ → {x}‾ belongs here (line 2 i'^* R^!i'', line 4 i^* = i'^* i''^*); the TeX silently "
    "has the correct i'^*. The thin second stroke may also be a stray mark: hold if read so.",
    corrected=r"\xrightarrow{\sim}i'^*\underline")

add(43, "same line, 'D_x' between i'^* and i''^*",
    "D̲_x: no bar over the subscript x (the underline of D ends at the x; in the next line D̲_x̄ has its own bar above "
    "the x)",
    r"\underline{D}_{\ol{x}}i''^*",
    "misprint_in_print", "medium", fx(r"_{\ol{x}}i''^*", r"_{x}i''^*"),
    "By the induction formula for i'' : {x}‾ → Y, R^!i'' D_Y ≃ D_{{x}‾} i''^*: the duality functor of the closure "
    "{x}‾ of the factorization above, not of x̄ (that one comes in the next line, by (4.3)). The TeX's \\ol{x} is "
    "neither the printed nor the correct reading. Independent of the previous entry (different characters).",
    corrected=r"_{\ol{\{x\}}}i''^*")

add(43, "same calculation, last line: '(par 4.3)), i.e. finalement un'",
    "(par 4.3)), two closing parentheses, one opening",
    r"\text{(par 4.3)), i.e. finalement un}",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading. Nothing is open before '(par'; the other references of the calculation stand "
    "in their own parentheses, and p. 41 has '(par (4.3) et la formule ...)', so the missing sign is probably the '(' "
    "before 4.3.",
    corrected="(par (4.3)), i.e. finalement un")

add(43, "numbered headings of §4 (here 4.6)",
    "'4.6.' with a full stop, run into 'Soient X un préschéma'; also '4.7.' (p. 44) and '4.2.' (p. 36)",
    r"\subsection*{4.6}, \subsection*{4.7}, \subsection*{4.2}: no full stop",
    "punctuation", "medium", None,
    "Convention of the transcription in §4, not reported on the earlier pages: one pass "
    r"'\subsection*{4.x}' -> '\subsection*{4.x.}' over the \subsection*{4.1}-{4.7} of Exposé I (check 4.1, 4.3, 4.5 "
    "on their pages), unless the full stop of a heading number counts as accepted label typesetting (as the '. :' of "
    "the run-in labels).")

# ---------------------------------------------------------------- p. 44
add(44, "top of the page: display (4.6.1)'",
    "p. 44 begins with \"(4.6.1)'  ℝ^!j(F)_x̄ x ℝΓ_x̄ j^*D_X(F) ⟶ A ,\"; p. 43 ends with \"d'où des accouplements "
    "parfaits\".",
    "the (4.6.1)' display ends page_043.tex; page_044.tex begins with (4.6.1)''.",
    "marker", "high", None,
    "Page 44 really begins at the '\\[' that opens (4.6.1)' (the line after 'd'où des accouplements parfaits'). Exact "
    "fix: python -I move_marker.py 5 44 '\\[' --before (simulated in memory on both layers: the marker then stands "
    "between 'd'où des accouplements parfaits' and that '\\['). Text not moved; it agrees with the print.")

add(44, "4.7, after 'de point fermé x.': 'Soit Y un fermé non vide de X, et considérons les immersions canoniques'",
    "the sentence is printed: 'Soit Y un fermé non vide de X , et considérons les immersions canoniques'",
    "page_044.tex: the sentence follows the note '% SGA→SGAA restauré (... FIX #57, 2026-07-03)' on the same line and "
    "is not printed. The live s5.tex (16:51) already has a line break after the note (fix log, from "
    "findings_036_040.json), but with no space before the '%' the output reads 'de point fermé x.Soit Y un fermé' "
    "(checked with pdflatex).",
    "missing", "high", fx("$x$.%", "$x$. %"),
    "Needed in the live file as it stands. Had the line break not been made, '2026-07-03) Soit' -> "
    "'2026-07-03)\\nSoit' would be needed as well. The same defect at the other FIX #57 note, p. 37 ('le morphisme "
    "canonique.% SGA→SGAA ...', then 'Soit $K$ ...' on the next line): output 'canonique.Soit K'; fix 'canonique.%' -> "
    "'canonique. %' (unique in s5.tex). Both layers.")

add(44, "Exemple 4.6.2, 'd = dim(O_{X,x})'",
    "O̲_{X,x}: no bar over the x",
    r"\dim(\cO_{X,\ol{x}})",
    "symbol", "high", fx(r"\cO_{X,\ol{x}}", r"\cO_{X,x}"),
    "The x̄ of the same sentence ('x̄ un point géométrique de X') has its bar.")

add(44, "Exemple 4.6.2, 'pour tout fermé Y contenant x'",
    "'contenant X': a capital X (cap height, as the Y and F of the line)",
    "contenant $x$",
    "misprint_in_print", "high", fx("contenant $x$", "contenant $X$"),
    "Y is a closed subset containing the point x (4.6: 'si Y est l'adhérence de x'); a closed Y containing X is X "
    "itself. The TeX silently corrects; the fix restores the printed reading.",
    corrected="contenant $x$")

add(44, "Exemple 4.6.2, \"avec F' = R Hom(F,(μ_n)_X^{⊗d})\"",
    "Hom underlined (H̲o̲m̲)",
    r"$F'=\R\Hom(F,(\mu_n)_X^{\otimes d})$",
    "underline", "high", fx(r"F'=\R\Hom(F,", r"F'=\R\underline{\Hom}(F,"),
    r"\Hom is the plain operator (\DeclareMathOperator); p. 40 writes the sheaf Hom \R\underline{\Hom}. The Hom of "
    "'D_x = R Hom( ,A)' (this page) and of (4.7.3)-(4.7.6) (p. 45) is plain in the print, as in the TeX.")

add(44, "4.7, '(et par hypothèse D_x = R Hom( ,A)): K_V = j^*K_X, K_U = i^*K_V, K_Y = RΓ_Y(K_X).' and the next "
        "paragraph",
    "the three formulas run on in the line after '):', not displayed; 'Soit G ∈ ob D^b_c(U), et posons' then begins a "
    "new, indented paragraph",
    r"a display \[K_V=j^*K_X, \qquad K_U=i^*K_V, \qquad K_Y=\R\Gamma_Y(K_X).\] followed by 'Soit $G$' in the same "
    "paragraph",
    "other", "high",
    fx("$):" + N + r"\[" + N + "K_V=j^*K_X," + N + r"\qquad K_U=i^*K_V," + N + r"\qquad K_Y=\R\Gamma_Y(K_X)." + N
       + r"\]" + N + "Soit $G",
       r"$): $K_V=j^*K_X$, $K_U=i^*K_V$, $K_Y=\R\Gamma_Y(K_X)$." + N + N + "Soit $G"),
    "Two layout differences in one edit: the formulas inline as printed, and the paragraph break before 'Soit G'.")

# ---------------------------------------------------------------- p. 45
add(45, "end of the page: the displays (4.7.7), (4.7.8) and 'En composant ... (4.7.1)'.'",
    "p. 45 ends with 'Enfin, la suite exacte' and the footnote (*); p. 46 begins with '(4.7.7)  0 ⟶ A_{V,X} ⟶ A_X ⟶ "
    "A_x ⟶ 0'.",
    "page_045.tex goes on to the end of 'En composant (4.7.5), (4.7.6) et (4.7.8), on obtient la flèche annoncée "
    "(4.7.1)'.'",
    "marker", "high", None,
    "Page 46 really begins at the '\\[' that opens (4.7.7) (the line after 'Enfin, la suite exacte'). Already reported "
    "in findings_046_050.json and applied: the live s5.tex (both layers, 16:59) has the folio-46 marker there. Nothing "
    "to do for the marker. The text that moved agrees with the p. 46 scan except the (4.7.8) sign, already fixed from "
    "findings_046_050.json. The footnote of p. 45 still stands under p. 46: see the 'missing' entry.")

add(45, "foot of the page: the footnote of the '(*)' in the second ⊗^L display",
    "(*) (ajouté en 77) Inexact : il est facile, en fait, de prolonger ⊗^L : D^-(A) x D^-(A) ⟶ D^-(A) en ⊗^L : "
    "D^-(A) x D(A) ⟶ D(A) .  (a later addition in another typeface; upright, not underlined; plain L)",
    r"not in page_045.tex; the TeX has it as a paragraph under the folio-46 marker (in page_046.tex as "
    r"'\emph{(*) (ajouté en 77) Inexact: ...}' with bold L; in the live s5.tex, after the p. 46 fixes, as the plain "
    r"paragraph '(*) (ajouté en 77) Inexact: ...' with \mathrm L, between '(4.7.1)'.' and 'Nous allons voir')",
    "missing", "high",
    fx(r"\D(A)\quad(*).",
       r"\D(A)\quad(*)\footnote{(*) (ajouté en 77) Inexact: il est facile, en fait, de prolonger "
       r"$\overset{\mathrm L}{\otimes}:\D^-(A)\times\D^-(A)\to\D^-(A)$ en "
       r"$\overset{\mathrm L}{\otimes}:\D^-(A)\times\D(A)\to\D(A)$.}."),
    "The note's text as it now stands in the live file, moved to its call in the file's form for the (*) notes of the "
    "1977 additions ('(*)\\footnote{(*) (ajouté en 1977) ...}', Exposé I §3); s5.tex has a \\footnote inside \\[...\\] "
    "elsewhere too, and this one compiles (checked). Apply together with the removal of the paragraph from p. 46: in "
    "the live s5.tex old '(*) (ajouté en 77) Inexact: il est facile, en fait, de prolonger "
    "$\\overset{\\mathrm L}{\\otimes}:\\D^-(A)\\times\\D^-(A)\\to\\D^-(A)$ en "
    "$\\overset{\\mathrm L}{\\otimes}:\\D^-(A)\\times\\D(A)\\to\\D(A)$.\\n\\n' (after '(4.7.1)'.\\n\\n'), new '' "
    "(else the note prints twice). As the p. 46 checker proposed.")

add(45, "same sentence, 'A = ℤ/ℓℤ'",
    "ℤ/ ℓ  ℤ: hand-written ℓ with a wide blank before ℤ, no trace of an exponent",
    r"$A=\Z/\ell\Z$",
    "misprint_in_print", "medium", None,
    "ℤ/ℓℤ is a field; 'de dimension cohomologique infinie pour ν ⩾ 2' is said of ℤ/ℓ^νℤ (the blank may have been left "
    "for the exponent). The TeX keeps the printed reading.",
    corrected=r"$A=\Z/\ell^{\nu}\Z$")

add(45, "same sentence, 'pour ν ⩾ 2'",
    "a hand-written ν (v-shape with a hooked right arm), unlike the looped ℓ earlier in the line",
    r"$\ell\geqslant2$",
    "symbol", "high", fx(r"$\ell\geqslant2$", r"$\nu\geqslant2$"),
    "Wrong letter in the TeX, not a misprint of the print; both layers.")

LNOTE = ("The print's L over ⊗ is a plain typed capital L on this page (no underline; the doubly underlined L of p. 37 "
         r"is the functor L i_?); the TeX's \mathbf L is bold. \mathrm{L} as in the preamble's \lten and the p. 37 fix.")
add(45, "(4.7.1)' (a pasted-in line in another typeface)",
    "plain L over ⊗",
    r"\overset{\mathbf L}{\otimes}_A",
    "font", "high",
    fx(r"\overset{\mathbf L}{\otimes}_A\R\Gamma(V,i_!G')[-1]", r"\overset{\mathrm{L}}{\otimes}_A\R\Gamma(V,i_!G')[-1]"),
    LNOTE)
add(45, "first display of the parenthesis, '⊗^L : D^-(A) x D^-(A) ⟶ D^-(A)'",
    "plain L over ⊗ (a blank between its foot and the ⊗)",
    r"\overset{\mathbf L}{\otimes}:\D^-(A)",
    "font", "high", fx(r"\overset{\mathbf L}{\otimes}:\D^-(A)", r"\overset{\mathrm{L}}{\otimes}:\D^-(A)"),
    "As (4.7.1)'.")
add(45, "second display, '⊗^L : D(A) x D^b(A)_torf ⟶ D(A) (*)'",
    "plain L over ⊗ (a blank between its foot and the ⊗)",
    r"\overset{\mathbf L}{\otimes}:\D(A)",
    "font", "high", fx(r"\overset{\mathbf L}{\otimes}:\D(A)", r"\overset{\mathrm{L}}{\otimes}:\D(A)"),
    "As (4.7.1)'.")
add(45, "'assurant que les deux facteurs de ⊗^L figurant dans (4.7.1)''",
    "plain L over ⊗ (its foot touches the ⊗; no underline visible)",
    r"facteurs de $\overset{\mathbf L}{\otimes}$",
    "font", "medium",
    fx(r"facteurs de $\overset{\mathbf L}{\otimes}$", r"facteurs de $\overset{\mathrm{L}}{\otimes}$"),
    "As (4.7.1)'.")
add(45, "(4.7.4)",
    "plain L over ⊗ (a blank between its foot and the ⊗)",
    r"\R i_*G\overset{\mathbf L}{\otimes}\underline{D}_V",
    "font", "high", fx(r"G\overset{\mathbf L}{\otimes}\underline{D}_V", r"G\overset{\mathrm{L}}{\otimes}\underline{D}_V"),
    "As (4.7.1)'.")
add(45, "(4.7.5) (in the typeface of (4.7.1)')",
    "plain L over ⊗",
    r"\overset{\mathbf L}{\otimes}_A",
    "font", "high",
    fx(r"\overset{\mathbf L}{\otimes}_A\R\Gamma(V,i_!G')\longrightarrow",
       r"\overset{\mathrm{L}}{\otimes}_A\R\Gamma(V,i_!G')\longrightarrow"),
    "As (4.7.1)'.")

add(45, "'Notons d'abord que, par la formule de dualité complémentaire (1.12 a) (ii) on a un isomorphisme canonique'",
    "no comma after (ii)",
    "(1.12 a) (ii), on a",
    "punctuation", "high", fx("(1.12 a) (ii), on a", "(1.12 a) (ii) on a"),
    "")

add(45, "same sentence, '(1.12 a) (ii)'",
    "(1.12 a) (ii): the parenthesis opened before 1.12 is not closed",
    "(1.12 a) (ii)",
    "misprint_in_print", "medium", None,
    "As '(cf. 1.12 b) (ii))' on p. 41. The TeX keeps the printed reading. Independent of the comma fix.",
    corrected="(1.12 a) (ii))")

add(45, "(4.7.4), the argument of D_V: 'D_V(R i_*G)'",
    "a plain R (one stem), while the R of R i_*G before ⊗ and those of (4.7.2)-(4.7.3) are double-struck",
    r"\underline{D}_V(\R i_*G)\longrightarrow K_V",
    "misprint_in_print", "high", fx(r"(\R i_*G)\longrightarrow", r"(\mathrm{R} i_*G)\longrightarrow"),
    "Treated as the plain R of pp. 16 and 38 (diplomatic layer only); the TeX silently has the double-struck R. "
    "Does not overlap the L fix of (4.7.4).",
    corrected=r"(\R i_*G)\longrightarrow")

add(45, "'Mais K_V = j^!K_X, et l'on a l'isomorphisme de dualité (SGAA 3.1.10) :'",
    "(SGAA 3.1.10), no exposé number",
    "(SGAA~3.1.10)",
    "misprint_in_print", "medium", None,
    "The same duality is cited '(SGAA~XVIII~3.1.10)' in Exposé I §3 ('Par dualité') and §4.4 ('cas particuliers "
    "triviaux de la dualité', p. 38); the TeX keeps the printed reading. p. 46 has the same '(SGAA~3.1.10)' ('par "
    "dualité'): both or neither.",
    corrected="(SGAA~XVIII~3.1.10)")

# ---------------------------------------------------------------- checks
ok = True
pages = {p: (B / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(41, 46)}
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    t = pages[d["page"]]
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"]:
        ok = False
        print("MARKER IN OLD", i)
    if d["kind"] == "misprint_in_print" and "corrected" not in d:
        ok = False
        print("NO CORRECTED", i)
# misprint fixes must not overlap other fixes on the same page
for p in pages:
    spans = []
    for i, d in enumerate(F):
        if d["page"] == p and d["fix"]:
            k = pages[p].find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), i, d["kind"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, a, b)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(41, 46):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("entries", len(F), "ok" if ok else "PROBLEMS")
