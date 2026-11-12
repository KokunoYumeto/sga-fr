import json, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II'
F = []
def m(page, where, scan, tex, corrected, conf, note):
    F.append({"page": page, "where": where, "scan": scan, "tex": tex,
              "kind": "misprint_in_print", "confidence": conf, "fix": None,
              "corrected": corrected, "note": note})

m(331, "Proposition 2.1, first line: 'une variété projective lisse purement de dimension paire 2n'",
  "purement de dimension paire 2n ('paire' underlined, '2n' not)",
  r"\underline{une variété projective lisse purement de dimension paire} $2n$",
  r"\underline{une variété projective lisse purement de dimension impaire} $2n+1$",
  "medium",
  "Authorial slip rather than a typing error; the TeX keeps the printed reading. The statement needs hyperplane sections H_s of "
  "dimension 2n (Ev(H_s) ⊂ H^{2n}(H_s, ℚ_ℓ); reflections x ↦ x − (−1)^n(x δ)δ on p. 332), so dim X = 2n+1, as in Théorème 1.4 "
  "(p. 330: 'purement de dimension 2n + 1', whose irreducibility statement is announced there to be extended in n° 2). "
  "Remarque 2.2 then extends the result to 'X de dimension paire'. The editor may prefer a note to a silent correction.")

m(332, "first paragraph: 'Son image dans GL(H^n(H_s, Q_ℓ)) est donc (topologiquement) engendrée'",
  "GL(H^n(H_s, ℚ_ℓ)): superscript n only (checked at 4x)",
  r"$\mathrm{GL}(H^n(H_s, \mathbb{Q}_\ell))$",
  r"$\mathrm{GL}(H^{2n}(H_s, \mathbb{Q}_\ell))$",
  "medium",
  "Wrong index: the monodromy acts on H^{2n}(H_s, ℚ_ℓ), the group of Proposition 2.1 and of the next sentence. "
  "The TeX keeps the printed reading.")

m(332, "first paragraph: 'engendré par les cycles évanescents et leur conjugués: Ev(H_s, Q_ℓ)'",
  "leur conjugués:",
  "leur conjugués:",
  "leurs conjugués:",
  "medium",
  "Agreement slip: the same paragraph prints 'et leurs conjugués', as does Remarque 3.5. The TeX keeps the printed reading.")

m(332, "first paragraph, last words: 'est engendré par les cycles évanescents et leur conjugués.'",
  "leur conjugués.",
  "leur conjugués.",
  "leurs conjugués.",
  "medium",
  "Agreement slip, as above. The TeX keeps the printed reading.")

m(332, "paragraph 'Soit V ⊂ Ev(H_s, Q_ℓ)': 'Puisque v - (-1)^m(v δ)δ ∈ V'",
  "(-1)^m (checked at 3x)",
  r"(-1)^m(v\ \delta)",
  r"(-1)^n(v\ \delta)",
  "high",
  "The reflection is x ↦ x − (−1)^n(x δ)δ, printed with n in the first paragraph of the page; no m is defined in this proof. "
  "The TeX keeps the printed m.")

m(332, "3.1, last sentence: 'Les résultats du présent exposé ne servirons plus'",
  "servirons (checked at 1.3x)",
  "servirons",
  "serviront",
  "high",
  "Conjugation slip (subject 'Les résultats'). The TeX keeps the printed reading.")

m(332, "3.1, last sentence: 'dans la suite de séminaire'",
  "la suite de / séminaire (across the line end)",
  "la suite de séminaire",
  "la suite du séminaire",
  "medium",
  "'de' for 'du'. The TeX keeps the printed reading.")

m(333, "3.2, last sentence: '1.3 est donc vrai en caractérisitque 0'",
  "caractérisitque (checked at 1.8x)",
  "caractérisitque",
  "caractéristique",
  "high",
  "Transposed letters. The TeX keeps the printed reading.")

m(333, "Proposition 3.3 (b): 'Les cycles évanescents et leur conjugués sont dans'",
  "leur conjugués",
  "et leur conjugués sont dans",
  "et leurs conjugués sont dans",
  "medium",
  "Agreement slip, as on p. 332. The TeX keeps the printed reading.")

m(333, "Proposition 3.3 (b): 'ils y forment un système de racine irréductible'",
  "système de racine irréductible (checked at 2x)",
  "système de racine irréductible",
  "système de racines irréductible",
  "medium",
  "Item (c) of the same proposition and p. 334 print 'système de racines'. The TeX keeps the printed reading.")

m(334, "first paragraph: 'les réflexions associées aux cycles évanescents δ et leur conjugués (XVIII 6.6.1 et n° 2)'",
  "leur conjugués",
  r"$\delta$ et leur conjugués (XVIII",
  r"$\delta$ et leurs conjugués (XVIII",
  "medium",
  "Agreement slip, as on p. 332. The TeX keeps the printed reading.")

m(334, "first paragraph: 'Les δ et leur conjugués forment donc un système de racines'",
  "leur conjugués",
  r"Les $\delta$ et leur conjugués forment",
  r"Les $\delta$ et leurs conjugués forment",
  "medium",
  "Agreement slip, as on p. 332. The TeX keeps the printed reading.")

m(335, "Remarque 3.5: 'Si les conditions équivalentes de 3.3 sont vérifiées'",
  "de 3.3 (checked at 1.6x)",
  "conditions équivalentes de 3.3",
  "conditions équivalentes de 3.4",
  "medium",
  "Wrong reference: the equivalent conditions (i), (ii) are those of Proposition 3.4; the following 'comme en 3.3' (the argument "
  "of the proof of 3.3) is correct. The TeX keeps the printed reading.")

m(335, "section 4, first paragraph: '(on plutôt Q_ℓ, ce qui revient au même)'",
  "(on plutôt (checked at 2x)",
  "(on plutôt",
  "(ou plutôt",
  "high",
  "'on' for 'ou'. The TeX keeps the printed reading.")

out = RUN + r'\findings_331_335_recheck.json'
with open(out, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
print('wrote', out, len(F))
