import json, os, sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
PAGES = os.path.join(RUN, "b361_365")
OUT = os.path.join(RUN, "findings_361_365.json")

findings = [
    {
        "page": 361,
        "where": "line before (4.3.5): 'peut aussi de décrire par'",
        "scan": "peut aussi de décrire par",
        "tex": "peut aussi de décrire par",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "peut aussi se décrire par",
        "note": "Print misprint ('de' for the reflexive 'se'). The TeX keeps the printed reading; 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 362,
        "where": "proof of 4.3.2, first sentence: 'il suffit de voir que l'application ensembliste sous-jacente aux morphismes Spec(k) -> A représentés par les deux membres sont les mêmes'",
        "scan": "l'application ensembliste sous-jacente aux morphismes ... sont les mêmes",
        "tex": "l'application ensembliste sous-jacente aux morphismes",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "les applications ensemblistes sous-jacentes aux morphismes",
        "note": "Agreement error of the print: singular subject 'l'application ensembliste sous-jacente' with plural 'sont les mêmes' (the maps underlying the two morphisms are compared). The TeX keeps the printed reading; 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 362,
        "where": "Corollaire 4.4: 'sont respectivement q^n, q^{n/2} et 1. En ce qui concerne les deux morceaux'",
        "scan": "'et' underlined, '1.' not underlined, then 'En ce qui concerne les deux morceaux' underlined",
        "tex": r"\underline{et 1. En ce qui concerne les deux morceaux}",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": r"\underline{et 1. En ce qui concerne les deux morceaux}",
            "new": r"\underline{et} 1. \underline{En ce qui concerne les deux morceaux}",
        },
        "note": "The print breaks the underline at the numeral '1.' (checked at 2x zoom).",
    },
    {
        "page": 363,
        "where": "end of the proof of 4.4: 'ce qui prouve la derniere assertion de 4.4'",
        "scan": "la derniere assertion (no grave accent; the final 're' is overtyped)",
        "tex": "la derniere assertion",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "la dernière assertion",
        "note": "Accent missing in the print (none visible at 4x zoom; the other accents on the page print clearly). The TeX keeps the printed reading.",
    },
    {
        "page": 363,
        "where": "after (4.5.3): 'On vérifie (loc. cit) que cette expression'",
        "scan": "(loc. cit) with no full stop after 'cit'",
        "tex": "(loc. cit)",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "(loc. cit.)",
        "note": "Abbreviation point omitted (checked at 2x zoom); everywhere else in the volume the transcription has 'loc. cit.'. The TeX keeps the printed reading.",
    },
    {
        "page": 364,
        "where": "proof of 4.6: 'des sous-Z_l-modules qui sont manisfestement des facteurs directs'",
        "scan": "manisfestement",
        "tex": "manisfestement",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "manifestement",
        "note": "Typing error of the print. The TeX keeps the printed reading.",
    },
    {
        "page": 364,
        "where": "footnote (*): 'l'exposant conducteur (total) de A_K'",
        "scan": "the underline begins under the l': 'l'exposant conducteur' underlined",
        "tex": r"l'\underline{exposant conducteur} (total)",
        "kind": "underline",
        "confidence": "high",
        "fix": {
            "old": r"l'\underline{exposant conducteur} (total)",
            "new": r"\underline{l'exposant conducteur} (total)",
        },
        "note": "Unlike 'l'exposant conducteur modéré' two lines up and 'l'exposant conducteur immodéré' in the text (underline from 'exposant'), here the underline includes the l' (checked at 2x zoom).",
    },
    {
        "page": 365,
        "where": "before (4.6.1): 'et psi le caractère de la représentation de I dans L-check'",
        "scan": "de la représentation de I dans Ľ (typed capital I, like the I of 'groupe d'inertie I' below; distinct from the Γ of the line above)",
        "tex": r"représentation de $\Gamma$ dans $\check{L}$",
        "kind": "symbol",
        "confidence": "high",
        "fix": {
            "old": r"représentation de $\Gamma$ dans $\check{L}$",
            "new": r"représentation de $I$ dans $\check{L}$",
        },
        "note": "The print has the inertia group I here (checked at 3x zoom). Not a misprint: S is strictly local, so I acts on Ľ through its quotient Γ and the sum over g in Γ in (4.6.1) still makes sense; Γ would only parallel 'la représentation de Γ dans V_i' in the line above.",
    },
    {
        "page": 365,
        "where": "'Prenant L = Sw, il en est de même du caractère psi(g) de L'",
        "scan": "L = Sw, with Sw the Swan module as everywhere else",
        "tex": "$L = Sw$",
        "kind": "font",
        "confidence": "medium",
        "fix": {
            "old": "$L = Sw$",
            "new": r"$L = \mathrm{Sw}$",
        },
        "note": r"The file writes the Swan module $\mathrm{Sw}$ everywhere else ((4.5.2), (4.5.3), (4.5.4), p. 364); only here it is set in math italic, as a product S w.",
    },
]

# Check: every fix 'old' occurs exactly once in its page file; every 'tex' occurs in it.
ok = True
for f in findings:
    path = os.path.join(PAGES, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if f["fix"] is not None:
        n = text.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", n, f["page"], repr(f["fix"]["old"]))
        # the old string must not cross a marker line
        if "%%%%%%%%%%" in f["fix"]["old"]:
            ok = False
            print("FIX CROSSES MARKER", f["page"])
    nt = text.count(f["tex"])
    if nt < 1:
        ok = False
        print("TEX NOT FOUND", f["page"], repr(f["tex"]))
    elif f["fix"] is None and nt != 1:
        print("note: tex occurs", nt, "times on page", f["page"], repr(f["tex"]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

print("ok" if ok else "PROBLEMS", len(findings), "findings written to", OUT)
