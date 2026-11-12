"""Build findings_131_135.json, check every old (exactly once in its page file, no control characters), and
simulate in memory: the fixes applied page by page to both layers of s5.tex, then the two marker moves.
Nothing but the findings file is written.  usage: python -I -B build_findings.py [--write]"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).parent
RUN = HERE.parent
BATCH = RUN / "b131_135"
W = RUN.parent
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = "<NL>"

LABEL = "Exposé III label form (the statement environment no longer adds a full stop)."
STMT = ("Statement text, underlined in the print; the Exposé III statement environment sets it upright, so the "
        "underline is written \\emph (the file's command for the print's underline), as in the statement fixes of "
        "pp. 79-110.")

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=conf,
             fix=None if old is None else dict(old=old.replace(NL, "\n"), new=new.replace(NL, "\n")))
    if corrected is not None:
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


# ---------------------------------------------------------------- p. 131
add(131, "Théorème 6.10, end of the statement (first line of the page): 'désignant les projections). Alors, avec les "
         "notations de 6.8, 6.9.3, on a'",
    "underlined: 'désignant les projections' (the underline stops before the parenthesis), 'Alors', "
    "'avec les notations de', 'on a'; '6.8, 6.9.3,' not underlined",
    "no underline", "underline", "high",
    r"désignant les projections). Alors, avec les notations de 6.8, 6.9.3, on a",
    r"\emph{désignant les projections}). \emph{Alors}, \emph{avec les notations de} 6.8, 6.9.3, \emph{on a}",
    STMT + " The statement begins on p. 130.")
add(131, "label of Remarques 6.11", "'Remarques 6.11. - a) On vérifie': a full stop after 6.11, then the dash",
    r"\begin{statement}{Remarques 6.11}", "punctuation", "high",
    r"{Remarques 6.11}", r"{Remarques 6.11. -}", LABEL + " This label prints both the full stop and the dash.")
add(131, "6.11 a), end of the first formula 'f_*L -(1)-> (ha)_*a_1^*L -> ... -(2)-> g_*M'",
    "nothing after g_*M (clean paper to the right)", r"\xrightarrow{(2)}g_*M,", "punctuation", "high",
    r"\xrightarrow{(2)}g_*M,", r"\xrightarrow{(2)}g_*M", "The TeX adds the comma.")
add(131, "6.11 a), the second formula '(resp. g_*M -(1)-> ... -(2)-> f_*L) , où (1) est la flèche ...'",
    "typed from the left margin, and the sentence runs on in the same line: 'f_*L)    , où (1) est' "
    "(next line 'la flèche de fonctorialité usuelle ...'); the first formula of a) is indented alone on its line",
    r"a display \[\text{(resp. }g_*M ... f_*L\text{)},\] followed by 'où (1) est' on a new line", "other", "medium",
    r"\[" + NL + r"\text{(resp. }g_*M\xrightarrow{(1)}(hb)_*b_2^*M\xrightarrow{(hb)_*v}(hb)_*b_1^*L=f_*b_{1*}b_1^*L"
    r"\xrightarrow{(2)}f_*L\text{)}," + NL + r"\]" + NL,
    r"(resp. $g_*M\xrightarrow{(1)}(hb)_*b_2^*M\xrightarrow{(hb)_*v}(hb)_*b_1^*L=f_*b_{1*}b_1^*L"
    r"\xrightarrow{(2)}f_*L$)," + NL,
    "Display against inline formula, as the logged fixes of pp. 44 and 122-124: the print runs the text on after "
    "the formula. Medium only because the formula fills its line; the first formula stays a display. One edit; no "
    "overlap with the comma edit above.")
add(131, "(6.11.1), the first product", "'(d_{Z/Y}s_i/s_i)': in parentheses, with a slash",
    r"\frac{d_{Z/Y}s_i}{s_i}", "formula", "high",
    r"\frac{d_{Z/Y}s_i}{s_i}", r"(d_{Z/Y}s_i/s_i)")
add(131, "(6.11.1), the second product", "'(d_{Z/X}t_j/t_j)': in parentheses, with a slash",
    r"\frac{d_{Z/X}t_j}{t_j}", "formula", "high",
    r"\frac{d_{Z/X}t_j}{t_j}", r"(d_{Z/X}t_j/t_j)",
    "The print's second closing parenthesis after t_j closes Res_z( (the TeX's \\right)).")
add(131, "end of display (6.11.1)", "nothing after '(d_{Z/X}t_j/t_j))'", r"\right),", "punctuation", "high",
    r"\right),", r"\right)", "The TeX adds the comma.")
add(131, "label of Corollaire 6.12", "'Corollaire 6.12 - (formule de Woods-Hole [1]).'",
    r"\begin{statement}{Corollaire 6.12}", "punctuation", "high",
    r"{Corollaire 6.12}", r"{Corollaire 6.12 -}", LABEL)
add(131, "Corollaire 6.12, from '(formule de Woods-Hole [1])' to '(i.e. un complexe parfait sur X'",
    "underlined: '(formule de Woods-Hole' (from the opening parenthesis), 'On suppose que', 'est le spectre "
    "d'un corps' (over the line end), 'Soient', 'un', 'schéma propre et lisse' (not 'S-'), 'un', 'endomorphisme de' "
    "(not 'S-'), 'un objet de', 'i.e. un complexe parfait sur' (the parenthesis before it not underlined); "
    "'[1]).', S, X, F, L, D(X)_parf not underlined",
    "no underline", "underline", "high",
    r"(formule de Woods-Hole [1]). On suppose que $S$ est le spectre d'un corps. Soient $X$ un $S$-schéma propre et "
    r"lisse, $F$ un $S$-endomorphisme de $X$, $L$ un objet de $D(X)_{\parf}$ (i.e. un complexe parfait sur $X$",
    r"\emph{(formule de Woods-Hole} [1]). \emph{On suppose que} $S$ \emph{est le spectre d'un corps}. \emph{Soient} "
    r"$X$ \emph{un} $S$-\emph{schéma propre et lisse}, $F$ \emph{un} $S$-\emph{endomorphisme de} $X$, $L$ "
    r"\emph{un objet de} $D(X)_{\parf}$ (\emph{i.e. un complexe parfait sur} $X$",
    STMT + " Ends before the ')' after X, where the comma edit below begins (no overlap).")
add(131, "Corollaire 6.12, '(i.e. un complexe parfait sur X ) u ∈ Hom(F*L,L) . On suppose'",
    "no comma between the closing parenthesis and u: 'X )  u ∈ Hom(F^*L,L)  .'",
    r"$X$), $u\in\Hom(F^*L,L)$", "punctuation", "high",
    r"), $u\in\Hom(F^*L,L)$", r") $u\in\Hom(F^*L,L)$", "The TeX adds the comma.")
add(131, "Corollaire 6.12, from 'On suppose que le schéma des points fixes' to 'Alors on a'",
    "underlined: 'On suppose que le schéma des points fixes', 'est fini et formé de points transversaux "
    "(i.e. où le graphe de' (over the line end, from the parenthesis), 'coupe transversalement la diagonale', "
    "'Alors on a'; X^F, F and ').' not underlined",
    "no underline", "underline", "high",
    r"On suppose que le schéma des points fixes $X^F$ est fini et formé de points transversaux (i.e. où le graphe "
    r"de $F$ coupe transversalement la diagonale). Alors on a",
    r"\emph{On suppose que le schéma des points fixes} $X^F$ \emph{est fini et formé de points transversaux (i.e. "
    r"où le graphe de} $F$ \emph{coupe transversalement la diagonale}). \emph{Alors on a}", STMT)
add(131, "Woods-Hole formula (Corollaire 6.12), left-hand side",
    "a bare typed Σ: 'Σ(-1)^i Tr((F,u),H^i(X,L))'", r"\sum_i(-1)^i", "extra", "high",
    r"\sum_i(-1)^i", r"\sum(-1)^i", "The TeX adds the summation index.")
add(131, "Woods-Hole formula, right-hand side", "'Tr(u_x)/det(1-dF_x)': one line, with a slash",
    r"\frac{\operatorname{Tr}(u_x)}{\det(1-dF_x)}", "formula", "high",
    r"\frac{\operatorname{Tr}(u_x)}{\det(1-dF_x)}", r"\operatorname{Tr}(u_x)/\det(1-dF_x)")
add(131, "Corollaire 6.12 after the formula: 'où (F,u) est l'endomorphisme de H^i(X,L) composé de H^i(X,L) -> ...' "
         "(last line of p. 131)",
    "underlined: 'où', 'est l'endomorphisme de', 'composé de'; the formulas not underlined",
    "no underline", "underline", "high",
    r"où $(F,u)$ est l'endomorphisme de $H^i(X,L)$ composé de $H^i(X,L)",
    r"\emph{où} $(F,u)$ \emph{est l'endomorphisme de} $H^i(X,L)$ \emph{composé de} $H^i(X,L)", STMT)
add(131, "Corollaire 6.12: '(image inverse) et de H^i(X,u) , Tr(u_x) désigne la' (printed at the top of p. 132; in "
         "page_131.tex as the files stand)",
    "underlined: '(image inverse) et de' (from the opening parenthesis), 'désigne la valeur en' (continued in "
    "page_132.tex); H^i(X,u) and Tr(u_x) not underlined",
    "no underline", "underline", "high",
    r"(image inverse) et de $H^i(X,u)$, $\operatorname{Tr}(u_x)$ désigne la",
    r"\emph{(image inverse) et de} $H^i(X,u)$, $\operatorname{Tr}(u_x)$ \emph{désigne la}",
    STMT + " Filed under p. 131 (where the TeX stands): apply before the folio-132 marker move, then use the anchor "
           "given in the p. 132 marker finding.")
add(131, "(6.10.1), cℓ_{Z/Y}(A) cℓ_{Z/X}(B)", "cℓ: c and a script ℓ", r"\cl_{Z/Y}(A)\cl_{Z/X}(B) (\cl = \operatorname{cl})",
    "font", "high", note="Convention of the transcription already reported on pp. 96 and 110 (\\cl throughout Exposé "
                         "III); no edit here, one decision for the volume.")

# ---------------------------------------------------------------- p. 132
add(132, "top of the page",
    "p. 132 begins '(image inverse) et de H^i(X,u) , Tr(u_x) désigne la valeur en x de l'endomorphisme'; "
    "p. 131 ends 'composé de H^i(X,L) -> H^i(X,F*L)'",
    "'(image inverse) et de $H^i(X,u)$, $\\operatorname{Tr}(u_x)$ désigne la' ends s5.tex line 4233, the last line "
    "of page_131.tex; the folio-132 marker (line 4234) follows it", "marker", "high",
    note="Page 132 really begins at '(image inverse)' in s5.tex line 4233 at 20:13 (after '$H^i(X,L)\\to H^i(X,F^*L)$ '). "
         "Exact fix, after this file's fixes are applied (the p. 131 underline fix puts \\emph{ before the "
         "parenthesis): python -I move_marker.py 5 132 '\\emph{(image inverse)' --before; on the files as they "
         "stand: python -I move_marker.py 5 132 '(image inverse)' --before (single quotes; simulated in memory on "
         "both layers: the marker then splits line 4233 after '$H^i(X,L)\\to H^i(X,F^*L)$ '). The moved words agree "
         "with the print apart from the underline fix filed under p. 131.")
add(132, "Corollaire 6.12, 'valeur en x de l'endomorphisme induit par u sur la fibre de L en x , et det(1-dF_x) la "
         "valeur en x du déterminant de l'application'",
    "underlined: 'valeur en' (continuing 'désigne la'), 'de l'endomorphisme induit par' (over the line end), "
    "'sur la fibre de', 'en', 'et', 'la valeur en', 'du dé-terminant de l'application'; x, u, L, det(1-dF_x) and the "
    "commas not underlined",
    "no underline", "underline", "high",
    r"valeur en $x$ de l'endomorphisme induit par $u$ sur la fibre de $L$ en $x$, et $\det(1-dF_x)$ la valeur en $x$ "
    r"du déterminant de l'application",
    r"\emph{valeur en} $x$ \emph{de l'endomorphisme induit par} $u$ \emph{sur la fibre de} $L$ \emph{en} $x$, "
    r"\emph{et} $\det(1-dF_x)$ \emph{la valeur en} $x$ \emph{du déterminant de l'application}", STMT)
add(132, "Corollaire 6.12, '(1 - application induite par F sur Ω^1_{X,x})'",
    "underlined: 'application induite par' and 'sur'", r"\text{application induite par }F\text{ sur }",
    "underline", "high",
    r"\text{application induite par }F\text{ sur }", r"\text{\emph{application induite par} }F\text{ \emph{sur} }",
    STMT + " Kept inside the TeX's \\text{}.")
add(132, "proof label 'Démonstration.'", "the underline covers 'Démonstration' only; the full stop after it is not "
                                          "underlined", r"\emph{Démonstration.}", "underline", "high",
    r"\emph{Démonstration.}", r"\emph{Démonstration}.",
    "As the global '\\emph{Preuve} :' form (punctuation outside the underline).")
add(132, "'(définissant un morphisme étale dans A^n_s )'",
    "the subscript of the double-struck A^n is a small s (compare the capital S of 'X x_S X' two lines above)",
    r"\mathbb A_S^n (silently corrected)", "misprint_in_print", "high",
    r"\mathbb A_S^n", r"\mathbb A_s^n",
    "The base is S (X is an S-scheme; no s is defined). The TeX silently corrects; the fix restores the printed "
    "reading (diplomatic layer only).", corrected=r"\mathbb A_S^n")
add(132, "'Notons qu'au numérateur on peut remplacer dy_i par dy_i - dF_i = dy_i - Σ (dF_i/dx_j)dx_j . Appliquant "
         "alors la formule ([8] III 9 R3)'",
    "the formula is typed from the left margin, not indented, and the sentence runs on in its line: "
    "'... (dF_i/dx_j)dx_j   . Appliquant alors la formule ([8] III 9'",
    r"a display \[dy_i-dF_i=dy_i-\sum_{1\le j\le n}(dF_i/dx_j)dx_j.\] before 'Appliquant'", "other", "medium",
    r"par" + NL + r"\[" + NL + r"dy_i-dF_i=dy_i-\sum_{1\le j\le n}(dF_i/dx_j)dx_j." + NL + r"\]" + NL + r"Appliquant",
    r"par $dy_i-dF_i=dy_i-\sum_{1\le j\le n}(dF_i/dx_j)dx_j$. Appliquant",
    "Display against inline formula, as the logged fixes of pp. 44 and 122-124 (the full stop printed after the "
    "formula is kept, outside it). No overlap with the misprint edit of the same sentence.")
add(132, "'à la situation (B ↪ Z -> S , (s_1,...,s_p) = (y_1 - F_1,...,y_n - F_n) ,'",
    "no closing parenthesis after S: 'S   , (s_1'; the parenthesis opened before B is never closed",
    r"$(B\hookrightarrow Z\to S)$ (silently corrected)", "misprint_in_print", "high",
    r"$(B\hookrightarrow Z\to S)$", r"$(B\hookrightarrow Z\to S$",
    "The TeX silently closes the parenthesis after S; the fix restores the printed reading (diplomatic layer only). "
    "The corrected reading is the TeX's.", corrected=r"$(B\hookrightarrow Z\to S)$")

# ---------------------------------------------------------------- p. 133
add(133, "label of Remarque 6.12.1", "'Remarque 6.12.1 - Si X^F est supposé seulement fini'",
    r"\begin{statement}{Remarque 6.12.1}", "punctuation", "high",
    r"{Remarque 6.12.1}", r"{Remarque 6.12.1 -}", LABEL)
add(133, "Remarque 6.12.1, display, left-hand side", "a bare typed Σ: 'Σ(-1)^i Tr((F,u),H^i(X,L))'",
    r"\sum_i(-1)^i", "extra", "high",
    r"l'on a" + NL + r"\[" + NL + r"\sum_i", r"l'on a" + NL + r"\[" + NL + r"\sum",
    "The TeX adds the summation index (the same left-hand side recurs in 6.13.1, hence the longer old).")
add(133, "(6.13.1), left-hand side", "a bare typed Σ", r"\sum_i(-1)^i", "extra", "high",
    r"\tag{6.13.1}" + NL + r"\sum_i", r"\tag{6.13.1}" + NL + r"\sum", "The TeX adds the summation index.")
add(133, "(6.13.2), left-hand side", "a bare typed Σ: 'Σ(-1)^i Tr(F,H^i(X,O_X))'", r"\sum_i(-1)^i", "extra", "high",
    r"\tag{6.13.2}" + NL + r"\sum_i", r"\tag{6.13.2}" + NL + r"\sum", "The TeX adds the summation index.")
add(133, "'sous la forme Σ(-1)^i Tr(F,H^i(X,F_p))'", "a bare typed Σ", r"$\sum_i(-1)^i\operatorname{Tr}(F,H^i(X,\mathbb F_p))$",
    "extra", "high", r"forme $\sum_i", r"forme $\sum", "The TeX adds the summation index.")

# ---------------------------------------------------------------- p. 134
add(134, "label of Théorème 6.13.3", "'Théorème 6.13. 3 (Deligne) - Soient' (a stray space after the second dot)",
    r"\begin{statement}{Théorème 6.13.3 (Deligne)}", "punctuation", "high",
    r"{Théorème 6.13.3 (Deligne)}", r"{Théorème 6.13.3 (Deligne) -}",
    LABEL + " 'Deligne' is underlined with the label word (the accepted label setting); the stray space is spacing.")
add(134, "Théorème 6.13.3, first sentence 'Soient X_o un schéma ... l'endomorphisme de Frobenius de X/k .'",
    "underlined: 'Soient', 'un schéma séparé et de type fini sur', 'le schéma déduit de', 'par extension des "
    "scalaires à une clôture algébrique', 'de', 'l'endomorphisme de Frobenius de'; X_o, F_q, X, k, F, X/k and the "
    "punctuation not underlined",
    "no underline", "underline", "high",
    r"Soient $X_0$ un schéma séparé et de type fini sur $\mathbb F_q$, $X$ le schéma déduit de $X_0$ par extension "
    r"des scalaires à une clôture algébrique $k$ de $\mathbb F_q$, $F$ l'endomorphisme de Frobenius de $X/k$.",
    r"\emph{Soient} $X_0$ \emph{un schéma séparé et de type fini sur} $\mathbb F_q$, $X$ \emph{le schéma déduit de} "
    r"$X_0$ \emph{par extension des scalaires à une clôture algébrique} $k$ \emph{de} $\mathbb F_q$, $F$ "
    r"\emph{l'endomorphisme de Frobenius de} $X/k$.", STMT)
add(134, "Théorème 6.13.3, 'Alors, pour tout L_o ∈ ob D_ctf(X_o,F_p) , on a, notant L l'image inverse de L_o sur X ,'",
    "underlined: 'Alors, pour tout' and 'on a, notant' (each one line through the comma), 'l'image inverse de', "
    "'sur'; the formulas not underlined",
    "no underline", "underline", "high",
    r"Alors, pour tout $L_0\in\ob D_{\ctf}(X_0,\mathbb F_p)$, on a, notant $L$ l'image inverse de $L_0$ sur $X$,",
    r"\emph{Alors, pour tout} $L_0\in\ob D_{\ctf}(X_0,\mathbb F_p)$, \emph{on a, notant} $L$ \emph{l'image inverse "
    r"de} $L_0$ \emph{sur} $X$,", STMT)
add(134, "Théorème 6.13.3, display, left-hand side", "a bare typed Σ: 'Σ(-1)^i Tr(F,H^i_c(X,L))'",
    r"\sum_i(-1)^i", "extra", "high", r"\sum_i(-1)^i", r"\sum(-1)^i", "The TeX adds the summation index.")
add(134, "'par un corps vérifiant (C_1) ([17] II 3), parexemple C(t) (Tsen)'",
    "'parexemple' typed as one word (no space)", "par exemple (silently corrected)", "misprint_in_print", "high",
    r"par exemple $\mathbb C(t)$", r"parexemple $\mathbb C(t)$",
    "Typing error. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
    corrected="par exemple")
add(134, "'(voir loc. cit. pour d'autre exemples)'", "'d'autre exemples' (no s on autre)",
    "d'autres exemples (silently corrected)", "misprint_in_print", "high",
    r"d'autres exemples", r"d'autre exemples",
    "Agreement error. The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
    corrected="d'autres exemples")

# ---------------------------------------------------------------- p. 135
add(135, "top of the page",
    "p. 135 begins with the paragraph number: '6.14   La formule de Woods Hole a de nombreuses autres "
    "applications'; p. 134 ends '... quand on écrit la condition (C_1) .'",
    "'\\subsection*{6.14}' and 'La' (s5.tex lines 4308-4309 at 20:13) end page_134.tex; the folio-135 marker "
    "(line 4310) follows them, so page_135.tex begins 'formule de Woods Hole'", "marker", "high",
    note="Page 135 really begins at '\\subsection*{6.14}', s5.tex line 4308 at 20:13. Exact fix: python -I "
         "move_marker.py 5 135 '\\subsection*{6.14}' --before (single quotes; simulated in memory on both layers: "
         "the marker then stands on its own line between '... la condition $(C_1)$.' and '\\subsection*{6.14}', "
         "and 'La' joins 'formule de Woods Hole'). The moved words agree with the print.")


# ---------------------------------------------------------------- checks
def pages_of(text):
    ms = list(MARK.finditer(text))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out[int(m.group(2))] = (m.start(), end)
    return out


ok = True
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    for s in (fx["old"], fx["new"]):
        bad = [c for c in s if ord(c) < 32 and c != "\n"]
        if bad:
            print("CONTROL CHAR", x["page"], repr(s[:60]))
            ok = False
    if MARK.search(fx["old"]) or MARK.search(fx["new"]):
        print("TOUCHES MARKER", x["page"])
        ok = False
    t = (BATCH / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        print("COUNT", n, x["page"], repr(fx["old"][:70]))
        ok = False
    if fx["old"] == fx["new"]:
        print("NO CHANGE", x["page"], repr(fx["old"][:60]))
        ok = False
print("checks:", "all olds unique" if ok else "PROBLEMS")


def move_marker(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for layer in ("diplomatic", "current"):
    t = (W / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")
    applied = skipped = 0
    for x in F:
        fx = x["fix"]
        if not fx:
            continue
        if layer == "current" and x["kind"] == "misprint_in_print":
            continue
        s, e = pages_of(t)[x["page"]]
        k = t.find(fx["old"], s, e)
        if k < 0 or t.find(fx["old"], k + 1, e) >= 0 and t.find(fx["old"], k + 1, e) + len(fx["old"]) <= e:
            skipped += 1
            print(layer, "not applied:", x["page"], repr(fx["old"][:60]))
            continue
        t = t[:k] + fx["new"] + t[k + len(fx["old"]):]
        applied += 1
    print(layer, "applied", applied, "skipped", skipped)
    for folio, anchor in ((132, r"\emph{(image inverse)"), (135, r"\subsection*{6.14}"), ):
        t3 = move_marker(t, folio, anchor)
        if t3 is None:
            print(layer, folio, "anchor not found")
            continue
        t = t3
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print(f"--- {layer} folio {folio}:")
        print(t[m.start() - 160:m.end() + 120])
    # the as-they-stand anchor of 132 on the unmodified file
    t0 = (W / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")
    t4 = move_marker(t0, 132, "(image inverse)")
    m = next(m for m in MARK.finditer(t4) if int(m.group(2)) == 132)
    print(f"--- {layer} folio 132 on the files as they stand:")
    print(t4[m.start() - 80:m.end() + 80])

if "--write" in sys.argv and ok:
    out = RUN / "findings_131_135.json"
    out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", out, len(F), "findings")
