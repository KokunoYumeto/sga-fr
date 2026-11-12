import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
OUT = RUN / "findings_086_090.json"

findings = [
    {
        "page": 86,
        "where": "(0.2.7), 'est premier aux caractéristique résiduelles de S'",
        "scan": "est premier aux caractéristique résiduelles de S (no s on caractéristique)",
        "tex": "caractéristique résiduelles",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "caractéristiques résiduelles",
        "note": "Agreement error of the print (plural 'aux ... résiduelles'). The TeX keeps the printed reading.",
    },
    {
        "page": 87,
        "where": "heading of Définition 1.1.2",
        "scan": "only 'Définition' is underlined; the rule stops before '1.1.2.' (checked at 3x), as for 'Rappel' 1.1.3 on the same page",
        "tex": "\\underline{Définition 1.1.2.}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": "\\underline{Définition 1.1.2.}",
            "new": "\\underline{Définition} 1.1.2.",
        },
        "note": "The TeX already writes the parallel heading on this page as \\underline{Rappel} 1.1.3.",
    },
    {
        "page": 87,
        "where": "1.1.1, second paragraph, 'est une action par automorphismesde G sur (Ȳ, F)'",
        "scan": "auto-/morphismesde G (no space between 'automorphismes' and 'de'; checked at 2x)",
        "tex": "automorphismesde",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "automorphismes de",
        "note": "Missing word space in the typescript. The TeX keeps the printed reading.",
    },
    {
        "page": 87,
        "where": "1.1.1, second paragraph, 'En d'autre termes, c'est un système d'isomorphismes'",
        "scan": "En d'autre / termes (no s after autre)",
        "tex": "En d'autre termes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "En d'autres termes",
        "note": "Same spelling error as on p. 83. The TeX keeps the printed reading.",
    },
    {
        "page": 87,
        "where": "Exposé XIII, 1.1.1 to the end of 1.1.3 (pp. 87-89): every sheaf letter F and G",
        "scan": "typed Fraktur letters: Fraktur F (a 3-shaped body under a top bar with a crossbar) and Fraktur G (a G with a hooked descender), some with a typed bar (p. 87) or a hand-drawn arrow (p. 88) above (checked at 4-10x)",
        "tex": "\\mathcal{F}, \\mathcal{G}",
        "kind": "font",
        "confidence": "high",
        "fix": None,
        "note": (
            "Convention of the transcription, reported once instead of 36 times: 13 \\mathcal{F} on p. 87, "
            "12 \\mathcal{F} and 6 \\mathcal{G} on p. 88, 5 \\mathcal{G} on p. 89. These are all the "
            "\\mathcal{F} and \\mathcal{G} of expose_XIII_body.tex (its only other \\mathcal is \\mathcal{O}_{S} "
            "on p. 98, not checked here). Examples: p. 87 'Soit $\\mathcal{F}$ un faisceau d'ensembles'; "
            "p. 88 '$\\mathcal{G} \\longmapsto (\\overline{\\varphi}_* \\mathcal{G})^{\\mathrm{Gal}(\\overline{k}/k)}$'; "
            "p. 89 'que pour $\\mathcal{G}'$ sur $Y_i$'. Fix: replace \\mathcal{F} by \\mathfrak{F} and "
            "\\mathcal{G} by \\mathfrak{G} on these three pages, keeping \\bar, \\vec and the primes. The "
            "diplomatic TeX of Exposés XVIII and XXI already writes \\mathfrak{F}."
        ),
    },
    {
        "page": 89,
        "where": "first display, left side, 'φ̄^*(φ_* G)^{Gal(k̄/k)}'",
        "scan": "φ̄*(φ_* G)^{Gal(k̄/k)}: the first φ carries the typed bar, the second has none (checked at 4x); the same expression on p. 88 is printed φ̄*(φ̄_* G)^{Gal(k̄/k)} with both bars",
        "tex": "\\overline{\\varphi}^*(\\varphi_*",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\overline{\\varphi}^*(\\overline{\\varphi}_*",
        "note": (
            "No unbarred, unindexed φ is defined (only φ_i and φ̄); the left side restates the arrow "
            "φ̄^*(φ̄_* G)^{Gal(k̄/k)} → G of p. 88. The TeX keeps the printed reading. Medium only because a "
            "lost typed bar cannot be excluded, though the other bars of the display are intact."
        ),
    },
    {
        "page": 89,
        "where": "1.2.2, diagram s → S ← η",
        "scan": "s ↪(i) S ↩(j) η  .  (a typed full stop follows the diagram on the same line)",
        "tex": "diagram without the full stop (the STRUCTURE comment records the period)",
        "kind": "punctuation",
        "confidence": "high",
        "fix": {
            "old": "\\eta \\arrow[l, hook, \"j\"']\n\\end{tikzcd}",
            "new": "\\eta \\arrow[l, hook, \"j\"']\n\\end{tikzcd}\\quad .",
        },
        "note": "Known case of punctuation after a diagram; written as in the earlier fixes (\\end{tikzcd}\\quad .).",
    },
]

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")

# check: every fix's old occurs exactly once in its page file; never touches a marker line
bad = 0
for x in findings:
    fx = x.get("fix")
    if not fx:
        continue
    page_file = RUN / "b086_090" / f"page_{x['page']:03d}.tex"
    t = page_file.read_text(encoding="utf-8")
    n = t.count(fx["old"])
    mark = "scan idx" in fx["old"] or "scan idx" in fx["new"]
    print(x["page"], x["kind"], "occurrences:", n, "marker:" if mark else "")
    if n != 1 or mark:
        bad += 1
# also check that the tex fields of null-fix misprints occur on their page
for x in findings:
    if x["kind"] == "misprint_in_print":
        page_file = RUN / "b086_090" / f"page_{x['page']:03d}.tex"
        t = page_file.read_text(encoding="utf-8")
        print(x["page"], "misprint tex occurs", t.count(x["tex"]), "times:", x["tex"])
print("bad:", bad)
