import json
import os
import sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
FOLDER = os.path.join(RUN, "b081_085")
OUT = os.path.join(RUN, "findings_081_085.json")

findings = [
    {
        "page": 81,
        "where": "C., 'est nul pour n impair, envoyè ±δ sur ±2δ' pour n pair > 0'",
        "scan": "envoyè ± δ sur ± 2 δ' (grave accent: its head sits at the upper left and it runs down to the right, like the è of 'près' in the paragraph above; the acute of 'équation' and 'Vérification' on this page leans the other way; checked at 8x)",
        "tex": "envoyé",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": {"old": "envoyé", "new": "envoyè"},
        "corrected": "envoie",
        "note": "Typing error for the present tense 'envoie', parallel to 'est nul'. The TeX has 'envoyé', which is neither the printed nor the correct reading; the fix restores the printed reading, and the corrected layer needs 'envoie' rather than the TeX's 'envoyé'. The accent is small and partly lost, hence medium confidence for è against é."
    },
    {
        "page": 82,
        "where": "title of Exposé XIII, 'Le formalisme des cycles évanescents'",
        "scan": "Le formalisme des cycles évanescents, underlined twice (two parallel rules); 'Exposé XIII' and 'par P. Deligne' have a single underline (checked at 1.5x and 5x)",
        "tex": "\\underline{Le formalisme des cycles évanescents}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{Le formalisme des cycles évanescents}",
            "new": "\\underline{\\underline{Le formalisme des cycles évanescents}}"
        },
        "note": "Same encoding as the double-underlined titles of the earlier exposés (e.g. QUADRIQUES, p. 62)."
    },
    {
        "page": 83,
        "where": "(a), second sentence, 'En d'autre termes, Γ définit une trivialisation'",
        "scan": "En d'autre termes, (no s after autre; checked at 3x)",
        "tex": "En d'autre termes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "En d'autres termes",
        "note": "Spelling error of the print (the phrase is 'en d'autres termes'). The TeX keeps the printed reading."
    },
    {
        "page": 83,
        "where": "display defining the monodromy, left side '(φ * X)_o'",
        "scan": "(φ * X)_o: the typed asterisk stands raised at the top of the X, at the same height as in '(φ* X)_1' on the right and in 'φ*X' in the text above; only the spacing differs (checked at 2.5x)",
        "tex": "(\\varphi * X)_o",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "(\\varphi * X)_o", "new": "(\\varphi^* X)_o"},
        "note": "The TeX's plain * renders as a centred binary asterisk; the print has the same raised star (inverse image) as on the right side, which the TeX writes \\varphi^* X."
    },
    {
        "page": 84,
        "where": "first line, 'cône d'application de (S^1 → P^t)'",
        "scan": "(S^1 → P^t): capital P standing on the baseline with the height of the S (the small p's of 'application' on the same line descend below it), raised t; a short horizontal stroke runs from the foot of the bowl to below the t (checked at 10x)",
        "tex": "(S^1 \\to p^t)",
        "kind": "symbol",
        "confidence": "high",
        "fix": {"old": "(S^1 \\to p^t)", "new": "(S^1 \\to P^t)"},
        "note": "Capital against small letter. The abbreviation stands for 'point' (the mapping cone of S^1 → point is the disc D). The stroke beside the bowl is of unclear meaning and is not reproduced."
    },
    {
        "page": 84,
        "where": "Construction 0.1, γ), 'dans le faisceau des T-invariants de F_t'",
        "scan": "'dans le faisceau des' and 'invariants de' underlined, 'T-' not (checked at 4x)",
        "tex": "\\underline{dans le faisceau des $T$-invariants de}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{dans le faisceau des $T$-invariants de}",
            "new": "\\underline{dans le faisceau des} $T$-\\underline{invariants de}"
        },
        "note": "The typed underline breaks at the T and the hyphen, as at the other symbols of the Construction (F, X_o × D, T, π_1(D*,t)), which the TeX already leaves outside the underlines."
    },
    {
        "page": 84,
        "where": "'Pour les faisceau R^iΨ_*ℤ , on a'",
        "scan": "Pour les faisceau  R^iΨ_*ℤ  , on a (singular, no x)",
        "tex": "Pour les faisceau",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Pour les faisceaux",
        "note": "Agreement error of the print (plural article 'les'). The TeX keeps the printed reading."
    },
    {
        "page": 85,
        "where": "β), 'muni d'une action continue T du groupe d'intertie I'",
        "scan": "du groupe d'intertie (checked at 3x)",
        "tex": "du groupe d'intertie",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "du groupe d'inertie",
        "note": "Typing error for 'inertie' (the inertia group I). The TeX keeps the printed reading."
    },
]

ok = True
for f in findings:
    path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
    with open(path, "r", encoding="utf-8", newline="") as fh:
        text = fh.read()
    for key in ("fix",):
        fx = f.get(key)
        if fx:
            n = text.count(fx["old"])
            if n != 1:
                ok = False
                print("NOT UNIQUE", f["page"], repr(fx["old"]), n)
            if "%%%%%%%%%%" in fx["old"]:
                ok = False
                print("MARKER IN OLD", f["page"])
    # the tex field should also be present (for null fixes) to locate the misprint
    n = text.count(f["tex"])
    if n < 1:
        ok = False
        print("TEX NOT FOUND", f["page"], repr(f["tex"]))
    elif f.get("fix") is None and n != 1:
        print("TEX not unique (null fix)", f["page"], repr(f["tex"]), n)

if not ok:
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("written", OUT, len(findings))
