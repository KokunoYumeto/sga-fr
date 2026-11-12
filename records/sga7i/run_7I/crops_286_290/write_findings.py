import json, sys
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\findings_286_290_recheck.json"
F = []
F.append({
 "page": 287,
 "where": "Heading of section 6",
 "scan": "6. Extensions et biextensions par le modèle de Néron de G_m . : the heading's underline ends after 'de'; G_m stands outside it, with its own short underline under the G only (the typescript's mark for the multiplicative group)",
 "tex": r"6. \underline{Extensions et biextensions par le modèle de Néron de $G_m$} .",
 "kind": "underline",
 "confidence": "high",
 "fix": {"old": r"Néron de $G_m$}", "new": r"Néron de} $\underline{G}_m$"},
 "note": r"The file writes the underlined-G multiplicative group as $\underline{G}_m$ (e.g. the table-of-contents line for this section)."
})
F.append({
 "page": 287,
 "where": "6.1, paragraph after (6.1.2): 'On constate aussitôt, grâce à (5.7.1)'",
 "scan": "graĉe (the circumflex typed over the c)",
 "tex": r"gra\^{c}e",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "grâce",
 "note": "Misplaced accent in the typescript; the TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 288,
 "where": "6.1.4, second paragraph: 'la catégorie des extensions de Z_Z par G'",
 "scan": "extensions de ℤ_Z par G (double-struck Z with subscript Z)",
 "tex": r"$\mathbb{Z}_Z$",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": r"$\mathbb{Z}_S$",
 "note": "Wrong index: the free Groupe on one generator introduced in the same sentence is Z_S, whose extensions by G VII 1.4 identifies with G-torsors. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 288,
 "where": "Lemme 6.2: 'image de la section 1 de Z_S sur S'",
 "scan": "sur S, with a stray typed G-bar (bar over G) set below and to the left of the S",
 "tex": r"${}_{\overline{G}}S$",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "$S$",
 "note": "Stray symbol in the typescript: the G-bar belongs to nothing in the sentence (read 'de Z_S sur S'). The TeX reproduces it as a left subscript; a further stray dash between the lines below 'sur' is rightly not transcribed. 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 289,
 "where": "6.2.1: 'l'isomorphisme canonique de G_U-torseurs f*_n(G-bar)|U = G_U, définie par la première relation (5.7.1)'",
 "scan": "définie par la première relation (5.7.1)",
 "tex": ", définie par la première",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": ", défini par la première",
 "note": "Agreement slip: the participle refers to 'l'isomorphisme' (masculine). The TeX keeps the printed reading (the corrected layer too). 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 289,
 "where": "6.2.1, same sentence: '..., est définie par la section s^(n) de F^(n)_U'",
 "scan": "est définie par la section s^(n)",
 "tex": "est définie par la section $s^{(n)}$",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": "est défini par la section $s^{(n)}$",
 "note": "Agreement slip: the subject is 'l'isomorphisme canonique' (masculine). The TeX keeps the printed reading (the corrected layer too). 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 289,
 "where": "6.2.1 b), compatibility condition: 'g_i et g_j coïncident sur S'_i n S'_j = U'",
 "scan": "g_i et g_j, both without the bar",
 "tex": "$g_i$ et $g_j$",
 "kind": "misprint_in_print",
 "confidence": "medium",
 "fix": None,
 "corrected": r"$\overline{g}_i$ et $\overline{g}_j$",
 "note": "Bars missing in the print: these are the sections g-bar_i of b), barred just before ('les sections g-bar_i') and in the display below; 6.2.2 has the bars in the same condition. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 289,
 "where": "Last paragraph: 'Comme la description 3.2 d'une extension G-bar de Z_{S,T} par G'",
 "scan": "la description 3.2",
 "tex": "la description 3.2 d'une",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "la description 6.2 d'une",
 "note": "Wrong reference: the description of an extension of Z_{S,T} by G is Lemme 6.2 (3.2 of this exposé concerns Q an abelian scheme). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
F.append({
 "page": 290,
 "where": "6.2.2: 'pour tout couple d'léments i,j dans I'",
 "scan": "d'léments",
 "tex": "d'léments",
 "kind": "misprint_in_print",
 "confidence": "high",
 "fix": None,
 "corrected": "d'éléments",
 "note": "Typing error (letter dropped); the TeX keeps the printed reading. 'corrected' replaces the 'tex' substring."
})
with open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("wrote", len(F))
