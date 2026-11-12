import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(RUN, "b336_340")
OUT = os.path.join(RUN, "findings_336_340_recheck.json")

KEEP = "The TeX keeps the printed reading."

findings = [
    {
        "page": 336,
        "where": "second paragraph, 'soit α un difféomorphisme orienté de ℓ - S vers ℙ¹(ℂ)'",
        "scan": "un difféomorphisme orienté de ℓ - S vers ℙ¹(ℂ) envoyant 0 sur 0 , ∞ sur ∞ et S dans la circonférence de rayon un",
        "tex": r"de $\ell - S$ vers $\mathbb{P}^1(\mathbb{C})$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"de $\ell$ vers $\mathbb{P}^1(\mathbb{C})$",
        "note": "α sends S into the unit circle, and αf makes X - T(A)^o a singular fibration over all of ℙ¹(ℂ) with singular fibres over α(S), so α is defined on ℓ; the non-compact ℓ - S has no diffeomorphism onto ℙ¹(ℂ). The 'ℓ - S' repeats the 'dans ℓ - S' of the line above. " + KEEP,
    },
    {
        "page": 336,
        "where": "third paragraph, 'dans la situation étudié en XIV 3.2.'",
        "scan": "dans la situation étudié en XIV 3.2.",
        "tex": "la situation étudié en XIV 3.2.",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "la situation étudiée en XIV 3.2.",
        "note": "The participle should agree with the feminine 'situation'. " + KEEP,
    },
    {
        "page": 337,
        "where": "4.3, 'en attachant des n+1-disque le long de sphères'",
        "scan": "des n+1-disque le long de sphères",
        "tex": r"des $n+1$-disque le long",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"des $n+1$-disques le long",
        "note": "The plural ending is missing after 'des' (one disc per vanishing cycle). " + KEEP,
    },
    {
        "page": 337,
        "where": "diagram (4.3.1), label of the diagonal arrow H^n(X) → H^{n+2}(X)",
        "scan": "ηΛ : the product sign is the typed capital Lambda (18 x 20 px, against 21 px for the capitals H and X of H^n(X) in the same diagram; thin left and heavier right stroke, like the typed Δ on this page), not a small wedge",
        "tex": r'"{\eta\wedge}"' + "'",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": r"{\eta\wedge}", "new": r"{\eta\Lambda}"},
        "corrected": r"{\eta\wedge}",
        "note": "The cup product with η is typed with the capital Λ, as on pp. 272 and 276-277 [coordinator ruling there: the typescript types the cup product as a capital Lambda; diplomatic only, the corrected layer keeps the wedge]. The STRUCTURE comment under the diagram names the label $\\eta\\wedge$ (its meaning); the 'old' string does not touch the comment.",
    },
    {
        "page": 338,
        "where": "'Puisque sur H^{2n}(V) la forme d'intersection est unimodulaire, et que η^{2n} n'est pas le multiple by (b > 1)'",
        "scan": "et que η^{2n} n'est pas le multiple by (b > 1)",
        "tex": r"et que $\eta^{2n}$ n'est pas",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"et que $\eta^n$ n'est pas",
        "note": "The argument needs η^n ∈ H^{2n}(V) to be indivisible in the unimodular lattice, so that its orthogonal Ev(V) has discriminant (η^n, η^n) = Π a_i, the display that follows; η^{2n} = (Π a_i)·[point] in H^{4n}(V) is divisible. " + KEEP,
    },
    {
        "page": 339,
        "where": "Proposition 5.2 (i)",
        "scan": "Pour V uhe quadrique de dimension paire (clear ascender on the h)",
        "tex": r"\underline{uhe quadrique de dimension paire}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\underline{une quadrique de dimension paire}",
        "note": "Typing error for 'une'. " + KEEP,
    },
    {
        "page": 339,
        "where": "5.3, 'est aussi un système de racine, ayant les mêmes caractéristiques'",
        "scan": "est aussi un système de racine, ayant",
        "tex": "un système de racine,",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "un système de racines,",
        "note": "The standard term, printed on p. 338 as 'le système de racines'. " + KEEP,
    },
    {
        "page": 339,
        "where": "5.3, 'est le groupe de Weil de R'",
        "scan": "est le groupe de Weil de R",
        "tex": "le groupe de Weil de",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "le groupe de Weyl de",
        "note": "The Weyl group of the root system R. " + KEEP,
    },
    {
        "page": 339,
        "where": "5.4, 'le résultat 4.2 (ii) est bien connu [1]'",
        "scan": "le résultat 4.2 (ii) est bien connu",
        "tex": "le résultat 4.2 (ii)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "le résultat 5.2 (ii)",
        "note": "Wrong reference number: the cubic surface (type E_6, the 27 lines of [1]) is Proposition 5.2 (ii); Théorème 4.2 has no parts. " + KEEP,
    },
    {
        "page": 339,
        "where": "5.4, 'pour les petites valeurs de n , 4.2 (iii) était connu'",
        "scan": "4.2 (iii) était connu",
        "tex": "4.2 (iii) était connu",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "5.2 (iii) était connu",
        "note": "Wrong reference number: the intersection of two quadrics is Proposition 5.2 (iii). " + KEEP,
    },
    {
        "page": 339,
        "where": "5.4, 'Il déduit 4.2 (iii) d'une étude'",
        "scan": "Il déduit 4.2 (iii) d'une étude",
        "tex": "Il déduit 4.2 (iii)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Il déduit 5.2 (iii)",
        "note": "The same wrong reference number as above. " + KEEP,
    },
]

ok = True
for f in findings:
    path = os.path.join(PAGES, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if "\r" in text:
        print("CR found in", path); ok = False
    if text.count(f["tex"]) < 1:
        print("tex snippet not found:", f["page"], repr(f["tex"])); ok = False
    if f["fix"] is not None:
        n = text.count(f["fix"]["old"])
        if n != 1:
            print("old occurs %d times:" % n, f["page"], repr(f["fix"]["old"])); ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("old touches a marker:", f["page"]); ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print("missing corrected:", f["page"]); ok = False

if not ok:
    sys.exit("checks failed; nothing written")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("written", OUT)
for p in range(336, 341):
    c = counts.get(p, [0, 0])
    print(p, "%d/%d" % (c[0], c[1]))
