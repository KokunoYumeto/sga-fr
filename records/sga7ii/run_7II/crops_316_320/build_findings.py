import json, sys, os
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II'
bdir = os.path.join(base, 'b316_320')
out = os.path.join(base, 'findings_316_320_recheck.json')

F = []
def add(page, where, scan, tex, conf, corrected, note, fix=None, kind='misprint_in_print'):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---- page 316
add(316, "par. 'Pour prouver ceci', second line: k(η) ⊂ K ⊂ K(η̄)",
    "k(η) ⊂ K ⊂ K(η̄): capital K before (η̄), the same glyph as the K before it (checked at 2.5x)",
    r"K \subset K(\overline{\eta})", "medium",
    r"K \subset k(\overline{\eta})",
    "No K(η̄) is defined; the field containing every finite Galois K over k(η) is k(η̄), the residue field of the geometric point η̄ (cf. π_1(η, η̄) = Gal(.../k(η)) at the foot of the page). The TeX keeps the printed capital.")
add(316, "par. 'est un revêtement étale', after 'd'où on déduit une action de'",
    "π_1^mod(D_η̄ - D_η ∩ Z, ā): bar over the first η only (checked at 2.5x)",
    r"(D_{\overline{\eta}} - D_{\eta} \cap Z, \overline{a})$ sur", "medium",
    r"(D_{\eta} - D_{\eta} \cap Z, \overline{a})$ sur",
    "The acting group is that of D_η − D_η∩Z, of which D_K − D_K∩Z is a tame covering (same sentence); the next paragraph prints π_1^mod(D_η − D_η∩Z, ā). The TeX keeps the printed bar.")
add(316, "'Nous prenons K suffisament grand'",
    "suffisament (one m; checked at 2x)",
    "suffisament", "high",
    "suffisamment",
    "Spelling slip of the typescript. The TeX keeps the printed reading.")
add(316, "last display: π_1^mod(D_η - D_η ∩ Z, ā) → π_1(η, η̄) = Gal(/k(η)  ,",
    "Gal(/k(η)   , : nothing between 'Gal(' and '/', and only one closing parenthesis (checked at 2.5x)",
    r"\mathrm{Gal}(/k(\eta) \quad ,", "medium",
    r"\mathrm{Gal}(k(\overline{\eta})/k(\eta)) \quad ,",
    "Two slips: the closing parenthesis of Gal( is missing (p. 317 prints Gal(/k(η)) with both), and the upper field is left out, as in both occurrences on p. 317. The parenthesis is certain; the field k(η̄) is the likely reading (k(η) ⊂ K ⊂ k(η̄) above) but is printed nowhere. The TeX keeps the printed reading.")

# ---- page 317
add(317, "first line, 'et l'action de Gal(/k(η)) sur ...'",
    "Gal(/k(η)): nothing between 'Gal(' and '/' (checked at 2x)",
    r"l'action de $\mathrm{Gal}(/k(\eta))$", "medium",
    r"l'action de $\mathrm{Gal}(k(\overline{\eta})/k(\eta))$",
    "The upper field of the Galois group is left out, as on p. 316 and two lines below; k(η̄) is the likely reading. The TeX keeps the printed reading.")
add(317, "first line, 'sur K_K ∩ Z est celle qui est compatible'",
    "K_K ∩ Z (capital K with subscript K; checked at 2x)",
    r"$K_K \cap Z$", "high",
    r"$D_K \cap Z$",
    "D_K ∩ Z is meant (p. 316 and the display just below: D_K ∩ Z ↪ ℙ^r_k ×_k K). The TeX keeps the printed reading.")
add(317, "'où Gal(/k(η)) n'agit sur ℙ^r_k ×_k K que via le deuxième facteur'",
    "Gal(/k(η)): nothing between 'Gal(' and '/' (checked at 2.5x)",
    r"où $\mathrm{Gal}(/k(\eta))$", "medium",
    r"où $\mathrm{Gal}(k(\overline{\eta})/k(\eta))$",
    "Same omission of the upper field as in the first line. The TeX keeps the printed reading.")
add(317, "end of Fait 6.1.8: '(en tant que polynôme en T à coefficients dans k(X_1,...,X_r).'",
    "k(X_1,...,X_r). : the parenthesis opened before 'en tant que' is never closed (checked at 2.5x)",
    r"$k(X_1,\ldots,X_r)$.", "medium",
    r"$k(X_1,\ldots,X_r)$).",
    "One closing parenthesis is missing in the print. The TeX keeps the printed reading.")

# ---- page 318
add(318, "Corollaire 6.1.10, second line: 'sur un corps k algébriquement clos k.'",
    "sur un corps k algébriquement clos k. (k typed twice; checked at 2x)",
    r"\underline{algébriquement clos} $k$.", "medium",
    r"\underline{algébriquement clos}.",
    "One of the two k is superfluous (the exposé writes both 'sur un corps k algébriquement clos', p. 267, and 'sur le corps algébriquement clos k', 6.2); dropping the second k is the smallest change. The TeX keeps the printed reading.")
add(318, "Corollaire 6.1.10: 'Supposons que n = dim X soit pair, ou que card(k) ≠ 2.'",
    "card(k) ≠ 2 (checked at 2x)",
    r"\mathrm{card}(k) \neq 2", "high",
    r"\mathrm{car}(k) \neq 2",
    "The characteristic is meant: k is algebraically closed, so card(k) ≠ 2 would be empty, and the same hypothesis reads car(k) ≠ 2 in 6.3.2 and 6.4. The TeX keeps the printed reading.")
add(318, "Démonstration, first line: 'Si dim (X̌) ≤ r-2, alor D ∩ X̌ est vide'",
    "alor (checked at 2x)",
    r"alor $D", "high",
    r"alors $D",
    "Typing slip. The TeX keeps the printed reading.")
add(318, "Démonstration: 'Le fait que l'action de π_1 sur H^{n-1}(X_η̄, ℚ_ℓ) soit modérée a été vue'",
    "a été vue",
    "a été vue", "medium",
    "a été vu",
    "The subject is 'Le fait', so the participle is masculine; 'vue' agrees with 'l'action' by attraction. The TeX keeps the printed reading.")

# ---- page 319
add(319, "(6.3.2) (v): '(où U est un ouvert non vide D au-dessus duquel ρ soit lisse)'",
    "est un ouvert non vide D (no 'de'; checked at 1.5x)",
    r"\underline{est un ouvert non vide} $D$", "medium",
    r"\underline{est un ouvert non vide de} $D$",
    "The word 'de' is left out in the print. The TeX keeps the printed reading.")

# ---- page 320
add(320, "Démonstration, second paragraph: '(ii) ⟺ (iii) par 6.1.6'",
    "(ii) ⟺ (iii) par 6.1.6 (checked at 1.5x)",
    "(iii) par 6.1.6", "medium",
    "(iii) par 6.1.10",
    "Wrong reference: (6.1.6) is the surjectivity of π_1(D_η̄ − D_η̄∩Z, ā) → π_1(ℙ^r − Z, ā) in the proof of 6.1.1 (p. 315). The equivalence of (ii) and (iii) is Corollaire 6.1.10 (if the representation is non-trivial, every inertia group acts non-trivially). The TeX keeps the printed reading.")
add(320, "Remarque 6.3.4: 'le système local sur ℙ^r - X formé des H^{n-1}(X ∩ H_s, Q_ℓ)'",
    "ℙ^r - X with no check over X (nothing above the X at 4x)",
    r"$\mathbb{P}^r - X$", "low",
    r"$\mathbb{P}^r - \check{X}$",
    "The local system of the H^{n-1}(X ∩ H_s) lives on the complement of the dual variety X̌ in the (dual) ℙ^r, which the exposé also writes ℙ^r ('X̌ est une hypersurface dans ℙ^r', p. 318); the handwritten check is missing. The TeX keeps the printed reading.")
add(320, "Remarque 6.3.4: 'H^{n-1}(X ∩ H_s, Q_ℓ)'",
    "H^{n-1}(X ∩ H_s, Q_ℓ): a plain typewriter Q (open bowl, no inner stroke), unlike the double-struck ℚ of the display on this page (compared side by side at 6x)",
    r"H_s, Q_\ell)", "medium",
    r"H_s, \mathbb{Q}_\ell)",
    "Typeface slip: the coefficients are ℚ_ℓ as everywhere else in §6. The TeX keeps the printed plain Q.")
add(320, "Remarque 6.3.4, last line: 'et de la surjectivité (6.1.2).'",
    "surjectivité (6.1.2)",
    "surjectivité (6.1.2)", "medium",
    "surjectivité (6.1.1)",
    "Wrong reference: the surjectivity of π_1^mod(D_o − D_o∩Z, ā) → π_1^mod(ℙ^r − Z, ā) is 6.1.1 (p. 313; p. 325 cites '6.1.1, qui donne la surjectivité'); 6.1.2 is the conjugacy of the inertia homomorphisms. The TeX keeps the printed reading.")

# ---- checks
ok = True
for d in F:
    p = d['page']
    with open(os.path.join(bdir, f'page_{p}.tex'), encoding='utf-8', newline='') as fh:
        txt = fh.read()
    n = txt.count(d['tex'])
    if n != 1:
        ok = False
        print('TEX NOT UNIQUE', p, n, d['tex'])
    if d['fix'] is not None:
        m = txt.count(d['fix']['old'])
        if m != 1:
            ok = False
            print('OLD NOT UNIQUE', p, m, d['fix']['old'])
print('all unique' if ok else 'PROBLEMS')
with open(out, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
c = Counter((d['page'], d['kind'] == 'misprint_in_print') for d in F)
for p in range(316, 321):
    print(p, 'normal', c[(p, False)], 'misprint', c[(p, True)])
print(len(F))
