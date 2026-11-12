import json
import sys

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b136_140"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_136_140.json"

GP_NOTE = ("Glyph boxes: the subscripts of G reach 5-6 px above the baseline of G and 22 px below it, "
           "like the capital P of T_{/P} on this page; the small p of E_p and P_p starts 2-4 px below "
           "the baseline and descends 30 px. Global item 26 (G_p for G_P).")

PE_NOTE = ("The print writes P (the Groupe) where the bitorseurs E_p, E_{p'}, E_{pp'} are meant: p. 137 "
           "introduces them as 'deux bitorseurs E_p , E_{p'} sous (G,G)', and from 1.1.4 on the print "
           "itself writes the same maps as E_p E_{p'} -> E_{pp'} (diagram (1.1.4.1), (1.1.5.2)). "
           "Same slip in every formula of 1.1.2.1-1.1.3 (pp. 136-138): correct all or none. "
           "The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 136 ----------------
add(page=136,
    where="1.1.2.1, 'la donnée d'un bitorseur sous le couple de Groupes (G_P,G_P) sur P équivaut à une section cartésienne'",
    scan="(G_P,G_P): capital P in both subscripts",
    tex=r"$(G_p,G_p)$ sur $P$",
    kind="symbol", confidence="high",
    fix={"old": r"$(G_p,G_p)$ sur $P$", "new": r"$(G_P,G_P)$ sur $P$"},
    note=GP_NOTE)
add(page=136,
    where="1.1.2.1, 'avec la catégorie des bitorseurs sous (G_P,G_P). Cet énoncé résulte'",
    scan="(G_P,G_P): capital P in both subscripts",
    tex=r"sous $(G_p,G_p)$. Cet",
    kind="symbol", confidence="high",
    fix={"old": r"sous $(G_p,G_p)$. Cet", "new": r"sous $(G_P,G_P)$. Cet"},
    note=GP_NOTE)
add(page=136,
    where="1.1.3, first line: 'La structure de bitorseur 1.1.2 sous (G_P,G_P) sur E'",
    scan="(G_P,G_P): capital P in both subscripts",
    tex=r"1.1.2 sous $(G_p,G_p)$ sur $E$",
    kind="symbol", confidence="high",
    fix={"old": r"1.1.2 sous $(G_p,G_p)$", "new": r"1.1.2 sous $(G_P,G_P)$"},
    note=GP_NOTE + " Pages 137-140 of the TeX already write G_P.")
add(page=136,
    where="1.1.2.1, 'on suppose donné de plus un isomorphisme de bitorseurs de P_p, avec l'image inverse de P_p par S' -> S'",
    scan="P_p, ... P_p (capital P, small p; the mark after the first P_p is a comma on the baseline, no prime)",
    tex=r"bitorseurs de $P_p$, avec l'image inverse de $P_p$ par",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"bitorseurs de $E_{p'}$, avec l'image inverse de $E_p$ par",
    note=("The sentence is about the compatibility of 'la formation de E_p' with base change: for the "
          "composed point p' : S' -> P one is given an isomorphism of E_{p'} with the inverse image of E_p "
          "by S' -> S. " + PE_NOTE))
add(page=136,
    where="1.1.2.1, 'donc pour toute catégorie fibrée sur T_{/P} le foncteur \"valeur en S\" est une équivalence ... et la catégorie fibre en P'",
    scan="\"valeur en S\"",
    tex=r'"valeur en $S$"',
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r'"valeur en $P$"',
    note=("The functor goes to the fibre category at P, P being the final object of the base T_{/P} "
          "(three lines earlier: le foncteur \"valeur en P\" induit une équivalence). "
          "The TeX keeps the printed reading."))

# ---------------- page 137 ----------------
add(page=137,
    where="first display, 'phi : P_p x P_p' --> P_pp''",
    scan="P_p x P_{p'} --> P_{pp'}",
    tex=r"\varphi : \quad P_p \times P_{p'} \ \longrightarrow\ P_{pp'}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\varphi : \quad E_p \times E_{p'} \ \longrightarrow\ E_{pp'}",
    note=PE_NOTE)
add(page=137,
    where="after (1.1.3.0), '(g,g' in G(S), x in P_p(S), x' in P_p'(S))'",
    scan="x ∈ P_p(S), x' ∈ P_{p'}(S)",
    tex=r"$x \in P_p(S)$, $x' \in P_{p'}(S))$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"$x \in E_p(S)$, $x' \in E_{p'}(S))$",
    note=PE_NOTE)
add(page=137,
    where="display after 'en termes du produit fibré contracté [2]', 'P_p x^G P_p' ,'",
    scan="P_p ×^G P_{p'}",
    tex=r"P_p \overset{G}{\times} P_{p'} \qquad ,",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"E_p \overset{G}{\times} E_{p'} \qquad ,",
    note=PE_NOTE)
add(page=137,
    where="display after 'se factorise en', 'P_p x P_p' --> P_p x^G P_p' --(phi_{p,p'})--> P_pp' ,'",
    scan="P_p x P_{p'} --> P_p ×^G P_{p'} --> P_{pp'}",
    tex=r"P_p \times P_{p'} \ \longrightarrow\ P_p \overset{G}{\times} P_{p'} \ \xrightarrow{\ \varphi_{p,p'}\ }\ P_{pp'}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"E_p \times E_{p'} \ \longrightarrow\ E_p \overset{G}{\times} E_{p'} \ \xrightarrow{\ \varphi_{p,p'}\ }\ E_{pp'}",
    note=PE_NOTE)
add(page=137,
    where="(1.1.3.1), 'phi_{p,p'} : P_p x^G P_p' --> P_pp''",
    scan="phi_{p,p'} : P_p ×^G P_{p'} --> P_{pp'}",
    tex=r"\varphi_{p,p'} \ :\ P_p \overset{G}{\times} P_{p'} \ \longrightarrow\ P_{pp'}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\varphi_{p,p'} \ :\ E_p \overset{G}{\times} E_{p'} \ \longrightarrow\ E_{pp'}",
    note=PE_NOTE)

# ---------------- page 138 ----------------
add(page=138,
    where="first sentence, 'sur le premier facteur P_p (resp. sur le deuxième facteur P_p')'",
    scan="P_p ... P_{p'}",
    tex=r"facteur $P_p$ (resp. sur le deuxième facteur $P_{p'}$)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"facteur $E_p$ (resp. sur le deuxième facteur $E_{p'}$)",
    note=PE_NOTE)

# ---------------- page 139 ----------------
add(page=139,
    where="after diagram (1.1.4.1), 'le produit contracté de bitorseurs sans signes x^{G_S} ,'",
    scan="the product sign with G_S over it: the S is the subscript of G (right of G, lower than G, still above the sign)",
    tex=r"$\times^{G}_{S}$",
    kind="formula", confidence="high",
    fix={"old": r"$\times^{G}_{S}$", "new": r"$\overset{G_S}{\times}$"},
    note=("The TeX sets S as a subscript of the product sign, below it; the print puts the group G_S above "
          "the sign, as G in P_p x^G P_{p'} on p. 137 (\\overset{G}{\\times} in the TeX)."))
add(page=139,
    where="diagram (1.1.4.1), after the right node",
    scan="a typed full stop right of the diagram, on the level of the bottom node",
    tex=r"\end{tikzcd}",
    kind="punctuation", confidence="high",
    fix={"old": r"\end{tikzcd}", "new": r"\end{tikzcd}\quad ."},
    note=("Sentence-final full stop of '... que le diagramme suivant est commutatif :' (7 x 8 px, the size of "
          "the typed full stops of the text; the STRUCTURE comment records it). Placed after the tikzcd as in "
          "the earlier diagram fixes of this volume (pp. 21, 99, 100)."))
add(page=139,
    where="'étant entendu que la multiplication contractéede deux bitorseurs Q.R'",
    scan="contractéede: the final e of 'contractée' was typed in afterwards over the word space; it touches the é, and only an 11 px gap (a word space is about 23 px) is left before 'de'",
    tex="contractéede",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="contractée de",
    note=("The typist's added e (agreement with 'multiplication') used up the space. The TeX keeps the "
          "run-together reading. 'corrected' replaces the 'tex' substring."))
add(page=139,
    where="'que cette opération de produit contracté estassociative à un isomorphisme canonique près [2]'",
    scan="estassociative: 'associative' (retyped in a lighter type) stands in the character cell right after 'est'; no word space",
    tex="estassociative",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="est associative",
    note="Missing word space in a retyped stretch of the line. The TeX keeps the printed reading.")
add(page=139,
    where="1.1.4.2, 'au cas \"universel\" S=PxP, p=pr_1,p' = pr_2 envisagé dans (1.1.3.2)'",
    scan="pr_1, pr_2: the projections (operator name)",
    tex=r"$p=pr_1,p' = pr_2$",
    kind="font", confidence="medium",
    fix={"old": r"$p=pr_1,p' = pr_2$", "new": r"$p=\mathrm{pr}_1,p' = \mathrm{pr}_2$"},
    note=("Math italic pr reads as the product of the variables p and r; the TeX writes the same projections "
          "\\mathrm{pr}_i and \\mathrm{pr}_1^* on p. 138 (operator-name issue, global items 19 and 26)."))

# ---------------- page 140 ----------------
add(page=140,
    where="first sentence, 'au cas \"universel\" où S=PxPxP, p=pr_1,p'=pr_2,p\"=pr_3 .'",
    scan="S=P×P×P, p=pr_1,p'=pr_2,p\"=pr_3 (pr the projections)",
    tex=r'S=P$\times$P$\times$P, $p=pr_1$,$p' + "'" + r'=pr_2$,$p"=pr_3$',
    kind="font", confidence="medium",
    fix={"old": r'S=P$\times$P$\times$P, $p=pr_1$,$p' + "'" + r'=pr_2$,$p"=pr_3$',
         "new": r'$S=P\times P\times P$, $p=\mathrm{pr}_1$,$p' + "'" + r'=\mathrm{pr}_2$,$p"=\mathrm{pr}_3$'},
    note=("The letters S and P stand outside math mode (roman, unlike every other variable of the TeX, e.g. "
          "$S = P\\times P$ on p. 138) and pr is in math italic; same projections as in 1.1.4.2 (p. 139)."))
add(page=140,
    where="1.1.5, '(NB les deux actions de G_P sur E, ou ce qui revient au même, de G sur P, sont sous-entendues dans les notations)'",
    scan="de G sur P",
    tex=r"de $G$ sur $P$, sont",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"de $G$ sur $E$, sont",
    note=("An action of the P-Groupe G_P on E (an object over P) amounts to an action of G on E compatible "
          "with j : E -> P; G does not act on P here. Low: 'sur P' may be meant as 'au-dessus de P'. "
          "The TeX keeps the printed reading."))

# ---------------- checks ----------------
ORDER = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
texts = {}
ok = True
for f in F:
    p = f["page"]
    if p not in texts:
        with open(f"{BASE}\\page_{p}.tex", encoding="utf-8", newline="") as fh:
            texts[p] = fh.read()
    t = texts[p]
    if f["tex"] not in t:
        print("TEX NOT FOUND", p, f["tex"]); ok = False
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        if n != 1:
            print("OLD COUNT", n, p, f["fix"]["old"]); ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("MARKER IN OLD", p); ok = False
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            print("NO CORRECTED", p); ok = False
    else:
        if "corrected" in f:
            print("CORRECTED ON NON-MISPRINT", p); ok = False

out = [{k: f[k] for k in ORDER if k in f} for f in F]
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    from collections import Counter
    c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
    for p in sorted(set(f["page"] for f in F) | {136, 137, 138, 139, 140}):
        print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
    print("written", OUT, len(out))
else:
    print("NOT WRITTEN")
    sys.exit(1)
