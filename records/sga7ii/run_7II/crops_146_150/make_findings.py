import json, os

FOLDER = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b146_150"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_146_150.json"

F = []

def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 146 ----------------
add(146,
    "3.1.12 (b), first lines of the page: 'φ classe d'homotopie de chemins de Id à ∂T , à isotopie près'",
    "chemins de Id à ∂T : no index o under the T (checked at 2.5x)",
    r"à $\partial T$ , à isotopie",
    "misprint_in_print", "medium", None,
    "Missing index: the pairs (T_o, φ) of (b) do not involve T; φ is a path from Id to the boundary of T_o, "
    "as in 3.1.11 (b) ('qui relie l'identité à ∂T_o', p. 145) and 3.2.5 ('le chemin suivant de Id à ∂T_o', p. 148); "
    "for T itself ∂T = Id. The TeX keeps the printed reading.",
    r"à $\partial T_o$ , à isotopie")

add(146,
    "3.1.13, second line: 'une trivialisation du fibré ∂B_{t,d} , variant continument avec θ'",
    "continument: no circumflex on the u (checked at 2.5x)",
    "variant continument avec",
    "misprint_in_print", "low", None,
    "Accent slip: the spelling of the period is 'continûment'. The TeX keeps the printed reading.",
    "variant continûment avec")

# ---------------- page 147 ----------------
add(147,
    "(3.2.2.2), second line: 'x.y = 0 (i.e. x ⊥ y dans ℝ^n )'",
    "dans ℝ^n: exponent n (checked at 2x)",
    r"\mathbb{R}^n\ )",
    "misprint_in_print", "medium", None,
    "Wrong exponent: z = (z_i) is a point of ℂ^{n+1} (3.2.1: f = Σ_1^{n+1} z_i^2 on ℂ^{n+1}), so x and y lie in "
    "ℝ^{n+1}, and X = x/|x| lies on S^n ⊂ ℝ^{n+1} (end of 3.2.2). The TeX keeps the printed reading.",
    r"\mathbb{R}^{n+1}\ )")

add(147,
    "3.2.3, second sentence: 'Le fibré sur ℝ image réciproque de B est isomorphe à R × V'",
    "R × V: a plain typed R, while the ℝ of 'Le fibré sur ℝ' in the same sentence and of 'identifie ℝ' "
    "in the line above are double-struck (checked at 1.2x)",
    r"$R \times V$",
    "misprint_in_print", "medium", None,
    "Font slip: the base is the real line ℝ of the same sentence (the universal cover of S_a). "
    "The TeX keeps the printed reading.",
    r"$\mathbb{R} \times V$")

# ---------------- page 148 ----------------
add(148,
    "second paragraph, first words: 'Au dessus du rayon ℝ^+ ∩ D_a'",
    "Au dessus: no hyphen (checked at 1.3x)",
    "Au dessus du rayon",
    "misprint_in_print", "low", None,
    "Hyphen slip: the same page prints 'au-dessus de chacun des rayons' and 'Au-dessus de (e^{2πiθ}ℝ^+) ∩ D_a'. "
    "The TeX keeps the printed reading.",
    "Au-dessus du rayon")

add(148,
    "3.2.5: 'chaque vecteur tangent unitaire le long de la geodésique qu'il engendre d'une longueur + πθ'",
    "geodésique: no accent on the first e (checked at 2.5x)",
    "la geodésique qu'il engendre d'une longueur",
    "misprint_in_print", "medium", None,
    "Accent slip; the same slip recurs in the next paragraph (reported separately). The TeX keeps the printed reading.",
    "la géodésique qu'il engendre d'une longueur")

add(148,
    "unnumbered paragraph after 3.2.5: 'Par 3.1.13, on obtient la description suivante de T'",
    "Par 3.1.13 (checked at 2x)",
    "Par 3.1.13, on obtient",
    "misprint_in_print", "low", None,
    "Probably a wrong reference: the description of T from the pair (T_o, φ) by a collar (T = T_o outside the collar, "
    "T(x) = T_o(φ(β(x))^{-1}(x)) inside) is the 'Concrètement' part of 3.1.12, (α) and (β) on p. 146, which this "
    "paragraph applies with |u| as collar coordinate; 3.1.13 is the variant of 3.1.11 (b) for computing the path φ, "
    "already applied in 3.2.4. Also, the print numbers no paragraph 3.2.6: this unnumbered paragraph follows 3.2.5 and "
    "the next is 3.2.7 (cited as 3.2.7 on p. 149); no edit proposed for that gap. The TeX keeps the printed reading.",
    "Par 3.1.12, on obtient")

add(148,
    "same paragraph: 'T consiste à déplacer u , le long de la geodésique qu'il engendre, d'une longueur'",
    "geodésique: no accent on the first e (checked at 2.5x)",
    "la geodésique qu'il engendre, d'une longueur",
    "misprint_in_print", "medium", None,
    "Accent slip, as in 3.2.5. The TeX keeps the printed reading.",
    "la géodésique qu'il engendre, d'une longueur")

add(148,
    "same paragraph: 'd'une longueur - π(1-φ(|u|) (près de |u| = 1 , c'est l'identité'",
    "- π(1-φ(|u|) : two opening parentheses, one closing (checked at 2.5x)",
    r"$- \pi(1-\varphi(|u|)$",
    "misprint_in_print", "high", None,
    "Missing closing parenthesis. The TeX keeps the printed reading.",
    r"$- \pi(1-\varphi(|u|))$")

add(148,
    "3.2.7, first line: 'Soient W une variété différentiable de dimension x'",
    "dimension x: a typed x (checked at 2.5x)",
    r"de dimension $x$",
    "misprint_in_print", "low", None,
    "Wrong letter: on p. 149 the zero section W ⊂ T(W) defines w ∈ H_d(T(W)) (resp. H^d_c(T(W))), so dim W = d; "
    "x is the letter of the coordinates x_i. The local coordinates on p. 149 are written (x_1,...,x_n), so n is the "
    "other possible reading. The TeX keeps the printed reading.",
    r"de dimension $d$")

# ---------------- page 150 ----------------
add(150,
    "3.2.10, first paragraph: 'le fibré normal à cette fibré est le fibré constant'",
    "cette fibré: accented é (checked at 2.5x)",
    "normal à cette fibré",
    "misprint_in_print", "high", None,
    "Wrong word: the noun is 'fibre' (feminine 'cette'), the fibre of the fibration of V^o over S^n named just before. "
    "The TeX keeps the printed reading.",
    "normal à cette fibre")

add(150,
    "(α): 'Γ_c(Ω^*_V) représente RΓ(V, ℝ) , d'où un isomorphisme H^i(Γ_c(V, Ω^*_V)) = H^i_c(V, ℝ)'",
    "RΓ(V, ℝ): no index c under the Γ, while both Γ_c of the same sentence have one (checked at 1.5x)",
    r"$R\Gamma(V, \mathbb{R})$",
    "misprint_in_print", "medium", None,
    "Missing index: Γ_c of a soft resolution computes cohomology with compact support, as the same sentence concludes "
    "('= H^i_c(V, ℝ)'). The TeX keeps the printed reading.",
    r"$R\Gamma_c(V, \mathbb{R})$")

add(150,
    "paragraph before the last displays: 'T(δ') coincide avec δ' dans un voisinage de ∂V'",
    "coincide: a plain dotted i, no diaeresis (checked at 2.5x)",
    "coincide avec",
    "misprint_in_print", "medium", None,
    "Accent slip, as 'coincide' on p. 131. The TeX keeps the printed reading.",
    "coïncide avec")

# ---------------- checks ----------------
ok = True
for d in F:
    p = os.path.join(FOLDER, "page_%03d.tex" % d["page"])
    with open(p, encoding="utf-8") as fh:
        txt = fh.read()
    n = txt.count(d["tex"])
    if n != 1:
        ok = False
        print("TEX COUNT", n, d["page"], repr(d["tex"]))
    if d["fix"] is not None:
        m = txt.count(d["fix"]["old"])
        if m != 1:
            ok = False
            print("OLD COUNT", m, d["page"], repr(d["fix"]["old"]))
print("all checks ok" if ok else "CHECK FAILURES")

with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("wrote", len(F), "findings to", OUT)
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for pg in (146, 147, 148, 149, 150):
    print(pg, "normal", c[(pg, False)], "misprint", c[(pg, True)])
