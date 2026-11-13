"""Build findings_401_405.json and check it: every fix's old occurs exactly once in its page file, no marker line is
touched, misprints carry 'corrected'; all fixes of a page applied in forward and reverse order keep their anchors."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b401_405"
OUT = RUN / "findings_401_405.json"
NL = "\n"


def L(*parts):
    return NL.join(parts)


F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 401
add(401, "display at the top of the page: K˙(G_S^{n,r}) = K˙(S)[c_1,...,c_n]/I_r",
    "G with two underlines (S is its index, to the right), both scans (crops_401_405/c401_G.png; w401_top.png)",
    r"K^{\bullet}(G_S^{n,r}) (plain G)", "font", "high",
    fx(r"K^{\bullet}(G_S^{n,r})=", r"K^{\bullet}(\mathbf G_S^{n,r})="),
    r"The file writes the print's doubly underlined letters as \mathbf in Exposé VI (X=\mathbf P(E); \mathbf D(E_i) of "
    r"Proposition 3.1, findings_386_390; \mathbf R, \mathbf L). The same plain G_S^{n,r}, G_S^{n,\infty} stands in 4.9-4.10 "
    r"(main.tex lines 10033-10049, pp. 399-400), for those batches.")
add(401, "'Il résulte alors de la définition (4.9.1) que K˙(G_S^{n,∞}) est le séparé complété'",
    "G with two underlines, both scans (crops_401_405/c401_G2.png; w401_top.png)",
    r"\(K^{\bullet}(G_S^{n,\infty})\) (plain G)", "font", "high",
    fx(r"(G_S^{n,\infty})\) est le séparé", r"(\mathbf G_S^{n,\infty})\) est le séparé"),
    "As the display above.")
add(401, "display γ_t(F_1-n) = 1 + c_1t + ... + c_nt^n = ∏(1+x_it)",
    "three typed full stops on the baseline between the + signs (both scans; crops_401_405/c401_dots.png)",
    r"\cdots", "symbol", "medium",
    fx(r"+c_1t+\cdots+c_nt^n", r"+c_1t+\ldots+c_nt^n"),
    r"\cdots sets the dots at mid-height; same kind of fix as pp. 387, 389, 390 (findings_386_390).")
add(401, "paragraph number 5.1",
    "'5.1.' with a full stop, then 'Dans ce paragraphe' (both scans)",
    r"\subsection*{5.1}", "punctuation", "high",
    fx(L(r"\subsection*{5.1}", "Dans ce paragraphe"), L(r"\subsection*{5.1.}", "Dans ce paragraphe")),
    r"The printed paragraph number ends with a full stop (as the \subsubsection*{2.3} etc. of findings_001_005); the "
    "run-in heading set as its own paragraph is accepted.")
add(401, "letters of Modules on pp. 401-405",
    "underlined in the print: E three times ('E un O_S-Module', 'associé à E', f^*(E)) and F in the exact sequence "
    "(p. 401); E and F of 'les classes de E, F, O_X(1)', G twice ('Si G est un O_X-Module', R^if_*(G)) (p. 402); "
    "E_1, E_n of 'E_1,...,E_n des O_S-Modules', E_i twice, and E_1, E_n of X = D(E_1)x_S...x_S D(E_n) (p. 404). "
    "Plain in the print: the classes E, F, ξ, x, the E of λ^i(E), c(E-n), Ě, F_j, and the E, F of p. 405 (both scans)",
    "all plain", "underline", "high", None,
    "Convention of the Exposé VI transcription, reported for pp. 366-390 (findings_381_385, findings_386_390): not "
    r"itemized. The underlined O of O_S, O_X written \mathcal O falls under the pending volume decision.")

# ---------------------------------------------------------------- page 402
add(402, "start of page (folio-402 marker)",
    "p. 401 ends with the display '0 → F → f^*(E) → O_X(1) → 0 ,'; p. 402 begins 'f étant le morphisme structural "
    "X → S.' (both scans; crops_401_405/w401_bot.png, w402_top.png)",
    "page_401.tex ends with the line '$f$' after that display, above the folio-402 marker; page_402.tex begins "
    "'étant le morphisme structural'",
    "marker", "high", None,
    "Page 402 really begins at '$f$' (one TeX line). Exact edit in main.tex, both layers (diplomatic lines "
    "10086-10087, current 10092-10093): replace '$f$\\n%%%%%%%%%%  scan idx 415  |  folio 402  %%%%%%%%%%\\n' by "
    "'%%%%%%%%%%  scan idx 415  |  folio 402  %%%%%%%%%%\\n$f$\\n' (simulated: crops_401_405/sim_markers.py).")
add(402, "'Comme ξ-1 et x sont dans Fil^1K˙(X), on a (ξ-1) x ∈ Fil²K˙(X), i.e. ... i.e.. x̄' = -x̄'",
    "the formulas stand inline: the text line after 'on a' begins at the left margin with '(ξ-1) x ∈ Fil²K˙(X), "
    "i.e. x ≡ ξ x = x' mod. Fil²K˙(X) i.e.. x̄' = -x̄' and ends there, with no full stop after -x̄; '5.2.' follows "
    "(both scans; crops_401_405/c402_inline.png, w402_top.png)",
    r"a display \[ ... \quad\text{i.e.}\quad ... \quad\text{i.e..}\quad \bar x'= -\bar x . \] (full stop added)",
    "other", "high",
    fx(L(r"on a", r"\[", r"  (\xi-1)x\in\Fil^2K^{\bullet}(X),",
         r"  \quad\text{i.e.}\quad x\equiv \xi x=x' \ \mathrm{mod.}\ \Fil^2K^{\bullet}(X)",
         r"  \quad\text{i.e..}\quad \bar x'= -\bar x .", r"\]"),
       r"on a $(\xi-1)x\in\Fil^2K^{\bullet}(X)$, i.e. $x\equiv \xi x=x'$ mod. $\Fil^2K^{\bullet}(X)$ i.e.. "
       r"$\bar x'= -\bar x$"),
    "Set inline as printed; the edit also drops the full stop the TeX adds after -x̄. It keeps the printed 'i.e..' "
    r"and '-x̄' (misprints, next two entries). The current layer has '\bar x'= \bar x' there: the same edit in that "
    r"layer keeps '\bar x'= \bar x'.")
add(402, "same line: '... mod. Fil²K˙(X) i.e.. x̄' = -x̄'",
    "'i.e..' with two full stops after the e (both scans; crops_401_405/c402_inline.png)",
    r"\text{i.e..} (printed reading kept)", "misprint_in_print", "high", None,
    "Doubled stop of the typist. The diplomatic layer keeps it (also the inline form of the entry above); the current "
    "layer still has 'i.e..'.",
    corrected="i.e.")
add(402, "same line: 'x ≡ ξ x = x' mod. Fil²K˙(X) i.e.. x̄' = -x̄'",
    "x̄' = -x̄ with a minus sign (both scans; crops_401_405/c402_inline.png)",
    r"\bar x'= -\bar x (printed reading kept)", "misprint_in_print", "high", None,
    "x ≡ ξx = x' mod Fil² gives x̄' = x̄; the sign contradicts the line itself. The current layer already reads "
    r"'\bar x'= \bar x'.",
    corrected=r"\bar x'=\bar x")
add(402, "paragraph number 5.2",
    "'5.2.' with a full stop, then 'Si G est un' (both scans)",
    r"\subsection*{5.2}", "punctuation", "high",
    fx(L(r"\subsection*{5.2}", "Si $G$ est"), L(r"\subsection*{5.2.}", "Si $G$ est")),
    "As 5.1 on p. 401.")
add(402, "(5.2.1) y = a_o + a_1ξ^{-1} + ... + a_rξ^{-r}",
    "three typed full stops on the baseline (both scans; crops_401_405/c402_521.png)",
    r"\cdots", "symbol", "medium",
    fx(r"a_1\xi^{-1}+\cdots+a_r", r"a_1\xi^{-1}+\ldots+a_r"),
    "As the dots of p. 401.")
add(402, "'Il est clair que l'homomorphisme ainsi défini est additif'",
    "'Il est clair que' begins a new, indented paragraph after (5.2.2) (both scans)",
    r"'\end{equation}' followed directly by 'Il est clair' (the paragraph runs on)", "other", "high",
    fx(L(r"  f_*(y)=a_0 .", r"\end{equation}", "Il est clair"), L(r"  f_*(y)=a_0 .", r"\end{equation}", "", "Il est clair")),
    "Missing paragraph break.")
add(402, "'On vérifie les relations suivantes :'",
    "'On vérifie les relations suivantes :' begins a new, indented paragraph after '... i.e. est K˙(S)-linéaire.' "
    "(both scans)",
    "'... -linéaire. On vérifie les relations suivantes :' in one paragraph", "other", "high",
    fx("-linéaire. On vérifie", L("-linéaire.", "", "On vérifie")),
    "Missing paragraph break; independent of the entry above.")
add(402, "'Pour vérifier le dernier groupe de relations'",
    "'Pour vérifier' begins a new, indented paragraph after (5.2.3) (both scans)",
    r"'\end{equation}' followed directly by 'Pour vérifier' (the paragraph runs on)", "other", "high",
    fx(L(r"\end{equation}", "Pour vérifier"), L(r"\end{equation}", "", "Pour vérifier")),
    "Missing paragraph break.")

# ---------------------------------------------------------------- page 403
add(403, "start of page (folio-403 marker)",
    "p. 402 ends 'On peut lui appliquer f_* :'; p. 403 begins with the display 'Σ_{i=0}^{r+1} (-1)^i λ^i(E) "
    "f_*(ξ^{n-i}) = 0 .', then 'Le résultat en découle aussitôt' (both scans; crops_401_405/w403_top.png)",
    "page_402.tex ends with that display and the word 'Le', above the folio-403 marker; page_403.tex begins "
    "'résultat en découle'",
    "marker", "high", None,
    "Page 403 really begins at the display's '\\[' (diplomatic line 10118, current 10124). Exact edit in main.tex, both "
    "layers: replace 'On peut lui appliquer $f_*$ :\\n\\[\\n  \\sum_{i=0}^{r+1}(-1)^i\\lambda^i(E)f_*(\\xi^{\\,n-i})=0 "
    ".\\n\\]\\nLe\\n%%%%%%%%%%  scan idx 416  |  folio 403  %%%%%%%%%%\\n' by 'On peut lui appliquer $f_*$ :\\n"
    "%%%%%%%%%%  scan idx 416  |  folio 403  %%%%%%%%%%\\n\\[\\n  \\sum_{i=0}^{r+1}(-1)^i\\lambda^i(E)f_*(\\xi^{\\,n-i})"
    "=0 .\\n\\]\\nLe\\n' (simulated: crops_401_405/sim_markers.py). The display and 'Le' match the print of p. 403.")
add(403, "display after 'une décomposition en somme directe de K˙(S)-modules :'",
    "no equation number: the display 'Fil^kK˙(X) = ... + Fil^{k-r}K˙(S).x^r ,' stands alone on its line and the "
    "left margin is empty (both scans; crops_401_405/c403_531b.png, w403_top.png), whereas (5.2.1)-(5.2.3) on p. 402 "
    "carry their numbers at the margin",
    r"\begin{equation}\tag{5.3.1}", "extra", "high",
    fx(L("-modules :", r"\begin{equation}\tag{5.3.1}"), L("-modules :", r"\begin{equation}\notag")),
    r"The number is the TeX's addition; Exposé VI never cites (5.3.1). amsmath's \notag suppresses the number inside "
    r"equation (tested with pdflatex). Independent of the K' and \cdots entries of the same display.")
add(403, "same display, its first two K",
    "Fil^kK˙(X) = Fil^kK˙(S): K with the raised dot, like the other K˙ of the display (both scans; "
    "crops_401_405/c403_531b.png)",
    r"\Fil^kK'(X)=\Fil^kK'(S)", "symbol", "high",
    fx(r"\Fil^kK'(X)=\Fil^kK'(S)", r"\Fil^kK^{\bullet}(X)=\Fil^kK^{\bullet}(S)"),
    r"Left by the 10 Nov K' -> K^{\bullet} pass of Exposé VI, which missed a K' after a superscript letter "
    r"(\Fil^kK', \Gr^kK', \Gr^iK'): seven places on pp. 403-405 (this and four more entries) and main.tex line 10436 "
    r"(diplomatic; current 10442), Problème 6.10 on p. 415, '\Fil^kK'(X)\subset', for its batch.")
add(403, "same display, '+ ... +'",
    "three typed full stops on the baseline (both scans; crops_401_405/c403_531b.png)",
    r"\cdots", "symbol", "medium",
    fx(r"(S).x+\cdots+\Fil^{k-r}", r"(S).x+\ldots+\Fil^{k-r}"),
    "As the dots of p. 401.")
add(403, "display x^n ∈ Fil^nK˙(S) + Fil^{n-1}K˙(S).x + ... + Fil^{n-r}K˙(S).x^r",
    "Fil^nK˙(S): K with the raised dot (both scans; crops_401_405/c403_xn.png)",
    r"\Fil^nK'(S)", "symbol", "high",
    fx(r"\Fil^nK'(S)", r"\Fil^nK^{\bullet}(S)"),
    "As the K' of (5.3.1).")
add(403, "same display, '+ ... +'",
    "three typed full stops on the baseline (both scans; crops_401_405/c403_xn.png)",
    r"\cdots", "symbol", "medium",
    fx(r"(S).x+\cdots+\Fil^{n-r}", r"(S).x+\ldots+\Fil^{n-r}"),
    "As the dots of p. 401.")
add(403, "'C'est évident pour n ≤ r ; on poursuit par récurrence.'",
    "'C'est évident' begins a new, indented paragraph after the display (both scans)",
    r"'\]' followed directly by 'C'est évident' (the paragraph runs on)", "other", "high",
    fx(L(r"\]", "C'est évident"), L(r"\]", "", "C'est évident")),
    "Missing paragraph break.")
add(403, "Proposition 5.3: 'Avec les notations et les hypothèses de 4.1'",
    "'de 4.1,' (both scans; crops_401_405/w403_top.png)",
    "hypothèses de 4.1 (printed reading kept)", "misprint_in_print", "high", None,
    "The statement uses x, r and Ě of 5.1 (4.1 sets up the flag bundles of a Module of rank n); Corollaires 5.6, 5.8 "
    "and Proposition 5.9 cite 5.1. The current layer already reads 5.1.",
    corrected="5.1")
add(403, "statements of pp. 403-405: Proposition 5.3, Corollaires 5.4-5.8, Proposition 5.9",
    "the print underlines the statements word group by word group, e.g. Proposition 5.3: 'Avec les notations et les "
    "hypothèses de', 'on a pour', 'tout', 'une décomposition en somme directe de', 'modules', 'la filtration "
    "considérée étant la filtration de', 'algèbre augmentée définie', 'en', 'et'; Corollaire 5.5: 'Soient', 'un "
    "schéma quasi', 'compact', 'des', 'Modules', 'localement libres de type fini', 'le schéma de drapeaux de', 'Alors "
    "l'homomorphisme canonique', 'est injectif'; Proposition 5.9: 'Avec les notations et les hypothèses de', 'on a "
    "pour', 'tout', 'En particulier', 'si on pose', 'on obtient'; formulas, numbers and punctuation plain; the labels "
    "underline only the word (both scans)",
    r"the statements in roman (no \underline, no \emph)", "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision): not itemized.")

# ---------------------------------------------------------------- page 404
add(404, "Corollaire 5.5, 'D(E_i) le schéma de drapeaux de E_i'",
    "D with two underlines (both scans; crops_401_405/c404_DEi.png, w404_DEi.png)",
    r"$D(E_1)$ (plain D)", "font", "high",
    fx(r"fini, $D", r"fini, $\mathbf D"),
    r"The file's form for the doubly underlined D (\mathbf D(E_i) in Proposition 3.1, findings_386_390). Independent "
    "of the index entry below (no common text).")
add(404, "Corollaire 5.5, 'D(E_i) le schéma de drapeaux de E_i,'",
    "index i in both places: a short stem with its dot and foot serif, unlike the tall flagged 1 of 'E_1,...,E_n' and "
    "'X = D(E_1)' (both scans; crops_401_405/c404_DEi.png, c404_Ei.png, c404_DE1.png, w404_DEi.png, w404_Ei.png, "
    "w404_DE1.png)",
    r"$D(E_1)$ le schéma de drapeaux de $E_1$", "formula", "high",
    fx(r"(E_1)$ le schéma de drapeaux de $E_1$", r"(E_i)$ le schéma de drapeaux de $E_i$"),
    "As 'D(E_i) le schéma des drapeaux de E_i' of Proposition 3.1.")
add(404, "Corollaire 5.5, 'X = D(E_1)x_S...x_S D(E_n)', first factor",
    "D with two underlines (both scans; crops_401_405/c404_DE1.png, w404_DE1.png)",
    r"\(X=D(E_1)\) ... (plain D)", "font", "high",
    fx(r"$X=D(E_1)", r"$X=\mathbf D(E_1)"),
    "Independent of the entries before and after (no common text).")
add(404, "same formula, last factor D(E_n)",
    "D with two underlines (both scans; crops_401_405/c404_DE1.png)",
    r"\times_S D(E_n) (plain D)", "font", "high",
    fx(r"\times_S D(E_n)", r"\times_S \mathbf D(E_n)"),
    "")
add(404, "same formula, 'x_S...x_S'",
    "three typed full stops on the baseline (both scans; crops_401_405/c404_DE1.png)",
    r"\cdots", "symbol", "medium",
    fx(r"\times_S\cdots", r"\times_S\ldots"),
    "As p. 390 (findings_386_390). The typed letter x for the product sign is handled globally; this edit and the "
    r"D(E_n) edit touch different \times_S.")
add(404, "Corollaire 5.6, display Gr^kK˙(X) = Gr^kK˙(S) ⊕ ..., its first two K",
    "K with the raised dot (both scans; crops_401_405/c404_gr.png, w404_top.png)",
    r"\Gr^kK'(X)=\Gr^kK'(S)", "symbol", "high",
    fx(r"\Gr^kK'(X)=\Gr^kK'(S)", r"\Gr^kK^{\bullet}(X)=\Gr^kK^{\bullet}(S)"),
    "As the K' of (5.3.1) on p. 403.")
add(404, "same display, '⊕ ... ⊕'",
    "three typed full stops on the baseline (both scans; crops_401_405/c404_gr.png)",
    r"\cdots", "symbol", "medium",
    fx(r".\bar x\oplus\cdots\oplus", r".\bar x\oplus\ldots\oplus"),
    "As the dots of p. 401.")
add(404, "Corollaire 5.7: 'la classe dans Gr^iK˙(X) de γ^i(F_j-p_j)'",
    "K with the raised dot (both scans; crops_401_405/c404_gri.png)",
    r"\Gr^iK'(X)", "symbol", "high",
    fx(r"\Gr^iK'(X)", r"\Gr^iK^{\bullet}(X)"),
    "As the K' of (5.3.1) on p. 403.")

# ---------------------------------------------------------------- page 405
add(405, "'(comparer [2], Exp 4).'",
    "'Exp 4' without a full stop after Exp (both scans; crops_401_405/c405_exp.png, w405_top.png)",
    "Exp. 4 (silently corrected)", "misprint_in_print", "high",
    fx("Exp. 4", "Exp 4"),
    "The abbreviation's stop is missing in the print; the diplomatic layer should drop it, the corrected edition "
    "keeps 'Exp. 4'.",
    corrected="Exp. 4")
add(405, "Corollaire 5.8, display f_*(Fil^kK˙(X)) ⊂ Fil^{k-r}K˙(S)",
    "Fil^kK˙(X): K with the raised dot (both scans; crops_401_405/w405_top.png)",
    r"\Fil^kK'(X)", "symbol", "high",
    fx(r"f_*(\Fil^kK'(X))", r"f_*(\Fil^kK^{\bullet}(X))"),
    "As the K' of (5.3.1) on p. 403.")
add(405, "'Conséquence immédiate de 5.3 et de la formule de projection.'",
    "begins a new, indented paragraph after the display of Corollaire 5.8 (both scans)",
    r"'\]' followed directly by 'Conséquence immédiate' (the paragraph runs on)", "other", "high",
    fx(L(r"\]", "Conséquence immédiate"), L(r"\]", "", "Conséquence immédiate")),
    "Missing paragraph break.")
add(405, "'On définit une application'",
    "begins a new, indented paragraph after the display f_*(λ_{-1}(F)) = 1 (both scans)",
    r"'\]' followed directly by 'On définit une application' (the paragraph runs on)", "other", "high",
    fx(L(r"\]", "On définit une application"), L(r"\]", "", "On définit une application")),
    "Missing paragraph break.")
add(405, "end of page (folio-406 marker)",
    "p. 405 ends 'De la relation E = F + ξ, on déduit donc :'; p. 406 begins with the display 'f̄ (λ_t(F)) = "
    "f̄_*(λ_t(E)λ_t(-ξ)) = λ_t(E)f̄_*(λ_t(-ξ)) ;', then 'Or f̄(λ_t(-ξ)) = ... = σ_{-t}(E) d'après (4.2.3). Utilisant "
    "la relation (1.12.1)' (both scans; crops_401_405/m406_top.png, w406_top.png)",
    "page_405.tex ends with that display and the line 'Or ... d'après (4.2.3).', above the folio-406 marker",
    "marker", "high", None,
    "Page 406 really begins at the display's '\\[' after 'on déduit donc :' (diplomatic line 10209, current 10215). "
    "Exact edit, both layers: move the marker line '%%%%%%%%%%  scan idx 419  |  folio 406  %%%%%%%%%%' (diplomatic "
    "line 10215, current 10221) up to stand directly after the line 'De la relation $E=F+\\xi$, on déduit donc :' "
    "(diplomatic 10208, current 10214); simulated: crops_401_405/sim_markers.py. The five TeX lines that change page "
    "match the print of p. 406 except the three misprints of the next entries, which the diplomatic layer keeps.")
add(405, "printed on p. 406 (above the folio-406 marker): first display, 'f̄ (λ_t(F)) = f̄_*(λ_t(E)λ_t(-ξ)) = ...'",
    "the first f̄ has no lower star, a blank where it would stand; the other members and 'f̄_*(λ_t(F)) = 1' below "
    "have it (both scans; crops_401_405/m406_top.png, w406_disp.png)",
    r"\bar f(\lambda_t(F))= (printed reading kept)", "misprint_in_print", "high", None,
    r"The map is f̄_*; the current layer already reads \bar f_*.",
    corrected=r"\bar f_*(\lambda_t(F))")
add(405, "printed on p. 406 (above the folio-406 marker): 'Or f̄(λ_t(-ξ)) = Σ (-1)^i f_*(ξ^i)t^i'",
    "f̄ without the lower star (both scans; crops_401_405/m406_top.png, w406_disp.png)",
    r"Or $\bar f(\lambda_t(-\xi))= (printed reading kept)", "misprint_in_print", "high", None,
    r"As the entry above; the current layer already reads \bar f_*.",
    corrected=r"\bar f_*(\lambda_t(-\xi))")
add(405, "printed on p. 406 (above the folio-406 marker): '= σ_{-t}(E) d'après (4.2.3).'",
    "'(4.2.3)' (both scans; crops_401_405/m406_top.png, w406_disp.png)",
    "d'après (4.2.3) (printed reading kept)", "misprint_in_print", "high", None,
    "f_*(ξ^i) = σ_i is (5.2.3); Exposé VI has no (4.2.3) (Lemme 4.2 has no numbered formula). The current layer "
    "already reads (5.2.3).",
    corrected="(5.2.3)")

# ---------------------------------------------------------------- checks
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
ok = True
pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(401, 406)}
counts = {}
for n, x in enumerate(F):
    if keys - set(x):
        print(n, "missing keys", keys - set(x)); ok = False
    if x["kind"] not in kinds or x["confidence"] not in ("high", "medium", "low"):
        print(n, "bad kind/confidence"); ok = False
    if (x["kind"] == "misprint_in_print") != ("corrected" in x):
        print(n, "corrected/misprint mismatch"); ok = False
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
    f = x["fix"]
    if f is not None:
        k = pages[x["page"]].count(f["old"])
        if k != 1:
            print(n, "page", x["page"], "old occurs", k, "times:", repr(f["old"])); ok = False
        if "%%%%%%%%%%" in f["old"] or "%%%%%%%%%%" in f["new"]:
            print(n, "touches a marker line"); ok = False
for order in ("forward", "reverse"):
    texts = dict(pages)
    for x in (F if order == "forward" else list(reversed(F))):
        f = x["fix"]
        if f is None:
            continue
        t = texts[x["page"]]
        if t.count(f["old"]) != 1:
            print(order, "page", x["page"], "anchor lost or doubled:", repr(f["old"])); ok = False
            continue
        texts[x["page"]] = t.replace(f["old"], f["new"])
    if order == "forward":
        final = texts
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
print("entries", len(F), "counts (normal/misprint):", {p: tuple(v) for p, v in sorted(counts.items())})
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    for n, x in enumerate(F):
        f = x["fix"]
        if f is not None and t.count(f["old"]) != 1:
            print("main.tex", layer, "entry", n, "page", x["page"], "old occurs", t.count(f["old"]), "times:",
                  repr(f["old"][:70]))
print("ALL OK" if ok else "PROBLEMS")
if "--show" in sys.argv:
    for p in sorted(final):
        print("=" * 30, p)
        print(final[p])
