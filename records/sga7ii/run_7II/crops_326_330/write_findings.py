import json, io

F = []
def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

add(326, "Démonstration, l. 2: the twisted module E",
    "tordu E = E^{n-1}(X_η̄, Q_ℓ(m). Soit ...  (one closing parenthesis only; checked at 1.6x)",
    r"$E = E^{n-1}(X_{\bar{\eta}},\mathbb{Q}_\ell(m)$",
    "misprint_in_print", "high", None,
    "The print omits the closing parenthesis of E^{n-1}( ... ). The TeX keeps the printed reading.",
    r"$E = E^{n-1}(X_{\bar{\eta}},\mathbb{Q}_\ell(m))$")

add(326, "Démonstration, l. 2: 'et soit χ un élément ≠ 0 de Ē'",
    "soit χ un élément ≠ 0 de Ē  (Greek chi, the same glyph as in 'engendré par χ'; checked at 1.6x)",
    r"soit $\chi$ un élément",
    "misprint_in_print", "medium", None,
    "The element is called x in every formula that follows (x.δ_i ≠ 0, σ_i(x) − x in (6.7.3), (6.7.4) and the display on p. 327); the typescript types χ for this x. The TeX keeps the printed χ.",
    r"soit $x$ un élément")

add(326, "Démonstration, l. 4: 'engendré par χ et ses conjugués sous π'",
    "engendré par χ et ses conjugués sous π  (checked at 2x)",
    r"engendré par $\chi$ et ses conjugués",
    "misprint_in_print", "medium", None,
    "Same element as in 'soit χ un élément', called x in the formulas. The TeX keeps the printed χ.",
    r"engendré par $x$ et ses conjugués")

add(326, "Démonstration, l. 6: 'Mais comme χ satisfait (LV)'",
    "Mais comme χ satisfait (LV)  (Greek chi; checked at 1.6x)",
    r"Mais comme $\chi$ satisfait (LV)",
    "misprint_in_print", "high", None,
    "(LV) is the hypothesis on the variety X (Corollaire 6.7: 'supposons que X satisfait à la condition (LV)'), and the clause that follows is that condition for X (cup-product form non-degenerate on H^{n-1}(X, Q_ℓ(m))). The TeX keeps the printed χ.",
    r"Mais comme $X$ satisfait (LV)")

add(327, "formula (6.7.4)",
    "σ_i^k(x) =  X + k σ_i(x.δ_i) δ_i  .  (capital X after '=', against the small x in (x) and (x.δ_i); checked at 1.6x)",
    r"\sigma_i^k(x) = \ \ X + k",
    "misprint_in_print", "high", None,
    "The capital X stands for the element x (σ_i^k(x) = x + ...). The TeX keeps the printed capital.",
    r"\sigma_i^k(x) = \ \ x + k")

add(327, "after (6.7.4): 'si et seulement il l'est sous un sous-groupe d'indice fini'",
    "si et seulement / il l'est sous un sous-groupe d'indice fini",
    r"si et seulement il l'est",
    "misprint_in_print", "medium", None,
    "The print drops the second 'si' of 'si et seulement si'. The TeX keeps the printed reading.",
    r"si et seulement s'il l'est")

add(327, "after (6.7.4): 'Donc un sous Q_ℓ-module M de E'",
    "Q_ℓ-module with a plain typed Q, without the stroke that the typescript's Q_ℓ has everywhere else on these pages (compared at 3x with Q_ℓ on p. 326)",
    r"sous $Q_\ell$-module",
    "misprint_in_print", "medium", None,
    "E = E^{n-1}(X_η̄, Q_ℓ(m)) is a Q_ℓ-vector space; the stroke of the double-struck Q is missing in the print. The TeX keeps the plain Q (the only plain Q_ℓ in the volume's TeX).",
    r"sous $\mathbb{Q}_\ell$-module")

add(327, "Bibliographie [3] (Lefschetz)",
    "Gauthiers-Villars, Paris 1924.",
    r"Gauthiers-Villars",
    "misprint_in_print", "high", None,
    "The publisher is Gauthier-Villars. The TeX keeps the printed spelling.",
    r"Gauthier-Villars")

add(327, "Bibliographie [3] (Lefschetz): title",
    "L'analyse situs et la Géométrie Algébrique,",
    r"L'analyse situs et la Géométrie Algébrique",
    "misprint_in_print", "low", None,
    "The book's title is 'L'analysis situs et la géométrie algébrique' (Gauthier-Villars, Paris, 1924). It may be the author's own French rendering rather than a typing slip; the TeX keeps the printed reading.",
    r"L'analysis situs et la Géométrie Algébrique")

add(327, "Bibliographie [4] (Lieberman): volume number",
    "Amer. J. Math, 15 (4) 1968 p.1165-1199.  (15 underlined; checked at 1.6x)",
    r"\underline{15} (4) 1968",
    "misprint_in_print", "medium", None,
    "D. Lieberman, Higher Picard varieties, is in Amer. J. Math. vol. 90, no. 4 (1968), 1165-1199. The print's volume number is wrong; the TeX keeps it.",
    r"\underline{90} (4) 1968")

add(329, "'Déduisons 1.2.1 de 1.3': the exceptional cases of 1.2",
    "pour lesquels Σ(d_i -1) ≤ 2  (letter d; checked at 1.5x)",
    r"$\Sigma(d_i -1) \leq 2$",
    "misprint_in_print", "high", None,
    "The multidegree is a = (a_i), d being the codimension: the exceptions (2), (3), (2, 2) of 1.2 are exactly the multidegrees with Σ(a_i − 1) ≤ 2, the negation of 1.3 (b) Σ(a_i − 1) > 2n for n = 1. The TeX keeps the printed d_i.",
    r"$\Sigma(a_i -1) \leq 2$")

add(330, "'Précisons le sens du mot générique', (a): 'la grassmanienne des droites'",
    "grassmanienne (one n after 'm'; checked at 2x)",
    r"grassmanienne",
    "misprint_in_print", "medium", None,
    "Spelling slip of the typescript for 'grassmannienne' (the volume prints both 'grassmannienne' and other slips such as 'grassmanniene'). The TeX keeps the printed spelling.",
    r"grassmannienne")

out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_326_330_recheck.json"
with io.open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
    f.write("\n")
print(len(F), "findings written")
