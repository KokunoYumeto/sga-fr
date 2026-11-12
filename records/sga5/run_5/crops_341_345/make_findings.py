import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b341_345"
OUT = RUN / "findings_341_345.json"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------- p. 341 ----------------
add(341, "(9.4.2)",
    "j_1*(j_1)_*g_1*(a) = [empty space] g_1*(b_p)ξ̄^p , with the typed index 0≤p≤d under the empty space: no summation sign",
    r"\sum_{0\le p\le d}",
    "misprint_in_print", "medium",
    fx(r"\sum_{0\le p\le d}", r"\mathop{\phantom{\sum}}\limits_{0\le p\le d}"),
    "The space left for the sign is empty: nothing darker than the paper between '=' and 'g' (pixel check), so not a "
    "faint stroke; the sign was never put in (on p. 344 the typed Σ of (9.7.1)-(9.7.3) prints normally). The TeX "
    "silently supplies \\sum.",
    r"\sum_{0\le p\le d}")
add(341, "text after (9.4.2)",
    "(ce qui d'ailleurs équivalent d'après 9.1.1)",
    "(ce qui d'ailleurs équivalent d'après 9.1.1)",
    "misprint_in_print", "high", None,
    "The verb 'est' is missing in the print; the TeX keeps the printed reading.",
    "(ce qui est d'ailleurs équivalent d'après 9.1.1)")
add(341, "after (9.4.3)",
    "z ∈ C•(N̂): C with a raised dot",
    r"z\in C^*(\widehat N)",
    "symbol", "high",
    fx(r"z\in C^*(\widehat N)", r"z\in C^{\bullet}(\widehat N)"),
    "A round raised dot, not the six-pointed asterisk of g_1* on the same lines (as A• on pp. 290-295).")
add(341, "after (9.4.3)",
    "aux deux membres de (9.4.3) on obtient, compte tenu (no comma after (9.4.3))",
    "aux deux membres de (9.4.3), on obtient",
    "punctuation", "high",
    fx("membres de (9.4.3), on obtient", "membres de (9.4.3) on obtient"),
    "The TeX adds a comma.")
add(341, "(9.4.4)",
    "[(j_1)_*g*(a)].(j_1)_*(1) - v_*(1).(j_1)_*(z).",
    r"\bigl[(j_1)_*g_1^*(a)\bigr](j_1)_*(1)-v_*(1)(j_1)_*(z).",
    "symbol", "high",
    fx("(j_1)_*(1)-v_*(1)(j_1)_*(z).", r"\cdot(j_1)_*(1)-v_*(1)\cdot(j_1)_*(z)."),
    "The TeX drops the two product dots (the typewriter's full stop, written \\cdot as in (9.5.2) on p. 342). "
    "Independent of the next item.")
add(341, "(9.4.4)",
    "[(j_1)_*g*(a)]: g without the index 1",
    r"\bigl[(j_1)_*g_1^*(a)\bigr]",
    "misprint_in_print", "high",
    fx(r"g_1^*(a)\bigr]", r"g^*(a)\bigr]"),
    "No stroke under the g (the left side has g_1*(b_o)); the TeX silently corrects.",
    r"g_1^*(a)\bigr]")
add(341, "before (9.4.5)",
    "déduite de (9.3.4), on obtient :",
    "déduite de (9.3.4), on obtient",
    "punctuation", "high",
    fx("déduite de (9.3.4), on obtient", "déduite de (9.3.4), on obtient :"),
    "The TeX drops the colon.")
add(341, "(9.4.5)",
    "(j_1)_*g_1*(a).f_1*u_*(1)-v_*(1).[(j_1)_*g_1*(a)+(j_1)_*(z)].",
    r"(j_1)_*g_1^*(a)f_1^*u_*(1)-v_*(1)\bigl[(j_1)_*g_1^*(a)+(j_1)_*(z)\bigr].",
    "symbol", "high",
    fx(r"g_1^*(a)f_1^*u_*(1)-v_*(1)\bigl[", r"g_1^*(a)\cdot f_1^*u_*(1)-v_*(1)\cdot\bigl["),
    "The TeX drops the two product dots.")
add(341, "(9.4.6)",
    "(j_1)_*g_1*(a).f_1*u_*(1) = 0 .",
    r"(j_1)_*g_1^*(a)f_1^*u_*(1)=0.",
    "symbol", "high",
    fx("(a)f_1^*u_*(1)=0", r"(a)\cdot f_1^*u_*(1)=0"),
    "The TeX drops the product dot.")
add(341, "(9.4.7)",
    "= -v_*(1)[j_1)_*g_1*(a)+(j_1)_*(z)].: no parenthesis after the bracket",
    r"=-v_*(1)\bigl[(j_1)_*g_1^*(a)+(j_1)_*(z)\bigr].",
    "misprint_in_print", "high",
    fx(r"=-v_*(1)\bigl[(j_1)", r"=-v_*(1)\bigl[j_1)"),
    "An opening parenthesis is missing in the print; the TeX silently adds it.",
    r"=-v_*(1)\bigl[(j_1)")
add(341, "before (9.4.8)",
    "d'où par (9.4.7) :",
    "d'où par (9.4.7)",
    "punctuation", "high",
    fx("d'où par (9.4.7)", "d'où par (9.4.7) :"),
    "The TeX drops the colon.")

# ---------------- p. 342 ----------------
add(342, "heading 9.5",
    "9.5. (with a full stop)",
    r"\subsection*{9.5}",
    "punctuation", "high",
    fx(r"\subsection*{9.5}", r"\subsection*{9.5.}"),
    "As '3.3.' and '3.8.' (pp. 290, 295); the '9.8' of p. 345 has no stop.")
add(342, "9.5, line 2",
    "Si y ∈ C•(Y): C with a raised dot",
    r"y\in C^*(Y)",
    "symbol", "high",
    fx(r"y\in C^*(Y)", r"y\in C^{\bullet}(Y)"),
    "Raised dot, as p. 341.")
add(342, "(9.5.1)",
    "i*i_*(y) = (i_1)*(x̄) , avec x̄ = p*i_*(y) .",
    r"i^*i_*(y)=(i_1)^*(\bar x),\qquad \bar x=p^*i_*(y).",
    "missing", "high",
    fx(r"(i_1)^*(\bar x),\qquad", r"(i_1)^*(\bar x),\quad\text{avec}\quad"),
    "The TeX drops the word 'avec'.")
add(342, "before (9.5.3)",
    "au dessus de Z ∸ Y: one bar with a dot above it",
    r"Z\doteq Y",
    "symbol", "high",
    fx(r"Z\doteq Y", r"Z\mathbin{\dot{-}}Y"),
    "One bar (5 pixel rows) under the dot; the '=' of 'Z = X x P1' two lines higher has two 3-row bars 3 rows apart. "
    "It stands for Z - Y (outside the centre of the blow-up); \\doteq is an equals sign with a dot.")
add(342, "(9.5.3)",
    "f_1*(x̄) = θ + (j_1)_*(w), avec w ∈ C•(N̂) .",
    r"f_1^*(\bar x)=\theta+(j_1)_*(w),\qquad w\in C^*(\widehat N).",
    "missing", "high",
    fx(r"(j_1)_*(w),\qquad", r"(j_1)_*(w),\quad\text{avec}\quad"),
    "The TeX drops the word 'avec'.")
add(342, "(9.5.3)",
    "w ∈ C•(N̂): C with a raised dot",
    r"w\in C^*(\widehat N)",
    "symbol", "high",
    fx(r"w\in C^*", r"w\in C^{\bullet}"),
    "Raised dot, as p. 341.")

# ---------------- p. 343 ----------------
add(343, "first paragraph",
    '"formule-clef" (straight typewriter quotes)',
    "«formule-clef»",
    "punctuation", "high",
    fx("«formule-clef»", "``formule-clef''"),
    "Guillemets for the print's straight quotes (as the logged p. 110).")
add(343, "first paragraph",
    '(pour "hyperplan") (straight typewriter quotes)',
    "(pour «hyperplan»)",
    "punctuation", "high",
    fx("«hyperplan»", "``hyperplan''"),
    "As the previous item.")
add(343, "Proposition 9.6, first sentence",
    "underlined: 'Soient' | 'un corps séparablement clos et' | 'une immersion fermée, purement de codimension' | 'de' | "
    "'schémas quasiprojectifs et lisses. Désignant par' | 'le' | 'schéma obtenu en faisant éclater' | 'le long de' | "
    "'soit'; k, i : Y -> X, d, 'k-', f : X' -> X, 'X-', X, Y not underlined",
    "no underline",
    "underline", "high",
    fx(r"Soient $k$ un corps séparablement clos et $i:Y\hookrightarrow X$ une immersion fermée, purement de "
       r"codimension $d$, de $k$-schémas quasiprojectifs et lisses. Désignant par $f:X'\to X$ le $X$-schéma obtenu "
       r"en faisant éclater $X$ le long de $Y$, soit",
       r"\emph{Soient} $k$ \emph{un corps séparablement clos et} $i:Y\hookrightarrow X$ \emph{une immersion fermée, "
       r"purement de codimension} $d$, \emph{de} $k$-\emph{schémas quasiprojectifs et lisses. Désignant par} "
       r"$f:X'\to X$ \emph{le} $X$-\emph{schéma obtenu en faisant éclater} $X$ \emph{le long de} $Y$, \emph{soit}"),
    "Exposé VII statements are underlined word group by word group; \\emph as in the logged statements of pp. 283-295.")
add(343, "Proposition 9.6, diagram, top arrow",
    "Y' ↪ X' (hooked arrow, label j above)",
    'Y\'\\arrow[r,"j"]',
    "symbol", "high",
    fx('Y\'\\arrow[r,"j"]', 'Y\'\\arrow[r,hook,"j"]'),
    "The print draws the hook at the tail of the arrow.")
add(343, "Proposition 9.6, diagram, bottom arrow",
    "Y ↪ X (hooked arrow, label i above the arrow)",
    'Y\\arrow[r,"i"\']&X',
    "symbol", "high",
    fx('Y\\arrow[r,"i"\']', 'Y\\arrow[r,hook,"i"]'),
    "Hook as on the top arrow; the print also sets the label i above the arrow, the TeX below (one edit gives both).")
add(343, "Proposition 9.6, after the diagram",
    "underlined: 'le diagramme cartésien construit à partir de' | 'et' | 'Alors, notant' | 'le' | "
    "'Module localement libre défini par la suite exacte canonique'; f, i, F, 'O_Y'-' not; Module with a capital M",
    r"le diagramme cartésien construit à partir de $f$ et $i$. Alors, notant $F$ le $\mathcal O_{Y'}$-module "
    r"localement libre défini par la suite exacte canonique",
    "underline", "high",
    fx(r"le diagramme cartésien construit à partir de $f$ et $i$. Alors, notant $F$ le $\mathcal O_{Y'}$-module "
       r"localement libre défini par la suite exacte canonique",
       r"\emph{le diagramme cartésien construit à partir de} $f$ \emph{et} $i$. \emph{Alors, notant} $F$ \emph{le} "
       r"$\mathcal O_{Y'}$-\emph{Module localement libre défini par la suite exacte canonique}"),
    "One edit: it also gives the print's capital M (word).")
add(343, "Proposition 9.6, before (9.6.2)",
    "'on a l'égalité' underlined",
    "on a l'égalité",
    "underline", "high",
    fx("on a l'égalité", r"\emph{on a l'égalité}"),
    "")
add(343, "(9.6.2)",
    "f*i_*(y) = j_*(g*(y)c_{d-1}(F̌)) ,",
    r"f^*i_*(y)=j_*(g^*(y)c_{d-1}(\check F))",
    "punctuation", "high",
    fx(r"g^*(y)c_{d-1}(\check F))", r"g^*(y)c_{d-1}(\check F)),"),
    "The TeX drops the comma at the end of the display.")
add(343, "Proposition 9.6, last line",
    "'dans' and 'pour tout' underlined; C•(X'), y ∈ C•(Y) with raised dots",
    r"dans $C^*(X')$, pour tout $y\in C^*(Y)$.",
    "underline", "high",
    fx(r"dans $C^*(X')$, pour tout $y\in C^*(Y)$.",
       r"\emph{dans} $C^{\bullet}(X')$, \emph{pour tout} $y\in C^{\bullet}(Y)$."),
    "One edit: it also gives the two raised dots (symbol, as p. 341).")
add(343, "Lemme 9.7",
    "'On a les égalités' underlined, then ' :'",
    "On a les égalités:",
    "underline", "high",
    fx("On a les égalités:", r"\emph{On a les égalités} :"),
    "")
add(343, "Lemme 9.7 (i)",
    "c_d(Ě) = k_*(c_{d-1}(F̌)) + (g_1)*(c_d(Ň)).",
    r"c_d(\check E)=k_*(c_{d-1}(\check F))+(g_1)^*(c_d(\check N)),",
    "punctuation", "high",
    fx(r"(c_d(\check N)),", r"(c_d(\check N))."),
    "The print ends with a full stop, the TeX with a comma.")
add(343, "Lemme 9.7 (i), number",
    "(i)",
    r"\tag{9.7 i}",
    "number", "high",
    fx(r"\tag{9.7 i}", r"\tag{i}"),
    "The print numbers the three lines (i), (ii), (iii); the TeX prints (9.7 i). Apply with the next two items.")
add(343, "Lemme 9.7 (ii), number",
    "(ii)",
    r"\tag{9.7 ii}",
    "number", "high",
    fx(r"\tag{9.7 ii}", r"\tag{ii}"),
    "As the previous item.")
add(343, "Lemme 9.7 (iii), number",
    "(iii)",
    r"\tag{9.7 iii}",
    "number", "high",
    fx(r"\tag{9.7 iii}", r"\tag{iii}"),
    "As the previous item.")
add(343, "Lemme 9.7 (ii)",
    "'pour tout' underlined",
    r"\text{pour tout }y",
    "underline", "high",
    fx(r"(y)\qquad\text{pour tout }y", r"(y)\qquad\text{\emph{pour tout} }y"),
    "")
add(343, "Lemme 9.7 (ii)",
    "y ∈ C•(Y) . (raised dot; full stop at the end)",
    r"y\in C^*(Y),",
    "symbol", "high",
    fx(r"\in C^*(Y),", r"\in C^{\bullet}(Y)."),
    "One edit: it also gives the print's full stop for the TeX's comma (punctuation).")
add(343, "Lemme 9.7 (iii)",
    "(j_1)_*[(i o g_1)*(t)]: square brackets",
    r"(j_1)_*((i\circ g_1)^*(t))",
    "formula", "high",
    fx(r"(j_1)_*((i\circ g_1)^*(t))", r"(j_1)_*[(i\circ g_1)^*(t)]"),
    "The TeX has parentheses for the print's brackets.")
add(343, "Lemme 9.7 (iii)",
    "'pour tout' underlined",
    r"\text{pour tout }t",
    "underline", "high",
    fx(r"(t)\qquad\text{pour tout }t", r"(t)\qquad\text{\emph{pour tout} }t"),
    "")
add(343, "Lemme 9.7 (iii)",
    "t ∈ C•(X): raised dot",
    r"t\in C^*(X)",
    "symbol", "high",
    fx(r"\in C^*(X)", r"\in C^{\bullet}(X)"),
    "Raised dot, as p. 341.")

# ---------------- p. 344 ----------------
add(344, "top of the page",
    "p. 344 begins with 'Preuve : Montrons (i). On pose ξ = c_1(O_Y'(1)) = k*(ξ̄). En paraphrasant la preuve de "
    "(8.4.1), on obtient les égalités :'",
    "page_344.tex begins at 'obtient les égalités'; the line '\\emph{Preuve} : Montrons (i). ... de (8.4.1), on' is "
    "the last line of page_343.tex",
    "marker", "high", None,
    "Page 344 really begins at the line '\\emph{Preuve} : Montrons (i). On pose ...' (after the blank line that follows "
    "\\end{statement} of Lemme 9.7; s5.tex diplomatic line 11720, current 11716). Exact fix: python -I move_marker.py "
    "5 344 '\\emph{Preuve} : Montrons (i)' --before. That line has no other finding.")
add(344, "Preuve, line 2",
    "on obtient les égalités :",
    "on obtient les égalités",
    "punctuation", "high",
    fx("obtient les égalités", "obtient les égalités :"),
    "The TeX drops the colon.")
add(344, "(9.7.1)",
    "c_d(Ě) = Σ_{p=0}^d g_1*(c_p(Ň))ξ̄^{d-p} .",
    r"c_d(\check E)=\sum_{p=0}^d g_1^*(c_p(\check N))\bar\xi^{\,d-p},",
    "punctuation", "high",
    fx(r"\bar\xi^{\,d-p},", r"\bar\xi^{\,d-p}."),
    "The print ends with a full stop, the TeX with a comma.")
add(344, "after (9.7.2)",
    "De (9.7.2), on déduit :",
    "De (9.7.2), on déduit",
    "punctuation", "high",
    fx("De (9.7.2), on déduit", "De (9.7.2), on déduit :"),
    "The TeX drops the colon.")
add(344, "after (9.7.3)",
    "Alors le cycle γ_*(y) = y x 0 et rationnellement équivalent",
    r"Alors le cycle $\gamma_*(y)=y\times0$ est rationnellement équivalent",
    "misprint_in_print", "high",
    fx("$ est rationnellement", "$ et rationnellement"),
    "'et' for 'est' in the print; the TeX silently corrects.",
    "$ est rationnellement")
add(344, "after (9.7.4)",
    "(y x 1)∩(Y x 0) = ∅: capital Y in the second factor",
    r"(y\times1)\cap(y\times0)=\emptyset",
    "formula", "high",
    fx(r"\cap(y\times0)", r"\cap(Y\times0)"),
    "The print has the capital Y (the zero section Y x 0, which also makes sense); the TeX has a small y.")
add(344, "before (9.7.5)",
    "il résulte de (9.1.2) que :",
    "il résulte de (9.1.2) que",
    "punctuation", "high",
    fx("il résulte de (9.1.2) que", "il résulte de (9.1.2) que :"),
    "The TeX drops the colon.")
add(344, "(9.7.5)",
    "p*(t).u_*(1),",
    r"p^*(t)u_*(1),",
    "symbol", "high",
    fx(r"p^*(t)u_*(1)", r"p^*(t)\cdot u_*(1)"),
    "The TeX drops the product dot. Independent of the next item.")
add(344, "(9.7.5)",
    "_*(t) = p*(t).u_*(1), : no letter before the subscript star",
    r"u_*(t)=p^*(t)u_*(1),",
    "misprint_in_print", "medium",
    fx("\\[\nu_*(t)", "\\[\n{}_*(t)"),
    "The u is missing in the print: nothing darker than the paper left of the star (pixel check) while the rest of the "
    "line is crisp, so a typing omission rather than a lost stroke. The TeX silently supplies it.",
    "\\[\nu_*(t)")
add(344, "last line",
    "d'où (iii) puisque p o f_1 o j_1 = ...",
    r"d'où (iii), puisque $p\circ f_1\circ j_1=",
    "punctuation", "high",
    fx("d'où (iii), puisque", "d'où (iii) puisque"),
    "The TeX adds a comma.")

# ---------------- p. 345 ----------------
add(345, "top of the page",
    "p. 345 begins with the heading '9.8' and 'Montrons maintenant 9.6.'",
    "'\\subsection*{9.8}' is the last line of page_344.tex; page_345.tex begins at 'Montrons maintenant 9.6.'",
    "marker", "high", None,
    "Page 345 really begins at '\\subsection*{9.8}' (s5.tex diplomatic line 11763, current 11759). Exact fix: "
    "python -I move_marker.py 5 345 '\\subsection*{9.8}' --before. The heading is printed '9.8' without a stop, as "
    "the TeX.")
add(345, "before the first unnumbered display",
    "De (9.7) (iii) résulte :",
    "De (9.7) (iii) résulte",
    "punctuation", "high",
    fx("De (9.7) (iii) résulte", "De (9.7) (iii) résulte :"),
    "The TeX drops the colon.")
add(345, "(9.8.2)",
    "f_1*(i_1)_*(y) - (j_1)_*g_1*(y c_d(Ň)).: no brackets",
    r"f_1^*(i_1)_*(y)-(j_1)_*[g_1^*(y\,c_d(\check N))].",
    "formula", "high",
    fx(r"(i_1)_*(y)-(j_1)_*[g_1^*(y\,c_d(\check N))]", r"(i_1)_*(y)-(j_1)_*g_1^*(y\,c_d(\check N))"),
    "The TeX adds square brackets.")
add(345, "display after 'on a immédiatement'",
    "(j_1)_*[(k_*k*g_1*(y))c_{d-1}(F̌)] ,",
    r"(j_1)_*\bigl[k_*k^*g_1^*(y)c_{d-1}(\check F)\bigr],",
    "misprint_in_print", "medium",
    fx(r"\bigl[k_*k^*g_1^*(y)c_{d-1}", r"\bigl[(k_*k^*g_1^*(y))c_{d-1}"),
    "The print's parentheses are misplaced: c_{d-1}(F̌) lives on Y', so k_* must apply to the product (v_*j_* = "
    "(j_1)_*k_*, g* = k*g_1*); the next display follows by the projection formula for k. The TeX silently drops them.",
    r"\bigl[k_*(k^*g_1^*(y)c_{d-1}(\check F))\bigr]")
add(345, "display after 'par la formule de projection pour k'",
    "v_*j_*(g*(y)c_{d-1}(F̌)]=(j_1)_*[...]: the parenthesis opened after j_* is closed by a bracket",
    r"v_*j_*(g^*(y)c_{d-1}(\check F)]",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading.",
    r"v_*j_*(g^*(y)c_{d-1}(\check F))")
add(345, "before (9.8.3)",
    "Utilisant (9.7)(i), on en déduit :",
    "Utilisant (9.7)(i), on en déduit",
    "punctuation", "high",
    fx("Utilisant (9.7)(i), on en déduit", "Utilisant (9.7)(i), on en déduit :"),
    "The TeX drops the colon.")
add(345, "(9.8.3)",
    "=(j_1)_*(g_1*(y)c_d(Ě))-(j_1)_*g_1*(y c_d(Ň)).: parentheses, then no brackets",
    r"=(j_1)_*[g_1^*(y)c_d(\check E)]-(j_1)_*[g_1^*(y\,c_d(\check N))].",
    "formula", "high",
    fx(r"=(j_1)_*[g_1^*(y)c_d(\check E)]-(j_1)_*[g_1^*(y\,c_d(\check N))]",
       r"=(j_1)_*(g_1^*(y)c_d(\check E))-(j_1)_*g_1^*(y\,c_d(\check N))"),
    "The TeX has brackets for the print's parentheses and adds brackets to the second term.")
add(345, "(9.8.4)",
    "(j_1)_*(g_1*(y)c_d(Ě)),",
    r"(j_1)_*[g_1^*(y)c_d(\check E)],",
    "formula", "high",
    fx(r"(y)=(j_1)_*[g_1^*(y)c_d(\check E)],", r"(y)=(j_1)_*(g_1^*(y)c_d(\check E)),"),
    "The TeX has brackets for the print's parentheses.")
add(345, "after (9.8.4)",
    "i.e. l'égalité correspondant à (9.6.2)",
    "c'est-à-dire l'égalité correspondant à (9.6.2)",
    "word", "high",
    fx("c'est-à-dire l'égalité", "i.e. l'égalité"),
    "The TeX writes the abbreviation out.")
add(345, "after (9.8.4)",
    "lorsqu'on remplace par X x P1 (no X after 'remplace')",
    r"lorsqu'on remplace $X$ par $X\times\mathbb P^1$",
    "misprint_in_print", "high",
    fx("remplace $X$ par", "remplace par"),
    "The object of 'remplace' is missing in the print; the TeX silently adds it.",
    "remplace $X$ par")
add(345, "display after 'Par (9.1.2), on a'",
    "(j_1)_*(g_1*(y)c_d(Ě))=(j_1)_*s_*(y) = β_*δ_*(y).",
    r"(j_1)_*[g_1^*(y)c_d(\check E)]=(j_1)_*s_*(y)=\beta_*\delta_*(y).",
    "formula", "high",
    fx(r"(j_1)_*[g_1^*(y)c_d(\check E)]=(j_1)_*s_*(y)", r"(j_1)_*(g_1^*(y)c_d(\check E))=(j_1)_*s_*(y)"),
    "The TeX has brackets for the print's parentheses.")
add(345, "before (9.8.5)",
    "(cf. (D_1) que δ_* = f_2*γ_* , d'où : (the parenthesis opened before 'cf.' is not closed)",
    r"(cf. $(D_1)$) que",
    "misprint_in_print", "high",
    fx("$(D_1)$) que", "$(D_1)$ que"),
    "A closing parenthesis is missing in the print; the TeX silently adds it.",
    "$(D_1)$) que")
add(345, "(9.8.5)",
    "(j_1)_*(g_1*(y) c_d(Ě)) = β_*f_2*γ_*(y).",
    r"(j_1)_*[g_1^*(y)\,c_d(\check E)]=\beta_*f_2^*\gamma_*(y).",
    "formula", "high",
    fx(r"(j_1)_*[g_1^*(y)\,c_d(\check E)]", r"(j_1)_*(g_1^*(y)\,c_d(\check E))"),
    "The TeX has brackets for the print's parentheses.")

# ---------------- checks ----------------
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = t.count(old)
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in d["fix"]["new"]:
        bad += 1
        print("MARKER IN FIX", d["page"], repr(old))
# overlap check per page (olds must not overlap in the original text)
from collections import defaultdict
spans = defaultdict(list)
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    k = t.find(d["fix"]["old"])
    spans[d["page"]].append((k, k + len(d["fix"]["old"]), d["fix"]["old"][:30]))
for p, ss in spans.items():
    ss.sort()
    for a, b in zip(ss, ss[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
# sequential application check: every fix still applies after all the others
for p in sorted(spans):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    fixes = [d["fix"] for d in F if d["page"] == p and d["fix"]]
    for fxd in fixes:
        if t.count(fxd["old"]) != 1:
            bad += 1
            print("SEQ FAIL", p, repr(fxd["old"]))
        t = t.replace(fxd["old"], fxd["new"], 1)
print("findings", len(F), "problems", bad)
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted({d["page"] for d in F}):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT)
