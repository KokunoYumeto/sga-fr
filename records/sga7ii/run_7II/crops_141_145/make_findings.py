import json, os, sys

FOLDER = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b141_145'
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_141_145.json'
NL = '\n'

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 141 ----------------
add(page=141,
    where="(3.1.8.4), after the last node of the second row",
    scan="RΓ(V, Λ) ⥲ RΓ(V^o, Λ) ←~ RΓ(B̄*, Λ)   .  (typed full stop to the right of the last node)",
    tex=r'''R\Gamma(\overline{B}^*, \Lambda) \arrow[l, "\sim"'] then \end{tikzcd}, no full stop''',
    kind="punctuation", confidence="high",
    fix={"old": r'R\Gamma(\overline{B}^*, \Lambda) \arrow[l, "\sim"' + "'" + ']' + NL + r'\end{tikzcd}',
         "new": r'R\Gamma(\overline{B}^*, \Lambda) \arrow[l, "\sim"' + "'" + ']' + NL + r'\end{tikzcd}\quad .'},
    note="The diagram's STRUCTURE comment itself records the printed full stop; the tikzcd omits it. Same form as the diagram-punctuation fixes on pp. 99-129.")

add(page=141,
    where="(3.1.8.5), after the last node of the second row",
    scan="RΓ(D̃_t, Rf_! Rj̄_* Λ)   .  (typed full stop to the right of the last node)",
    tex=r'''\arrow[u, "\text{\textcircled{3}}", "\wr"'] then \end{tikzcd}, no full stop''',
    kind="punctuation", confidence="high",
    fix={"old": r'"\wr"' + "'" + ']' + NL + r'\end{tikzcd}',
         "new": r'"\wr"' + "'" + ']' + NL + r'\end{tikzcd}\quad .'},
    note="The STRUCTURE comment records the printed full stop; the tikzcd omits it.")

# ---------------- page 142 ----------------
add(page=142,
    where="(3.1.8.6), sign between the two sides",
    scan="R^iΓ_{0}(RΨ_η(Λ))  ═  H^i_c(V^o, Λ) . : a long equals sign, two straight strokes about 35 px long (two typed = side by side; checked at 8x and by stroke profile)",
    tex=r"\simeq",
    kind="symbol", confidence="medium",
    fix={"old": r'\simeq H^i_c(V^o, \Lambda) .', "new": r'= H^i_c(V^o, \Lambda) .'},
    note="Both strokes are straight: the centre line of the upper stroke varies by about 1.5 px along its length, like the lower stroke (1 px), against 4 px for the wavy upper stroke of the ≃ in '(_fC ≃ ∂_fB' on p. 143, which the TeX rightly gives as \\simeq. Each stroke is about twice the width of a single typed = (16 px), with a small step near the middle where two typed = signs meet.")

add(page=142,
    where="(3.1.8.6), subscript of RΓ",
    scan="RΓ_{0}: the oval inside the braces (16 x 21 px) is the same glyph as on p. 141 (3.1.8.5), where the TeX writes \\{0\\}",
    tex=r"R^i\Gamma_{\{O\}}",
    kind="symbol", confidence="low",
    fix={"old": r'R^i\Gamma_{\{O\}}', "new": r'R^i\Gamma_{\{0\}}'},
    note="In this typeface the digit 0 and the letter O have the same width (17 px: the 0 of '[0, 1]' and the O of 'On garde' on p. 143), so the glyph is read by its meaning: the support is the singular point 0 of B_o, written 0 in 'est constant en dehors de 0' on p. 141, and the same printed RΓ_{0}(RΨ_η(Λ)) is \\{0\\} in the TeX of (3.1.8.5) on p. 141 (and H^i_{\\{0\\}} on p. 139). Apply together with the p. 143 fix, or neither.")

add(page=142,
    where="3.1.9, 'qui résoud le morphisme évident'",
    scan="qui résoud le morphisme évident",
    tex="qui résoud le morphisme évident",
    kind="misprint_in_print", confidence="high",
    fix=None, corrected="qui résout le morphisme évident",
    note="Spelling error of the print (the present of résoudre is 'résout'). The TeX keeps the printed reading.")

add(page=142,
    where="3.1.9, 'Sous des hypothèses raisonables'",
    scan="Sous des hypothèses raisonables",
    tex="Sous des hypothèses raisonables",
    kind="misprint_in_print", confidence="high",
    fix=None, corrected="Sous des hypothèses raisonnables",
    note="Spelling error of the print (raisonnable has nn). The TeX keeps the printed reading.")

add(page=142,
    where="3.1.9, label over the quasi-isomorphism Γ_Φ(X-Y, Λ*_X) → RΓ(X mod Y, Λ)",
    scan="a handwritten ≈ (two stacked tildes joined at the right end) above the arrow; label 14 px high (checked at 8x)",
    tex=r"\overset{\sim}{\longrightarrow}",
    kind="symbol", confidence="medium",
    fix={"old": r'\overset{\sim}{\longrightarrow} R\Gamma (X \bmod Y, \Lambda)',
         "new": r'\overset{\approx}{\longrightarrow} R\Gamma (X \bmod Y, \Lambda)'},
    note="The single tildes over the iso arrows of pp. 141, 143 and 144 (3.1.10.1) are 7-11 px high and one stroke; this one has two separate wavy strokes. The same ≈ stands over both arrows of 'Puisque Λ → Rq_*Λ et Λ → Rq'_*Λ' on p. 144.")

# ---------------- page 143 ----------------
add(page=143,
    where="second paragraph, 'dans ce coisinage'",
    scan="de Y et, dans ce coisinage, est l'identité (checked at 4x)",
    tex="dans ce coisinage",
    kind="misprint_in_print", confidence="high",
    fix=None, corrected="dans ce voisinage",
    note="Typing error (c for v); the same sentence has 'dans un voisinage de Y'. The TeX keeps the printed reading.")

add(page=143,
    where="Proposition 3.1.10, subscript of RΓ in (RΦ_η(Λ))_o → RΓ_{0}(RΨ_η(Λ))",
    scan="RΓ_{0}: the same oval glyph as in (3.1.8.5) on p. 141 (17 x 22 px, the width of both the 0 of '[0, 1]' and the O of 'On garde' on this page)",
    tex=r"R\Gamma_{\{O\}}",
    kind="symbol", confidence="low",
    fix={"old": r'R\Gamma_{\{O\}}', "new": r'R\Gamma_{\{0\}}'},
    note="Read by its meaning, as on p. 142: the target is the RΓ_{0}(RΨ_η(Λ)) of (3.1.8.5)-(3.1.8.6), written \\{0\\} on p. 141. Apply together with the p. 142 fix, or neither.")

add(page=143,
    where="3.1.10, proof: 'dont la fibre en y ∈ D_t induite l'identité'",
    scan="dont la fibre en y ∈ D_t induite l'iden-tité",
    tex="induite l'identité",
    kind="misprint_in_print", confidence="medium",
    fix=None, corrected="induise l'identité",
    note="The relative clause needs a verb: 'induise' (subjunctive, a condition on the trivialisation) or 'induit'; 'induite' is a typing slip. The TeX keeps the printed reading.")

# ---------------- page 144 ----------------
add(page=144,
    where="first diagram, top right node (source of j̄ and q')",
    scan="₁B̄* : a typed subscript 1 at the lower left of B̄*, as in the bottom right node (checked at 5x; the q' arrow starts below it)",
    tex=r'''{}_1\bar{B}^* \arrow[l, hook, "\bar{\jmath}"'] \arrow[d, "q'"]''',
    kind="misprint_in_print", confidence="medium",
    fix=None, corrected=r'''\bar{B}^* \arrow[l, hook, "\bar{\jmath}"'] \arrow[d, "q'"]''',
    note="The top right node must be B̄*: j̄ is the inclusion of B̄* in B̄ (Rj̄_* on p. 141), and q' is the quotient map B̄* → ₁B̄* = B̄*/R (p. 143), as the text after the diagram uses it ('Λ ⥲ Rq'_*Λ ... une résolution équivariante de Λ sur ₁B̄*'). As printed, q' would map ₁B̄* to itself. The TeX keeps the printed reading.")

add(page=144,
    where="first diagram, after the last node of the second row",
    scan="₁B̄*        .  (typed full stop far to the right of the bottom right node)",
    tex=r'''\arrow[l, hook, "\bar{\jmath}"'] then \end{tikzcd}, no full stop''',
    kind="punctuation", confidence="high",
    fix={"old": r'"\bar{\jmath}"' + "'" + ']' + NL + r'\end{tikzcd}',
         "new": r'"\bar{\jmath}"' + "'" + ']' + NL + r'\end{tikzcd}\quad .'},
    note="The STRUCTURE comment records the printed full stop but leaves it out as sentence punctuation; by the edition's rule it is reproduced.")

add(page=144,
    where="'la variation se calcule à partir du morphisme de complexe'",
    scan="du morphisme / de complexe",
    tex="du morphisme de complexe",
    kind="misprint_in_print", confidence="medium",
    fix=None, corrected="du morphisme de complexes",
    note="Agreement slip: a morphism between complexes ('morphisme de complexes'), as with 'morphisme de foncteurs'. The TeX keeps the printed reading.")

add(page=144,
    where="'Puisque Λ ⥲ Rq_*Λ', label over the first arrow",
    scan="a handwritten ≈ above the arrow: two stacked tildes, label 15 px high (checked at 16x)",
    tex=r"\stackrel{\sim}{\longrightarrow}",
    kind="symbol", confidence="medium",
    fix={"old": r'\Lambda \stackrel{\sim}{\longrightarrow} Rq_*\Lambda',
         "new": r'\Lambda \stackrel{\approx}{\longrightarrow} Rq_*\Lambda'},
    note="The tildes over the arrows of (3.1.10.1) on the same page are single strokes 8-11 px high.")

add(page=144,
    where="'et Λ ⥲ Rq'_*Λ', label over the second arrow",
    scan="a handwritten ≈ drawn tightly: one thick wavy mark 12 px high with a white line inside it along its length (two strokes nearly merged; checked at 16x)",
    tex=r"\stackrel{\sim}{\longrightarrow}",
    kind="symbol", confidence="low",
    fix={"old": r'\Lambda \stackrel{\sim}{\longrightarrow} Rq' + "'" + r'_*\Lambda',
         "new": r'\Lambda \stackrel{\approx}{\longrightarrow} Rq' + "'" + r'_*\Lambda'},
    note="Paired with the clear ≈ of the first arrow in the same sentence; a single tilde in this hand is a thin stroke 7-9 px high.")

add(page=144,
    where="second morphism, 'Λ[o] → ī* ₁j̄_*(Λ)'",
    scan="ī* ₁j̄_*(Λ)   .  (no asterisk on Λ; checked at 4x), against ī* j̄_* (Λ*) in the first morphism",
    tex=r"{}_1\bar{\jmath}_*(\Lambda)",
    kind="misprint_in_print", confidence="low",
    fix=None, corrected=r"{}_1\bar{\jmath}_*(\Lambda^*)",
    note="The sentence computes the variation 'à l'aide d'une résolution équivariante de Λ sur ₁B̄*', so the morphism should go to ī* ₁j̄_* of that resolution, as Λ* in the first morphism; the asterisk is probably dropped. The TeX keeps the printed reading.")

add(page=144,
    where="(3.1.10.1), after the last node of the second row",
    scan="RΓ (₁B̄* mod ₁C̄*, Λ)    ,  (typed comma to the right of the bottom right node)",
    tex=r'''\arrow[l, "\sim"', "\text{\textcircled{2}}"] then \end{tikzcd}, no comma''',
    kind="punctuation", confidence="high",
    fix={"old": r'"\text{\textcircled{2}}"]' + NL + r'\end{tikzcd}',
         "new": r'"\text{\textcircled{2}}"]' + NL + r'\end{tikzcd}\quad ,'},
    note="The STRUCTURE comment records the printed comma but leaves it out; by the edition's rule it is reproduced.")

add(page=144,
    where="'(ce groupe agit sur ₁B̄* via son action 1.15; ...)'",
    scan="via son action 1.15; (digits 1 . 1 5 with one full stop; checked at 4x)",
    tex="via son action 1.15;",
    kind="misprint_in_print", confidence="medium",
    fix=None, corrected="via son action 1.1.5;",
    note="Exposé XIV has no 1.15 (§1 runs 1.1-1.4 with three-part numbers). The action of π_1(D*) on a universal covering is defined in 1.1.5 and cited as such on pp. 119 ('agissant sur D̃* par 1.1.5') and 120 ('(1.1.5)'). The TeX keeps the printed reading.")

# ---------------- checks ----------------
ok = True
for x in F:
    p = x['page']
    path = os.path.join(FOLDER, 'page_%03d.tex' % p)
    txt = open(path, encoding='utf-8', newline='').read()
    if '\r' in txt:
        print('WARNING CR in', path)
    if x.get('fix'):
        old = x['fix']['old']
        n = txt.count(old)
        if n != 1:
            ok = False
            print('NOT UNIQUE', p, n, repr(old))
        if '%%%%%%%%%%' in old or '%%%%%%%%%%' in x['fix']['new']:
            ok = False
            print('MARKER TOUCHED', p)
    if x['kind'] == 'misprint_in_print':
        assert 'corrected' in x
    else:
        assert 'corrected' not in x

order = ['page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'corrected', 'note']
out = [{k: x[k] for k in order if k in x} for x in F]
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print('written', len(out))
    from collections import Counter
    c = Counter((x['page'], x['kind'] == 'misprint_in_print') for x in out)
    for p in [141, 142, 143, 144, 145]:
        print(p, c[(p, False)], '/', c[(p, True)])
else:
    print('NOT WRITTEN')
    sys.exit(1)
