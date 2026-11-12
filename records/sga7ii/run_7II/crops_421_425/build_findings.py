# Builds findings_421_425_recheck.json and checks every fix's "old" (exactly once)
# and every "tex" (present) against the page files. "⏎" stands for a line break.
import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(RUN, 'b421_425')
OUT = os.path.join(RUN, 'findings_421_425_recheck.json')

def R(s):
    return s.replace('⏎', '\n') if isinstance(s, str) else s

def fix(old, new):
    return {"old": R(old), "new": R(new)}

F = []
def add(page, where, scan, tex, kind, conf, fx, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": R(tex), "kind": kind,
         "confidence": conf, "fix": fx}
    if kind == 'misprint_in_print':
        d["corrected"] = R(corrected)
    d["note"] = note
    F.append(d)

# ---------------- page 421 ----------------
add(421, "Lemme 4.5.8, heading",
    "Lemme 4.5.8 (ou lemme de la trace (DWORK)). -- underlined: 'Lemme' and 'ou lemme de la trace' only",
    r"\underline{Lemme 4.5.8 (ou lemme de la trace (DWORK)).}",
    "underline", "high",
    fix(r"\underline{Lemme 4.5.8 (ou lemme de la trace (DWORK)).}",
        r"\underline{Lemme} 4.5.8 (\underline{ou lemme de la trace} (DWORK))."),
    "The number, the opening parenthesis and '(DWORK)).' are not underlined.")

add(421, "Lemme 4.5.8, statement before the display",
    "Soient [ul] b ∈ ℚ, b > 0, k ∈ ℤ, k ≥ 2, et [ul] G ∈ L(b/k). Alors le composé [ul]",
    r"\underline{Soient $b\in\mathbb Q$, $b>0$, $k\in\mathbb Z$, $k\geq2$, et⏎$G\in L(b/k)$. Alors le composé}",
    "underline", "high",
    fix(r"\underline{Soient $b\in\mathbb Q$, $b>0$, $k\in\mathbb Z$, $k\geq2$, et⏎$G\in L(b/k)$. Alors le composé}",
        r"\underline{Soient} $b\in\mathbb Q$, $b>0$, $k\in\mathbb Z$, $k\geq2$, \underline{et}⏎$G\in L(b/k)$. \underline{Alors le composé}"),
    "The print underlines the words only; the formulas are not underlined.")

add(421, "Lemme 4.5.8, statement after the display",
    "noté [ul] ψ_k ∘ G, est complètement continu, et sa trace [ul] [cf. [4]] est donnée par la formule [ul]",
    r"\underline{noté $\psi_k\circ G$, est complètement continu, et sa trace⏎[cf. [4]] est donnée par la formule}",
    "underline", "high",
    fix(r"\underline{noté $\psi_k\circ G$, est complètement continu, et sa trace⏎[cf. [4]] est donnée par la formule}",
        r"\underline{noté} $\psi_k\circ G$, \underline{est complètement continu, et sa trace}⏎[cf. [4]] \underline{est donnée par la formule}"),
    "ψ_k∘G and the reference [cf. [4]] are not underlined. The print restarts the underline after 'continu,'; kept as one underline (global rule).")

add(421, "(4.5.9), exponent of the denominator",
    "tr(ψ_k∘G) = 1/(k-1)^{n+2} Σ_{X∈(μ_{k-1}(Ω))^{n+3}} G(X)",
    r"\frac1{(k-1)^{n+2}}",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed n+2. L(b) consists of series in the n+3 variables X_0,...,X_{n+2} (4.5.1-4.5.2) and the sum runs over (μ_{k-1})^{n+3}; Σ_X X^U is (k-1)^{n+3} when k-1 divides every U_i and 0 otherwise, and tr(ψ_k∘G) = Σ_W B_{(k-1)W}, so tr(ψ_k∘G) = (k-1)^{-(n+3)} Σ G(X). Only this exponent turns (4.4.6) (p. 419) into the printed (4.5.10), whose (q^ν-1)^{n+3}/q^ν is needed again for (4.5.12). Author's slip rather than a typing error.",
    r"\frac1{(k-1)^{n+3}}")

add(421, "(4.5.10), left-hand side",
    "(q-1)card V*(𝔽_{q^ν}) -- no handwritten ν in this factor",
    r"(q-1)\operatorname{card}",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed (q-1). (4.4.6), which (4.5.10) rewrites, has (q^ν-1)Card V*(𝔽_{q^ν}) on the left, and dividing (4.5.10) by q^ν-1 is what gives (4.5.12). The ν added by hand in the other factors q^ν-1 is missing here.",
    r"(q^\nu-1)\operatorname{card}")

add(421, "(4.5.10), operator inside tr",
    "tr(ψ_q ∏_{j=0}^{ord(q^ν)-1} H^{τ^j}(X^{p^j}) | L(1/(p-1)))",
    r"\left.\psi_q⏎\prod",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed ψ_q. The lemma is applied with k = q^ν (display above), so the operator is ψ_{q^ν}; (4.5.16) also needs ψ_{q^ν}, since α^{ord(q^ν)} = q^{-ν}ψ_{q^ν}∘∏H^{τ^j}(X^{p^j}) by (4.5.14). Same in (4.5.12).",
    r"\left.\psi_{q^\nu}⏎\prod")

add(421, "line before (4.5.11), 'Il est stable sous ψ∘G'",
    "Il est stable sous ψ ∘G -- no index k after ψ",
    r"sous $\psi_k\circ G$, et",
    "misprint_in_print", "medium",
    fix(r"sous $\psi_k\circ G$, et", r"sous $\psi\circ G$, et"),
    "The print has no k after ψ here: blank paper where the subscript would stand, while the k of ψ_k elsewhere on the page is a dark typed letter. The TeX silently supplies it.",
    r"sous $\psi_k\circ G$, et")

add(421, "(4.5.12), denominator of the second term",
    "(q^ν-1)^{n+2} over q -- no ν",
    r"\frac{(q^\nu-1)^{n+2}}{q}",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed q. From (4.5.10) (left side (q^ν-1)card V*) and (4.5.11) with G(0)=1: (q^ν-1)card V* = (q^ν-1)^{n+2} + (q^ν-1)^{n+3}q^{-ν}tr(…|L^0), so the denominator is q^ν, as in (4.5.10); (4.5.16) agrees.",
    r"\frac{(q^\nu-1)^{n+2}}{q^\nu}")

add(421, "(4.5.12), operator inside tr",
    "tr(ψ_q ∘ ∏_{j=0}^{ord(q^ν)-1} H^{τ^j}(X^{p^j}) | L^0(1/(p-1)))",
    r"\left.\psi_q\circ",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed ψ_q; ψ_{q^ν} is meant, as in (4.5.10) (k = q^ν).",
    r"\left.\psi_{q^\nu}\circ")

# ---------------- page 422 ----------------
add(422, "formula number between (4.5.13) and (4.5.15)",
    "(5.4.14)",
    r"\tag{5.4.14}",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed number; the formula is (4.5.14).",
    r"\tag{4.5.14}")

add(422, "(4.5.16), end",
    "tr((α)^{ord(q^ν)} | L^0(1/(p-1)) .  -- the parenthesis opened at tr( is not closed",
    r"L^0\!\left(\frac1{p-1}\right)\right..",
    "misprint_in_print", "high", None,
    "One closing parenthesis is missing in the print. The TeX keeps the printed reading (\\right.).",
    r"L^0\!\left(\frac1{p-1}\right)\right).")

# ---------------- page 423 ----------------
add(423, "'Evidemment chaque sous-espace ⊕ L^A(b)', index of the sum",
    "⊕_{A⊆B} L^A(b) -- ⊂ opening towards B, with a bar under it (compare A⊃B in (4.5.20) and A⊋B in the next line)",
    r"\bigoplus_{A\supset B}L^A(b)$ est stable",
    "misprint_in_print", "medium",
    fix(r"\bigoplus_{A\supset B}L^A(b)$ est stable", r"\bigoplus_{A\subseteq B}L^A(b)$ est stable"),
    "The subspace meant is the one of (4.5.20), the sum over A ⊇ B. The print reverses the inclusion; the TeX silently corrects it.",
    r"\bigoplus_{A\supseteq B}L^A(b)$ est stable")

add(423, "formula number of 'Récrivons encore (4.5.16)'",
    "(4.5.2.3)",
    r"\tag{4.5.2.3}",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed number; the formula is (4.5.23), cited so on p. 424.",
    r"\tag{4.5.23}")

add(423, "last sentence, 'y faisant la substitution en X_i = 0'",
    "le polynôme déduit de f(X) y faisant la substitution en X_i = 0 pour i ∉ A.",
    r"de $f(X)$ y faisant la⏎substitution en $X_i=0$",
    "misprint_in_print", "medium", None,
    "The 'en' is displaced: 'déduit de f(X) en y faisant la substitution X_i = 0', as after (4.5.22) ('se déduit de H(X) en y faisant la substitution X_i = 0'). The TeX keeps the printed order.",
    r"de $f(X)$ en y faisant la⏎substitution $X_i=0$")

# ---------------- page 424 ----------------
add(424, "(4.5.25), exponent of the first term",
    "(q^ν-1)^{car(A)-1}",
    r"\operatorname{car}(A)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed 'car'; card(A) is meant (next term: card(A)).",
    r"\operatorname{card}(A)")

add(424, "(4.5.25), trace term",
    "tr((α_B))^{ord(q^ν)})",
    r"\left((\alpha_B))^{\operatorname{ord}(q^\nu)}\right)",
    "misprint_in_print", "high", None,
    "One closing parenthesis too many after α_B (cf. tr((α_A)^{ord(q^ν)}) in (4.5.23) and (4.5.27)). The TeX keeps the printed reading.",
    r"\left((\alpha_B)^{\operatorname{ord}(q^\nu)}\right)")

add(424, "(4.5.27), index set of the second sum",
    "B⊆S / B≠∅ -- the ⊂ has a bar under it",
    r"B\subset S\\B\ne\varnothing",
    "symbol", "medium",
    fix(r"B\subset S\\B\ne\varnothing", r"B\subseteq S\\B\ne\varnothing"),
    "Same barred ⊂ as 'A ⊆ S' in the third line of the page (TeX \\subseteq); the index sets of (4.5.25) and (4.5.26) have a plain ⊂.")

# ---------------- page 425 ----------------
add(425, "formula number after '(4.5.27) se récrit'",
    "(4.5.23)",
    r"\tag{4.5.23}",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed number. (4.5.23) is the formula of p. 423 (cited so on p. 424); this one follows (4.5.32).",
    r"\tag{4.5.33}")

add(425, "Lemme 4.6.6, heading",
    "Lemme [ul] 4.6.6.",
    r"\underline{Lemme 4.6.6.}",
    "underline", "high",
    fix(r"\underline{Lemme 4.6.6.}", r"\underline{Lemme} 4.6.6."),
    "The number is not underlined.")

add(425, "Lemme 4.6.6, statement",
    "Δ_B(t) ∈ 1 + t𝒪[[t]], et si un entier [ul] j vérifie [ul]",
    r"\underline{$\Delta_B(t)\in1+t\mathcal O[[t]]$, et si un entier $j$ vérifie}",
    "underline", "high",
    fix(r"\underline{$\Delta_B(t)\in1+t\mathcal O[[t]]$, et si un entier $j$ vérifie}",
        r"$\Delta_B(t)\in1+t\mathcal O[[t]]$, \underline{et si un entier} $j$ \underline{vérifie}"),
    "The formula and j are not underlined.")

# ---------------- checks ----------------
ok = True
texts = {}
for d in F:
    p = d['page']
    if p not in texts:
        with open(os.path.join(PAGES, 'page_%d.tex' % p), encoding='utf-8', newline='') as fh:
            texts[p] = fh.read()
    t = texts[p]
    if d['tex'] not in t:
        print('TEX NOT FOUND', p, d['where']); ok = False
    if d['fix']:
        n = t.count(d['fix']['old'])
        if n != 1:
            print('OLD COUNT', n, p, d['where']); ok = False
        if '%%%%%%%%%%' in d['fix']['old']:
            print('MARKER IN OLD', p, d['where']); ok = False
        if d['fix']['old'] == d['fix']['new']:
            print('NO-OP FIX', p, d['where']); ok = False
for p, t in texts.items():
    if '\r' in t:
        print('CRLF in page', p)

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

from collections import Counter
c = Counter((d['page'], d['kind'] == 'misprint_in_print') for d in F)
for p in sorted(set(d['page'] for d in F)):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
print('ALL OK' if ok else 'PROBLEMS', len(F))
