import json, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/"
PAGES = BASE + r"b451_455/page_%d.tex"
OUT = BASE + r"findings_451_455.json"
NL = "<NL>"

def nl(s):
    return None if s is None else s.replace(NL, "\n")

F = []
def add(page, where, scan, tex, kind, conf, old=None, new=None, note="", corrected=None, after=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_after"] = after
    F.append(d)

UL_NOTE = r"""Exposé XV: the statement environment has no underline markup; \emph is the file's command for the print's underline (as for the statements of Exposé VII, pp. 301-317, and \emph{(Transitivité.)} on p. 445). Formulas and punctuation are not underlined in the print."""

# ---------------- page 451 ----------------
add(451, "start of page, before the heading n°4",
    r"""p. 451 begins with the heading 'n°4. Morphisme de Frobenius itéré ; préschémas parfaits.'""",
    r"""page_451.tex begins with 'morphisme de Frobenius \[\Fr_{X/S}:X\longrightarrow X^{(p)}\] est défini par l'élévation à la puissance $p$-ième des coordonnées $T_i$, ce qui détermine un morphisme $\mathcal{A}^{(p)}\to\mathcal{A}$.' (end of n°3, printed on p. 450)""",
    "marker", "high",
    note=r"""The folio-451 marker belongs just before '\subsubsection*{n\textsuperscript{o} 4. Morphisme de Frobenius itéré...'; the lines above it are the end of p. 450.""")
add(451, "heading n°4",
    r"""n°4. Morphisme de Frobenius itéré ; préschémas parfaits.""",
    r"""\subsubsection*{n\textsuperscript{o} 4. Morphisme de Frobenius itéré; préschémas parfaits}""",
    "punctuation", "high", r"""préschémas parfaits}""", r"""préschémas parfaits.}""",
    "The underlined title ends with a full stop in the print.")
add(451, "first paragraph of n°4, 'se factorise (d'une manière unique) en un S-morphisme'",
    r"""se factorise (d'une manière unique) en un S -morphisme""",
    r"""se factorise, d'une manière unique, en un $S$-morphisme""",
    "punctuation", "high", r"""se factorise, d'une manière unique, en un""", r"""se factorise (d'une manière unique) en un""",
    "Parentheses in the print, commas in the TeX.")
add(451, "'suivi de la projection : X^(p^ν/S) --> X (cf. n°2)'",
    r"""suivi de la projection : X^(p^ν/S) --> X""",
    r"""suivi de la projection $X^{(p^\nu/S)}\to X$""",
    "punctuation", "high", r"""la projection $X""", r"""la projection : $X""",
    "The print has a colon after 'projection'.")
add(451, "display Fr^ν_{X/S} = (Fr^{ν-1}_{X/S})^(p) o Fr_{X/S}",
    r"""... o Fr_{X/S} with no punctuation; the next line begins 'modulo l'identification'""",
    r"""\Fr_{X/S}^\nu=(\Fr_{X/S}^{\nu-1})^{(p)}\circ\Fr_{X/S},""",
    "punctuation", "high", r"""\circ\Fr_{X/S},<NL>\]""", r"""\circ\Fr_{X/S}<NL>\]""",
    "Comma added at the end of the display.")
add(451, "Définition 4, statement",
    r"""underlined: 'On dit qu'un préschéma' | 'de caractéristique' | 'est' / 'parfait si' | 'est un automorphisme de' (S, p, fr_S and the final 'S .' not); 'parfait' has a second underline (the defined term)""",
    r"""On dit qu'un préschéma $S$ de caractéristique $p$ est parfait si $\fr_S$ est un automorphisme de $S$. (no underline markup)""",
    "underline", "high",
    r"""On dit qu'un préschéma $S$ de caractéristique $p$ est parfait si $\fr_S$ est un automorphisme de $S$.""",
    r"""\emph{On dit qu'un préschéma} $S$ \emph{de caractéristique} $p$ \emph{est \underline{parfait} si} $\fr_S$ \emph{est un automorphisme de} $S$.""",
    UL_NOTE + r""" The doubly underlined defined term is given as \underline inside the \emph (volume decision).""")
add(451, "'au moyen du morphisme fr_S^{-1} o g : X --> S où g est'",
    r"""fr_S^{-1}og : X --> S  où  g  est le morphisme structural (no comma)""",
    r"""$\fr_S^{-1}\circ g:X\to S$, où $g$""",
    "punctuation", "high", r"""g:X\to S$, où""", r"""g:X\to S$ où""",
    "Comma added.")
add(451, "'modulo cette identification Fr_{X/S} = fr_X .'",
    r"""modulo cette identification  Fr_{X/S} = fr_X .""",
    r"""modulo cette identification, $\Fr_{X/S}=\fr_X$.""",
    "punctuation", "high", r"""modulo cette identification, $""", r"""modulo cette identification $""",
    "Comma added.")
add(451, "'S = Spec(F_q) où q = p^ν'",
    r"""S = Spec(F_q)  où  q = p^ν""",
    r"""$S=\Spec(\mathbb F_q)$, où $q=p^\nu$""",
    "punctuation", "high", r"""\Spec(\mathbb F_q)$, où""", r"""\Spec(\mathbb F_q)$ où""",
    "Comma added.")
add(451, "'en effet dans ce cas fr^ν_S = id_S'",
    r"""en effet dans ce cas""",
    r"""en effet, dans ce cas""",
    "punctuation", "high", r"""en effet, dans ce cas""", r"""en effet dans ce cas""",
    "Comma added.")
add(451, "last display of page_451.tex, 'X^(p^ν/S) = X et Fr^ν_{X/S} = fr^ν_X .' (printed at the top of p. 452)",
    r"""que  X^(p^ν/S) = X  et  Fr^ν_{X/S} = fr^ν_X .""",
    r"""X^{(p^\nu/S)}=X, \qquad \Fr_{X/S}^\nu=\fr_X^\nu.""",
    "word", "high", r"""X^{(p^\nu/S)}=X,<NL>\qquad""", r"""X^{(p^\nu/S)}=X<NL>\quad\text{et}\quad""",
    "The print joins the two formulas with 'et'; the TeX has a comma. This text sits under the folio-451 marker but is printed on p. 452 (marker finding of p. 452).")

# ---------------- page 452 ----------------
add(452, "start of page",
    r"""p. 452 begins with 'que X^(p^ν/S) = X et Fr^ν_{X/S} = fr^ν_X . Notons que pour ν = 1 ...'; p. 451 ends with '... Si X est un S -préschéma, on voit'""",
    r"""page_452.tex begins with 'Notons que pour $\nu=1$'; 'que \[X^{(p^\nu/S)}=X, \qquad \Fr_{X/S}^\nu=\fr_X^\nu.\]' is the end of page_451.tex""",
    "marker", "high",
    note=r"""The folio-452 marker belongs between 'on voit' and 'que' in the last paragraph of page_451.tex (before 'que' + the display 'X^{(p^\nu/S)}=X,').""")
add(452, "'on obtient S = Spec(F_p) pour lequel fr_S = id_S'",
    r"""S = Spec(F_p)  pour lequel""",
    r"""$S=\Spec(\mathbb F_p)$, pour lequel""",
    "punctuation", "high", r"""\Spec(\mathbb F_p)$, pour lequel""", r"""\Spec(\mathbb F_p)$ pour lequel""",
    "Comma added.")
add(452, "heading § 2",
    r"""§ 2. CORRESPONDANCE DE FROBENIUS. (capitals, underlined)""",
    r"""\subsection*{§ 2. Correspondance de Frobenius}""",
    "word", "high", r"""§ 2. Correspondance de Frobenius""", r"""§ 2. CORRESPONDANCE DE FROBENIUS""",
    "The print types the § heading in capitals. The TeX also sets § 1 (p. 442) and § 3 (p. 461) in small letters (not checked here against the print).")
add(452, "heading § 2, final full stop",
    r"""FROBENIUS.""",
    r"""...de Frobenius}""",
    "punctuation", "high", r"""}<NL><NL>\subsubsection*{n""", r""".}<NL><NL>\subsubsection*{n""",
    "The underlined title ends with a full stop in the print. Kept apart from the capitals edit (no overlap).")
add(452, "heading n°1",
    r"""n°1. Définition.""",
    r"""\subsubsection*{n\textsuperscript{o} 1. Définition}""",
    "punctuation", "high", r"""Définition}""", r"""Définition.}""",
    "The underlined title ends with a full stop in the print.")
add(452, "display F(Fr_{U/X}) : fr_{X*}(F)(U) --> F(U)",
    r"""F(Fr_{U/X}) : fr_{X*}(F)(U) --> F(U)  visiblement (no comma)""",
    r"""F(\Fr_{U/X}):\fr_{X*}(F)(U)\longrightarrow F(U),""",
    "punctuation", "high", r"""\longrightarrow F(U),<NL>\]""", r"""\longrightarrow F(U)<NL>\]""",
    "Comma added at the end of the display.")
add(452, "'visiblement fonctoriellement en U'",
    r"""visiblement fonctoriellement en U""",
    r"""visiblement fonctorielle en $U$""",
    "word", "high", r"""visiblement fonctorielle en""", r"""visiblement fonctoriellement en""",
    "The print has the adverb ('définit une application ... visiblement fonctoriellement en U', modifying 'définit'); the TeX silently changes it to the adjective.")
add(452, "'il en résulte que le morphisme précédent (fr_X)_*(F) --> F est un isomorphisme'",
    r"""que le morphisme précédent  (fr_X)_*(F) --> F  est un isomorphisme ;""",
    r"""que le morphisme précédent est un isomorphisme.""",
    "missing", "high", r"""morphisme précédent est""", r"""morphisme précédent $(\fr_X)_*(F)\to F$ est""",
    "The formula after 'précédent' is missing in the TeX.")
add(452, "'est un isomorphisme ; dans le cas où'",
    r"""est un isomorphisme ;  dans le cas où ('isomorphisme' underlined; semicolon; small d)""",
    r"""est un isomorphisme. Dans le cas où""",
    "underline", "high", r"""isomorphisme. Dans le cas""", r"""\emph{isomorphisme}; dans le cas""",
    "'isomorphisme' is underlined; the print also continues with ';' and a small 'dans' where the TeX starts a new sentence (one edit, as the two touch).")
add(452, "'(..., Λ anneau de base donné) cet isomorphisme'",
    r"""Λ anneau de base donné) cet isomorphisme (no comma)""",
    r"""$\Lambda$ anneau de base donné), cet isomorphisme""",
    "punctuation", "high", r"""donné), cet""", r"""donné) cet""",
    "Comma added.")

# ---------------- page 453 ----------------
add(453, "start of page",
    r"""p. 453 begins with '(fr_X)^* est adjoint à gauche du foncteur (fr_X)_* , un morphisme'; p. 452 ends with 'de cet isomorphisme définit, puisque'""",
    r"""page_453.tex begins with 'adjoint à gauche'; '$(\fr_X)^*$ est' is the end of page_452.tex""",
    "marker", "high",
    note=r"""The folio-453 marker belongs between 'puisque' and '$(\fr_X)^*$ est' at the end of page_452.tex.""")
add(453, "'(§ 1 n°2, prop. 2a)) les foncteurs'",
    r"""(§ 1 n°2, prop. 2a)) les foncteurs (no comma)""",
    r"""(§ 1 n$^\circ$2, prop. 2a)), les foncteurs""",
    "punctuation", "high", r"""prop. 2a)), les""", r"""prop. 2a)) les""",
    "Comma added.")
add(453, "Définition 1, statement",
    r"""underlined: 'Etant donnés un préschéma' | 'de caractéristique' | 'et un faisceau d'ensembles' | 'sur' | 'on appelle correspondance' / 'de Frobenius sur' | 'le couple' | 'formé de l'endomor-' / 'phisme de Frobenius' | 'de' | 'et de l'isomorphisme' (X, p, F, X_ét, (X,F), (fr_X,Fr^*_{F/X}), fr_X, X and the display not); 'correspondance' / 'de Frobenius' have a second underline (the defined term)""",
    r"""Étant donnés un préschéma $X$ ... et de l'isomorphisme (no underline markup)""",
    "underline", "high",
    r"""Étant donnés un préschéma $X$ de caractéristique $p$ et un faisceau d'ensembles $F$ sur $X_{\et}$, on appelle correspondance de Frobenius sur $(X,F)$ le couple $(\fr_X,\Fr^*_{F/X})$ formé de l'endomorphisme de Frobenius $\fr_X$ de $X$ et de l'isomorphisme""",
    r"""\emph{Étant donnés un préschéma} $X$ \emph{de caractéristique} $p$ \emph{et un faisceau d'ensembles} $F$ \emph{sur} $X_{\et}$, \emph{on appelle \underline{correspondance de Frobenius} sur} $(X,F)$ \emph{le couple} $(\fr_X,\Fr^*_{F/X})$ \emph{formé de l'endomorphisme de Frobenius} $\fr_X$ \emph{de} $X$ \emph{et de l'isomorphisme}""",
    UL_NOTE + r""" The doubly underlined defined term is given as \underline inside the \emph, as in Définition 4 (p. 451).""")
add(453, "'F est représentable par un préschéma V'",
    r"""'représentable' underlined""",
    r"""est représentable par""",
    "underline", "high", r"""est représentable par""", r"""est \emph{représentable} par""",
    "")
add(453, "'alors fr^*_X(F) = V^(p/X)'",
    r"""fr^*_X(F) = V^(p/X) (no parentheses around fr_X)""",
    r"""$(\fr_X)^*(F)=V^{(p/X)}$""",
    "formula", "high", r"""alors $(\fr_X)^*(F)=V^{(p/X)}$""", r"""alors $\fr_X^*(F)=V^{(p/X)}$""",
    "")
add(453, "'Fr_{X*}(F)(V) = F(V^(p/X)) = Hom_X(V^(p/X),V)'",
    r"""Fr_{X*}(F)(V): the star is typed after the subscript X, at the subscript level (direct image), not raised""",
    r"""(\fr_X)^*(F)(V)""",
    "formula", "high", r"""(\fr_X)^*(F)(V)""", r"""\fr_{X*}(F)(V)""",
    "The print has the direct image (as on p. 452: (fr_X)_*(F)(U) = F(U^(p/X))); the TeX's inverse image (\\fr_X)^* is another formula. Apply before the misprint edit that follows.")
add(453, "same formula, the letters Fr of Fr_{X*}",
    r"""capital Fr (double underline), as in Fr_{U/X}""",
    r"""\fr_{X*}(F)(V) (after the preceding edit)""",
    "misprint_in_print", "medium", r"""\fr_{X*}(F)(V)""", r"""\Fr_{X*}(F)(V)""",
    "The direct image by the Frobenius endomorphism fr_X is meant (cf. p. 452 and F(V^(p/X)) on the right); the typist wrote a capital F. The TeX writes small \\fr (silent correction). 'old' is taken from the text after the preceding formula edit.",
    corrected=r"""\fr_{X*}(F)(V)""", after=-1)
add(453, "display ending 'Hom_X(V^(p/X),V) et F(Fr_{V/X})'",
    r"""Hom_X(V^(p/X),V)  et (no comma)""",
    r"""\Hom_X(V^{(p/X)},V),""",
    "punctuation", "high", r"""\Hom_X(V^{(p/X)},V),<NL>\]""", r"""\Hom_X(V^{(p/X)},V)<NL>\]""",
    "Comma added at the end of the display.")
add(453, "'pour F = V étale sur X on a : Fr^*_{V/X} = (Fr_{V/X})^{-1}'",
    r"""on a : Fr^*_{V/X} = (Fr_{V/X})^{-1} .""",
    r"""on a \[ \Fr^*_{V/X}=(\Fr_{V/X})^{-1}. \]""",
    "punctuation", "high", r"""étale sur $X$ on a<NL>""", r"""étale sur $X$ on a :<NL>""",
    "Colon missing.")

# ---------------- page 454 ----------------
add(454, "'si le faisceau F est constant il est clair que'",
    r"""'constant' underlined""",
    r"""est constant il""",
    "underline", "high", r"""est constant il""", r"""est \emph{constant} il""",
    "")
add(454, "'fr^*_X(F) = F et Fr^*_{F/X} = id_F .'",
    r"""fr^*_X(F) = F (no parentheses around fr_X)""",
    r"""(\fr_X)^*(F)=F""",
    "formula", "high", r"""(\fr_X)^*(F)=F""", r"""\fr_X^*(F)=F""",
    "")
add(454, "same line, 'et'",
    r"""fr^*_X(F) = F  et  Fr^*_{F/X} = id_F .""",
    r"""(\fr_X)^*(F)=F, \qquad \Fr^*_{F/X}=\id_F.""",
    "word", "high", r""",<NL>\qquad<NL>\Fr^*_{F/X}=\id_F""", r"""<NL>\quad\text{et}\quad<NL>\Fr^*_{F/X}=\id_F""",
    "The print joins the two formulas with 'et'; the TeX has a comma.")
add(454, "Proposition 1 a), first sentence",
    r"""underlined: 'L'isomorphisme' | 'dépend fonctoriellement du faisceau' | 'autrement dit on a un isomorphisme fonctoriel' (Fr^*_{F/X}, 'F ;' and the display not)""",
    r"""no underline markup""",
    "underline", "high",
    r"""\item L'isomorphisme $\Fr^*_{F/X}$ dépend fonctoriellement du faisceau $F$; autrement dit on a un isomorphisme fonctoriel""",
    r"""\item \emph{L'isomorphisme} $\Fr^*_{F/X}$ \emph{dépend fonctoriellement du faisceau} $F$; \emph{autrement dit on a un isomorphisme fonctoriel}""",
    UL_NOTE)
add(454, "Proposition 1 a), '(où X̃_ét est la catégorie des faisceaux d'ensembles sur X_ét).'",
    r"""(où X̃_ét est la catégorie des faisceaux d'ensembles sur X_ét). in parentheses; 'où' and 'est la catégorie des faisceaux d'ensembles sur' underlined""",
    r"""où $\widetilde X_{\et}$ est la catégorie des faisceaux d'ensembles sur $X_{\et}$.""",
    "punctuation", "high",
    r"""où $\widetilde X_{\et}$ est la catégorie des faisceaux d'ensembles sur $X_{\et}$.""",
    r"""(\emph{où} $\widetilde X_{\et}$ \emph{est la catégorie des faisceaux d'ensembles sur} $X_{\et}$).""",
    "The TeX drops the parentheses; the edit also adds the statement's underline for these words.")
add(454, "Proposition 1 b), up to 'des faisceaux'",
    r"""underlined: 'La correspondance de Frobenius' | 'sur' | 'est' / 'compatible avec le changement de la base' | 'C'est-à-dire que, si' / 'désigne la catégorie fibrée sur' | 'des faisceaux (pour la' ((fr_X,Fr^*_{F/X}), (X,F), 'X .', the script F, (Sch)_p not)""",
    r"""no underline markup""",
    "underline", "high",
    r"""\item La correspondance de Frobenius $(\fr_X,\Fr^*_{F/X})$ sur $(X,F)$ est compatible avec le changement de la base $X$. C'est-à-dire que, si $\mathcal F$ désigne la catégorie fibrée sur $(\Sch)_p$ des faisceaux""",
    r"""\item \emph{La correspondance de Frobenius} $(\fr_X,\Fr^*_{F/X})$ \emph{sur} $(X,F)$ \emph{est compatible avec le changement de la base} $X$. \emph{C'est-à-dire que, si} $\mathcal F$ \emph{désigne la catégorie fibrée sur} $(\Sch)_p$ \emph{des faisceaux}""",
    UL_NOTE)
add(454, "Proposition 1 b), 'des faisceaux (pour la topologie étale) sur des préschémas'",
    r"""des faisceaux (pour la topologie étale) sur (parentheses; underlined)""",
    r"""des faisceaux, pour la topologie étale, sur des""",
    "punctuation", "high", r""", pour la topologie étale, """, r""" (\emph{pour la topologie étale}) """,
    "Parentheses in the print, commas in the TeX; the edit also adds the underline of these words.")
add(454, "Proposition 1 b), 'sur des préschémas de caractéristique p variables, les foncteurs'",
    r"""underlined: 'sur des préschémas de caractéristique' | 'variables' | 'les foncteurs' (p not)""",
    r"""no underline markup""",
    "underline", "high", r"""sur des préschémas de caractéristique $p$ variables, les foncteurs""",
    r"""\emph{sur des préschémas de caractéristique} $p$ \emph{variables}, \emph{les foncteurs}""",
    "")
add(454, "Proposition 1 b), 'les foncteurs fr^*_X (X ∈ Ob(Sch)_p) définissent'",
    r"""fr^*_X (X ∈ Ob(Sch)_p) définissent""",
    r"""$\fr_X^*$, $X\in\Ob(\Sch)_p$, définissent""",
    "punctuation", "high", r"""_X^*$, $X\in\Ob(\Sch)_p$, """, r"""_X^*$ ($X\in\Ob(\Sch)_p$) """,
    "Parentheses in the print, commas in the TeX.")
add(454, "Proposition 1 b), 'définissent un (Sch)_p -foncteur cartésien'",
    r"""underlined: 'définissent un' | 'foncteur' / 'cartésien' ((Sch)_p not)""",
    r"""no underline markup""",
    "underline", "high", r"""définissent un $(\Sch)_p$-foncteur cartésien""",
    r"""\emph{définissent un} $(\Sch)_p$-\emph{foncteur cartésien}""",
    "")
add(454, "Proposition 1 b), 'fr^* : F --- F' (script F)",
    r"""three dashes without an arrowhead between the two script F (the other arrows of the page are typed -->)""",
    r"""\fr^*: \mathcal F\longrightarrow\mathcal F,""",
    "misprint_in_print", "medium", r"""\mathcal F\longrightarrow\mathcal F""", r"""\mathcal F\relbar\joinrel\relbar\mathcal F""",
    "The typist left out the '>' of the arrow: the dashes are sharp and no trace of a head is visible, so not a defect of the scan. The TeX silently corrects.",
    corrected=r"""\mathcal F\longrightarrow\mathcal F""")
add(454, "Proposition 1 b), 'et les morphismes'",
    r"""underlined""",
    r"""no underline markup""",
    "underline", "high", r"""et les morphismes""", r"""\emph{et les morphismes}""",
    "")
add(454, "Proposition 1 b), 'Fr^*_{F/X} (X ∈ Ob(Sch)_p , F ∈ Ob X̃_ét) définissent'",
    r"""Fr^*_{F/X} (X ∈ Ob(Sch)_p , F ∈ Ob X̃_ét) définissent""",
    r"""$\Fr^*_{F/X}$, $X\in\Ob(\Sch)_p$, $F\in\Ob\widetilde X_{\et}$, définissent""",
    "punctuation", "high", r"""_{F/X}$, $X\in\Ob(\Sch)_p$, $F\in\Ob\widetilde X_{\et}$, """,
    r"""_{F/X}$ ($X\in\Ob(\Sch)_p$, $F\in\Ob\widetilde X_{\et}$) """,
    "Parentheses in the print, commas in the TeX.")
add(454, "Proposition 1 b), 'définissent un (Sch)_p -morphisme fonctoriel'",
    r"""underlined: 'définissent un' | 'morphisme fonctoriel' ((Sch)_p not)""",
    r"""no underline markup""",
    "underline", "high", r"""définissent un $(\Sch)_p$-morphisme fonctoriel""",
    r"""\emph{définissent un} $(\Sch)_p$-\emph{morphisme fonctoriel}""",
    "")
add(454, "Proposition 1 b), end: '(qui est un isomorphisme).'",
    r"""Fr^*_/ : fr^* --> id_F  (qui est un isomorphisme). in parentheses, the words underlined""",
    r"""\] qui est un isomorphisme.""",
    "punctuation", "high", r"""\]<NL>qui est un isomorphisme.""", r"""\]<NL>(\emph{qui est un isomorphisme}).""",
    "The TeX drops the parentheses; the edit also adds the underline.")
add(454, "Proposition 1 c)",
    r"""underlined: 'Inversement ces propriétés caractérisent' | 'c'est-à-' / 'dire qu'il existe un' | 'morphisme fonctoriel et un seul de' | 'dans' (Fr^*_/, (Sch)_p, fr^*, id_F not)""",
    r"""no underline markup""",
    "underline", "high",
    r"""\item Inversement ces propriétés caractérisent $\Fr^*_{/}$, c'est-à-dire qu'il existe un $(\Sch)_p$-morphisme fonctoriel et un seul de $\fr^*$ dans $\id_{\mathcal F}$.""",
    r"""\item \emph{Inversement ces propriétés caractérisent} $\Fr^*_{/}$, \emph{c'est-à-dire qu'il existe un} $(\Sch)_p$-\emph{morphisme fonctoriel et un seul de} $\fr^*$ \emph{dans} $\id_{\mathcal F}$.""",
    "")
add(454, "Proposition 1 b): 'X ∈ Ob(Sch)_p' (twice) and 'F ∈ Ob X̃_ét'",
    r"""Ob with a capital O (three places)""",
    r"""\Ob, which prints 'ob': \providecommand{\Ob}{\operatorname{ob}} (s5.tex line 101) wins over the later \providecommand{\Ob}{\operatorname{Ob}} (lines 226, 300)""",
    "word", "high",
    note=r"""Convention of the macro, reported once and not itemized (as for Exposé VIII, GLOBAL_ISSUES 12 Nov): redefine \Ob as \operatorname{Ob} for Exposé XV, or write \operatorname{Ob} at these three places.""")
add(454, "'ce dernier est tout-à-fait évident'",
    r"""tout-à-fait""",
    r"""tout à fait""",
    "punctuation", "high", r"""tout à fait évident""", r"""tout-à-fait évident""",
    "Hyphens in the print.")
add(454, "'posons F' = g^*(F) , et plus généralement affectons'",
    r"""F' = g^*(F) , et plus généralement affectons""",
    r"""$F'=g^*(F)$ et, plus généralement, affectons""",
    "punctuation", "high", r"""$F'=g^*(F)$ et, plus généralement, affectons""", r"""$F'=g^*(F)$, et plus généralement affectons""",
    "The print has one comma, before 'et'; the TeX has two, after 'et' and after 'généralement'.")
add(454, "'affectons d'un ' l'image inverse'",
    r"""d'un  '  l'image inverse (the prime sign itself)""",
    r"""d'un prime l'image inverse""",
    "word", "high", r"""d'un prime l'image""", r"""d'un $'$ l'image""",
    "The print types the sign ', the TeX writes the word 'prime'.")
add(454, "last display of page_454.tex (printed at the top of p. 455): fr^*_{X'}(F') = fr^*_{X'}(g^*(F)) = g^*(fr^*_X(F)) = (fr^*_X(F))' ,",
    r"""fr^*_{X'}(g^*(F)) = g^*(fr^*_X(F)) = (fr^*_X(F))'  , (arguments in parentheses; comma at the end)""",
    r"""\fr_{X'}^*(g^*F)=g^*(\fr_X^*F)=(\fr_X^*F)'""",
    "formula", "high", r"""\fr_{X'}^*(g^*F)=g^*(\fr_X^*F)=(\fr_X^*F)'""", r"""\fr_{X'}^*(g^*(F))=g^*(\fr_X^*(F))=(\fr_X^*(F))',""",
    "The TeX drops the parentheses of g^*(F) and fr^*_X(F) and the final comma. The display sits under the folio-454 marker but is printed on p. 455 (marker finding of p. 455).")

# ---------------- page 455 ----------------
add(455, "start of page",
    r"""p. 455 begins with the display 'fr^*_{X'}(F') = fr^*_{X'}(g^*(F)) = g^*(fr^*_X(F)) = (fr^*_X(F))' ,'; p. 454 ends with '... Comme g o fr_{X'} = fr_X o g , on a'""",
    r"""the display \[\fr_{X'}^*(F')=...\] is the end of page_454.tex; page_455.tex begins with 'd'où le'""",
    "marker", "high",
    note=r"""The folio-455 marker belongs after 'on a' in page_454.tex, before the display '\fr_{X'}^*(F')=...'.""")
add(455, "end of page",
    r"""p. 455 ends with '... on sait que F(U) s'identifie à Hom_U(U,F|U)'""",
    r"""page_455.tex continues ' et $\varphi_F(U):F(U)\to F(U)$ à l'application \[s\longmapsto ...\] où $s\in\Hom_U(U,F|U)$; comme le'""",
    "marker", "high",
    note=r"""The folio-456 marker belongs between the first '$\Hom_U(U,F|U)$' and ' et $\varphi_F(U)' (the text after it is printed on p. 456, not checked here).""")
add(455, "'Il reste à prouver que Fr^*_{F'/X'} = (Fr^*_{F/X})' ; en utilisant'",
    r"""(Fr^*_{F/X})'  ;  en utilisant (semicolon, small e)""",
    r"""(\Fr^*_{F/X})'. \] En utilisant""",
    "punctuation", "high", r"""(\Fr^*_{F/X})'.<NL>\]<NL>En utilisant""", r"""(\Fr^*_{F/X})';<NL>\]<NL>en utilisant""",
    "The print continues the sentence after a semicolon.")
add(455, "'par l'application bijective :'",
    r"""bijective :""",
    r"""par l'application bijective \[""",
    "punctuation", "high", r"""l'application bijective<NL>""", r"""l'application bijective :<NL>""",
    "Colon missing.")
add(455, "display Hom_{X'}(F', fr_{X'*}(F')) = Hom_{X'}(g^*(F), fr_{X'*}g^*(F)) ...",
    r"""Hom_{X'}(g^*(F),fr_{X'*}g^*(F))""",
    r"""\Hom_{X'}(g^*F,\fr_{X'*}g^*F)""",
    "formula", "high", r"""=\Hom_{X'}(g^*F,\fr_{X'*}g^*F)""", r"""=\Hom_{X'}(g^*(F),\fr_{X'*}g^*(F))""",
    "The TeX drops the parentheses of g^*(F).")
add(455, "same display, the isomorphism arrow",
    r"""an arrow with a tilde above it""",
    r"""\simeq""",
    "symbol", "high", r"""\simeq \Hom_X""", r"""\xrightarrow{\sim} \Hom_X""",
    "")
add(455, "same display, last term Hom_X(F, g_* fr_{X'*} g^*(F))",
    r"""g^*(F)""",
    r"""g^*F""",
    "formula", "high", r"""g^*F)<NL>\]<NL>($g^*$ adjoint""", r"""g^*(F))<NL>\]<NL>($g^*$ adjoint""",
    "")
add(455, "display Hom_X(F, fr_{X*}(F)) --> ...",
    r"""Hom_X(F,fr_{X*}(F))""",
    r"""\Hom_X(F,\fr_{X*}F)""",
    "formula", "high", r"""_{X*}F)\longrightarrow""", r"""_{X*}(F))\longrightarrow""",
    "")
add(455, "same display, Hom_X(F, fr_{X*}g_*g^*(F)) = Hom_X(F, g_* fr_{X'*} g^*(F))",
    r"""g^*(F) twice""",
    r"""g^*F twice""",
    "formula", "high", r"""\Hom_X(F,\fr_{X*}g_*g^*F)=<NL>\Hom_X(F,g_*\fr_{X'*}g^*F)""",
    r"""\Hom_X(F,\fr_{X*}g_*g^*(F))=<NL>\Hom_X(F,g_*\fr_{X'*}g^*(F))""",
    "")
add(455, "'définie par le morphisme d'adjonction : F --α--> g_*g^*(F)'",
    r"""d'adjonction : F""",
    r"""d'adjonction $F""",
    "punctuation", "high", r"""d'adjonction $F""", r"""d'adjonction : $F""",
    "Colon missing.")
add(455, "same formula, g_*g^*(F)",
    r"""g_*g^*(F)""",
    r"""g_*g^*F""",
    "formula", "high", r"""g_*g^*F$; autrement""", r"""g_*g^*(F)$; autrement""",
    "")
add(455, "display α o F(Fr_{/X}) = g_*(F'(Fr_{/X'})) o fr_{X*}(α)",
    r"""... o fr_{X*}(α)  c'est-à-dire (no comma)""",
    r"""\circ\fr_{X*}(\alpha),""",
    "punctuation", "high", r"""\circ\fr_{X*}(\alpha),<NL>\]""", r"""\circ\fr_{X*}(\alpha)<NL>\]""",
    "Comma added at the end of the display.")
add(455, "'c'est-à-dire que pour tout préschéma U étale sur X on a'",
    r"""c'est-à-dire que pour tout préschéma U étale sur X on a (no commas)""",
    r"""c'est-à-dire que, pour tout préschéma $U$ étale sur $X$, on a""",
    "punctuation", "high", r"""c'est-à-dire que, pour tout préschéma $U$ étale sur $X$, on a""",
    r"""c'est-à-dire que pour tout préschéma $U$ étale sur $X$ on a""",
    "Two commas added.")
add(455, "'un diagramme commutatif :'",
    r"""commutatif :""",
    r"""diagramme commutatif% FIX#59 ...""",
    "punctuation", "high", r"""diagramme commutatif%""", r"""diagramme commutatif :%""",
    "Colon missing.")
add(455, "diagram, label of the lower arrow",
    r"""F'(Fr_{U'/X'}) above the lower arrow (as F(Fr_{U/X}) above the upper one)""",
    r"""\arrow[r,"F'(\Fr_{U'/X'})"'] (label below the arrow)""",
    "other", "high", r"""\arrow[r,"F'(\Fr_{U'/X'})"']""", r"""\arrow[r,"F'(\Fr_{U'/X'})"]""",
    "The swap mark ' after the label sets it below the arrow; the print has it above.")
add(455, "'on se ramène en composant avec (Fr^*_/)^{-1} à prouver'",
    r"""on se ramène en composant avec (Fr^*_/)^{-1} à prouver (no commas)""",
    r"""on se ramène, en composant avec $(\Fr^*_{/})^{-1}$, à prouver""",
    "punctuation", "high", r"""on se ramène, en composant avec $(\Fr^*_{/})^{-1}$, à prouver""",
    r"""on se ramène en composant avec $(\Fr^*_{/})^{-1}$ à prouver""",
    "Two commas added.")
add(455, "'Or si φ est un (Sch)_p -endomorphisme'",
    r"""Or si""",
    r"""Or, si""",
    "punctuation", "high", r"""Or, si $\varphi$""", r"""Or si $\varphi$""",
    "Comma added.")

# ---------------- checks ----------------
texts = {}
for p in range(451, 456):
    b = open(PAGES % p, 'rb').read()
    assert b'\r' not in b, ("CR in", p)
    texts[p] = b.decode('utf-8')

ok = True
# 1) every independent fix: old occurs exactly once in the original page file
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    old = f["fix"]["old"]
    if f["_after"] is None:
        n = texts[f["page"]].count(old)
        if n != 1:
            ok = False
            print("NOT UNIQUE (%d):" % n, f["page"], repr(old))
    else:
        prev = F[i + f["_after"]]
        t2 = texts[f["page"]].replace(prev["fix"]["old"], prev["fix"]["new"], 1)
        n = t2.count(old)
        if n != 1:
            ok = False
            print("DEPENDENT NOT UNIQUE (%d):" % n, f["page"], repr(old))
        else:
            print("dependent ok (after the preceding edit):", f["page"], repr(old))
    if "\r" in old or "\r" in f["fix"]["new"]:
        ok = False; print("CR in fix", i)
    if any(ord(c) < 32 and c != "\n" for c in old + f["fix"]["new"]):
        ok = False; print("control char in fix", i, repr(old))

# 2) apply all fixes in order on each page; every old must be found exactly once at its turn
for p in range(451, 456):
    t = texts[p]
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        n = t.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL FAIL (%d):" % n, p, repr(f["fix"]["old"]))
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

# no fix touches a marker line
for f in F:
    if f["fix"] and "%%%%%%%%%%" in f["fix"]["old"]:
        ok = False; print("marker line in fix", f)

print("checks ok:", ok)
counts = {}
for f in F:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts, "total", len(F))

out = []
for f in F:
    d = {k: v for k, v in f.items() if k != "_after"}
    out.append(d)
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("written", OUT)
