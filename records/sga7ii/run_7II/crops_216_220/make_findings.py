# -*- coding: utf-8 -*-
import json, sys, os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(RUN, 'b216_220')
OUT = os.path.join(RUN, 'findings_216_220.json')

F = []
def add(**kw):
    F.append(kw)

# ---------------- page 216 ----------------
add(page=216,
    where="2.2, after the definition: 'Nous allons voir plus bas (3.2.1) que les pinceaux de Lefschetz forment un ouvert de Gr(1, P^r)'",
    scan="Gr(l, ℙ^r): double-struck P with no check above it (checked at 2x)",
    tex=r"$\mathrm{Gr}(1, \mathbb{P}^r)$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"$\mathrm{Gr}(1, \check{\mathbb{P}}^r)$",
    note="Pencils of hyperplanes are lines of the dual space: 2.3, the footnote *) and 3.2.1 (the result announced here) all print Gr(1, ℙ̌^r). The TeX keeps the printed reading.")

add(page=216,
    where="2.4, first word",
    scan="Rappellons (double l)",
    tex=r"Rappellons",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"Rappelons",
    note="Spelling slip. The TeX keeps the printed reading.")

add(page=216,
    where="2.4, 'qui s'écrit en termes des coordonnés homogènes X_o,...,X_r'",
    scan="coordonnés homogènes",
    tex=r"coordonnés homogènes",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"coordonnées homogènes",
    note="Agreement slip (les coordonnées). The TeX keeps the printed reading.")

add(page=216,
    where="2.4, display (X_o,...,X_r) --S_d--> (,...,X^W,...)",
    scan="(,...,X^W,...): a comma directly after the opening parenthesis (checked at 2x)",
    tex=r"(,\ldots,X^W,\ldots)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"(\ldots,X^W,\ldots)",
    note="Stray comma before the first dots. The TeX keeps the printed reading.")

add(page=216,
    where="2.4, 'où X^W = X_o^{W_o} ... X_r^{W_o} parcourt les monômes de degré d'",
    scan="X_r^{W_o}: the exponent of X_r is W with subscript o, the same as for X_o (checked at 2x)",
    tex=r"X_r^{W_o}",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"X_r^{W_r}",
    note="Wrong index: the monomial is X_o^{W_o} ... X_r^{W_r}. The TeX keeps the printed reading.")

# ---------------- page 217 ----------------
add(page=217,
    where="Théorème 2.5, 'muni d'un plongement i : X ↪ P^r'",
    scan="a plain typed P with a single stem and no second stroke (pixel map checked); every other P^r of pp. 216-220 is the double-struck ℙ",
    tex=r"$i : X \hookrightarrow P^r$",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"$i : X \hookrightarrow \mathbb{P}^r$",
    note="Font slip of the typist (the second stem of the double-struck P left out), as in 2.1 on p. 215. The TeX correctly gives the printed plain P and keeps the printed reading.")

add(page=217,
    where="2.5.2, 'Si k est de caractéristique nulle; le plongement donné i'",
    scan="nulle; (a semicolon: dot above the comma, checked at 4x)",
    tex=r"\underline{est de caractéristique nulle};",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\underline{est de caractéristique nulle},",
    note="The conditional clause 'Si k est ...' takes a comma; on the typewriter the two keys are neighbours. The TeX keeps the printed semicolon.")

add(page=217,
    where="last line, 'comme étant le composé P(N) --ν--> X × P̌^r --pr_2--> P̌^r .'",
    scan="the arrow labelled pr_2 is a plain rule with no arrowhead (checked at 4x: the rule ends clean, white paper before the ℙ̌^r); the ν arrow of the same line and the arrow of (3.1.2) have their heads",
    tex=r"\xrightarrow{\ \mathrm{pr}_2\ }",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"\xrightarrow{\ \mathrm{pr}_2\ }",
         "new": r"\stackrel{\mathrm{pr}_2}{\relbar\joinrel\relbar\joinrel\relbar}"},
    corrected=r"\xrightarrow{\ \mathrm{pr}_2\ }",
    note="The second projection X × ℙ̌^r → ℙ̌^r. The TeX silently supplies the head; the edit restores the printed plain rule with the \\stackrel{..}{\\relbar\\joinrel\\relbar} construction already used on p. 33.")

# ---------------- page 218 ----------------
add(page=218,
    where="Remarque 3.1.5, 'donc Y → P̌^r fait de Y une intersection complète relative'",
    scan="the first Y (source of the arrow) is not underlined (checked at 2x); the Y after 'fait de' and all other Y of 3.1.5 are underlined",
    tex=r"donc $Y \longrightarrow",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"donc $\underline{Y} \longrightarrow",
    note="Y underlined is the incidence subscheme throughout 3.1.5. The TeX keeps the printed reading.")

add(page=218,
    where="Remarque 3.1.5, 'le sous-schéma jacobien J_{n-1}(Y/P̌^r) (VI 5.2 )'",
    scan="P̌^r with a plain typed P: one stem, no trace of the second stroke at 8x or in a pixel map, whereas the double-struck ℙ of 'ℙ(N)' on the same line shows its thin second stroke plainly",
    tex=r"$\underline{J}_{n-1}(\underline{Y}/\check{\mathbb{P}}^r)$",
    kind="font", confidence="low",
    fix={"old": r"(\underline{Y}/\check{\mathbb{P}}^r)",
         "new": r"(\underline{Y}/\check{P}^r)"},
    note="Low confidence: the hand-drawn second stroke is faint on several ℙ of these pages (ℙ̌^r(k) on this page keeps only dots of it), but here nothing at all is visible. Apply before the next finding, which concerns the same spot.")

add(page=218,
    where="Remarque 3.1.5, 'J_{n-1}(Y/P̌^r)'",
    scan="plain P (see the font entry above), while the same space is the double-struck ℙ̌^r everywhere else in 3.1.5",
    tex=r"(\underline{Y}/\check{P}^r) (after the font fix above; at present (\underline{Y}/\check{\mathbb{P}}^r))",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"(\underline{Y}/\check{\mathbb{P}}^r)",
    note="Font slip of the typist (second stem left out), as for the plain P of Théorème 2.5 on p. 217. After the font fix the TeX keeps the printed reading.")

add(page=218,
    where="Proposition 3.2, 'formé des hyperplans H tel que X·H ait un et un seul point singulier'",
    scan="tel que (underlined)",
    tex=r"\underline{tel que}",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\underline{tels que}",
    note="Agreement with 'des hyperplans'. The TeX keeps the printed reading.")

# ---------------- page 219 ----------------
add(page=219,
    where="after Proposition 3.2, 'C'est un cas particulier de XV 1.3.2, , s'appuyant'",
    scan="XV 1.3.2, , (two commas, checked at 1.5x)",
    tex=r"XV 1.3.2, ,",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"XV 1.3.2,",
    note="Doubled comma. The TeX keeps the printed reading.")

add(page=219,
    where="same sentence, 's'appuyant la théorie des \"modules henséliens\"'",
    scan="s'appuyant la théorie",
    tex=r"s'appuyant la théorie",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"s'appuyant sur la théorie",
    note="The preposition 'sur' is missing. The TeX keeps the printed reading.")

add(page=219,
    where="proof of 3.2.1, condition (3.2.6) 'D n'est pas contenue dans X'",
    scan="plain X with no check (checked at 2x)",
    tex=r"(3.2.6) $D$ n'est pas contenue dans $X$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"(3.2.6) $D$ n'est pas contenue dans $\check{X}$",
    note="D is a line in ℙ̌^r, so it can only lie in the dual variety X̌ of 3.1.3; (3.2.6) excludes the lines contained in X̌. The TeX keeps the printed reading.")

# ---------------- page 220 ----------------
add(page=220,
    where="proof of 3.2.1, 'Parce que dim X ≤ r-1 , l'ouvert (3.2.6) est non-vide'",
    scan="dim X with a plain X, no check (checked at 3x)",
    tex=r"Parce que $\dim X \leq r-1$ , l'ouvert",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"Parce que $\dim \check{X} \leq r-1$ , l'ouvert",
    note="The open set (3.2.6) of lines not contained in X̌ is non-empty because X̌ is a proper closed subset of ℙ̌^r (3.1.4: dim X̌ ≤ r-1); the next sentence prints the check for the same bound. The TeX keeps the printed reading.")

add(page=220,
    where="proof of 3.2.1, 'un tel H existe car dim X̌ ≤ r-1'",
    scan="a hand-drawn check above the X (checked at 6x): one slanting stroke ending at the top of the X, its right arm lost or very short",
    tex=r"existe car $\dim X \leq r-1$",
    kind="symbol", confidence="high",
    fix={"old": r"existe car $\dim X \leq r-1$",
         "new": r"existe car $\dim \check{X} \leq r-1$"},
    note="The dual variety X̌: a hyperplane transversal to X exists because X̌ ≠ ℙ̌^r.")

add(page=220,
    where="proof of 3.2.1, 'Parce que dim (X·G)ˇ ≤ r-1 , il existe un hyperplan G'",
    scan="a hand-drawn check over 'X·', its vertex above the centre dot, i.e. over the middle of (X·G) (checked at 6x)",
    tex=r"$\dim (X \cdot G) \leq r-1$",
    kind="symbol", confidence="high",
    fix={"old": r"$\dim (X \cdot G) \leq r-1$",
         "new": r"$\dim \check{(X \cdot G)} \leq r-1$"},
    note="The dual variety of the section. Apply before the next finding, which concerns the same expression.")

add(page=220,
    where="same expression, 'dim (X·G)ˇ ≤ r-1'",
    scan="(X·G): G (checked at 6x)",
    tex=r"\check{(X \cdot G)} (after the preceding fix; at present (X \cdot G))",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\check{(X \cdot H)}",
    note="G is only introduced afterwards, as a hyperplane transversal to X·H; such a G exists because the dual variety of X·H is not all of ℙ̌^r. After the symbol fix the TeX keeps the printed G.")

add(page=220,
    where="proof of 3.2.1, 'la droite D passant par H et G a une axe'",
    scan="a une axe",
    tex=r"a une axe",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"a un axe",
    note="'axe' is masculine. The TeX keeps the printed reading.")

add(page=220,
    where="proof of 3.2.8, 'D'après (3.2.1), les-dits pinceaux'",
    scan="les-dits (with hyphen)",
    tex=r"les-dits",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"lesdits",
    note="Spelling. The TeX keeps the printed reading.")

# ---------------- checks ----------------
ok = True
for f in F:
    fx = f.get('fix')
    path = os.path.join(BATCH, 'page_%03d.tex' % f['page'])
    txt = open(path, encoding='utf-8').read()
    if fx:
        n = txt.count(fx['old'])
        if n != 1:
            ok = False
            print('NOT UNIQUE', f['page'], n, fx['old'])
        lines = txt.split('\n')
        for ln in lines:
            if ln.startswith('%%%%%%%%%%') and fx['old'] in ln:
                ok = False; print('touches marker', f['page'])
    else:
        t = f['tex'].split(' (after')[0]
        n = txt.count(t)
        print('tex-check', f['page'], n, t)
    if f['kind'] != 'misprint_in_print' and 'corrected' in f:
        ok = False; print('corrected on non-misprint', f)
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
        ok = False; print('missing corrected', f)

order = ['page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'corrected', 'note']
out = [{k: f[k] for k in order if k in f} for f in F]
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
print('written', OUT, len(out), 'ok' if ok else 'PROBLEMS')
