import json

OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_116_120.json"
DIR = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b116_120"

F = []

F.append({
    "page": 116,
    "where": "title of Exposé XIV, 'Comparaison avec la théorie transcendante'",
    "scan": "Comparaison avec la théorie transcendante, underlined twice (two parallel rules); 'Exposé XIV', 'par P. Deligne' and 'Sommaire' have a single underline",
    "tex": r"\underline{Comparaison avec la théorie transcendante}",
    "kind": "underline",
    "confidence": "high",
    "fix": {"old": r"\underline{Comparaison avec la théorie transcendante}",
            "new": r"\underline{\underline{Comparaison avec la théorie transcendante}}"},
    "note": "Same encoding as the double-underlined titles of the earlier exposés (e.g. Exposé XIII, p. 82; QUADRIQUES, p. 62).",
})

F.append({
    "page": 117,
    "where": "1.1.3, first sentence: 'Les π_1(X, x) pour x variable sont les fibre d'un faisceau en groupes'",
    "scan": "sont les fibre d'un faisceau (no s on 'fibre'; checked at 2.5x)",
    "tex": "sont les fibre d'un faisceau",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "sont les fibres d'un faisceau",
    "note": "Agreement slip (plural article, singular noun). The TeX keeps the printed reading.",
})

F.append({
    "page": 117,
    "where": "1.1, first paragraph: 'des ambiguités de signes risquent d'apparaître'",
    "scan": "ambiguités: a plain dotted i, no diaeresis (checked at 4x)",
    "tex": "ambiguités",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "ambiguïtés",
    "note": "Accent slip of the typescript (no tréma on the i). The TeX keeps the printed reading.",
})

F.append({
    "page": 118,
    "where": "1.1.6: 'pour le disque standard, O = O et t ∈ D*'",
    "scan": "O = 0: the base point O of the standard disc is the complex number 0 (both glyphs 17-18 px wide)",
    "tex": "$O = O$",
    "kind": "symbol",
    "confidence": "medium",
    "fix": {"old": "$O = O$", "new": "$O = 0$"},
    "note": "In this typeface the capital O and the digit zero have the same width (17-18 px: the digit 0 of '[0, 1]' on p. 117, the letter O of 'On pose' on p. 119, both glyphs of f(0) = 0 on p. 119), so the glyph is read by its meaning, as on p. 24. 'O = O' says nothing; the sentence identifies the point O with the origin 0 of C. The TeX writes the digit elsewhere ([0, 1], H^0, a(0)).",
})

F.append({
    "page": 118,
    "where": "1.1.7, first sentence: 'Soit z : D → C une uniformisante ((dz)_o ≠ O)'",
    "scan": "((dz)_o ≠ 0): the differential of z at O is non-zero (same O/0 glyph, 17 px wide)",
    "tex": r"$((dz)_{o} \neq O)$",
    "kind": "symbol",
    "confidence": "medium",
    "fix": {"old": r"\neq O)", "new": r"\neq 0)"},
    "note": "Read by its meaning, as 'O = 0' in 1.1.6: (dz)_o is a linear form, and the condition on a uniformizing parameter is (dz)_o ≠ 0.",
})

F.append({
    "page": 118,
    "where": "1.1.7, second sentence: 'Soit D̃* un revêtement universel de D'",
    "scan": "un revêtement universel de D . (no asterisk after D; checked at 2.5x)",
    "tex": "un revêtement universel de $D$ .",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": r"un revêtement universel de $D^{*}$",
    "note": "D is a disc, hence simply connected, and log z (z vanishes at O) lives on a universal covering of the punctured disc: the notation D̃* and 1.1.9, 1.1.10 ('un revêtement universel de D*') say so. The TeX keeps the printed reading.",
})

F.append({
    "page": 119,
    "where": "1.1.8, second paragraph: 'soient T l'espace tangent à D en O, et T* = T-{O}'",
    "scan": "T* = T-{0}: the tangent space minus its origin (same O/0 glyph)",
    "tex": r"$T^{*} = T-\{O\}$",
    "kind": "symbol",
    "confidence": "low",
    "fix": {"old": r"$T^{*} = T-\{O\}$", "new": r"$T^{*} = T-\{0\}$"},
    "note": "Read by its meaning: T is a vector space, whose origin is 0, and 1.1.6 separates the point O from the number 0 ('O = 0'). The glyph alone cannot exclude a letter O for the origin of T. Apply together with f(O) = 0 in the next sentence, or neither.",
})

F.append({
    "page": 119,
    "where": "1.1.8, second paragraph: 'f : D' ↪ T avec f(O) = O et (df)_o = Id'",
    "scan": "f(O) = 0: f sends the point O of D' to the origin of T (same O/0 glyph)",
    "tex": "$f(O) = O$",
    "kind": "symbol",
    "confidence": "low",
    "fix": {"old": "$f(O) = O$", "new": "$f(O) = 0$"},
    "note": "Read by its meaning, as T* = T-{0} just before: the argument is the point O of D', the value the origin of the tangent space T. Apply together with the T* fix, or neither.",
})

F.append({
    "page": 119,
    "where": "1.1.8, 'est une équivalence [f] de la catégorie des faisceaux localement constant sur T*'",
    "scan": "des faisceaux localement constant sur T* (no s)",
    "tex": r"des faisceaux localement constant sur $T^{*}$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"des faisceaux localement constants sur $T^{*}$",
    "note": "Agreement slip; the end of the paragraph prints 'faisceaux localement constants sur T*'. The TeX keeps the printed reading.",
})

F.append({
    "page": 119,
    "where": "1.1.8, same sentence: 'avec celle des faisceaux localement constant sur D*. A isomorphisme canonique près'",
    "scan": "avec celle des faisceaux localement constant sur D* (no s)",
    "tex": r"des faisceaux localement constant sur $D^{*}$ . A isomorphisme",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"des faisceaux localement constants sur $D^{*}$",
    "note": "Same agreement slip as in the first half of the sentence. The TeX keeps the printed reading.",
})

F.append({
    "page": 120,
    "where": "1.1.9 c): 'les p^{-1}(U), pour U voisinage de O dans D, formant un système fondamental de voisinages'",
    "scan": "formant un système fondamental (checked at 2.5x)",
    "tex": "formant un système fondamental",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "forment un système fondamental",
    "note": "The clause after 'de sorte que' (end of p. 119) needs a finite verb, like a) 'est ouvert' and b) 'prolonge'. The TeX keeps the printed reading.",
})

# validation: every fix old occurs exactly once in its page file
ok = True
for f in F:
    if f["fix"] is not None:
        with open(rf"{DIR}\page_{f['page']}.tex", encoding="utf-8", newline="") as fh:
            src = fh.read()
        n = src.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", f["page"], repr(f["fix"]["old"]), n)
        if "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
            print("TOUCHES MARKER", f["page"])
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
    else:
        assert "corrected" not in f

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in (116, 117, 118, 119, 120):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
print("ALL OLD UNIQUE" if ok else "CHECK FAILED")
