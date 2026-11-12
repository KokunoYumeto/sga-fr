import json
import pathlib

OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_236_240.json")
SRC = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b236_240")

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 236 ----------------
add(236, "display after 'pas fermé, mais qu'on a'",
    "4.1.4.      l'adhérence de  F_2 ⊂ F_1 ∪ F_2  ,   (number 4.1.4. at the left margin)",
    r"l'adhérence de $F_2 \subset F_1 \cup F_2$ ,",
    "number", "high",
    {"old": r"l'adhérence de $F_2", "new": r"4.1.4.\quad l'adhérence de $F_2"},
    "The number of the display is left out; the next sentence cites it ('L'inclusion 4.1.4.').")

add(236, "paragraph before Proposition 4.2: 'D'autre part, 3.8.1 et 4.1.2 nous assurent que'",
    "3.8.1 (checked at 1.4x)",
    r"D'autre part, 3.8.1 et 4.1.2",
    "misprint_in_print", "medium", None,
    "Wrong reference: Exposé XVII has no 3.8. (3.7.1) gives, for every d ≥ 2, a hypersurface of degree d with an "
    "ordinary quadratic singularity at a given point, i.e. the open set 4.1 is non-empty for the d-th multiple "
    "embedding, which is the hypothesis of Lemme 4.1.2. The TeX keeps the printed reading.",
    corrected=r"D'autre part, 3.7.1 et 4.1.2")

add(236, "same sentence: 'on aura codim(F_2) ≥ 2 . On conclut que 2.5.1 sera prouvé'",
    "codim_{P̌^r}(F_2) ≥ 2 (subscript 2, checked at 1.4x)",
    r"on aura $\mathrm{codim}_{\check{\mathbb{P}}^r}(F_2) \geq 2$",
    "misprint_in_print", "high", None,
    "Of the two conditions just stated, this sentence settles the one for F_1: Lemme 4.1.2 concerns F_1, and the "
    "next sentence leaves F_2 to Proposition 4.2. The TeX keeps the printed reading.",
    corrected=r"on aura $\mathrm{codim}_{\check{\mathbb{P}}^r}(F_1) \geq 2$")

add(236, "Proposition 4.2: 'la partie F_2 de P̌^{(n+d over d)-1} = P̌^N'",
    "exponent (n+d over d)-1 (checked at 1.4x)",
    r"$\check{\mathbb{P}}^{{n+d \choose d}-1} = \check{\mathbb{P}}^N$",
    "misprint_in_print", "high", None,
    "The hypersurfaces of degree d in P^r form a projective space of dimension binom(r+d,d)-1 (Proposition 4.3 "
    "writes r+d); n is dim X. The TeX keeps the printed reading.",
    corrected=r"$\check{\mathbb{P}}^{{r+d \choose d}-1} = \check{\mathbb{P}}^N$")

add(236, "4.2.1, first word: 'Commencons par le cas spécial'",
    "Commencons (no cedilla, checked at 2.5x)",
    r"4.2.1. Commencons par",
    "misprint_in_print", "high", None,
    "Missing cedilla; the typewriter has ç (remplaçant on this page, Commençons in 5.1 on p. 240). The TeX keeps "
    "the printed reading.",
    corrected=r"4.2.1. Commençons par")

add(236, "4.2.1: 'Choisissons des coordonnés homogènes X_o,...,X_r'",
    "coordonnés homogènes",
    r"Choisissons des coordonnés homogènes",
    "misprint_in_print", "high", None,
    "Agreement slip, as on earlier pages of the exposé. The TeX keeps the printed reading.",
    corrected=r"Choisissons des coordonnées homogènes")

add(236, "last line: 'de telle facon que X soit défini par'",
    "facon (no cedilla, checked at 1.6x)",
    r"de telle facon que",
    "misprint_in_print", "high", None,
    "Missing cedilla (the print has 'façon' twice on p. 239). The TeX keeps the printed reading.",
    corrected=r"de telle façon que")

# ---------------- page 237 ----------------
add(237, "first line: 'et des coordonnés homogènes (λ, μ) dans P^1'",
    "coordonnés homogènes",
    r"et des coordonnés homogènes $(\lambda, \mu)$",
    "misprint_in_print", "high", None,
    "Agreement slip, as on p. 236. The TeX keeps the printed reading.",
    corrected=r"et des coordonnées homogènes $(\lambda, \mu)$")

add(237, "(4.2.3), the pencil for n = 2k+1",
    "H_{(λ,μ)} = (λX_1+μX_o)X_o + Σ_{i=1}^{k} (λX_{2i}+μX_i)X_{2i+1}  (μX_i with a dotted i, checked at 2x)",
    r"\sum_{i=1}^{k}\ (\lambda X_{2i} + \mu X_i) X_{2i+1}",
    "misprint_in_print", "medium", None,
    "As printed the pencil fails for n = 2k+1 ≥ 7: for k = 3, H_{(0,1)} = X_o^2 + X_1X_3 + X_2X_5 + X_3X_7 is "
    "singular along the plane X_o = X_2 = X_3 = X_5 = 0, X_1 + X_7 = 0, so X·H_{(0,1)} does not have a single "
    "ordinary quadratic point (in any characteristic) and the pencil meets F; the formula is right for k ≤ 2 "
    "(n = 1, 3, 5). No reading of the print gives the intended index, so the 'corrected' formula is one repair, "
    "not a recovered reading: it changes only the μ-index for i ≥ 3 and agrees with the print for k ≤ 2; checked "
    "for all k ≥ 0 (H_{(0,1)} = X_o^2 + X_1X_3 + Σ_{i≥2} X_{2i-2}X_{2i+1} is singular only at the coordinate point "
    "of X_{2k} (of X_1 when k = 0), and H_{(λ,μ)} is smooth for λ ≠ 0). The TeX keeps the printed reading.",
    corrected=r"\sum_{i=1}^{k}\ (\lambda X_{2i} + \mu X_{\max(1,\,2i-2)}) X_{2i+1}")

add(237, "display after 'de sorte qu'il suffira de démontrer'",
    "(4.2.5)   dim Btg^d(X) ≤ N-2  si  d ≥ 3 , ou si  d = 2  et  X  n'est pas linéaire.",
    r"$\dim \mathrm{Btg}^d(X) \leq N-2$ si $d \geq 3$ , ou si ... (no number)",
    "number", "high",
    {"old": r"$\dim \mathrm{Btg}^d(X) \leq N-2$", "new": r"(4.2.5)\quad $\dim \mathrm{Btg}^d(X) \leq N-2$"},
    "The formula number is left out; p. 238 cites (4.2.5).")

add(237, "display defining Lin(X×X)",
    "(4.2.6)   Lin(X×X)={(x_1,x_2)∈X×X | x_1≠x_2 , et la droite ...",
    r"$\mathrm{Lin}(X \times X) = \{(x_1,x_2) \in X \times X \mid ... (no number)",
    "number", "high",
    {"old": r"$\mathrm{Lin}(X \times X) = \{", "new": r"(4.2.6)\quad $\mathrm{Lin}(X \times X) = \{"},
    "The formula number is left out.")

add(237, "(4.2.6), second line",
    "{(x_1,x_2)∈X×X|x_1≠ x_2 et x_2 ∈ X∩Tg (x_1)}  .  with no '=' before it (no ink left of the brace, even at a "
    "light threshold)",
    r"\\ $\{(x_1,x_2) \in X \times X \mid x_1 \neq x_2$ et",
    "misprint_in_print", "medium", None,
    "The second description of Lin(X×X) needs '='; the line starts to the right of the first line's brace, as if "
    "space had been left for a hand-written '=' that was never added. The TeX keeps the printed reading.",
    corrected=r"\\ $= \{(x_1,x_2) \in X \times X \mid x_1 \neq x_2$ et")

# ---------------- page 238 ----------------
add(238, "after (4.2.8): 'considérés comme des sous-variétés de P̌^N, sont'",
    "considérés (checked at 2x)",
    r"considérés comme des sous-variétés",
    "misprint_in_print", "high", None,
    "Agreement slip: the participle refers to 'les fibres du morphisme'. The TeX keeps the printed reading.",
    corrected=r"considérées comme des sous-variétés")

add(238, "Proposition 4.3: 'Dans l'espace P̌^N = P̌^{(r+d over d)-d}'",
    "exponent (r+d over d)-d (checked at 2x)",
    r"$\check{\mathbb{P}}^N = \check{\mathbb{P}}^{\binom{r+d}{d}-d}$",
    "misprint_in_print", "high", None,
    "The space of hypersurfaces of degree d in P^r has dimension binom(r+d,d)-1, the N of Proposition 4.2 "
    "(exponent ...-1 there). The TeX keeps the printed reading.",
    corrected=r"$\check{\mathbb{P}}^N = \check{\mathbb{P}}^{\binom{r+d}{d}-1}$")

# ---------------- page 239 ----------------
add(239, "Démonstration of 4.3: 'Or, en termes de coordonnés homogènes choisies de telle façon'",
    "coordonnés homogènes choisies",
    r"en termes de coordonnés homogènes choisies",
    "misprint_in_print", "high", None,
    "Agreement slip (note 'choisies'). The TeX keeps the printed reading.",
    corrected=r"en termes de coordonnées homogènes choisies")

add(239, "same sentence: 'si et seulement si les coéfficients des monômes X_o^{d-1}X_i'",
    "coéfficients (acute on the first e; the second occurrence in the sentence is 'coefficients'; checked at 1.4x)",
    r"les coéfficients des monômes",
    "misprint_in_print", "high", None,
    "Spurious accent. The TeX keeps the printed reading.",
    corrected=r"les coefficients des monômes")

add(239, "'alors les conditions de tangentialité sont indépendentes. On se ramène au cas'",
    "indépendentes (checked at 2x; 'indépendantes' earlier on the page and on p. 240)",
    r"tangentialité sont indépendantes.",
    "misprint_in_print", "high",
    {"old": r"tangentialité sont indépendantes", "new": r"tangentialité sont indépendentes"},
    "The TeX silently corrects the printed spelling; the fix restores it.",
    corrected=r"tangentialité sont indépendantes")

add(239, "'On choisit des coordonnés homogènes X_o,...,X_r de telle façon'",
    "coordonnés homogènes",
    r"On choisit des coordonnés homogènes",
    "misprint_in_print", "high", None,
    "Agreement slip. The TeX keeps the printed reading.",
    corrected=r"On choisit des coordonnées homogènes")

add(239, "same sentence: 'x_1 = (1,0,...,0) , x_1 = (0,1,0...0) et L_2 soit l'hyperplan'",
    "second point written x_1 (subscript 1, checked at 2x)",
    r"$x_1 = (0,1,0...0)$",
    "misprint_in_print", "high", None,
    "The second point is x_2 (the line (x_1,x_2); p. 240 uses x_2 = (0,1,0,...0)). The TeX keeps the printed "
    "reading.",
    corrected=r"$x_2 = (0,1,0...0)$")

# ---------------- page 240 ----------------
add(240, "first line: 'tangente à X_o = 0 en (0,1,...,0) si et seulement si A_{ij} = 0 pour j = 1,...,r'",
    "A_{ij} (first subscript letter dotted, i.e. i, not the undotted typewriter 1; checked at 1.4x)",
    r"$A_{ij} = 0$ pour $j = 1,\ldots,r$",
    "misprint_in_print", "high", None,
    "The quadric passes through x_2 = (0,1,0,...,0) and is tangent there to X_o = 0 iff A_{1j} = 0 for "
    "j = 1,...,r; with the r+1 conditions A_{oj} = 0 this gives the 2r+1 conditions counted. The TeX keeps the "
    "printed reading.",
    corrected=r"$A_{1j} = 0$ pour $j = 1,\ldots,r$")

add(240, "'En termes de coordonnés homogènes dans lesquelles x_1 = (1,0,..,0)'",
    "coordonnés homogènes",
    r"En termes de coordonnés homogènes dans lesquelles",
    "misprint_in_print", "high", None,
    "Agreement slip (note 'lesquelles'). The TeX keeps the printed reading.",
    corrected=r"En termes de coordonnées homogènes dans lesquelles")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- checks: every fix's old occurs exactly once in its page_NNN.tex; tex excerpts present ----
ok = True
for d in F:
    t = (SRC / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    if d["fix"]:
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", d["page"], n, d["fix"]["old"])
        if "%%%%" in d["fix"]["old"] or "%%%%" in d["fix"]["new"]:
            ok = False
            print("MARKER", d["page"])
    tex = d["tex"].split(" ... ")[0].split(" (no ")[0]
    if tex not in t:
        print("tex excerpt not verbatim (informational):", d["page"], tex[:60])
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("all fix olds unique:", ok)
print("counts (normal/misprint):", counts, "total", len(F))
