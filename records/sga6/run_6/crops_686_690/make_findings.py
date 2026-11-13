"""Build findings_686_690.json for the SGA 6 scan check (pages 686-690)."""
import json
import pathlib

OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_686_690.json")

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def title(page, item, text, note="As the bibliography titles fixed on pp. 19, 159, 273, 296, 364, 415, 497 and 594."):
    add(page, f"bibliography {item}, title", f"'{text}' typed plain, neither underlined nor italic (both scans)",
        r"\emph{" + text + "}", "font", "high", (r"\emph{" + text + "}", text),
        "The typescript neither underlines nor italicizes the titles of this bibliography. " + note)


def prange(page, item, old, new):
    add(page, f"bibliography {item}, page range", f"'{new}': 'p.' and a typed hyphen (both scans)", old, "word", "high",
        (old, new), "The TeX writes 'pp.' for the print's 'p.' and an en dash for its hyphen; one edit for both "
        "(the en dash as in the bibliography ranges fixed on pp. 220-221, 497 and 594).")


# ---------------- page 686 ----------------
add(686, "end of the first paragraph, 'postulées dans 7.1 (*)'",
    "'dans 7.1 (*)': no full stop after 7.1 or after the call; the next paragraph follows (both scans; crops_686_690/w686_71.png)",
    r"dans 7.1.\footnote{", "punctuation", "high", (r"dans 7.1.\footnote{", r"dans 7.1\footnote{"),
    "The TeX adds a sentence-final full stop the print does not have. The (*) call printed as a LaTeX number is the volume convention of findings_016_020 (p. 20).")
add(686, "footnote (*), 'par L. ILLUSIE; cf. [13]'", "'L. ILLUSIE' typed in capitals (both scans; crops_686_690/w686_foot.png)",
    "par L. Illusie;", "word", "high", ("par L. Illusie;", "par L. ILLUSIE;"),
    "Capitals against small letters, as the applied author lines 'par L. ILLUSIE' (pp. 78, 160, 222, 274).")
add(686, "footnote (*), end: 'cf. [13]'", "'cf. [13]' ends the note without a full stop (both scans; crops_686_690/w686_foot.png)",
    r"cf. [13].}", "punctuation", "high", (r"cf. [13].}", r"cf. [13]}"),
    "The TeX adds the final full stop. Independent of the ILLUSIE entry (no overlap).")
add(686, "§ 8, first sentence: 'définir l'équivalence rationelle des cycles'",
    "'rationelle' with one n (both scans)", "rationelle", "misprint_in_print", "high", None,
    "Spelling slip of the typescript ('rationnelle'); the TeX keeps the printed reading. The same slip stands in bibliography [4] (p. 687). The second reading (sga6_fr_r1) has the corrected 'rationnelle'.",
    corrected="rationnelle")
add(686, "§ 8, third paragraph: 'les substituts Gr˙(X), Gr˙_top(X)'",
    "Gr followed by the same raised typed dot as the next Gr˙_top(X); the apostrophe of l'anneau in the same line is a different, vertical mark (both scans; crops_686_690/m686_gr.png, w686_gr_zoom.png)",
    r"$\operatorname{Gr}'(X)$", "symbol", "high", (r"$\operatorname{Gr}'(X)$", r"$\operatorname{Gr}^\bullet(X)$"),
    r"Prime for the print's raised dot; the TeX writes the second substitute \Gtop^\bullet(X) and Exposé XIV has \operatorname{Gr}^\bullet 33 times (Gr' only here and on p. 683; the raised dot in Gr is written \bullet by the global rule). The second reading also has Gr' here (its image check ended at p. 678, where it reads primes); on this page both scans show the dot.")
add(686, "last line of the page: 'des anneaux locaux à singularité'",
    "'à singularité' without s at the end of the page (both scans; crops_686_690/w686_sing.png)",
    "à singularités", "word", "high", ("à singularités", "à singularité"),
    "Plural for the print's singular; the phrase continues on p. 687 with 'isolée' (also singular there). Apply together with the p. 687 'isolée' entry. The second reading has the same plural.")

# ---------------- page 687 ----------------
add(687, "first line: 'isolée sont des invariants géométriques'",
    "'isolée' singular (both scans; crops_686_690/w687_top.png)", "isolées sont", "word", "high",
    ("isolées sont", "isolée sont"),
    "Goes with the p. 686 entry 'à singularité': the print reads 'à singularité isolée'.")
add(687, "first paragraph: 'dans l'étude \"arithmétiques\" de ces anneaux locaux'",
    "'arithmétiques' with a final s (both scans; crops_686_690/w687_top.png)", "``arithmétiques''",
    "misprint_in_print", "medium", None,
    "Agreement slip: the adjective qualifies 'l'étude' (singular). The TeX keeps the printed reading; the second reading has 'arithmétique'.",
    corrected="arithmétique")
add(687, "second paragraph: 'les relations établies resp. conjecturées au n° 4'",
    "'n°' with the raised o (both scans)", "au no. 4", "symbol", "high", ("au no. 4", r"au n\textsuperscript{o} 4"),
    r"The file's form of the numéro sign is n\textsuperscript{o} (26 times in main.tex, e.g. [17] on p. 688; applied on p. 631); 'no.' for the numéro sign occurs in main.tex only in Exposé XIV (8 times, 4 of them on pp. 687-688).")
add(687, "second paragraph, end: 'énoncée au n° 3.'", "'n°' with the raised o (both scans)", "au no. 3.", "symbol", "high",
    ("au no. 3.", r"au n\textsuperscript{o} 3."), "As 'au n° 4' in the same paragraph.")
add(687, "heading of the bibliography", "'BIBLIOGRAPHIE': the word alone, typed in capitals (both scans)",
    r"\subsection*{Bibliographie de l'Exposé XIV}", "extra", "high",
    (r"\subsection*{Bibliographie de l'Exposé XIV}", r"\subsection*{BIBLIOGRAPHIE}"),
    r"The TeX adds 'de l'Exposé XIV' and sets the word in small letters; same form as eight other bibliography headings of main.tex (\subsection*{BIBLIOGRAPHIE}).")
title(687, "[1] Atiyah-Hirzebruch", r"The Riemann--Roch theorem for analytic embeddings",
      "Riemann--Roch keeps its joint-name dash (global rule).")
prange(687, "[1] Atiyah-Hirzebruch", "pp. 151--166", "p. 151-166")
add(687, "bibliography [2] Borel-Serre, 'J.P. Serre'", "'J.P.' without hyphen (both scans)", "J.-P. Serre", "punctuation",
    "high", ("J.-P. Serre", "J.P. Serre"), "The TeX adds a hyphen to the initials (as fixed on p. 19).")
title(687, "[2] Borel-Serre", r"Le théorème de Riemann--Roch", "Riemann--Roch keeps its joint-name dash (global rule).")
prange(687, "[2] Borel-Serre", "pp. 97--136", "p. 97-136")
add(687, "bibliography [3] Bott-Samelson, 'Amer. Journ. of Math. vol 80'",
    "'vol 80' without the abbreviation's stop (both scans; crops_686_690/w687_b3.png)", "vol. 80",
    "misprint_in_print", "medium", ("vol. 80", "vol 80"),
    "Typing slip: the other entries write 'vol.'. The TeX silently supplies the stop; the fix restores the printed reading.",
    corrected="vol. 80")
title(687, "[4] Chevalley", r"Les classes d'équivalence rationelle")
add(687, "bibliography [4] Chevalley, title: 'Les classes d'équivalence rationelle'",
    "'rationelle' with one n (both scans)", "rationelle", "misprint_in_print", "high", None,
    "As on p. 686; the TeX keeps the printed reading (the \\emph entry of the same title does not touch the word).",
    corrected="rationnelle")
title(687, "[5] Chevalley", "Classification des groupes de Lie algébriques")
title(687, "[6] Dold-Puppe", "Homologie nicht-additiver Funktoren. Anwendungen")
add(687, "bibliography [6] Dold-Puppe, 'Annales de l'Inst. Fourier t. XI'",
    "no comma after 'Fourier' (both scans; crops_686_690/w687_b6.png)", "Fourier, t. XI", "punctuation", "high",
    ("Fourier, t. XI", "Fourier t. XI"), "The TeX adds a comma.")
prange(687, "[6] Dold-Puppe", "pp. 201--312", "p. 201-312")
title(687, "[7] Grauert", "Ein Theorem der analytischen Garbentheorie")
add(687, "bibliography [7] Grauert, 'Pub. Math. n° 5'", "'n°' with the raised o (both scans)", "Math. no. 5", "symbol",
    "high", ("Math. no. 5", r"Math. n\textsuperscript{o} 5"), "As 'au n° 4' above.")
prange(687, "[7] Grauert", "pp. 5--64", "p. 5-64")
title(687, "[8] Grothendieck", r"Classes de faisceaux et théorème de Riemann--Roch",
      "Riemann--Roch keeps its joint-name dash (global rule).")
title(687, "[9] Grothendieck", "La théorie des classes de Chern")
add(687, "bibliography [9] Grothendieck, 'Bull. Soc. Math. France vol. 86, p. 137-154'",
    "no comma after 'France'; 'p.' and a typed hyphen (both scans; crops_686_690/w687_b9.png)",
    "France, vol. 86, pp. 137--154", "punctuation", "high",
    ("France, vol. 86, pp. 137--154", "France vol. 86, p. 137-154"),
    "One edit for the added comma and the page range ('pp.', en dash), since 'France, vol. 86' alone also matches entry [2], which has the comma in the print.")

# ---------------- page 688 ----------------
add(688, "start of the page: bibliography entry [10]",
    "the page begins with '[10] A.Grothendieck, Classes de Chern et représentations ...'; p. 687 ends with entry [9] (both scans)",
    r"'\item A.' is the last line of page_687.tex, above the marker; page_688.tex begins with 'Grothendieck,'",
    "marker", "high", None,
    r"The marker of folio 688 stands one TeX line too late: move it above '\item A.': python -I move_marker.py 6 688 '\item A.' --before (single quotes; the last '\item A.' before the marker is that line; simulated in memory on both layers with crops_686_690/sim_marker.py: '... pp. 137--154 (1958).' / the marker / '\item A.' / 'Grothendieck, \emph{Classes de Chern ...'). No other entry of pp. 687-688 quotes the moved line.")
title(688, "[10] Grothendieck", "Classes de Chern et représentations linéaires des groupes discrets")
title(688, "[10] Grothendieck, the book", "Dix exposés sur la cohomologie des schémas")
add(688, "bibliography [10], end: 'Masson-North Holland Pub. Cie'",
    "no full stop after 'Cie' (both scans; crops_686_690/w688_b10.png)", "Pub. Cie.", "punctuation", "high",
    ("Pub. Cie.", "Pub. Cie"),
    "The TeX adds the final stop. Masson--North Holland (hyphen in the print) is a joint name: handled globally.")
title(688, "[11] Hironaka", "Resolution of singularities of an algebraic variety over a field of characteristic zero")
prange(688, "[11] Hironaka", "pp. 109--326", "p. 109-326")
add(688, "bibliography [14] Serre, 'J.P. Serre'", "'J.P.' without hyphen (both scans)", "J.-P. Serre", "punctuation",
    "high", ("J.-P. Serre", "J.P. Serre"), "As [2] on p. 687.")
title(688, "[14] Serre", "Algébre Locale, Multiplicités")
add(688, "bibliography [14] Serre, title: 'Algébre Locale'", "'Algébre' with an acute accent (both scans; crops_686_690/w688_b14.png)",
    "Algébre", "misprint_in_print", "high", None,
    "Accent slip ('Algèbre'); the TeX keeps the printed reading. The \\emph entry of the same title does not touch the word.",
    corrected="Algèbre")
add(688, "bibliography [14] Serre, 'Lecture Notes in Math . n° 11'", "'n°' with the raised o (both scans)", "Math. no. 11",
    "symbol", "high", ("Math. no. 11", r"Math. n\textsuperscript{o} 11"), "As the n° entries of p. 687.")
title(688, "[15] Borel", "Sous-groupes commutatifs et torsion des groupes de Lie compacts connexes")
prange(688, "[15] Borel", "pp. 216--240", "p. 216-240")
title(688, "[16] Deligne, the book", "Théorie des topos et cohomologie étale des schémas (SGA 6)")
add(688, "bibliography [16] Deligne, '(SGA 6)'", "'(SGA 6)' (both scans; crops_686_690/w688_b16_17.png)", "(SGA 6)",
    "misprint_in_print", "high", None,
    "Théorie des topos et cohomologie étale des schémas is SGA 4. The TeX keeps the printed reading; the corrected layer already reads SGA 4 (RECONCILE_CODEX_6, SGA-SRC-001457).",
    corrected="(SGA 4)")
add(688, "bibliography [17], author: 'U. Mausin'", "'U. Mausin' (both scans; crops_686_690/w688_b16_17.png)",
    "Yu. I. Manin", "misprint_in_print", "high", ("Yu. I. Manin", "U. Mausin"),
    "The name is Yu. I. Manin (the note on p. 689 prints MANIN). The TeX silently corrects it; the fix restores the printed reading. RECONCILE_CODEX_6 SGA-SRC-001458 left the diplomatic layer to this check; the base text of the second reading (sga6_fr_r1/base/fr.tex) reads 'U. Mausin', as the print.",
    corrected="Yu. I. Manin")
title(688, "[17] Manin", "Correspondances, motifs et transformations monoïdales")
add(688, "bibliography [17], 'MAt. Sborik'", "'MAt.' with a capital A (both scans; crops_686_690/w688_b16_17.png)", "Mat.",
    "misprint_in_print", "high", ("Mat.", "MAt."),
    "Typing slip (Mat. Sbornik); the TeX silently corrects it. Disjoint from the next entry.", corrected="Mat.")
add(688, "bibliography [17], 'MAt. Sborik'", "'Sborik' without n (both scans; crops_686_690/w688_b16_17.png)", "Sbornik",
    "misprint_in_print", "high", ("Sbornik", "Sborik"),
    "Typing slip for Sbornik; the TeX silently corrects it.", corrected="Sbornik")
add(688, "bibliography [17], 't 77 (119)'", "'t 77' without the abbreviation's stop (both scans)", "t. 77",
    "misprint_in_print", "medium", ("t. 77", "t 77"),
    "Typing slip ('t.' as in [6] 't. XI'); the TeX silently supplies the stop.", corrected="t. 77")
add(688, "bibliography [17], 't 77 (119) n° 4 , 1968.'", "no comma after '(119)' (both scans)", "(119),", "punctuation",
    "high", ("(119),", "(119)"), r"The TeX adds a comma. The n\textsuperscript{o} 4 that follows is right.")
add(688, "footnote (*) of [16]-[17]: 'Ajouté en février 1969'",
    "no full stop after 1969 (both scans; crops_686_690/w688_foot.png)", r"février 1969.}", "punctuation", "high",
    (r"février 1969.}", r"février 1969}"), "The TeX adds the final stop.")

# ---------------- page 689 ----------------
add(689, "first heading: 'Note pour la page 1.'",
    "'Note pour la page 1.' run into the text, with a full stop after 1 (both scans)",
    r"\subsection*{Note pour la page 1}", "punctuation", "low",
    (r"\subsection*{Note pour la page 1}", r"\subsection*{Note pour la page 1.}"),
    "The heading set as its own paragraph and without the underline is accepted; only the printed full stop is restored (as for the run-in paragraph numbers of pp. 394-464). Drop if headings set apart lose their stop by convention.")
add(689, "Note pour la page 1, line 2: 'des opérations λ^i dans K˙(X)'",
    "K with a raised typed dot; the apostrophes of the page (l'hypothèse, d'Algèbres) are vertical ticks (both scans; crops_686_690/m689_K.png, w689_K.png)",
    "dans $K'(X)$", "symbol", "high", ("dans $K'(X)$", r"dans $K^\bullet(X)$"),
    r"Prime for the print's raised dot; Exposé XIV's TeX writes K^\bullet 39 times (K' only here and on pp. 682 and 685).")
add(689, "Note pour la page 1: 'Il prouve que K˙(X) devient ainsi'", "K with a raised typed dot (both scans)",
    "que $K'(X)$ devient", "symbol", "high", ("que $K'(X)$ devient", r"que $K^\bullet(X)$ devient"),
    "As the previous entry.")
add(689, "Note pour la page 1: 'que K˙(X) est même un λ-anneau'", "K with a raised typed dot (both scans)",
    "que $K'(X)$ est même", "symbol", "high", ("que $K'(X)$ est même", r"que $K^\bullet(X)$ est même"),
    "As the previous entries.")
add(689, "Note pour la page 1, last sentence: 'se débarasser de l'hypothèse'", "'débarasser' with one r (both scans)",
    "débarasser", "misprint_in_print", "high", None,
    "Spelling slip ('débarrasser'); the TeX keeps the printed reading; the second reading has 'débarrasser'.",
    corrected="débarrasser")
add(689, "Notes pour la page 11, note (*): '(sans hyperplan quasi-projectif, et dans le cas lisse relatif'",
    "'sans hyperplan quasi-projectif' (both scans)", "(sans hyperplan quasi-projectif,", "misprint_in_print", "medium",
    None,
    "The sense is 'without the quasi-projectivity hypothesis' (Mumford's result needs it, Jouanolou's does not). The TeX keeps the printed reading; the corrected layer already reads it so (RECONCILE_CODEX_6, SGA-SRC-001459).",
    corrected="(sans hypothèse quasi-projective,")
add(689, "Notes pour la page 11, note (**): 'DELIGNE et MANIN 17 avaient'",
    "bare '17' between spaces, no brackets in either scan (crops_686_690/w689_manin.png)", "MANIN 17", "misprint_in_print",
    "medium", None,
    "Citation of bibliography [17] without its brackets (the typist left the spaces; the brackets of this typescript are drawn by hand and were not added). The TeX keeps the printed reading, which is right for the diplomatic layer; RECONCILE_CODEX_6 SGA-SRC-001460 left this to the check of p. 689.",
    corrected="MANIN [17]")
add(689, "Notes pour la page 11, note (**): 'et même pour y = 1 dans 16 ,'",
    "bare '16' between spaces, no brackets in either scan (crops_686_690/w689_manin.png)", "dans 16,", "misprint_in_print",
    "medium", None, "As 'MANIN 17': citation of bibliography [16] without its brackets; the TeX keeps the printed reading.",
    corrected="dans [16],")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(len(F), "findings written to", OUT)
