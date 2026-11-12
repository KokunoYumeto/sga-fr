import json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
FOLDER = os.path.join(BASE, "b061_065")
OUT = os.path.join(BASE, "findings_061_065.json")

F = []

F.append({
    "page": 62,
    "where": "title of the exposé, 'QUADRIQUES'",
    "scan": "QUADRIQUES underlined twice (two parallel rules); 'E X P O S E XII' and 'par P. DELIGNE' have a single underline",
    "tex": r"\underline{QUADRIQUES}",
    "kind": "underline",
    "confidence": "high",
    "fix": {"old": r"\underline{QUADRIQUES}", "new": r"\underline{\underline{QUADRIQUES}}"},
    "note": "Same encoding as the double-underlined titles of Exposés X and XI.",
})

F.append({
    "page": 63,
    "where": "1.1, case b) after 'Si A est un corps, alors :'",
    "scan": "b) pour n impair et card(A) = 2 : (card; checked at 2x)",
    "tex": r"$\mathrm{card}(A) = 2$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"$\mathrm{car}(A) = 2$",
    "note": "Case b) is the complement of case a) ('n pair ou car(A) ≠ 2'), and the bilinear form is called alternée, which needs characteristic 2; card(A) = 2 would cover only the field with two elements. The TeX keeps the printed reading; the corrected layer still reads card(A).",
})

F.append({
    "page": 64,
    "where": "Proposition 1.2, both displayed normal forms (n = 2m, and resp. n = 2m+1), upper bound of the second sum",
    "scan": "Σ with limits 1 and m-1 before x_i x_{i+m}, in both displays (checked at 2x)",
    "tex": r"\sum_{1}^{m-1} x_i x_{i+m}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\sum_{1}^{m} x_i x_{i+m}",
    "note": "With the bound m-1 the coordinates x_m and x_{2m} do not occur, so Q would be degenerate, against 'Q ordinaire'; the proof splits off one hyperbolic plane per induction step, m in all (empty sum for m = 0). Applies to both displays. The TeX keeps the printed reading; the corrected layer already reads m in both.",
})

F.append({
    "page": 64,
    "where": "Proposition 1.2, second display '(resp. Q(...) = ... (λ inversible) .'",
    "scan": "(resp.  Q(Σ x_i e_i) = Σ x_i x_{i+m} + λx^2_{2m+1}  (λ inversible) .  (the parenthesis opened by '(resp.' is never closed)",
    "tex": r"(\lambda \text{ inversible}) \;.",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"(\lambda \text{ inversible})) \;.",
    "note": "Unclosed parenthesis. The TeX keeps the printed reading; the corrected layer too.",
})

F.append({
    "page": 64,
    "where": "proof of 1.2, 'Si f = -Q(f').e+f, on a'",
    "scan": "f = -Q(f').e+f,  (no prime on the last f; checked at 4x)",
    "tex": r"$f = -Q(f').e+f$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"$f = -Q(f').e+f'$",
    "note": "f is built from the f' just chosen: f = f' - Q(f')e gives Q(f) = Q(f') - Q(f')Φ(e,f') = 0 and Φ(e,f) = 1, as stated next. The TeX keeps the printed reading; the corrected layer already reads f'.",
})

F.append({
    "page": 65,
    "where": "paragraph 'Supposons Q partout non nulle sur S. Alors, le lemme 1.2.1 ...'",
    "scan": "le lemme 1.2.1 (checked at 1.3x)",
    "tex": "le lemme 1.2.1",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "le lemme 1.3.1",
    "note": "The homomorphisms [λ] : C^+(λQ) → C^+(Q) are those of Lemme 1.3.1 (p. 64); 1.2 is a proposition and there is no 1.2.1. The TeX keeps the printed reading; the corrected layer still reads 1.2.1.",
})

F.append({
    "page": 65,
    "where": "1.4, displayed definition of the contraction f⌞(e_1∧...∧e_p)",
    "scan": "Σ (-1)^i < e_i,f > e_o∧... ê_i...∧e_p : first factor e with index o (zero) and sign (-1)^i, while the left side is e_1∧...∧e_p (checked at 1.6x)",
    "tex": r"\sum (-1)^{i} < e_i , f > e_o \wedge",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\sum (-1)^{i-1} < e_i , f > e_1 \wedge",
    "note": "The left side starts at e_1, so the first factor on the right is e_1, and with indices from 1 the sign is (-1)^{i-1}: then f⌞e = <e,f>, which the isomorphism s of the next page (s(ρ(e,0)) = e∧, s(ρ(0,f)) = f⌞) needs for (e∧ + f⌞)^2 = Q(e+f) = <e,f>; with (-1)^i it gives -<e,f>. The print's e_0 and (-1)^i are the 0-based form of the formula. The TeX keeps the printed reading; the corrected layer already reads (-1)^{i-1} and e_1.",
})

F.append({
    "page": 65,
    "where": "first paragraph: 'la partie T^+(E) de l'algèbre tensorielle de E, qui vaut λ^n sur T^{2n}(E)'",
    "scan": "T^+(E), de E, T^{2n}(E) (letter E, three times)",
    "tex": r"$T^{+}(E)$ de l'algèbre tensorielle de $E$, qui vaut $\lambda^{n}$ sur $T^{2n}(E)$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"$T^{+}(V)$ de l'algèbre tensorielle de $V$, qui vaut $\lambda^{n}$ sur $T^{2n}(V)$",
    "note": "No E is defined in the exposé: the module is V (Lemme 1.3.1 takes x, y ∈ V; the next display has x ⊗ x - λQ(x)). E is the letter of Bourbaki, Alg. IX § 9, cited in 1.3, so this is probably the author's slip of notation rather than a typing error. The TeX keeps the printed reading; the corrected layer still reads E.",
})

# checks
ok = True
for f in F:
    path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
    txt = open(path, encoding="utf-8", newline="").read()
    if "\r" in txt:
        print("CRLF in", path)
    if f["fix"] is not None:
        n = txt.count(f["fix"]["old"])
        print(f["page"], "fix old count", n, repr(f["fix"]["old"]))
        if n != 1:
            ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
            print("marker in old")
    n2 = txt.count(f["tex"])
    print(f["page"], "tex count", n2, repr(f["tex"]))
    if n2 < 1:
        ok = False
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
    else:
        assert "corrected" not in f

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("written", OUT, len(F), "ok" if ok else "PROBLEM")
