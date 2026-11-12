import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
BATCH = os.path.join(RUN, "b436_438")
OUT = os.path.join(RUN, "findings_436_438.json")

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 436
add(436, "(6.2.4), first line of the brace",
    "H^o( ℙ^{n+1}, 𝒪_ℙ) ≃ 𝔽_q  (the brace has three lines)",
    "the cases begin with H^i(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P})=0",
    "missing", "high",
    fx("\\begin{cases}\nH^i(",
       "\\begin{cases}\nH^0(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P})\\simeq\\mathbb F_q\\\\\nH^i("),
    "The first line of (6.2.4) is missing from the TeX.")

add(436, "(6.2.4), second and third lines",
    "H^i(ℙ^{n+1}, 𝒪_ℙ) = 0   i ≠ 0 / H^i(ℙ^{n+1}, 𝒪_ℙ(-d)) = 0   i ≠ 0, n+1   ,  (only the final comma)",
    "=0,&i\\ne0,\\\\ ... =0,&i\\ne0,n+1,",
    "punctuation", "high",
    fx("=0,&i\\ne0,\\\\\nH^i(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P}(-d))=0,&i\\ne0,n+1,",
       "=0&i\\ne0\\\\\nH^i(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P}(-d))=0&i\\ne0,n+1,"),
    "The TeX adds three commas: after = 0 in both lines and after the first i ≠ 0.")

add(436, "sentence before (6.2.5)",
    "la suite exacte longue de cohomologie associé à (6.2.2), donne",
    "associée à (6.2.2) donne",
    "misprint_in_print", "high",
    fx("associée à", "associé à"),
    "Agreement error of the print (la suite ... associée). The TeX silently corrects.",
    corrected="associée à")

add(436, "sentence before (6.2.5)",
    "associé à (6.2.2), donne",
    "associée à (6.2.2) donne",
    "punctuation", "high",
    fx("(6.2.2) donne", "(6.2.2), donne"),
    "The print has a comma after (6.2.2).")

add(436, "(6.2.5), first and second lines",
    "H^o(V, 𝒪_V) ≃ 𝔽_q / H^i(V, 𝒪_V) = 0  si  i ≠ 0,n  (no punctuation; full stop only after the third line)",
    "\\simeq\\mathbb F_q,\\\\ ... =0,&\\text{si }i\\ne0,n,\\\\",
    "punctuation", "high",
    fx("\\simeq\\mathbb F_q,\\\\\nH^i(V,\\mathcal O_V)=0,&\\text{si }i\\ne0,n,\\\\",
       "\\simeq\\mathbb F_q\\\\\nH^i(V,\\mathcal O_V)=0&\\text{si }i\\ne0,n\\\\"),
    "The TeX adds three commas.")

add(436, "(6.2.7), right-hand side",
    "det (1-t(f^{q-1}𝔉_q)| H^{n+1}(ℙ^{n+1}, 𝒪_ℙ(-d))  .",
    "1-tf^{q-1}\\mathfrak F_q",
    "formula", "high",
    fx("=\n\\det\\!\\left(\n1-tf^{q-1}\\mathfrak F_q\n",
       "=\n\\det\\!\\left(\n1-t(f^{q-1}\\mathfrak F_q)\n"),
    "The print puts f^{q-1}𝔉_q in parentheses.")

add(436, "(6.2.7), right-hand side, end",
    "det (1-t(f^{q-1}𝔉_q)| H^{n+1}(ℙ^{n+1}, 𝒪_ℙ(-d))  .  (four opening, three closing parentheses)",
    "\\right).",
    "misprint_in_print", "high",
    fx("\\right).", "\\right.."),
    "The parenthesis after det is never closed in the print. The TeX silently closes it; the fix keeps \\left( and drops the closing parenthesis.",
    corrected="\\right).")

add(436, "(6.2.8), left-hand side",
    "det(1-t(f^{q-1}𝔉_q)|H^{n+1}(ℙ^{n+1},𝒪_ℙ(-d))  =",
    "1-tf^{q-1}\\mathfrak F_q",
    "formula", "high",
    fx("&\\det\\!\\left(\n1-tf^{q-1}\\mathfrak F_q\n",
       "&\\det\\!\\left(\n1-t(f^{q-1}\\mathfrak F_q)\n"),
    "The print puts f^{q-1}𝔉_q in parentheses, as in (6.2.7).")

add(436, "(6.2.8), left-hand side, end",
    "det(1-t(f^{q-1}𝔉_q)|H^{n+1}(ℙ^{n+1},𝒪_ℙ(-d))  =  (four opening, three closing parentheses)",
    "\\right)\\\\",
    "misprint_in_print", "high",
    fx("\\right)\\\\", "\\right.\\\\"),
    "As in (6.2.7): the parenthesis after det is never closed. The TeX silently closes it.",
    corrected="\\right)\\\\")

add(436, "(6.2.8), right-hand side",
    "Ψ_q·(X_o f(X))^{q-1}  (filled centred dot)",
    "\\psi_q\\circ(X_0f(X))^{q-1}",
    "symbol", "high",
    fx("\\psi_q\\circ(X_0f(X))^{q-1}\n\\mathrel",
       "\\psi_q\\cdot(X_0f(X))^{q-1}\n\\mathrel"),
    "A filled centred dot, not the small circle of (6.3.2).")

add(436, "(6.2.8), right-hand side",
    "det(1-t(Ψ_q·(X_o f(X))^{q-1}|W_S(1))  (the parenthesis before Ψ_q is never closed)",
    "\\det\\!\\left(\n1-t\\,\\psi_q",
    "misprint_in_print", "high",
    fx("1-t\\,", "1-t\\,("),
    "The print opens a parenthesis before Ψ_q and closes none for it (five opening, four closing). The TeX silently drops it; its reading without the parenthesis is the corrected one.",
    corrected="1-t\\,")

add(436, "(6.2.8), end",
    "...|W_S(1))  (no punctuation; the line is the right-most text of the page)",
    "\\right),",
    "punctuation", "high",
    fx("\\right),", "\\right)"),
    "The TeX adds a comma after (6.2.8).")

add(436, "Proposition 6.3, label and first words",
    "Proposition (underlined) 6.3. (not underlined)  Il y a un isomorphisme (underlined)",
    "\\underline{Proposition 6.3.}\nIl y a un isomorphisme",
    "underline", "high",
    fx("\\underline{Proposition 6.3.}\nIl y a un isomorphisme",
       "\\underline{Proposition} 6.3.\n\\underline{Il y a un isomorphisme}"),
    "The number is not underlined; the statement is.")

add(436, "Proposition 6.3, after (6.3.1)",
    "par rapport auquel l'opérateur (underlined)",
    "par rapport auquel l'opérateur",
    "underline", "high",
    fx("par rapport auquel l'opérateur", "\\underline{par rapport auquel l'opérateur}"),
    "Part of the statement of Proposition 6.3.")

add(436, "(6.3.1)",
    "Hom_{𝔽_q}(H^{n+1}( ℙ^{n+1}. 𝒪_ℙ(-d), 𝔽_q)  (full stop after ℙ^{n+1})",
    "H^{n+1}(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P}(-d)),",
    "misprint_in_print", "high",
    fx("\\left(\nH^{n+1}(\\mathbb P^{n+1},", "\\left(\nH^{n+1}(\\mathbb P^{n+1}."),
    "A round full stop on the baseline (7 px high), without the tail of the comma before 𝔽_q in the same line (12 px). The TeX silently corrects.",
    corrected="\\left(\nH^{n+1}(\\mathbb P^{n+1},")

add(436, "(6.3.1)",
    "𝒪_ℙ(-d), 𝔽_q)  (H^{n+1}( is never closed)",
    "(-d)),",
    "misprint_in_print", "high",
    fx("(-d)),", "(-d),"),
    "The print has one closing parenthesis after -d. The TeX silently supplies the second.",
    corrected="(-d)),")

# ---------------------------------------------------------------- page 437
add(437, "first line",
    "est le transposé de (underlined)",
    "est le transposé de",
    "underline", "high",
    fx("est le transposé de", "\\underline{est le transposé de}"),
    "End of the statement of Proposition 6.3.")

add(437, "(6.3.4), left-hand side",
    "H^{i+1}(ℙ^{n+1}, 𝒪_ℙ(-d))",
    "H^{i+1}(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P}(-d))",
    "misprint_in_print", "high",
    None,
    "The group computed is H^{n+1} (named in the sentence before). The TeX keeps the printed i+1.",
    corrected="H^{n+1}(\\mathbb P^{n+1},\\mathcal O_{\\mathbb P}(-d))")

add(437, "(6.3.4), second line",
    "X_1^{W_1}...X_{n+2}^{W_{n+2}} / les W_i ∈ ℤ vérifiant Σ W_i = -d",
    "X_{n+2}^{W_{n+2}},\n\\qquad W_i\\in\\mathbb Z,\\quad",
    "missing", "high",
    fx("X_{n+2}^{W_{n+2}},\n\\qquad W_i\\in\\mathbb Z,\\quad",
       "X_{n+2}^{W_{n+2}}\n\\qquad\\text{les }W_i\\in\\mathbb Z\\text{ vérifiant }"),
    "The TeX drops the words 'les' and 'vérifiant' and puts commas (after the monomial and after ℤ) in their place.")

add(437, "(6.3.4), second line",
    "Σ W_i = -d  (Σ without index)",
    "\\sum_iW_i",
    "formula", "high",
    fx("\\sum_iW_i", "\\sum W_i"),
    "The TeX adds the index i under Σ.")

add(437, "(6.3.4), second line, end",
    "= -d  (no punctuation)",
    "=-d,\\\\",
    "punctuation", "high",
    fx("=-d,\\\\", "=-d\\\\"),
    "The TeX adds a comma.")

add(437, "(6.3.5), second line",
    "(π X_o) X_1^{U_1}... X_{n+2}^{U_{n+2}} vérifiant Σ U_i = d,  U_i > 0 ∀_i .",
    "X_{n+2}^{U_{n+2}},\n\\qquad\n\\sum_iU_i",
    "missing", "high",
    fx("X_{n+2}^{U_{n+2}},\n\\qquad\n", "X_{n+2}^{U_{n+2}}\n\\text{ vérifiant }\n"),
    "The TeX drops 'vérifiant' and puts a comma in its place.")

add(437, "(6.3.5), second line",
    "Σ U_i = d  (Σ without index)",
    "\\sum_iU_i",
    "formula", "high",
    fx("\\sum_iU_i", "\\sum U_i"),
    "The TeX adds the index i under Σ.")

add(437, "(6.3.5), second line, end",
    "U_i > 0 ∀_i .  (the i after ∀ is a subscript)",
    "\\forall i.",
    "formula", "high",
    fx("\\forall i.", "\\forall_i."),
    "The i after ∀ is typed at the level of the subscript of U_i.")

add(437, "(6.3.7), left-hand side",
    "(classe de π X_o X_1^{U_1}...X_{n+2}^{U_{n+2}}, X_1^{W_1}...X_{n+2}^{W_{n+2}})",
    "\\operatorname{classe}\\!\\left(\n\\pi X_0X_1^{U_1}\\cdots X_{n+2}^{U_{n+2}}\n\\right),",
    "word", "high",
    fx("\\operatorname{classe}\\!\\left(\n\\pi X_0X_1^{U_1}\\cdots X_{n+2}^{U_{n+2}}\n\\right),",
       "\\text{classe de }\\pi X_0X_1^{U_1}\\cdots X_{n+2}^{U_{n+2}},"),
    "The print reads 'classe de' with no parentheses round the monomial; the TeX writes classe(...) without 'de'.")

add(437, "(6.3.7), first case",
    "1 si U_1 = -W_i pour tout i  (no punctuation)",
    "1,&\\text{si }",
    "punctuation", "high",
    fx("1,&\\text{si }", "1&\\text{si }"),
    "The TeX adds a comma after the value 1.")

add(437, "(6.3.7), first case",
    "1 si U_1 = -W_i pour tout i  (subscript 1, the digit of the value 1)",
    "U_i=-W_i",
    "misprint_in_print", "high",
    fx("U_i=-W_i", "U_1=-W_i"),
    "U_1 for U_i (against W_i and 'pour tout i'). The TeX silently corrects.",
    corrected="U_i=-W_i")

add(437, "(6.3.7), end of both cases",
    "... pour tout i / 0 sinon  (no punctuation)",
    "i,\\\\\n0,&\\text{sinon},",
    "punctuation", "high",
    fx("i,\\\\\n0,&\\text{sinon},", "i\\\\\n0&\\text{sinon}"),
    "The TeX adds three commas (after 'tout i', after 0 and after 'sinon').")

add(437, "last paragraph",
    "Ψ_q.(X_o f(X))^{q-1}  (dot typed low, as a full stop)",
    "\\psi_q\\circ(X_0f(X))^{q-1}",
    "symbol", "high",
    fx("\\psi_q\\circ", "\\psi_q\\cdot"),
    "A filled dot, not the small circle (the circle next to it is the index o of X_o).")

add(437, "last paragraph",
    "f(X)^{q-1}•f_q  (centred dot)",
    "$f(X)^{q-1}\\mathfrak F_q$",
    "symbol", "high",
    fx("$f(X)^{q-1}", "$f(X)^{q-1}\\cdot "),
    "The print's centred dot is omitted. The trailing space keeps the next command separate.")

add(437, "last paragraph",
    "f(X)^{q-1}•f_q, ce qui  (small typed f)",
    "\\mathfrak F_q$, ce qui",
    "misprint_in_print", "high",
    fx("\\mathfrak F_q$, ce", "f_q$, ce"),
    "The print types the letter f of f(X) for the Fraktur 𝔉_q of (6.3.3). The TeX silently corrects.",
    corrected="\\mathfrak F_q$, ce")

# ---------------------------------------------------------------- page 438
bib = [
    ("[1]", "\\item Ax, J.", "\\item AX, J.", "AX, J.",
     "\\emph{Zeroes of Polynomials Over Finite Fields}"),
    ("[2]", "255--261.\n\\item Dwork, B.", "255--261.\n\\item DWORK, B.", "DWORK, B.",
     "\\emph{On the Rationality of the Zeta Function of an\n  Algebraic Variety}"),
    ("[3]", "631--648.\n\\item Dwork, B.", "631--648.\n\\item DWORK, B.", "DWORK, B.",
     "\\emph{An Algebraic Variety}"),
    ("[4]", "(miméo).\n\\item Dwork, B.", "(miméo).\n\\item DWORK, B.", "DWORK, B.",
     "\\emph{On the Zeta Function of Hypersurface II}"),
    ("[5]", "\\item Grothendieck,", "\\item GROTHENDIECK,", "GROTHENDIECK, A.,",
     "\\emph{Le Groupe de Brauer III}, dans\n  \\emph{Dix Exposés sur la Cohomologie des Schémas}"),
    ("[6]", "1968.\n\\item Serre, J.P.", "1968.\n\\item SERRE, J.P.", "SERRE, J.P.",
     "\\emph{Groupes Algébriques et Corps de Classes}"),
    ("[7]", "1959.\n\\item Serre, J.P.", "1959.\n\\item SERRE, J.P.", "SERRE, J.P.",
     "\\emph{Endomorphismes Complètement Continus des Espaces\n  de Banach $p$-Adiques}"),
    ("[8]", "\\item Chevalley, C.", "\\item CHEVALLEY, C.", "CHEVALLEY, C.",
     "\\emph{Démonstration d'une hypothèse de M. Artin}"),
]


def unemph(s):
    return s.replace("\\emph{", "").replace("}", "")


for lab, nold, nnew, nscan, eold in bib:
    name_tex = nold.split("\\item ")[1]
    add(438, "Bibliographie %s, author" % lab,
        "%s (capitals)" % nscan, name_tex,
        "word", "high", fx(nold, nnew),
        "Author's name in capitals in the print.")
    if lab == "[5]":
        add(438, "Bibliographie [5], after the initial",
            "GROTHENDIECK, A.,  Le Groupe", "Grothendieck, A. \\emph{Le Groupe",
            "punctuation", "high", fx(" A. ", " A., "),
            "The print has a comma after the initial.")
    add(438, "Bibliographie %s, title" % lab,
        "%s (plain type, not underlined)" % unemph(eold).replace("\n  ", " "),
        eold.replace("\n  ", " "),
        "font", "high", fx(eold, unemph(eold)),
        "Titles are typed plain in the print; the TeX sets them in \\emph." if lab == "[1]" else "As in [1].")
    if lab == "[2]":
        add(438, "Bibliographie [2], title",
            "On the Rationality of the Zéta Function  (é)",
            "Zeta Function of an",
            "misprint_in_print", "medium", fx("Zeta Function of an", "Zéta Function of an"),
            "Typed é (the accent of 'Algébriques' on this page) in the English title; [4] prints Zeta. The TeX silently corrects. Apply after the \\emph fix of this title (overlapping strings).",
            corrected="Zeta Function of an")
    if lab == "[7]":
        add(438, "Bibliographie [7], title",
            "Endomorphismes Complétement, Continus  (acute accent)",
            "Complètement",
            "misprint_in_print", "medium", fx("Complètement", "Complétement"),
            "Acute accent (the grave of 'hypothèse' in [8] slopes the other way); Serre's title has 'complètement'. The TeX silently corrects. Apply after the \\emph fix of this title.",
            corrected="Complètement")
        add(438, "Bibliographie [7], title",
            "Complétement, Continus  (comma inside the title)",
            "Complètement Continus",
            "misprint_in_print", "high", fx(" Continus", ", Continus"),
            "Stray comma inside the title. The TeX silently drops it. Apply after the \\emph fix of this title.",
            corrected=" Continus")

# ---------------------------------------------------------------- checks
texts = {}
for p in (436, 437, 438):
    with open(os.path.join(BATCH, "page_%d.tex" % p), encoding="utf-8", newline="") as fh:
        texts[p] = fh.read()

ok = True
work = dict(texts)
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    n_orig = texts[d["page"]].count(old)
    n_work = work[d["page"]].count(old)
    if "%%%%%%%%%%" in old:
        print("MARKER IN OLD", i)
        ok = False
    flag = "" if n_orig == 1 else "  <-- count in original page file = %d" % n_orig
    if n_work != 1:
        flag += "  <-- count at sequential application = %d" % n_work
        ok = False
    if n_orig != 1:
        ok = ok and n_work == 1
    print(d["page"], d["kind"], repr(old)[:70], n_orig, n_work, flag)
    work[d["page"]] = work[d["page"]].replace(old, new, 1)

print("ALL OK" if ok else "PROBLEMS")
for p in (436, 437, 438):
    print("=" * 30, p)
    print(work[p])

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", OUT, len(F))
