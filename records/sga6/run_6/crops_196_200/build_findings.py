"""Write findings_196_200.json and check that every fix 'old' occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b196_200"
OUT = RUN / "findings_196_200.json"


def fx(old, new):
    return {"old": old, "new": new}


F = []

# ---------------------------------------------------------------- page 196
F.append(dict(
    page=196, where="top of the page: end of Lemme 1.1 (ii)",
    scan="The page begins 'tel que H_i(f^{n'},A) ⟶ H_i(f^n,A) soit nul.' on one line ('tel que' and 'soit nul' "
         "underlined); p. 195 ends 'il existe n' ≥ n'.",
    tex=r"page_195.tex ends '... il existe $n'\geq n$ tel que' / '\[' / ' H_i(\mathbf f^{n'},A)\longrightarrow "
        r"H_i(\mathbf f^n,A)' / '\]'; the folio-196 marker follows, so page_196.tex begins 'soit nul.'",
    kind="marker", confidence="high", fix=None,
    note=r"Page 196 really begins at 'tel que'. Exact fix in main.tex: split the line '\item le pro-objet "
         r"$n\mapsto H_i(\mathbf f^n,A)$ est nul, i.e. pour tout $n$, il existe $n'\geq n$ tel que' after "
         r"'$n'\geq n$' and put the folio-196 marker there: '... il existe $n'\geq n$' / marker / 'tel que' / '\[' / "
         r"' H_i(\mathbf f^{n'},A)\longrightarrow H_i(\mathbf f^n,A)' / '\]' / 'soit nul.'. The print sets this "
         r"formula inline ('tel que $H_i(\mathbf f^{n'},A)\longrightarrow H_i(\mathbf f^n,A)$ soit nul.'), the TeX "
         r"as a display."))
F.append(dict(
    page=196, where="1.2, second line: definition of A",
    scan="'M = ∐ B/(f^n) , A la B-algèbre D_B(M)': no 'et' (both scans)",
    tex=r"$M=\coprod_{n>0}B/(\mathbf f^n)$, et $A$ la $B$-algèbre",
    kind="extra", confidence="high", fix=fx(", et $A$ la", ", $A$ la"),
    note="The TeX adds 'et' before 'A la B-algèbre'."))
F.append(dict(
    page=196, where="1.2, second line: M = ∐ B/(f^n)",
    scan="The index under the hand-drawn coproduct reads 'n 0', with a blank where the relation sign belongs (never "
         "drawn in; both scans: crops_196_200/c196_coprod.png, w196_coprod.png).",
    tex=r"\coprod_{n>0}",
    kind="misprint_in_print", confidence="medium", fix=fx(r"\coprod_{n>0}", r"\coprod_{n\ 0}"),
    corrected=r"\coprod_{n>0}",
    note="The TeX silently supplies '>'. Correct reading n>0 (n≥0 gives the same module, since B/(f^0)=0)."))
F.append(dict(
    page=196, where="1.2: 'On a trivialement' and the first display",
    scan="The footnote call (^1) stands at the right end of the display line, after its full stop: "
         "'H_2^A(f^n,A) ≃ H_2^B(f^n,A) . (^1)'; nothing after 'trivialement'.",
    tex=r"On a trivialement\footnote{L'exposant A ou B ...} followed by the display",
    kind="other", confidence="medium",
    fix=fx(r"""trivialement\footnote{L'exposant A ou B indique relativement à quel anneau on calcule le complexe de Koszul.}
\[
 H_2^A(\mathbf f^n,A)\simeq H_2^B(\mathbf f^n,A).
\]""", r"""trivialement
\[
 H_2^A(\mathbf f^n,A)\simeq H_2^B(\mathbf f^n,A).\qquad\text{\footnotemark}
\]
\footnotetext{L'exposant A ou B indique relativement à quel anneau on calcule le complexe de Koszul.}"""),
    note=r"Footnote call moved to the display as the file does elsewhere (\qquad\text{\footnotemark} in a display, "
         r"\footnotetext after it, main.tex Exposé 0); the footnote text is unchanged."))
F.append(dict(
    page=196, where="1.2, display after 'On a d'autre part'",
    scan="'H_2^B(f^n,A) ≃ H_2^B(f^n,B) ⊕ H_2^B(f^n,M)' with no punctuation after it (both scans)",
    tex=r"\oplus H_2^B(\mathbf f^n,M),",
    kind="punctuation", confidence="high",
    fix=fx(r"\oplus H_2^B(\mathbf f^n,M),", r"\oplus H_2^B(\mathbf f^n,M)"),
    note="Comma added at the end of the display."))
F.append(dict(
    page=196, where="1.2, 'mais H_2^B(f^n,B) = 0 puisque f est une suite régulière'",
    scan="The formula stands inline in the running line, with no comma after '= 0' (both scans).",
    tex=r"mais / \[ H_2^B(\mathbf f^n,B)=0, \] / puisque",
    kind="punctuation", confidence="high",
    fix=fx("mais\n\\[\n H_2^B(\\mathbf f^n,B)=0,\n\\]\npuisque", r"mais $H_2^B(\mathbf f^n,B)=0$ puisque"),
    note="The TeX makes the inline formula a display and adds a comma after it."))
F.append(dict(
    page=196, where="1.2, display after 'donc on a'",
    scan="'H_2^B(f^n,A) ≃ H_2^B(f^n,M) ,': a comma, and the next line begins with a capital, 'On a enfin' (both "
         "scans).",
    tex=r"H_2^B(\mathbf f^n,A)\simeq H_2^B(\mathbf f^n,M).",
    kind="misprint_in_print", confidence="medium",
    fix=fx(r"H_2^B(\mathbf f^n,M).", r"H_2^B(\mathbf f^n,M),"),
    corrected=r"H_2^B(\mathbf f^n,M).",
    note="The print ends the display with a comma before the new sentence 'On a enfin'; the TeX silently corrects "
         "it to a full stop."))
F.append(dict(
    page=196, where="1.2, 'On a enfin (EGA II 1.1.3.3)'",
    scan="(EGA II 1.1.3.3) (both scans)",
    tex="(EGA II 1.1.3.3)",
    kind="misprint_in_print", confidence="medium", fix=None, corrected="(EGA III 1.1.3.3)",
    note="The TeX keeps the printed reading. The Koszul isomorphism H_2 ≅ H^0 cited here is in EGA III §1.1 (the "
         "same paragraph cites EGA III 1.1.4 and 1.1.6); EGA II has no Koszul complex."))
F.append(dict(
    page=196, where="1.2, 'au sous-module ... de M annulé par (f^n)'",
    scan="(f^n) set below the line before M, M on the line: the left-subscript notation _{(f^n)}M (both scans; "
         "crops_196_200/c196_subM.png)",
    tex=r"$(\mathbf f^n)^M$",
    kind="formula", confidence="high",
    fix=fx(r"$(\mathbf f^n)^M$", r"${}_{(\mathbf f^n)}M$"),
    note="The TeX writes M as an exponent of (f^n); the print has (f^n) as a left subscript of M."))
F.append(dict(
    page=196, where="display (*)",
    scan="'H_2^A(f^n,A ≃ _{(f^n)}M .': (f^n) below the line before M (both scans; crops_196_200/c196_star.png)",
    tex=r"(\mathbf f^n)^M.",
    kind="formula", confidence="high",
    fix=fx(r"(\mathbf f^n)^M.", r"{}_{(\mathbf f^n)}M."),
    note="As in the line above (the submodule of M annihilated by (f^n))."))
F.append(dict(
    page=196, where="display (*)",
    scan="'H_2^A(f^n,A ≃': the closing parenthesis after A is missing (both scans)",
    tex=r"H_2^A(\mathbf f^n,A\simeq",
    kind="misprint_in_print", confidence="high", fix=None, corrected=r"H_2^A(\mathbf f^n,A)\simeq",
    note="The TeX keeps the printed reading."))
F.append(dict(
    page=196, where="1.2, 'que le pro-objet n ⟼ H_2^A(f^n,A) n'est pas nul'",
    scan="'le pro-objet' and 'n'est pas nul' underlined (running text of the proof, not a statement; both scans)",
    tex=r"que le pro-objet $n\mapsto H_2^A(\mathbf f^n,A)$ n'est pas nul.",
    kind="underline", confidence="high",
    fix=fx(r"que le pro-objet $n\mapsto H_2^A(\mathbf f^n,A)$ n'est pas nul.",
           r"que \emph{le pro-objet} $n\mapsto H_2^A(\mathbf f^n,A)$ \emph{n'est pas nul}."),
    note=r"Exposé II writes the print's underline with \emph."))

# ---------------------------------------------------------------- page 197
F.append(dict(
    page=197, where="display after 'D'autre part, on a, d'après (II 3.4 et 3.5)'",
    scan="R̳Q R̳j_{1*}(Ĩ) ≃ j_{1*}(Ĩ): both derived-functor R double-underlined (both scans; "
         "crops_196_200/c197_RQ.png)",
    tex=r"RQ\,Rj_{1*}(\widetilde I) (plain R)",
    kind="font", confidence="high",
    fix=fx(r"RQ\,Rj_{1*}", r"\mathbb RQ\,\mathbb Rj_{1*}"),
    note=r"Same form as the double-underlined R of pp. 175-182 (\mathbb R there). The R^1, R^2 of the other "
         "displays of the page are plain in the print, as in the TeX."))

# ---------------------------------------------------------------- page 198
F.append(dict(
    page=198, where="top of the page",
    scan="The page begins 'tie de (0.3).', the second half of 'par-tie' divided at the page break (p. 197 ends "
         "'on a prouvé la première par-').",
    tex="page_197.tex ends 'on a prouvé la première partie de (0.3).'; page_198.tex begins 'Enfin, soit ...'",
    kind="marker", confidence="high", fix=None,
    note=r"Page 198 really begins at 'tie de (0.3).'. Exact fix in main.tex: 'Le faisceau $j_{1*}\widetilde I$ "
         r"étant injectif dans $\Qcoh(Z)$, on a prouvé la première par%' / folio-198 marker / 'tie de (0.3).' / "
         "blank line / 'Enfin, soit ...' (the split-word form of marker_split_word.py)."))
F.append(dict(
    page=198, where="first display (isomorphisme de dualité)",
    scan="R̳ Hom_Mod(E,R̳j_{1*}(Ĩ)) ≃ R̳ Hom_Mod(j_1^*E,Ĩ): the three R double-underlined, Hom plain (both scans)",
    tex=r"R\Hom_{\Mod}(E,Rj_{1*}(\widetilde I)) \simeq R\Hom_{\Mod}(j_1^*E,\widetilde I) (plain R)",
    kind="font", confidence="high",
    fix=fx("R\\Hom_{\\Mod}(E,Rj_{1*}(\\widetilde I))\n \\simeq R\\Hom",
           "\\mathbb R\\Hom_{\\Mod}(E,\\mathbb Rj_{1*}(\\widetilde I))\n \\simeq \\mathbb R\\Hom"),
    note="As p. 197."))
F.append(dict(
    page=198, where="second display (after 'mais comme X est affine, on a (II 3.5)')",
    scan="R̳ Hom_Mod(j_1^*E,Ĩ) ≃ R̳ Hom_Qcoh(j_1^*E,I) ≃ Hom(j_1^*E,Ĩ): both R double-underlined (both scans)",
    tex=r"R\Hom_{\Mod}(j_1^*E,\widetilde I) \simeq R\Hom_{\Qcoh}(j_1^*E,I) (plain R)",
    kind="font", confidence="high",
    fix=fx("R\\Hom_{\\Mod}(j_1^*E,\\widetilde I)\n \\simeq R\\Hom_{\\Qcoh}",
           "\\mathbb R\\Hom_{\\Mod}(j_1^*E,\\widetilde I)\n \\simeq \\mathbb R\\Hom_{\\Qcoh}"),
    note="As p. 197."))
F.append(dict(
    page=198, where="third display (after 'On en déduit')",
    scan="R̳ Hom_Mod(E,R̳j_{1*}(Ĩ)) ≃ Hom(j_1^*E,Ĩ): both R double-underlined (both scans)",
    tex=r"R\Hom_{\Mod}(E,Rj_{1*}(\widetilde I)) \simeq \Hom(j_1^*E,\widetilde I) (plain R)",
    kind="font", confidence="high",
    fix=fx("R\\Hom_{\\Mod}(E,Rj_{1*}(\\widetilde I))\n \\simeq \\Hom",
           "\\mathbb R\\Hom_{\\Mod}(E,\\mathbb Rj_{1*}(\\widetilde I))\n \\simeq \\Hom"),
    note="As p. 197."))

# ---------------------------------------------------------------- page 199
F.append(dict(
    page=199, where="title of Appendice II",
    scan="'APPENDICE II' / 'DÉFINITION DE L'INDICE ANALYTIQUE D'UN COMPLEXE ELLIPTIQUE RELATIF': no 'Exposé II'",
    tex=r"\section*{Exposé II, Appendice II. Définition de l'indice analytique d'un complexe elliptique relatif}",
    kind="extra", confidence="medium",
    fix=fx(r"\section*{Exposé II, Appendice II.", r"\section*{Appendice II."),
    note=r"The TeX adds 'Exposé II, ' to the title (the running head 'II Ap. II' is not part of it); Appendice I "
         r"(p. 195) is '\section*{Appendice I. ...}' without it. The capitals of the typed title are typesetting."))

# ---------------------------------------------------------------- page 200
F.append(dict(
    page=200, where="end of the page",
    scan="The page ends 'On a des isomorphismes canoniques'; the display 'P^0_{X/S} ≃ O_X , P^1_{X/S} ≃ O_X ⊕ "
         "Ω^1_{X/S} ,' is printed at the top of p. 201.",
    tex=r"page_200.tex ends with '\[' / '\begin{aligned}' / 'P^0_{X/S}&\simeq\cO_X,\\' / "
        r"'P^1_{X/S}&\simeq\cO_X\oplus\Omega^1_{X/S},'; the folio-201 marker stands inside the aligned "
        r"environment, before '\end{aligned}'.",
    kind="marker", confidence="high", fix=None,
    note=r"Page 201 really begins at this display. Exact fix: move the folio-201 marker up four lines, to stand "
         r"after the line ending 'On a des isomorphismes canoniques' and before '\['."))
F.append(dict(
    page=200, where="definition of the variété mixte",
    scan="'variété mixte' and 'de classe' underlined; the 'C^r' after them not underlined (both scans; "
         "crops_196_200/c200_varmixte.png)",
    tex=r"\emph{variété mixte de classe $C^r$}",
    kind="underline", confidence="high",
    fix=fx(r"\emph{variété mixte de classe $C^r$}", r"\emph{variété mixte de classe} $C^r$"),
    note="The emphasis covers the formula C^r, which the print leaves plain."))
F.append(dict(
    page=200, where="1.2.1, 'des parties principales à l'ordre n sur X'",
    scan="'parties principales à l'ordre' underlined at the end of the line; the 'n' that begins the next line "
         "is not underlined (both scans; crops_196_200/c200_parties.png)",
    tex=r"\emph{parties principales à l'ordre $n$}",
    kind="underline", confidence="high",
    fix=fx(r"\emph{parties principales à l'ordre $n$}", r"\emph{parties principales à l'ordre} $n$"),
    note="The emphasis covers the n, which the print leaves plain."))
F.append(dict(
    page=200, where="'où U' (resp. V') est un ouvert de U'",
    scan="où U' (resp. V')",
    tex="où $U'$ ( / resp. $V'$): a line break after the parenthesis, which prints '( resp.'",
    kind="other", confidence="low",
    fix=fx("où $U'$ (\nresp. $V'$)", "où $U'$ (resp. $V'$)"),
    note="Stray line break inside the parenthesis (also in main.tex); the output has a space the print does not "
         "have."))

ok = True
for f in F:
    if f["fix"] is None:
        continue
    t = (PAGES / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    marker_cross = "%%%%%%%%%%" in f["fix"]["old"]
    if n != 1 or marker_cross:
        ok = False
        print("BAD", f["page"], n, marker_cross, repr(f["fix"]["old"])[:80])
order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = [{k: f[k] for k in order if k in f} for f in F]
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(196, 201):
    print(p, c[(p, False)], "/", c[(p, True)])
print("all olds unique:", ok, "| findings:", len(F))
