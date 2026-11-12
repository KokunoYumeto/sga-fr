import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
FOLDER = os.path.join(RUN, "b066_070")
OUT = os.path.join(RUN, "findings_066_070.json")

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 66 ----------------
add(page=66,
    where="first paragraph, 'L'algèbre End(∧ W_1) est alors Z/2-gradué'",
    scan="L'algèbre End(∧ W_1) est alors Z/2-gradué : (checked at 2x)",
    tex=r"est alors $\mathbb{Z}/2$-gradué :",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"est alors $\mathbb{Z}/2$-graduée :",
    note="Agreement error: the subject is 'L'algèbre'. The same slip recurs twice on p. 68. The TeX keeps the printed reading; the corrected layer too.")

add(page=66,
    where="second paragraph, 'l'existence d'un unique isomorphisme d'algèbre Z/2-graduées s'",
    scan="isomorphisme d'algèbre Z/2-graduées s entre",
    tex=r"isomorphisme d'algèbre $\mathbb{Z}/2$-graduées $s$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"isomorphisme d'algèbres $\mathbb{Z}/2$-graduées $s$",
    note="Agreement error: singular noun with a feminine plural adjective (an isomorphism of Z/2-graded algebras). The TeX keeps the printed reading; the corrected layer too.")

add(page=66,
    where="display after 'tel que', left formula",
    scan="s(ρ((e,0)) = e ∧ : three parentheses opened, two closed (checked at 3x)",
    tex=r"s(\rho((e,0))) = e \wedge",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"s(\rho((e,0)))", "new": r"s(\rho((e,0))"},
    corrected=r"s(\rho((e,0)))",
    note="The parenthesis opened after s is never closed. The TeX silently adds it; the fix restores the printed reading. The corrected layer has the closing parenthesis.")

add(page=66,
    where="display after 'tel que', right formula",
    scan="s(ρ((0,f)) = f⌞ : three parentheses opened, two closed (checked at 3x)",
    tex=r"s(\rho((0,f))) = f \llcorner",
    kind="misprint_in_print", confidence="high",
    fix={"old": r"s(\rho((0,f)))", "new": r"s(\rho((0,f))"},
    corrected=r"s(\rho((0,f)))",
    note="As in the left formula. The TeX silently adds the parenthesis; the fix restores the printed reading. The corrected layer has it.")

add(page=66,
    where="paragraph 'Désignons provisoirement ...', the idempotents defining Z(Q) = A ⊕ A",
    scan="par les idempotents e(W_1,W_2) et 1 - e (W_2,W_1). (checked at 1x)",
    tex=r"et $1 - e(W_2,W_1)$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"et $1 - e(W_1,W_2)$",
    note="The decomposition A ⊕ A is given by an idempotent and its complement, e(W_1,W_2) and 1 - e(W_1,W_2). Exchanging W_1 and W_2 changes the idempotent when m is odd (Proposition 1.12 with W_1 ∩ W_2 = 0). Check m = 1 with the formulas of p. 70: e(W_1,W_2) = fe and e(W_2,W_1) = ef = 1 - fe, so the printed pair is fe, fe. The printed reading holds only for m even. Possibly the author's slip rather than a typing error. The TeX keeps the printed reading; the corrected layer too.")

# ---------------- page 67 ----------------
add(page=67,
    where="'Puisqu'il existe toujours de telles formes B, W admet des supplémentaires totalement singulier.'",
    scan="W admet des supplémentaires / totalement singulier. L'un d'eux (checked at 1x)",
    tex=r"des supplémentaires totalement singulier. L'un",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"des supplémentaires totalement singuliers. L'un",
    note="Agreement error. The TeX keeps the printed reading; the corrected layer too.")

add(page=67,
    where="'l'ensemble des supplémentaire totalement singulier W'_o de W'",
    scan="l'ensemble des / supplémentaire totalement singulier W'_o de W (checked at 1x)",
    tex=r"l'ensemble des supplémentaire totalement singulier $W'_o$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"l'ensemble des supplémentaires totalement singuliers $W'_o$",
    note="Agreement error with the plural article 'des'. The TeX keeps the printed reading; the corrected layer too.")

add(page=67,
    where="'est compatible à toute extension des scalaires, dont définit un morphisme'",
    scan="dont définit un morphisme de S-schémas (checked at 2x)",
    tex=r"dont définit un morphisme",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"donc définit un morphisme",
    note="Typing error for 'donc': being compatible with every extension of scalars, the function defines a morphism of S-schemes. The TeX keeps the printed reading; the corrected layer too.")

add(page=67,
    where="'Le morphisme e se factorise donc par une section de E(∧^2 W') sur S'",
    scan="se factorise donc par une / section de E ( ∧^2 W') sur S, i.e. e(x) est indépendant de x",
    tex=r"se factorise donc par une section de $\mathbb{E}(\overset{2}{\wedge} W')$ sur $S$",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"se factorise donc par une section de $\mathrm{Spec}(Z(Q))$ sur $S$",
    note="e goes from E(∧^2 W') to the étale S-scheme Spec(Z(Q)); since E(∧^2 W') is flat with geometrically connected fibres, e factors through S, that is, through a section of Spec(Z(Q)) over S. A section of E(∧^2 W') over S has the wrong target. The author's slip. The TeX keeps the printed reading; the corrected layer already rewrites the clause ('se factorise donc par S, et par suite par une section de Spec(Z(Q)) sur S').")

add(page=67,
    where="1.8, 'On a vu en 1.6 que, pour λ inversible, C^+(Q) s'identifie à C^+(λ Q)'",
    scan="On a vu en 1.6 que (checked at 2.5x)",
    tex=r"On a vu en 1.6 que",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"On a vu en 1.3 que",
    note="Wrong reference number. The identification of C^+(Q) with C^+(λQ) is made in 1.3 (Lemme 1.3.1 and the paragraph after it, pp. 64-65); 1.6 treats the supplements of W and supplies only the continuity argument recalled next. The TeX keeps the printed reading; the corrected layer already reads 1.3.")

# ---------------- page 68 ----------------
add(page=68,
    where="1.9, 'si B et C sont deux algèbres Z/2-gradués'",
    scan="deux algèbres Z/2-gradués, alors, (checked at 2x)",
    tex=r"deux algèbres $\mathbb{Z}/2$-gradués, alors",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"deux algèbres $\mathbb{Z}/2$-graduées, alors",
    note="Agreement error. The TeX keeps the printed reading; the corrected layer too.")

add(page=68,
    where="'on identifie les algèbres Z/2-gradués End(P) ⊗' End(Q) et End(P ⊗ Q)'",
    scan="les algèbres Z/2-gradués End(P) ⊗' End(Q) (checked at 1x)",
    tex=r"les algèbres $\mathbb{Z}/2$-gradués $\mathrm{End}(P)",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"les algèbres $\mathbb{Z}/2$-graduées $\mathrm{End}(P)",
    note="Agreement error (the 'A-modules ... Z/2-gradués' of the line before are right). The TeX keeps the printed reading; the corrected layer too.")

add(page=68,
    where="heading 'Lemme 1.10.'",
    scan="only 'Lemme' is underlined; '1.10.' is not (checked at 2.2x)",
    tex=r"\underline{Lemme 1.10.}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{Lemme 1.10.}", "new": r"\underline{Lemme} 1.10."},
    note="The TeX underlines the number too. The other headings of the exposé already have the number outside: \\underline{Lemme} 1.3.1, \\underline{Proposition} 1.5, \\underline{Notation} 1.7, \\underline{Remarque} 2.2.")

add(page=68,
    where="diagram of Lemme 1.10, left vertical line from C(Q) to End(∧(W_1 ⊕ W_2))",
    scan="the ≀ stands to the right of the vertical line",
    tex=r'''\arrow[d, dash, "\wr"']''',
    kind="other", confidence="medium",
    fix={"old": r'''\arrow[d, dash, "\wr"']''', "new": r'''\arrow[d, dash, "\wr"]'''},
    note="Compiled: with the swap mark ' tikz-cd sets the label to the left of a downward line, without it to the right, as printed and as the file's own STRUCTURE comment says ('placed to the RIGHT of the stroke'). Placement only.")

# ---------------- page 69 ----------------
add(page=69,
    where="1.11, 'on peut ragarder Z'",
    scan="on peut ragarder Z (checked at 2x)",
    tex=r"on peut ragarder $Z$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"on peut regarder $Z$",
    note="Typing error. The TeX keeps the printed reading; the corrected layer too.")

add(page=69,
    where="1.11, 'comme un Z/2-torseurs sur S'",
    scan="comme un Z/2-torseurs sur S. (checked at 2x)",
    tex=r"comme un $\mathbb{Z}/2$-torseurs sur $S$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"comme un $\mathbb{Z}/2$-torseur sur $S$",
    note="Agreement error with the singular article. The TeX keeps the printed reading; the corrected layer too.")

add(page=69,
    where="1.11, 'soit e(s) l'idempotent de ρ_*O_Z'",
    scan="ρ_*O_Z with the Greek ρ, the same glyph as in s(ρ((e,0)) on p. 66; the p of 'p : Z → S' two lines above is a typed Latin p (checked at 2.5x)",
    tex=r"l'idempotent de $\rho_* \mathcal{O}_Z$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"l'idempotent de $p_* \mathcal{O}_Z$",
    note="The direct image is along p : Z → S, introduced in the same paragraph; ρ is the canonical map V → C(Q) of 1.3. The TeX keeps the printed reading; the corrected layer too.")

add(page=69,
    where="heading 'Proposition 1.12.'",
    scan="only 'Proposition' is underlined; '1.12.' is not (checked at 2x)",
    tex=r"\underline{Proposition 1.12.}",
    kind="underline", confidence="high",
    fix={"old": r"\underline{Proposition 1.12.}", "new": r"\underline{Proposition} 1.12."},
    note="As for Lemme 1.10 on p. 68.")

add(page=69,
    where="Proposition 1.12, 'V un vectoriel de dimension 2m > 0 sur V'",
    scan="un vectoriel de dimension 2m > 0 / sur V, Q une forme quadratique (checked at 2.5x)",
    tex=r"\underline{sur} $V$, $Q$",
    kind="misprint_in_print", confidence="high", fix=None,
    corrected=r"\underline{sur} $A$, $Q$",
    note="V is the vector space; the field is A ('Soient A un corps'). The TeX keeps the printed reading; the corrected layer already reads A.")

# ---------------- page 70 ----------------
add(page=70,
    where="section title '2. Quadriques'",
    scan="a small typed comma-shaped mark at mid-letter height right after the underlined 'Quadriques' (checked at 6x)",
    tex=r"2. \underline{Quadriques}'",
    kind="misprint_in_print", confidence="medium", fix=None,
    corrected=r"2. \underline{Quadriques}",
    note="A stray keystroke with no meaning in the title. The TeX keeps it as an apostrophe; the corrected layer too.")

# ---------------- validation ----------------
ok = True
texts = {}
for p in sorted({f["page"] for f in F} | {66, 67, 68, 69, 70}):
    with open(os.path.join(FOLDER, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()
for f in F:
    t = texts[f["page"]]
    if f["tex"] and t.count(f["tex"]) < 1:
        print("TEX QUOTE NOT FOUND", f["page"], repr(f["tex"])); ok = False
    if f["fix"]:
        n = t.count(f["fix"]["old"])
        if n != 1:
            print("FIX OLD COUNT", n, f["page"], repr(f["fix"]["old"])); ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("MARKER IN OLD", f["page"]); ok = False
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            print("NO CORRECTED", f["page"], f["where"]); ok = False
    elif "corrected" in f:
        print("CORRECTED ON NON-MISPRINT", f["page"], f["where"]); ok = False

# fixes on one page must not overlap
for p in texts:
    spans = []
    for f in F:
        if f["page"] == p and f["fix"]:
            i = texts[p].find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("OVERLAP", p, a[2], "|", b[2]); ok = False

# apply all fixes to a copy to make sure they apply in sequence
for p in texts:
    s = texts[p]
    for f in F:
        if f["page"] == p and f["fix"]:
            assert s.count(f["fix"]["old"]) == 1, (p, f["fix"]["old"])
            s = s.replace(f["fix"]["old"], f["fix"]["new"], 1)

order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
out = [{k: f[k] for k in order if k in f} for f in F]
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT, len(out))
else:
    print("NOT WRITTEN")
    sys.exit(1)

from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in sorted(texts):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
