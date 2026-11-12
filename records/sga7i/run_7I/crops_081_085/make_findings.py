import json, os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
BATCH = os.path.join(RUN, "b081_085")
OUT = os.path.join(RUN, "findings_081_085.json")

F = []

def add(**kw):
    F.append(kw)

# ---------------- page 81 ----------------
add(page=81,
    where="Corollary 3.8 (a), 'If A, B are R-algebras such that Tor^R_i(A, B) = 0'",
    scan="'are' and 'algebras such that' are underlined; the underline starts after the hyphen of 'R-' (checked in a crop)",
    tex=r"$R$\underline{-algebras such that}",
    kind="underline", confidence="medium",
    fix={"old": r"$R$\underline{-algebras such that}", "new": r"$R$-\underline{algebras such that}"},
    note=r"Underline extent only: neither R nor the hyphen is underlined. The file's own form for this is R-\underline{algebra} (Corollary 3.13).")

add(page=81,
    where="Corollary 3.8 (b), 'Let A be an R-algebra such that Tor^R_i(A, A) = 0'",
    scan="'be an' and 'algebra such that' are underlined; the underline starts after the hyphen of 'R-' (checked in a crop)",
    tex=r"$R$\underline{-algebra such that}",
    kind="underline", confidence="medium",
    fix={"old": r"$R$\underline{-algebra such that}", "new": r"$R$-\underline{algebra such that}"},
    note="Underline extent only, as in (a).")

add(page=81,
    where="Proof of 3.8 (a), exact sequence (*)",
    scan="... -> H^i(A(x)_R B A, F_A) -> H^i(A(x)_R B R, F) -> H^i(A |R, F) -> ....: no bar in the first two terms (clean gaps in a crop); the third term has its inked bar",
    tex=r"H^{i}(A\underset{R}{\otimes}B\ A,\ F_{A}) \rightarrow H^{i}(A\underset{R}{\otimes}B\ R,\ F)",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"H^{i}(A\underset{R}{\otimes}B|A,\ F_{A}) \rightarrow H^{i}(A\underset{R}{\otimes}B|R,\ F)",
    note="The two inked bars were never drawn: the same groups are H^i(A(x)_R B|A, F_A) and H^i(A(x)_R B|R, F) in the diagram below and on p. 82. The TeX keeps the printed gaps. 'corrected' replaces the 'tex' substring.")

add(page=81,
    where="Proof of 3.8 (a), 'the ring homomorphisms R -> A -> A(x)_R B gives us the exact sequence'",
    scan="homomorphisms ... gives us",
    tex="gives us the exact sequence",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected="give us the exact sequence",
    note="Verb agreement slip (plural subject); the proof of 3.9 on p. 82 repeats it. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 82 ----------------
add(page=82,
    where="Proof of 3.9, 'the ring homomorphisms R -> A -> S^{-1}A gives us the exact sequence'",
    scan="homomorphisms ... gives us",
    tex="gives us the exact sequence",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected="give us the exact sequence",
    note="Verb agreement slip, as in the proof of 3.8 (a) on p. 81. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 83 ----------------
add(page=83,
    where="Definition 3.10, 'Let A be an R-algebra. For each A-module M we set'",
    scan="'algebra. For each' is underlined from the a of 'algebra'; 'R-' is not underlined (checked in a crop)",
    tex=r"$R$\underline{-algebra. For each}",
    kind="underline", confidence="medium",
    fix={"old": r"$R$\underline{-algebra. For each}", "new": r"$R$-\underline{algebra. For each}"},
    note="Underline extent only (the hyphen), as on p. 81.")

add(page=83,
    where="Definition 3.10, 'For each A-module M we set'",
    scan="'module' is underlined; 'A-' is not (checked in a crop)",
    tex=r"$A$\underline{-module}",
    kind="underline", confidence="medium",
    fix={"old": r"$A$\underline{-module}", "new": r"$A$-\underline{module}"},
    note="Underline extent only (the hyphen). Does not overlap the previous entry.")

add(page=83,
    where="Proof of Lemma 3.10, exact sequence (b), last term 'Hom_A(I, M) -> 0'",
    scan="Hom_A(I, M): plain I without the overbar (clean in a crop, beside the barred I of Hom_A(I-bar^(n), M) in the same line)",
    tex=r"\mathrm{Hom}_A(I,\ M) \to 0",
    kind="misprint_in_print", confidence="medium",
    fix=None,
    corrected=r"\mathrm{Hom}_A(\overline{I},\ M) \to 0",
    note="Hom(Delta, M) is induced by the diagonal I-bar -> I-bar^(n) (Delta(I-bar) in the first term), and I is not an A-module; p. 84 uses Hom_A(I-bar, M) in the resulting exact sequence. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=83,
    where="Proof of Lemma 3.10, 'Since {I -> 0} , {I -> I} admits sections'",
    scan="admits",
    tex="admits sections",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected="admit sections",
    note="Verb agreement slip (two subjects). Low: possibly the author's own wording ('each admits'). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 84 ----------------
add(page=84,
    where="Lemma 3.11, 'D^2(A|R, M) ~ Coker(H^1(K_I, M) -> Hom_A(H_1(K^I), M))'",
    scan="H_1(K^I): the I of K is raised as a superscript (checked in a crop); K_I with subscript earlier in the same formula",
    tex=r"H_1(K^I)",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"H_1(K_I)",
    note="K_I is the Koszul complex just defined ('denoted ... by K_I'); the proof on p. 85 has Hom_P(H_1(K_I), M). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring. See the p. 85 entry for the proof's last line.")

add(page=84,
    where="Proof of Lemma 3.11, first line 'D^2(A|R, M) = H^1(A|R, H^1_{A|R}(Der_R(-, M)))'",
    scan="the inner H is not underlined (clean in a crop); it is underlined in Lemma 3.10, at the end of the D^1 block and in the 'since' line below",
    tex=r"&= H^1(A|R,\ H^1_{A|R}",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected=r"&= H^1(A|R,\ \underline{H}^1_{A|R}",
    note="The coefficient is the presheaf H-underline^1_{A|R}(Der_R(-, M)) of Lemma 3.10. Low: a left-out underline rather than a typing error. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

add(page=84,
    where="Proof of Lemma 3.11, 'since [H^1_{A|R}(Der_R(-, M))](P_A^0) = ...'",
    scan="P_A^0: superscript 0 without parentheses (checked in a crop)",
    tex=r"](P_A^0)",
    kind="misprint_in_print", confidence="low",
    fix=None,
    corrected=r"](P_A^{(0)})",
    note="Elsewhere P_A^{(n)} with parentheses (P_A^{(0)} = P in the simplicial algebra (*) of p. 83). Low: a notation slip. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.")

# ---------------- page 85 ----------------
add(page=85,
    where="'D^2(A|R, M) = Ker(D^1(P_A^(1)|R, M) => D^1(P_A^(2)|R, M))'",
    scan="three stacked arrows between the two D^1 (checked in a crop), as in the corresponding Ker(H^1(...) => H^1(...)) on p. 84",
    tex=r"M) \rightrightarrows D^1(",
    kind="symbol", confidence="high",
    fix={"old": r"M) \rightrightarrows D^1(", "new": r"M) \mathrel{\substack{\to\\ \to\\ \to}} D^1("},
    note=r"The TeX sets two arrows. The replacement is the file's own form for the triple arrow (p. 84, p. 83 (*)).")

add(page=85,
    where="'Now 0 -> (F) -> P[F] --P[0]-- P -> 0'",
    scan="P[0] over a ruled line with no arrowhead; the line ends cleanly (checked in a crop)",
    tex=r"\xrightarrow{\;\;P[0]\;\;}",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"\xrightarrow{\;\;P[0]\;\;}", "new": r"\overset{\;\;P[0]\;\;}{\relbar\joinrel\relbar\joinrel\relbar}"},
    corrected=r"\xrightarrow{\;\;P[0]\;\;}",
    note=r"The head was never drawn (the other arrows of the two lines have theirs). The TeX silently supplies it; the fix restores the printed headless rule in the file's own form (p. 38 a' \overset{\ \rho\ }{\relbar\joinrel\relbar\joinrel\relbar} a_1). 'corrected' is the current TeX. Goes with the next entry.")

add(page=85,
    where="'0 -> (F_gamma) -> P[F] --P[gamma]-- P -> 0 .'",
    scan="P[gamma] over a ruled line with no arrowhead; the line ends cleanly (checked in a crop)",
    tex=r"\xrightarrow{\;\;P[\gamma]\;\;}",
    kind="misprint_in_print", confidence="medium",
    fix={"old": r"\xrightarrow{\;\;P[\gamma]\;\;}", "new": r"\overset{\;\;P[\gamma]\;\;}{\relbar\joinrel\relbar\joinrel\relbar}"},
    corrected=r"\xrightarrow{\;\;P[\gamma]\;\;}",
    note="As the previous entry (same display). 'corrected' is the current TeX.")

add(page=85,
    where="Last display, '= Coker(H^1(K_I, M) -> Hom_A(H^1(K_I), M))'",
    scan="Hom_A(H^1(K_I), M): the 1 of the second H is raised (checked in a crop)",
    tex=r"\mathrm{Hom}_A(H^1(K_I), M)",
    kind="misprint_in_print", confidence="high",
    fix=None,
    corrected=r"\mathrm{Hom}_A(H_1(K_I), M)",
    note="The homology H_1(K_I) of the line above (Hom_P(H_1(K_I), M)) and of Lemma 3.11. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring. With the p. 84 entry (K^I), statement and proof then both read Hom_A(H_1(K_I), M).")

# ---------------- checks ----------------
ok = True
for x in F:
    p = os.path.join(BATCH, "page_%03d.tex" % x["page"])
    s = open(p, encoding="utf-8").read()
    n_tex = s.count(x["tex"])
    if n_tex != 1:
        ok = False
        print("TEX COUNT", x["page"], n_tex, repr(x["tex"]))
    if x["fix"] is not None:
        n_old = s.count(x["fix"]["old"])
        if n_old != 1:
            ok = False
            print("OLD COUNT", x["page"], n_old, repr(x["fix"]["old"]))
        if "%%%%%%%%%%" in x["fix"]["old"]:
            ok = False
            print("MARKER IN OLD", x["page"])
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        ok = False
        print("NO CORRECTED", x["page"], x["where"])
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        ok = False
        print("CORRECTED ON NON-MISPRINT", x["page"])

order = ["page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"]
F2 = [{k: x[k] for k in order if k in x} for x in F]
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F2, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
for pg in range(81, 86):
    print(pg, "normal", c[(pg, False)], "misprint", c[(pg, True)])
print("ALL CHECKS OK" if ok else "CHECK FAILURES", len(F))
