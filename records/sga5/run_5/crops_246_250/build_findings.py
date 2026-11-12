"""Build findings_246_250.json; '¶' in old/new stands for a line break. Checks every old against its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b246_250"
OUT = RUN / "findings_246_250.json"


def F(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if old is None else dict(old=old.replace("¶", "\n"), new=new.replace("¶", "\n")))
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace("¶", "\n") if corrected is not None else None
    d["note"] = note
    return d


M248 = (r"Page 248 begins with a typed repeat of the end of p. 247: the display E_r^{(n)}(X) = (E_r^{p,q}(X))_{p+q=n} "
        r"and 'est canoniquement muni d'une structure de (gr•(S),D)-module gradué. Il en est de même par passage à la "
        r"limite pour :' (the TeX gives them once, on p. 247; the misprint record filed under p. 247 inserts the repeat "
        r"in the diplomatic layer only). Then follow the display ℰ_r^{(n)}(X) = ... and 'L'anneau S, ... Par suite le "
        r"gradué strict grs (X) est', which the TeX has under the folio-247 marker. Exact fix, after this batch has "
        r"been processed (Git Bash quoting): (1) python -I move_marker.py 5 248 $'\\[\nE^{(n)}_r(X)' --before: the "
        r"anchor exists only in the inserted repeat (its display is written E^{(n)}_r for this purpose), so this puts "
        r"the diplomatic marker on its own line just before the repeat and finds nothing in the corrected layer (nor "
        r"anywhere before the batch is processed); (2) python -I move_marker.py 5 248 $'\\[\n\\mathcal E_r^{(n)}(X)' "
        r"--before: puts the corrected layer's marker just before the ℰ display and finds nothing before the moved "
        r"diplomatic marker. Both orders of (1) and (2) give the same result (simulated in memory on both layers of "
        r"the live s5.tex). Text not moved.")

M249 = (r"Page 249 really begins at the display '\[' / '\bigl[\mathcal B_r^{(n)}(X)\bigr]_{r\in\mathbb N} et ...' "
        r"after 'on en déduit que les suites' (end of page_248.tex); 'sont stationnaires.' and the 'Il' just above the "
        r"marker are also printed on p. 249. Exact fix: python -I move_marker.py 5 249 '\[' --before (the last '\[' "
        r"before the marker opens this display; run it once; simulated in memory on both layers of the live s5.tex "
        r"after this batch). Text not moved.")

M251 = (r"Page 250 ends with the display ℰ_∞^{(n)}(X) = grs•T^n(X) . (the rest of the page is blank). In the page "
        r"file '\section*{Exposé VI}' and '\begin{center}' (printed on p. 251) stood under the folio-250 marker; the "
        r"live s5.tex already has the folio-251 marker on its own line before '\section*{EXPOSÉ VI}' (batch 251-255): "
        r"no action. Do not run a '--before' move for this marker now: with the anchor '\section*{Expos' it would go "
        r"back to Exposé III B.")

items = [
    # ---------------- page 246 ----------------
    F(246, "first paragraph, 'les limites des systèmes projectifs essentiellement constants'",
      "projectifs essentiellement constants (underlined)", "projectifs essentiellement constants", "underline", "high",
      r"projectifs essentiellement constants", r"projectifs \emph{essentiellement constants}",
      "Exposé V: the TeX has no underline markup; \\emph as in the logged fixes of pp. 204-205 and 236-240."),
    F(246, "paragraph 'Supposant toujours que X vérifie (ML)'", "new indented paragraph",
      "runs on after the display", "other", "high",
      r"\]¶Supposant toujours", r"\]¶¶Supposant toujours", "Paragraph break of the print."),
    F(246, "'B_r^{pq}(X_α) = B_{r+1}^{pq}(X_α) dès que r > p (cf. b)), on a une suite'",
      "B_r^pq(X_α) = B_r+1^pq(X_α)  dès que  r > p  (cf. b )) , on a une suite de monomorphismes",
      r"display B_r^{pq}(X_\alpha)=B_{r+1}^{pq}(X_\alpha)\qquad(r>p),", "missing", "high",
      r"\[¶B_r^{pq}(X_\alpha)=B_{r+1}^{pq}(X_\alpha)\qquad(r>p),¶\]",
      r"\(B_r^{pq}(X_\alpha)=B_{r+1}^{pq}(X_\alpha)\) dès que \(r>p\) (cf. b)),",
      "The TeX leaves out 'dès que' and '(cf. b))' and writes '(r>p)' instead; the print runs the formula into the "
      "text, as the fix does."),
    F(246, "display (S)", "..⊂ ℰ_r^pq(X) ⊂ .......... ℰ_p+2^pq(X) ⊂ ℰ_p+1^pq(X) .",
      r"\cdots\subset\mathcal E_r^{pq}(X)\subset\cdots\subset\mathcal E_{p+2}^{pq}(X)\subset...", "extra", "high",
      r"\subset\cdots\subset\mathcal E_{p+2}", r"\subset\cdots\mathcal E_{p+2}",
      "The print has no inclusion sign between the row of dots and ℰ_{p+2} (crop p246_S.png)."),
    F(246, "paragraph 'Supposons désormais X strict.'", "new indented paragraph", "runs on after (S)", "other",
      "high", r"\end{equation}¶Supposons désormais", r"\end{equation}¶¶Supposons désormais",
      "Paragraph break of the print."),
    F(246, "'Supposons désormais X strict.'", "strict (underlined)", "strict", "underline", "high",
      r"\(X\) strict.", r"\(X\) \emph{strict}."),
    F(246, "display Z_r^{pq}(X_n) = Im[...]", "no punctuation after ']'", r"\right],", "punctuation", "high",
      r"\right],¶\]¶\[", r"\right]¶\]¶\[", "The TeX adds a comma at the end of the display."),
    F(246, "display B_r^{pq}(X_n) = Im[...]", "no punctuation after ']'", r"\right],", "punctuation", "high",
      r"\right],¶\]¶montrent", r"\right]¶\]¶montrent", "The TeX adds a comma at the end of the display."),
    F(246, "display (d_1), the bracket", "a square bracket [ before the two lines", r"\left\{", "symbol", "high",
      r"\left\{", r"\left[", "As (d_2) on p. 247; the \\right. stays."),
    F(246, "display (d_1), end of the first line 'pour m ≥ n ≥ p'", "no punctuation", "p,", "punctuation", "high",
      r"m\ge n\ge p,\\", r"m\ge n\ge p\\", "The TeX adds a comma."),
    F(246, "display (d_1), end of the second line 'pour m ≥ n ≥ p+r-1'", "no punctuation", "p+r-1,", "punctuation",
      "high", r"p+r-1,¶", r"p+r-1¶", "The TeX adds a comma."),
    F(246, "'est un isomorphisme.' after the display ℰ_r^{pq}(X) -> E_r^{pq}(X_{p+r-1})",
      "isomorphisme (underlined)", "isomorphisme", "underline", "high",
      r"est un isomorphisme", r"est un \emph{isomorphisme}"),
    F(246, "paragraph 'Par ailleurs, il résulte de b) que'", "new indented paragraph",
      "runs on after 'est un isomorphisme.'", "other", "high",
      r". Par ailleurs", r".¶¶Par ailleurs", "Paragraph break of the print."),
    # ---------------- page 247 ----------------
    F(247, "display (d_2), the bracket", "a square bracket [ before the two lines", r"\left\{", "symbol", "high",
      r"\left\{", r"\left[", "As (d_1) on p. 246; the \\right. stays."),
    F(247, "display (d_2), second line", "et   B_∞^pq(X_p+r-1) = B_r^pq(X_p+r-1)   (r > p)",
      r"B_\infty^{pq}(X_{p+r-1})=B_r^{pq}(X_{p+r-1})&(r>p).", "missing", "high",
      r"\\[3pt]¶B_\infty^{pq}", r"\\[3pt]¶\text{et}\quad B_\infty^{pq}",
      "The print has 'et' before the second line of (d_2)."),
    F(247, "display (d_2), end of the first line '(r ≥ 1)'", "no punctuation", "(r\\ge1),", "punctuation", "high",
      r"(r\ge1),", r"(r\ge1)", "The TeX adds a comma."),
    F(247, "display (d_2), end of the second line '(r > p)'", "no punctuation", "(r>p).", "punctuation", "high",
      r"(r>p).¶\end{array}", r"(r>p)¶\end{array}", "The TeX adds a full stop."),
    F(247, "'Ceci permet de définir, pour tout r, un épimorphisme canonique'",
      "tout and épimorphisme underlined", "no underline", "underline", "high",
      r"pour tout \(r\), un épimorphisme canonique", r"pour \emph{tout} \(r\), un \emph{épimorphisme} canonique"),
    F(247, "'qui est un isomorphisme lorsque r > p'", "isomorphisme lorsque (underlined)", "no underline",
      "underline", "high", r"qui est un isomorphisme lorsque", r"qui est un \emph{isomorphisme lorsque}"),
    F(247, "'(par exemple a = p+1 convient) , de sorte que'", "(par exemple a = p+1 convient) ,",
      r"par exemple \(a=p+1\) convient,", "punctuation", "high",
      r"par exemple \(a=p+1\) convient,", r"(par exemple \(a=p+1\) convient),", "The print's parentheses."),
    F(247, "diagram (d_3), upper arrow", "θ_s^pq above the arrow, nothing below it",
      r"\xrightarrow[\epi]{\theta_s^{pq}}", "extra", "high",
      r"\xrightarrow[\epi]{\theta_s^{pq}}", r"\xrightarrow{\theta_s^{pq}}",
      "No 'épi' under the arrows of (d_3) on p. 247 (crop p247_d3a.png); the label belongs to the diagram of p. 249."),
    F(247, "diagram (d_3), lower arrow", "θ_r^pq above the arrow, nothing below it",
      r"\xrightarrow[\epi]{\theta_r^{pq}}", "extra", "high",
      r"\xrightarrow[\epi]{\theta_r^{pq}}", r"\xrightarrow{\theta_r^{pq}}", "As the upper arrow."),
    F(247, "diagram (d_3), left vertical arrow", "hooked (inclusion) arrow pointing down", r"\downarrow", "symbol",
      "high", r"\downarrow&&\downarrow\can", r"\rotatebox[origin=c]{-90}{$\hookrightarrow$}&&\downarrow\can",
      "The left arrow is drawn with a hook at the top (crop p247_d3a.png), the inclusion of (S bis); graphicx is "
      "loaded in s5.tex. The right arrow 'can' is plain, as in the TeX."),
    F(247, "heading A.3", "A.3. Une variante du théorème de Shih. (title underlined)",
      r"\subsubsection*{A.3. Une variante du théorème de Shih}", "punctuation", "high",
      r"théorème de Shih}", r"théorème de Shih.}", "Underlined title: the print's full stop."),
    F(247, "A.3, 'par des idéaux F^i(S) (i ≥ 0) et opérant sur X'", "(i ≥ 0)  et opérant", r"\((i\ge0)\), et",
      "punctuation", "high", r"\((i\ge0)\), et", r"\((i\ge0)\) et", "The TeX adds a comma."),
    F(247, "'Des généralités de A 1 résulte que'", "A 1 (no full stop)", "A.1", "misprint_in_print", "medium",
      r"A.1 résulte", r"A 1 résulte",
      "The typescript has 'A 1' without the full stop (crop p247_A1zoom.png; p. 250 has 'A.2. a)'). The TeX silently "
      "corrects; the edit restores the printed reading (diplomatic layer only).", corrected=r"A.1 résulte"),
    F(247, "'En particulier pour tout entier n :'", "En particulier pour tout entier n :",
      r"En particulier, pour tout entier \(n\):", "punctuation", "high",
      r"En particulier, pour tout entier", r"En particulier pour tout entier", "The TeX adds a comma."),
    F(247, "'est canoniquement muni d'une structure de (gr (S),D)-module gradué' (last lines of the printed page)",
      "(gr (S),𝒟) : a gap after gr, no raised dot", r"\((\gr^\bullet(S),\mathcal D)\)", "misprint_in_print",
      "medium", r"\gr^\bullet(S)", r"\gr(S)",
      "p. 247 prints 'gr (S)' with no raised dot (crop p247_grzoom.png, no trace of one); the repeat of the sentence "
      "typed at the top of p. 248 has gr•(S). Typing omission; the TeX silently corrects. The edit restores the "
      "printed reading (diplomatic layer only); it must be applied before the repeat insertion below, whose new text "
      "also contains \\gr^\\bullet(S) (list order).", corrected=r"\gr^\bullet(S)"),
    F(247, "'Il en est de même par passage à la limite pour :' (end of the printed page)", "pour :", "pour",
      "punctuation", "high", r"limite pour¶", r"limite pour:¶", "The print's colon."),
    F(247, "top of p. 248, printed repeat of the end of p. 247 (text now under the folio-247 marker)",
      "p. 248 opens with E_r^(n)(X) = (E_r^p,q(X))_p+q=n / est canoniquement muni d'une structure de (gr•(S),𝒟) - "
      "module gradué. Il en est de même par passage à la limite pour : / ℰ_r^(n)(X) = ...",
      "the passage once (p. 247), then the ℰ display", "misprint_in_print", "high",
      r"\[¶\mathcal E_r^{(n)}(X)=",
      r"\[¶E^{(n)}_r(X)=\bigl(E_r^{p,q}(X)\bigr)_{p+q=n}¶\]¶est canoniquement muni d'une structure de "
      r"\((\gr^\bullet(S),\mathcal D)\)-module gradué. Il en est de même par passage à la limite pour:¶\[¶"
      r"\mathcal E_r^{(n)}(X)=",
      "The typescript repeats at the top of p. 248 the last display and sentence of p. 247 (this time with gr•(S)); "
      "the TeX gives them once. The edit inserts the printed repeat before the ℰ display (diplomatic layer only; the "
      "corrected layer keeps the passage once). The display is written E^{(n)}_r (same output) so that the folio-248 "
      "marker can be moved before it: see the marker finding of p. 248. Apply in list order, after the 'gr (S)' "
      "misprint fix above.", corrected=r"\[¶\mathcal E_r^{(n)}(X)="),
    F(247, "'Par suite le gradué strict grs (X) est' (printed on p. 248, under the folio-247 marker in the TeX)",
      "Par suite le gradué", "Par suite, le gradué", "punctuation", "high",
      r"Par suite, le gradué", r"Par suite le gradué", "The TeX adds a comma."),
    # ---------------- page 248 ----------------
    F(248, "top of the page", "see note", "see note", "marker", "high", note=M248),
    F(248, "'le gradué strict grs•T^n(X) est canoniquement muni'", "grs•T^n(X) (raised dot)",
      r"\(\grs\,T^n(X)\)", "symbol", "high",
      r"strict \(\grs\,T^n(X)\)", r"strict \(\grs^\bullet T^n(X)\)",
      "The raised dot of the print, as in Théorème A.3 (ii) and on p. 250; \\grs^\\bullet as in the hypothesis of "
      "A.3. In 'grs (X)' two lines above, a faint speck stands where a raised dot would be, too faint to read as one "
      "(crop p248_grszoom.png): the TeX's \\grs(X) is left as it is."),
    F(248, "Théorème A.3, first sentence", "Supposons que pour un entier (underlined)  n  les (underlined)  "
      "(gr•(S),𝒟) - modules gradués (underlined)",
      r"Supposons que, pour un entier \(n\), les ...-modules gradués", "underline", "high",
      r"Supposons que, pour un entier \(n\), les \((\gr^\bullet(S),\mathcal D)\)-modules gradués",
      r"\emph{Supposons que pour un entier} \(n\) \emph{les} \((\gr^\bullet(S),\mathcal D)\)-\emph{modules gradués}",
      "The statement's underline (Exposé V, \\emph); the same edit removes the two commas the TeX adds."),
    F(248, "Théorème A.3, display, first term", "T^n(grs•(X))", r"T^n(\grs^\bullet X)", "formula", "high",
      r"T^n(\grs^\bullet X)", r"T^n(\grs^\bullet(X))", "The print has parentheses around X."),
    F(248, "Théorème A.3, display, second term", "T^n-1(grs•(X))", r"T^{n-1}(\grs^\bullet X)", "formula", "high",
      r"T^{n-1}(\grs^\bullet X)", r"T^{n-1}(\grs^\bullet(X))", "The print has parentheses around X."),
    F(248, "Théorème A.3, 'soient noethériens. Alors :'", "soient noethériens. Alors (underlined) :",
      "no underline", "underline", "high", r"soient noethériens. Alors:", r"\emph{soient noethériens. Alors}:"),
    F(248, "Théorème A.3 (i)", "(i)  T^n(X)  vérifie (MLAR) ,  (vérifie (MLAR) underlined)",
      r"\(T^n(X)\) vérifie (MLAR);", "punctuation", "high",
      r"vérifie (MLAR);", r"\emph{vérifie (MLAR)},",
      "Comma, not semicolon, in the print; the same edit sets the statement's underline."),
    F(248, "Théorème A.3 (ii), 'grs•T^n(X)'", "grs•T^n(X) (raised dot)", r"\(\grs\,T^n(X)\)", "symbol", "high",
      r"\item \(\grs\,T^n(X)\)", r"\item \(\grs^\bullet T^n(X)\)", "As in the paragraph before the theorem."),
    F(248, "Théorème A.3 (ii), 'est un (gr•(S),D)-module noethérien.'",
      "est un (underlined) (gr•(S),𝒟) - module noethérien. (underlined)", "no underline", "underline", "high",
      r"est un \((\gr^\bullet(S),\mathcal D)\)-module noethérien.",
      r"\emph{est un} \((\gr^\bullet(S),\mathcal D)\)-\emph{module noethérien}."),
    F(248, "proof of A.3, after the label", "'Preuve :' on a line of its own, then 'i) Pour tout couple' as an "
      "indented paragraph", "label run into 'i) Pour tout couple'", "other", "medium",
      r"\begin{prooftext}¶i) Pour", r"\begin{prooftext}¶¶i) Pour",
      "Paragraph break of the print after the label (as 'Exemples :' p. 228); the environment prints 'Preuve :'."),
    F(248, "proof of A.3 i), 'de sous-(gr•(S),D- modules gradués'", "sous-(gr•(S),𝒟- modules (no closing "
      "parenthesis)", r"sous-\((\gr^\bullet(S),\mathcal D)\)-modules", "misprint_in_print", "high",
      r"de sous-\((\gr^\bullet(S),\mathcal D)\)-modules", r"de sous-\((\gr^\bullet(S),\mathcal D\)-modules",
      "The typescript drops the parenthesis after D (crop p248_sous.png). The TeX silently corrects; the edit restores "
      "the printed reading (diplomatic layer only).",
      corrected=r"de sous-\((\gr^\bullet(S),\mathcal D)\)-modules"),
    F(248, "proof of A.3 i), 'Utilisant les fait que'", "Utilisant les fait que", "Utilisant le fait que",
      "misprint_in_print", "high", r"Utilisant le fait", r"Utilisant les fait",
      "Typing slip ('les' for 'le'; crop p248_sous.png). The TeX silently corrects; the edit restores the printed "
      "reading (diplomatic layer only).", corrected=r"Utilisant le fait"),
    # ---------------- page 249 ----------------
    F(249, "top of the page", "see note", "see note", "marker", "high", note=M249),
    F(249, "'sont nulles. Autrement dit les monomorphismes'", "Autrement dit les monomorphismes",
      "Autrement dit, les monomorphismes", "punctuation", "high",
      r"Autrement dit, les monomorphismes", r"Autrement dit les monomorphismes", "The TeX adds a comma."),
    F(249, "'sont en fait des isomorphismes.'", "isomorphismes (underlined)", "no underline", "underline", "high",
      r"sont en fait des isomorphismes.", r"sont en fait des \emph{isomorphismes}."),
    F(249, "diagram, upper arrow, label below", "épi", r"\epi (\operatorname{epi}: 'epi')", "accent", "high",
      r"\xrightarrow[\epi]{\theta_s^{pq}}", r"\xrightarrow[\text{épi}]{\theta_s^{pq}}",
      "The print writes 'épi' with the accent (crop p249_diag.png). Once the p. 247 labels are removed, \\epi is used "
      "only on this page, so redefining the macro would do the same."),
    F(249, "diagram, lower arrow, label below", "épi", r"\epi (\operatorname{epi}: 'epi')", "accent", "high",
      r"\xrightarrow[\epi]{\theta_r^{pq}}", r"\xrightarrow[\text{épi}]{\theta_r^{pq}}", "As the upper arrow."),
    F(249, "diagram, left vertical arrow", "≀↓ (vertical tilde beside the arrow)", r"\downarrow\sim", "symbol",
      "medium", r"\downarrow\sim&&\downarrow", r"\wr\downarrow&&\downarrow",
      "The isomorphism mark is a vertical tilde, set to the left of the arrow (crop p249_diag.png); s5.tex writes "
      "this sign \\wr elsewhere (\\uparrow\\wr)."),
    F(249, "display E_∞^{pq}(X_{p+s-1}) -> E_∞^{pq}(X_{p+r-1})", "no punctuation", "comma at the end",
      "punctuation", "high", r"E_\infty^{pq}(X_{p+r-1}),¶\]", r"E_\infty^{pq}(X_{p+r-1})¶\]",
      "The TeX adds a comma at the end of the display."),
    F(249, "'un monomorphisme (cf. a)) est un épimorphisme'", "(cf. a))  est un", "(cf. a)), est un",
      "punctuation", "high", r"(cf. a)),", r"(cf. a))", "The TeX adds a comma."),
    F(249, "display r -> [⊕_p gr^p T^n(X_{p+r})]_{r≥1}", "plain arrow ⟶", r"\longmapsto", "symbol", "high",
      r"r\longmapsto", r"r\longrightarrow", "The print draws a plain arrow."),
    F(249, "'donc T^n(X) vérifie (MLAR) d'après (4.1.3).'", "(MLAR)  d'après", "(MLAR), d'après",
      "punctuation", "high", r"(MLAR), d'après", r"(MLAR) d'après", "The TeX adds a comma."),
    F(249, "ii), 'les \"limites\" des divers systèmes projectifs'", "les\"limites\" (straight double quotes)",
      "les «limites»", "punctuation", "high", r"«limites»", r"``limites''",
      "The print's straight quotes, written ``...'' in Exposé V (as the p. 240 fix); the guillemets are not the "
      "print's."),
    # ---------------- page 250 ----------------
    F(250, "display ℰ_∞^{(n)}(X) = grs• T^n(X) .", "grs• T^n(X) (raised dot)", r"\grs\,T^n(X)", "symbol", "high",
      r"=\grs\,T^n(X).", r"=\grs^\bullet T^n(X).", "The raised dot of the print."),
    F(250, "end of the page / start of Exposé VI", "see note", "see note", "marker", "high", note=M251),
]

# checks: every old once in the original page file, and once again when the page's fixes are applied in list order
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(246, 251)}
work = dict(pages)
ok = True
for x in items:
    fx = x["fix"]
    if not fx:
        continue
    p, old, new = x["page"], fx["old"], fx["new"]
    n0 = pages[p].count(old)
    n1 = work[p].count(old)
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
        print("MARKER TOUCHED", p, repr(old)); ok = False
    if n0 != 1 or n1 != 1:
        print("NOT UNIQUE", p, n0, n1, repr(old)); ok = False
        continue
    work[p] = work[p].replace(old, new, 1)
print("all olds unique:", ok)
OUT.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
for p in range(246, 251):
    (RUN / "crops_246_250" / f"fixed_{p}.tex").write_text(work[p], encoding="utf-8", newline="")
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in items)
for p in range(246, 251):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(items))
