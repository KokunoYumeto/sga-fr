import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
D = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5'
OUT = D + r'\findings_151_155.json'
N = '\n'

LABEL_NOTE = ("Exposé III B prints its run-in labels with ' -', as Exposé III does. The III B statement environment "
              "(s5.tex line 4329) still appends a full stop, so this edit gives the print's '{L} -' only together "
              "with an environment that adds none for III B (as Exposé III, line 1938); same as the labels of pp. 146-150.")
UL_NOTE = ("The print underlines the statements of Exposé III B word group by word group (letters, formulas and "
           "punctuation not underlined); the III B TeX has no underlining at all. \\emph is the file's command for "
           "the print's underline in statements (Exposé III).")
PMOD_NOTE = "\\pmod adds parentheses the print does not have; \\mod gives the plain 'mod'."

F = []


def add(page, where, scan, tex, kind, conf, fix, note='', corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------- page 151
add(151, "first paragraph, 'Par l'isomorphisme de dualité (SGA 4 XVIII 3.19.6) (plus un passage à la limite), on a'",
    "'(SGA 4 XVIII 3.19.6) (plus un passage à la limite), on a': the second clause in parentheses",
    "(SGA 4 XVIII 3.19.6), plus un passage à la limite, on a",
    "punctuation", "high",
    fx(r"(SGA 4 XVIII 3.19.6), plus un passage à la limite, on a",
       r"(SGA 4 XVIII 3.19.6) (plus un passage à la limite), on a"),
    "The TeX turns the printed parentheses into commas.")
add(151, "display of the inclusions f', g', f, g: second line, 'f : T - Z ↪ T'",
    "f : T - Z ↪ T (a clear Z; the line above reads f' : Z - Y ↪ Z)",
    r"f:T-Y\hookrightarrow T",
    "misprint_in_print", "high",
    fx(r"f:T-Y\hookrightarrow T", r"f:T-Z\hookrightarrow T"),
    "f is the inclusion of T - Y in T, as f' : Z - Y ↪ Z above (g : T - (X ∪ Y) ↪ T - Y lands in its source; "
    "(2.6.3) applies Rf_* to g_!(...)). The TeX silently corrects the printed Z; the edit restores it and changes only that letter.",
    corrected=r"f:T-Y\hookrightarrow T")
add(151, "same display, end of the second line 'g : T - (X ∪ Y) ↪ T - Y ,'",
    "a comma after T - Y, as after Z - Y at the end of the first line",
    r"g:T-(X\cup Y)\hookrightarrow T-Y (no comma)",
    "punctuation", "high",
    fx(r"\hookrightarrow T-Y" + N + r"\]", r"\hookrightarrow T-Y," + N + r"\]"))
add(151, "last paragraph, 'une ramification modérée (l'action de l'inertie ... pour un nombre premier ℓ ≠ p) , puis traiterons'",
    "the clause 'l'action de l'inertie se faisant plus précisément à travers un ℓ-groupe, pour un nombre premier ℓ ≠ p' stands in parentheses",
    "the clause set off by commas",
    "punctuation", "high",
    fx(r"modérée, l'action de l'inertie se faisant plus précisément à travers un $\ell$-groupe, pour un nombre premier $\ell\ne p$, puis",
       r"modérée (l'action de l'inertie se faisant plus précisément à travers un $\ell$-groupe, pour un nombre premier $\ell\ne p$), puis"),
    "Both parentheses in one edit.")

# ---------------- page 152
add(152, "heading of n° 3",
    "'3.- Réduction au cas modéré.' (underlined; a hyphen right after '3.', a full stop after the title)",
    r"\subsection*{3. Réduction au cas modéré}",
    "punctuation", "high",
    fx(r"\subsection*{3. Réduction au cas modéré}", r"\subsection*{3.- Réduction au cas modéré.}"),
    "Underlined titles end with a full stop in the print; the underline is the accepted \\subsection* setting. "
    "This heading has no space between '3.' and the hyphen (p. 146 prints '2. - ').")
add(152, "end of 3.2, 'l'image inverse de A (resp. B) dans T' , E' = ...'",
    "'dans T' ,' and then the formula E' = (P ⊗_S Q)|T' - (X' ∪ Y') = ... on the next line; no 'et'",
    "dans $T'$, et",
    "extra", "high",
    fx(r"dans $T'$, et", r"dans $T'$,"),
    "Word added by the TeX.")

# ---------------- page 153
add(153, "'pourvu que l'on s'assure que A', B' vérifient les hyptohèses de position générale de 1.2'",
    "hyptohèses (t and o transposed)",
    "hypothèses",
    "misprint_in_print", "high",
    fx(r"vérifient les hypothèses", r"vérifient les hyptohèses"),
    "Typing error; the TeX silently corrects it. The edit changes only the two transposed letters.",
    corrected="hypothèses")
add(153, "Lemme 3.3, label",
    "'Lemme 3.3 - Sous les hypothèses de 1.2, ...' (Lemme underlined, then ' -', no full stop)",
    r"\begin{statement}{Lemme 3.3}  (renders 'Lemme 3.3.')",
    "punctuation", "high",
    fx(r"\begin{statement}{Lemme 3.3}", r"\begin{statement}{Lemme 3.3 -}"),
    LABEL_NOTE.replace('{L}', 'Lemme 3.3'))
add(153, "Lemme 3.3, first line 'Sous les hypothèses de 1.2, a et b étant des immersions fermées, soient'",
    "underlined: 'Sous les hypothèses de', 'et', 'étant des immersions fermées' and 'soient' (not 1.2, a, b)",
    "no underline",
    "underline", "high",
    fx(r"Sous les hypothèses de 1.2, $a$ et $b$ étant des immersions fermées, soient",
       r"\emph{Sous les hypothèses de} 1.2, $a$ \emph{et} $b$ \emph{étant des immersions fermées}, \emph{soient}"),
    UL_NOTE)
add(153, "Lemme 3.3, 'des revêtements finis de S-traits strictement locaux, de même degré d'",
    "underlined: 'des revêtements finis de', 'traits strictement locaux' (not S-), 'de même degré' (across the line break; not d)",
    "no underline",
    "underline", "high",
    fx(r"des revêtements finis de $S$-traits strictement locaux, de même degré",
       r"\emph{des revêtements finis de} $S$-\emph{traits strictement locaux}, \emph{de même degré}"),
    "Underlined statement (see the first underline finding of Lemme 3.3).")
add(153, "Lemme 3.3, 'de même degré d , notons A' (resp. B')'",
    "'d , notons': a comma and a small n, one sentence; 'notons' underlined",
    "$d$. Notons",
    "punctuation", "high",
    fx(r"$d$. Notons", r"$d$, \emph{notons}"),
    "The TeX splits the statement into two sentences. The new text also carries the print's underline of 'notons'.")
add(153, "Lemme 3.3, 'l'image inverse de A (resp. B) dans X' ×_S Y' . Alors les couples'",
    "underlined: 'l'image inverse de', 'dans', 'Alors les couples' (not the letters, not X' ×_S Y')",
    "no underline",
    "underline", "high",
    fx(r"l'image inverse de $A$ (resp. $B$) dans $X'\times_S Y'$. Alors les couples",
       r"\emph{l'image inverse de} $A$ (resp. $B$) \emph{dans} $X'\times_S Y'$. \emph{Alors les couples}"),
    "Underlined statement.")
add(153, "Lemme 3.3, 'sont chacun en position générale (au sens de 1.2) (*)'",
    "'sont chacun en po-sition générale (au sens de' underlined across the line break; '1.2) (*).' not",
    "no underline",
    "underline", "high",
    fx(r"sont chacun en position générale (au sens de 1.2)",
       r"\emph{sont chacun en position générale (au sens de} 1.2)"),
    "Underlined statement.")
add(153, "Lemme 3.4, label",
    "'Lemme 3.4 - Soient ...' (Lemme underlined, then ' -', no full stop)",
    r"\begin{statement}{Lemme 3.4}  (renders 'Lemme 3.4.')",
    "punctuation", "high",
    fx(r"\begin{statement}{Lemme 3.4}", r"\begin{statement}{Lemme 3.4 -}"),
    LABEL_NOTE.replace('{L}', 'Lemme 3.4'))
add(153, "Lemme 3.4, first line 'Soient X ← W → Y des morphismes finis de S-traits,'",
    "underlined: 'Soient', 'des morphismes finis de', 'traits' (not S-, not the comma)",
    "no underline",
    "underline", "high",
    fx(r"Soient $X\xleftarrow{s_1}W\xrightarrow{s_2}Y$ des morphismes finis de $S$-traits,",
       r"\emph{Soient} $X\xleftarrow{s_1}W\xrightarrow{s_2}Y$ \emph{des morphismes finis de} $S$-\emph{traits},"),
    "Underlined statement.")
add(153, "Lemme 3.4, 's = (s_1,s_2) : W → X ×_S Y , u, v, w des uniformisantes de X, Y, W'",
    "'X ×_S Y , u, v, w des uniformisantes': no 'et'",
    "$s=(s_1,s_2):W\\to X\\times_SY$, et $u,v,w$",
    "extra", "high",
    fx(r"X\times_SY$, et $u,v,w$", r"X\times_SY$, $u,v,w$"),
    "Word added by the TeX.")
add(153, "Lemme 3.4, 'des uniformisantes de X, Y, W respectivement, de sorte que'",
    "underlined: 'des uniformisantes de', 'respecti-vement', 'de sorte que' (not the comma)",
    "no underline",
    "underline", "high",
    fx(r"des uniformisantes de $X,Y,W$ respectivement, de sorte que",
       r"\emph{des uniformisantes de} $X,Y,W$ \emph{respectivement}, \emph{de sorte que}"),
    "Underlined statement.")
add(153, "Lemme 3.4, display 's_1^*u = aw^m mod w^{m+1} , s_2^*v = bw^n mod w^{n+1} ,'",
    "plain 'mod' in both congruences, no parentheses",
    r"\pmod {w^{m+1}} and \pmod {w^{n+1}} (render '(mod ...)')",
    "formula", "high",
    fx(r"aw^m\pmod {w^{m+1}},\qquad" + N + r"s_2^*v=bw^n\pmod {w^{n+1}}",
       r"aw^m\mod {w^{m+1}},\qquad" + N + r"s_2^*v=bw^n\mod {w^{n+1}}"),
    PMOD_NOTE)
add(153, "Lemme 3.4, 'avec a,b ∈ k* . Alors : (i)'",
    "'avec' and 'Alors' underlined",
    "no underline",
    "underline", "high",
    fx(r"avec $a,b\in k^*$. Alors:", r"\emph{avec} $a,b\in k^*$. \emph{Alors}:"),
    "Underlined statement.")
add(153, "Lemme 3.4, '(i) Si m < n'",
    "'Si' with a capital S (underlined)",
    "(i) si $m<n$",
    "word", "high",
    fx(r"(i) si $m<n$", r"(i) \emph{Si} $m<n$"),
    "Capital S in the print; the new text also carries the print's underline of 'Si'.")
add(153, "Lemme 3.4 (i), 's(W) est tangent à X en z = (x,y)'",
    "'est tangent à' and 'en' underlined",
    "no underline",
    "underline", "high",
    fx(r"est tangent à $X$ en", r"\emph{est tangent à} $X$ \emph{en}"),
    "Underlined statement.")
add(153, "Lemme 3.4, end of (i), 'en z = (x,y).'",
    "a full stop after (x,y); (ii) starts a new indented line",
    "$z=(x,y)$; (ii)",
    "punctuation", "high",
    fx(r"$z=(x,y)$;", r"$z=(x,y)$."),
    "The new line before (ii) is layout and is left out of the edit.")
add(153, "Lemme 3.4, '(ii) Si m = n'",
    "'Si' with a capital S (underlined)",
    "(ii) si $m=n$",
    "word", "high",
    fx(r"(ii) si $m=n$", r"(ii) \emph{Si} $m=n$"),
    "Capital S in the print; the new text also carries the print's underline of 'Si'.")
add(153, "Lemme 3.4 (ii), 'est tangent au sous-schéma de X ×_S Y d'équation'",
    "'est tangent au sous-schéma de' and 'd'équation' underlined",
    "no underline",
    "underline", "high",
    fx(r"est tangent au sous-schéma de $X\times_SY$ d'équation",
       r"\emph{est tangent au sous-schéma de} $X\times_SY$ \emph{d'équation}"),
    "Underlined statement.")

# ---------------- page 154
add(154, "'Dans la situation de 3.4, nous définirons la pente de W par rapport à ((X,u), (Y,v))'",
    "'pente' underlined (the term being defined)",
    "la pente de $W$ (no underline)",
    "underline", "high",
    fx(r"définirons la pente de", r"définirons la \emph{pente} de"))
add(154, "Lemme 3.5, label",
    "'Lemme 3.5 - Soient ...' (Lemme underlined, then ' -', no full stop)",
    r"\begin{statement}{Lemme 3.5}  (renders 'Lemme 3.5.')",
    "punctuation", "high",
    fx(r"\begin{statement}{Lemme 3.5}", r"\begin{statement}{Lemme 3.5 -}"),
    LABEL_NOTE.replace('{L}', 'Lemme 3.5'))
add(154, "Lemme 3.5, 'Soient f : X' → X , g : Y' → Y des morphismes finis de S-traits de même indice de ramification d'",
    "underlined: 'Soient', 'des morphismes finis de', 'traits' and 'de même indice de ramification' (across the line break; not S-, not d)",
    "no underline",
    "underline", "high",
    fx(r"Soient $f:X'\to X$, $g:Y'\to Y$ des morphismes finis de $S$-traits de même indice de ramification",
       r"\emph{Soient} $f:X'\to X$, $g:Y'\to Y$ \emph{des morphismes finis de} $S$-\emph{traits de même indice de ramification}"),
    UL_NOTE)
add(154, "Lemme 3.5, 'de même indice de ramification d , u , v , u' , v' des uniformisantes'",
    "no 'et' before u , v , u' , v'",
    "$d$, et $u,v,u',v'$",
    "extra", "high",
    fx(r"$d$, et $u,v,u',v'$", r"$d$, $u,v,u',v'$"),
    "Word added by the TeX.")
add(154, "Lemme 3.5, 'des uniformisantes de X , Y , X' , Y' respectivement. Il existe alors C ∈ k*'",
    "underlined: 'des uniformisantes de', 'respectivement' (not the full stop), 'Il existe alors'",
    "no underline",
    "underline", "high",
    fx(r"des uniformisantes de $X,Y,X',Y'$ respectivement. Il existe alors",
       r"\emph{des uniformisantes de} $X,Y,X',Y'$ \emph{respectivement}. \emph{Il existe alors}"),
    "Underlined statement.")
add(154, "Lemme 3.5, 'tel que, pour tout diagramme commutatif de morphismes finis de S-traits'",
    "underlined: 'tel que', 'pour tout diagramme com-mutatif de morphismes finis de', 'traits' (not the comma, not S-)",
    "no underline",
    "underline", "high",
    fx(r"tel que, pour tout diagramme commutatif de morphismes finis de $S$-traits",
       r"\emph{tel que}, \emph{pour tout diagramme commutatif de morphismes finis de} $S$-\emph{traits}"),
    "Underlined statement.")
add(154, "Lemme 3.5, diagram, middle vertical arrow W' → W",
    "h stands to the left of the arrow (as f; g stands to the right of the right arrow)",
    '\\arrow[d,"h"] (label to the right)',
    "other", "high",
    fx(r'\arrow[d,"h"]', r'''\arrow[d,"h"']'''))
add(154, "Lemme 3.5, diagram, bottom row X ← W → Y",
    "s_1 and s_2 stand above their arrows, as s'_1 and s'_2 in the top row",
    '''\\arrow[l,"s_1"] \\arrow[r,"s_2"'] (both labels below the arrows)''',
    "other", "high",
    fx(r'''W \arrow[l,"s_1"] \arrow[r,"s_2"']''', r'''W \arrow[l,"s_1"'] \arrow[r,"s_2"]'''))
add(154, "Lemme 3.5, after the diagram, 'on ait λ = C λ'^d , où λ (resp. λ') est la pente de W (resp. W') par rapport à'",
    "underlined: 'on ait', 'où', 'est la pente de', 'par rapport à' (across the line break)",
    "no underline",
    "underline", "high",
    fx(r"on ait $\lambda=C{\lambda'}^d$, où $\lambda$ (resp. $\lambda'$) est la pente de $W$ (resp. $W'$) par rapport à",
       r"\emph{on ait} $\lambda=C{\lambda'}^d$, \emph{où} $\lambda$ (resp. $\lambda'$) \emph{est la pente de} $W$ (resp. $W'$) \emph{par rapport à}"),
    "Underlined statement.")
add(154, "proof of 3.5, display 'f*u = α u'^d mod u'^{d+1} , g*v = β v'^d mod v'^{d+1} ,'",
    "plain 'mod', no parentheses",
    r"\pmod {u'{}^{d+1}}, \pmod {v'{}^{d+1}}",
    "formula", "high",
    fx(r"\alpha u'{}^d\pmod {u'{}^{d+1}},\qquad" + N + r"g^*v=\beta v'{}^d\pmod {v'{}^{d+1}}",
       r"\alpha u'{}^d\mod {u'{}^{d+1}},\qquad" + N + r"g^*v=\beta v'{}^d\mod {v'{}^{d+1}}"),
    PMOD_NOTE)
add(154, "proof of 3.5, display 's_1^*u = aw^m mod w^{m+1} , s_2^*v = bw^n mod w^{n+1} ,'",
    "plain 'mod', no parentheses",
    r"\pmod {w^{m+1}}, \pmod {w^{n+1}}",
    "formula", "high",
    fx(r"aw^m\pmod {w^{m+1}},\qquad" + N + r"s_2^*v=bw^n\pmod {w^{n+1}}",
       r"aw^m\mod {w^{m+1}},\qquad" + N + r"s_2^*v=bw^n\mod {w^{n+1}}"),
    PMOD_NOTE)
add(154, "proof of 3.5, display 's'_1^*u' = a'w'^{m'} mod w'^{m'+1} , s'_2^*v' = b'w'^{n'} mod w'^{n'+1} ,'",
    "plain 'mod', no parentheses",
    r"\pmod {w'{}^{m'+1}}, \pmod {w'{}^{n'+1}}",
    "formula", "high",
    fx(r"a'w'{}^{m'}\pmod {w'{}^{m'+1}},\qquad" + N + r"s'_2{}^*v'=b'w'{}^{n'}\pmod {w'{}^{n'+1}}",
       r"a'w'{}^{m'}\mod {w'{}^{m'+1}},\qquad" + N + r"s'_2{}^*v'=b'w'{}^{n'}\mod {w'{}^{n'+1}}"),
    PMOD_NOTE)
add(154, "proof of 3.5, display 'h^*w = γ w'^r mod w'^{r+1} ,'",
    "plain 'mod', no parentheses",
    r"\pmod {w'{}^{r+1}}",
    "formula", "high",
    fx(r"\gamma w'{}^r\pmod {w'{}^{r+1}}", r"\gamma w'{}^r\mod {w'{}^{r+1}}"),
    PMOD_NOTE)

# ---------------- page 155
add(155, "top of the page",
    "p. 155 begins 'm'd = rm , n'd = rn , d'où m'/n' = m/n . Supposons d'abord m = n .'; "
    "p. 154 ends '... La commutativité des carrés du diagramme entraîne'",
    "the display '\\[ m'd=rm,\\qquad n'd=rn, \\]' and 'd'où $m'/n'=m/n$.' are the last four lines of page_154.tex "
    "(s5.tex lines 4904-4907); the folio-155 marker (line 4908) follows them",
    "marker", "high",
    None,
    "Page 155 really begins at the '\\[' that opens 'm'd=rm,\\qquad n'd=rn,' (s5.tex line 4904 in both layers, "
    "as of 20:16). Exact fix: python -I move_marker.py 5 155 '\\[' --before (simulated in memory on both layers: "
    "the marker then stands between '... du diagramme entraîne' and '\\[', and no other text moves). "
    "No edit of this batch has its 'old' in the four lines that move.")
add(155, "display '(fs'_1)^*u = αa'^d w'^N mod w'^{N+1} , (s_1h)^*u = a γ^m w'^N mod w'^{N+1} ,'",
    "plain 'mod', no parentheses",
    r"\pmod {w'{}^{N+1}} twice",
    "formula", "high",
    fx(r"w'{}^N\pmod {w'{}^{N+1}},\qquad" + N + r"(s_1h)^*u=a\gamma^m w'{}^N\pmod {w'{}^{N+1}}",
       r"w'{}^N\mod {w'{}^{N+1}},\qquad" + N + r"(s_1h)^*u=a\gamma^m w'{}^N\mod {w'{}^{N+1}}"),
    PMOD_NOTE)
add(155, "'Soient (x_i)_{1 ≤ i ≤ m} (resp. (y_j)_{1 ≤ i ≤ m}) les points de Ã (resp. B̃)'",
    "(y_j)_{1 ≤ i ≤ m}: the index range of (x_i) repeated",
    r"$(y_j)_{1\le i\le m}$",
    "misprint_in_print", "high",
    None,
    "The points y_j of B̃ above y are indexed by 1 ≤ j ≤ n (B̃ = ∐_{1≤j≤n} B_j below). The TeX keeps the printed reading.",
    corrected=r"$(y_j)_{1\le j\le n}$")
add(155, "'Choisissons des uniformisantes u , v , u' , v\" , de X , Y , X' , Y' respectivement'",
    "v\" (double prime, as in U\" of p. 152) and a comma before 'de'",
    r"$u,v,u',v''$ de $X,Y,X',Y'$",
    "misprint_in_print", "high",
    fx(r"$u,v,u',v''$ de", r"$u,v,u',v''$, de"),
    "The uniformizer of Y' is v' (used below in ((X',u'),(Y',v'))); the typed double prime and the stray comma "
    "are one typing slip. The TeX keeps v'' but drops the comma; the edit restores only the comma.",
    corrected=r"$u,v,u',v'$ de")
add(155, "same sentence, 'respectivement, notons λ_i (resp. μ_j)'",
    "a comma after 'respectivement'",
    "respectivement; notons",
    "punctuation", "high",
    fx(r"respectivement; notons", r"respectivement, notons"))
add(155, "(2), third condition 'λ'_j ≠ μ'_j pour tous i , j'",
    "λ'_j ≠ μ'_j (j under the λ', a clear descender, as under μ'_j)",
    r"\lambda'_i\ne\mu'_j",
    "misprint_in_print", "high",
    fx(r"\lambda'_i\ne\mu'_j", r"\lambda'_j\ne\mu'_j"),
    "(2) is (1) for the primed data ('pour tous i , j', and (1) prints λ_i ≠ μ_j); the TeX silently corrects the index. "
    "The edit changes only that index.",
    corrected=r"\lambda'_i\ne\mu'_j")

# ---------------- checks
ok = True
pages = {}
for p in (151, 152, 153, 154, 155):
    pages[p] = open(D + r'\b151_155\page_%03d.tex' % p, encoding='utf-8', newline='').read()
spans = {}
for i, f in enumerate(F):
    if f['fix'] is None:
        continue
    t = pages[f['page']]
    old = f['fix']['old']
    c = t.count(old)
    if c != 1:
        ok = False
        print('COUNT', c, f['page'], repr(old))
        continue
    k = t.find(old)
    for (a, b, j) in spans.get(f['page'], []):
        if k < b and a < k + len(old):
            ok = False
            print('OVERLAP', f['page'], i, j)
    spans.setdefault(f['page'], []).append((k, k + len(old), i))
    if '%%%%%%%%%%' in old:
        ok = False
        print('MARKER IN OLD', i)
cnt = {}
for f in F:
    a = cnt.setdefault(f['page'], [0, 0])
    a[1 if f['kind'] == 'misprint_in_print' else 0] += 1
print('counts', cnt, 'total', len(F), 'ok', ok)
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('written', OUT)
