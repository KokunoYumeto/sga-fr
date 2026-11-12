# -*- coding: utf-8 -*-
import json, sys

NL = chr(10)
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_241_245.json"

F = []

F.append({
    "page": 241,
    "where": "paragraph after (5.1.1): 'en coordon-/nés homogènes'",
    "scan": "coordon-/nés homogènes (line-end hyphen; the word printed is coordonnés)",
    "tex": "coordonnés",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "coordonnées",
    "note": "The feminine noun 'coordonnée' lacks its final e in the print (the same slip occurs on p. 234). The TeX keeps the printed reading.",
})

F.append({
    "page": 241,
    "where": "(5.1.3), last non-zero term",
    "scan": "0 → Ω^1_{P^r/k}| X → (O_X(-1))^{r+1} → O_P → 0 . : the subscript of the last O is the blackboard P (checked at 1.6x)",
    "tex": r"\underline{O}_{\mathbb{P}} \longrightarrow 0 \quad .",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"\underline{O}_X \longrightarrow 0 \quad .",
    "note": "(5.1.3) is (5.1.2) restricted to X, and the print writes the other two terms restricted (Ω^1_{P^r/k}|X and (O_X(-1))^{r+1}); the restriction of O_P to X is O_X. The TeX keeps the printed reading.",
})

F.append({
    "page": 242,
    "where": "paragraph after the display ∫_T z: 'La classe dans CH^1(T) d'un faisceau inversible L sur T sera noté également L'",
    "scan": "sera noté également (checked at 1x)",
    "tex": "sera noté également",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "sera notée également",
    "note": "Agreement slip: the subject is 'La classe', and the sentence continues 'quand elle se trouve sous le signe d'intégration'. The TeX keeps the printed reading.",
})

F.append({
    "page": 242,
    "where": "same sentence: 'quand aucun confusion n'est à craindre'",
    "scan": "aucun confusion (checked at 1x)",
    "tex": "aucun confusion",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "aucune confusion",
    "note": "Agreement slip ('confusion' is feminine). The TeX keeps the printed reading.",
})

F.append({
    "page": 243,
    "where": "paragraph after (5.2.2): 'nul si et seulement si dim X < r-1 (=dim P(N))'",
    "scan": "dim X < r-1 with no check over the X (checked at 1.6x; the checks over X̌ in the line above and in (5.2.2)-(5.2.4) are clearly visible)",
    "tex": r"$\dim X < r-1$",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"$\dim \check{X} < r-1$",
    "note": "deg(φ) for φ : P(N) → X̌ is zero exactly when φ is not generically finite, i.e. when dim X̌ < dim P(N) = r-1. The condition on dim X is not equivalent (a smooth non-linear curve in P^3 has dim X = 1 < 2 and a dual surface, so deg(φ) ≠ 0). Same slip as on p. 235. The TeX keeps the printed reading.",
})

F.append({
    "page": 243,
    "where": "paragraph before (5.2.5): '(resp. O_{P(O_X(1)^{r+1})} sur P(O_X(1)^{r+1}) )'",
    "scan": "O_{P(O_X(1)^{r+1})} with no (1) after it (checked at 1.2x), while ξ is O_{P(N)}(1) in the same sentence",
    "tex": r"\underline{O}_{\mathbb{P}(\underline{O}_X(1)^{r+1})}$ sur",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"\underline{O}_{\mathbb{P}(\underline{O}_X(1)^{r+1})}(1)$ sur",
    "note": "τ is the canonical invertible sheaf O(1) of P(O_X(1)^{r+1}), parallel to ξ = O_{P(N)}(1): (5.2.5) α^*(τ) = ξ and (5.2.6) τ = pr_1^*(H) ⊗ pr_2^*(η). Without (1) the sheaf would be the structure sheaf. The TeX keeps the printed reading.",
})

F.append({
    "page": 244,
    "where": "first line: 'D'autre part, moyenant l'identification'",
    "scan": "moyenant (one n; checked at 1x)",
    "tex": "moyenant",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "moyennant",
    "note": "Spelling slip of the typescript. The TeX keeps the printed reading.",
})

F.append({
    "page": 244,
    "where": "second formula numbered (5.2.6): 'ξ = α^*(τ) = π^*(H) ⊗ φ^*(η)'",
    "scan": "(5.2.6), the same number as the formula τ = pr_1^*(H) ⊗ pr_2^*(η) earlier on the page",
    "tex": r"\tag{5.2.6}" + NL + r"\xi = \alpha^*(\tau)",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"\tag{5.2.6'}" + NL + r"\xi = \alpha^*(\tau)",
    "note": "Duplicate formula number. The first (5.2.6) is the one cited in 'appliquant α^* aux deux membres de (5.2.6)'; (5.2.7) and (5.2.8) follow and 5.2.8 is cited by number, so no number is free. The corrected reading (5.2.6') is only a suggestion. The TeX keeps the printed reading.",
})

F.append({
    "page": 244,
    "where": "sentence after (5.2.8): 'Le deuxieme membre de 5.2.8'",
    "scan": "deuxieme (no grave accent; checked at 1.6x)",
    "tex": "deuxieme",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "deuxième",
    "note": "Missing accent; the typewriter has è (homogènes p. 241, homogène p. 245). The TeX keeps the printed reading.",
})

with open(OUT, "w", encoding="utf-8", newline=NL) as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write(NL)
print("wrote", len(F), "findings")
