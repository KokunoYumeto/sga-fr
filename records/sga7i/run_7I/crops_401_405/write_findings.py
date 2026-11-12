import io
import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(RUN, "b401_405")
OUT = os.path.join(RUN, "findings_401_405_recheck.json")

KEEP = "The TeX keeps the printed reading."

F = []


def add(page, where, scan, tex, conf, corrected, note):
    F.append({
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": "misprint_in_print",
        "confidence": conf,
        "fix": None,
        "corrected": corrected,
        "note": note,
    })


# ---------------- page 401 ----------------
add(401,
    "7.1.3, 'L'idée naturelle serait de partir d'un Module inversible ample M de G'",
    "partir d'un Module inversible ample M̲ de G, et de montrer que pour tout n, la restriction L̲_n de L̲ à G_n",
    "ample $\\underline{M}$ de $G$",
    "high",
    "ample $\\underline{L}$ de $G$",
    "The print names the ample Module on G 'M' and goes on with 'la restriction L_n de L à G_n'; L is introduced nowhere else, "
    "and M is the letter of the Modules on the B_n (M_n, M̂). The correct reading is L. " + KEEP)

add(401,
    "7.1.3, 'provient par image inverse d'un Module inversible M_n sur B_n. J'ignore si de tels M_n existent'",
    "d'un Module inversible M_n sur B_n. J'ignore si de tels M_n existent (neither M underlined; checked at 2x)",
    "d'un Module inversible $M_n$ sur $B_n$. J'ignore si de tels $M_n$ existent",
    "low",
    "d'un Module inversible $\\underline{M}_n$ sur $B_n$. J'ignore si de tels $\\underline{M}_n$ existent",
    "The invertible Modules on the B_n are M̲_n in the same paragraph ('une suite de Modules inversibles M̲_n sur les B_n', "
    "'des Modules inversibles M̲_n (symétriques) sur les B_n'); both underlines are missing on this one typed line. " + KEEP)

add(401,
    "7.1.3, 'en construisant une polarisation de B, i.e. un système projectif de polarisations ρ_n des B_n'",
    "une polarisation de B, i.e. un système (no hat on B; checked at 2x)",
    "une \\underline{polarisation} de $B$, i.e.",
    "low",
    "une \\underline{polarisation} de $\\hat{B}$, i.e.",
    "The polarisation is one of the formal abelian scheme B̂ = (B_n): the 'i.e.' spells it out, and the paragraph closes with "
    "'une polarisation de B̂'; B without hat is the algebraisation (p. 400), not yet available here. The hat is omitted. " + KEEP)

add(401,
    "7.1.3, 'et fourniront le M cherché'",
    "et fourniront le M̲ cherché. (no hat; checked at 2x)",
    "fourniront le $\\underline{M}$ cherché",
    "low",
    "fourniront le $\\underline{\\hat{M}}$ cherché",
    "The Module sought is the M̲̂ on B̂ of the first sentence ('un Module inversible M̲̂ sur B̂'), glued from the M̲_n. "
    "The hat is omitted. " + KEEP)

add(401,
    "7.1.3, 'correspondent biunivoquement aux biextensions de (A_n,A_n) par G_mS'",
    "aux biextensions de (A_n,A_n) par G_mS . Pour (no index n under S; checked at 2x)",
    "biextensions de $(A_n,A_n)$ par $\\mathbb{G}_{mS}$",
    "low",
    "biextensions de $(A_n,A_n)$ par $\\mathbb{G}_{m\\,S_n}$",
    "A_n lives over S_n, and the parallel clause just before reads 'biextension de (B_n,B_n) par G_{m S_n}'; VIII 3.5 compares "
    "biextensions by G_m over one and the same base. The index n is missing. " + KEEP)

# ---------------- page 402 ----------------
LAM = ("The typescript types a light Greek Λ without crossbar (the A of 'SGA' on the last line, and of 'A=A^o', has one) "
       "for the group scheme of the category C. The statement itself then calls it A ('A ⟼ Â le foncteur de C dans C'', "
       "'A_o = A×_S S_o', p. 403), as does 7.2.1.2 ('A ∈ ob C', p. 404). ")
add(402,
    "Lemme 7.2.1, 'C la catégorie des schémas en groupes Λ sur S'",
    "des schémas en groupes Λ sur S",
    "\\underline{la catégorie des schémas en groupes} $\\Lambda$",
    "medium",
    "\\underline{la catégorie des schémas en groupes} $A$",
    LAM + "The TeX keeps the printed Λ.")

add(402,
    "Lemme 7.2.1, 'tels que Λ/Λ^o soit un schéma en groupes étale fini sur S'",
    "Λ/Λ^o soit un schéma en groupes étale fini",
    "$\\Lambda/\\Lambda^o$",
    "medium",
    "$A/A^o$",
    "Same Λ for A as in 'schémas en groupes Λ'. The TeX keeps the printed Λ.")

add(402,
    "Lemme 7.2.1, 'et que Λ^o soit une extension d'un schéma abélien B'",
    "et que Λ^o soit une",
    "\\underline{et que} $\\Lambda^o$",
    "medium",
    "\\underline{et que} $A^o$",
    "Same Λ for A as in 'schémas en groupes Λ'. The TeX keeps the printed Λ.")

# ---------------- page 403 ----------------
add(403,
    "Lemme 7.2.1, definition of C': 'schémas formels de type fini (EGA I 10.3.3 )'",
    "(EGA I 10.3.3 ) (checked at 4x: 10.3.3)",
    "(EGA I 10.3.3 )",
    "medium",
    "(EGA I 10.13.3 )",
    "Wrong reference number. In EGA I (1960), 10.3.3 defines an Idéal de définition of an affine formal scheme; "
    "'préschéma formel de type fini' is Définition 10.13.3 (§10.13, Morphismes de type fini). The digit 1 is dropped. "
    "The TeX keeps 10.3.3.")

VRING = "The ring of the lemma is V: S is the spectrum of V, m is an ideal of V, and S_o = Spec(V/m) in the same sentence; A is the group scheme. "
add(403,
    "Lemme 7.2.1, definition of C': '... de type fini (EGA I 10.3.3 ) sur Specf(A)'",
    "sur Specf(A),",
    "\\underline{sur} $\\mathrm{Specf}(A)$",
    "high",
    "\\underline{sur} $\\mathrm{Specf}(V)$",
    VRING + KEEP)

add(403,
    "Lemme 7.2.1 b), 'lisse sur Ŝ = Specf(A)'",
    "lisse sur Ŝ = Specf(A) (i.e.",
    "$\\hat{S} = \\mathrm{Specf}(A)$",
    "high",
    "$\\hat{S} = \\mathrm{Specf}(V)$",
    VRING + KEEP)

add(403,
    "Lemme 7.2.1 b), 'sur les S_n = Spec(A/m^{n+1})'",
    "sur les S_n = Spec(A/m̲^{n+1}) soient",
    "$S_n = \\mathrm{Spec}(A/\\underline{m}^{n+1})$",
    "high",
    "$S_n = \\mathrm{Spec}(V/\\underline{m}^{n+1})$",
    VRING + "Compare S_n = Spec(V/m̲^{n+1}) in 7.1 (p. 400). " + KEEP)

add(403,
    "Lemme 7.2.1 b), '(i.e. tel que les schémas ordinaires A_n = A×_Ŝ S_n ...)'",
    "A_n = A×_Ŝ S_n (typed A, no handwritten script letter)",
    "$A_n = A \\times_{\\hat{S}} S_n$",
    "low",
    "$A_n = \\mathcal{A} \\times_{\\hat{S}} S_n$",
    "The object fibred with S_n over Ŝ is the formal group 𝒜 of b); b) has no group A. The typescript has a typed A "
    "where the handwritten script letter belongs. " + KEEP)

add(403,
    "Lemme 7.2.1 b), 'Soient 𝒜^o = (A_n^o)_{n≥0}, 𝒜/𝒜^o = (A_n/A_n^o) n ≥ 0'",
    "𝒜^o = (A^o_n)_{n ≥ 0}, 𝒜/𝒜^o = (A_n/A_n^o) n ≥ 0 ˙ Alors (the second n ≥ 0 on the line, not lowered)",
    "(A_n/A_n^{\\,o})$ $n \\geq 0$",
    "low",
    "(A_n/A_n^{\\,o})_{n \\geq 0}$",
    "The index range of the second family is typed on the line instead of as a subscript, unlike '(A^o_n)_{n≥0}' just before. "
    "The TeX reproduces the printed layout.")

# ---------------- page 404 ----------------
add(404,
    "7.2.1.2, 'dont nous désignerons par M le groupe dual'",
    "dont nous désignerons par M le groupe dual;sa restriction (M not underlined; checked at 4x)",
    "par $M$ le groupe dual",
    "low",
    "par $\\underline{M}$ le groupe dual",
    "The twisted constant dual group is M̲ everywhere else on the page: M̲_n in (*), 'isomorphe à M̲_n', 'le fait que M̲ est un "
    "schéma somme', (**) M̲ ⟶ B'. The underline is missing. " + KEEP)


def main():
    texts = {}
    for p in sorted({f["page"] for f in F}):
        with io.open(os.path.join(PAGES, "page_%d.tex" % p), encoding="utf-8", newline="") as fh:
            texts[p] = fh.read()
    ok = True
    for f in F:
        t = texts[f["page"]]
        n = t.count(f["tex"])
        if n != 1:
            ok = False
            print("TEX COUNT %d on page %d: %r" % (n, f["page"], f["tex"]))
        if f["fix"] is not None:
            m = t.count(f["fix"]["old"])
            if m != 1:
                ok = False
                print("OLD COUNT %d on page %d: %r" % (m, f["page"], f["fix"]["old"]))
    if not ok:
        sys.exit(1)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    counts = {}
    for f in F:
        c = counts.setdefault(f["page"], [0, 0])
        c[1 if f["kind"] == "misprint_in_print" else 0] += 1
    print("written", OUT, len(F))
    print(", ".join("p%d %d/%d" % (p, counts.get(p, [0, 0])[0], counts.get(p, [0, 0])[1]) for p in range(401, 406)))


main()
