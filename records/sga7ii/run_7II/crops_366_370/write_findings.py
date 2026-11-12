import json, sys
sys.stdout.reconfigure(encoding='utf-8')
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_366_370_recheck.json"
F = []
def add(**k):
    F.append(k)

# ---- page 366
add(page=366,
    where="Définition 1.0 (continued), first line: 'qui est nilpotente (ou, ce qui revient au même, posant'",
    scan="'qui est nilpotente' underlined, then ' (' not underlined; the underline restarts at 'ou'",
    tex=r"\underline{qui est nilpotente (ou, ce qui revient au même, posant}",
    kind="underline", confidence="medium",
    fix={"old": r"\underline{qui est nilpotente (ou, ce qui revient au même, posant}",
         "new": r"\underline{qui est nilpotente} (\underline{ou, ce qui revient au même, posant}"},
    note=r"The TeX runs the underline through the opening parenthesis; the print breaks it there (the same page already writes '(\underline{de dimension} $n$)'). The inner commas are left to the global rule.")
add(page=366,
    where="Définition 1.0 (continued), second line: 'si l'opération p^M-linéaire'",
    scan="'si l'opération' underlined; 'p^M-' not underlined; 'linéaire' underlined",
    tex=r"\underline{si l'opération $p^M$-linéaire}",
    kind="underline", confidence="medium",
    fix={"old": r"\underline{si l'opération $p^M$-linéaire}",
         "new": r"\underline{si l'opération} $p^M$-\underline{linéaire}"},
    note=r"The TeX underlines the formula p^M and the hyphen; the print does not (compare '$p$-\underline{linéaire}' in Définition 1.0 on the previous page).")
add(page=366,
    where="end of Définition 1.0: '(ou, ce qui revient au même, ... tue H^{dimX}(X,O_X).'",
    scan="tue H^{dimX}(X,O_X).  (the parenthesis opened before 'ou' is never closed)",
    tex=r"\underline{tue} $H^{\dim X}(X,\mathcal{O}_X)$.",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"\underline{tue} $H^{\dim X}(X,\mathcal{O}_X)$).",
    note="Unbalanced parenthesis in the print: the parenthetical clause opened at '(ou,' on the first line has no closing parenthesis. The TeX keeps the printed reading.")
add(page=366,
    where="Théorème 1.1: 'parmi toute les intersections complètes'",
    scan="toute les",
    tex="parmi toute les intersections",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="parmi toutes les intersections",
    note="Agreement error in the print; the TeX keeps the printed reading.")

# ---- page 367
add(page=367,
    where="after (1.1.2): 'Cela donne le théroème si p = 1'",
    scan="théroème",
    tex="le théroème si",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected="le théorème si",
    note="Typing error (transposed letters); the TeX keeps the printed reading.")
add(page=367,
    where="after (1.1.2): 'pour toute intersection complète vérifiante (1.1.0)'",
    scan="vérifiante",
    tex="complète vérifiante (1.1.0)",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="complète vérifiant (1.1.0)",
    note="The present participle takes a direct object here and is invariable; the TeX keeps the printed reading.")
add(page=367,
    where="Proposition 1.1.5: 'Si X n'a pas des points F_q-rationnels'",
    scan="n'a pas des points",
    tex=r"\underline{n'a pas des points}",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\underline{n'a pas de points}",
    note="After the negation the partitive is 'de'; the TeX keeps the printed reading.")

# ---- page 369
add(page=369,
    where="(1.2.1)",
    scan="H(X_1),...,X_{n+2}) ∈ F_q[X_1,...,X_{n+2}]",
    tex=r"H(X_1),\dots,X_{n+2})",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"H(X_1,\dots,X_{n+2})",
    note="Stray closing parenthesis after X_1 in the print; the TeX keeps it.")
add(page=369,
    where="before (1.2.3): 'des éléments de E qui sont linéairement indépendant sur F_q'",
    scan="indépendant",
    tex="linéairement indépendant sur",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="linéairement indépendants sur",
    note="Agreement with 'éléments'; the TeX keeps the printed reading.")
add(page=369,
    where="(1.2.4)",
    scan="Σ with i below and r above: Σ_i^r d_i ≥ n+r+1 ,",
    tex=r"\sum_i^r d_i",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected=r"\sum_{i=1}^r d_i",
    note="The lower limit lacks '=1' (cf. (1.1.0) and Proposition 1.2); the TeX keeps the printed reading.")
add(page=369,
    where="(1.2.6), first line",
    scan="d_1 ≥ a_o",
    tex=r"d_1 & \geq & a_o",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"d_1 & \geq & a_1",
    note="Wrong index: H_1 is a form in the a_1 variables X_1,...,X_{a_1} (p. 370), so the condition is d_1 ≥ a_1 (= a_1 - a_0 with a_0 = 0); d_1 ≥ a_0 is empty. The TeX keeps the printed a_o (o for zero is the global convention).")

# ---- page 370
add(page=370,
    where="after the first display: 'en a_i - a_{i-1} variable qui a la propriété (1.2.2)'",
    scan="variable  qui (a double space after 'variable')",
    tex="$a_i - a_{i-1}$ variable",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected="$a_i - a_{i-1}$ variables",
    note="Plural needed; the TeX keeps the printed reading.")
add(page=370,
    where="display 'H_1(X_1,...,X_{a_1}), .... , H_r(...)'",
    scan="H_r(X_{a_{r-1}},...,X_{a_r})",
    tex=r"H_r(X_{a_{r-1}},\dots,X_{a_r})",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"H_r(X_{a_{r-1}+1},\dots,X_{a_r})",
    note="By the definition of H_i just above, the first variable of H_r is X_{a_{r-1}+1}; the TeX keeps the printed reading.")
add(page=370,
    where="Démonstration of Théorème 1.3: '(paramétérisées par)'",
    scan="paramétérisées",
    tex="(paramétérisées par)",
    kind="misprint_in_print", confidence="low", fix=None,
    corrected="(paramétrisées par)",
    note="Misspelling (extra 'é'); the TeX keeps the printed reading.")
add(page=370,
    where="(1.3.1)",
    scan="P(H^o(X,O_X(d)) = U (three opening, two closing parentheses)",
    tex=r"\mathbb{P}(H^0(X,\mathcal{O}_X(d)) = U",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\mathbb{P}(H^0(X,\mathcal{O}_X(d))) = U",
    note="The print drops one closing parenthesis; the TeX keeps the printed reading.")

# order keys
keys = ["page","where","scan","tex","kind","confidence","fix","corrected","note"]
G = []
for f in F:
    g = {}
    for k in keys:
        if k in f:
            g[k] = f[k]
    G.append(g)
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(G, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(G), "findings written")
