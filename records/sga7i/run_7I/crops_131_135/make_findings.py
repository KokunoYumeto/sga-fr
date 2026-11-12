import json

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_131_135.json"

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 131 ----------------
add(131, "Definition 6.6, first line: 'be a k-scheme of finite type.'",
    "'be a' underlined; 'k-' not underlined; the underline resumes at 'scheme of finite type'",
    r"\underline{be a k-scheme of finite type.}",
    "underline", "high",
    {"old": r"\underline{be a k-scheme of finite type.}",
     "new": r"\underline{be a} k-\underline{scheme of finite type.}"},
    "The typescript leaves the letter k and its hyphen outside the underline (same in Corollary 6.8 on p. 132; "
    "fixed the same way on pp. 92 and 104). The full stop is left as it is (global rule).")

add(131, "Definition 6.6 (i), start of the second line: 'then a is a non-degenerate quadratic singularity rational over k'",
    "a", r"$a$",
    "misprint_in_print", "high", None,
    "The print has the letter a where the point z of the definition is meant ('A closed point z in X is called ... "
    "if the following holds: (i) ... then z is a non-degenerate quadratic singularity'). The TeX keeps the printed reading.",
    corrected=r"$z$")

add(131, "Proof of Lemma 6.7, last display: 'dF = 1 -> sum_{0<=i<=2n} (df/dX_i) dX_i + dX_0 ,'",
    "+ dX_0", r"+ dX_0",
    "misprint_in_print", "medium", None,
    "With F = f + t_1 + tX_0 the coefficient of dX_0 in dF is df/dX_0 + t, so the last term is t dX_0; the next page "
    "uses it (I_A(A|R) = (t, x_1, ..., x_{2n})). The print omits the t; the TeX keeps the printed reading.",
    corrected=r"+ tdX_0")

# ---------------- page 132 ----------------
add(132, "Corollary 6.8, first line: 'be a k-scheme of finite type with isolated non-smooth points only such that'",
    "'be a' underlined; 'k-' not underlined; the underline resumes at 'scheme of finite type with isolated non-smooth'",
    r"\underline{be a k-scheme of finite type with isolated non-smooth points only such that}",
    "underline", "high",
    {"old": r"\underline{be a k-scheme of finite type with isolated non-smooth points only such that}",
     "new": r"\underline{be a} k-\underline{scheme of finite type with isolated non-smooth points only such that}"},
    "Same as Definition 6.6 on p. 131.")

add(132, "Corollary 6.8 (2): 'I_R(X|R) = _{1<=i<=m} I_R(X_(z_i)|R)'",
    "blank space between '=' and the subscript '1<=i<=m': no operator is printed (no trace of it under contrast enhancement)",
    r"\mathop{\hphantom{\bigcap}}_{1 \leq i \leq m}",
    "misprint_in_print", "medium", None,
    "The handwritten operator was never put in; the TeX reproduces the blank with a phantom. Theorem 6.4 (3) states the "
    "same thing with a product sign (TeX there: \\prod_{1\\leq\\ i\\leq\\ m}), and the product of the principal ideals "
    "(t_i^2) is what makes I_R(X|R) principal.",
    corrected=r"\prod_{1 \leq i \leq m}")

# ---------------- page 133 ----------------
add(133, "title of Exposé VII: 'BIEXTENSIONS DE FAISCEAUX DE GROUPES'",
    "the title is underlined twice", r"\underline{BIEXTENSIONS DE FAISCEAUX DE GROUPES}",
    "underline", "high",
    {"old": r"\underline{BIEXTENSIONS DE FAISCEAUX DE GROUPES}",
     "new": r"\underline{\underline{BIEXTENSIONS DE FAISCEAUX DE GROUPES}}"},
    "'E X P O S E VII' and 'par A. Grothendieck' have a single underline. The titles of Exposés I, II, VI and IX are "
    "already \\underline{\\underline{...}} in the diplomatic TeX.")

add(133, "Introduction, line 6: 'des (x)^L et RHom (3.6.4 et 3.6.5)'",
    "RHom with only 'Hom' underlined (the underline starts under H); upright type",
    r"$\underline{RHom}$",
    "underline", "high",
    {"old": r"$\underline{RHom}$",
     "new": r"$\mathrm{R}\underline{\mathrm{Hom}}$"},
    "The R is not underlined. The same edit sets the operator name upright, as \\mathrm{Hom} elsewhere in this exposé "
    "(the TeX's math italic RHom is the operator-name issue of item 19).")

# ---------------- page 135 ----------------
P_NOTE = ("The print has a capital P in the subscript (cap height, no descender), as in every G_P of 1.1.2-1.1.2.1, "
          "against the small p with a descender in E_p; the later pages of the TeX already write G_P.")

add(135, "1.1.2, 'le groupe induit G_P = G x P par G'",
    "G_P (capital P)", r"$G_p = GxP$",
    "symbol", "high",
    {"old": r"$G_p = G", "new": r"$G_P = G"},
    P_NOTE)

add(135, "1.1.2, 'le groupe induit G_P = G x P par G'",
    "G×P: the product sign is a serifless cross, not the letter x (the typeface's x and X have serifs, cf. 'x' in "
    "'x ∈ E(S)' and 'IX' on p. 134)",
    r"GxP",
    "symbol", "high",
    {"old": r"GxP", "new": r"G\times P"},
    "The TeX of this exposé writes the product as \\times elsewhere (P\\times P, G_{P\\times Q}). Independent of the "
    "G_P edit just before it.")

add(135, "1.1.2, 'par G dans T_{/P} opère sur E'",
    "T underlined with subscript /P (capital P)", r"\underline{T}_{/p}",
    "symbol", "high",
    {"old": r"\underline{T}_{/p}", "new": r"\underline{T}_{/P}"},
    "Capital P, as in E_{/P} two lines above and in \\underline{T}_{/P} on the following pages of the TeX.")

add(135, "1.1.2, 'sur P, de groupe G_P , et que'",
    "G_P", r"de groupe $G_p$",
    "symbol", "high",
    {"old": r"de groupe $G_p$", "new": r"de groupe $G_P$"},
    P_NOTE)

add(135, "1.1.2, 'un bitorseur sous (G_P,G_P). Rappelons [2]'",
    "(G_P,G_P)", r"$(G_p,G_p)$. Rappelons",
    "symbol", "high",
    {"old": r"$(G_p,G_p)$. Rappelons", "new": r"$(G_P,G_P)$. Rappelons"},
    P_NOTE)

add(135, "1.1.2, 'par l'action droite de G_P , et que l'action gauche'",
    "G_P", r"droite de $G_p$ , et que",
    "symbol", "high",
    {"old": r"droite de $G_p$ , et que", "new": r"droite de $G_P$ , et que"},
    P_NOTE)

add(135, "1.1.2, 'induit un isomorphisme de G_P avec le Groupe des automorphismes de E_d'",
    "G_P", r"isomorphisme de $G_p$ avec",
    "symbol", "high",
    {"old": r"isomorphisme de $G_p$ avec", "new": r"isomorphisme de $G_P$ avec"},
    P_NOTE)

add(135, "1.1.2, 'qui commutent à l'action droite de G_P sur E)'",
    "G_P", r"droite de $G_p$ sur",
    "symbol", "high",
    {"old": r"droite de $G_p$ sur", "new": r"droite de $G_P$ sur"},
    P_NOTE)

add(135, "1.1.2, 'savoir que l'action gauche de G_P sur E fait de E'",
    "G_P", r"gauche de $G_p$ sur",
    "symbol", "high",
    {"old": r"gauche de $G_p$ sur", "new": r"gauche de $G_P$ sur"},
    P_NOTE)

add(135, "1.1.2, 'du Groupe opposé G_P^o de G_P avec'",
    "G_P^o ... G_P", r"$G_p^{\;o}$ de $G_p$",
    "symbol", "high",
    {"old": r"$G_p^{\;o}$ de $G_p$", "new": r"$G_P^{\;o}$ de $G_P$"},
    P_NOTE)

add(135, "1.1.2.1, 'la donnée d'un bitorseur E sous (G_P,G_P) équivaut manifestement'",
    "(G_P,G_P)", r"sous  $(G_p,G_p)$  équivaut",
    "symbol", "high",
    {"old": "sous  $(G_p,G_p)$  équivaut", "new": "sous  $(G_P,G_P)$  équivaut"},
    P_NOTE)

add(135, "1.1.2.1, 'la donnée d'un bitorseur E sous (G_P,G_P) équivaut à la donnée, pour tout \"point\"'",
    "(G_P,G_P)", r"$(G_p,G_p)$ équivaut à",
    "symbol", "high",
    {"old": "$(G_p,G_p)$ équivaut à", "new": "$(G_P,G_P)$ équivaut à"},
    P_NOTE)

add(135, "1.1.2, 'comme un objet du topos induit E_{/P} , alors'",
    "E_{/P}", r"$E_{/P}$",
    "misprint_in_print", "low", None,
    "E is to be regarded as an object of the induced topos T_{/P} (named two lines below: 'G_P = G x P par G dans "
    "T_{/P}'); E_{/P} is not a topos. The TeX keeps the printed reading.",
    corrected=r"$\underline{T}_{/P}$")

add(135, "1.1.2.1, 'Une interprétation analogue peut-être donnée dans le cas général'",
    "peut-être", "peut-être",
    "misprint_in_print", "high", None,
    "The verb 'peut être' (can be) is meant, not the adverb 'peut-être'. The TeX keeps the printed reading.",
    corrected="peut être")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
