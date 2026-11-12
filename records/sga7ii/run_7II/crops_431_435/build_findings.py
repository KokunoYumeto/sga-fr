import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

BATCH = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b431_435'
OUT = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_431_435.json'

F = []


def add(page, where, scan, tex, kind, conf, old=None, new=None, note='', corrected=None, after_previous=False):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind, 'confidence': conf,
         'fix': None if old is None else {'old': old, 'new': new}}
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    d['_after_previous'] = after_previous
    F.append(d)


# ---------------- page 431 ----------------
add(431, 'top of page (before "est ≤ n-2j")',
    'the page begins with the unnumbered display E^n_DR(V) = Coker (H^n_Hdg(ℙ^{n+1}) ↪ H^n_Hdg(V))  ,',
    'that display (\\begin{equation*} E_{\\mathrm{DR}}^n(V) ... \\end{equation*}) is the last item under the folio-430 marker',
    'marker', 'high', None, None,
    "Page 431 really begins with the display \\begin{equation*} E_{\\mathrm{DR}}^n(V)=\\operatorname{Coker}... \\end{equation*} "
    "that ends page_430.tex; 'est $\\leq n-2j$' is its second item. Text not moved. Once the marker is moved, that display "
    "needs two edits to match the print: the arrow is a hooked arrow and a comma follows the display: "
    "'\\longrightarrow H_{\\mathrm{Hdg}}^n(V)\\right)' -> '\\hookrightarrow H_{\\mathrm{Hdg}}^n(V)\\right),'.")

add(431, 'first paragraph, after (XXI A.2)', 'divisibles par (underlined) q^j', 'divisibles par $q^j$ (no underline)',
    'underline', 'high', '(XXI A.2) divisibles par', '(XXI A.2) \\underline{divisibles par}')

add(431, 'first paragraph', 'Le résultat de AX 5.0. vient', 'Le résultat de Ax 5.0 vient',
    'word', 'high', 'de Ax', 'de AX', 'The print gives the name in capitals (as d\'AX in the heading of section 5).')

add(431, 'first paragraph', 'AX 5.0. vient (full stop after 5.0 in mid-sentence)', '5.0 vient',
    'misprint_in_print', 'medium', '5.0 vient', '5.0. vient',
    'Stray full stop after the reference number. The TeX silently drops it.', corrected='5.0 vient')

add(431, 'first paragraph, last line', 'conjectures de HODGE [5]', 'conjectures de Hodge [5]',
    'word', 'high', 'de Hodge [5]', 'de HODGE [5]', 'Name in capitals in the print.')

add(431, 'first paragraph, last line', 'et de TATE [5] :', 'et de Tate [5] :',
    'word', 'high', 'de Tate [5]', 'de TATE [5]', 'Name in capitals in the print.')

add(431, 'Conjecture 5.2, label and first line',
    'Conjecture (underlined) 5.2. (not underlined); underlined: Soient / un morphisme propre et lisse / avec / intègre / de type fini sur',
    '\\underline{Conjecture 5.2.} and no underline in the statement',
    'underline', 'high',
    '\\underline{Conjecture 5.2.}\nSoient $f:X\\to S$ un morphisme propre et lisse, avec $S$ intègre, de type\nfini sur',
    '\\underline{Conjecture} 5.2.\n\\underline{Soient} $f:X\\to S$ \\underline{un morphisme propre et lisse}, \\underline{avec} $S$ \\underline{intègre}, \\underline{de type\nfini sur}',
    'The statement is underlined in the print; the number is not.')

add(431, 'Conjecture 5.2, second and third lines',
    'underlined: et dominant / des entiers / Supposons que le co-niveau de Hodge du / de la fibre générique de / soit',
    'no underline',
    'underline', 'high',
    'et dominant\n$\\operatorname{Spec}(\\mathbb Z)$, $i,j$ des entiers. Supposons que le\nco-niveau de Hodge du $H^i$ de la fibre générique de $f$ soit $\\geq j$.',
    '\\underline{et dominant}\n$\\operatorname{Spec}(\\mathbb Z)$, $i,j$ \\underline{des entiers}. \\underline{Supposons que le\nco-niveau de Hodge du} $H^i$ \\underline{de la fibre générique de} $f$ \\underline{soit} $\\geq j$.')

add(431, 'Conjecture 5.2, from "Alors"',
    'underlined: Alors pour tout point / le coniveau / de / est / donc / si / est un point fermé de / les valeurs propres de Frobenius opérant sur / sont des entiers algébriques divisibles par / où',
    'no underline',
    'underline', 'high',
    'Alors pour tout point $s\\in S$, le coniveau (XX 2.0.6) de\n$H^i(X_s,\\mathbb Q_\\ell)$ est $\\geq j$, donc (XX 2.2) si $s$ est un point\nfermé de $S$, les valeurs propres de Frobenius opérant sur\n$H^i(X_s,\\mathbb Q_\\ell)$ sont des entiers algébriques divisibles par\n$q^j$, où $q',
    '\\underline{Alors pour tout point} $s\\in S$, \\underline{le coniveau} (XX 2.0.6) \\underline{de}\n$H^i(X_s,\\mathbb Q_\\ell)$ \\underline{est} $\\geq j$, \\underline{donc} (XX 2.2) \\underline{si} $s$ \\underline{est un point\nfermé de} $S$, \\underline{les valeurs propres de Frobenius opérant sur}\n$H^i(X_s,\\mathbb Q_\\ell)$ \\underline{sont des entiers algébriques divisibles par}\n$q^j$, \\underline{où} $q')

add(431, 'heading of section 6', '6. Fin de la démonstration de la formule de congruence. (full stop at the end)',
    '\\section*{6. Fin de la démonstration de la formule de congruence}',
    'punctuation', 'high', 'formule de congruence}', 'formule de congruence.}',
    'As in the heading of section 5 on p. 428.')

add(431, '(6.0.1)', '... mod 1 + qt 𝒪[[t]]  . (no parentheses)', '\\pmod{1+qt\\mathcal O[[t]]}',
    'formula', 'high', '\\pmod{1+qt\\mathcal O[[t]]}', '\\mod{1+qt\\mathcal O[[t]]}',
    'Convention of the transcription: every printed "mod x" (always without parentheses) is written \\pmod, which prints '
    '"(mod x)". Other cases on these pages, left for a global pass: p. 433 Cor. 6.0.12 \\pmod{\\pi\\mathcal O[[t]]}; '
    'p. 434 (6.1.8) three times \\pmod{\\text{degré }p}, (6.1.10) and (6.1.11) \\pmod p. p. 428 (5.0.6) was already changed to \\mod.')

add(431, 'line before (6.0.2)', 'Définissons (cf. (4.6.11) :  (only one closing parenthesis)', '(cf. (4.6.11)) :',
    'misprint_in_print', 'high', '(4.6.11)) :', '(4.6.11) :',
    'The print does not close the parenthesis opened by "(cf.". The TeX silently closes it.', corrected='(4.6.11)) :')

add(431, '(6.0.2), end', 'W_S = R_B ⊗_𝒪 𝔽_q  ,', 'W_S=R_B\\otimes_{\\mathcal O}\\mathbb F_q.',
    'punctuation', 'high', '\\otimes_{\\mathcal O}\\mathbb F_q.', '\\otimes_{\\mathcal O}\\mathbb F_q,',
    'The print has a comma (the definitions continue on p. 432), not a full stop.')

add(431, '(6.0.2)', 'W_S = R_B ⊗_𝒪 𝔽_q', 'W_S=R_B\\otimes_{\\mathcal O}\\mathbb F_q',
    'misprint_in_print', 'medium', None, None,
    'R_B for R_S: everything after it uses R_S (R_S(i) in (6.0.4)-(6.0.5), α_S(R_S) in 6.0.6), with B = S in the '
    'notation of (4.6.11). The TeX keeps the printed R_B.', corrected='W_S=R_S\\otimes_{\\mathcal O}\\mathbb F_q')

# ---------------- page 432 ----------------
add(432, '(6.0.4)', 'R_S(t) le sous-module de R_S forme ... (no "=")', 'R_S(i)=\\text{le sous-module ...}',
    'extra', 'high', '=\\text{le sous-module', '\\text{ le sous-module',
    'The TeX inserts an equals sign; the print reads "R_S(t) le sous-module", like (6.0.3) "W_S ⟶ W_S l\'opération".')

add(432, '(6.0.4)', 'R_S(t)', 'R_S(i)',
    'misprint_in_print', 'high', '\\tag{6.0.4}\nR_S(i)', '\\tag{6.0.4}\nR_S(t)',
    'The argument is printed t; the definition is of R_S(i) (degree i, used in (6.0.5)). The TeX silently corrects.',
    corrected='\\tag{6.0.4}\nR_S(i)')

add(432, '(6.0.4)', 'forme des éléments (no accent on forme)', 'formé des éléments',
    'misprint_in_print', 'high', 'formé des', 'forme des',
    'The other accents of the line are clear. The TeX silently corrects.', corrected='formé des')

add(432, 'Proposition 6.0.6', 'Proposition (underlined) 6.0.6. On a l\'inclusion (underlined)',
    '\\underline{Proposition 6.0.6.} On a l\'inclusion', 'underline', 'high',
    '\\underline{Proposition 6.0.6.}\nOn a l\'inclusion', '\\underline{Proposition} 6.0.6.\n\\underline{On a l\'inclusion}',
    'The number is not underlined; the statement is.')

add(432, '(6.0.7)', 'α_S = τ^{-1} ∘ (1/p) Ψ_p ∘ H(X)  .', '\\alpha_S=\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ H(X).',
    'formula', 'high', '\\frac1p\\,\\tau^{-1}\\circ\\psi_p', '\\tau^{-1}\\circ\\frac1p\\,\\psi_p',
    'The print has the factor 1/p between τ^{-1}∘ and ψ_p.')

add(432, '(6.0.8)', 'H(X) . R_S ⊂ R_S  ,', 'H(X)\\,R_S\\subset R_S,',
    'symbol', 'high', 'H(X)\\,R_S', 'H(X)\\cdot R_S', 'The print\'s multiplication dot is omitted.')

add(432, 'Corollaire 6.0.11', 'Corollaire (underlined) 6.0.11. On a l\'inclusion (underlined)',
    '\\underline{Corollaire 6.0.11.} On a l\'inclusion', 'underline', 'high',
    '\\underline{Corollaire 6.0.11.}\nOn a l\'inclusion', '\\underline{Corollaire} 6.0.11.\n\\underline{On a l\'inclusion}', '')

add(432, 'display of Corollaire 6.0.11', 'ᾱ_S W_S ⊂ W_S(1)  . (no parentheses)', '\\bar\\alpha_S(W_S)\\subset W_S(1).',
    'formula', 'high', '\\bar\\alpha_S(W_S)', '\\bar\\alpha_S W_S', 'The TeX adds parentheses.')

# ---------------- page 433 ----------------
add(433, 'Corollaire 6.0.12', 'Corollaire (underlined) 6.0.12. On a la congruence (underlined)',
    '\\underline{Corollaire 6.0.12.} On a la congruence', 'underline', 'high',
    '\\underline{Corollaire 6.0.12.}\nOn a la congruence', '\\underline{Corollaire} 6.0.12.\n\\underline{On a la congruence}', '')

add(433, 'Proposition 6.1, label', 'Proposition (underlined) 6.1. L\'opération (underlined)',
    '\\underline{Proposition 6.1.} L\'opération', 'underline', 'high',
    '\\underline{Proposition 6.1.}\nL\'opération', '\\underline{Proposition} 6.1.\n\\underline{L\'opération}', '')

add(433, 'Proposition 6.1', 'τ^1-linéaire with "linéaire" underlined', '$\\tau^{-1}$-linéaire', 'underline', 'high',
    '-linéaire', '-\\underline{linéaire}', '')

add(433, 'Proposition 6.1', 'est égale à l\'opération (underlined)', 'est égale à l\'opération', 'underline', 'high',
    'est égale à l\'opération', '\\underline{est égale à l\'opération}', '')

add(433, 'Proposition 6.1', 'L\'opération τ^1-linéaire (superscript 1 without minus)', '$\\tau^{-1}$-linéaire',
    'misprint_in_print', 'medium', '$\\tau^{-1}$', '$\\tau^{1}$',
    'The minus of the exponent is missing (clean scan there; p. 432 prints τ^{-1}-linéaire). The TeX silently corrects.',
    corrected='$\\tau^{-1}$')

add(433, '(6.1.1)', 'τ^{-1}Ψ_p ∘ (X_o f(X))^{p-1}  . (no 1/p, no ∘ between τ^{-1} and Ψ_p)',
    '\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ(X_0f(X))^{p-1}.',
    'extra', 'high', '\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ(X_0f(X))', '\\tau^{-1}\\psi_p\\circ(X_0f(X))',
    'The TeX adds the factor 1/p (mathematically wrong: (6.1.11) absorbs it) and a ∘ after τ^{-1}.')

add(433, '(6.1.2), end', 'H(X) = 1 + Σ_{i≥1} H_i(X)  (no punctuation)', 'H(X)=1+\\sum_{i\\geq1}H_i(X),',
    'punctuation', 'high', '\\sum_{i\\geq1}H_i(X),', '\\sum_{i\\geq1}H_i(X)', 'The TeX adds a comma.')

add(433, '(6.1.5)', 'H_i(X) . R_S(j) ⊂ R_S(i+j)  ,', 'H_i(X)\\,R_S(j)\\subset R_S(i+j),',
    'symbol', 'high', 'H_i(X)\\,R_S(j)', 'H_i(X)\\cdot R_S(j)', 'The print\'s multiplication dot is omitted.')

add(433, '(6.1.6)', '(α_S - (τ^{-1} over p) Ψ_p H_{p-1}(X))(R_S(1)) ⊂ p R_S  .',
    '\\alpha_S-\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ H_{p-1}(X)',
    'formula', 'high', '\\alpha_S-\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ H_{p-1}(X)',
    '\\alpha_S-\\frac{\\tau^{-1}}p\\,\\psi_pH_{p-1}(X)',
    'In the print τ^{-1} is the numerator of the fraction, and there is no ∘ (as in (4.6.14)).')

add(433, '(6.1.7)', '[(α_S)^{ord(q)} - ((τ^{-1} over p) Ψ_p . H_{p-1}(X))^{ord(q)}] R_S(1) ⊂ p R_S  .',
    '\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ H_{p-1}(X)',
    'formula', 'high', '\\left(\n\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ H_{p-1}(X)',
    '\\left(\n\\frac{\\tau^{-1}}p\\,\\psi_p\\cdot H_{p-1}(X)',
    'τ^{-1} is the numerator; no ∘ after it; a multiplication dot between ψ_p and H_{p-1}(X).')

# ---------------- page 434 ----------------
add(434, '(6.1.8), first line', 'H(X) = ∏_W Θ(A_W X_o X^W)  (no π)', '\\Theta(\\pi A_WX_0X^W)',
    'extra', 'high', '\\Theta(\\pi A_WX_0X^W)', '\\Theta(A_WX_0X^W)',
    'The TeX adds π. The print is right: Θ(X) = E(πX) by (4.1.7), as in (4.4.4).')

add(434, '(6.1.8), second line', 'Σ_{n≥0} ... ^{p^n} / p^n  (index n)', '\\sum_{r\\geq0}\\frac{(\\pi A_WX_0X^W)^{p^r}}{p^r}',
    'formula', 'high', '\\sum_{r\\geq0}\\frac{(\\pi A_WX_0X^W)^{p^r}}{p^r}',
    '\\sum_{n\\geq0}\\frac{(\\pi A_WX_0X^W)^{p^n}}{p^n}',
    'The print\'s summation index is n, not r. Apply before the next (misprint) fix.')

add(434, '(6.1.8), second line', 'numerator πA_W X_o X^W)^{p^n}: no opening parenthesis before π',
    '\\frac{(\\pi A_WX_0X^W)^{p^r}}', 'misprint_in_print', 'medium',
    '\\sum_{n\\geq0}\\frac{(\\pi', '\\sum_{n\\geq0}\\frac{\\pi',
    'The opening parenthesis is missing (present in the third line). The TeX silently supplies it. "old" is taken from '
    'the text after the previous fix (n for r).', corrected='\\sum_{n\\geq0}\\frac{(\\pi', after_previous=True)

add(434, '(6.1.8), third line', '∏_W ∏_{n≥0} exp((πA_W X_o X^W)^{p^n} / p^n)  (index n)',
    '\\prod_{r\\geq0} ... ^{p^r}}{p^r}', 'formula', 'high',
    '\\prod_{r\\geq0}\n\\exp\\!\\left(\\frac{(\\pi A_WX_0X^W)^{p^r}}{p^r}\\right)',
    '\\prod_{n\\geq0}\n\\exp\\!\\left(\\frac{(\\pi A_WX_0X^W)^{p^n}}{p^n}\\right)', 'Index n in the print.')

add(434, '(6.1.8), fifth line', '≡ exp (π Σ A_W X_o X^W) mod degré p  (Σ without index)', '\\pi\\sum_WA_WX_0X^W',
    'formula', 'high', '\\pi\\sum_WA_WX_0X^W', '\\pi\\sum A_WX_0X^W', 'The TeX adds the index W under Σ.')

add(434, '(6.1.8), last line', '≡ exp (π X_o F(X)) mod degré p,  (capital F)', '\\exp(\\pi X_0f(X))',
    'formula', 'high', '\\pi X_0f(X)', '\\pi X_0F(X)',
    'Capital F: the lift F(X) = Σ A_w X^w of f(X) defined in (4.4.2); the small f only comes back mod p in (6.1.11).')

add(434, '(6.1.9)', 'H_{p-1}(X) ≡ π^{p-1}X_o^{p-1}/(p-1)! F(X)^{p-1}  (congruence sign)', 'H_{p-1}(X)\n=\\frac{...}',
    'symbol', 'high', '=\\frac{\\pi^{p-1}X_0^{p-1}}', '\\equiv\\frac{\\pi^{p-1}X_0^{p-1}}',
    'The print has ≡ (three bars), not =.')

add(434, '(6.1.9)', 'F(X)^{p-1}  (capital F)', '\\,f(X)^{p-1}.', 'formula', 'high',
    '\\,f(X)^{p-1}.', '\\,F(X)^{p-1}.', 'Capital F (the lift of (4.4.2)), as in the last line of (6.1.8).')

add(434, '(6.1.10), end', 'π^{p-1}/p ≡ -1  mod  p  (no punctuation)', '\\equiv-1\\pmod p,',
    'punctuation', 'high', 'p,\n\\end{equation}\n\ndonc', 'p\n\\end{equation}\n\ndonc', 'The TeX adds a comma.')

add(434, '(6.1.11)', '(1/p) H_{p-1}(X) ≡ (X_o f(X)^{p-1} mod p ,  (one closing parenthesis)', '\\equiv(X_0f(X))^{p-1}',
    'misprint_in_print', 'high', '\\equiv(X_0f(X))', '\\equiv(X_0f(X)',
    'The parenthesis before X_o is never closed. The TeX silently closes it.', corrected='\\equiv(X_0f(X))')

add(434, 'Corollaire 6.1.12', 'Corollaire (underlined) 6.1.12. L\'opérateur linéaire (underlined)',
    '\\underline{Corollaire 6.1.12.} L\'opérateur linéaire', 'underline', 'high',
    '\\underline{Corollaire 6.1.12.}\nL\'opérateur linéaire', '\\underline{Corollaire} 6.1.12.\n\\underline{L\'opérateur linéaire}', '')

add(434, 'Corollaire 6.1.12, last line', 'n\'est autre que (underlined)', 'n\'est autre que', 'underline', 'high',
    'n\'est autre que', '\\underline{n\'est autre que}', '')

# ---------------- page 435 ----------------
add(435, 'Démonstration, first line', 'D\'après (6.1.1)  (no punctuation)', 'D\'après (6.1.1),',
    'punctuation', 'high', 'D\'après (6.1.1),', 'D\'après (6.1.1)', 'The TeX adds a comma.')

add(435, 'display, first line', '(τ^{-1}Ψ_p ∘ (X_o f(X))^{p-1})^{ord(q)}  (no 1/p, no ∘ after τ^{-1})',
    '\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ(X_0f(X))^{p-1}', 'extra', 'high',
    '\\frac1p\\,\\tau^{-1}\\circ\\psi_p\\circ(X_0f(X))^{p-1}', '\\tau^{-1}\\psi_p\\circ(X_0f(X))^{p-1}',
    'Same as (6.1.1): the TeX adds 1/p and a ∘.')

add(435, 'display, second line', '= Ψ_q ∏_{j=0}^{ord(a)-1} ...  (no ∘ after Ψ_q)', '\\psi_q\\circ\n\\prod_{j=0}^{\\operatorname{ord}(a)-1}',
    'extra', 'high', '\\psi_q\\circ\n\\prod_{j=0}^{\\operatorname{ord}(a)-1}', '\\psi_q\n\\prod_{j=0}^{\\operatorname{ord}(a)-1}',
    'The TeX adds ∘.')

add(435, 'display, second line', 'upper limit ord(a)-1', '\\prod_{j=0}^{\\operatorname{ord}(a)-1}',
    'misprint_in_print', 'high', None, None,
    'ord(a) for ord(q) (the next line has ord(q)-1). The TeX keeps the printed reading.',
    corrected='\\prod_{j=0}^{\\operatorname{ord}(q)-1}')

add(435, 'display, third line', '= Ψ_q ∏_{j=0}^{ord(q)-1} (X_o f(X))^{p^j(p-1)}  (no ∘ after Ψ_q)',
    '\\psi_q\\circ\n\\prod_{j=0}^{\\operatorname{ord}(q)-1}', 'extra', 'high',
    '\\psi_q\\circ\n\\prod_{j=0}^{\\operatorname{ord}(q)-1}', '\\psi_q\n\\prod_{j=0}^{\\operatorname{ord}(q)-1}',
    'The TeX adds ∘ (the last line prints Ψ_q∘).')

add(435, 'Corollaire 6.1.13', 'Corollaire (underlined) 6.1.13. On a la congruence mod (underlined) p :',
    '\\underline{Corollaire 6.1.13.} On a la congruence mod $p$ :', 'underline', 'high',
    '\\underline{Corollaire 6.1.13.}\nOn a la congruence mod $p$ :',
    '\\underline{Corollaire} 6.1.13.\n\\underline{On a la congruence mod} $p$ :', '')

add(435, 'display of Corollaire 6.1.13', 'det(1-t Ψ_q(X_o f(X))^{q-1} | W_S(1))  (no ∘ after Ψ_q)',
    '1-t\\,\\psi_q\\circ(X_0f(X))^{q-1}', 'extra', 'high',
    '1-t\\,\\psi_q\\circ(X_0f(X))^{q-1}', '1-t\\,\\psi_q(X_0f(X))^{q-1}', 'The TeX adds ∘.')

add(435, '(6.2.1)', 'élévation à la puissance q\'ième', 'puissance $q$-ième',
    'punctuation', 'high', '$q$-ième', '$q$\'ième', 'Apostrophe, not hyphen (cf. "$p$\'ième" in (4.2.2)).')

add(435, '(6.2.2), last term', '... ⟶ 𝒪_V ⟶ 𝒪  ,  (script O, the same handwritten letter as in 𝒪_V, for 0)',
    '\\longrightarrow\\mathcal O_V\\longrightarrow0,', 'misprint_in_print', 'high',
    'O_V\\longrightarrow0,', 'O_V\\longrightarrow\\mathcal O,',
    'The final 0 of the exact sequence is printed as the script 𝒪 (the first 0 is typed). The TeX silently corrects. '
    'Same in both rows of (6.2.3).', corrected='O_V\\longrightarrow0,')

add(435, '(6.2.3), top row, last node', '𝒪_V ⟶ 𝒪 (script O for 0)', '0\\\\', 'misprint_in_print', 'high',
    '"\\mathfrak F_q"\'] &\n0\\\\', '"\\mathfrak F_q"\'] &\n\\mathcal O\\\\',
    'As in (6.2.2). The TeX silently corrects.', corrected='"\\mathfrak F_q"\'] &\n0\\\\')

add(435, '(6.2.3), bottom row, last node', '𝒪_V ⟶ 𝒪  . (script O for 0)', '0 .', 'misprint_in_print', 'high',
    '\\arrow[r] &\n0 .', '\\arrow[r] &\n\\mathcal O .',
    'As in (6.2.2). The TeX silently corrects.', corrected='\\arrow[r] &\n0 .')


# ---------------- validation ----------------
texts = {}
for p in sorted({f['page'] for f in F}):
    with open(os.path.join(BATCH, 'page_%d.tex' % p), encoding='utf-8', newline='') as fh:
        texts[p] = fh.read()
    assert '\r' not in texts[p]

ok = True
work = dict(texts)  # sequentially edited copy per page
for i, f in enumerate(F):
    fx = f['fix']
    if fx is None:
        continue
    p = f['page']
    base = work[p] if f['_after_previous'] else texts[p]
    n = base.count(fx['old'])
    marker_hit = any(line.startswith('%%%%%%%%%%') for line in fx['old'].split('\n'))
    if n != 1 or marker_hit:
        ok = False
        print('BAD', i, p, n, repr(fx['old']))
    # apply to working copy (in order); check old still applies there too
    if work[p].count(fx['old']) != 1:
        ok = False
        print('BAD-SEQ', i, p, work[p].count(fx['old']), repr(fx['old']))
    else:
        work[p] = work[p].replace(fx['old'], fx['new'], 1)

# overlap check among fixes on the same page against the original text (except declared sequential ones)
for p in texts:
    spans = []
    for i, f in enumerate(F):
        if f['page'] != p or f['fix'] is None or f['_after_previous']:
            continue
        s = texts[p].find(f['fix']['old'])
        spans.append((s, s + len(f['fix']['old']), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print('OVERLAP', p, a, b)

for f in F:
    del f['_after_previous']

print('ok' if ok else 'PROBLEMS')
counts = {}
for f in F:
    k = 'misprint' if f['kind'] == 'misprint_in_print' else 'normal'
    counts.setdefault(f['page'], {'normal': 0, 'misprint': 0})[k] += 1
print(counts)
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
    print('written', OUT, len(F))
