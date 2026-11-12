"""Build findings_306_310.json; check every fix's old: exactly once in the original page file and exactly once at its
turn when the page's fixes are applied in the listed order. <NL> stands for a line feed."""
import json, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b306_310"
OUT = RUN / "findings_306_310.json"

def nl(s):
    return None if s is None else s.replace("<NL>", "\n")

F = []
def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None, fix_null=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix_null else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)

UL = "Exposé VII: \\emph is the file's underline (as the applied statements of pp. 283-295)."
MOD = "Capital M (sheaf of modules), as the logged 'Module' fixes of pp. 286-295."
RPLAIN = "The typewriter's plain R; \\R is \\mathbb{R} in this file (\\mathrm{R} as the logged fixes of pp. 274-285)."
DOT = "The print's raised dot, not a star (A^{\\bullet} as the logged fixes of pp. 290-295)."

# ---------------- page 306
add(306, "section title 5", "5. SCHEMAS DE DRAPEAUX (capitals, underlined)", r"\section*{5. Schémas de drapeaux}",
    "word", "high", r"\section*{5. Schémas de drapeaux}", r"\section*{5. SCHÉMAS DE DRAPEAUX}",
    "Capitals as printed, as the applied titles 1-3 of Exposé VII (FIBRES VECTORIELS, SCHÉMAS PROJECTIFS, CLASSES DE CHERN); accented É by the volume's rule.")
add(306, "first sentence, 'E un O_S-Module localement libre de rang r'", "O_S-Module (script O)", r"$\mathcal O_S$-module",
    "word", "high", r"$\mathcal O_S$-module", r"$\mathcal O_S$-Module", MOD)
add(306, "'On rappelle qu'on appelle drapeau de type (p_1,...,p_m) de E'", "'drapeau de type' underlined", "no underline",
    "underline", "high", r"appelle drapeau de type", r"appelle \emph{drapeau de type}", "Defined term. " + UL)
add(306, "'de E telle que pour tout entier i ∈ [1,m] le quotient'", "no commas", r"telle que, pour tout entier $i\in[1,m]$, le quotient",
    "punctuation", "high", r"telle que, pour tout entier $i\in[1,m]$, le quotient", r"telle que pour tout entier $i\in[1,m]$ le quotient",
    "The TeX adds two commas.")
add(306, "'(EGA I 2ème édition)'", "2 with a raised 'ème'", "2ème on the line",
    "word", "high", r"2ème édition", r"2\textsuperscript{ème} édition",
    "\\textsuperscript{ème} as the file's '2\\textsuperscript{ème} Réduction'.")
add(306, "'et on appelle S-schéma des drapeaux de type (p_1,...,p_m) de E tout représentant'", "'schéma des drapeaux de type' underlined (not the S-)", "no underline",
    "underline", "high", r"appelle $S$-schéma des drapeaux de type", r"appelle $S$-\emph{schéma des drapeaux de type}", "Defined term. " + UL)
add(306, "'le O_X-Module f*(E) admet une filtration finie canonique'", "O_X- Module (script O)", r"$\mathcal O_X$-module",
    "word", "high", r"$\mathcal O_X$-module", r"$\mathcal O_X$-Module", MOD)
add(306, "'Notant pour tout entier i ∈ [1,m]' before g_i : D_i → X", "no commas", r"Notant, pour tout entier $i\in[1,m]$,",
    "punctuation", "high", r"Notant, pour tout entier $i\in[1,m]$,", r"Notant pour tout entier $i\in[1,m]$",
    "The TeX adds two commas.")
add(306, "display (5.1) (printed at the top of p. 307; in page_306.tex as the files stand)",
    "h = f o g : Π_X D_i → S, with i under the product sign and X as its subscript (fibre product over X)",
    r"h=f\circ g:\prod_iD_i\to S", "formula", "high", r"\prod_iD_i\to S", r"\prod_i{}_XD_i\to S",
    "Printed on p. 307; filed under p. 306, where the display stands until the marker move of p. 307 (the edit does not touch the move's anchor '\\['). Same form as D = Π_X(D_i) on p. 307.")

# ---------------- page 307
add(307, "top of the page: display (5.1)",
    "p. 307 begins with '(5.1) h = f o g : Π_X D_i → S'; p. 306 ends '... X-schémas D_i , il est clair que le composé' and blank space",
    "'\\[', 'h=f\\circ g:\\prod_iD_i\\to S', '\\tag{5.1}', '\\]' end page_306.tex (diplomatic s5.tex lines 10372-10375); the folio-307 marker (line 10376) stands after them, before 'est $S$-'",
    "marker", "high", None, None,
    "Page 307 really begins at the '\\[' that opens display (5.1) (diplomatic s5.tex line 10372, current 10367, at the time of the check). Exact fix: python -I move_marker.py 5 307 '\\[' --before (simulated in memory on both layers: the nearest '\\[' before the marker is that of (5.1); the marker then stands on its own line between '... il est clair que le composé' and '\\['). Text not moved.",
    fix_null=True)
add(307, "'donc écrire D = Π_X(D_i) .'", "D = Π_X(D_i) . with i under the product sign, X as its subscript, parentheses around D_i",
    r"D=\prod_iD_i.", "formula", "high", r"D=\prod_iD_i.", r"D=\prod_i{}_X(D_i).",
    "The TeX drops the subscript X and the parentheses (as display (5.1)).")
add(307, "Proposition 5.2, statement", "'On a, dans' and 'un isomorphisme' underlined; D^b(S,A), not", "no underline",
    "underline", "high", r"On a, dans $D^b(S,A)$, un isomorphisme", r"\emph{On a, dans} $D^b(S,A)$, \emph{un isomorphisme}", UL)
add(307, "Proposition 5.2, display, R^{2i}", "IR f_*(A) ≃ ⊕_i R^{2i} f_*(A)[-2i]: double-struck first R, plain R in R^{2i}",
    r"\R^{2i}f_*(A)", "font", "high", r"\R^{2i}f_*", r"\mathrm{R}^{2i}f_*",
    "The first R of the display is the hand-drawn double-struck R (\\R stands). " + RPLAIN)
add(307, "Proposition 5.2, end of the display", "no full stop after [-2i]", r"[-2i].",
    "punctuation", "high", r"[-2i].", r"[-2i]", "The TeX adds a full stop at the end of the display.")
add(307, "proof of 5.2, 'Le morphisme k étant composé d'un nombre fini de morphismes du type'", "k (clearly typed)", r"Le morphisme $h$",
    "misprint_in_print", "high", r"Le morphisme $h$", r"Le morphisme $k$",
    "The morphism is h = f o g of (5.1), a composite of projective bundles; the TeX silently corrects the printed k.",
    corrected=r"Le morphisme $h$")
add(307, "display (Q), '(F O_T-Module localement libre)'", "O_T-Module (plain typed O)", r"\text{-module localement libre}",
    "word", "high", r"\text{-module localement libre}", r"\text{-Module localement libre}", MOD)
add(307, "display (Q), after the parenthesis", "no comma", r"localement libre}),",
    "punctuation", "high", r"),<NL>\tag{Q}", r")<NL>\tag{Q}", "The TeX adds a comma at the end of the display.")
add(307, "display IR h_*(A) ≃ ⊕_j R^j h_*(A)[-j] .", "plain R in R^j", r"\R^jh_*(A)",
    "font", "high", r"\R^jh_*", r"\mathrm{R}^jh_*", "The first R (double-struck) stands. " + RPLAIN)
add(307, "display IR g_*(A) ≃ ⊕_j R^j g_*(A)[-j] .", "plain R in R^j", r"\R^jg_*(A)",
    "font", "high", r"\R^jg_*", r"\mathrm{R}^jg_*", "The first R (double-struck) stands. " + RPLAIN)
add(307, "display IR f_*(g_*A) ≃ ⊕_j R^j f_*(g_*A)[-j] .", "plain R in R^j", r"\R^j f_*(g_*A)",
    "font", "high", r"\R^j f_*", r"\mathrm{R}^j f_*", "The first R (double-struck) stands. " + RPLAIN)
add(307, "display (5.2.1), R^{2i+1} f_*(A) = 0 (i ∈ IN) .", "plain R", r"\R^{2i+1}f_*(A)",
    "font", "high", r"\R^{2i+1}f_*", r"\mathrm{R}^{2i+1}f_*", RPLAIN)

# ---------------- page 308
add(308, "Corollaire 5.3, statement before the display", "'Pour tout morphisme de schémas' and 'la suite spectrale de Leray' underlined; u : S → T , not",
    "no underline", "underline", "high",
    r"Pour tout morphisme de schémas $u:S\to T$, la suite spectrale de Leray",
    r"\emph{Pour tout morphisme de schémas} $u:S\to T$, \emph{la suite spectrale de Leray}", UL)
add(308, "Corollaire 5.3, display E_2^{pq} = R^p u_* R^q f_*(A) ⇒ R^{p+q}(u o f)_*(A)", "three plain typed R",
    r"\R^p u_*\,\R^q f_*(A)\Rightarrow \R^{p+q}", "font", "high",
    r"\R^p u_*\,\R^q f_*(A)\Rightarrow \R^{p+q}", r"\mathrm{R}^p u_*\,\mathrm{R}^q f_*(A)\Rightarrow \mathrm{R}^{p+q}", RPLAIN)
add(308, "Corollaire 5.3, 'est dégénérée.'", "'est dégénérée' underlined", "no underline",
    "underline", "high", r"est dégénérée.", r"\emph{est dégénérée}.", UL)
add(308, "proof of 5.3, 'Preuve : cf. [6] 1.2.'", "cf.", "Cf.",
    "word", "high", r"Cf. [6]", r"cf. [6]", "Capital against small letter.")
add(308, "display α : A•(S)[T_{ij_i}] → A•(X)", "A with a raised dot (twice)", r"A^*(S) ... A^*(X)",
    "symbol", "high", r"\alpha:A^*(S)[T_{ij_i}]_{1\le i\le m,\,1\le j_i\le p_m}\to A^*(X)",
    r"\alpha:A^{\bullet}(S)[T_{ij_i}]_{1\le i\le m,\,1\le j_i\le p_m}\to A^{\bullet}(X)", DOT)
add(308, "display α, index range '1 ≤ j_i ≤ p_m'", "p_m", r"1\le j_i\le p_m",
    "misprint_in_print", "medium", None, None,
    "Wrong index: E_i has rank p_i, so T_{ij_i} (sent to c_{j_i}(E_i)) runs over 1 ≤ j_i ≤ p_i, as the p_i elements (U_{p_1+...+p_{i-1}+s})_{1≤s≤p_i} of Lemme 5.4.1 b), whose V = R[T_{ij_i}] has the same printed p_m (p. 309). The TeX keeps the printed reading.",
    corrected=r"1\le j_i\le p_i", fix_null=True)
add(308, "'en envoyant A•(S) dans A•(X) par l'image réciproque f*'", "A with a raised dot (twice)", r"$A^*(S)$ dans $A^*(X)$",
    "symbol", "high", r"en envoyant $A^*(S)$ dans $A^*(X)$", r"en envoyant $A^{\bullet}(S)$ dans $A^{\bullet}(X)$", DOT)
add(308, "'f* et pour tout couple (i,j) comme ci-dessus l'élément T_{ij_i}'", "no commas", r"et, pour tout couple $(i,j)$, comme ci-dessus, l'élément",
    "punctuation", "high", r"et, pour tout couple $(i,j)$, comme ci-dessus, l'élément", r"et pour tout couple $(i,j)$ comme ci-dessus l'élément",
    "The TeX adds three commas.")
add(308, "'sur la j_i^{ème} classe de Chern'", "j_i with a raised 'ème'", r"$j_i$-ème",
    "word", "high", r"$j_i$-ème classe", r"$j_i^{\text{ème}}$ classe", "As the logged i^{ème} of p. 290.")
add(308, "'Pour tout entier p , on a d'après (3.4 (iii))'", "no commas", r"on a, d'après (3.4 (iii)),",
    "punctuation", "high", r"on a, d'après (3.4 (iii)),", r"on a d'après (3.4 (iii))", "The TeX adds two commas.")
add(308, "display c_p(E) - Σ T_{1,i_1}...T_{m,i_m}, summation index", "i_1+...i_m=p (no + before i_m; the display above has i_1+i_2+...+i_m=p)",
    r"\sum_{i_1+\cdots+i_m=p}", "extra", "high", r"\sum_{i_1+\cdots+i_m=p}", r"\sum_{i_1+\cdots i_m=p}",
    "The TeX adds a +, as the logged omitted \\subset after the dots on pp. 292-293.")
add(308, "display φ_X : (A•(S)[T_{ij_i}]_{(i,j_i)})/J_X → A•(X).", "A with a raised dot (twice)", r"A^*(S) ... A^*(X)",
    "symbol", "high", r"\bigl(A^*(S)[T_{ij_i}]_{(i,j_i)}\bigr)/J_X\to A^*(X).",
    r"\bigl(A^{\bullet}(S)[T_{ij_i}]_{(i,j_i)}\bigr)/J_X\to A^{\bullet}(X).", DOT)
add(308, "Proposition 5.4, first sentence", "'Le morphisme d'anneaux' and 'ci-dessus est un isomorphisme' underlined; φ_X and the full stop, not",
    "no underline", "underline", "high",
    r"Le morphisme d'anneaux $\varphi_X$ ci-dessus est un isomorphisme.",
    r"\emph{Le morphisme d'anneaux} $\varphi_X$ \emph{ci-dessus est un isomorphisme}.", UL)
add(308, "Proposition 5.4, 'Le A•(S)-module A•(X) est libre de rang'", "'module' and 'est libre de rang' underlined, 'Le' not; A with raised dots",
    r"Le $A^*(S)$-module $A^*(X)$ est libre de rang", "underline", "high",
    r"Le $A^*(S)$-module $A^*(X)$ est libre de rang",
    r"Le $A^{\bullet}(S)$-\emph{module} $A^{\bullet}(X)$ \emph{est libre de rang}",
    "One edit: it also gives the two raised dots (symbol). " + DOT)
add(308, "Proposition 5.4, display of the rank", "(r!)/(p_1!p_2!...p_m!). on one line", r"\frac{r!}{p_1!p_2!\cdots p_m!}.",
    "formula", "high", r"\frac{r!}{p_1!p_2!\cdots p_m!}.", r"(r!)/(p_1!p_2!\cdots p_m!).",
    "The print writes the quotient with a slash and parentheses.")

# ---------------- page 309
add(309, "Lemme 5.4.1 a), 'Soit R'", "'Soit' underlined", "no underline",
    "underline", "high", r"a) Soit $R$", r"a) \emph{Soit} $R$", "The TeX has no underline markup in this lemma. " + UL)
add(309, "Lemme 5.4.1 a), 'un anneau commutatif'", "underlined", "no underline",
    "underline", "high", r"un anneau commutatif", r"\emph{un anneau commutatif}", UL)
add(309, "Lemme 5.4.1 a), 'Soit R un anneau commutatif (a_i)_{1≤i≤r} r éléments de R .'",
    "no words between 'commutatif' and (a_i)", r"un anneau commutatif, et soient $(a_i)_{1\le i\le r}$",
    "misprint_in_print", "high", r", et soient", r"",
    "Words left out by the typist (the sentence lacks its second verb); the TeX silently supplies ', et soient'.",
    corrected=r"\emph{un anneau commutatif}, et soient $(a_i)_{1\le i\le r}$")
add(309, "Lemme 5.4.1 a), 'éléments de R'", "'éléments de' underlined", "no underline",
    "underline", "high", r"$r$ éléments de $R$.", r"$r$ \emph{éléments de} $R$.", UL)
add(309, "Lemme 5.4.1 a), 'Désignant par σ_i la'", "'Désignant par' and 'la' underlined", "no underline",
    "underline", "high", r"Désignant par $\sigma_i$ la", r"\emph{Désignant par} $\sigma_i$ \emph{la}", UL)
add(309, "Lemme 5.4.1 a), 'i^{ème} fonction symétrique élémentaire des éléments'", "i with a raised 'ème'; 'fonction symétrique élémentaire des éléments' underlined",
    r"$i$-ème fonction symétrique élémentaire des éléments", "word", "high",
    r"$i$-ème fonction symétrique élémentaire des éléments",
    r"$i^{\text{ème}}$ \emph{fonction symétrique élémentaire des éléments}",
    "As the logged i^{ème} of p. 290. One edit: it also gives the underline.")
add(309, "Lemme 5.4.1 a), '(U_i)_{1≤i≤r} et par I'", "no comma; 'et par' underlined", r"$(U_i)_{1\le i\le r}$, et par",
    "punctuation", "high", r"$(U_i)_{1\le i\le r}$, et par", r"$(U_i)_{1\le i\le r}$ \emph{et par}",
    "The TeX adds a comma. One edit: it also gives the underline.")
add(309, "Lemme 5.4.1 a), 'l'idéal de l anneau de polynômes'", "the letter l (as the l of l'idéal), not the digit 1; the phrase underlined",
    r"l'idéal de 1 anneau de polynômes", "word", "high",
    r"l'idéal de 1 anneau de polynômes", r"\emph{l'idéal de l anneau de polynômes}",
    "The TeX has the digit 1 for the letter l. One edit: it also gives the underline.")
add(309, "Lemme 5.4.1 a), 'de l anneau'", "de l anneau (no apostrophe)", r"de 1 anneau (de l anneau after the previous item)",
    "misprint_in_print", "high", None, None,
    "Apostrophe left out by the typist. After the previous item (1 -> l) the TeX keeps the printed reading.",
    corrected=r"\emph{l'idéal de l'anneau de polynômes}", fix_null=True)
add(309, "Lemme 5.4.1 a), 'engendré par les éléments σ_i - a_i , la R-algèbre'", "'engendré par les éléments', 'la' and 'algèbre' underlined (not R-)",
    "no underline", "underline", "high",
    r"engendré par les éléments $\sigma_i-a_i$, la $R$-algèbre",
    r"\emph{engendré par les éléments} $\sigma_i-a_i$, \emph{la} $R$-\emph{algèbre}", UL)
add(309, "Lemme 5.4.1 a), 'est un R-module libre de rang r !'", "'est un' and 'module libre de rang' underlined (not R-)", "no underline",
    "underline", "high", r"est un $R$-module libre de rang", r"\emph{est un} $R$-\emph{module libre de rang}", UL)
add(309, "Lemme 5.4.1 a), end: 'r !'", "no full stop after r !", r"$r!$.",
    "punctuation", "high", r"$r!$.", r"$r!$", "The TeX adds a full stop.")
add(309, "Lemme 5.4.1 b), 'Soient'", "underlined", "no underline",
    "underline", "high", r"b) Soient $r", r"b) \emph{Soient} $r", UL)
add(309, "Lemme 5.4.1 b), 'des entiers >0 vérifiant l'égalité'", "'des entiers' and 'vérifiant l'égalité' underlined", "no underline",
    "underline", "high", r"des entiers $>0$ vérifiant l'égalité", r"\emph{des entiers} $>0$ \emph{vérifiant l'égalité}", UL)
add(309, "Lemme 5.4.1 b), 'Alors le morphisme d'anneaux de polynômes'", "underlined", "no underline",
    "underline", "high", r"Alors le morphisme d'anneaux de polynômes", r"\emph{Alors le morphisme d'anneaux de polynômes}", UL)
add(309, "Lemme 5.4.1 b), display V = R[T_{ij_i}] ...", "T_{ij_i} (no comma in the index)", r"T_{i,j_i}",
    "formula", "high", r"V=R[T_{i,j_i}]", r"V=R[T_{ij_i}]", "The TeX adds a comma between the indices.")
add(309, "Lemme 5.4.1 b), display V, index range '1 ≤ j_i ≤ p_m'", "p_m", r"1\le j_i\le p_m",
    "misprint_in_print", "medium", None, None,
    "As on p. 308: T_{i,j_i} goes to the j_i-th elementary symmetric function of p_i elements, so j_i ≤ p_i. The TeX keeps the printed reading.",
    corrected=r"1\le j_i\le p_i", fix_null=True)
add(309, "Lemme 5.4.1 b), end of display V → W", "comma after W", r"=W",
    "punctuation", "high", r"=W<NL>", r"=W,<NL>", "The TeX drops the comma at the end of the display.")
add(309, "Lemme 5.4.1 b), 'obtenu en envoyant T_{i,j_i} sur la'", "'obtenu en envoyant' and 'sur la' underlined", "no underline",
    "underline", "high", r"obtenu en envoyant $T_{i,j_i}$ sur la", r"\emph{obtenu en envoyant} $T_{i,j_i}$ \emph{sur la}", UL)
add(309, "Lemme 5.4.1 b), 'sur la j^{ème} fonctions'", "j with a raised 'ème', no index i", r"$j_i$-ème",
    "misprint_in_print", "medium", r"$j_i", r"$j",
    "The index i is left out (p. 308 and p. 310 print j_i^{ème} in the same phrase); the TeX silently supplies it. Disjoint from the next item, which gives the superscript form.",
    corrected=r"$j_i^{\text{ème}}$")
add(309, "Lemme 5.4.1 b), 'ème fonctions symétrique élémentaire des éléments'", "raised 'ème'; 'fonctions symétrique élémentaire des éléments' underlined",
    r"$j_i$-ème fonctions symétrique élémentaire des éléments", "word", "high",
    r"$-ème fonctions symétrique élémentaire des éléments",
    r"^{\text{ème}}$ \emph{fonctions symétrique élémentaire des éléments}",
    "The old starts at the $ that closes $j_i$ (disjoint from the previous item). As the logged i^{ème} of p. 290. One edit: it also gives the underline.")
add(309, "Lemme 5.4.1 b), 'fonctions symétrique'", "fonctions", "fonctions",
    "misprint_in_print", "high", None, None, "Typing error; the TeX keeps the printed reading.",
    corrected=r"\emph{fonction symétrique élémentaire des éléments}", fix_null=True)
add(309, "Lemme 5.4.1 b), after (U_{p_1+...+p_{i-1}+s})_{1≤s≤p_i}", "comma after the formula", "no comma",
    "punctuation", "high", r"s\le p_i}<NL>\]", r"s\le p_i},<NL>\]", "The TeX drops the comma (the print runs the formula into the text).")
add(309, "Lemme 5.4.1 b), 'est injectif et fait de W un V-module libre de rang'", "'est injectif et fait de', 'un', 'module libre de rang' underlined (not W, V-)",
    "no underline", "underline", "high",
    r"est injectif et fait de $W$ un $V$-module libre de rang",
    r"\emph{est injectif et fait de} $W$ \emph{un} $V$-\emph{module libre de rang}", UL)
add(309, "Lemme 5.4.1 b), end: 'p_1!... p_m !'", "no full stop", r"$p_1!\cdots p_m!$.",
    "punctuation", "high", r"$p_1!\cdots p_m!$.", r"$p_1!\cdots p_m!$", "The TeX adds a full stop.")
add(309, "Lemme 5.4.1, 'En particulier, le morphisme de R-algèbres'", "the whole line underlined, R- included", "no underline",
    "underline", "high", r"En particulier, le morphisme de $R$-algèbres", r"\emph{En particulier, le morphisme de $R$-algèbres}", UL)
add(309, "Lemme 5.4.1, last sentence, 'obtenu en envoyant T_i sur la'", "'obtenu en envoyant' and 'sur la' underlined", "no underline",
    "underline", "high", r"obtenu en envoyant $T_i$ sur la", r"\emph{obtenu en envoyant} $T_i$ \emph{sur la}", UL)
add(309, "Lemme 5.4.1, last sentence, 'i^{ème} fonction symétrique élémentaire des'", "raised 'ème'; 'fonction symétrique élémentaire des' underlined",
    r"$i$-ème fonction symétrique élémentaire des $U_j$", "word", "high",
    r"$i$-ème fonction symétrique élémentaire des $",
    r"$i^{\text{ème}}$ \emph{fonction symétrique élémentaire des} $",
    "As the logged i^{ème} of p. 290. One edit: it also gives the underline. The old ends at the $ that opens $U_j$ (disjoint from the next two items).")
add(309, "Lemme 5.4.1, last sentence, 'des U_i,'", "U_i", r"U_j",
    "misprint_in_print", "medium", r"U_j", r"U_i",
    "The print reuses the index i of T_i (the i-th elementary symmetric function of all the U's); the TeX silently writes U_j.",
    corrected=r"U_j")
add(309, "Lemme 5.4.1, last sentence, 'U_i, est injec-tif et fait du deuxième membre un module libre de rang r !'",
    "comma after U_i; 'est injectif ... de rang' underlined", r"$U_j$ est injectif et fait du deuxième membre un module libre de rang",
    "punctuation", "high",
    r"$ est injectif et fait du deuxième membre un module libre de rang",
    r"$, \emph{est injectif et fait du deuxième membre un module libre de rang}",
    "The TeX drops the comma. One edit: it also gives the underline. The old starts at the $ that closes $U_j$.")
add(309, "Lemme 5.4.1, 'sur le premier.'", "'sur le premier' underlined", "no underline",
    "underline", "high", r"sur le premier.", r"\emph{sur le premier}.", UL)

# ---------------- page 310
add(310, "top of the page: 'où X est le schéma D des drapeaux de E'",
    "p. 310 begins 'où X est le schéma D des drapeaux de E et posons'; p. 309 ends '... Plaçons-nous d'abord dans le cas'",
    "page_309.tex ends '... Plaçons-nous d'abord dans le cas où $X$ est le' (diplomatic s5.tex line 10483); the folio-310 marker (line 10484) stands before 'schéma $D$'",
    "marker", "high", None, None,
    "Page 310 really begins at 'où $X$ est le' (end of diplomatic s5.tex line 10483, current 10478, at the time of the check). Exact fix: python -I move_marker.py 5 310 'où $X$ est le' --before (single quotes keep the $ literal; simulated in memory on both layers: the nearest occurrence is 14 characters before the marker, which then splits the line after 'dans le cas'). Text not moved.",
    fix_null=True)
add(310, "'avec M_i un O_{Y_i}-Module localement libre de rang r-i+1'", "O_{Y_i}-Module (plain typed O)", r"$\mathcal O_{Y_i}$-module",
    "word", "high", r"$\mathcal O_{Y_i}$-module", r"$\mathcal O_{Y_i}$-Module", MOD)
add(310, "'on déduit de (2.2.6) que A•(D) est un A•(S)-module'", "A with a raised dot (twice)", r"$A^*(D)$ ... $A^*(S)$",
    "symbol", "high", r"(2.2.6) que $A^*(D)$ est un $A^*(S)$-module", r"(2.2.6) que $A^{\bullet}(D)$ est un $A^{\bullet}(S)$-module", DOT)
add(310, "'libre de rang r ! et que le morphisme φ_D'", "no comma", r"$r!$, et que",
    "punctuation", "high", r"$r!$, et que", r"$r!$ et que", "The TeX adds a comma.")
add(310, "'est également un A•(S)-Module libre de rang r!'", "A with a raised dot; capital M", r"$A^*(S)$-module",
    "word", "high", r"également un $A^*(S)$-module", r"également un $A^{\bullet}(S)$-Module",
    MOD + " One edit: it also gives the raised dot (symbol). " + DOT)
add(310, "'libre de rang r! d'où l'assertion dans le cas X = D.'", "no semicolon", r"$r!$; d'où",
    "punctuation", "high", r"$r!$; d'où", r"$r!$ d'où", "The TeX adds a semicolon.")
add(310, "'d'où l'assertion dans le cas X = D. Dans le cas général'", "one paragraph: 'Dans le cas général' starts a line at the margin, without the paragraph indent of the typescript",
    "blank line (new paragraph)", "other", "low", r"$X=D$.<NL><NL>Dans le cas général", r"$X=D$. Dans le cas général",
    "Layout only; drop if paragraph breaks are not checked.")
add(310, "diagram, top row A•(X) → A•(D)", "A with a raised dot (twice)", r"A^*(X) ... A^*(D)",
    "symbol", "high", r'A^*(X) \arrow[r,"g^*"] & A^*(D)', r'A^{\bullet}(X) \arrow[r,"g^*"] & A^{\bullet}(D)', DOT)
add(310, "diagram, bottom left C = A•(S)[T_{i,j_i}]/J_X", "A with a raised dot", r"C=A^*(S)",
    "symbol", "high", r"C=A^*(S)", r"C=A^{\bullet}(S)", DOT)
add(310, "diagram, bottom right A•(S)[U_k]/J_D", "A with a raised dot", r"A^*(S)[U_k]/J_D",
    "symbol", "high", r"A^*(S)[U_k]/J_D", r"A^{\bullet}(S)[U_k]/J_D", DOT)
add(310, "diagram, bottom arrow γ", "γ above the arrow", r'\arrow[r,"\gamma"' + "'] (label below the arrow)",
    "other", "medium", r'\arrow[r,"\gamma"' + "']", r'\arrow[r,"\gamma"]',
    "Label position as in the print (as the logged label fixes of pp. 39, 57, 71, 265, 277-278); drop if label placement is left as layout.")
add(310, "'à partir du morphisme de A•(S)-algèbres'", "A with a raised dot", r"$A^*(S)$-algèbres",
    "symbol", "high", r"morphisme de $A^*(S)$-algèbres", r"morphisme de $A^{\bullet}(S)$-algèbres", DOT)
add(310, "display A•(S)[T_{i,j_i}] → A•[U_k]", "A•[U_k] (no (S))", r"A^\bullet[U_k]",
    "misprint_in_print", "medium", None, None,
    "The target is the A•(S)-algebra A•(S)[U_k] of the diagram; the (S) is left out. The TeX keeps the printed reading.",
    corrected=r"A^\bullet(S)[U_k]", fix_null=True)
add(310, "'défini en envoyant T_{i,j_i} sur la j_i^{ème} fonction'", "j_i with a raised 'ème'", r"$j_i$-ème",
    "word", "high", r"$j_i$-ème", r"$j_i^{\text{ème}}$", "As the logged i^{ème} of p. 290.")
add(310, "'il résulte de 5.4.1. b)'", "5.4.1. with a full stop", r"5.4.1 b)",
    "punctuation", "high", r"résulte de 5.4.1", r"résulte de 5.4.1.", "The TeX drops the full stop after the number.")
add(310, "'b) que A•(D)'", "A with a raised dot", r"$A^*(D)$",
    "symbol", "high", r"b) que $A^*(D)$", r"b) que $A^{\bullet}(D)$", DOT)
add(310, "'que A•(D) un C-module libre de rang'", "no 'est' (the line ends with A•(D), the next begins 'un C-module')", r"$A^*(D)$ est un $C$-module",
    "misprint_in_print", "high", r" est un $C$", r" un $C$",
    "Word left out by the typist; the TeX silently supplies 'est'. Disjoint from the previous item.",
    corrected=r"que $A^{\bullet}(D)$ est un $C$-module")
add(310, "'montre que A•(D) est aussi un A•(X)-module'", "A with a raised dot (twice)", r"$A^*(D)$ ... $A^*(X)$",
    "symbol", "high", r"montre que $A^*(D)$ est aussi un $A^*(X)$-module", r"montre que $A^{\bullet}(D)$ est aussi un $A^{\bullet}(X)$-module", DOT)
add(310, "'on convient de poser pour tout schéma Y'", "no comma", r"de poser, pour",
    "punctuation", "high", r"de poser, pour", r"de poser pour", "The TeX adds a comma.")
add(310, "'et tout A_Y-Module M'", "A_Y-Module", r"$A_Y$-module",
    "word", "high", r"$A_Y$-module", r"$A_Y$-Module", MOD)
add(310, "'et tout A_Y-Module M' before the display Q(Y,M)", "no comma", r"$M$,",
    "punctuation", "high", r"$M$,<NL>\[", r"$M$<NL>\[", "The TeX adds a comma.")

# ---------------- checks
ok = True
pages = {}
for d in F:
    pages.setdefault(d["page"], []).append(d)
for p, items in sorted(pages.items()):
    orig = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    t = orig
    marker_line = [l for l in orig.split("\n") if "scan idx" in l][0]
    for d in items:
        fx = d["fix"]
        if fx is None:
            continue
        old, new = fx["old"], fx["new"]
        c0 = orig.count(old)
        c1 = t.count(old)
        bad = (c0 != 1) or (c1 != 1) or ("scan idx" in old) or (old == new)
        if bad:
            ok = False
            print("PROBLEM", p, repr(old), "orig count", c0, "seq count", c1)
        t = t.replace(old, new, 1)
    assert marker_line in t
    (RUN / "crops_306_310" / f"after_{p}.tex").write_text(t, encoding="utf-8", newline="\n")
print("all olds unique (original and sequential):", ok)
from collections import Counter
cnt = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted(pages):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("total", len(F))
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print("written", OUT)
