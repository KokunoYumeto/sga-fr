"""Build findings_226_230.json (run once; the checks are in check_findings.py)."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "findings_226_230.json"
F = []


def add(page, where, scan, tex, kind, conf, old, new, note="", corrected=None, fix_null=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix_null else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 226 ----------------
add(226, "after the first display: 'Nous allons voir que pour tout couple (m,n)'",
    "voir que pour tout couple (no comma)", r"voir que, pour tout couple", "punctuation", "high",
    r"voir que, pour", r"voir que pour", "The TeX adds a comma.")
add(226, "'(iii) => (i) : Notant Y le système projectif de (iii)'",
    "(iii) => (i) : Notant (colon, as '(i) => (ii) :' and '(ii) => (i) :' on pp. 227-228)",
    r"$(iii)\Rightarrow(i)$. Notant", "punctuation", "high",
    r"$(iii)\Rightarrow(i)$. Notant", r"$(iii)\Rightarrow(i)$: Notant", "Full stop in the TeX for the print's colon.")
add(226, "'soit r un entier tel que :' before the display Im(Y[s] -> Y) = Im(Y[r] -> Y)",
    "entier tel que : (colon)", "un entier tel que (no colon)", "punctuation", "high",
    "un entier tel que\n", "un entier tel que:\n", "")
add(226, "'... de celle de X_l et par suite, munissant ...'",
    "de celle de X_l et par suite, munissant (no comma before or after 'et')",
    r"de celle de $X_\ell$, et, par suite,", "punctuation", "high",
    r"$X_\ell$, et, par suite", r"$X_\ell$ et par suite", "The TeX adds two commas.")
add(226, "'la condition (iii) s'exprime en disant que dès que l >= n+r'",
    "en disant que dès que (no comma)", "en disant que, dès que", "punctuation", "high",
    "disant que, dès", "disant que dès", "The TeX adds a comma.")
add(226, "heading 4.1.4 (last lines of page_226.tex; printed at the top of p. 227)",
    "'4.1.4.' with a full stop", r"\subsubsection*{4.1.4}", "punctuation", "high",
    r"\subsubsection*{4.1.4}", r"\subsubsection*{4.1.4.}",
    "Printed on p. 227 (see the marker finding there); as \\subsubsection*{3.6.5.} p. 97 and {5.4.} p. 166.")

# ---------------- page 227 ----------------
add(227, "top of the page",
    "p. 227 begins with '4.1.4. Si X est un objet de P vérifiant (ML)'; p. 226 ends with 'd'où (i) .' and blank paper",
    r"'\subsubsection*{4.1.4}' and 'Si $X$ est un' (s5.tex lines 7578-7579, diplomatic) end page_226.tex; "
    "the folio-227 marker (line 7580) stands between 'un' and 'objet'", "marker", "high", None, None,
    "Page 227 really begins at s5.tex line 7578 '\\subsubsection*{4.1.4}'. Exact fix: python -I move_marker.py 5 227 "
    "'\\subsubsection*{4.1.4}' --before (simulated in memory on both layers). Text not moved.", fix_null=True)
add(227, "4.1.4, 'Si X est un objet de P vérifiant (ML)'",
    "P typed plain (typewriter capital, like the text; the C of this page is the hand-drawn letter)",
    r"\(\mathcal P\)", "font", "high",
    r"\(\mathcal P\) vérifiant", r"\(P\) vérifiant",
    "The category P = Hom(N°,C) is typed plain on p. 227 (also Définition 4.2.1 and Lemme 4.2.2); "
    "Exposé V's earlier pages write $P$ (s5.tex line 7511).")
add(227, "4.1.4, 'rappelé en (4.1.1) que pour tout entier p le système projectif :'",
    "que pour tout entier p le système projectif : (no commas; colon before the display)",
    r"que, pour tout entier \(p\), le système projectif (no colon)", "punctuation", "high",
    "(4.1.1) que, pour tout entier \\(p\\), le système projectif\n",
    "(4.1.1) que pour tout entier \\(p\\) le système projectif:\n",
    "The TeX adds two commas and drops the colon.")
add(227, "4.1.4, display gr^p(X) = ...",
    "gr^p(X) = gr^p(X_n)_{n∈N}: no parentheses around gr^p(X_n)",
    r"\gr^p(X)=\bigl(\gr^p(X_n)\bigr)_{n\in\mathbb N}", "formula", "high",
    r"\bigl(\gr^p(X_n)\bigr)_{n\in\mathbb N}", r"\gr^p(X_n)_{n\in\mathbb N}", "The TeX adds the parentheses.")
add(227, "'Sa limite projective (qui existe ... abélienne C ) sera appelée'",
    "the clause in parentheses: '(qui existe sans hypothèse sur la catégorie abélienne C )'",
    r"commas: 'projective, qui existe ... \(\mathcal C\), sera'", "punctuation", "high",
    r"projective, qui existe sans hypothèse sur la catégorie abélienne \(\mathcal C\), sera",
    r"projective (qui existe sans hypothèse sur la catégorie abélienne \(\mathcal C\)) sera", "")
add(227, "'sera appelée p-ème composante'", "p - ème", r"\(p\)-ième", "word", "high",
    r"\(p\)-ième", r"\(p\)-ème", "")
add(227, "'composante du gradué strict de X'",
    "'composante du gradué strict de' underlined (the term being defined); X not",
    "no underline", "underline", "high",
    "composante du gradué strict de", r"\emph{composante du gradué strict de}", "")
add(227, "'de X et notée :' before the display grs^p(X)",
    "X et notée : (no comma; colon)", r"\(X\), et notée (no colon)", "punctuation", "high",
    "\\(X\\), et notée\n", "\\(X\\) et notée:\n", "")
add(227, "heading 4.2", "'4.2. Systèmes projectifs adaptés à J et lemme d'Artin-Rees.' with a full stop (title underlined)",
    r"\subsection*{4.2. ... lemme d'Artin-Rees}", "punctuation", "high",
    "lemme d'Artin-Rees}", "lemme d'Artin-Rees.}", "Underlined title: the print's full stop.")
add(227, "4.2, 'un idéal J de A et une A-catégorie abélienne'",
    "de A et une (no comma)", r"de \(A\), et une", "punctuation", "high",
    r"de \(A\), et une", r"de \(A\) et une", "The TeX adds a comma.")
add(227, "4.2, end of the first sentence",
    "'et une A-catégorie abélienne.': the category is not named", r"abélienne \(\mathcal C\).", "extra", "high",
    r"abélienne \(\mathcal C\).", "abélienne.",
    "The TeX adds C (the abelian category of 4.1, which the definition below uses).")
add(227, "Définition 4.2.1, 'Un objet X de la catégorie'",
    "'Un objet', 'de la catégorie' underlined; X not", "no underline markup", "underline", "high",
    r"Un objet \(X\) de la catégorie", r"\emph{Un objet} \(X\) \emph{de la catégorie}",
    "Exposé V: the print underlines the statements; \\emph as on pp. 204-205.")
add(227, "Définition 4.2.1, 'P = Hom(N°,C)'", "P typed plain", r"\(\mathcal P=", "font", "high",
    r"\(\mathcal P=", r"\(P=", "As the P of 4.1.4.")
add(227, "Définition 4.2.1, 'Hom(N°,C)'", "Hom underlined", r"\Hom(\mathbb N^\circ,\mathcal C)", "underline", "high",
    r"\Hom(\mathbb N^\circ", r"\uHom(\mathbb N^\circ",
    "\\uHom (\\underline{\\Hom}) is defined in the preamble; as Ĉ = Hom(C,Ens)° on p. 205.")
add(227, "Définition 4.2.1, from 'est dit adapté à J' to 'est vérifiée'",
    "underlined: 'est dit / adapté à', 'si sa filtration', 'de système projectif', 'est / compatible avec la filtration', "
    "'adique de', 'i.e. si pour tout couple', 'd'entiers positifs ou nuls l'inclusion ci-dessous est vérifiée'; "
    "not J, (F^pX)_{p∈N}, (4.1.1), J-, X, (p,q), the colon",
    "no underline markup", "underline", "high",
    r"est dit adapté à \(J\) si sa filtration \((F^pX)_{p\in\mathbb N}\) de système projectif (4.1.1) est compatible "
    r"avec la filtration \(J\)-adique de \(X\), i.e. si pour tout couple \((p,q)\) d'entiers positifs ou nuls "
    r"l'inclusion ci-dessous est vérifiée",
    r"\emph{est dit adapté à} \(J\) \emph{si sa filtration} \((F^pX)_{p\in\mathbb N}\) \emph{de système projectif} "
    r"(4.1.1) \emph{est compatible avec la filtration} \(J\)-\emph{adique de} \(X\), \emph{i.e. si pour tout couple} "
    r"\((p,q)\) \emph{d'entiers positifs ou nuls l'inclusion ci-dessous est vérifiée}", "")
add(227, "Lemme 4.2.2, 'Soit X un objet de la catégorie P'",
    "'Soit', 'un objet de la catégorie' underlined; X, P not", "no underline markup", "underline", "high",
    r"Soit \(X\) un objet de la catégorie", r"\emph{Soit} \(X\) \emph{un objet de la catégorie}", "")
add(227, "Lemme 4.2.2, 'de la catégorie P .'", "P typed plain", r"\(\mathcal P\).", "font", "high",
    r"\(\mathcal P\).", r"\(P\).", "As the P of 4.1.4.")
add(227, "Lemme 4.2.2, 'Les assertions suivantes sont équivalentes :'",
    "underlined, not the colon", "no underline markup", "underline", "high",
    "Les assertions suivantes sont équivalentes:", r"\emph{Les assertions suivantes sont équivalentes}:", "")
add(227, "Lemme 4.2.2 (i)", "'est adapté à' underlined; X, J not", "no underline markup", "underline", "high",
    r"\item \(X\) est adapté à \(J\).", r"\item \(X\) \emph{est adapté à} \(J\).", "")
add(227, "Lemme 4.2.2 (ii)", "'Pour tout couple', 'd'entiers avec', 'on a' underlined; (n,p), p <= n+1 not",
    "no underline markup", "underline", "high",
    r"\item Pour tout couple \((n,p)\) d'entiers avec \(p\le n+1\), on a",
    r"\item \emph{Pour tout couple} \((n,p)\) \emph{d'entiers avec} \(p\le n+1\), \emph{on a}", "")
add(227, "proof of Lemme 4.2.2, label",
    "'Preuve :' ('Preuve' underlined) on a line of its own, then '(i) => (ii) : alors ...'",
    r"\begin{prooftext} without argument: the Exposé V environment prints 'Proof.'", "word", "high",
    "\\begin{prooftext}\n\\((i)\\Rightarrow(ii)\\)", "\\emph{Preuve} :\n\n\\((i)\\Rightarrow(ii)\\)",
    "The global form \\emph{Preuve} : (as pp. 38-39). Apply together with the removal of the matching "
    "\\end{prooftext} on p. 228.")

# ---------------- page 228 ----------------
add(228, "top of the page",
    "p. 228 begins with '(ii) => (i) : Si n < p+q'; p. 227 ends with '(i) => (ii) : alors "
    "J^pF^{n-p+1}(X_n) ⊂ F^{n+1}(X_n) = 0 .' (formula run into the line)",
    r"page_228.tex begins with the display J^pF^{\,n-p+1}(X_n)\subset F^{n+1}(X_n)=0. (s5.tex lines 7617-7619, "
    "diplomatic), the end of p. 227", "marker", "high", None, None,
    "Page 228 really begins at s5.tex line 7621 '\\((ii)\\Rightarrow(i)\\): si'. Exact fix: python -I move_marker.py 5 228 "
    "'\\((ii)\\Rightarrow(i)\\)' (forward, no --before; simulated in memory on both layers). Text not moved.",
    fix_null=True)
add(228, "(ii) => (i), first word", "'Si' (capital)", "si", "word", "high",
    r"\): si \(n<p+q\)", r"\): Si \(n<p+q\)", "")
add(228, "'J^{n+1-q}F^q(X_n) et ce dernier est nul par hypothèse'",
    "no comma before 'et ce dernier'", r"\(J^{\,n+1-q}F^q(X_n)\), et ce dernier", "punctuation", "high",
    r"F^q(X_n)\), et ce dernier", r"F^q(X_n)\) et ce dernier", "The TeX adds a comma.")
add(228, "(ii) => (i), second case 'Si n > p+q'", "n > p+q (a clear >, no bar)", r"\(n>p+q\), as printed",
    "misprint_in_print", "high", None, None,
    "After 'Si n < p+q' the case n = p+q is left out; the printed argument covers it unchanged. The TeX keeps the "
    "printed reading; the corrected layer already reads \\(n\\ge p+q\\) (Codex record SGA-SRC-002203).",
    corrected=r"\(n\ge p+q\)", fix_null=True)
add(228, "end of the proof of Lemme 4.2.2", "no environment: 'Preuve :' is a plain label (p. 227)",
    r"\end{prooftext}", "extra", "high",
    "\\end{prooftext}\n", "",
    "Only together with the label fix of p. 227 (\\begin{prooftext} -> \\emph{Preuve} :).")
add(228, "label 'Exemples :'", "'Exemples :' ('Exemples' underlined), on a line of its own",
    r"\paragraph{Exemples.}", "punctuation", "medium",
    "\\paragraph{Exemples.}\n", "\\emph{Exemples} :\n\n",
    "The print has ' :', not a full stop; as p. 90 (\\emph{Exemples.} -> \\emph{Exemples} :) and the global "
    "\\emph{Preuve} :. Medium only for the form of the label.")
add(228, "heading 4.2.3", "'4.2.3. Gradué d'un système projectif adapté à J .' (title underlined, full stop)",
    r"\subsubsection*{4.2.3. ... adapté à \(J\)}", "punctuation", "high",
    r"adapté à \(J\)}", r"adapté à \(J\).}", "Underlined title: the print's full stop.")
add(228, "4.2.3, first display", "gr^p(X)_{p∈N}: no parentheses",
    r"\bigl(\gr^p(X)\bigr)_{p\in\mathbb N}", "formula", "high",
    r"\bigl(\gr^p(X)\bigr)_{p\in\mathbb N}", r"\gr^p(X)_{p\in\mathbb N}",
    "The TeX adds the parentheses. The later grs(X) = (grs^p(X))_{p∈N} has them in the print and is right.")

# ---------------- page 229 ----------------
add(229, "top of the page",
    "p. 229 begins with the display 'ω_pq : J^p/J^{p+1} ⊗_A F^q(X_q) -> F^{p+q}(X_{p+q}) .'; p. 228 ends with "
    "'l'on définit les morphismes correspondants :' and blank paper",
    "the display (s5.tex lines 7652-7654, diplomatic) ends page_228.tex; the folio-229 marker (line 7655) "
    "stands after it, before 'Le'", "marker", "high", None, None,
    "Page 229 really begins at s5.tex line 7652 '\\['. Exact fix: python -I move_marker.py 5 229 '\\[' --before "
    "(simulated in memory on both layers). Text not moved.", fix_null=True)
add(229, "'vu que J^{p+1}F^q(X_{p+q}) ⊂ F^{p+q+1}(X_{p+q}) = 0 , et J^pF^{q+1}(X_{p+q}) ⊂ ...'",
    "'= 0 , et' between the two inclusions", r"=0,\qquad (no 'et')", "missing", "high",
    "=0,\\qquad\n", "=0,\\qquad\\text{et}\\qquad\n",
    "The print runs the two inclusions into the text (layout not reported); only the word is missing.")
add(229, "display after 'à travers'",
    "(J^p/J^{p+1}) ⊗_A (F^q(X_{p+q})/F^{q+1}(X_{p+q})): parentheses around J^p/J^{p+1}",
    r"J^p/J^{p+1}\otimes_A \bigl(...\bigr)", "formula", "high",
    "\\[\nJ^p/J^{p+1}\\otimes_A", "\\[\n(J^p/J^{p+1})\\otimes_A", "As in the next display (beta).")
add(229, "Lemme 4.2.4, before the display",
    "underlined: 'Soit', 'un système projectif', 'adique', 'Le morphisme canonique'; not X, J-, the full stop",
    "no underline markup", "underline", "high",
    r"Soit \(X\) un système projectif \(J\)-adique. Le morphisme canonique",
    r"\emph{Soit} \(X\) \emph{un système projectif} \(J\)-\emph{adique}. \emph{Le morphisme canonique}", "")
add(229, "Lemme 4.2.4, 'Le morphisme canonique,' before the display",
    "a comma after 'canonique'", "no comma", "punctuation", "high",
    "\n\\[\n\\gr_J(A)\\otimes_A X_0", ",\n\\[\n\\gr_J(A)\\otimes_A X_0", "")
add(229, "Lemme 4.2.4, after the display",
    "underlined: 'provenant de la structure de', '-module gradué de', 'est un / épimorphisme'; "
    "not gr_J(A), grs(X), the comma, the stop",
    "no underline markup", "underline", "high",
    r"provenant de la structure de \(\gr_J(A)\)-module gradué de \(\grs(X)\), est un épimorphisme.",
    r"\emph{provenant de la structure de} \(\gr_J(A)\)-\emph{module gradué de} \(\grs(X)\), "
    r"\emph{est un épimorphisme}.", "")
add(229, "proof of Lemme 4.2.4", "'Preuve : Résulte immédiatement ...' ('Preuve' underlined)",
    r"\begin{prooftext} ... \end{prooftext} (prints 'Proof.')", "word", "high",
    "\\begin{prooftext}\nRésulte immédiatement de l'explication des morphismes \\(\\omega_{pq}\\) donnée dans "
    "(4.2.3).\n\\end{prooftext}",
    "\\emph{Preuve} : Résulte immédiatement de l'explication des morphismes \\(\\omega_{pq}\\) donnée dans (4.2.3).",
    "One edit: the environment begins and ends on this page.")
add(229, "Proposition 4.2.5, title",
    "'(Caractérisation des systèmes projectifs stricts AR-J-adiques au moyen des gradués associés) .': in "
    "parentheses; underlined except AR-J-, the parentheses and the stop",
    "Caractérisation ... associés. (no parentheses, no underline)", "punctuation", "high",
    r"Caractérisation des systèmes projectifs stricts AR-\(J\)-adiques au moyen des gradués associés.",
    r"(\emph{Caractérisation des systèmes projectifs stricts} AR-\(J\)-\emph{adiques au moyen des gradués associés}).",
    "One edit: the parentheses and the underline touch.")

# ---------------- page 230 ----------------
add(230, "Proposition 4.2.5, 'indexé par N à valeurs dans C'", "no comma after N",
    r"\(\mathbb N\), à valeurs", "punctuation", "high",
    r"\(\mathbb N\),", r"\(\mathbb N\)", "The TeX adds a comma.")
add(230, "Proposition 4.2.5, 'Soit X un système projectif strict indexé par'",
    "'Soit', 'un système projectif strict indexé par' underlined; X not", "no underline markup", "underline", "high",
    r"Soit \(X\) un système projectif strict indexé par",
    r"\emph{Soit} \(X\) \emph{un système projectif strict indexé par}", "")
add(230, "Proposition 4.2.5, 'à valeurs dans'", "underlined", "no underline markup", "underline", "high",
    "à valeurs dans", r"\emph{à valeurs dans}", "")
add(230, "Proposition 4.2.5, 'On suppose que pour tout entier'", "underlined; 'C .' before it not",
    "no underline markup", "underline", "high",
    "On suppose que pour tout entier", r"\emph{On suppose que pour tout entier}", "")
add(230, "Proposition 4.2.5, 'n , on a :'", "'on a' underlined", "no underline markup", "underline", "high",
    r"\(n\), on a", r"\(n\), \emph{on a}", "")
add(230, "Proposition 4.2.5, 'on a :' before the display J^{n+1}X_n = 0", "a colon after 'on a'", "no colon",
    "punctuation", "high",
    "\n\\[\nJ^{n+1}X_n=0.", ":\n\\[\nJ^{n+1}X_n=0.", "")
add(230, "Proposition 4.2.5, 'Les assertions suivantes sont équivalentes :'", "underlined, not the colon",
    "no underline markup", "underline", "high",
    "Les assertions suivantes sont équivalentes:", r"\emph{Les assertions suivantes sont équivalentes}:", "")
add(230, "Proposition 4.2.5 (i)", "'est', 'adique' underlined; X, AR-J-, the stop not",
    "no underline markup", "underline", "high",
    r"\item \(X\) est AR-\(J\)-adique.", r"\item \(X\) \emph{est} AR-\(J\)-\emph{adique}.", "")
add(230, "Proposition 4.2.5 (ii), 'Il existe un entier r > 0 tel que pour tout entier'",
    "'Il existe un entier', 'tel que pour tout entier' underlined; r > 0 not", "no underline markup",
    "underline", "high",
    r"Il existe un entier \(r>0\) tel que pour tout entier",
    r"\emph{Il existe un entier} \(r>0\) \emph{tel que pour tout entier}", "")
add(230, "Proposition 4.2.5 (ii), 'n l'inclusion ci-dessous soit réalisée :'",
    "no comma after n; 'l'inclusion / ci-dessous soit réalisée' underlined",
    r"\(n\), l'inclusion ci-dessous soit réalisée (no underline)", "punctuation", "high",
    r"\(n\), l'inclusion ci-dessous soit réalisée", r"\(n\) \emph{l'inclusion ci-dessous soit réalisée}",
    "The TeX adds a comma. One edit: the comma and the underline touch.")
add(230, "Proposition 4.2.5 (iii)",
    "underlined: 'Il existe un entier', 'tel que, pour tout entier', 'le morphisme / canonique ci-dessous soit un "
    "isomorphisme dès que'; not r, m, n >= m+r, the colon",
    "no underline markup", "underline", "high",
    r"Il existe un entier \(r\) tel que, pour tout entier \(m\), le morphisme canonique ci-dessous soit un "
    r"isomorphisme dès que",
    r"\emph{Il existe un entier} \(r\) \emph{tel que, pour tout entier} \(m\), \emph{le morphisme canonique "
    r"ci-dessous soit un isomorphisme dès que}", "")
add(230, "Proposition 4.2.5, last sentence 'Dans l'énoncé de (ii) ...'",
    "underlined: 'Dans l'énoncé de', 'on convient de poser', 'pour'; not (ii), the formula, n<r",
    "no underline markup", "underline", "high",
    r"Dans l'énoncé de (ii), on convient de poser \(J^{\,n-r}X_n=X_n\) pour \(n<r\).",
    r"\emph{Dans l'énoncé de} (ii), \emph{on convient de poser} \(J^{\,n-r}X_n=X_n\) \emph{pour} \(n<r\).", "")
add(230, "proof of Proposition 4.2.5, label", "'Preuve : L'équivalence ...' ('Preuve' underlined)",
    r"\begin{prooftext} (prints 'Proof.')", "word", "high",
    "\\begin{prooftext}\nL'équivalence", "\\emph{Preuve} : L'équivalence",
    "Apply together with the removal of the matching \\end{prooftext} at s5.tex line 7752 (p. 231, diplomatic).")
add(230, "proof of Proposition 4.2.5, 'Prouvons celles de (i) et (ii)'", "'celles' (plural; clear)",
    "Prouvons celle de", "misprint_in_print", "high",
    "Prouvons celle de", "Prouvons celles de",
    "Refers to 'l'équivalence' (singular): the print's plural is a typing error; the TeX silently corrects. "
    "The fix restores the printed reading (diplomatic layer only).", corrected="Prouvons celle de")
add(230, "'Considérons alors le diagramme commutatif exact ci-dessous.'", "full stop after 'ci-dessous'",
    "ci-dessous: (colon)", "punctuation", "high",
    "exact ci-dessous:", "exact ci-dessous.", "")
DIAG_OLD = "\n".join([
    r"&&0&&0\\",
    r"&&\downarrow&&\downarrow\\",
    r"&&J^{n+1}X_{m+1}&\longrightarrow&J^{n+1}X_m&\longrightarrow&0\\",
    r"&&\downarrow&&\downarrow\\",
    r"0&\longrightarrow&F^{m+1}(X_{m+1})&\longrightarrow&X_{m+1}&\longrightarrow&X_m&\longrightarrow&0\\",
    r"&&\downarrow&&\downarrow\\",
    r"&&X_{m+1}/J^{n+1}X_{m+1}&\longrightarrow&X_m/J^{n+1}X_m&\longrightarrow&0\\",
    r"&&\downarrow&&\downarrow\\",
    r"&&0&&0",
])
DIAG_NEW = "\n".join([
    r"&&&&0&&0\\",
    r"&&&&\downarrow&&\downarrow\\",
    r"&&&&J^{n+1}X_{m+1}&\longrightarrow&J^{n+1}X_m&\longrightarrow&0\\",
    r"&&&&\downarrow&&\downarrow\\",
    r"0&\longrightarrow&F^{m+1}(X_{m+1})&\longrightarrow&X_{m+1}&\longrightarrow&X_m&\longrightarrow&0\\",
    r"&&&&\downarrow&&\downarrow\\",
    r"&&&&X_{m+1}/J^{n+1}X_{m+1}&\longrightarrow&X_m/J^{n+1}X_m&\longrightarrow&0\\",
    r"&&&&\downarrow&&\downarrow\\",
    r"&&&&0&&0",
])
add(230, "diagram, positions of the two vertical columns",
    "the columns 0 -> J^{n+1}X_{m+1} -> X_{m+1} -> X_{m+1}/J^{n+1}X_{m+1} -> 0 and 0 -> J^{n+1}X_m -> X_m -> "
    "X_m/J^{n+1}X_m -> 0 stand under X_{m+1} and X_m of the middle row",
    "the array puts the columns in array columns 3 and 5, i.e. under F^{m+1}(X_{m+1}) and X_{m+1} "
    "(J^{n+1}X_{m+1} above F^{m+1}(X_{m+1}), X_m/J^{n+1}X_m below X_{m+1})",
    "formula", "high", DIAG_OLD, DIAG_NEW,
    "Shift the top, bottom and vertical-arrow rows two array columns to the right (columns 5 and 7); the middle "
    "row is unchanged.")
add(230, "diagram, end", "no full stop after the bottom 0s", "&&0&&0 .", "punctuation", "high",
    " .\n\\end{array}", "\n\\end{array}", "The TeX adds a full stop at the end of the display.")
add(230, "end of the page",
    "p. 230 ends with the diagram (bottom row '0   0', then blank paper); 'Il' is not on this page",
    "'Il' (s5.tex line 7739, diplomatic), the last line of page_230.tex, stands before the folio-231 marker "
    "(line 7740), which splits 'Il montre'", "marker", "high", None, None,
    "Page 231 really begins at s5.tex line 7739 'Il'. Exact fix: python -I move_marker.py 5 231 'Il' --before "
    "(simulated in memory on both layers). Text not moved.", fix_null=True)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(F), "findings written to", OUT)
