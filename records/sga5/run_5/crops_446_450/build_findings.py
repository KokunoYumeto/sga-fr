import json
import sys

# Builds findings_446_450.json and checks every fix: old occurs exactly once in its page file, olds of one page do
# not overlap, and all fixes of a page apply one after another. Strings are raw; <NL> stands for a line break.
sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
PAGEFILE = {p: rf"{RUN}\b446_450\page_{p}.tex" for p in range(446, 451)}
PAGEFILE[451] = rf"{RUN}\b451_455\page_451.tex"
OUT = rf"{RUN}\findings_446_450.json"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": nl(tex), "kind": kind, "confidence": conf,
         "fix": None if nofix else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


UL = ("The print underlines the statement of Proposition 2 word group by word group and leaves the formulas out; "
      "the TeX has no underline markup in the statements of Exposé XV. \\emph as the exposé's own "
      "\\emph{(Transitivité.)} on p. 445 (and as itemized for III B and V); punctuation kept outside.")

# ---------------- page 446 ----------------
add(446, "Proposition 2 b), first sentence",
    "b) Si X --> S est une immersion ouverte, X^(p) = X et Fr_X/S = id_X . : 'Si', 'est une immersion ouverte' and 'et' underlined, the formulas not",
    r"""\item Si $X\to S$ est une immersion ouverte, $X^{(p)}=X$ et $\Fr_{X/S}=\id_X$.""",
    "underline", "high",
    r"""\item Si $X\to S$ est une<NL>immersion ouverte, $X^{(p)}=X$ et $\Fr_{X/S}=\id_X$.""",
    r"""\item \emph{Si} $X\to S$ \emph{est une<NL>immersion ouverte}, $X^{(p)}=X$ \emph{et} $\Fr_{X/S}=\id_X$.""",
    UL)
add(446, "Proposition 2 b), second sentence",
    "Si X --> S est une immersion fermée, identifiant X à un sous-espace annelé fermé (|X|, O_S/J) de S , alors : 'Si', 'est une immersion fermée', 'identifiant', 'à un sous-espace annelé fermé', 'de', 'alors' underlined",
    r"""Si $X\to S$ est une immersion fermée, identifiant $X$ à un sous-espace annelé fermé $(|X|,\OO_S/\JJ)$ de $S$, alors""",
    "underline", "high",
    r""" Si $X\to S$ est une immersion fermée, identifiant $X$ à un sous-espace annelé fermé $(|X|,\OO_S/\JJ)$ de $S$, alors""",
    r""" \emph{Si} $X\to S$ \emph{est une immersion fermée}, \emph{identifiant} $X$ \emph{à un sous-espace annelé fermé} $(|X|,\OO_S/\JJ)$ \emph{de} $S$, \emph{alors}""",
    "As the first sentence.")
add(446, "Proposition 2 b), 'et Fr_X/S = (id_|X|, φ)'",
    "'et' underlined",
    r"""et $\Fr_{X/S}=(\id_{|X|},\varphi)$""",
    "underline", "high",
    r"""\]<NL>et $\Fr_{X/S}=(""",
    r"""\]<NL>\emph{et} $\Fr_{X/S}=(""",
    "As the first sentence.")
add(446, "Proposition 2 b), 'Fr_X/S = (id_|X|, φ) où φ : ...'",
    "=(id_|X|, φ)  où  φ : O_S/J^p --> O_S/J : no comma before 'où' (checked at 1.5x)",
    r"""$\Fr_{X/S}=(\id_{|X|},\varphi)$, où""",
    "punctuation", "high",
    r"""\varphi)$,""",
    r"""\varphi)$""",
    "The TeX adds a comma.")
add(446, "Proposition 2 b), 'où φ : O_S/J^p --> O_S/J'",
    "'où' underlined",
    r"""où $\varphi:\OO_S/\JJ^p\to\OO_S/\JJ$""",
    "underline", "high",
    r"""où $\varphi:""",
    r"""\emph{où} $\varphi:""",
    "As the first sentence.")
add(446, "Proposition 2 b), last line",
    "est l'augmentation évidente. (underlined up to 'évidente')",
    r"""$ est l'augmentation évidente.""",
    "underline", "high",
    r"""$ est l'augmentation évidente.""",
    r"""$ \emph{est l'augmentation évidente}.""",
    "As the first sentence.")
add(446, "Proposition 2 c), first sentence",
    "c) Supposons X localement de présentation finie sur S . : 'Supposons' and 'localement de présentation finie sur' underlined",
    r"""\item Supposons $X$ localement de présentation finie sur $S$.""",
    "underline", "high",
    r"""\item Supposons $X$ localement de présentation finie sur $S$.""",
    r"""\item \emph{Supposons} $X$ \emph{localement de présentation finie sur} $S$.""",
    "As b).")
add(446, "Proposition 2 c) 1)",
    "1) Les trois conditions suivantes sont équivalentes : (underlined up to 'équivalentes')",
    r"""\item Les trois conditions suivantes sont équivalentes:""",
    "underline", "high",
    r"""\item Les trois conditions suivantes sont équivalentes:""",
    r"""\item \emph{Les trois conditions suivantes sont équivalentes}:""",
    "As b).")
add(446, "c) 1), condition (i)",
    "(i)  X  est non ramifié sur  S : 'est non ramifié sur' underlined",
    r"""X\text{ est non ramifié sur }S,""",
    "underline", "high",
    r"""\text{ est non ramifié sur }""",
    r"""\text{ \emph{est non ramifié sur} }""",
    "As b).")
add(446, "c) 1), end of condition (i)",
    "est non ramifié sur  S (nothing after S)",
    r"""\text{ est non ramifié sur }S,\\""",
    "punctuation", "high",
    r""",\\<NL>\text{(ii)}&""",
    r"""\\<NL>\text{(ii)}&""",
    "The TeX adds a comma at the end of the line: the print's conditions (i), (ii), (i'), (ii') end without punctuation, (iii) and (iii') with a full stop (as the TeX).")
add(446, "c) 1), condition (ii)",
    "Fr_X/S  est non ramifié ('est non ramifié' underlined)",
    r"""\Fr_{X/S}\text{ est non ramifié},""",
    "underline", "high",
    r"""\text{ est non ramifié}""",
    r"""\text{ \emph{est non ramifié}}""",
    "As b).")
add(446, "c) 1), end of condition (ii)",
    "Fr_X/S  est non ramifié (nothing after it)",
    r"""\text{ est non ramifié},\\""",
    "punctuation", "high",
    r""",\\<NL>\text{(iii)}&""",
    r"""\\<NL>\text{(iii)}&""",
    "The TeX adds a comma.")
add(446, "c) 1), condition (iii)",
    "Fr_X/S  est un monomorphisme. ('est un monomorphisme' underlined)",
    r"""\Fr_{X/S}\text{ est un monomorphisme}.""",
    "underline", "high",
    r"""\text{ est un monomorphisme}""",
    r"""\text{ \emph{est un monomorphisme}}""",
    "As b).")
add(446, "Proposition 2 c) 2)",
    "2) De même les trois conditions suivantes sont équivalentes : (no comma after 'De même'; underlined from 'De' to 'équivalentes')",
    r"""\item De même, les trois conditions suivantes sont équivalentes:""",
    "underline", "high",
    r"""\item De même, les trois conditions suivantes sont équivalentes:""",
    r"""\item \emph{De même les trois conditions suivantes sont équivalentes}:""",
    "One edit for two differences: the underline (as b)) and the comma the TeX adds after 'De même'.")
add(446, "c) 2), condition (i')",
    "(i')  X  est étale sur  S : 'est étale sur' underlined",
    r"""X\text{ est étale sur }S,""",
    "underline", "high",
    r"""\text{ est étale sur }""",
    r"""\text{ \emph{est étale sur} }""",
    "As b).")
add(446, "c) 2), end of condition (i')",
    "est étale sur  S (nothing after S)",
    r"""\text{ est étale sur }S,\\""",
    "punctuation", "high",
    r""",\\<NL>\text{(ii')}&""",
    r"""\\<NL>\text{(ii')}&""",
    "The TeX adds a comma.")
add(446, "c) 2), condition (ii')",
    "Fr_X/S  est étale ('est étale' underlined)",
    r"""\Fr_{X/S}\text{ est étale},""",
    "underline", "high",
    r"""\text{ est étale}""",
    r"""\text{ \emph{est étale}}""",
    "As b).")
add(446, "c) 2), end of condition (ii')",
    "Fr_X/S  est étale (nothing after it)",
    r"""\text{ est étale},\\""",
    "punctuation", "high",
    r""",\\<NL>\text{(iii')}&""",
    r"""\\<NL>\text{(iii')}&""",
    "The TeX adds a comma.")
add(446, "c) 2), condition (iii')",
    "Fr_X/S  est un isomorphisme. ('est un isomorphisme' underlined)",
    r"""\Fr_{X/S}\text{ est un isomorphisme}.""",
    "underline", "high",
    r"""\text{ est un isomorphisme}""",
    r"""\text{ \emph{est un isomorphisme}}""",
    "As b).")
add(446, "proof of a), first words",
    "Démontrons a) ; le composé (semicolon, small l; checked at 4x)",
    r"""Démontrons a). Le composé""",
    "punctuation", "high",
    r"""Démontrons a). Le composé""",
    r"""Démontrons a); le composé""",
    "The TeX has a full stop and a new sentence for the print's semicolon.")
add(446, "proof of a), first sentence",
    "= fr_X  est entier / surjectif et radiciel : no comma after 'entier' at the line end (checked at 2x)",
    r"""est entier, surjectif et radiciel""",
    "punctuation", "high",
    r"""est entier, surjectif""",
    r"""est entier surjectif""",
    "The TeX adds a comma.")
add(446, "proof of a)",
    "; de plus  π_X/S  est séparé et radiciel (no comma after 'de plus')",
    r"""de plus, $\pi_{X/S}$""",
    "punctuation", "high",
    r"""de plus, $\pi_{X/S}$""",
    r"""de plus $\pi_{X/S}$""",
    "The TeX adds a comma.")
add(446, "proof of b)",
    "pour tout Idéal J de O_S (capital I; checked at 2x)",
    r"""pour tout idéal $\JJ$ de $\OO_S$.""",
    "word", "high",
    r"""pour tout idéal""",
    r"""pour tout Idéal""",
    "The print capitalizes Idéal (sheaf of ideals), as Module and Algèbre, which the TeX keeps; also pp. 447 and 450.")
add(446, "proof of c), label",
    "Preuve de c) : on sait que (colon, small o; not underlined)",
    r"""Preuve de c). On sait que""",
    "punctuation", "high",
    r"""Preuve de c). On""",
    r"""Preuve de c) : on""",
    "Proof label as printed (the global form '\\emph{Preuve} :' has the same ' :').")
add(446, "proof of c), first line",
    "on sait que pour qu'un morphisme soit un mo- (no comma after 'que')",
    r"""On sait que, pour qu'un morphisme""",
    "punctuation", "high",
    r"""sait que, pour""",
    r"""sait que pour""",
    "The TeX adds a comma.")

# ---------------- page 447 ----------------
RESP = "The TeX writes out the print's 'resp.' and replaces its parentheses by commas."
add(447, "first line (proof of c))",
    "(mo)nomorphisme (resp. un isomorphisme) il faut et il suffit (no comma after the parenthesis)",
    r"""monomorphisme, respectivement un isomorphisme, il faut""",
    "word", "high",
    r"""monomorphisme, respectivement un isomorphisme, il faut""",
    r"""monomorphisme (resp. un isomorphisme) il faut""",
    RESP)
add(447, "first sentence",
    "radiciel et non ramifié (resp. radiciel étale et surjectif) ; d'où (no comma after the second 'radiciel')",
    r"""non ramifié, respectivement radiciel, étale et surjectif;""",
    "word", "high",
    r"""non ramifié, respectivement radiciel, étale et surjectif;""",
    r"""non ramifié (resp. radiciel étale et surjectif);""",
    RESP + " The TeX also adds a comma after 'radiciel'.")
add(447, "first sentence, end",
    "l'équivalence de (ii) et (iii) (resp. (ii') et (iii')).",
    r"""(iii), respectivement de (ii') et (iii').""",
    "word", "high",
    r"""(iii), respectivement de (ii') et (iii').""",
    r"""(iii) (resp. (ii') et (iii')).""",
    RESP + " The TeX also adds 'de'.")
add(447, "second paragraph, first line",
    "critère différentiel de non rami-/fication : a space between 'non' and 'rami-'; the hyphen is the line-end break",
    r"""non-ramification""",
    "punctuation", "high",
    r"""non-ramification""",
    r"""non ramification""",
    "The TeX adds a hyphen between 'non' and 'ramification'.")
add(447, "second paragraph, reference",
    "(S.G.A. I 3)",
    r"""(SGA I 3)""",
    "punctuation", "high",
    r"""(SGA I 3)""",
    r"""(S.G.A. I 3)""",
    "The print writes S.G.A. with full stops (three times on this page; EGA on p. 446 without); the TeX drops them.")
add(447, "second paragraph, the isomorphism Ω^1_X/S -> Ω^1_X/X^(p)",
    "a hand-drawn arrow with a tilde above it (arrowhead clear at 7x); the plain ≃ signs of pp. 448-450 have no arrowhead",
    r"""\Omega^1_{X/S}\simeq \Omega^1_{X/X^{(p)}}""",
    "symbol", "high",
    r"""S}\simeq \Omega""",
    r"""S}\xrightarrow{\sim} \Omega""",
    "Isomorphism arrow, written \\xrightarrow{\\sim} as elsewhere in the file.")
add(447, "exact sequence, first term",
    "Fr_X/S(Ω^1_X(p)/S) --> Ω^1_X/S --> Ω^1_X/X(p) --> 0 : no star on Fr (checked at 2.5x)",
    r"""\Fr_{X/S}(\Omega^1_{X^{(p)}/S})""",
    "misprint_in_print", "high", None, None,
    "The first term of the canonical sequence is the inverse image Fr^*_X/S(Ω^1); the print leaves out the star. The TeX keeps the printed reading; the corrected layer (current/s5.tex) already reads \\Fr_{X/S}^*.",
    corrected=r"""\Fr_{X/S}^*(\Omega^1_{X^{(p)}/S})""", nofix=True)
add(447, "after the exact sequence",
    "(S.G.A. II 4), dans laquelle",
    r"""(SGA II 4)""",
    "punctuation", "high",
    r"""(SGA II 4)""",
    r"""(S.G.A. II 4)""",
    "As (S.G.A. I 3) above.")
add(447, "third paragraph, first sentence",
    "il en est de même de X^(p) (changement de base), et par suite",
    r"""de $X^{(p)}$ par changement de base, et par suite""",
    "word", "high",
    r"""$X^{(p)}$ par changement de base,""",
    r"""$X^{(p)}$ (changement de base),""",
    "The TeX adds 'par' and drops the parentheses.")
add(447, "third paragraph",
    "donc X est non ramifié sur S ; autrement dit le morphisme structural (semicolon, small a, no comma after 'dit'; checked at 2.5x)",
    r"""sur $S$. Autrement dit, le""",
    "punctuation", "high",
    r"""sur $S$. Autrement dit, le""",
    r"""sur $S$; autrement dit le""",
    "The TeX has a full stop, a new sentence and a comma.")
add(447, "third paragraph",
    "est localement sur X (pour la topologie étale) une immersion fermée",
    r"""sur $X$, pour la topologie étale, une""",
    "punctuation", "high",
    r"""sur $X$, pour la topologie étale, une""",
    r"""sur $X$ (pour la topologie étale) une""",
    "Parentheses in the print; the TeX has commas.")
add(447, "third paragraph, reference",
    "(S.G.A. I cor.7.8)",
    r"""(SGA I cor. 7.8)""",
    "punctuation", "high",
    r"""(SGA I cor.""",
    r"""(S.G.A. I cor.""",
    "Full stops of S.G.A., as above (the space after 'cor.' is spacing, left alone).")
add(447, "third paragraph",
    "si Fr_X/S est un isomorphisme  g  est une immersion ouverte (no comma; checked at 1.2x)",
    r"""est un isomorphisme, $g$ est une immersion ouverte""",
    "punctuation", "high",
    r"""isomorphisme, $g$ est""",
    r"""isomorphisme $g$ est""",
    "The TeX adds a comma.")
add(447, "third paragraph",
    "Or X est défini par un Idéal J de type fini : (capital I)",
    r"""Or $X$ est défini par un idéal $\JJ$""",
    "word", "high",
    r"""par un idéal""",
    r"""par un Idéal""",
    "As p. 446.")
add(447, "third paragraph, before the display X = (|X|, O_S/J)",
    "de type fini : (colon; checked at 1.2x)",
    r"""de type fini,""",
    "punctuation", "high",
    r"""de type fini,<NL>\[""",
    r"""de type fini:<NL>\[""",
    "Colon in the print, comma in the TeX.")
add(447, "display X = (|X|, O_S/J)",
    "X = (|X|, O_S/J ) et, d'après b), (nothing after the formula)",
    r"""X=(|X|,\OO_S/\JJ),""",
    "punctuation", "high",
    r"""\JJ),<NL>\]<NL>et, d'après""",
    r"""\JJ)<NL>\]<NL>et, d'après""",
    "The TeX adds a comma at the end of the display.")
add(447, "display of X^(p) and Fr_X/S, and the next words",
    "Fr_X/S = (id_|X|, O_S/J^p --> O_S/J ) ; dire que Fr_X/S est un (semicolon, small d)",
    r"""\Fr_{X/S}=(\id_{|X|},\OO_S/\JJ^p\to\OO_S/\JJ).<NL>\]<NL>Dire que""",
    "punctuation", "high",
    r"""\to\OO_S/\JJ).<NL>\]<NL>Dire que""",
    r"""\to\OO_S/\JJ);<NL>\]<NL>dire que""",
    "The TeX has a full stop and a new sentence for the print's semicolon.")
add(447, "last sentence",
    "revient donc à dire que J = J^p , et comme J est (comma after J^p, no comma after 'et')",
    r"""$\JJ=\JJ^p$; et, comme""",
    "punctuation", "high",
    r"""$\JJ=\JJ^p$; et,""",
    r"""$\JJ=\JJ^p$, et""",
    "Semicolon for the print's comma, and a comma added after 'et'.")
add(447, "last sentence",
    "de type fini on en déduit par le lemme de Nakayama (no comma)",
    r"""de type fini, on en déduit""",
    "punctuation", "high",
    r"""fini, on en déduit""",
    r"""fini on en déduit""",
    "The TeX adds a comma.")
add(447, "last sentence",
    "ou J_s = O_S,s  pour tout point s ∈ S , d'où (no comma after O_S,s)",
    r"""$\JJ_s=\OO_{S,s}$, pour tout point""",
    "punctuation", "high",
    r"""\OO_{S,s}$, pour""",
    r"""\OO_{S,s}$ pour""",
    "The TeX adds a comma.")

# ---------------- page 448 ----------------
add(448, "title of n°3",
    "n°3. Effet sur un Module. Exemples. (underlined, ends with a full stop)",
    r"""\subsubsection*{n\textsuperscript{o} 3. Effet sur un Module. Exemples}""",
    "punctuation", "high",
    r"""Module. Exemples}""",
    r"""Module. Exemples.}""",
    "The TeX drops the full stop that ends the underlined title.")
add(448, "first paragraph",
    "pour tout O_X-Module E (faisceau pour la topologie de Zariski), on pose",
    r"""$\cE$, faisceau pour la topologie de Zariski, on pose""",
    "punctuation", "high",
    r"""$\cE$, faisceau pour la topologie de Zariski, on pose""",
    r"""$\cE$ (faisceau pour la topologie de Zariski), on pose""",
    "Parentheses in the print; the TeX has commas.")
add(448, "paragraph 'Le cas le plus intéressant', last sentence",
    "qui n'est pas O_S-linéaire, mais \"p -linéaire\" (en un sens évident) ; c'est visi-blement",
    r"""mais $p$-linéaire, en un sens évident;""",
    "punctuation", "high",
    r"""mais $p$-linéaire, en un sens évident;""",
    r"""mais ``$p$-linéaire'' (en un sens évident);""",
    "The TeX drops the print's straight quotes (written ``...'' elsewhere in the exposé, e.g. ``topologiquement unipotent'') and replaces the parentheses by a comma.")
add(448, "same sentence",
    "un morphisme  p -linéaire universel de E : 'morphisme' underlined, and 'linéaire universel' underlined from the l (the hyphen is not; checked at 3x)",
    r"""un morphisme $p$-linéaire universel de $\cE$""",
    "underline", "high",
    r"""visiblement un morphisme $p$-linéaire universel""",
    r"""visiblement un \emph{morphisme} $p$-\emph{linéaire universel}""",
    "Emphasis by underlining, \\emph as for the statements. The second 'morphisme p-linéaire universel' (end of the page) is not underlined.")
add(448, "paragraph 'Il est clair'",
    "le foncteur E ~~> E^(p) : a hand-drawn wavy arrow (checked at 1.2x)",
    r"""\cE\mapsto\cE^{(p)}""",
    "symbol", "high",
    r"""\cE\mapsto\cE^{(p)}""",
    r"""\cE\rightsquigarrow\cE^{(p)}""",
    "The file writes the print's wavy arrow \\rightsquigarrow elsewhere (Exposé VIII).")
add(448, "paragraph 'Il est clair'",
    "est exact à droite (mais pas exact en général) ; il commute",
    r"""à droite, mais pas exact en général;""",
    "punctuation", "high",
    r"""à droite, mais pas exact en général;""",
    r"""à droite (mais pas exact en général);""",
    "Parentheses in the print; the TeX has a comma.")
add(448, "paragraph 'Il est clair'",
    "etc. En particulier si L est un faisceau inversible (no comma)",
    r"""En particulier, si""",
    "punctuation", "high",
    r"""En particulier, si""",
    r"""En particulier si""",
    "The TeX adds a comma.")

# ---------------- page 449 ----------------
add(449, "top of the page",
    "p. 449 begins with 'Si A est une O_S-Algèbre, A^(p) possède une struc-ture de O_S-Algèbre déduite de celle de A .'; p. 448 ends with '... est un morphisme p-linéaire universel.'",
    r"""The line 'Si $\mathcal{A}$ est une $\OO_S$-Algèbre, $\mathcal{A}^{(p)}$ possède une structure de $\OO_S$-' is the last line of page_448.tex; the folio-449 marker stands after it, between '$\OO_S$-' and 'Algèbre déduite'.""",
    "marker", "high", None, None,
    "Page 449 really begins at the paragraph 'Si $\\mathcal{A}$ est une $\\OO_S$-Algèbre' (s5.tex about line 15051 as the file stands; line numbers move while other batches are applied). Exact fix: python -I move_marker.py 5 449 'Si $\\mathcal{A}$ est une' --before (single quotes keep the shell from expanding $; simulated in memory on both layers: the marker lands on its own line just before that paragraph). Text not moved; the line agrees with the print of p. 449. No edit of this batch touches it.",
    nofix=True)
add(449, "first paragraph",
    "Supposons A quasi-cohérente (resp. graduée et quasi-cohérente) ; il en est de même",
    r"""quasi-cohérente, respectivement graduée et quasi-cohérente;""",
    "word", "high",
    r"""quasi-cohérente, respectivement graduée et quasi-cohérente;""",
    r"""quasi-cohérente (resp. graduée et quasi-cohérente);""",
    RESP)
add(449, "first paragraph, end",
    "il en est de même de A^(p) et on a : (colon; checked at 2x)",
    r"""et on a""",
    "punctuation", "high",
    r"""et on a<NL>\[""",
    r"""et on a:<NL>\[""",
    "The TeX drops the colon.")
add(449, "display Spec(A^(p)) = ...",
    "... = Spec(A)^(p) (nothing after it; '(resp.' follows on the next line)",
    r"""=\Spec(\mathcal{A})^{(p)},""",
    "punctuation", "high",
    r"""\Spec(\mathcal{A})^{(p)},<NL>\]""",
    r"""\Spec(\mathcal{A})^{(p)}<NL>\]""",
    "The TeX adds a comma at the end of the display.")
add(449, "'(resp.' and the Proj display",
    "(resp. / Proj(A^(p)) = Proj(A ⊗_O_S O_(S,fr_S)) ≃ Proj(A) x_S (S,fr_S) = Proj(A)^(p)). : the parenthesis opened by '(resp.' closes before the final full stop",
    r"""respectivement \[ \Proj(\mathcal{A}^{(p)})=... =\Proj(\mathcal{A})^{(p)}. \]""",
    "word", "high",
    r"""respectivement<NL>\[<NL>\Proj(\mathcal{A}^{(p)})=\Proj(\mathcal{A}\otimes_{\OO_S}\OO_{(S,\fr_S)})<NL> \simeq \Proj(\mathcal{A})\times_S(S,\fr_S)=\Proj(\mathcal{A})^{(p)}.""",
    r"""(resp.<NL>\[<NL>\Proj(\mathcal{A}^{(p)})=\Proj(\mathcal{A}\otimes_{\OO_S}\OO_{(S,\fr_S)})<NL> \simeq \Proj(\mathcal{A})\times_S(S,\fr_S)=\Proj(\mathcal{A})^{(p)}).""",
    RESP + " One edit, so that both parentheses go in together (the display set apart is layout).")
add(449, "paragraph 'La projection'",
    "--> Spec(A) (resp. π_Proj(A)/S) s'identifie",
    r"""$, respectivement $\pi_{\Proj(\mathcal{A})/S}$, s'identifie""",
    "word", "high",
    r"""$, respectivement $\pi_{\Proj(\mathcal{A})/S}$, s'identifie""",
    r"""$ (resp. $\pi_{\Proj(\mathcal{A})/S}$) s'identifie""",
    RESP)
add(449, "paragraph 'La projection'",
    "D'autre part Fr_Spec(A)/S (resp. Fr_Proj(A)/S) provient",
    r"""$, respectivement $\Fr_{\Proj(\mathcal{A})/S}$, provient""",
    "word", "high",
    r"""$, respectivement $\Fr_{\Proj(\mathcal{A})/S}$, provient""",
    r"""$ (resp. $\Fr_{\Proj(\mathcal{A})/S}$) provient""",
    RESP)
add(449, "paragraph 'La projection'",
    "Pour le voir on observe (no comma)",
    r"""Pour le voir, on""",
    "punctuation", "high",
    r"""Pour le voir, on""",
    r"""Pour le voir on""",
    "The TeX adds a comma.")
add(449, "paragraph 'La projection', end",
    "avec A --> A^(p) (à droite) est l'élévation",
    r"""$\mathcal{A}\to\mathcal{A}^{(p)}$, à droite, est""",
    "punctuation", "high",
    r"""$, à droite, est""",
    r"""$ (à droite) est""",
    "Parentheses in the print; the TeX has commas.")
add(449, "paragraph 'Considérons le cas particulier'",
    "où A est l'Algèbre sym-/métrique (capital A)",
    r"""l'algèbre symétrique""",
    "word", "high",
    r"""l'algèbre""",
    r"""l'Algèbre""",
    "Capital A as the print (Algèbre of a sheaf of algebras, as 'O_S-Algèbre' above, which the TeX keeps).")
add(449, "same sentence",
    "l'Algèbre sym- / métrique : the line ends with 'sym-' and the next begins 'métrique', i.e. 'symmétrique' with two m (the same spelling stands mid-line on p. 450)",
    r"""symétrique""",
    "misprint_in_print", "medium",
    r"""symétrique""",
    r"""symmétrique""",
    "Spelling slip of the typescript; the TeX silently corrects it. Diplomatic layer only. The olds of this edit and of the capital-A edit before it do not overlap.",
    corrected=r"""symétrique""")
add(449, "same sentence",
    "A^(p) ≃ Sym(E^(p))  donc (no comma; checked at 2x)",
    r"""\Sym(\cE^{(p)})$, donc""",
    "punctuation", "high",
    r"""\Sym(\cE^{(p)})$, donc""",
    r"""\Sym(\cE^{(p)})$ donc""",
    "The TeX adds a comma.")
add(449, "display V(E^(p)) ≃ ...",
    "... = V(E)^(p) (nothing after it)",
    r"""=\mathbb V(\cE)^{(p)},""",
    "punctuation", "high",
    r"""=\mathbb V(\cE)^{(p)},<NL>\]""",
    r"""=\mathbb V(\cE)^{(p)}<NL>\]""",
    "The TeX adds a comma at the end of the display.")
add(449, "display P(E^(p)) ≃ ... and the next words",
    "... = P(E)^(p)  ; / quant à Fr_V(E)/S (semicolon, small q)",
    r"""=\mathbb P(\cE)^{(p)}.<NL>\]<NL>Quant à""",
    "punctuation", "high",
    r"""=\mathbb P(\cE)^{(p)}.<NL>\]<NL>Quant à""",
    r"""=\mathbb P(\cE)^{(p)};<NL>\]<NL>quant à""",
    "The TeX has a full stop and a new sentence for the print's semicolon.")
add(449, "'quant à ...'",
    "quant à Fr_V(E)/S (resp. Fr_P(E)/S) , il se factorise",
    r"""$, respectivement $\Fr_{\mathbb P(\cE)/S}$, il""",
    "word", "high",
    r"""$, respectivement $\Fr_{\mathbb P(\cE)/S}$, il""",
    r"""$ (resp. $\Fr_{\mathbb P(\cE)/S}$), il""",
    RESP)
add(449, "last display",
    "V(E) --> V(Sym^p(E)) --> V(E^(p))  (resp. P(E) --> P(Sym^p(E)) --> P(E^(p))) : one line; nothing after V(E^(p)); the parenthesis closes after P(E^(p)); no punctuation at the end (checked at 2.5x)",
    r"""\mathbb V(\cE^{(p)}), \] respectivement \[ ... \mathbb P(\cE^{(p)}), \]""",
    "word", "high",
    r"""\mathbb V(\cE^{(p)}),<NL>\]<NL>respectivement<NL>\[<NL>\mathbb P(\cE)\longrightarrow \mathbb P(\Sym^p(\cE))\longrightarrow \mathbb P(\cE^{(p)}),""",
    r"""\mathbb V(\cE^{(p)})<NL>\]<NL>(resp.<NL>\[<NL>\mathbb P(\cE)\longrightarrow \mathbb P(\Sym^p(\cE))\longrightarrow \mathbb P(\cE^{(p)}))""",
    RESP + " The TeX also adds a comma at the end of both displays. One edit, so that both parentheses go in together (two displays for the print's one line: layout).")

# ---------------- page 450 ----------------
add(450, "end of the page",
    "p. 450 ends with '... et le morphisme de Frobenius Fr_X/S : X --> X^(p) est défini par l'élévation à la puissance p -ième des \"coordonnées\" T_i (qui détermine un morphisme A^(p) --> A ).'; p. 451 begins with the title 'n°4. Morphisme de Frobenius itéré ; préschémas parfaits.' (scan of p. 451)",
    r"""page_450.tex ends with '..., et le'; the end of the sentence ('morphisme de Frobenius', the display \Fr_{X/S}:X\longrightarrow X^{(p)}, 'est défini par ... $\mathcal{A}^{(p)}\to\mathcal{A}$.') stands under the folio-451 marker, before \subsubsection*{n\textsuperscript{o} 4. ...}.""",
    "marker", "high", None, None,
    "Page 451 really begins at '\\subsubsection*{n\\textsuperscript{o} 4. Morphisme de Frobenius itéré; préschémas parfaits}'. Exact fix: python -I move_marker.py 5 451 '\\subsubsection*{n\\textsuperscript{o} 4.' (forward search; simulated in memory on both layers: the marker lands on its own line just before the title). Text not moved. Apply the two edits filed under page 451 (the end of this sentence, compared with the print of p. 450) before the move.",
    nofix=True)
add(450, "first line",
    "où la première flèche est définie par le morphisme canonique : (colon; checked at 2.5x)",
    r"""le morphisme canonique (no colon before the display)""",
    "punctuation", "high",
    r"""le morphisme canonique<NL>\[""",
    r"""le morphisme canonique:<NL>\[""",
    "The TeX drops the colon.")
add(450, "after the first display",
    "qui provient de Sym^p(E) --> Sym(E)  tandis que (no comma)",
    r"""\Sym(\cE)$, tandis que""",
    "punctuation", "high",
    r"""\Sym(\cE)$, tandis que""",
    r"""\Sym(\cE)$ tandis que""",
    "The TeX adds a comma.")
add(450, "after the second display",
    "provenant du morphisme  p -linéaire :  E --> Sym^p(E) , donné par (colon after 'linéaire', comma after the formula; checked at 1.2x)",
    r"""$p$-linéaire $\cE\to\Sym^p(\cE)$ donné par""",
    "punctuation", "high",
    r"""$p$-linéaire $\cE\to\Sym^p(\cE)$ donné par""",
    r"""$p$-linéaire: $\cE\to\Sym^p(\cE)$, donné par""",
    "The TeX drops the colon and the comma.")
add(450, "same sentence",
    "l'élévation à la puissance symmétrique  p -ième des sections (two m)",
    r"""puissance symétrique""",
    "misprint_in_print", "high",
    r"""puissance symétrique""",
    r"""puissance symmétrique""",
    "Spelling slip of the typescript (as 'sym-/métrique' on p. 449); the TeX silently corrects it. Diplomatic layer only.",
    corrected=r"""puissance symétrique""")
add(450, "paragraph 'Lorsque'",
    "X = V(E) = S[T_1,...,T_n]  (resp.  X = P(E) = P^n-1_S) ; il est clair",
    r"""$, respectivement $X=\mathbb P(\cE)=\mathbb P_S^{n-1}$, il est clair""",
    "word", "high",
    r"""$, respectivement $X=\mathbb P(\cE)=\mathbb P_S^{n-1}$, il est clair""",
    r"""$ (resp. $X=\mathbb P(\cE)=\mathbb P_S^{n-1}$); il est clair""",
    RESP + " Semicolon after the parenthesis in the print.")
add(450, "paragraph 'Lorsque', last sentence",
    "provient de l'endomorphisme de l'Algèbre O_S[T_1,...,T_n] (capital A)",
    r"""de l'algèbre $\OO_S[T_1,\ldots,T_n]$""",
    "word", "high",
    r"""de l'algèbre $\OO_S""",
    r"""de l'Algèbre $\OO_S""",
    "Capital A as the print (as p. 449).")
add(450, "paragraph 'Considérons maintenant'",
    "affine de type fini (resp. projectif) sur S ,défini",
    r"""de type fini, respectivement projectif, sur $S$""",
    "word", "high",
    r"""de type fini, respectivement projectif, sur $S$""",
    r"""de type fini (resp. projectif) sur $S$""",
    RESP)
add(450, "paragraph 'Considérons maintenant'",
    "défini par un Idéal (resp. un Idéal homogène) J ⊂ O_S[T_1,...,T_n] . (capital I twice; nothing after the parenthesis)",
    r"""par un idéal, respectivement un idéal homogène,""",
    "word", "high",
    r"""par un idéal, respectivement un idéal homogène,""",
    r"""par un Idéal (resp. un Idéal homogène)""",
    RESP + " The edit also restores the print's capital I of Idéal (twice) and drops the comma the TeX adds before the display.")
add(450, "'Ainsi X = Spec(A) ...'",
    "Ainsi X = Spec(A)  (resp. = Proj(A)) où A = ... : no second 'X' inside the parenthesis",
    r"""$, respectivement $X=\Proj(\mathcal{A})$, où""",
    "word", "high",
    r"""$, respectivement $X=\Proj(\mathcal{A})$, où""",
    r"""$ (resp. $=\Proj(\mathcal{A})$) où""",
    RESP + " The TeX also adds 'X'.")
add(450, "display A = O_S[T_1,...,T_n]/J and the next words",
    "où A = O_S[T_1,...,T_n]/J ; on voit que (semicolon, small o)",
    r"""\mathcal{A}=\OO_S[T_1,\ldots,T_n]/\JJ.<NL>\]<NL>On voit que""",
    "punctuation", "high",
    r"""/\JJ.<NL>\]<NL>On voit que""",
    r"""/\JJ;<NL>\]<NL>on voit que""",
    "The TeX has a full stop and a new sentence for the print's semicolon.")
JNOTE = ("The print tells the two ideals apart by the letter, not by a prime: a second hand-drawn script J with a loop "
         "at the foot, three times on this page (this display, 'où J' est l'image', 'l'Idéal J' se déduit'), against "
         "the J with a top bar of the given ideal; the TeX writes \\JJ' in all three. \\mathscr{J} (mathrsfs is loaded "
         "in the preamble) gives a distinct script J. Apply the three edits together.")
add(450, "display A^(p) ≃ O_S[T_1,...,T_n]/J'",
    "the quotient is by a second hand-drawn script J with a loop at the foot, without prime (checked at 2.5x)",
    r"""\OO_S[T_1,\ldots,T_n]/\JJ'""",
    "symbol", "medium",
    r"""]/\JJ'""",
    r"""]/\mathscr{J}""",
    JNOTE)
add(450, "end of the same display",
    ".../J'  (nothing after it), then 'où J' est l'image'",
    r"""/\JJ',""",
    "punctuation", "high",
    r""",<NL>\]<NL>où""",
    r"""<NL>\]<NL>où""",
    "The TeX adds a comma at the end of the display. The old starts at the comma, so it does not overlap the letter edit before it.")
add(450, "'où J' est l'image dans ...'",
    "où J' est l'image : the same looped script J, no prime",
    r"""où $\JJ'$ est l'image""",
    "symbol", "medium",
    r"""$\JJ'$ est l'image""",
    r"""$\mathscr{J}$ est l'image""",
    JNOTE)
add(450, "'l'Idéal J' se déduit de J'",
    "l'Idéal (capital I)",
    r"""l'idéal $\JJ'$ se déduit""",
    "word", "high",
    r"""l'idéal $""",
    r"""l'Idéal $""",
    "As p. 446. The old ends before \\JJ', so it does not overlap the letter edit after it.")
add(450, "'l'Idéal J' se déduit de J'",
    "l'Idéal J' se déduit : the same looped script J, no prime",
    r"""l'idéal $\JJ'$ se déduit""",
    "symbol", "medium",
    r"""\JJ'$ se déduit""",
    r"""\mathscr{J}$ se déduit""",
    JNOTE)
add(450, "last line",
    "on a X^(p) = Spec(A^(p))  (resp. Proj(A^(p))) et le morphisme",
    r"""$, respectivement $\Proj(\mathcal{A}^{(p)})$, et le""",
    "word", "high",
    r"""$, respectivement $\Proj(\mathcal{A}^{(p)})$, et le""",
    r"""$ (resp. $\Proj(\mathcal{A}^{(p)})$) et le""",
    RESP)

# ---------------- filed under page 451 (printed on p. 450) ----------------
add(451, "head of page_451.tex, printed at the end of p. 450: 'des \"coordonnées\" T_i'",
    "à la puissance p -ième des \"coordonnées\" T_i (straight quotes)",
    r"""des coordonnées $T_i$""",
    "punctuation", "high",
    r"""des coordonnées $T_i$""",
    r"""des ``coordonnées'' $T_i$""",
    "Printed on p. 450; filed under p. 451 because the text stands in page_451.tex until the folio-451 marker is moved (marker item of p. 450): apply before the move. The TeX drops the quotes (``...'' as elsewhere in the exposé). Batch 451-455 may report the same text: apply once.")
add(451, "head of page_451.tex, printed at the end of p. 450: last words of the sentence",
    "(qui détermine un morphisme A^(p) --> A ).",
    r"""$T_i$, ce qui détermine un morphisme $\mathcal{A}^{(p)}\to\mathcal{A}$.""",
    "word", "high",
    r""", ce qui détermine un morphisme $\mathcal{A}^{(p)}\to\mathcal{A}$.""",
    r""" (qui détermine un morphisme $\mathcal{A}^{(p)}\to\mathcal{A}$).""",
    "The print has the parenthesis '(qui détermine ...)'; the TeX adds 'ce' and replaces the parentheses by a comma. Filed under p. 451 as the item before: apply before the marker move.")

# ---------------- checks ----------------
ok = True
texts = {p: open(f, encoding="utf-8", newline="").read() for p, f in PAGEFILE.items()}
spans = {}
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    t = texts[d["page"]]
    old = d["fix"]["old"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE", n, i, d["page"], repr(old))
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in d["fix"]["new"]:
        ok = False
        print("MARKER IN FIX", i)
    k = t.find(old)
    spans.setdefault(d["page"], []).append((k, k + len(old), i))
for p, ss in spans.items():
    ss.sort()
    for a, b in zip(ss, ss[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP page", p, a, b)
# apply all fixes of each page in order
for p, t in texts.items():
    for d in F:
        if d["page"] != p or d["fix"] is None:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        if t.count(old) != 1:
            ok = False
            print("SEQUENTIAL FAIL", p, repr(old))
        t = t.replace(old, new, 1)
    open(rf"{RUN}\crops_446_450\applied_{p}.tex", "w", encoding="utf-8", newline="").write(t)
    if t.count("{") != t.count("}"):
        ok = False
        print("BRACES", p, t.count("{"), t.count("}"))
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in sorted(texts):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("total", len(F), "ok" if ok else "PROBLEMS")
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
