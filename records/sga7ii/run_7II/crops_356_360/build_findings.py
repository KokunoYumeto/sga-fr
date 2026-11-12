import json, pathlib, sys
from collections import Counter

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
B = RUN / "b356_360"
OUT = RUN / "findings_356_360_recheck.json"


def M(page, where, scan, tex, conf, corrected, note):
    return {"page": page, "where": where, "scan": scan, "tex": tex, "kind": "misprint_in_print",
            "confidence": conf, "fix": None, "corrected": corrected, "note": note}


F = [
    M(356, "4.3, first sentence: 'du moins pour D assez général  On a déjà vu que'",
      "assez général  On a déjà vu (no full stop after 'général': its character cell is blank at 5x; the next word is capitalised)",
      "assez général  On a déjà vu", "medium", "assez général. On a déjà vu",
      "A full stop is missing between two sentences. The TeX keeps the printed reading."),
    M(356, "4.3, 'rendent plausibles qu'il en est encore de même si car k > 0'",
      "rendent plausibles qu'il en est",
      "rendent plausibles qu'il en est", "medium", "rendent plausible qu'il en est",
      "Agreement slip: the attribute of the que-clause is invariable, as in '(resp rendent plausible) que' three lines lower. The TeX keeps the printed reading."),
    M(356, "4.3, '(théorie de Hodge, resp cohomologie cristalline)'",
      "resp at the end of the line, with no point (5x)",
      "resp cohomologie cristalline", "medium", "resp. cohomologie cristalline",
      "The abbreviation lacks its point; the same paragraph has '(resp. tout pinceau'. The TeX keeps the printed reading."),
    M(356, "4.3, 'prouvent (resp  rendent plausible) que'",
      "(resp  rendent: no point; the character cell after 'resp' is blank (5x)",
      "(resp  rendent plausible)", "medium", "(resp. rendent plausible)",
      "The abbreviation lacks its point, as in the previous line. The TeX keeps the printed reading."),
    M(356, "4.4, first sentence: 'Soit z un cycle algébrique de codimension n sur X , tel que'",
      "de codimension n sur X",
      "de codimension $n$ sur $X$", "medium", "de codimension $m$ sur $X$",
      "4.4 proves Théorème 4.1 (p. 355: X of dimension n = 2m, z of codimension m, cl(z) in H^{2m}(X,Q_l(m))); "
      "4.4 itself works with H^{*+2(m-1)}, H^{2m-1} and Prim^{2m}, and a cycle of codimension n = dim X would restrict "
      "to zero on X_eta-bar. Same n-for-m slip as in (4.4.4) and three times on p. 360. The TeX keeps the printed n."),
    M(357, "(4.4.3)",
      "t_i(eta-bar) : Sp(k(eta-bar)) --> C , i=1,2 , (target C with no subscript)",
      "\\mathrm{Sp}(k(\\bar{\\eta})) \\longrightarrow C \\quad", "low",
      "\\mathrm{Sp}(k(\\bar{\\eta})) \\longrightarrow C_{\\bar{\\eta}} \\quad",
      "The sections are k(eta-bar)-points of the curve C_eta-bar of (4.4.2); a curve C (C --> U with generic geometric "
      "fibre C_eta-bar) is introduced only on p. 359. Possibly a deliberate abbreviation, hence low. The TeX keeps the printed C."),
    M(357, "(4.4.4)",
      "un cycle algébrique P_eta-bar sur C_eta-bar x X_eta-bar , de codimension n ,",
      "\\text{, de codimension} \\quad n \\;", "medium",
      "\\text{, de codimension} \\quad m \\;",
      "P_eta-bar(t_1) - P_eta-bar(t_2) = z_eta-bar has codimension m (Théorème 4.1), and (4.4.6) shifts degree by 2(m-1) "
      "and twist by m-1, which needs codimension m on C_eta-bar x X_eta-bar. Same n-for-m slip as on p. 356. The TeX keeps the printed n."),
    M(357, "(4.4.6), target",
      "H^{*+2(m-1)}(X_eta-bar, Q_l((i+m-1)) : doubled opening parenthesis (2x)",
      "\\mathbb{Q}_{\\ell}((i+m-1))", "high", "\\mathbb{Q}_{\\ell}(i+m-1))",
      "Three opening and two closing parentheses; (4.4.7)-(4.4.9) write Q_l(i+m-1). The TeX keeps the printed reading."),
    M(357, "after (4.4.7): 'une correspondance algébrique composée Q_eta-bar = V_eta-bar o P sur'",
      "V_eta-bar o P, P without subscript (2x)",
      "V_{\\bar{\\eta}} \\circ P$ sur", "low", "V_{\\bar{\\eta}} \\circ P_{\\bar{\\eta}}$ sur",
      "Only P_eta-bar is defined, and (4.4.8) repeats the composite as V_eta-bar o P_eta-bar. The TeX keeps the printed reading."),
    M(357, "last line: 'la correspondance composée m^* Q_eta-bar _eta-bar sur (C_eta-bar, X_eta-bar)'",
      "m^* Q_eta-bar followed by a second, free-standing handwritten eta-bar with nothing above it (3x)",
      "m^{*} Q_{\\bar{\\eta}} \\;\\; {}_{\\bar{\\eta}}", "medium", "m^{*} Q_{\\bar{\\eta}}",
      "Stray subscript: the composite is m^*Q_eta-bar, as in (4.4.9). The TeX reproduces it."),
    M(358, "(4.4.10)",
      "R_eta-bar = P_eta-bar m^*Q_eta-bar =(id-m^*V_eta-bar)P_eta-bar : no minus sign between P_eta-bar and m^*Q_eta-bar; "
      "the dash right of P is the bar of its eta-bar, placed as after R (pixel map of the line)",
      "R_{\\bar\\eta} = P_{\\bar\\eta} m^*Q_{\\bar\\eta}", "high",
      "R_{\\bar\\eta} = P_{\\bar\\eta} - m^*Q_{\\bar\\eta}",
      "(id - m^*V_eta-bar)P_eta-bar = P_eta-bar - m^*Q_eta-bar by (4.4.8)-(4.4.9). The TeX keeps the printed reading."),
    M(358, "formula number (4 4.12) before 'l'homomorphisme (4.4.11) est nul'",
      "(4 4.12): the character cell between the first 4 and the second 4 is blank (6x)",
      "(4 4.12)", "medium", "(4.4.12)",
      "Missing point in the formula number (it may have failed to print; nothing shows in the scan). The TeX keeps the printed reading."),
    M(358, "'Choissisons maintenant une extension finie'",
      "Choissisons",
      "Choissisons", "high", "Choisissons",
      "Typing error. The TeX keeps it."),
    M(359, "display 'z_U = M^* pr_i^*(z) ,'",
      "pr with a dotted i as subscript (3x); the typewriter's digit 1 has no dot (t_1 in (4.4.13))",
      "\\mathrm{pr}_i^*(z)", "medium", "\\mathrm{pr}_1^*(z)",
      "z is a cycle on X, so the first projection X x U --> X is meant (pr_2, the projection to U, labels u_{pr_2} on p. 360). "
      "The TeX keeps the printed i."),
    M(360, "display after '(XVIII 5.8.7)', source of grif",
      "Prim^{2m}(X, Q_l(n))",
      "\\mathrm{Prim}^{2m}(X,\\mathbb{Q}_\\ell(n))", "medium",
      "\\mathrm{Prim}^{2m}(X,\\mathbb{Q}_\\ell(m))",
      "The Griffiths map keeps the twist (XVIII 5.8.7.1: Prim^n(X,Q_l(j)) --> H^1(V,R^{n-1}rho_{V*}Q_l(j)), modulo the "
      "fixed part); the target here has (m), and cl(z) lies in H^{2m}(X,Q_l(m)) (Théorème 4.1). Same n-for-m slip. "
      "The TeX keeps the printed n."),
    M(360, "same display, denominator",
      "M^*H^1(U,H^{2m-1}(X,Q_l(m)) : three opening, two closing parentheses",
      "{M^*H^1(U,H^{2m-1}(X,\\mathbb{Q}_\\ell(m))}", "high",
      "{M^*H^1(U,H^{2m-1}(X,\\mathbb{Q}_\\ell(m)))}",
      "A closing parenthesis is missing. The TeX keeps it."),
    M(360, "'se trouve dans M^*(H^1(U,H^{2m-1}(X,Q_l(m)) .'",
      "M^*(H^1(U,H^{2m-1}(X,Q_l(m)) : four opening, two closing parentheses",
      "$M^*(H^1(U,H^{2m-1}(X,\\mathbb{Q}_\\ell(m))$", "high",
      "$M^*(H^1(U,H^{2m-1}(X,\\mathbb{Q}_\\ell(m))))$",
      "Two closing parentheses are missing. The TeX keeps it."),
    M(360, "'Or, compte tenu de la décomposition (4.4.13), et de la commutativité de (1 4.2)'",
      "(1 4.2): the character cell between 1 and 4 is blank (5x)",
      "commutativité de (1 4.2)", "medium", "commutativité de (1.4.2)",
      "The commutative diagram (1.4.2) of p. 346, cited as (1.4.2) on pp. 347 and 349. Missing point; the TeX keeps the printed reading."),
    M(360, "diagram, row 1 column 2",
      "Prim^{2m}(XxU/U, Q_l(n))",
      "\\mathrm{Prim}^{2m}(X\\times U/U,\\mathbb{Q}_\\ell(n))", "medium",
      "\\mathrm{Prim}^{2m}(X\\times U/U,\\mathbb{Q}_\\ell(m))",
      "M^* and u_{pr_2} send this node to objects with twist (m), and Q (a correspondence of codimension m) sends "
      "Prim^2(C/U,Q_l(1)) to twist m. Same n-for-m slip. The TeX keeps the printed n; the STRUCTURE comment (row 1, col 2) repeats it."),
    M(360, "diagram, row 2 column 2",
      "H^1(U,H^{2m-1}(X,Q_l(m)) : one closing parenthesis missing",
      "H^1(U,H^{2m-1}(X,\\mathbb{Q}_\\ell(m)) \\arrow[r", "high",
      "H^1(U,H^{2m-1}(X,\\mathbb{Q}_\\ell(m))) \\arrow[r",
      "The TeX keeps it; its STRUCTURE comment records the missing parenthesis."),
    M(360, "display 'u_0(R(t_1) - R(t_2)) = 0 dans H^1(U,R^{2n-1}rho_{U*}Q_l(n)) ,'",
      "R^{2n-1} ... Q_l(n)",
      "H^1(U,R^{2n-1}\\rho_{U*}\\mathbb{Q}_\\ell(n))", "medium",
      "H^1(U,R^{2m-1}\\rho_{U*}\\mathbb{Q}_\\ell(m))",
      "u_0 is defined (display above and diagram) with target H^1(U,R^{2m-1}rho_{U*}Q_l(m)). Same n-for-m slip. "
      "The TeX keeps the printed reading."),
    M(360, "'qui est conséquence de (4.3.12), grâce à 1.7.'",
      "(4.3.12)",
      "conséquence de (4.3.12)", "high", "conséquence de (4.4.12)",
      "4.3 has no numbered formulas; the statement used is (4 4.12) on p. 358 (the homomorphism (4.4.11) is zero), "
      "with Proposition 1.7. The TeX keeps the printed number."),
]

PRETTY = [("eta-bar", "η̄"), ("Q_l", "Q_ℓ"), ("rho_{", "ρ_{"), ("-->", "⟶"), ("XxU", "X×U"),
          (" x ", " × "), (" o P", " ∘ P")]
for f in F:
    for key in ("where", "scan", "note"):
        s = f[key]
        for a, b in PRETTY:
            s = s.replace(a, b)
        f[key] = s

ok = True
for f in F:
    txt = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = txt.count(f["tex"])
    if n != 1:
        ok = False
        print("TEX COUNT", n, f["page"], repr(f["tex"]))
    if f["fix"] is not None:
        m = txt.count(f["fix"]["old"])
        if m != 1:
            ok = False
            print("FIX OLD COUNT", m, f["page"], repr(f["fix"]["old"]))
print("all tex snippets unique:", ok)
if "--write" in sys.argv and ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("wrote", OUT, len(F))
print(sorted(Counter((f["page"], f["kind"]) for f in F).items()))
