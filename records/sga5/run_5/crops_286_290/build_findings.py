import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
B = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/b286_290/page_%d.tex"
OUT = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/findings_286_290.json"
NL = "\u23ce"  # placeholder for a line break in the raw strings below


def s(x):
    return None if x is None else x.replace(NL, "\n")


def fx(old, new):
    return {"old": s(old), "new": s(new)}


SMALLP = ("The subscript is a small p: bowl about 15 rows and stem about 6-7 rows below it at 300 dpi, as the p of "
          "'par'; the typed capital P has a bowl of 12-13 rows and a stem of 9 (as in 'O_P -Module', p. 286, "
          "and mu_P in Cor. 2.2.6, p. 289, which are capitals). P is the projective bundle (p its projection), so "
          "the small p is a typing error; the TeX silently corrects it. One of the small-p items of pp. 286-288: "
          "apply all or none.")
RPLAIN = ("Plain typewriter R (one stem); \\R is \\mathbb{R} in this file. On these pages only the total derived "
          "functors Rp_* and RGamma have the double-struck R.")

F = []


def add(page, where, scan, tex, kind, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 286
add(286, "before display (2.1.2): 'on obtient enfin un morphisme de'",
    "the line ends 'un morphisme de', then the display (2.1.2)",
    "on obtient enfin un morphisme", "missing", "high",
    fx(r"on obtient enfin un morphisme⏎", r"on obtient enfin un morphisme de⏎"),
    "The TeX drops the printed 'de' before the display.")
for where, old in [
    ("display after 'on définit un morphisme de résolutions'",
     r"C^*(X,A_X)\otimes C^*(X,A_X)\longrightarrow C^*(X,A_X\otimes A_X)."),
    ("display after 'En le composant avec le morphisme'",
     r"C^*(X,A_X\otimes A_X)\longrightarrow C^*(X,A_X)⏎"),
    ("display (2.1.2)",
     r"C^*(X,A_X)\otimes C^*(X,A_X)\longrightarrow C^*(X,A_X).⏎\tag{2.1.2}"),
    ("display after 'A_Y-Modules'",
     r"f_*C^*(X,A_X)\otimes f_*C^*(X,A_X)\longrightarrow f_*C^*(X,A_X),"),
]:
    add(286, where, "C• (raised dot) in every Godement complex", "C^* (star)", "symbol", "high",
        fx(old, old.replace("C^*", r"C^{\bullet}")),
        "The print's raised dot, not the star of f_*; written C^{\\bullet} as the logged fix of p. 285 "
        "('Notons pour cela C•(X,A_X)').")
add(286, "'un morphisme de complexes de A_Y-Modules'", "Modules with a capital M", "$A_Y$-modules", "word", "high",
    fx(r"$A_Y$-modules", r"$A_Y$-Modules"))
add(286, "2.2, 'E un O_S-Module localement libre de rang r+1'", "Module with a capital M",
    r"$\mathcal O_S$-module", "word", "high",
    fx(r"$\mathcal O_S$-module", r"$\mathcal O_S$-Module"),
    "The O is a plain typed O without underline (see the message).")
add(286, "2.2, 'Le O_P-Module canonique'", "Module with a capital M", r"$\mathcal O_P$-module", "word", "high",
    fx(r"$\mathcal O_P$-module", r"$\mathcal O_P$-Module"))
add(286, "2.2, 'Le O_P-Module canonique O_p(1)'", "O_p(1): small p subscript", r"$\mathcal O_P(1)$",
    "misprint_in_print", "medium",
    fx(r"$\mathcal O_P(1)$", r"$\mathcal O_p(1)$"), SMALLP, corrected=r"$\mathcal O_P(1)$")
add(286, "2.2, 'O_p(1) définit comme on sait, grâce à'", "no comma after 'définit'",
    "définit, comme on sait,", "punctuation", "high",
    fx(r"définit, comme on sait", r"définit comme on sait"), "The TeX adds a comma.")
add(286, "display H^2(P,μ) → H^0(S,R^2p_*(μ))", "R^2: plain typewriter R", r"\R^2p_*(\mu)", "font", "high",
    fx(r"\R^2p_*(\mu)", r"\mathrm{R}^2p_*(\mu)"), RPLAIN)
add(286, "Leray spectral sequence H^i(S,R^jp_*(μ)) ⇒ H^{i+j}(P,μ)", "R^j: plain typewriter R", r"\R^jp_*(\mu)",
    "font", "high", fx(r"\R^jp_*(\mu)", r"\mathrm{R}^jp_*(\mu)"), RPLAIN)
add(286, "'une flèche A_p → μ_p [2] de D(P)'", "A_p, μ_p: small p subscripts", r"$A_P\to\mu_P[2]$",
    "misprint_in_print", "medium", fx(r"$A_P\to\mu_P[2]$", r"$A_p\to\mu_p[2]$"), SMALLP,
    corrected=r"$A_P\to\mu_P[2]$")
add(286, "'par transposition μ_p^{⊗-1}[-2] → A_p'", "μ_p, A_p: small p subscripts",
    r"$\mu_P^{\otimes -1}[-2]\to A_P$", "misprint_in_print", "medium",
    fx(r"$\mu_P^{\otimes -1}[-2]\to A_P$", r"$\mu_p^{\otimes -1}[-2]\to A_p$"), SMALLP,
    corrected=r"$\mu_P^{\otimes -1}[-2]\to A_P$")
add(286, "display c : μ_S^{⊗-1}[2] → Rp_*(A_p)", "[2]: no minus sign (the line above prints [-2])",
    r"[-2]\longrightarrow", "misprint_in_print", "high",
    fx(r"[-2]\longrightarrow \R p_*", r"[2]\longrightarrow \R p_*"),
    "The arrow c is the adjoint of μ_P^{⊗-1}[-2] → A_P and gives η in degree 2, so [-2] is meant; the TeX "
    "silently corrects. The bracket follows the 2 directly, no room for a lost minus.",
    corrected=r"[-2]\longrightarrow \R p_*")
add(286, "display c : ... → Rp_*(A_p)", "(A_p): small p subscript", "(A_P),", "misprint_in_print", "medium",
    fx(r"(A_P),", r"(A_p),"), SMALLP, corrected=r"(A_P),")

# ---------------------------------------------------------------- page 287
add(287, "first line, 'Par produit tensoriel la flèche c définit'", "no comma after 'tensoriel'",
    "tensoriel, la", "punctuation", "high", fx(r"tensoriel, la", r"tensoriel la"), "The TeX adds a comma.")
add(287, "first line, 'grâce à (2.2.1), des flèches'", "(2.2.1)", "(2.2.1)", "misprint_in_print", "medium", None,
    "Wrong reference: the c_i are products of c by the cup-product morphism (2.1.1) (p. 285); 2.2.1 is the "
    "theorem stated below (γ is an isomorphism). The TeX keeps the printed reading.", corrected="(2.1.1)")
add(287, "display c_i : μ_S^{⊗-i}[-2i] → Rp_*(A_p)", "(A_p): small p subscript", "(A_P),", "misprint_in_print",
    "medium", fx(r"(A_P),", r"(A_p),"), SMALLP, corrected=r"(A_P),")
add(287, "'la flèche d'adjonction A_S → Rp_*(A_p).'", "(A_p): small p subscript", "(A_P).", "misprint_in_print",
    "medium", fx(r"(A_P).", r"(A_p)."), SMALLP, corrected=r"(A_P).")
add(287, "display γ = ⊕ c_i : ... → Rp_*(A_p)", "(A_p): small p subscript", "(A_P)", "misprint_in_print",
    "medium", fx(r"(A_P)⏎\]⏎de", r"(A_p)⏎\]⏎de"), SMALLP, corrected=r"(A_P)")
add(287, "Théorème 2.2.1", "'La flèche' and 'est un isomorphisme' underlined, γ not", "no underline markup",
    "underline", "high",
    fx(r"La flèche $\gamma$ est un isomorphisme.", r"\emph{La flèche} $\gamma$ \emph{est un isomorphisme}."),
    "Exposé VII statements are underlined word group by word group; \\emph as in the logged statements of "
    "pp. 283-285.")
add(287, "'(2.2.1) équivaut à son corollaire suivant :'", "a colon at the end", "suivant.", "punctuation", "high",
    fx(r"son corollaire suivant.", r"son corollaire suivant :"), "The TeX has a full stop for the print's colon.")
add(287, "Proposition 2.2.2, 'Sous les hypothèses précédentes, on a :'",
    "'Sous les hypothèses précédentes, on a' underlined, the colon not", "no underline markup", "underline",
    "high", fx(r"Sous les hypothèses précédentes, on a:", r"\emph{Sous les hypothèses précédentes, on a} :"))
add(287, "Proposition 2.2.2 a), R^{2i+1}p_*(A_p) = 0", "plain typewriter R", r"\R^{2i+1}p_*", "font", "high",
    fx(r"\R^{2i+1}p_*", r"\mathrm{R}^{2i+1}p_*"), RPLAIN)
add(287, "Proposition 2.2.2 a), R^{2i+1}p_*(A_p) = 0", "(A_p): small p subscript", "(A_P)=0",
    "misprint_in_print", "medium", fx(r"(A_P)=0", r"(A_p)=0"), SMALLP, corrected=r"(A_P)=0")
add(287, "Proposition 2.2.2 a), 'pour tout i ∈ N'", "'pour tout' underlined", r"\text{pour tout }i",
    "underline", "high", fx(r"\text{pour tout }i", r"\text{\emph{pour tout} }i"))
add(287, "Proposition 2.2.2 b), 'Lorsqu'on munit'", "underlined", "no underline markup", "underline", "high",
    fx(r"\item Lorsqu'on munit", r"\item \emph{Lorsqu'on munit}"))
add(287, "Proposition 2.2.2 b), ⊕ R^{2i}p_*(μ_p^{⊗i}) in the text", "plain typewriter R",
    r"$\bigoplus_i \R^{2i}p_*", "font", "high",
    fx(r"$\bigoplus_i \R^{2i}p_*", r"$\bigoplus_i \mathrm{R}^{2i}p_*"), RPLAIN)
add(287, "Proposition 2.2.2 b), ⊕ R^{2i}p_*(μ_p^{⊗i}) in the text", "μ_p: small p subscript",
    r"(\mu_P^{\otimes i})$", "misprint_in_print", "medium",
    fx(r"(\mu_P^{\otimes i})$", r"(\mu_p^{\otimes i})$"), SMALLP, corrected=r"(\mu_P^{\otimes i})$")
add(287, "Proposition 2.2.2 b), 'de sa structure de A_S-Algèbre déduite du cup-produit, le morphisme de "
         "A_S-Algèbres'",
    "underlined: 'de sa structure de' | 'Algèbre déduite du cup-produit, le morphisme de' | 'Algèbres' "
    "(A_S- not); Algèbre(s) with a capital A", "no underline markup; algèbre(s)", "underline", "high",
    fx(r"de sa structure de $A_S$-algèbre déduite du cup-produit, le morphisme de $A_S$-algèbres",
       r"\emph{de sa structure de} $A_S$-\emph{Algèbre déduite du cup-produit, le morphisme de} "
       r"$A_S$-\emph{Algèbres}"),
    "One edit: it also gives the print's capital A twice (word).")
add(287, "display A_S[T] → ⊕ R^2p_*(μ_p^{⊗i})", "plain typewriter R", r"\R^{2i}", "font", "high",
    fx(r"A_S[T]\longrightarrow \bigoplus_i \R", r"A_S[T]\longrightarrow \bigoplus_i \mathrm{R}"), RPLAIN)
add(287, "display A_S[T] → ⊕ R^2p_*(μ_p^{⊗i})", "R^2: the exponent is 2 only (no i)", r"\R^{2i}",
    "misprint_in_print", "high",
    fx(r"^{2i}p_*(\mu_P^{\otimes i})⏎", r"^{2}p_*(\mu_P^{\otimes i})⏎"),
    "The exponent is 2i (as in the text above and in θ below); the TeX silently corrects. Changes only the "
    "exponent; apply after the font fix above and before the μ_p item below (both olds are unique in the file).",
    corrected=r"^{2i}p_*(\mu_P^{\otimes i})")
add(287, "display A_S[T] → ⊕ R^2p_*(μ_p^{⊗i})", "μ_p: small p subscript", r"(\mu_P^{\otimes i})",
    "misprint_in_print", "medium",
    fx(r"(\mu_P^{\otimes i})⏎", r"(\mu_p^{\otimes i})⏎"),
    SMALLP + " Apply after the R^2 item above and before the full-stop fix of the θ display.",
    corrected=r"(\mu_P^{\otimes i})")
add(287, "Proposition 2.2.2 b), 'défini par η a pour noyau l'Idéal (T^{r+1}) et définit donc un isomorphisme de "
         "A_S-Algèbres'",
    "underlined: 'défini par' | 'a pour noyau l'Idéal' | 'et définit donc un isomorphisme de' | 'Algèbres'; "
    "Idéal and Algèbres with capitals", "no underline markup; idéal, algèbres", "underline", "high",
    fx(r"défini par $\eta$ a pour noyau l'idéal $(T^{r+1})$ et définit donc un isomorphisme de $A_S$-algèbres",
       r"\emph{défini par} $\eta$ \emph{a pour noyau l'Idéal} $(T^{r+1})$ \emph{et définit donc un "
       r"isomorphisme de} $A_S$-\emph{Algèbres}"),
    "One edit: it also gives the print's capitals I and A (word).")
add(287, "display θ : A_S[T]/(T^{r+1}) ≃ ⊕ R^{2i} p_*(μ_p^{⊗i})", "plain typewriter R", r"\R^{2i}", "font",
    "high", fx(r"\xrightarrow{\sim}\bigoplus_i \R", r"\xrightarrow{\sim}\bigoplus_i \mathrm{R}"), RPLAIN)
add(287, "display θ : A_S[T]/(T^{r+1}) ≃ ⊕ R^{2i} p_*(μ_p^{⊗i})", "no punctuation at the end of the display",
    r"(\mu_P^{\otimes i}).", "punctuation", "high",
    fx(r"^{\otimes i}).⏎", r"^{\otimes i})⏎"), "The TeX adds a full stop.")
add(287, "display θ : A_S[T]/(T^{r+1}) ≃ ⊕ R^{2i} p_*(μ_p^{⊗i})", "μ_p: small p subscript",
    r"(\mu_P^{\otimes i})", "misprint_in_print", "medium",
    fx(r"\sim}\bigoplus_i \mathrm{R}^{2i}p_*(\mu_P", r"\sim}\bigoplus_i \mathrm{R}^{2i}p_*(\mu_p"),
    SMALLP + " Its old is taken from the text after the font fix of the same display (listed above).",
    corrected=r"\sim}\bigoplus_i \mathrm{R}^{2i}p_*(\mu_P")
add(287, "Proposition 2.2.2 c), 'Le morphisme'", "underlined", "no underline markup", "underline", "high",
    fx(r"\item Le morphisme", r"\item \emph{Le morphisme}"))
add(287, "Proposition 2.2.2 c), display A_S → R^{2r} p_*(μ^{⊗r})", "plain typewriter R", r"\R^{2r}", "font",
    "high", fx(r"A_S\longrightarrow \R^{2r}", r"A_S\longrightarrow \mathrm{R}^{2r}"), RPLAIN)
add(287, "Proposition 2.2.2 c), 'obtenu en composant θ ... l'inverse du morphisme Trace (SGA 4 XVIII)'",
    "underlined: 'obtenu en composant' | 'et la restriction à' | 'de la multiplication par' | 'de' | "
    "'dans lui-même est l'inverse du morphisme Trace' (θ, A_S, T^r, A_S[T]/(T^{r+1}) and the reference not); "
    "Trace with a capital T", "no underline markup; trace", "underline", "high",
    fx(r"obtenu en composant $\theta$ et la restriction à $A_S$ de la multiplication par $T^r$ de "
       r"$A_S[T]/(T^{r+1})$ dans lui-même est l'inverse du morphisme trace",
       r"\emph{obtenu en composant} $\theta$ \emph{et la restriction à} $A_S$ \emph{de la multiplication par} "
       r"$T^r$ \emph{de} $A_S[T]/(T^{r+1})$ \emph{dans lui-même est l'inverse du morphisme Trace}"),
    "One edit: it also gives the print's capital T (word).")
add(287, "Proposition 2.2.2 c), display R^{2r} p_*(μ^{⊗r}) → A_S ;", "plain typewriter R", r"\R^{2r}", "font",
    "high", fx(r"\R^{2r}p_*(\mu^{\otimes r})\longrightarrow A_S;",
                r"\mathrm{R}^{2r}p_*(\mu^{\otimes r})\longrightarrow A_S;"), RPLAIN)
add(287, "Proposition 2.2.2 c), 'en d'autres termes, on a'", "underlined", "no underline markup", "underline",
    "high", fx(r"en d'autres termes, on a", r"\emph{en d'autres termes, on a}"))

# ---------------------------------------------------------------- page 288
add(288, "proof, '(SGA 4 XVIII) permettent de se ramener'", "no comma after the reference",
    "(SGA 4 XVIII), permettent", "punctuation", "high",
    fx(r"(SGA 4 XVIII), permettent", r"(SGA 4 XVIII) permettent"), "The TeX adds a comma.")
add(288, "Lemme 2.2.3, statement", "underlined: 'Soient' | 'un corps séparablement clos et' | 'la projection "
    "canonique. Alors' (k, p : P^r_k → k and the colon not)", "no underline markup", "underline", "high",
    fx(r"Soient $k$ un corps séparablement clos et $p:\mathbb P_k^r\to k$ la projection canonique. Alors:",
       r"\emph{Soient} $k$ \emph{un corps séparablement clos et} $p:\mathbb P_k^r\to k$ \emph{la projection "
       r"canonique. Alors} :"))
add(288, "Lemme 2.2.3 a), R^{2i+1}p_*(A_p) = 0", "plain typewriter R", r"\R^{2i+1}", "font", "high",
    fx(r"\R^{2i+", r"\mathrm{R}^{2i+"), RPLAIN)
add(288, "Lemme 2.2.3 a), R^{2i+1}p_*(A_p) = 0", "(A_p): small p subscript", "(A_P)", "misprint_in_print",
    "medium", fx(r"1}p_*(A_P)", r"1}p_*(A_p)"), SMALLP, corrected=r"1}p_*(A_P)")
add(288, "Lemme 2.2.3 a), 'pour tout i .'", "'pour tout' underlined", r"\text{pour tout }i.", "underline",
    "high", fx(r"\text{pour tout }i.", r"\text{\emph{pour tout} }i."))
add(288, "Lemme 2.2.3 b), R^{2i}p_*(A_p) ≃ A_k", "plain typewriter R", r"\R^{2i}", "font", "high",
    fx(r"\item⏎\[⏎\R^{2i}", r"\item⏎\[⏎\mathrm{R}^{2i}"), RPLAIN)
add(288, "Lemme 2.2.3 b), R^{2i}p_*(A_p) ≃ A_k", "(A_p): small p subscript", "(A_P)", "misprint_in_print",
    "medium", fx(r"p_*(A_P)\simeq", r"p_*(A_p)\simeq"), SMALLP, corrected=r"p_*(A_P)\simeq")
add(288, "Lemme 2.2.3 b), 'pour i ∈ [0,r]'", "'pour' underlined", r"\text{pour }i", "underline", "high",
    fx(r"\text{pour }i\in", r"\text{\emph{pour} }i\in"))
add(288, "Lemme 2.2.3 b), second clause", "', ≃ 0 si i > r .' ('si' underlined): no repeated left side, ≃ not =",
    r"\R^{2i}p_*(A_P)=0\quad\text{si }i>r.", "formula", "high",
    fx(r"\R^{2i}p_*(A_P)=0\quad\text{si }i>r.", r"\simeq 0\quad\text{\emph{si} }i>r."),
    "The TeX repeats R^{2i}p_*(A_P) and writes = for the print's ≃; the edit also underlines 'si'.")
add(288, "'Supposons donc qu'il est vrai pour r-1'", "'est' (typed smaller, as a correction)", "qu'il soit vrai",
    "word", "high", fx(r"qu'il soit vrai", r"qu'il est vrai"),
    "The print reads 'est' (a typed insertion); the TeX writes the subjunctive.")
add(288, "exact sequence ... → H^i_!(E^r_k) → ... → H^{i+1}_!(E^r_k) → ...", "no full stop at the end",
    r"\longrightarrow\cdots.", "punctuation", "high",
    fx(r"H_!^{i+1}(\mathbb E_k^r)\longrightarrow\cdots.", r"H_!^{i+1}(\mathbb E_k^r)\longrightarrow\cdots"),
    "The TeX adds a full stop.")
add(288, "'(1.1) montre que si i ≠ (2r,2r-1)'", "no comma after 'que'", "montre que, si", "punctuation",
    "high", fx(r"(1.1) montre que, si", r"(1.1) montre que si"), "The TeX adds a comma.")
add(288, "'les relations [display] montre que'", "'montre' (singular)", "montrent que", "misprint_in_print",
    "high", fx(r"montrent que", r"montre que"),
    "The subject is 'les relations'; the TeX silently corrects the verb.", corrected="montrent que")
add(288, "'Le lemme entraîne la partie a) de 2.2.1.'", "2.2.1", "2.2.1", "misprint_in_print", "medium", None,
    "Wrong reference: part a) (R^{2i+1}p_*(A_P) = 0) is Proposition 2.2.2 a), the statement being proved; "
    "Theorem 2.2.1 has no parts. The TeX keeps the printed reading.", corrected="2.2.2")
add(288, "last display A[T]/(T^{r+1}) → ⊕ H^{2i}(P,μ^{⊗i})", "no punctuation; the sentence continues on p. 289",
    r"(P,\mu^{\otimes i}).", "punctuation", "high",
    fx(r"^{\otimes i}).⏎", r"^{\otimes i})⏎"), "The TeX adds a full stop.")
add(288, "end of the page / top of p. 289 'de sorte que'",
    "p. 289 continues the sentence after the display: 'de sorte que' at the left margin, no indent",
    "two blank lines before the folio-289 marker (a new paragraph)", "other", "high",
    fx(r"\]⏎⏎⏎", r"\]⏎"),
    "Paragraph break added by the TeX (global issue 44); drop it if paragraphing is left to a global pass. The "
    "marker line then follows '\\]' directly; the marker itself is in the right place.")

# ---------------------------------------------------------------- page 289
add(289, "'l'assertion sera prouvée si on montre que pour tout'", "'si on'", "si l'on", "word", "high",
    fx(r"si l'on", r"si on"))
add(289, "'si on montre que pour tout i ∈ [0,r]'", "no comma after 'que'", "que, pour tout", "punctuation",
    "high", fx(r"que, pour tout $i", r"que pour tout $i"), "The TeX adds a comma.")
add(289, "diagram, label of the hooked arrow", "'inj.' with a full stop", r"\mathrm{inj}", "punctuation", "high",
    fx(r'"\mathrm{inj}"', r'"\mathrm{inj.}"'),
    "The abbreviation stop of the print. (The print draws k centred below, both arrows to k diagonal: layout.)")
add(289, "diagram, vertex k", "no comma after k", "& k ,", "punctuation", "high", fx(r"& k ,", r"& k"),
    "The TeX adds a comma.")
add(289, "Corollaire 2.2.4, 'Soit L un complexe de A_S-Modules. La flèche'",
    "underlined: 'Soit' | 'un complexe de' | 'Modules. La flèche' (L and A_S- not); Modules with a capital M",
    "no underline markup; modules", "underline", "high",
    fx(r"Soit $L$ un complexe de $A_S$-modules. La flèche",
       r"\emph{Soit} $L$ \emph{un complexe de} $A_S$-\emph{Modules. La flèche}"),
    "One edit: it also gives the print's capital M (word).")
add(289, "Corollaire 2.2.4, display RΓ(S, γ ⊗ id(L))", "a tensor sign with two short bars under it; no L, no A",
    r"\gamma\lten_A\mathrm{id}(L)", "symbol", "medium",
    fx(r"\gamma\lten_A\mathrm{id}(L)", r"\gamma\mathbin{\underline{\underline{\otimes}}}\mathrm{id}(L)"),
    "\\lten is \\overset{\\mathrm L}{\\otimes}. Written as the logged fix of the tensor of (2.1.1) on p. 285; one "
    "decision with the other occurrences of the exposé.")
add(289, "Corollaire 2.2.4, 'est un isomorphisme.'", "underlined", "no underline markup", "underline", "high",
    fx(r"est un isomorphisme.⏎\end{statement}", r"\emph{est un isomorphisme}.⏎\end{statement}"))
add(289, "'à l'isomorphisme γ ⊗_A id_L .'", "⊗ with A below it; no L above, no bars", r"\gamma\lten_A\mathrm{id}_L",
    "symbol", "high", fx(r"\gamma\lten_A\mathrm{id}_L", r"\gamma\otimes_A\mathrm{id}_L"),
    "The TeX adds the L of the derived tensor, which the print does not have here.")
add(289, "numbered paragraph 2.2.5", "'2.2.5.' (with a full stop)", r"\subsubsection*{2.2.5}", "punctuation",
    "high", fx(r"\subsubsection*{2.2.5}", r"\subsubsection*{2.2.5.}"), "As the logged '2.1.' of p. 285.")
add(289, "2.2.5, 'nous poserons pour tout schéma X'", "no commas", "nous poserons, pour tout schéma $X$,",
    "punctuation", "high", fx(r"nous poserons, pour tout schéma $X$,", r"nous poserons pour tout schéma $X$"),
    "The TeX adds two commas.")
add(289, "'et nous utiliserons sytématiquement cette notation'", "'sytématiquement' (no s before t)",
    "systématiquement", "misprint_in_print", "high", fx(r"systématiquement", r"sytématiquement"),
    "Typing error; the TeX silently corrects it.", corrected="systématiquement")
add(289, "Corollaire 2.2.6, 'L'homomorphisme image réciproque'", "underlined", "no underline markup",
    "underline", "high", fx(r"L'homomorphisme image réciproque", r"\emph{L'homomorphisme image réciproque}"))
add(289, "Corollaire 2.2.6, sentence after the display",
    "underlined: 'est un morphisme injectif d'anneaux unitaires, et les éléments' | 'forment une base du' | "
    "'module' | 'En particulier' | 'est un' | 'module libre de même rang que' (formulas, A•(S)- and E not)",
    "no underline markup", "underline", "high",
    fx(r"est un morphisme injectif d'anneaux unitaires, et les éléments $1,\xi,\ldots,\xi^r$ forment une base du "
       r"$A^\bullet(S)$-module $A^\bullet(P)$. En particulier, $A^\bullet(P)$ est un $A^\bullet(S)$-module libre "
       r"de même rang que $E$.",
       r"\emph{est un morphisme injectif d'anneaux unitaires, et les éléments} $1,\xi,\ldots,\xi^r$ \emph{forment "
       r"une base du} $A^\bullet(S)$-\emph{module} $A^\bullet(P)$. \emph{En particulier}, $A^\bullet(P)$ "
       r"\emph{est un} $A^\bullet(S)$-\emph{module libre de même rang que} $E$."))

# ---------------------------------------------------------------- page 290
add(290, "section title 3", "'3. CLASSES DE CHERN': hand-drawn capitals, underlined, no full stop",
    r"\section*{3. Classes de Chern}", "word", "high",
    fx(r"\section*{3. Classes de Chern}", r"\section*{3. CLASSES DE CHERN}"),
    "Capitals as printed, as the logged '1. FIBRES VECTORIELS' (p. 282) and '2. SCHEMAS PROJECTIFS' (p. 285).")
add(290, "'E un O_S-Module localement libre de rang constant r'", "Module with a capital M",
    r"$\mathcal O_S$-module", "word", "high",
    fx(r"$\mathcal O_S$-module localement libre de rang", r"$\mathcal O_S$-Module localement libre de rang"))
add(290, "'le A•(S)-module A•(P) est libre de base'", "A• (raised dot), as A•(X) of 2.2.5",
    r"$A^*(S)$-module $A^*(P)$", "symbol", "high",
    fx(r"le $A^*(S)$-module $A^*(P)$", r"le $A^\bullet(S)$-module $A^\bullet(P)$"),
    "The TeX has a star; written A^\\bullet as the file writes A•(X) on p. 289.")
add(290, "'il est immédiat pour des raisons d'homogénéité qu'il existe'", "no commas",
    "immédiat, pour des raisons d'homogénéité,", "punctuation", "high",
    fx(r"immédiat, pour des raisons d'homogénéité, qu'il", r"immédiat pour des raisons d'homogénéité qu'il"),
    "The TeX adds two commas.")
add(290, "number of the relation 3.1", "'3.1.' at the left: no parentheses, a full stop", r"\tag{3.1}",
    "punctuation", "high", fx(r"\tag{3.1}", r"\tag*{3.1.}"),
    "\\tag prints '(3.1)'; the print has '3.1.' (and Définition 3.2 cites 'la relation 3.1.').")
add(290, "'Soit maintenant E un O_S-Module localement libre quelconque'", "Module with a capital M",
    r"$\mathcal O_S$-module", "word", "high",
    fx(r"$\mathcal O_S$-module localement libre quelconque", r"$\mathcal O_S$-Module localement libre quelconque"))
add(290, "'pour tout A_S-Module M et tout entier i'", "Module with a capital M", r"$A_S$-module $M$", "word", "high",
    fx(r"$A_S$-module $M$", r"$A_S$-Module $M$"))
add(290, "Définition 3.2, first sentence and 'Pour tout entier i ≥ 0, on appelle'",
    "underlined: 'Soient' | 'un schéma et' | 'un' | 'Module localement libre. Pour tout entier' | 'on appelle' "
    "(S, E, O_S-, i ≥ 0, not); Module with a capital M", "no underline markup; module", "underline", "high",
    fx(r"Soient $S$ un schéma et $E$ un $\mathcal O_S$-module localement libre. Pour tout entier $i\ge0$, on appelle",
       r"\emph{Soient} $S$ \emph{un schéma et} $E$ \emph{un} $\mathcal O_S$-\emph{Module localement libre. Pour "
       r"tout entier} $i\ge0$, \emph{on appelle}"),
    "One edit: it also gives the print's capital M (word).")
add(290, "Définition 3.2, 'i^{ème} classe de Chern'", "i with a raised 'ème' (no hyphen)", "$i$-ème", "word",
    "high", fx(r"$i$-ème", r"$i^{\text{ème}}$"), "As the logged ν^{èmes} of p. 282.")
add(290, "Définition 3.2, 'classe de Chern de E et on note c_i(E) , l'élément de H^{2i}(S,μ^{⊗i})'",
    "underlined: 'classe de Chern de' | 'et on note' | 'l'élément de' (line break between 'l'élément' and "
    "'de'); a comma after c_i(E)", "no underline markup; no comma", "underline", "high",
    fx(r"classe de Chern de $E$ et on note $c_i(E)$ l'élément de $H^{2i}",
       r"\emph{classe de Chern de} $E$ \emph{et on note} $c_i(E)$, \emph{l'élément de} $H^{2i}"),
    "One edit: it also gives the print's comma after c_i(E) (punctuation).")
add(290, "Définition 3.2, 'dont, pour tout entier r ≥ 0, ... l'élément'",
    "underlined: 'dont, pour tout entier' | 'la restriction à l'ouvert' | 'de' | 'formé des points où' | "
    "'est de rang' | 'est l'élément' | 'défini par la relation' | 'Si le rang de' | 'est borné, on appelle "
    "classe de Chern totale de' | 'l'élément' (formulas and '3.1.' not)", "no underline markup", "underline",
    "high",
    fx(r"dont, pour tout entier $r\ge0$, la restriction à l'ouvert $S_r$ de $S$ formé des points où $E$ est de "
       r"rang $r$ est l'élément $c_i$ défini par la relation 3.1. Si le rang de $E$ est borné, on appelle classe "
       r"de Chern totale de $E$ l'élément",
       r"\emph{dont, pour tout entier} $r\ge0$, \emph{la restriction à l'ouvert} $S_r$ \emph{de} $S$ \emph{formé "
       r"des points où} $E$ \emph{est de rang} $r$ \emph{est l'élément} $c_i$ \emph{défini par la relation} 3.1. "
       r"\emph{Si le rang de} $E$ \emph{est borné, on appelle classe de Chern totale de} $E$ \emph{l'élément}"))
add(290, "Définition 3.2, 'de A•(S) ; dans le cas général, on désigne ainsi l'élément correspondant dans'",
    "underlined: 'de' | 'dans le cas général, on désigne ainsi l'élément correspondant dans'; A• (raised dot)",
    "no underline markup; $A^*(S)$", "underline", "high",
    fx(r"de $A^*(S)$; dans le cas général, on désigne ainsi l'élément correspondant dans",
       r"\emph{de} $A^\bullet(S)$; \emph{dans le cas général, on désigne ainsi l'élément correspondant dans}"),
    "One edit: it also gives the raised dot for the TeX's star (symbol). Independent of the marker move below "
    "(its anchor is the next line).")
add(290, "end of the page / folio-291 marker",
    "p. 290 ends with '... l'élément correspondant dans' (rest of the page blank); the display "
    "Â•(S) = Π A^i(S), the end of Définition 3.2 and '3.3 Il est' are printed on p. 291",
    "the display \\widehat A^*(S)=\\prod_i A^i(S)., \\end{statement}, \\subsubsection*{3.3} and 'Il est' stand "
    "under the folio-290 marker; the folio-291 marker follows 'Il est'", "marker", "high", None,
    "Page 291 really begins at the display '\\[' + '\\widehat A^*(S)=...' after 'correspondant dans' (s5.tex "
    "diplomatic line 9761, current 9756, at the time of the check). Exact fix (bash): python -I move_marker.py 5 "
    "291 $'\\\\[\\n\\\\widehat A' --before (the anchor is '\\[', a line break, '\\widehat A'; simulated in memory "
    "on both layers, identical: the marker then stands on its own line between 'l'élément correspondant dans' "
    "and '\\[', no blank line, so no paragraph break). Text not moved. The p. 291 check may report the same move.")

# ---------------------------------------------------------------- validation
ok = True
for page in sorted({f["page"] for f in F}):
    orig = open(B % page, encoding="utf-8", newline="").read()
    cur = orig
    for f in [f for f in F if f["page"] == page]:
        if f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
            print("MARKER IN FIX", page, f["where"]); ok = False
        n_cur, n_orig = cur.count(old), orig.count(old)
        flag = "" if (n_cur == 1 and n_orig == 1) else "  <-- cur %d orig %d" % (n_cur, n_orig)
        if n_cur != 1:
            ok = False
        if flag:
            print(page, f["kind"], repr(old[:60]), flag)
        cur = cur.replace(old, new, 1)
    # corrected layer: skip misprint fixes, all others must still apply
    cor = orig
    for f in [f for f in F if f["page"] == page]:
        if f["fix"] is None or f["kind"] == "misprint_in_print":
            continue
        if cor.count(f["fix"]["old"]) != 1:
            print("CORRECTED-LAYER PROBLEM", page, repr(f["fix"]["old"][:60])); ok = False
        cor = cor.replace(f["fix"]["old"], f["fix"]["new"], 1)

counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))
print("ALL OK" if ok else "PROBLEMS")
if ok and "--write" in sys.argv:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
