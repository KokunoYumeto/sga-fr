"""Build findings_046_050.json; check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib
import sys
import time
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
RUN = W / "run_5"
OUT = RUN / "findings_046_050.json"
NL = "\n"


def pagefile(n):
    d = "b041_045" if n <= 45 else "b046_050"
    return RUN / d / f"page_{n:03d}.tex"


F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 45: text printed at the top of p. 46 that stands under the folio-45 marker -------------
add(45, "display (4.7.8), printed at the top of p. 46 (it stands under the folio-45 marker)",
    "(4.7.8)  R Hom(A_{V,X} , K_X) -> R Hom(A_x,K_X) ≃ A .  The last sign is a hand-drawn ≃ (tilde over a bar) "
    "without arrowhead; the arrowed sign of the last display of p. 46 (R Hom(A_{V,X}, F'_{U,X})[1] ≃> ...) has one.",
    r"\R\Hom(A_x,K_X)\xrightarrow{\sim}A.", "symbol", "high",
    r"(A_x,K_X)\xrightarrow{\sim}A.", r"(A_x,K_X)\simeq A.",
    "Printed on p. 46, filed under p. 45 because the text stands in page_045.tex until the folio-46 marker is moved "
    "(marker finding of p. 46): apply before moving the marker. The rest of that block ((4.7.7), 'donne un "
    "homomorphisme de degré +1 :', 'En composant (4.7.5), (4.7.6) et (4.7.8), on obtient la flèche annoncée "
    "(4.7.1)' .') agrees with the print of p. 46.")

# ---------------- page 46 ----------------
add(46, "top of the page: display (4.7.7) to '(4.7.1)'.', and the footnote (*) under the marker",
    "p. 46 begins with '(4.7.7)  0 -> A_{V,X} -> A_X -> A_x -> 0', then 'donne un homomorphisme de degré +1 :', "
    "(4.7.8) and 'En composant (4.7.5), (4.7.6) et (4.7.8), on obtient la flèche annoncée (4.7.1)' .'. p. 45 ends "
    "with 'Enfin, la suite exacte' and, at its foot under a short rule, the footnote '(*) (ajouté en 77) Inexact : "
    "...'. p. 46 has no footnote.",
    r"The display (4.7.7) through '(4.7.1)'.' ends page_045.tex; the folio-46 marker follows it, and page_046.tex "
    r"opens with the footnote paragraph '\emph{(*) (ajouté en 77) Inexact: ...}' of p. 45.",
    "marker", "high", None, None,
    r"Page 46 really begins at the '\[' of the display (4.7.7), the line after 'Enfin, la suite exacte' (s5.tex "
    r"line 1287 at 16:52; the marker is at line 1296). Exact fix (bash): python -I move_marker.py 5 46 "
    r"$'\\[\n(4.7.7)' --before (the anchor is '\[', a line break, '(4.7.7)'; '\[' alone would land on the (4.7.8) "
    r"display and '(4.7.7)' alone would split the display; simulated in memory on both layers, identical here: the "
    r"marker lands between 'Enfin, la suite exacte' and '\['). Text not moved. After the move the footnote "
    r"paragraph (line 1297 and the blank line after it) still stands under p. 46, after '(4.7.1)'.': it is the foot "
    r"of p. 45 (its call '(*)' is in the display ending '\D(A)\quad(*).', line 1262). Move it before the marker, "
    r"just after 'Enfin, la suite exacte', or set it as \footnote like the '(ajouté en 1977)' notes (lines 762, 779, "
    r"whose calls stand in running text). The fix of (4.7.8) is filed under p. 45: apply it before moving the marker.")

add(46, r"the footnote (*) of p. 45 at the head of page_046.tex: opening of the \emph",
    "foot of p. 45: '(*) (ajouté en 77) Inexact : il est facile, en fait, de prolonger ...' in the plain upright "
    "type of the 1977 typewriter; nothing in the note is underlined",
    r"\emph{(*) (ajouté en 77) Inexact: il est facile, ... \D(A)$.}", "underline", "high",
    r"\emph{(*) (ajouté en 77)", r"(*) (ajouté en 77)",
    r"\emph is this file's command for the print's underline; the note is not underlined. Apply together with the "
    r"next finding (the closing brace): either alone breaks the LaTeX.")

add(46, r"the footnote (*) of p. 45: closing brace of the \emph",
    "the note ends '... D^-(A) x D(A) -> D(A) .', not underlined",
    r"...\D^-(A)\times\D(A)\to\D(A)$.}", "underline", "high",
    r"\to\D(A)$.}", r"\to\D(A)$.",
    "Apply together with the previous finding.")

add(46, "the footnote (*) of p. 45: the two L over the tensor sign",
    "both L over ⊗ are ordinary upright typed capitals of the note's typewriter, not bold",
    r"$\overset{\mathbf L}{\otimes}:...$ en $\overset{\mathbf L}{\otimes}:...$", "font", "high",
    r"\mathbf L}{\otimes}:\D^-(A)\times\D^-(A)\to\D^-(A)$ en $\overset{\mathbf L}",
    r"\mathrm L}{\otimes}:\D^-(A)\times\D^-(A)\to\D^-(A)$ en $\overset{\mathrm L}",
    r"Independent of the two \emph edits. \mathrm L is the file's form at s5.tex lines 99-303 "
    r"(\overset{\mathrm L}) and in Exposé I pp. 9-11 (\limits^{\mathrm{L}}). The bold form also stands for the print's "
    r"plain typed L on p. 45 ((4.7.1)', (4.7.5)): see the message.")

add(46, "end of the triangle (b), after R Gamma_x(F')",
    "a full stop after the triangle (b), level with its bottom row",
    r"... \R\Gamma_x(F') \arrow[ll] \end{tikzcd} \] with no punctuation", "punctuation", "high",
    r"\end{tikzcd}", r"\end{tikzcd}\quad .",
    "Same form as the logged fixes of punctuation after a diagram.")

add(46, "first display of p. 47 (it stands under the folio-46 marker): its second line",
    "'≃ R Hom(A_V , i_!G')   par dualité (SGAA 3.1.10)': a plain hand-drawn ≃ (tilde over a bar), no arrowhead",
    r"&\xrightarrow{\sim}\R\Hom(A_V,i_!G')", "symbol", "high",
    r"&\xrightarrow{\sim}\R\Hom(A_V,i_!G')", r"&\simeq\R\Hom(A_V,i_!G')",
    "Printed on p. 47, filed under p. 46 because the text stands in page_046.tex until the folio-47 marker is moved: "
    "apply before moving the marker.")

add(46, "first display of p. 47 (under the folio-46 marker): end of its second line",
    "'par dualité (SGAA 3.1.10)' with no punctuation; the next line is 'd'où finalement un isomorphisme canonique'",
    r"\text{par dualité (SGAA~3.1.10)},", "punctuation", "high",
    r"(SGAA~3.1.10)},", r"(SGAA~3.1.10)}",
    "Comma added at the end of the display. Printed on p. 47: apply before moving the folio-47 marker. Independent "
    "of the previous fix.")

# ---------------- page 47 ----------------
add(47, "top of the page: 'Mais on a' and its display",
    "p. 47 begins with 'Mais on a', then the two-line display R Hom(A_{V,X} , F'_{U,X}) = R Hom(j_!A_V , j_!i_!G') / "
    "≃ R Hom(A_V , i_!G') par dualité (SGAA 3.1.10), then 'd'où finalement un isomorphisme canonique'; p. 46 ends "
    "with the display R Hom(A_{V,X} , F'_{U,X})[1] ≃> R Gamma_x(F'_{U,X}) .",
    "'Mais on a' through 'd'où finalement un' end page_046.tex; the folio-47 marker stands between 'un' and "
    "'isomorphisme canonique'.",
    "marker", "high", None, None,
    r"Page 47 really begins at 'Mais on a' (s5.tex line 1323 at 16:52; the marker is at line 1331). Exact fix: "
    r"python -I move_marker.py 5 47 " + '"Mais on a"' + r" --before (simulated in memory on both layers: the marker "
    r"lands between the '\]' of the display above and 'Mais on a'). Text not moved. The two fixes of that display "
    r"(the iso sign, the added comma) are filed under p. 46: apply them before moving the marker.")

add(47, "(4.7.10), left-hand side",
    "R Gamma_V(i_!G') [-1]: Gamma with the subscript V, the parenthesis holding only i_!G'",
    r"(4.7.10)\qquad \R\Gamma(V,i_!G')", "formula", "high",
    r"(4.7.10)\qquad \R\Gamma(V,i_!G')", r"(4.7.10)\qquad \R\Gamma_V(i_!G')",
    "The print's own notation here ((4.7.1)', p. 46 and (**) of 4.7.16 write R Gamma(V,i_!G')); not wrong, since "
    "i_!G' lives on V, so not classed as a misprint.")

add(47, "(4.7.10), the isomorphism sign",
    "[-1] ≃ R Gamma_x(F'_{U,X}) . : a plain hand-drawn ≃ (tilde over a bar), no arrowhead",
    r"[-1]\xrightarrow{\sim}\R\Gamma_x(F'_{U,X}).", "symbol", "high",
    r"[-1]\xrightarrow{\sim}\R\Gamma_x(F'_{U,X}).", r"[-1]\simeq\R\Gamma_x(F'_{U,X}).",
    "Independent of the previous fix.")

add(47, "(4.7.11), end of the display",
    "'... -> A_Y -> 0 .' with a full stop (a round dot without tail; the comma after (4.7.9) on p. 46 has a clear "
    "tail), then 'qui donne naissance ...' in lower case",
    r"A_Y\longrightarrow0,", "misprint_in_print", "medium",
    r"A_Y\longrightarrow0,", r"A_Y\longrightarrow0.",
    "Full stop for a comma (the sentence runs on with 'qui'); the TeX silently corrects it: changed back to the "
    "printed reading.",
    corrected=r"A_Y\longrightarrow0,")

add(47, "'qui donne naissance à un triangle distingué.' before the triangle (a)",
    "a full stop after 'distingué'",
    "qui donne naissance à un triangle distingué (no punctuation)", "punctuation", "high",
    "un triangle distingué", "un triangle distingué.",
    "The parallel sentence before the triangle (b) on p. 46 has none, as the TeX there.")

add(47, "end of the triangle (a), after R Gamma_X(F)",
    "a full stop after the triangle (a), level with its bottom row",
    r"... \R\Gamma_X(F) \arrow[ul] \end{tikzcd} \] with no punctuation", "punctuation", "high",
    r"\end{tikzcd}", r"\end{tikzcd}\quad .",
    "Same form as the logged fixes of punctuation after a diagram.")

add(47, "last paragraph: 'les accouplements (4.7.12), (4.7.13), et (4.7.14)'",
    "(4.7.12), (4.7.13), et (4.7.14): a comma after (4.7.13)",
    "(4.7.12), (4.7.13) et (4.7.14)", "punctuation", "high",
    "(4.7.13) et (4.7.14) sont", "(4.7.13), et (4.7.14) sont",
    "Comma left out.")

# ---------------- page 48 ----------------
add(48, "first word of the page, 'L'accouplement'",
    "L'accouplement, one word",
    "'L'' and 'accouplement' on two lines: the line end prints a space (L' accouplement)", "other", "high",
    "L'" + NL + "accouplement", "L'accouplement",
    "A line break after an elided article, right after the marker; the same break stands elsewhere in the file "
    "(see the message).")

add(48, "'En résumé, nous pouvons énoncer :' after (4.7.15)",
    "a new paragraph (indented) after the display",
    r"runs on from the display (no blank line after \])", "other", "high",
    "\\]" + NL + "En résumé", "\\]" + NL + NL + "En résumé",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

add(48, "Proposition 4.7.16: 'Pour G ∈ ob D_c^b(U), on a un accouplement parfait :'",
    "a new paragraph (indented) after '(d'où des complexes dualisants associés sur V, U, Y).'",
    "run into the preceding sentence", "other", "high",
    "sur $V,U,Y$). Pour", "sur $V,U,Y$)." + NL + NL + "Pour",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

add(48, "Proposition 4.7.16: 'Si G = F|U , où F ∈ ob D_c^b(X), on a un isomorphisme canonique'",
    "a new paragraph (indented) after '(où G' = D_U(G)) .'",
    r"run on after '(où $G'=\underline{D}_U(G)$).'", "other", "high",
    r"(où $G'=\underline{D}_U(G)$). Si", r"(où $G'=\underline{D}_U(G)$)." + NL + NL + "Si",
    "Paragraph break; drop it if paragraphing is left to a global pass.")

add(48, "end of the two triangles of Proposition 4.7.16, after R Gamma_x(F')",
    "a comma after the right-hand triangle, level with its bottom row",
    r"\end{tikzpicture} with no punctuation", "punctuation", "high",
    r"\end{tikzpicture}", r"\end{tikzpicture}\quad ,",
    "The sentence goes on at the top of p. 49 ('compatible avec l'accouplement (*) ...').")

# ---------------- page 49 ----------------
add(49, "Remarque 4.7.17: 'on voit donc que la dualité locale sur X'",
    "'la dualité locale sur X' underlined",
    "que la dualité locale sur $X$ (sous la forme (4.2.2)')", "underline", "high",
    "que la dualité locale sur $X$ (sous", r"que \underline{la dualité locale sur $X$} (sous",
    "Underline left out.")

add(49, "Remarque 4.7.17: 'équivaut à la dualité \"globale\" sur U = X - x,'",
    "'équivaut à la dualité \"globale\" sur U = X - x,' underlined, the rule running under the final comma",
    "équivaut à la dualité ``globale'' sur $U=X-x$,", "underline", "high",
    "équivaut à la dualité ``globale'' sur $U=X-x$,", r"\underline{équivaut à la dualité ``globale'' sur $U=X-x$,}",
    "Underline left out; the comma is kept inside because the rule reaches it.")

# ---------------- page 50 ----------------
add(50, "section heading",
    "'5. Dualité locale sur les courbes.' (underlined, with a full stop)",
    r"\section*{5. Dualité locale sur les courbes}", "punctuation", "high",
    r"\section*{5. Dualité locale sur les courbes}", r"\section*{5. Dualité locale sur les courbes.}",
    "As the logged fix of the heading of section 3 (p. 21).")

add(50, "proof of Théorème 5.1, its label",
    "'Démonstration : Supposons prouvée la pureté.': 'Démonstration' underlined, then ' :', run into the text",
    r"\begin{prooftext}[Démonstration] (prints '\emph{Démonstration.}')", "other", "high",
    r"\begin{prooftext}[Démonstration]" + NL, r"\emph{Démonstration} : ",
    r"Apply together with the removal of the matching '\end{prooftext}' and its line break on p. 52, after '... Nous "
    r"utiliserons le lemme élémentaire suivant.' (s5.tex line 1498 at 16:52), outside this batch: LaTeX fails "
    r"otherwise. Same form as the global '\emph{Preuve} :' and the p. 32 fix.")

add(50, "proof of 5.1, first paragraph: 'que dim.q.inj(A_X) = 2'",
    "dim.q.inj typed upright throughout",
    r"$\dim.q.inj(A_X)=2$ (q.inj in math italic)", "font", "high",
    r"\dim.q.inj(A_X)", r"\dim.\mathrm{q.inj}(A_X)",
    r"The file's form elsewhere: \dim.\mathrm{q.inj} at s5.tex lines 379-428, 971 and in the Appendice.")

add(50, "'Soient x son point fermé, (π = car(k(x)), η son point générique'",
    "( π = car(k(x)), : only two closing parentheses after x (crisp type), so the parenthesis opened before π is "
    "never closed",
    r"$(\pi=\car(k(x)))$", "misprint_in_print", "high",
    r"$(\pi=\car(k(x)))$", r"$(\pi=\car(k(x))$",
    "A closing parenthesis missing in the print; the TeX silently balances it: changed back to the printed reading.",
    corrected=r"$(\pi=\car(k(x)))$")

add(50, "reference before (5.1.1): '[CL Chap. IV § 2 Exer 2]'",
    "[CL  Chap. IV § 2 Exer 2]: no comma after CL, no full stop after Exer",
    r"[CL, Chap.~IV \S~2 Exer.~2]", "punctuation", "high",
    r"[CL, Chap.~IV \S~2 Exer.~2]", r"[CL Chap.~IV \S~2 Exer~2]",
    "Comma and abbreviation point added by the TeX.")

add(50, "after (5.1.1): 'Z_l(1) = lim mu_{l^nu}'",
    "lim with the arrow under it and the index ν written below the arrow",
    r"\Z_\ell(1)=\varprojlim \mu_{\ell^\nu}", "formula", "high",
    r"\varprojlim \mu_{\ell^\nu}", r"\varprojlim_{\nu} \mu_{\ell^\nu}",
    "Index of the limit left out.")

add(50, "end of '(Bien entendu, H est isomorphe, mais non canoniquement, à prod Z_l .).'",
    "prod_{l≠π} Z_l .). : a full stop before and another after the closing parenthesis",
    r"à $\prod_{\ell\ne\pi}\Z_\ell$.)", "misprint_in_print", "medium",
    r"\Z_\ell$.)", r"\Z_\ell$.).",
    "Doubled full stop; the TeX silently drops the second: changed back to the printed reading.",
    corrected=r"\Z_\ell$.)")

# ---------------- checks ----------------
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    p = pagefile(d["page"]).read_text(encoding="utf-8")
    old, new = d["fix"]["old"], d["fix"]["new"]
    c = p.count(old)
    if c != 1 or "%%%%%%%%%%" in old or old == new or "\r" in old:
        bad += 1
        print("BAD", d["page"], repr(old), c)
    for ch in old + new:
        if ord(ch) < 32 and ch != "\n":
            bad += 1
            print("CTRL", d["page"], repr(old), repr(new))
            break
print("findings:", len(F), "bad:", bad)
cnt = Counter((d["page"], "misprint" if d["kind"] == "misprint_in_print" else "normal") for d in F)
for k in sorted(cnt):
    print(k, cnt[k])
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(json.dumps(F, ensure_ascii=False, indent=1) + "\n")
print("written", OUT, time.strftime("%H:%M:%S"))
