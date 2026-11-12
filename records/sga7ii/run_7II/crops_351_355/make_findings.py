import json, io
from collections import Counter

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
OUT = RUN + r"\findings_351_355_recheck.json"

F = []

# ---------------- page 351 ----------------
F.append({
 "page": 351,
 "where": "heading of Proposition 2.1, mark between 2 and 1",
 "scan": "Proposition 2.1, : the mark after the 2 is a heavy dot with a short spur on top and no comma tail (centroid 2 px above the baseline, 5 of its 43 pixels below it; the commas of the same line, after 'propre' and after the 1, put a third of their pixels below the baseline). Compared side by side with the commas of the page and the heavy full stops of '3.1.' on p. 352 (checked at 8x).",
 "tex": "\\underline{Proposition} 2,1,",
 "kind": "punctuation",
 "confidence": "low",
 "fix": {"old": "2,1,", "new": "2.1,"},
 "note": "At reading size the blob looks like a comma because it is as large as one (probably a full stop struck twice), but it has the shape and height of a full stop. If the coordinator reads it as a comma, drop this fix; the misprint entry below then applies to '2,1,' (corrected '2.1.')."
})
F.append({
 "page": 351,
 "where": "heading of Proposition 2.1, mark after the 1",
 "scan": "Proposition 2.1, : the mark after the 1 descends below the baseline like a comma (checked at 8x)",
 "tex": "2.1,",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "2.1.",
 "note": "Propositions 2.2 and 2.3 print '2.2.' and '2.3.'. The TeX keeps the printed comma; this tex is the text after the punctuation fix above (without that fix the TeX reads '2,1,', corrected '2.1.')."
})

# ---------------- page 352 ----------------
F.append({
 "page": 352,
 "where": "(3.1.2)",
 "scan": "un pinceau de Lefschetz d'hypersurfacesde degré d (no word space)",
 "tex": "d'hypersurfacesde degré $d$",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "d'hypersurfaces de degré $d$",
 "note": "Missing word space in the print. The TeX keeps the printed reading."
})
F.append({
 "page": 352,
 "where": "(3.1.6), last line",
 "scan": "agit de façon irréductible sur E^{2n-1}(X_η̄, ℚ_ℓ(i)) (exponent 2n-1, checked at 2x)",
 "tex": "E^{2n-1}(X_{\\bar{\\eta}},\\mathbb{Q}_{\\ell}(i))",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "E^{n-1}(X_{\\bar{\\eta}},\\mathbb{Q}_{\\ell}(i))",
 "note": "The vanishing cohomology is E^{n-1} (3.1.5); the proof of 3.2 (p. 353) cites 'l'irréductibilité (3.1.6) de E^{n-1}(X_η̄, ℚ_ℓ(i))'. The TeX keeps the printed reading."
})

# ---------------- page 353 ----------------
F.append({
 "page": 353,
 "where": "Démonstration, first sentence",
 "scan": "Supposons que l'image d'un tel homomorphisme (3.2.3) n'est pas contenu dans",
 "tex": "n'est pas contenu dans",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "n'est pas contenue dans",
 "note": "The participle agrees with 'l'image'. The TeX keeps the printed reading."
})
F.append({
 "page": 353,
 "where": "Démonstration, 'que son image dans E^{n-1}(...) = H^{n-1}(X_η̄, ...) H^{n-1}(X, Q_ℓ(i)) n'est pas nulle'",
 "scan": "= H^{n-1}(X_η̄, ℚ_ℓ(i)) H^{n-1}(X,Q_ℓ(i)): no quotient sign in the gap (nothing there at 5x), and the second Q is a plain typewriter Q without the stroke (this H^{n-1}(X,Q_ℓ(i)) is typed in a bolder face)",
 "tex": "H^{n-1}(X_{\\bar{\\eta}},\\mathbb{Q}_{\\ell}(i)) \\quad H^{n-1}(X,Q_{\\ell}(i))",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "H^{n-1}(X_{\\bar{\\eta}},\\mathbb{Q}_{\\ell}(i)) / H^{n-1}(X,\\mathbb{Q}_{\\ell}(i))",
 "note": "E^{n-1}, the orthogonal of m^*H^{n-1}(X) (3.1.5), is identified with the quotient of H^{n-1}(X_η̄) by the image of H^{n-1}(X); the slash is missing, and the plain Q is a typeface slip for ℚ. The TeX keeps both (the gap as \\quad, the plain Q)."
})
F.append({
 "page": 353,
 "where": "Démonstration, 'l'irréductibilité (3.1.6) de E^{n-1}(X_η̄, ℚ_ℓ(i) se récrit en disant'",
 "scan": "E^{n-1}(X_η̄,ℚ_ℓ(i) se récrit: one closing parenthesis only (checked at 2x)",
 "tex": "\\mathbb{Q}_{\\ell}(i)$ se récrit",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "\\mathbb{Q}_{\\ell}(i))$ se récrit",
 "note": "The closing parenthesis of E^{n-1}( is missing in the print. The TeX keeps the printed reading."
})
F.append({
 "page": 353,
 "where": "first display of the proof: H^{n-1}(X_η̄, Q_ℓ(i)) = m^*H^{n-1}(X, Q_ℓ(i)) + l'image de (3.2.3)",
 "scan": "both Q are plain typewriter Q without the stroke of the page's other ℚ_ℓ (compared at 2x with the display at the foot of the page); the ℓ are handwritten",
 "tex": "H^{n-1}(X_{\\bar{\\eta}},Q_{\\ell}(i)) = m^{*}H^{n-1}(X,Q_{\\ell}(i))",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "H^{n-1}(X_{\\bar{\\eta}},\\mathbb{Q}_{\\ell}(i)) = m^{*}H^{n-1}(X,\\mathbb{Q}_{\\ell}(i))",
 "note": "Typeface slip: the coefficients are ℚ_ℓ(i), as in the same equation at the end of the proof. The TeX keeps the plain Q."
})

# ---------------- page 354 ----------------
F.append({
 "page": 354,
 "where": "(3.3.3), after V_η̄",
 "scan": "V_η̄ ; H^{n-1}(X_η̄, ℚ_ℓ(i)): a semicolon; below the lower dot there is a comma tail to the lower left (checked at 5x; the colons of (3.3.1), (3.3.4) and of the other pages have nothing below the lower dot)",
 "tex": "V_{\\overline{\\eta}} : H^{n-1}",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": {"old": "V_{\\overline{\\eta}} : H^{n-1}", "new": "V_{\\overline{\\eta}} ; H^{n-1}"},
 "corrected": "V_{\\overline{\\eta}} : H^{n-1}",
 "note": "Typing slip (; for :, neighbouring keys on a French typewriter). The TeX silently corrects; the fix restores the printed semicolon."
})
F.append({
 "page": 354,
 "where": "(3.3.4), target of m^*",
 "scan": "H^{n-1}(X_η, ℚ_ℓ(i)) , : no bar over η (checked at 3x)",
 "tex": "H^{n-1}(X_{\\eta},\\mathbb{Q}_{\\ell}(i))",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "H^{n-1}(X_{\\overline{\\eta}},\\mathbb{Q}_{\\ell}(i))",
 "note": "m : X_η̄ → X ×_k k(η̄) (3.3.1), and V_η̄ (3.3.3) starts from H^{n-1}(X_η̄); the bar is missing. The TeX keeps the printed reading."
})
F.append({
 "page": 354,
 "where": "(3.4), first sentence",
 "scan": "est algébrique (cf. [4, 2.12 (ii)]. On conjecture: the parenthesis opened at '(cf.' is never closed (checked at 4x)",
 "tex": "(cf. [4, 2.12 (ii)].",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "(cf. [4, 2.12 (ii)]).",
 "note": "One closing parenthesis is missing in the print. The TeX keeps the printed reading."
})

# ---------------- page 355 ----------------
F.append({
 "page": 355,
 "where": "Théorème 4.1, 'de dimension paire n = 2m ≥ 4 Soit D'",
 "scan": "n = 2m ≥ 4    Soit D: no full stop (empty cells after the 4, checked at 2x)",
 "tex": "$n = 2m \\geq 4$ \\underline{Soit}",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "$n = 2m \\geq 4$. \\underline{Soit}",
 "note": "The full stop between the two sentences is missing. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "(4.1.2), 'vérifie (3.2.2), i e. (3.2)'",
 "scan": "i e. : the type cell between i and e is empty (checked at 8x); the full stop after e is very faint",
 "tex": "\\underline{i e.}",
 "kind": "misprint_in_print",
 "confidence": "low",
 "fix": None,
 "corrected": "\\underline{i.e.}",
 "note": "The point after i is missing; it may have been struck too lightly to print, since the point after e barely shows. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "(4.1.3), 'l'inclusion m^* : X_η̄ ↪ X ×_k k(η̄)'",
 "scan": "l'inclusion m^* : X_η̄ ↪ X ×_k k(η̄) (asterisk over the m, checked at 2x)",
 "tex": "\\underline{l'inclusion} $m^* :",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "\\underline{l'inclusion} $m :",
 "note": "The inclusion is m (3.1.4, 3.3.1); m^* is the map it induces on cohomology. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "after (4.1.3), 'est tel que sa restriction(en tant que cycle algébrique) à X_η̄'",
 "scan": "restriction(en tant que cycle algébrique): the parenthesis stands in the cell right after the n (the parenthetical is typed in afterwards)",
 "tex": "restriction(en",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "restriction (en",
 "note": "Missing word space in the print. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "4.2, 'de degré d > 2n D'autre part, on va prouver'",
 "scan": "d > 2n    D'autre part: no full stop (empty cells after 2n)",
 "tex": "$d > 2n$  D'autre part",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "$d > 2n$. D'autre part",
 "note": "The full stop ending the sentence is missing. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "4.2, 'la condition (4.1 2) pour un pinceau'",
 "scan": "(4.1 2): the cell between 1 and 2 is empty (checked at 5x)",
 "tex": "(4.1 2)",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "(4.1.2)",
 "note": "The second point of the reference number is missing. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "4.2, 'pour un pinceau \"général\"d'hypersurfaces de degré d > 2n (XXI 5.2 )'",
 "scan": "\"général\"d'hypersurfaces: the d stands in the cell right after the closing quote",
 "tex": "pour un pinceau ``général''d'",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "pour un pinceau ``général'' d'",
 "note": "Missing word space after the closing quote. The TeX keeps the printed reading."
})
F.append({
 "page": 355,
 "where": "4.2, last sentence, 'Donc un pinceau \"général\"d'hypersurfaces'",
 "scan": "\"général\"d'hypersurfaces: the d stands in the cell right after the closing quote",
 "tex": "Donc un pinceau ``général''d'",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "Donc un pinceau ``général'' d'",
 "note": "Missing word space after the closing quote, as two lines above. The TeX keeps the printed reading."
})

# ------------- checks -------------
pages = {}
for p in (351, 352, 353, 354, 355):
    with io.open(RUN + "\\b351_355\\page_%d.tex" % p, encoding="utf-8", newline="") as fh:
        pages[p] = fh.read()
    print(p, "CR count:", pages[p].count("\r"))

ok = True
for i, f in enumerate(F):
    t = pages[f["page"]]
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in f:
            ok = False
            print("missing key", k, i)
    if (f["kind"] == "misprint_in_print") != ("corrected" in f):
        ok = False
        print("corrected key mismatch", i)
    if f["fix"] is not None:
        old = f["fix"]["old"]
        c = t.count(old)
        if c != 1:
            ok = False
            print("FIX OLD NOT UNIQUE", i, f["page"], c, repr(old))
        if "%%%%%%%%%%" in old or "\n" in old:
            print("check old spans line/marker", i)
    c = t.count(f["tex"])
    if c != 1:
        print("tex count", i, f["page"], c, repr(f["tex"]))
    for s in [f["tex"], f.get("corrected") or ""] + ([f["fix"]["old"], f["fix"]["new"]] if f["fix"] else []):
        if any(ord(ch) < 32 for ch in s):
            ok = False
            print("control char", i, repr(s))

t351 = pages[351].replace(F[0]["fix"]["old"], F[0]["fix"]["new"], 1)
print("post-fix count of '2.1,' on 351:", t351.count("2.1,"))

if ok:
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", len(F))
    cnt = Counter()
    for f in F:
        cnt[(f["page"], f["kind"] == "misprint_in_print")] += 1
    print("; ".join("%d: %d/%d" % (p, cnt[(p, False)], cnt[(p, True)]) for p in (351, 352, 353, 354, 355)))
