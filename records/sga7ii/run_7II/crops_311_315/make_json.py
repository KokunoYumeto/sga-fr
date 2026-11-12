import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
OUT = os.path.join(RUN, "findings_311_315_recheck.json")

F = []

F.append({
    "page": 311,
    "where": "heading 5.9",
    "scan": "n'est pas vérifiéé (two accented e at the end)",
    "tex": r"\underline{n'est pas vérifiéé}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "vérifiée",
    "note": "Typing error of the typescript (checked at 2.5x). The TeX keeps the printed reading.",
})

F.append({
    "page": 311,
    "where": "5.9, first paragraph, 'sont chacun la réunion'",
    "scan": "sont chacun la réunion de deux droites",
    "tex": "sont chacun la réunion de deux droites",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "sont chacune la réunion de deux droites",
    "note": "Agreement slip: the subject is 'les fibres singulières'. The TeX keeps the printed reading.",
})

F.append({
    "page": 312,
    "where": "heading of section 6",
    "scan": "cycles evanescents (no accent on the initial e)",
    "tex": "des cycles evanescents}",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "évanescents",
    "note": "Accent left out (checked at 1.6x); the same line prints 'théorie' with é, and the volume elsewhere prints 'évanescents'. The TeX keeps the printed reading.",
})

F.append({
    "page": 312,
    "where": "Proposition 6.1, 'Choissisons un point géométrique'",
    "scan": "Choissisons",
    "tex": r"\underline{Choissisons un point géométrique}",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "Choisissons",
    "note": "Typing error (checked at 1.4x); p. 313 prints 'Choisissons'. The TeX keeps the printed reading.",
})

F.append({
    "page": 313,
    "where": "6.1.2, first sentence, '\"chemin\" dans'",
    "scan": "'et d'un' underlined at the line end; on the next line only the word chemin is underlined, both quotation marks stand outside the underline, and 'dans' carries its own underline",
    "tex": r"\underline{et d'un ``chemin'' dans}",
    "kind": "underline",
    "confidence": "high",
    "fix": {
        "old": r"\underline{et d'un ``chemin'' dans}",
        "new": r"\underline{et d'un} ``\underline{chemin}'' \underline{dans}",
    },
    "note": "Checked at 2.2x.",
})

F.append({
    "page": 313,
    "where": "6.1.2, second sentence, '\"le\" groupe d'inertie'",
    "scan": "'dont l'image est' underlined; only the word le is underlined, its quotation marks stand outside the underline; 'groupe d'inertie en' carries its own underline",
    "tex": r"\underline{dont l'image est ``le'' groupe d'inertie en}",
    "kind": "underline",
    "confidence": "high",
    "fix": {
        "old": r"\underline{dont l'image est ``le'' groupe d'inertie en}",
        "new": r"\underline{dont l'image est} ``\underline{le}'' \underline{groupe d'inertie en}",
    },
    "note": "Checked at 2x.",
})

F.append({
    "page": 313,
    "where": "Démonstration, first line",
    "scan": "de la grassmanniene formée",
    "tex": "de la grassmanniene formée",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "grassmannienne",
    "note": "Typing error: one n missing in the ending (-iene for -ienne). The TeX keeps the printed reading.",
})

F.append({
    "page": 313,
    "where": "(ii), parenthesis",
    "scan": "une droite \"joingnant ā au point générique",
    "tex": r"``joingnant $\overline{a}$",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "joignant",
    "note": "Typing error. The TeX keeps the printed reading.",
})

F.append({
    "page": 313,
    "where": "last sentence",
    "scan": "Soit o le point T correspondant à la droite donnée D_o .",
    "tex": "Soit o le point T correspondant",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "Soit o le point de T correspondant",
    "note": "A word is missing: o is the point of T that corresponds to D_o. The TeX keeps the printed reading.",
})

F.append({
    "page": 314,
    "where": "first paragraph, 'entre η̄ et O dans T'",
    "scan": "entre η̄ et O dans T: a capital O (or a zero), not the small o that names the point",
    "tex": r"et $O$ dans $T$",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": "$o$",
    "note": "The point is called o on p. 313 ('Soit o le point T') and in the arrow labels η̄ ⟶ o of (6.1.3), (6.1.4.1) and (6.1.5). In this typeface capital O and zero have the same size (18x22 px here; 19x23 and 18x24 px on p. 315), so the glyph cannot be told apart from 0; the TeX's O stands. The TeX keeps the printed reading.",
})

F.append({
    "page": 314,
    "where": "(6.1.3), source of the arrow",
    "scan": "π_1^mod(D_η̄ - D_η̄ ∩ Z), ā): a closing parenthesis after Z that closes nothing",
    "tex": r"\pi_1^{\mathrm{mod}}(D_{\bar{\eta}} - D_{\bar{\eta}} \cap Z), \bar{a})",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\pi_1^{\mathrm{mod}}(D_{\bar{\eta}} - D_{\bar{\eta}} \cap Z, \bar{a})",
    "note": "Superfluous parenthesis in the print (checked at 1.5x). The TeX keeps the printed reading.",
})

F.append({
    "page": 314,
    "where": "6.1.4, first line",
    "scan": "Les homomorphisme (6.1.2.1) de monodromie locale",
    "tex": "Les homomorphisme (6.1.2.1)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "Les homomorphismes",
    "note": "Plural s missing ('s'obtiennent' follows). The TeX keeps the printed reading.",
})

F.append({
    "page": 314,
    "where": "6.1.4, unnumbered display, target",
    "scan": "π_1(D_o-D_o∩Z,ā) without the superscript mod",
    "tex": r"\longrightarrow \pi_1(D_o - D_o \cap Z, \bar{a})",
    "kind": "misprint_in_print",
    "confidence": "low",
    "fix": None,
    "corrected": r"\pi_1^{\mathrm{mod}}(D_o - D_o \cap Z, \bar{a})",
    "note": "The display restates the homomorphisms (6.1.2.1), whose target is π_1^mod(D_o - D_o ∩ Z, ā); the composite (6.1.4.1) has the same target. The TeX keeps the printed reading.",
})

F.append({
    "page": 315,
    "where": "end of the paragraph before 6.1.6.1",
    "scan": "(pour la flèche composé E ⟶ ...",
    "tex": "(pour la flèche composé $E",
    "kind": "misprint_in_print",
    "confidence": "medium",
    "fix": None,
    "corrected": "la flèche composée",
    "note": "Agreement slip: 'flèche' is feminine. The TeX keeps the printed reading.",
})

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", OUT, len(F))
