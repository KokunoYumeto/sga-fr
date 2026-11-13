"""build_findings.py: write run_6/findings_521_525.json and check every fix's old once in its page file."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b521_525"
OUT = RUN / "findings_521_525.json"
NL = "\n"


def fx(old, new):
    return {"old": old, "new": new}


F = []

# ---------------------------------------------------------------- p. 521
F.append({
    "page": 521,
    "where": "conventions of pp. 521-525: letters the print underlines",
    "scan": "underlined in the print (both scans): p. 521 the G, G', G'' of (1.1.7) and every F of the Démonstration ('Si F est un', f_*(cl.(F)), R^if_*(F), Supp(F)); p. 522 E ('Si E est un', cl˙(E), both E of (1.2.1)), the E_p and n_p of (1.2.4) and of the last line; p. 523 E and F of the bifunctor display and of 'où E est un ... et F un'; p. 524 the E of (1.3.5) and of 'où m ≥ i et E', L_1, ..., L_n and the E, L_1, L_n of the last display; p. 525 L_r (twice), L, R_X, F, F/O_X, F/L, the E of 'de E sur X', L_1, ..., L_n, the E and L_n of (1.3.7), the k of k(e). Plain in the print: the n of (1.3.5) and of 'de rang n > 0', the L_1 of (1.3.7), X, Z, D, D_e, x, x_p, P, e, u",
    "tex": "all plain",
    "kind": "underline",
    "confidence": "high",
    "fix": None,
    "note": r"Convention of the Exposé X transcription on these pages (no underlined letter; the underlined O written \mathcal O falls under the pending volume decision): not itemized; no blind script (the plain n and L_1 above). Three examples, in the form to use if the diplomatic layer reproduces the underline: p. 521 '\cl_\bullet(G)=\cl_\bullet(G')+\cl_\bullet(G'')' -> '\cl_\bullet(\underline{G})=\cl_\bullet(\underline{G}')+\cl_\bullet(\underline{G}'')'; p. 522 'de rang $n_p\in H^0(X,\mathbb Z)$' -> 'de rang $\underline{n}_p\in H^0(X,\mathbb Z)$'; p. 525 'constant $R_X$ des fonctions' -> 'constant $\underline{R}_X$ des fonctions'.",
})
F.append({
    "page": 521,
    "where": "statements of pp. 521-523: Proposition 1.1.8 (p. 521), Théorème 1.3.2 and Corollaire 1.3.3 (p. 523)",
    "scan": "underlined word group by word group (both scans): Prop. 1.1.8 'Soit', 'un morphisme propre de schémas localement noethériens et soit', 'le morphisme induit par', 'Alors', 'pour tout entier'; Th. 1.3.2 'Soit', 'un schéma noethérien', 'Pour tout', 'la loi de composition', 'induit par restriction une loi de composition'; Cor. 1.3.3 'Si', 'est un schéma noethérien de dimension', 'alors l'homomorphisme canonique', 'défini par', 'induit pour tout', 'un homomorphisme'; letters, formulas, displays, references and punctuation plain; the labels underline only the word",
    "tex": r"the statements in roman (no \emph, no \underline)",
    "kind": "underline",
    "confidence": "high",
    "fix": None,
    "note": r"Exposé X follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision): not itemized. The TeX adds no \emph on defined terms here, and pp. 521-525 have no category letter.",
})
F.append({
    "page": 521,
    "where": "'Alors l'assertion (1.1.3) pour tous les membres de (1.1.5) découle'",
    "scan": "'tous' underlined (both scans; crops_521_525/w521_top.png)",
    "tex": "no emphasis",
    "kind": "underline",
    "confidence": "high",
    "fix": fx("pour tous les membres", r"pour \emph{tous} les membres"),
    "note": r"\emph is the file's command for underlined words in running text (\emph{Démonstration :} on pp. 521 and 523).",
})
F.append({
    "page": 521,
    "where": "heading 1.2 (printed at the top of p. 522; in page_521.tex above the folio-522 marker)",
    "scan": "'1.2.' with a full stop (both scans)",
    "tex": r"\subsection*{1.2}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": fx(r"\subsection*{1.2}", r"\subsection*{1.2.}"),
    "note": r"The printed paragraph number ends with a full stop (as the applied heading fixes of Exposé VII, e.g. \subsection*{4.10.} on p. 464). The same line moves with the folio-522 marker (p. 522 marker entry).",
})

# ---------------------------------------------------------------- p. 522
F.append({
    "page": 522,
    "where": "start of page (folio-522 marker)",
    "scan": "p. 521 ends 'd'où l'assertion.' (the rest of the page blank); p. 522 begins with the heading '1.2. Soit maintenant X un schéma quelconque' (both scans; crops_521_525/wit_522_small.png)",
    "tex": r"page_521.tex ends '\subsection*{1.2}' above the folio-522 marker; page_522.tex begins 'Soit maintenant'",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": r"Page 522 really begins at the heading 1.2 (a heading at the top of a page, not moved by the 10 Nov script). Exact edit in main.tex, both layers (each string occurs once): replace '\subsection*{1.2}\n%%%%%%%%%%  scan idx 535  |  folio 522  %%%%%%%%%%\n' by '%%%%%%%%%%  scan idx 535  |  folio 522  %%%%%%%%%%\n\subsection*{1.2}\n' (write {1.2.} in both strings if the p. 521 heading fix is applied first).",
})
F.append({
    "page": 522,
    "where": "conventions of pp. 522-525: K and cl with a raised dot",
    "scan": "K˙ and cl˙ (a raised filled dot, distinct from the lower dot of K. and cl.) in every place: K˙(X), K˙(D) 12 times (p. 522 six, p. 523 four, pp. 524 and 525 one each), cl˙(E), cl˙(E_p), cl˙(L_r), ... 15 times (p. 522 four, p. 524 four, p. 525 seven); both scans (crops_521_525/c522_Kdot.png, c522_cldot.png, w522_Kdot.png, c524_sumdots.png, c525_137.png)",
    "tex": r"K^\circ (12 places) and \cl^\circ (15 places)",
    "kind": "symbol",
    "confidence": "high",
    "fix": None,
    "note": r"As for Exposés IV, VI and VII (the print's raised dot is K^{\bullet}): one script for Exposé X, both layers (main.tex has 55 K^\circ and 28 \cl^\circ from the Exposé X heading to Exposé XII; only pp. 522-525 checked here); not itemized. Three examples: p. 522 'le groupe $K^\circ(X)$ des classes' -> 'le groupe $K^{\bullet}(X)$ des classes'; p. 522 'on désignera par $\cl^\circ(E)$' -> 'on désignera par $\cl^{\bullet}(E)$'; p. 525 '\in K^\circ(D).' -> '\in K^{\bullet}(D).'.",
})
F.append({
    "page": 522,
    "where": "after (1.2.2): '(V 2.2). Rappelons que dans la λ-filtration'",
    "scan": "'(V 2.2). Rappelons ...' starts at the left margin, not indented: the paragraph goes on after the display (the paragraphs of these pages are indented: 'On sait que', 'Le théorème 1.3.2', 'Distinguons'); both scans (crops_521_525/wit_522_small.png)",
    "tex": r"a blank line between \end{equation} and '(V 2.2).' (a new paragraph)",
    "kind": "other",
    "confidence": "medium",
    "fix": fx(r"\end{equation}" + NL + NL + "(V 2.2).", r"\end{equation}" + NL + "(V 2.2)."),
    "note": "Spurious paragraph break: '(V 2.2).' is the reference that closes the definition by (1.2.1) and (1.2.2).",
})
F.append({
    "page": 522,
    "where": "(1.2.1): λ^k(cl˙(E)) = cl˙(Λ^k_O E)",
    "scan": "the exterior power is the typist's serifless capital Lambda, of capital height (the glyph GLOBAL_ISSUES 88 identified as the typist's capital Lambda); both scans (crops_521_525/c522_wedge.png)",
    "tex": r"\wedge_{\mathcal O}^kE",
    "kind": "symbol",
    "confidence": "low",
    "fix": fx(r"\wedge_{\mathcal O}^kE", r"\Lambda_{\mathcal O}^kE"),
    "note": r"Item 88 kept \Lambda for this glyph in Exposé V; Exposé X writes \wedge (4 in the exposé). The reading is the same either way: apply only if the volume follows item 88 here.",
})
F.append({
    "page": 522,
    "where": "'(donc le sous-groupe abelien, si X est connexe)'",
    "scan": "'abelien' without an accent (both scans; crops_521_525/c522_abelien.png, w522_abelien.png)",
    "tex": "abélien (silently corrected)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": fx("sous-groupe abélien", "sous-groupe abelien"),
    "corrected": "sous-groupe abélien",
    "note": "The current layer also reads 'abélien' (the corrected edition keeps it).",
})
F.append({
    "page": 522,
    "where": "heading 1.3 (printed at the top of p. 523; in page_522.tex above the folio-523 marker)",
    "scan": "'1.3.' with a full stop (both scans)",
    "tex": r"\subsection*{1.3}",
    "kind": "punctuation",
    "confidence": "high",
    "fix": fx(r"\subsection*{1.3}", r"\subsection*{1.3.}"),
    "note": "As the p. 521 entry for 1.2. The same line moves with the folio-523 marker (p. 523 marker entry).",
})

# ---------------------------------------------------------------- p. 523
F.append({
    "page": 523,
    "where": "start of page (folio-523 marker)",
    "scan": "p. 522 ends 'E_p étant un O_X-module localement libre de rang n_p ∈ H^0(X,Z) .' (the rest of the page blank); p. 523 begins with the heading '1.3. Rappelons (IV2.10) que le bifoncteur' (both scans)",
    "tex": r"page_522.tex ends '\subsection*{1.3}' above the folio-523 marker; page_523.tex begins 'Rappelons (IV 2.10)'",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": r"Page 523 really begins at the heading 1.3. Exact edit in main.tex, both layers (each string occurs once): replace '\subsection*{1.3}\n%%%%%%%%%%  scan idx 536  |  folio 523  %%%%%%%%%%\n' by '%%%%%%%%%%  scan idx 536  |  folio 523  %%%%%%%%%%\n\subsection*{1.3}\n' (write {1.3.} in both strings if the p. 522 heading fix is applied first).",
})
F.append({
    "page": 523,
    "where": "Démonstration: 'et pour tout sous-schéma intègre fermé de dimension ≤ j , implique (1.3.2)'",
    "scan": "'tout' underlined (both scans; crops_521_525/w523_mid.png)",
    "tex": "no emphasis",
    "kind": "underline",
    "confidence": "high",
    "fix": fx("et pour tout sous-schéma intègre fermé de dimension", r"et pour \emph{tout} sous-schéma intègre fermé de dimension"),
    "note": "Independent of the next entry. The 'pour tout x ∈ Filt^i(X)' of the next sentence is plain in the print.",
})
F.append({
    "page": 523,
    "where": "Démonstration: 'et pour tout sous-schéma intègre fermé Z de dimension ≤ j on a'",
    "scan": "'tout' underlined (both scans; crops_521_525/w523_mid.png)",
    "tex": "no emphasis",
    "kind": "underline",
    "confidence": "high",
    "fix": fx("pour tout sous-schéma intègre fermé $Z$", r"pour \emph{tout} sous-schéma intègre fermé $Z$"),
    "note": "Independent of the previous entry.",
})
F.append({
    "page": 523,
    "where": "Théorème 1.3.2 with its display (1.3.3), then 'Corollaire 1.3.3.'",
    "scan": "the display of Théorème 1.3.2 is numbered (1.3.3) and the next statement is 'Corollaire 1.3.3.' (both scans): the number 1.3.3 is used twice; the next display is (1.3.4)",
    "tex": r"\tag{1.3.3} and \textbf{Corollaire 1.3.3.} (printed reading kept)",
    "kind": "other",
    "confidence": "low",
    "fix": None,
    "note": "Numbering clash of the print, kept by the TeX as the diplomatic layer should. The references '(1.3.3)' on pp. 523-524 ('Montrons d'abord que (1.3.3), pour ... tout sous-schéma intègre fermé de dimension ≤ j', 'd'après (1.1.8) et (1.3.3) pour X = Z') fit the corollary; no renumbering can be read off the print. For the corrected layer's notes only.",
})

# ---------------------------------------------------------------- p. 524
F.append({
    "page": 524,
    "where": "'Pour éviter toute confusion, désignons par ε_Z la classe de O_Z dans K.(Z).'",
    "scan": "'désignons par ε_Z' (a typed epsilon with subscript Z; both scans; crops_521_525/c524_eps.png, w524_eps.png); the formulas that follow write 1_Z (x α_*(1_Z), α_*(α^*(x) 1_Z) twice; w524_1Z.png)",
    "tex": "désignons par $1_Z$ (silently corrected)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": fx("désignons par $1_Z$", r"désignons par $\varepsilon_Z$"),
    "corrected": "désignons par $1_Z$",
    "note": r"The print names the class ε_Z and then writes 1_Z in all three formulas: the ε is the slip. \varepsilon as for the ε of p. 522 (the epsilon form is a global matter). The current layer also reads 1_Z (the corrected edition keeps it).",
})
F.append({
    "page": 524,
    "where": "'Le théorème 1.3.2 est trivial pour i+j ≤ 0 . Supposons le démontré par récurrence'",
    "scan": "'Supposons le' without a hyphen (both scans; crops_521_525/c524_supposons.png, w524_supposons.png)",
    "tex": "Supposons-le (silently corrected)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": fx("Supposons-le", "Supposons le"),
    "corrected": "Supposons-le",
    "note": "The imperative takes the hyphen (as 'montrons la', findings_461_465). The current layer also reads 'Supposons-le'.",
})
F.append({
    "page": 524,
    "where": "'il nous reste à démontrer que pour tout schéma noethérien intègre X de dimension j'",
    "scan": "'intègre' underlined, the rest of the sentence plain (both scans; crops_521_525/w524_top.png)",
    "tex": "no emphasis",
    "kind": "underline",
    "confidence": "high",
    "fix": fx("noethérien intègre $X$", r"noethérien \emph{intègre} $X$"),
    "note": "Independent of the 'Supposons le' entry (no overlap).",
})
F.append({
    "page": 524,
    "where": "'où m ≥ i et E est un O_X-module localement libre de rang n > 0. Distinguons deux cas :'",
    "scan": "'Distinguons deux cas :' begins a new, indented paragraph, indented as 'I. Supposons' below (both scans; crops_521_525/w524_bottom.png)",
    "tex": "the sentence runs on after 'de rang $n>0$.'",
    "kind": "other",
    "confidence": "high",
    "fix": fx("de rang $n>0$. Distinguons", "de rang $n>0$." + NL + NL + "Distinguons"),
    "note": "Missing paragraph break.",
})

# ---------------------------------------------------------------- p. 525
F.append({
    "page": 525,
    "where": "end of page (folio-526 marker)",
    "scan": "p. 525 ends 'Alors on peut trouver un point rationnel u de la fibre générique D_e de D' (the rest of the page blank); p. 526 begins 'sur k(e), car ces points sont en correspondance biunivoque' (both scans; crops_521_525/w526_top.png)",
    "tex": "page_525.tex ends '... de la fibre générique $D_e$ de $D$ sur $k(e)$, car ces' above the folio-526 marker; page 526 begins 'points sont en correspondance'",
    "kind": "marker",
    "confidence": "high",
    "fix": None,
    "note": r"Page 526 really begins at 'sur $k(e)$, car ces'. Exact edit in main.tex, both layers (the string occurs once): replace 'de $D$ sur $k(e)$, car ces\n%%%%%%%%%%  scan idx 539  |  folio 526  %%%%%%%%%%\npoints sont' by 'de $D$\n%%%%%%%%%%  scan idx 539  |  folio 526  %%%%%%%%%%\nsur $k(e)$, car ces points sont'.",
})

# ---------------------------------------------------------------- write and check
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
data = json.loads(OUT.read_text(encoding="utf-8"))
ok = True
for i, f in enumerate(data):
    t = (B / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    if f["fix"] is not None:
        n = t.count(f["fix"]["old"])
        if n != 1 or "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
        print(i, f["page"], f["kind"], "old count", n, repr(f["fix"]["old"][:60]))
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        print("missing corrected", i)
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        ok = False
        print("stray corrected", i)
counts = {}
for f in data:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("entries", len(data), "counts", counts, "ALL OK" if ok else "PROBLEM")
