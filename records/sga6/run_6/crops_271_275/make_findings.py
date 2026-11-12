"""Build findings_271_275.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b271_275"
OUT = RUN / "findings_271_275.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 271 ----------------
add(271, "start of page",
    "p. 271 begins 'y ⟼ rg_{k(x)} H^p(E ⊗^L_X k(y)) est localement constante d'après (5.5 (ii)).'; "
    "p. 270 ends '... soit exact sur Mod(U), et, sur U, la fonction' (both scans)",
    r"'\(y\mapsto\operatorname{rg}_{k(x)}H^p(E\otimes_X^{\mathrm L}k(y))\) est' ends the last line of page_270.tex "
    r"(under the folio-270 marker); page_271.tex begins 'localement constante'",
    "marker", "high", None,
    r"Page 271 really begins with the formula y ⟼ rg ... and 'est'. Split the last line of p. 270 before it: "
    r"python -I move_marker.py 6 271 '\(y\mapsto\operatorname{rg}_{k(' --before (simulated on both layers: "
    r"'... et, sur \(U\), la fonction ', the marker, '\(y\mapsto\operatorname{rg}_{k(x)}H^p(...)\) est' "
    r"(k(y) in the corrected layer), 'localement constante d'après ...'). The anchor stops before k(x)/k(y), so it "
    r"fits both layers.")

add(271, "first line (text now under the folio-270 marker): 'y ⟼ rg_{k(x)} H^p(E ⊗^L_X k(y)) est localement constante'",
    "rg_{k(x)}: the index of rg is k(x) (both scans; crops_271_275/c271_top.png, w282_a.png)",
    r"\operatorname{rg}_{k(x)} in the last line of page_270.tex (printed reading kept); the corrected layer has k(y)",
    "misprint_in_print", "high", None,
    "The rank of the k(y)-vector space H^p(E ⊗^L_X k(y)) is taken over k(y) (5.6 (i): x ⟼ rg_{k(x)} H^p(E ⊗ k(x))); "
    "x is the generic point of X, fixed before. The diplomatic layer keeps the printed reading; no edit. "
    "The text moves to p. 271 with the marker move above.",
    corrected=r"\operatorname{rg}_{k(y)}")

add(271, "Proposition 5.7, 'E ∈ ob D^b(f)_parf (4.2)'",
    "parf underlined: a short underline of its own below the lowered subscript, while the statement's word "
    "underlines leave 'E ∈ ob D^b(f)' and '(4.2)' plain (both scans; crops_271_275/c271_parf.png)",
    r"D^b(f)_{\parf} (plain parf)",
    "underline", "high",
    {"old": r"D^b(f)_{\parf}", "new": r"D^b(f)_{\uparf}"},
    r"Notation 4.2 (p. 251) distinguishes D(f)_parf (complexes parfaits) from D(f) with underlined parf "
    r"(d'amplitude parfaite finie), which the TeX writes \uparf (pp. 251, 257, 258); the '(4.2)' here refers to it. "
    r"X is quasi-compact, so the two agree (4.2), but the print writes the underlined one.")

add(271, "Proposition 5.7 (i), 'les H^i(Rf_*(E) ⊗^L_Y k(y) sont des espaces vectoriels'",
    "H^i(Rf_*(E) ⊗^L_Y k(y) sont: only the parenthesis of k(y) is closed, the one of H^i( is not (both scans; "
    "crops_271_275/c271_i.png, w282_a.png)",
    r"H^i(Rf_*(E)\otimes_Y^{\mathrm L}k(y))\) sont (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"k(y))\) sont", "new": r"k(y)\) sont"},
    "The edit restores the printed reading (removes one closing parenthesis).",
    corrected=r"H^i(Rf_*(E)\otimes_Y^{\mathrm L}k(y))")

add(271, "Proposition 5.7 (i), display 'y ⟼ Σ (-1)^i rg_{k(y)} H^i(Rf_*(E) ⊗^L_Y k(y)'",
    "the display ends 'k(y)': the parenthesis of H^i( is not closed (both scans; crops_271_275/c271_disp1.png)",
    r"...H^i(Rf_*(E)\otimes_Y^{\mathrm L}k(y)) (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"H^i(Rf_*(E)\otimes_Y^{\mathrm L}k(y))" + NL + r"\]",
     "new": r"H^i(Rf_*(E)\otimes_Y^{\mathrm L}k(y)" + NL + r"\]"},
    "Same omission as in the sentence before it. The edit restores the printed reading.",
    corrected=r"H^i(Rf_*(E)\otimes_Y^{\mathrm L}k(y))")

add(271, "Proposition 5.7 (ii), display 'y ⟼ rg_{k(y)} H^p(Rf_*(E) ⊗^L_Y k(y)).' before 'est constructible'",
    "a full stop after the display, although the sentence goes on with 'est constructible et semi-continue' "
    "(both scans; crops_271_275/c271_disp2.png, w282_b.png)",
    "no full stop (silently corrected)",
    "misprint_in_print", "medium",
    {"old": r"H^p(Rf_*(E)\otimes_Y^{\mathrm L}k(y))" + NL + r"\]",
     "new": r"H^p(Rf_*(E)\otimes_Y^{\mathrm L}k(y))." + NL + r"\]"},
    "A stray full stop inside the sentence 'La fonction ... est constructible'. The edit restores the printed stop "
    "in the diplomatic layer; the corrected reading has none.",
    corrected=r"H^p(Rf_*(E)\otimes_Y^{\mathrm L}k(y))")

add(271, "Proposition 5.7 (statement, items (i)-(iii))",
    "the statement is underlined word group by word group: 'Soient', 'un morphisme propre de schémas "
    "quasi-compacts', 'et' (also the 'et' of '(EGA III 7.7.5 et 7.9.4)'), 'Alors', 'sous réserve de validité de', "
    "'donc par exemple si', 'est projectif ou', 'si', 'est noethérien'; (i) 'Pour', 'les', 'sont des espaces "
    "vectoriels de rang fini sur', 'nuls sauf un nombre fini', 'et la fonction', 'est localement constante sur'; "
    "(ii), (iii) likewise (both scans)",
    "the statement in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé III follows the Exposé II pattern of GLOBAL_ISSUES 82 (as reported for pp. 222 and 227): not itemized, "
    "for the scripted per-exposé decision.")

add(271, "proof of 5.6, last line: 'au foncteur T_{-p} = H^p(E ⊗ . ) .'",
    "the place-holder is a typed full stop on the baseline (both scans; crops_271_275/c271_Tp.png)",
    r"H^p(E\otimes\,\cdot\,)",
    "symbol", "low",
    {"old": r"H^p(E\otimes\,\cdot\,)", "new": r"H^p(E\otimes\,.\,)"},
    r"\cdot raises the typed stop to mid-height; same kind of entry as (P,\cdot) -> (P,.) on p. 89 (applied) and "
    r"pp. 117, 136.")

# ---------------- p. 272 ----------------
add(272, "Preuve of 5.7, before 'L'assertion (i) (resp. (ii)) résulte'",
    "after 'Rf_*(E) est un complexe parfait.' (a short line) a blank of about two lines, then 'L'assertion (i) "
    "(resp. (ii)) résulte' starts a new line, indented, and the next line 'donc de (5.5 (i)) ...' starts at the "
    "margin (a pasted-in strip; both scans)",
    "one paragraph: 'complexe parfait. L'assertion (i) ...'",
    "other", "low",
    {"old": "complexe parfait. L'assertion (i)", "new": "complexe parfait." + NL + NL + "L'assertion (i)"},
    "The print begins a new indented line after the gap; low because the gap and the indent come from the "
    "paste-up of a corrected strip.")

add(272, "Remarques 5.8 a), 'On peut montrer (cf. (EGA III 6 et (IV 3.1.0) que pour f plat'",
    "(cf. (EGA III 6 et (IV 3.1.0) que: three opening parentheses, one closing (both scans; "
    "crops_271_275/c272_cf.png, w283_cf.png)",
    "(cf. (EGA III 6 et (IV 3.1.0) que (printed reading kept, both layers)",
    "misprint_in_print", "medium", None,
    "Two closing parentheses are missing. The TeX keeps the printed reading; the corrected layer has it too. "
    "Where the two parentheses belong is a guess (each reference in its own parentheses, as '(5.5 (ii) et (iii)) "
    "et (5.2 (iv))' on p. 271).",
    corrected="(cf. (EGA III 6) et (IV 3.1.0)) que")

# ---------------- p. 273 ----------------
add(273, "start of page",
    "p. 273 begins 'b) On peut développer pour les espaces analytiques complexes'; p. 272 ends 'où E_y = "
    "Li_y^*(E) (resp. i_y^*(E)).' and blank space (both scans)",
    r"'\item On' is the last line of page_272.tex (under the folio-272 marker); page_273.tex begins 'peut "
    r"développer'",
    "marker", "high", None,
    r"Page 273 really begins with item b). Move the folio-273 marker above that line: python -I move_marker.py 6 "
    r"273 '\item On' --before (simulated on both layers: '... (resp. \(i_y^*(E)\)).', the marker, '\item On', "
    r"'peut développer ...').")

add(273, "Remarque 5.8 b), display 'Rf_*(E) ⊗^L M) ⟶ Rf_*(E ⊗^L_Y M)'",
    "the left side ends 'M)' with a closing parenthesis that nothing opens (both scans; "
    "crops_271_275/c273_disp.png, w284_a.png)",
    r"Rf_*(E)\otimes^{\mathrm L}M)\longrightarrow (printed reading kept)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the corrected layer already has it without the parenthesis.",
    corrected=r"Rf_*(E)\otimes^{\mathrm L}M\longrightarrow Rf_*(E\otimes_Y^{\mathrm L}M)")

add(273, "Remarque 5.8 b), 'est un isomorphime (l'hypothèse sur X'",
    "isomorphime (both scans)",
    "isomorphime (printed reading kept)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed reading; the corrected layer already has 'isomorphisme'.",
    corrected="isomorphisme")

add(273, "Remarque 5.8 b), before 'A la différence de l'énoncé 1)'",
    "'... donc que Rf_* est défini sur D(X)).' ends a short line; 'A la différence de l'énoncé 1), l'énoncé 2) est "
    "essentiellement trivial,' starts an indented new paragraph (both scans)",
    r"same paragraph: 'défini sur \(D(X)\)). A la différence'",
    "other", "high",
    {"old": r"sur \(D(X)\)). A la différence", "new": r"sur \(D(X)\))." + NL + NL + "A la différence"},
    "Missing paragraph break (inside item b)).")

add(273, "heading of the bibliography",
    "BIBLIOGRAPHIE: typed capitals, underlined (both scans)",
    r"\subsection*{Bibliographie}",
    "word", "medium",
    {"old": r"\subsection*{Bibliographie}", "new": r"\subsection*{BIBLIOGRAPHIE}"},
    "As the p. 220 heading (findings_216_220) and pp. 19, 158; the missing underline of a section title is accepted.")

add(273, "bibliography entry [1], title",
    "'Ein Theorem der Analytischen Garbentheorie ...': plain type, not underlined (both scans)",
    r"\emph{Ein Theorem der Analytischen Garbentheorie}",
    "font", "high",
    {"old": r"\emph{Ein Theorem der Analytischen Garbentheorie}", "new": "Ein Theorem der Analytischen Garbentheorie"},
    "The typescript neither underlines nor italicizes the titles; same fix as the bibliographies of pp. 19 and 159 "
    "(applied).")

add(273, "bibliography entry [H], title",
    "'Residues and Duality': plain type, not underlined (both scans)",
    r"\emph{Residues and Duality}",
    "font", "high",
    {"old": r"\emph{Residues and Duality}", "new": "Residues and Duality"},
    "As entry [1].")

add(273, "bibliography entry [T.F], title",
    "'Théorie des faisceaux': plain type, not underlined (both scans)",
    r"\emph{Théorie des faisceaux}",
    "font", "high",
    {"old": r"\emph{Théorie des faisceaux}", "new": "Théorie des faisceaux"},
    "As entry [1].")

add(273, "footnote (1), 'C'est d'ailleurs dans ce oadre que ces propriétés'",
    "oadre: a closed round o, unlike the open c of 'ce' and 'ces' beside it (both scans; "
    "crops_271_275/c273_oadre.png, w284_oadre.png)",
    "ce cadre que (silently corrected)",
    "misprint_in_print", "high",
    {"old": "ce cadre que", "new": "ce oadre que"},
    "A typing error, not a filled c: the letter has the shape of the typewriter's o. The edit restores the printed "
    "reading.",
    corrected="cadre")

# ---------------- p. 274 ----------------
add(274, "exposé heading and title",
    "EXPOSE IV in typed capitals with a single underline and no full stop, on its own line; then the title "
    "GROUPES DE GROTHENDIECK DES TOPOS ANNELES in capitals with a double underline (both scans)",
    r"\section*{Exposé IV. Groupes de Grothendieck des topos annelés}",
    "word", "medium",
    {"old": r"\section*{Exposé IV. Groupes de Grothendieck des topos annelés}",
     "new": r"\section*{\underline{EXPOSÉ IV}\\[3pt] \underline{\underline{GROUPES DE GROTHENDIECK DES TOPOS ANNELÉS}}}"},
    "Same form as the applied Exposé II and III headings (main.tex: \\section*{\\underline{EXPOSÉ III}\\\\[3pt] "
    "\\underline{\\underline{CONDITIONS DE FINITUDE RELATIVES}}}); É keeps the TeX's accent (rule for typed capitals).")

add(274, "author line",
    "par L. ILLUSIE: the name in capitals, the whole line underlined (both scans)",
    "par L. Illusie",
    "word", "medium",
    {"old": "par L. Illusie", "new": r"\underline{par L. ILLUSIE}"},
    "As the applied author lines of pp. 78, 160 and 222.")

add(274, "1.1, 'Soit C une catégorie triangulée.'",
    "'triangulée' underlined (both scans)",
    "une catégorie triangulée. (plain)",
    "underline", "high",
    {"old": "une catégorie triangulée. Rappelons", "new": r"une catégorie \emph{triangulée}. Rappelons"},
    r"\emph is the file's command for underlined words here (\emph{additive} in the same paragraph).")

add(274, "statements of Exposé IV: Lemme 1.2 here, Lemmes 1.3 and 1.4 on p. 275",
    "the statements are underlined word group by word group: Lemme 1.2 'Soient', 'une catégorie triangulée', 'et', "
    "a) 'Pour tout', 'on a', 'Si', 'sont des objets de', 'tels qu'on ait', 'alors on a', b) 'Supposons qu'il existe', "
    "'tel que', 'soit représen-table', 'Alors on a'; Lemme 1.3 'Soient', 'une catégorie triangulée', 'une "
    "sous-catégorie épaisse', 'Les foncteurs d'inclusion et de passage au quotient définissent une suite exacte'; "
    "Lemme 1.4 'Soient', 'une catégorie additive', 'resp.', 'abélienne', 'et', 'une fonction additive', 'sur', "
    "'Pour', 'on a' (both scans)",
    "the statements in roman (no \\underline, no \\emph)",
    "underline", "high", None,
    "Exposé IV continues the Exposé II/III pattern of GLOBAL_ISSUES 82: not itemized; the scripted per-exposé "
    "decision should include Exposé IV.")

# ---------------- p. 275 ----------------
add(275, "start of page",
    "p. 275 begins with the display ∐_{i≥0} L[2ni] ≃ L ⊕ (∐_{i≥0} L[2ni])[2n] ,; p. 274 ends 'Pour b), il suffit de "
    "remarquer qu'on a' (both scans)",
    "page_275.tex begins with the line 'remarquer qu'on a' under the folio-275 marker",
    "marker", "high", None,
    r"'remarquer qu'on a' ends p. 274: move the folio-275 marker down one line, below it and above the display: "
    r"python -I move_marker.py 6 275 '\[' (simulated on both layers: '... il suffit de', 'remarquer qu'on a', the "
    r"marker, '\[', the display).")

add(275, "1.5, 'Soient C une catégorie abélienne et A une sous-catégorie pleine'",
    "'abélienne' underlined (both scans)",
    "une catégorie abélienne et (plain)",
    "underline", "high",
    {"old": "une catégorie abélienne et", "new": r"une catégorie \emph{abélienne} et"},
    r"As 'triangulée' in 1.1 (p. 274); \emph{additive} in the same paragraph.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

# checks
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"]:
        bad += 1
        print("BAD", d["page"], n, repr(fx["old"]))
print(len(F), "findings;", bad, "bad olds")
from collections import Counter
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(271, 276):
    print(p, c[(p, False)], "/", c[(p, True)])
