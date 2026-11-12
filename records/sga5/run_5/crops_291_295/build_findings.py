"""Build findings_291_295.json (batch 291-295, SGA 5 Exposé VII) and check every fix against its page file."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
N = "\n"
F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


UL = ("Exposé VII: the TeX has no underline markup for statements; \\emph is the file's command here "
      "(as the applied statements of pp. 283-285).")
OP = ("The subscript is a small p: its bowl takes 14-15 of the letter's 20-22 pixel rows and it sits 4-5 px "
      "below the foot of the O, like the p of p^* on the same lines; the capital P of O_P(1) (p. 292) and of "
      "O_P(-1) in (3.6.2) (p. 294) has its bowl in 11-12 of 21 rows and its top at the foot of the O. "
      "O_P(-1) is the twisting sheaf on P (p is the projection).")

# ---------------- p. 290 (text printed on p. 291, standing under the folio-290 marker) ----------------
add(290, "display at the top of p. 291 (end of Définition 3.2), 'Â•(S) = Π_i A^i(S) .'",
    "A with a hat and a raised dot (A•), as A•(S), A•(P) of Corollaire 2.2.6 (p. 289) and A•(S) at the foot of p. 290",
    "\\widehat A^*(S)=\\prod_i A^i(S).", "symbol", "high",
    "\\widehat A^*(S)=\\prod_i", "\\widehat A^{\\bullet}(S)=\\prod_i",
    "Printed on p. 291; filed under p. 290, where the display stands until the marker move of p. 291 (the edit "
    "does not touch the move's anchor). The TeX has a star; written like the file's A^{\\bullet}(X) of p. 282.")
add(290, "numbered paragraph 3.3 (top of p. 291)", "'3.3.' (with a full stop)", "\\subsubsection*{3.3}",
    "punctuation", "high", "\\subsubsection*{3.3}", "\\subsubsection*{3.3.}",
    "Printed on p. 291; filed under p. 290 until the marker move. As '2.1.' (p. 285, batch 281-285).")

# ---------------- p. 291 ----------------
add(291, "top of the page", "p. 291 begins with the display 'Â•(S) = Π_i A^i(S) .' (the end of Définition 3.2), then "
    "'3.3. Il est évident que ...'; p. 290 ends with '... on désigne ainsi l'élément correspondant dans'",
    "page_290.tex ends with the display '\\widehat A^*(S)=\\prod_i A^i(S).', '\\end{statement}', "
    "'\\subsubsection*{3.3}' and 'Il est'; the folio-291 marker stands before 'évident que'",
    "marker", "high", None, None,
    "Page 291 really begins at the '\\[' that opens the display '\\widehat A^*(S)=\\prod_i A^i(S).' (the line after "
    "'... l'élément correspondant dans'). Exact fix: python -I move_marker.py 5 291 '\\[' --before (simulated in "
    "memory on both layers: the marker then stands on its own line between '... correspondant dans' and '\\['). "
    "The anchor is the last '\\[' above the marker, so run the command once only (not again if batch 286-290 "
    "reports the same move). Text not moved; the two fixes of the text that moves to p. 291 are filed under p. 290.")
add(291, "3.3, 'Il est évident que quels que soient S et E'", "no comma after 'que'", "évident que, quels",
    "punctuation", "high", "évident que, quels", "évident que quels", "The TeX adds a comma.")
add(291, "3.3, 'et que si le rang de E est borné par d'", "no comma after 'que'", "et que, si le rang",
    "punctuation", "high", "et que, si le rang", "et que si le rang", "The TeX adds a comma.")
add(291, "Proposition 3.4, first sentence",
    "'Les classes de Chern précédemment définies satisfont aux propriétés / suivantes' underlined, no full stop "
    "after 'suivantes' (then (i))",
    "Les classes de Chern précédemment définies satisfont aux propriétés suivantes.", "punctuation", "high",
    "Les classes de Chern précédemment définies satisfont aux propriétés suivantes.",
    "\\emph{Les classes de Chern précédemment définies satisfont aux propriétés suivantes}",
    "The TeX adds a full stop. One edit: it also gives the underline. " + UL)
add(291, "Proposition 3.4 (i), the item title", "'(i) (Normalisation) Soit': the title in parentheses, not "
    "underlined, no full stop", "\\emph{Normalisation.}", "punctuation", "high",
    "\\emph{Normalisation.}", "(Normalisation)",
    "The TeX drops the parentheses, adds a full stop and sets the title in \\emph (the file's underline), which the "
    "print does not have.")
add(291, "Proposition 3.4 (i)", "underlined: 'Soit' | 'un' | 'Module inversible. Désignant par' | 'l'image' / "
    "'de la classe de' | 'par le morphisme bord' (L, O_S, [L] not); Module with a capital M",
    "Soit $L$ un $\\mathcal O_S$-module inversible. Désignant par ... (no underline markup)", "underline", "high",
    "Soit $L$ un $\\mathcal O_S$-module inversible. Désignant par $[L]$ l'image de la classe de $L$ par le "
    "morphisme bord",
    "\\emph{Soit} $L$ \\emph{un} $\\mathcal O_S$-\\emph{Module inversible. Désignant par} $[L]$ \\emph{l'image de "
    "la classe de} $L$ \\emph{par le morphisme bord}",
    "One edit: it also gives the print's capital M (word).")
add(291, "Proposition 3.4 (i), 'on a' before c(L) = 1 + [L]", "'on a' underlined", "on a", "underline", "high",
    "on a" + N + "\\[" + N + "c(L)", "\\emph{on a}" + N + "\\[" + N + "c(L)")
add(291, "Proposition 3.4 (ii), the item title", "'(ii) (Stabilité par changement de base).': in parentheses, "
    "not underlined, the full stop after the parenthesis", "\\emph{Stabilité par changement de base.}",
    "punctuation", "high", "\\emph{Stabilité par changement de base.}", "(Stabilité par changement de base).",
    "The TeX drops the parentheses and sets the title in \\emph.")
add(291, "Proposition 3.4 (ii)", "underlined: 'Soient' | 'un morphisme de schémas' / 'et' | 'un' | 'Module "
    "localement libre. Pour tout entier' | 'on a' (f : S'→S, E, O_S, i not); Module with a capital M",
    "Soient $f:S'\\to S$ un morphisme de schémas et ... (no underline markup)", "underline", "high",
    "Soient $f:S'\\to S$ un morphisme de schémas et $E$ un $\\mathcal O_S$-module localement libre. Pour tout "
    "entier $i$, on a",
    "\\emph{Soient} $f:S'\\to S$ \\emph{un morphisme de schémas et} $E$ \\emph{un} $\\mathcal O_S$-\\emph{Module "
    "localement libre. Pour tout entier} $i$, \\emph{on a}",
    "One edit: it also gives the capital M (word).")
add(291, "Proposition 3.4 (iii), the item title", "'(iii) (Additivité).': in parentheses, not underlined",
    "\\emph{Additivité.}", "punctuation", "high", "\\emph{Additivité.}", "(Additivité).",
    "The TeX drops the parentheses and sets the title in \\emph.")
add(291, "Proposition 3.4 (iii), 'Soit' before 0 → E' → E → E'' → 0", "'Soit' underlined", "Soit", "underline",
    "high", "Soit" + N + "\\[" + N + "0\\to E'", "\\emph{Soit}" + N + "\\[" + N + "0\\to E'")
add(291, "Proposition 3.4 (iii)", "underlined: 'une suite exacte de' | 'Modules localement' / 'libres. Pour tout "
    "entier' | 'on a la relation' (O_S, n not); Modules with a capital M",
    "une suite exacte de $\\mathcal O_S$-modules ... (no underline markup)", "underline", "high",
    "une suite exacte de $\\mathcal O_S$-modules localement libres. Pour tout entier $n$, on a la relation",
    "\\emph{une suite exacte de} $\\mathcal O_S$-\\emph{Modules localement libres. Pour tout entier} $n$, "
    "\\emph{on a la relation}",
    "One edit: it also gives the capital M (word).")
add(291, "Proposition 3.4 (iii), end of the display c_n(E) = Σ_{i+j=n} c_i(E')c_j(E'')",
    "no full stop: after (E\") only a 3 x 6 px tick at mid-height (a speck), unlike the 8 x 7 px typed full stops "
    "on the baseline of the other displays (crop p291_sumend.png)", "c_i(E')c_j(E'').", "punctuation", "medium",
    "c_i(E')c_j(E'').", "c_i(E')c_j(E'')",
    "The TeX adds a full stop at the end of the display.")
add(291, "Corollaire 3.5", "underlined: 'Pour toute suite exacte' | 'de' | 'Modules localement' / 'libres, on a' "
    "(the sequence and O_S not); Modules with a capital M",
    "Pour toute suite exacte ... (no underline markup)", "underline", "high",
    "Pour toute suite exacte $0\\to E'\\to E\\to E''\\to0$ de $\\mathcal O_S$-modules localement libres, on a",
    "\\emph{Pour toute suite exacte} $0\\to E'\\to E\\to E''\\to0$ \\emph{de} $\\mathcal O_S$-\\emph{Modules "
    "localement libres, on a}",
    "One edit: it also gives the capital M (word).")
add(291, "Corollaire 3.5, display", "'c(E) = c(E').c(E\")': the typewriter's full stop as product dot",
    "c(E)=c(E')c(E'')", "symbol", "high", "c(E)=c(E')c(E'')", "c(E)=c(E')\\cdot c(E'')",
    "The TeX drops the product dot (the typewriter's full stop, written \\cdot by the volume's rule).")
add(291, "Corollaire 3.5, 'dans Â•(S) .'", "'dans' underlined", "dans $\\widehat A^*(S)$.", "underline", "high",
    "dans $\\widehat", "\\emph{dans} $\\widehat")
add(291, "Corollaire 3.5, 'dans Â•(S) .'", "A with a hat and a raised dot (A•)", "\\widehat A^*(S)", "symbol", "high",
    "A^*(S)$.", "A^{\\bullet}(S)$.", "As the display at the top of the page (filed under p. 290).")
add(291, "proof label 'Preuve de 3.4.'", "'Preuve' and 'de' underlined, '3.4.' not",
    "\\emph{Preuve de 3.4.}", "underline", "high", "\\emph{Preuve de 3.4.}", "\\emph{Preuve de} 3.4.",
    "Proof label: the TeX also underlines the number.")
add(291, "reference 'La théorie des classes de Chern.'", "the title is not underlined",
    "\\emph{La théorie des classes de Chern}", "underline", "high",
    "\\emph{La théorie des classes de Chern}", "La théorie des classes de Chern", "The TeX adds emphasis.")
add(291, "reference 'pp. 137-154'", "a hyphen", "137--154", "punctuation", "high", "137--154", "137-154",
    "The TeX writes an en dash.")

# ---------------- p. 292 ----------------
add(292, "proof of 3.4 (i), 'Soit E un O_S-Module localement libre ;'", "Module with a capital M",
    "$\\mathcal O_S$-module", "word", "high",
    "$\\mathcal O_S$-module localement libre;", "$\\mathcal O_S$-Module localement libre;",
    "The typescript's capital M (sheaf of modules), as the applied 'Module' of pp. 282-283.")
add(292, "'En particulier si E est inversible'", "no comma after 'En particulier'", "En particulier, si",
    "punctuation", "high", "En particulier, si", "En particulier si", "The TeX adds a comma.")
add(292, "(iii), 'les Modules considérés'", "Modules with a capital M", "les modules considérés", "word", "high",
    "les modules considérés", "les Modules considérés")
add(292, "Lemme 3.6, first sentence", "underlined: 'Soit' | 'un' | 'Module localement libre muni d'une filtration "
    "finie' (E, O_S not); Module with a capital M", "Soit $E$ un $\\mathcal O_S$-module ... (no underline markup)",
    "underline", "high",
    "Soit $E$ un $\\mathcal O_S$-module localement libre muni d'une filtration finie",
    "\\emph{Soit} $E$ \\emph{un} $\\mathcal O_S$-\\emph{Module localement libre muni d'une filtration finie}",
    "One edit: it also gives the capital M (word).")
add(292, "Lemme 3.6, the filtration", "'0 = E_o ⊂ E_1 ⊂ ... E_i ⊂ ... E_r = E': no inclusion sign after either row "
    "of dots", "E_1\\subset\\cdots\\subset E_i\\subset\\cdots\\subset E_r=E", "extra", "high",
    "\\subset\\cdots\\subset E_i\\subset\\cdots\\subset E_r", "\\subset\\cdots E_i\\subset\\cdots E_r",
    "The TeX adds two \\subset (as the logged p. 246).")
add(292, "Lemme 3.6, second sentence", "underlined: 'dont les quotients consécutifs' | 'sont inversibles. Alors "
    "l'éga-' / 'lité ci-dessous est vérifiée' (the formulas and the colon not)",
    "dont les quotients consécutifs ... (no underline markup)", "underline", "high",
    "dont les quotients consécutifs $L_i=E_i/E_{i-1}$ $(1\\le i\\le r)$ sont inversibles. Alors l'égalité "
    "ci-dessous est vérifiée:",
    "\\emph{dont les quotients consécutifs} $L_i=E_i/E_{i-1}$ $(1\\le i\\le r)$ \\emph{sont inversibles. Alors "
    "l'égalité ci-dessous est vérifiée}:")
add(292, "'Il est clair par définition des schémas de drapeaux que'", "no commas",
    "Il est clair, par définition des schémas de drapeaux, que", "punctuation", "high",
    "Il est clair, par définition des schémas de drapeaux, que",
    "Il est clair par définition des schémas de drapeaux que", "The TeX adds two commas.")
add(292, "end of the display c(h*(E)) = ... = c(h*(E'))c(h*(E''))", "no comma (p. 293 goes on 'soit grâce à (ii)')",
    "=c(h^*(E'))c(h^*(E'')),", "punctuation", "high",
    "=c(h^*(E'))c(h^*(E'')),", "=c(h^*(E'))c(h^*(E''))", "The TeX adds a comma at the end of the display.")

# ---------------- p. 293 ----------------
add(293, "first line, 'soit grâce à (ii)'", "no commas", "soit, grâce à (ii),", "punctuation", "high",
    "soit, grâce à (ii),", "soit grâce à (ii)", "The TeX adds two commas.")
add(293, "number of the display (3.5.1)", "'(3.5.1.)' with a full stop inside the parenthesis", "\\tag{3.5.1}",
    "number", "high", "\\tag{3.5.1}", "\\tag{3.5.1.}", "As printed; the reference 'grâce à (3.5.1)' has no stop.")
add(293, "display (3.5.1)", "'h*(c(E').c(E\"))': the typewriter's full stop as product dot",
    "h^*(c(E')c(E''))", "symbol", "high", "h^*(c(E')c(E''))", "h^*(c(E')\\cdot c(E''))",
    "The TeX drops the product dot.")
add(293, "'(F O_T-Module loc. libre),'", "the abbreviation 'loc.'; Module with a capital M",
    "\\text{-module localement libre}", "word", "high",
    "\\text{-module localement libre}", "\\text{-Module loc. libre}",
    "The TeX writes the abbreviation out and gives a small m.")
add(293, "'donc (2.2.5) l'homomorphisme, image réciproque'", "(2.2.5)", "(2.2.5)", "misprint_in_print", "medium",
    None, None,
    "Wrong reference number: in the print 2.2.5 is the paragraph that introduces the notation A•(X) and the "
    "injectivity of the pull-back is Corollaire 2.2.6 (p. 289; p. 290 cites it as '(2.2.6)'). The TeX keeps the "
    "printed reading; the current layer already reads 'donc, d'après le corollaire (2.2.6),'.",
    corrected="(2.2.6)")
add(293, "'l'homomorphisme, image réciproque h* : A•(S) → A•(Z) est une injection'",
    "a comma after 'l'homomorphisme' (no comma closes the apposition)", "l'homomorphisme image réciproque",
    "misprint_in_print", "medium", "l'homomorphisme image réciproque", "l'homomorphisme, image réciproque",
    "A stray comma of the typist (the phrase is 'L'homomorphisme image réciproque' in Corollaire 2.2.6); the TeX "
    "silently drops it. Drop this item if the comma is taken as intended.",
    corrected="l'homomorphisme image réciproque")
add(293, "'h* : A•(S) → A•(Z)'", "A with a raised dot (A•), twice", "A^*(S)\\to A^*(Z)", "symbol", "high",
    "A^*(S)\\to A^*(Z)", "A^{\\bullet}(S)\\to A^{\\bullet}(Z)", "The TeX has stars (as p. 291).")
add(293, "'Pour tout i ∈ [1,r] le monomorphisme'", "no comma", "Pour tout $i\\in[1,r]$, le", "punctuation", "high",
    "Pour tout $i\\in[1,r]$, le", "Pour tout $i\\in[1,r]$ le", "The TeX adds a comma.")
add(293, "display S ≃ Y_1 ⊂ Y_2 ... Y_i ⊂ ... ⊂ Y_r = P", "no inclusion sign before or after the first row of dots",
    "Y_2\\subset\\cdots\\subset Y_i", "extra", "high", "Y_2\\subset\\cdots\\subset Y_i", "Y_2\\cdots Y_i",
    "The TeX adds two \\subset.")
add(293, "'Notons aussi pour tout couple (i,j) d'entiers avec 1 ≤ i ≤ j ≤ r'", "no commas",
    "Notons aussi, pour tout couple $(i,j)$ d'entiers avec $1\\le i\\le j\\le r$,", "punctuation", "high",
    "Notons aussi, pour tout couple $(i,j)$ d'entiers avec $1\\le i\\le j\\le r$,",
    "Notons aussi pour tout couple $(i,j)$ d'entiers avec $1\\le i\\le j\\le r$",
    "The TeX adds two commas (after 'aussi' and before the display).")
add(293, "display α*_{i+1}(p*(Ľ_{i+1}) ⊗ O_p(-1)).", "O with a small p: 'O_p(-1)'", "\\mathcal O_P(-1)",
    "misprint_in_print", "medium", "\\mathcal O_P(-1)", "\\mathcal O_p(-1)",
    OP + " The TeX silently corrects it. The same O_p(-1) recurs on pp. 294 (three times) and 295.",
    corrected="\\mathcal O_P(-1)")
add(293, "Lemme 3.6.1, first sentences", "underlined: 'Soit' | 'une suite exacte de' | 'Modules localement "
    "libres.' / 'Alors la suite' (the sequence and O_S not); Modules with a capital M",
    "Soit $0\\to L\\to E\\to F\\to0$ une suite exacte ... (no underline markup)", "underline", "high",
    "Soit $0\\to L\\to E\\to F\\to0$ une suite exacte de $\\mathcal O_S$-modules localement libres. Alors la suite",
    "\\emph{Soit} $0\\to L\\to E\\to F\\to0$ \\emph{une suite exacte de} $\\mathcal O_S$-\\emph{Modules localement "
    "libres. Alors la suite}",
    "One edit: it also gives the capital M (word).")
add(293, "Lemme 3.6.1, after the display", "underlined: 'dans laquelle' | 'désigne le morphisme évident et' | 'est le "
    "morphisme de degré un cor-' / 'respondant à l'inclusion de' | 'dans' | 'est une suite exacte de' | 'Modules "
    "gradués' (v, u, L, E, O_S not); Modules with a capital M",
    "dans laquelle $v$ désigne ... (no underline markup)", "underline", "high",
    "dans laquelle $v$ désigne le morphisme évident et $u$ est le morphisme de degré un correspondant à l'inclusion "
    "de $L$ dans $E$, est une suite exacte de $\\mathcal O_S$-modules gradués.",
    "\\emph{dans laquelle} $v$ \\emph{désigne le morphisme évident et} $u$ \\emph{est le morphisme de degré un "
    "correspondant à l'inclusion de} $L$ \\emph{dans} $E$, \\emph{est une suite exacte de} $\\mathcal O_S$-"
    "\\emph{Modules gradués}.",
    "One edit: it also gives the capital M (word).")

# ---------------- p. 294 ----------------
add(294, "number of the display (3.6.2)", "'(3.6.2.)' with a full stop inside the parenthesis", "\\tag{3.6.2}",
    "number", "high", "\\tag{3.6.2}", "\\tag{3.6.2.}", "As printed ((3.6.5) has no stop).")
add(294, "'de S-chémas lisses'", "'S-chémas': no s between the hyphen and 'chémas'", "$S$-schémas",
    "misprint_in_print", "high", "$S$-schémas", "$S$-chémas",
    "Typing error; the TeX silently corrects it.", corrected="$S$-schémas")
add(294, "'définie par un Idéal J de O_X'", "Idéal with a capital I (sheaf of ideals)", "par un idéal $J$", "word",
    "high", "par un idéal $J$", "par un Idéal $J$", "'(3.6.4) Si l'idéal J' has a small i, as the TeX.")
add(294, "'de O_X :' before (3.6.3)", "a colon", "$\\mathcal O_X$.", "punctuation", "high",
    "\\mathcal O_X$.", "\\mathcal O_X$ :", "The TeX has a full stop.")
add(294, "paragraph number (3.6.3)", "'(3.6.3) Il satisfait à la formule de projection': the number opens the "
    "paragraph (new line); the display under it has no number",
    "'Il satisfait ...' runs on after 'de $\\mathcal O_X$.'; \\tag{3.6.3} on the display", "number", "medium",
    " Il satisfait", N + N + "(3.6.3) Il satisfait",
    "Apply together with the next item (removal of \\tag{3.6.3}).")
add(294, "display of (3.6.3)", "no number at the display", "\\tag{3.6.3}", "number", "medium",
    "\\tag{3.6.3}" + N + "\\]", "\\]", "Apply together with the previous item.")
add(294, "display of (3.6.3), u_*(x.u*(y)) = u_*(x).y .",
    "the typewriter's full stop as product dot twice, and a full stop at the end", "u_*(x\\,u^*(y))=u_*(x)y,",
    "symbol", "high", "u_*(x\\,u^*(y))=u_*(x)y,", "u_*(x\\cdot u^*(y))=u_*(x)\\cdot y.",
    "The TeX has a thin space for the first dot, drops the second, and ends with a comma where the print has a "
    "full stop (punctuation).")
add(294, "paragraph number (3.6.4)", "'(3.6.4) Si l'idéal J est inversible, on a la relation': the number opens the "
    "paragraph; the display under it has no number",
    "\\tag{3.6.4} on the display", "number", "medium",
    "Si l'idéal $J$ est inversible", N + "(3.6.4) Si l'idéal $J$ est inversible",
    "Apply together with the next item (removal of \\tag{3.6.4}).")
add(294, "display of (3.6.4)", "no number at the display", "\\tag{3.6.4}", "number", "medium",
    "\\tag{3.6.4}" + N + "\\]", "\\]", "Apply together with the previous item.")
add(294, "'voir à partir de là par récurrence croissante sur l'entier i que l'on a'", "no commas",
    "voir à partir de là, par récurrence croissante sur l'entier $i$, que", "punctuation", "high",
    "voir à partir de là, par récurrence croissante sur l'entier $i$, que",
    "voir à partir de là par récurrence croissante sur l'entier $i$ que", "The TeX adds two commas.")
add(294, "display (3.6.5)", "O with a small p: 'O_p(-1)'", "\\mathcal O_P(-1)]\\Bigr)", "misprint_in_print",
    "medium", "\\mathcal O_P(-1)]\\Bigr)", "\\mathcal O_p(-1)]\\Bigr)",
    OP + " The TeX silently corrects it.", corrected="\\mathcal O_P(-1)]\\Bigr)")
add(294, "display Π_i [p*(Ľ_i) ⊗ O_p(-1)] = 0,", "O with a small p: 'O_p(-1)'", "\\mathcal O_P(-1)]=0,",
    "misprint_in_print", "medium", "\\mathcal O_P(-1)]=0,", "\\mathcal O_p(-1)]=0,",
    OP + " The TeX silently corrects it.", corrected="\\mathcal O_P(-1)]=0,")
add(294, "display Π_i (ξ + c_1(p*(Ľ_i)) = 0,", "three opening and two closing parentheses: '(ξ+ c_1(p*(Ľ_i))'",
    "(\\xi+c_1(p^*(\\check L_i)))=0,", "misprint_in_print", "high",
    "(\\xi+c_1(p^*(\\check L_i)))=0,", "(\\xi+c_1(p^*(\\check L_i))=0,",
    "A closing parenthesis is missing in the print; the TeX silently adds it.",
    corrected="(\\xi+c_1(p^*(\\check L_i)))=0,")
add(294, "'Supposons la vraie pour i'", "'Supposons' ends the line and 'la vraie' begins the next, with no hyphen",
    "Supposons-la", "misprint_in_print", "low", "Supposons-la", "Supposons la",
    "The imperative needs the hyphen; the TeX silently adds it. Low: the place is a line break; drop this item "
    "if line-end hyphens are not checked.", corrected="Supposons-la")
add(294, "'Posons pour simplifier N = Π_{j≤i} [p*(Ľ_j) ⊗ O_p(-1)].'", "O with a small p: 'O_p(-1)'",
    "\\mathcal O_P(-1)].", "misprint_in_print", "medium", "\\mathcal O_P(-1)].", "\\mathcal O_p(-1)].",
    OP + " The TeX silently corrects it.", corrected="\\mathcal O_P(-1)].")

# ---------------- p. 295 ----------------
add(295, "first display, '(α_{i+1})*(N).(α_{i+1})*'", "the typewriter's full stop as product dot",
    "(N)(\\alpha_{i+1})^*", "symbol", "high", "(N)(\\alpha_{i+1})^*", "(N)\\cdot(\\alpha_{i+1})^*",
    "The TeX drops the product dot.")
add(295, "first display, 'O_p(-1)'", "O with a small p: 'O_p(-1)'", "\\mathcal O_P", "misprint_in_print",
    "medium", "L_{i+1})\\otimes\\mathcal O_P", "L_{i+1})\\otimes\\mathcal O_p",
    OP + " The TeX silently corrects it.", corrected="L_{i+1})\\otimes\\mathcal O_P")
add(295, "first display, '(p*(Ľ_{i+1}) ⊗ O_p(-1)] = 0,'",
    "the parenthesis opened after (α_{i+1})* is never closed: '(-1)]'", "(-1))\\bigr]", "misprint_in_print", "high",
    "(-1))\\bigr]", "(-1)\\bigr]",
    "A closing parenthesis is missing in the print; the TeX silently adds it. Independent of the O_p item "
    "(the two olds do not overlap).", corrected="(-1))\\bigr]")
add(295, "Corollaire 3.7 (i)", "underlined: 'Pour tout' | 'Module localement libre' | 'et tout entier' | 'on a' "
    "(O_S, E, i not); Module with a capital M",
    "\\item Pour tout $\\mathcal O_S$-module ... (no underline markup)", "underline", "high",
    "\\item Pour tout $\\mathcal O_S$-module localement libre $E$ et tout entier $i$, on a",
    "\\item \\emph{Pour tout} $\\mathcal O_S$-\\emph{Module localement libre} $E$ \\emph{et tout entier} $i$, "
    "\\emph{on a}",
    "One edit: it also gives the capital M (word).")
add(295, "Corollaire 3.7 (ii)", "underlined: 'Si' | 'est un' | 'Module localement libre de rang' | 'on a' "
    "(E, O_S, r not); Module with a capital M",
    "\\item Si $E$ est un $\\mathcal O_S$-module ... (no underline markup)", "underline", "high",
    "\\item Si $E$ est un $\\mathcal O_S$-module localement libre de rang $r$, on a",
    "\\item \\emph{Si} $E$ \\emph{est un} $\\mathcal O_S$-\\emph{Module localement libre de rang} $r$, \\emph{on a}",
    "One edit: it also gives the capital M (word).")
add(295, "Corollaire 3.7 (iii)", "underlined from 'Plus généralement' to 'dans'; '(SGA 6 V 6.1).' not",
    "\\item Plus généralement, ... (no underline markup)", "underline", "high",
    "\\item Plus généralement, les classes de Chern d'un produit tensoriel ou d'une puissance extérieure "
    "s'expriment au moyen des polynômes universels explicités dans (SGA",
    "\\item \\emph{Plus généralement, les classes de Chern d'un produit tensoriel ou d'une puissance extérieure "
    "s'expriment au moyen des polynômes universels explicités dans} (SGA")
add(295, "display Λ^r(E) ≃ ⊗_i(L_i) .", "(L_i) in parentheses", "\\bigotimes_i L_i.", "formula", "high",
    "\\bigotimes_i L_i.", "\\bigotimes_i (L_i).", "The TeX drops the parentheses.")
add(295, "numbered paragraph 3.8", "'3.8.' (with a full stop)", "\\subsubsection*{3.8}", "punctuation", "high",
    "\\subsubsection*{3.8}", "\\subsubsection*{3.8.}", "As '3.3.' (filed under p. 290) and '2.1.' (p. 285).")
add(295, "3.8, 'sur spec(C)'", "'spec' with a small s", "\\operatorname{Spec}(\\mathbb C)", "word", "high",
    "\\operatorname{Spec}(\\mathbb C)", "\\operatorname{spec}(\\mathbb C)", "As the applied 'spec(C)' of p. 285.")
add(295, "3.8, 'On dispose de ce fait par voie de topologie algébrique d'une théorie'", "no commas",
    "On dispose de ce fait, par voie de topologie algébrique, d'une", "punctuation", "high",
    "On dispose de ce fait, par voie de topologie algébrique, d'une",
    "On dispose de ce fait par voie de topologie algébrique d'une", "The TeX adds two commas.")
add(295, "3.8, 'un O_C-Module localement libre de type fini'", "Module with a capital M (the O is a hand-drawn "
    "script O)", "$\\mathcal O_\\mathbb C$-module", "word", "high",
    "$\\mathcal O_\\mathbb C$-module", "$\\mathcal O_\\mathbb C$-Module")
add(295, "last line, 's'il n'y a pas de confusion possible'", "no comma after 'possible'", "confusion possible,",
    "punctuation", "high", "confusion possible,", "confusion possible", "The TeX adds a comma.")

# ---------------- checks ----------------
pagefile = {p: RUN / ("b286_290" if p == 290 else "b291_295") / ("page_%03d.tex" % p) for p in range(290, 296)}
ok = True
texts = {p: pagefile[p].read_text(encoding="utf-8") for p in pagefile}
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    t = texts[d["page"]]
    c = t.count(fx["old"])
    if c != 1 or "%%%%" in fx["old"] or "%%%%" in fx["new"]:
        ok = False
        print("BAD", d["page"], c, repr(fx["old"][:60]))
# apply all edits page by page in order on copies: every old must still be found once
for p in pagefile:
    t = texts[p]
    for d in F:
        if d["page"] == p and d["fix"]:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("SEQ", p, repr(d["fix"]["old"][:60]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
    (RUN / "crops_291_295" / ("page_%03d_applied_preview.tex" % p)).write_text(t, encoding="utf-8")
cnt = {}
for d in F:
    k = "m" if d["kind"] == "misprint_in_print" else "n"
    cnt.setdefault(d["page"], {"n": 0, "m": 0})[k] += 1
print("ok" if ok else "PROBLEMS", len(F), cnt)
(RUN / "findings_291_295.json").write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
