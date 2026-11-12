import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5'
OUT = RUN + r'\findings_371_375.json'
F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


UL = ("Exposé X has no underline markup; \\emph is this file's command for the print's underline in "
      "statements (as in III B, V and VII). Formulas, numbers and the punctuation between the pieces are not "
      "underlined in the print.")
PLAIN_R = ("The derived-functor R is a typed plain R here (one stem, checked at 4-8x), while other R of the "
           "same pages are the hand-drawn double-struck R (\\R in this file is \\mathbb{R}).")

# ---------------- page 371 ----------------
add(371, "run-in label 'Exemples.' (first line)",
    "Exemples. typed plain, not underlined (checked at 2x)",
    r"\emph{Exemples.}", "underline", "high",
    r"\emph{Exemples.}", "Exemples.",
    "\\emph is this file's command for the print's underline; the label is not underlined. Exposé VIII sets "
    "its run-in labels in \\emph although the print leaves them plain (also 'Démonstration du lemme.', p. 367).")
add(371, "run-in label 'Remarques.'",
    "Remarques. typed plain, not underlined (checked at 2x)",
    r"\emph{Remarques.}", "underline", "high",
    r"\emph{Remarques.}", "Remarques.",
    "As 'Exemples.' above.")
add(371, "remark a), 'et par conséquent, on obtient'",
    "Λ ⊗_Z Z G   et par conséquent, on obtient un homomorphisme (no comma after 'et')",
    "et, par conséquent, on obtient", "punctuation", "high",
    "et, par conséquent,", "et par conséquent,",
    "The TeX adds a comma after 'et'.")
add(371, "end of remark a)",
    "d'un anneau Λ non-commutatif. (hyphen inside the line, not a line-break hyphen)",
    "non commutatif", "word", "high",
    "non commutatif", "non-commutatif",
    "")
add(371, "remark b), 'opère - qui ne s'explicite plus'",
    "a typewriter hyphen between spaces (same length as the hyphen of pro-préschéma)",
    "opère -- qui", "punctuation", "high",
    "opère -- qui", "opère - qui",
    "En dash for the print's hyphen.")
add(371, "remark b), 'sur un anneau - et le foncteur'",
    "a typewriter hyphen between spaces",
    "anneau -- et", "punctuation", "high",
    "anneau -- et", "anneau - et",
    "En dash for the print's hyphen.")
add(371, "end of remark b), 'cf SGA3 I 4.7.2).'",
    "', cf SGA3 I 4.7.2).': no full stop after cf (checked at 2.5x)",
    "cf. SGA 3 I 4.7.2).", "punctuation", "high",
    "cf. SGA", "cf SGA",
    "The TeX adds the abbreviation's full stop. The print also types 'SGA3' without a space (spacing, not changed).")
add(371, "heading 'Bibliographie.'",
    "Bibliographie. (small letters, underlined, then a full stop)",
    r"\subsection*{Bibliographie}", "punctuation", "high",
    r"\subsection*{Bibliographie}", r"\subsection*{Bibliographie.}",
    "Full stop after the underlined title, as the rule for underlined titles; the small letters are as printed.")
add(371, "[1], title 'Elements de Géométrie Algébrique'",
    "typed plain, not underlined",
    r"\emph{Elements de Géométrie Algébrique}", "underline", "high",
    r"\emph{Elements de Géométrie Algébrique}", "Elements de Géométrie Algébrique",
    "As the logged bibliography titles of pp. 54 and 72.")
add(371, "[2], title 'Catégories Dérivées'",
    "typed plain, not underlined",
    r"\emph{Catégories Dérivées}", "underline", "high",
    r"\emph{Catégories Dérivées}", "Catégories Dérivées",
    "As [1].")

# ---------------- page 372 ----------------
add(372, "exposé heading",
    "'Exposé X' alone (small letters, underlined); the title follows once, centred in capitals",
    r"\section*{Exposé X --- Formule d'Euler--Poincaré en cohomologie étale}", "extra", "high",
    r"\section*{Exposé X --- Formule d'Euler--Poincaré en cohomologie étale}", r"\section*{Exposé X}",
    "The heading repeats the title, which the print gives only in the centred capitals below (as "
    "'\\section*{Exposé VIII}'). The underline of 'Exposé X' is the accepted \\section* setting.")
add(372, "title 'FORMULE D'EULER-POINCARE EN COHOMOLOGIE ETALE'",
    "EULER-POINCARE with a hyphen",
    r"\textbf{FORMULE D'EULER--POINCARÉ EN COHOMOLOGIE ÉTALE}", "punctuation", "high",
    "EULER--POINCARÉ", "EULER-POINCARÉ",
    "En dash for the print's hyphen; the unaccented capitals are covered by the volume rule.")
add(372, "byline 'par A. GROTHENDIECK'",
    "surname in capitals",
    "par A. Grothendieck", "word", "high",
    "par A. Grothendieck", "par A. GROTHENDIECK",
    "As printed (as the logged bylines of Exposés V-VII, 'J. P. JOUANOLOU').")
add(372, "byline '(Rédigé par I.BUCUR)'",
    "(Rédigé par I.BUCUR): capital R, surname in capitals",
    "(rédigé par I. Bucur)", "word", "high",
    "(rédigé par I. Bucur)", "(Rédigé par I. BUCUR)",
    "The print has no space after 'I.' (spacing, not changed).")
add(372, "first paragraph, 'du type d'Euler-Poincaré'",
    "Euler-Poincaré with a hyphen",
    "du type d'Euler--Poincaré.", "punctuation", "high",
    "type d'Euler--Poincaré", "type d'Euler-Poincaré",
    "En dash for the print's hyphen.")
add(372, "second paragraph, 'La formule d'Euler-Poincaré utilise'",
    "Euler-Poincaré with a hyphen",
    "La formule d'Euler--Poincaré utilise", "punctuation", "high",
    "La formule d'Euler--Poincaré", "La formule d'Euler-Poincaré",
    "En dash for the print's hyphen.")
add(372, "section title 1",
    "1. Faisceaux sur un schéma à opérateurs. (underlined, then a full stop)",
    r"\subsection*{1. Faisceaux sur un schéma à opérateurs}", "punctuation", "high",
    "à opérateurs}", "à opérateurs.}",
    "Full stop after the underlined title dropped by the TeX.")
add(372, "'ou simplement \"faisceau sur (X_et , G)\" .'",
    "straight typewriter double quotes; subscript 'et' without accent (2.5x)",
    "« faisceau sur $(X_{\\et},G)$ »", "punctuation", "high",
    "« faisceau sur $(X_{\\et},G)$ »", "``faisceau sur $(X_{\\mathrm{et}},G)$''",
    "Guillemets for the print's straight quotes (written ``...'' in this file). One edit: it also writes the "
    "subscript 'et' without accent (accent: \\et is \\mathrm{\\acute{e}t}, s5.tex line 77), as the three "
    "other \\et places of pp. 372-373.")
add(372, "'un faisceau F ∈ Ob(X~_et)'",
    "Ob with a capital O (checked at 2.5x)",
    r"F\in \Ob(\widetilde X_{\et})", "word", "high",
    r"F\in \Ob(", r"F\in \operatorname{Ob}(",
    "\\Ob prints 'ob' in this file: the first \\providecommand (s5.tex line 101, \\operatorname{ob}) wins and "
    "line 226's \\operatorname{Ob} has no effect. Exposé X has 25 \\Ob.")
add(372, "'Ob(X~_et)', subscript",
    "subscript 'et' without accent (2.5x)",
    r"\widetilde X_{\et})", "accent", "high",
    r"\widetilde X_{\et})", r"\widetilde X_{\mathrm{et}})",
    "\\et prints 'ét' (s5.tex line 77); the typescript's subscript has no accent.")

# ---------------- page 373 ----------------
add(373, "condition a)",
    "a)   S_e = 1_F (no punctuation after the formula)",
    r"\text{a) }\quad S_e=1_F,", "punctuation", "high",
    "S_e=1_F,", "S_e=1_F",
    "Comma added at the end of the display.")
add(373, "condition b), 'le diagramme :'",
    "b) Pour g,h ∈ G, le diagramme :",
    "b) Pour $g,h\\in G$, le diagramme", "punctuation", "high",
    "le diagramme", "le diagramme :",
    "The colon before the diagram is missing.")
add(373, "diagram, right vertical arrow C_{h,g}(F)",
    "a vertical arrow with heads at both ends and the mark ≀ beside its shaft (checked at 4x); label C_{h,g}(F) on the right",
    "\\arrow[d,\"C_{h,g}(F)\"]", "symbol", "high",
    "\\arrow[d,\"C_{h,g}(F)\"]", "\\arrow[d,leftrightarrow,\"\\wr\"',\"C_{h,g}(F)\"]",
    "The TeX has a plain down arrow. (The bottom label h*(S_g) is printed above its arrow, the TeX sets it "
    "below: the volume decision of item 85 of the global list, not itemized.)")
add(373, "'C_{h,g}(F) : (hg)*(F) --> (h*g*)(F) est l'isomorphisme canonique'",
    "target written (h*g*)(F)",
    r"C_{h,g}(F):(hg)^*(F)\longrightarrow h^*(g^*(F))", "formula", "high",
    r"\longrightarrow h^*(g^*(F))", r"\longrightarrow (h^*g^*)(F)",
    "The diagram above has h*(g*(F)) as printed; this line has (h*g*)(F).")
add(373, "'on obtient une catégorie X~_{et,G} qui est un topos'",
    "subscript 'et,G' without accent (2.5x)",
    r"$\widetilde X_{\et,G}$ qui", "accent", "high",
    r"$\widetilde X_{\et,G}$ qui", r"$\widetilde X_{\mathrm{et},G}$ qui",
    "As p. 372.")
add(373, "'Un anneau A de X~_{et,G} étant donné'",
    "subscript 'et,G' without accent (2.5x)",
    r"de $\widetilde X_{\et,G}$ étant", "accent", "high",
    r"de $\widetilde X_{\et,G}$ étant", r"de $\widetilde X_{\mathrm{et},G}$ étant",
    "As p. 372.")
add(373, "'la catégorie abélienne des A-Modules'",
    "A-Modules with a capital M (checked at 2x)",
    "des $A$-modules", "word", "high",
    "des $A$-modules", "des $A$-Modules",
    "The typescript's capital M (Modules on the topos).")
add(373, "'le faisceau constant Λ_X associé à Λ d'une structure'",
    "no commas around 'associé à Λ'",
    "$\\Lambda_X$, associé à $\\Lambda$, d'une", "punctuation", "high",
    "$\\Lambda_X$, associé à $\\Lambda$, d'une", "$\\Lambda_X$ associé à $\\Lambda$ d'une",
    "Two commas added by the TeX.")
add(373, "last paragraph, 'dans [T] chap. V,'",
    "Tous les résultats démontrés dans [T] chap. V, peuvent",
    "dans [T], chap. V,", "punctuation", "high",
    "dans [T], chap. V,", "dans [T] chap. V,",
    "Comma after [T] added by the TeX.")

# ---------------- page 374 ----------------
add(374, "'Rappelons le résultat suivant de (SGA 4 XVII) :'",
    "reference in parentheses, then a colon",
    "Rappelons le résultat suivant de SGA 4 XVII.", "punctuation", "high",
    "suivant de SGA 4 XVII.", "suivant de (SGA 4 XVII) :",
    "")
add(374, "statement of Lemme 2.1",
    "underlined word group by word group: Soient / et / deux schémas et / un morphisme propre / avec / "
    "quasi-compact / Désignons par / un anneau de torsion / et soit / un complexe de faisceaux de / modules sur / "
    "de / alors / est de tor-dimension finie; 'tor-dimension finie (SGA 4 XVII)' on the third line is not underlined",
    "no underline", "underline", "high",
    "Soient $X$ et $Y$ deux schémas et $f:X\\to Y$ un morphisme propre, avec $Y$ quasi-compact. Désignons par $A$ "
    "un anneau de torsion, et soit $F^\\bullet$ un complexe de faisceaux de $A$-modules sur $X$ de tor-dimension "
    "finie (SGA 4 XVII); alors $\\R f_*(F^\\bullet)$ est de tor-dimension finie.",
    "\\emph{Soient} $X$ \\emph{et} $Y$ \\emph{deux schémas et} $f:X\\to Y$ \\emph{un morphisme propre}, "
    "\\emph{avec} $Y$ \\emph{quasi-compact}. \\emph{Désignons par} $A$ \\emph{un anneau de torsion}, "
    "\\emph{et soit} $F^\\bullet$ \\emph{un complexe de faisceaux de} $A$-\\emph{modules sur} $X$ \\emph{de} "
    "tor-dimension finie (SGA 4 XVII); \\emph{alors} $\\R f_*(F^\\bullet)$ \\emph{est de tor-dimension finie}.",
    UL)
add(374, "statement of Proposition 2.2, up to 'et librement sur V,'",
    "underlined: Soient / un schéma propre sur le corps / séparablement clos / un groupe fini opérant sur / "
    "un ouvert de / stable par / et tel que / opère de façon admissible / et librement sur",
    "no underline", "underline", "high",
    "Soient $X$ un schéma propre sur le corps $k$ séparablement clos, $G$ un groupe fini opérant sur $X$, $V$ un "
    "ouvert de $X$ stable par $G$ et tel que $G$ opère de façon admissible (SGA 1 V 1.7) et librement sur $V$,",
    "\\emph{Soient} $X$ \\emph{un schéma propre sur le corps} $k$ \\emph{séparablement clos}, $G$ \\emph{un groupe "
    "fini opérant sur} $X$, $V$ \\emph{un ouvert de} $X$ \\emph{stable par} $G$ \\emph{et tel que} $G$ "
    "\\emph{opère de façon admissible} (SGA 1 V 1.7) \\emph{et librement sur} $V$,",
    UL)
add(374, "Proposition 2.2, 'Λ = Z/ℓ^nZ  avec ℓ'",
    "no comma before 'avec'",
    "$\\Lambda=\\mathbb Z/\\ell^n\\mathbb Z$, avec", "punctuation", "high",
    "\\ell^n\\mathbb Z$,", "\\ell^n\\mathbb Z$",
    "Comma added by the TeX. Independent of the underline edits around it.")
add(374, "Proposition 2.2, from 'avec ℓ' to 'Désignons par'",
    "underlined: avec / un nombre premier différent de la caractéristique de / et / le faisceau constant sur / "
    "associé à / muni de sa structure triviale de faisceau à groupe / d'opérateurs / Désignons par",
    "no underline", "underline", "high",
    "avec $\\ell$ un nombre premier différent de la caractéristique de $k$, et $\\Lambda_V$ le faisceau constant "
    "sur $V$ associé à $\\Lambda$, muni de sa structure triviale de faisceau à groupe $G$ d'opérateurs. Désignons par",
    "\\emph{avec} $\\ell$ \\emph{un nombre premier différent de la caractéristique de} $k$, \\emph{et} "
    "$\\Lambda_V$ \\emph{le faisceau constant sur} $V$ \\emph{associé à} $\\Lambda$, \\emph{muni de sa structure "
    "triviale de faisceau à groupe} $G$ \\emph{d'opérateurs}. \\emph{Désignons par}",
    UL)
add(374, "Proposition 2.2, 'i : V --> X'",
    "a hooked arrow (V with a hook at the start of the arrow, checked at 2.5x)",
    "i:V\\longrightarrow X", "symbol", "high",
    "i:V\\longrightarrow X", "i:V\\hookrightarrow X",
    "")
add(374, "Proposition 2.2, from 'l'immersion de V' to 'Λ[G]-modules'",
    "underlined: l'immersion de / dans / et soit / Dans ces conditions le complexe de / modules; no comma after 'dans X'",
    "l'immersion de $V$ dans $X$, et soit ... $\\Lambda[G]$-modules (no underline)", "underline", "high",
    "l'immersion de $V$ dans $X$, et soit $\\Lambda_{V,X}=i_!(\\Lambda_V)$. Dans ces conditions le complexe de "
    "$\\Lambda[G]$-modules",
    "\\emph{l'immersion de} $V$ \\emph{dans} $X$ \\emph{et soit} $\\Lambda_{V,X}=i_!(\\Lambda_V)$. "
    "\\emph{Dans ces conditions le complexe de} $\\Lambda[G]$-\\emph{modules}",
    UL + " One edit: it also removes the comma after 'dans $X$' that the print does not have (punctuation).")
add(374, "Proposition 2.2, last words 'est un complexe parfait (VIII 7).'",
    "underlined: est un complexe parfait",
    "est un complexe parfait (VIII 7).", "underline", "high",
    "est un complexe parfait (VIII 7).", "\\emph{est un complexe parfait} (VIII 7).",
    UL)
add(374, "proof label",
    "Démonstration : (not underlined, then a colon)",
    "\\begin{prooftext}[Démonstration] (prints \\emph{Démonstration.})", "other", "high",
    "\\begin{prooftext}[Démonstration]\n", "Démonstration : ",
    "Apply together with the p. 375 edit that removes '\\end{prooftext}'. The environment (as redefined at "
    "s5.tex line 8465) prints the label in \\emph with a full stop; the print has 'Démonstration :' plain.")
add(374, "display 'RΓ_X(Λ_{V,X}) ≃ RΓ_X(Rp_*(Λ_{V,X}))', Rp_*",
    "Rp_*: a typed plain R",
    "\\R\\Gamma_Y(\\R p_*(\\Lambda_{V,X}))", "font", "high",
    "(\\R p_*(\\Lambda_{V,X}))", "(\\mathrm{R}p_*(\\Lambda_{V,X}))",
    PLAIN_R + " Here both R of RΓ are double-struck. Independent of the misprint edit of \\Gamma_Y (next item).")
add(374, "same display, index of the second Γ",
    "RΓ_X(Rp_*(Λ_{V,X})): the second Γ has the index X (clear at 2.5x)",
    "\\R\\Gamma_Y(\\R p_*(\\Lambda_{V,X}))", "misprint_in_print", "high",
    "\\Gamma_Y", "\\Gamma_X",
    "Rp_*(Λ_{V,X}) lives on Y, so Γ_Y is meant, as printed on p. 375 ('= ℝΓ_Y(Rp_*(Λ_{V,X}))'). The TeX "
    "silently corrects.",
    corrected="\\Gamma_Y")
add(374, "'D'autre part le complexe'",
    "no comma after 'D'autre part'",
    "D'autre part, le complexe", "punctuation", "high",
    "D'autre part, le", "D'autre part le",
    "")
add(374, "'le complexe Rp_*(Λ_{V,X}) de Λ[G]-modules'",
    "Rp_*: a typed plain R (8x)",
    "complexe $\\R p_*(\\Lambda_{V,X})$", "font", "high",
    "complexe $\\R p_*", "complexe $\\mathrm{R}p_*",
    PLAIN_R)
add(374, "'En effet p : X --> Y étant'",
    "no comma after 'En effet'",
    "En effet, $p:X\\to Y$", "punctuation", "high",
    "En effet, $p", "En effet $p",
    "")
add(374, "'on a R^q p_*(Λ_{V,X}) = 0 si q ≠ 0'",
    "= 0 si q ≠ 0 (the word 'si', no parentheses)",
    "\\R^q p_*(\\Lambda_{V,X})=0\\qquad(q\\ne0)", "word", "high",
    "=0\\qquad(q\\ne0)", "=0\\quad\\text{si }q\\ne0",
    "The R of R^q is double-struck, as the TeX.")
add(374, "'Il en résulte donc que :'",
    "colon at the end of the line",
    "Il en résulte donc que", "punctuation", "high",
    "Il en résulte donc que", "Il en résulte donc que :",
    "")
add(374, "display 'Rp_*(Λ_{V,X}) = p_*(Λ_{V,X})' (printed at the top of p. 375)",
    "no full stop after the display",
    "\\R p_*(\\Lambda_{V,X})=p_*(\\Lambda_{V,X}).", "punctuation", "high",
    "=p_*(\\Lambda_{V,X}).", "=p_*(\\Lambda_{V,X})",
    "Printed on p. 375 (see the marker item there); filed under p. 374, where the line stands now: apply before "
    "the marker move of p. 375. Its R is double-struck, as the TeX.")

# ---------------- page 375 ----------------
add(375, "top of the page",
    "p. 375 begins with the display 'Rp_*(Λ_{V,X}) = p_*(Λ_{V,X})', then '(SGA 4 VIII 5.5) nous donne aussi'; "
    "p. 374 ends with 'Il en résulte donc que :'",
    "the display '\\[ \\R p_*(\\Lambda_{V,X})=p_*(\\Lambda_{V,X}). \\]' ends page_374.tex (s5.tex lines "
    "12765-12767 diplomatic, 12761-12763 current); the folio-375 marker follows it",
    "marker", "high", None, None,
    "Page 375 really begins at the '\\[' of that display (diplomatic line 12765). Exact fix: python -I "
    "move_marker.py 5 375 '\\[' --before (simulated in memory on both layers: the marker then stands between "
    "'Il en résulte donc que' and '\\['). Apply the p. 374 edit of the display's full stop before the move.")
add(375, "display of the fibres, left-hand side",
    "p_*(Λ_{V,X})_ȳ ≃ (no outer parentheses)",
    "\\bigl(p_*(\\Lambda_{V,X})\\bigr)_{\\bar y}\\simeq", "formula", "high",
    "\\bigl(p_*(\\Lambda_{V,X})\\bigr)_{\\bar y}", "p_*(\\Lambda_{V,X})_{\\bar y}",
    "The TeX adds parentheses.")
add(375, "display of the fibres, first case, stalk Λ_{V,X,x}",
    "Λ_{V,X,x}: x without bar (4x), while ȳ on the left has its bar",
    "\\Lambda_{V,X,\\bar x}", "symbol", "high",
    "\\Lambda_{V,X,\\bar x}", "\\Lambda_{V,X,x}",
    "The TeX adds the bar.")
add(375, "display of the fibres, first case",
    "Λ[G] si y ∈ p(V) (the word 'si', no commas)",
    "\\Lambda[G],& y\\in p(V),\\\\[1em]", "word", "high",
    "\\Lambda[G],& y\\in p(V),\\\\[1em]", "\\Lambda[G]& \\text{si } y\\in p(V)\\\\[1em]",
    "One edit per line: it also removes the two commas the print does not have.")
add(375, "display of the fibres, second case",
    "0      si  y ∉ p(V) (the word 'si', no commas)",
    "0,& y\\notin p(V),", "word", "high",
    "0,& y\\notin p(V),", "0& \\text{si } y\\notin p(V)",
    "One edit: it also removes the two commas the print does not have.")
add(375, "'au morphisme canonique Y --> Spec(k) on déduit que'",
    "no comma before 'on déduit'",
    "$Y\\to\\Spec(k)$, on déduit que", "punctuation", "high",
    "\\Spec(k)$, on", "\\Spec(k)$ on",
    "")
add(375, "display 'RΓ_X(Λ_{V,X}) = RΓ_Y(Rp_*(Λ_{V,X}))', first R",
    "RΓ_X: a typed plain R (8x)",
    "\\R\\Gamma_X(\\Lambda_{V,X})=", "font", "high",
    "\\R\\Gamma_X(\\Lambda_{V,X})=", "\\mathrm{R}\\Gamma_X(\\Lambda_{V,X})=",
    PLAIN_R + " The R of RΓ_Y in the same display is double-struck.")
add(375, "same display, Rp_*",
    "Rp_*: a typed plain R (4x)",
    "\\R\\Gamma_Y(\\R p_*(\\Lambda_{V,X}))", "font", "high",
    "(\\R p_*(\\Lambda_{V,X}))", "(\\mathrm{R}p_*(\\Lambda_{V,X}))",
    PLAIN_R)
add(375, "'Pour conclure que RΓ_X(Λ_{V,X}) est parfait'",
    "RΓ_X: a typed plain R (4x)",
    "Pour conclure que $\\R\\Gamma_X(\\Lambda_{V,X})$", "font", "high",
    "conclure que $\\R\\Gamma_X", "conclure que $\\mathrm{R}\\Gamma_X",
    PLAIN_R)
add(375, "'est parfait il nous reste à démontrer'",
    "no comma after 'parfait'",
    "est parfait, il nous reste", "punctuation", "high",
    "parfait, il nous", "parfait il nous",
    "")
add(375, "'pour vérifier que RΓ_X(Λ_{V,X}) est pseudo-cohérent'",
    "RΓ_X: a typed plain R (4x)",
    "pour vérifier que $\\R\\Gamma_X(\\Lambda_{V,X})$", "font", "high",
    "vérifier que $\\R\\Gamma_X", "vérifier que $\\mathrm{R}\\Gamma_X",
    PLAIN_R)
add(375, "'appliqué au Λ-Module Λ_{V,X}'",
    "Λ-Module with a capital M (2x)",
    "au $\\Lambda$-module", "word", "high",
    "au $\\Lambda$-module", "au $\\Lambda$-Module",
    "The typescript's capital M (sheaf of modules), as 'A-Modules' on p. 373.")
add(375, "end of the proof, after 'Λ_{V,X}'",
    "no full stop after Λ_{V,X} (clean paper, 2x)",
    "$\\Lambda_{V,X}$.", "punctuation", "high",
    "$\\Lambda_{V,X}$.", "$\\Lambda_{V,X}$",
    "")
add(375, "end of the proof environment",
    "the proof ends without a mark; the label is 'Démonstration :' (p. 374)",
    "\\end{prooftext}", "other", "high",
    "\\end{prooftext}\n", "",
    "Apply together with the p. 374 edit of the label (which removes '\\begin{prooftext}[Démonstration]').")
add(375, "'la classe cl_{K˙(Λ[G])}(RΓ_X(Λ_{V,X}))'",
    "RΓ_X: a typed plain R (4x)",
    "(\\R\\Gamma_X(\\Lambda_{V,X}))$", "font", "high",
    "(\\R\\Gamma_X(\\Lambda_{V,X}))$", "(\\mathrm{R}\\Gamma_X(\\Lambda_{V,X}))$",
    PLAIN_R)

# ---------------- write and check ----------------
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

bad = 0
counts = {}
for d in F:
    p = d['page']
    c = counts.setdefault(p, [0, 0])
    c[1 if d['kind'] == 'misprint_in_print' else 0] += 1
    if d['fix'] is None:
        continue
    t = open(RUN + r'\b371_375\page_%d.tex' % p, encoding='utf-8', newline='').read()
    n = t.count(d['fix']['old'])
    if n != 1 or '%%%%%%%%%%' in d['fix']['old']:
        bad += 1
        print('BAD', p, n, repr(d['fix']['old'][:80]))
print('findings', len(F), 'bad', bad)
for p in sorted(counts):
    print(p, '%d/%d' % tuple(counts[p]))
