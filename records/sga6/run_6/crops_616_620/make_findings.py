import json, pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
OUT = RUN / "findings_616_620.json"

F = []

# ---------------- p. 616 ----------------
F.append({
    "page": 616,
    "where": "heading and title of Exposé XIII",
    "scan": "two blocks: 'E X P O S E  XIII' in typed capitals, letter-spaced, single underline, no full stop, at the left; then the centred title 'LES THEOREMES DE FINITUDE POUR LE FONCTEUR DE PICARD' in typed capitals on one line with a double underline (both scans; b616_620/page_616_s1.png, crops_616_620/wit_p627_half.png)",
    "tex": r"\section*{Expos\'e XIII. Les th\'eor\`emes de finitude pour le foncteur de Picard}: number and title run together with a full stop, the title in small letters, no underline",
    "kind": "word",
    "confidence": "medium",
    "fix": {
        "old": r"\section*{Expos\'e XIII. Les th\'eor\`emes de finitude pour le foncteur de Picard}",
        "new": r"\section*{\underline{EXPOS\'E XIII}\\[3pt] \underline{\underline{LES TH\'EOR\`EMES DE FINITUDE POUR LE FONCTEUR DE PICARD}}}",
    },
    "note": r"Same form as the headings of Exposés III and IV in main.tex and those reported for Exposés VIII, IX, X and XII (findings_466_470, 496_500, 516_520, 591_595), in the form \section*{\underline{EXPOSÉ X}\\[3pt] \underline{\underline{...}}}; É and È keep the TeX's accents (rule for typed capitals: the print has EXPOSE, THEOREMES), written with the line's own \'E, \`E. The print has the title on one line; \underline cannot break a line, so if the build reports it overfull at \section* size, split it as the two-line title of Exposé XII. Independent of the author-line entry.",
})
F.append({
    "page": 616,
    "where": "author line of the heading",
    "scan": "'par S. KLEIMAN': the name in typed capitals, the whole line underlined (both scans; b616_620/page_616_s1.png, crops_616_620/wit_p627_half.png)",
    "tex": "par S. Kleiman (in a center environment, no underline)",
    "kind": "word",
    "confidence": "medium",
    "fix": {"old": "par S. Kleiman", "new": r"\underline{par S. KLEIMAN}"},
    "note": r"As the applied author lines (\underline{par P. BERTHELOT}; \underline{par O. Jussila}, p. 519; \underline{par M. Raynaud (rédigé par S. Kleiman)}, p. 595). Independent of the heading entry.",
})
F.append({
    "page": 616,
    "where": "the structure sheaf O_X, pp. 616-619 (convention of the Exposé XIII transcription, reported once; 15 places: p. 616 three, p. 617 four, p. 618 three, p. 619 five)",
    "scan": "a plain typed capital O, not underlined, on every page: p. 616 'ample O_X(1)', Déf. 1.1 'F, O_X(1) est engendré', 1.3 (ii) 'H^o(O_X(1))'; p. 617 'σ ∈ H^o(O_X(1))' and both diagrams; p. 618 'M⊗_k O_X' and the diagram; p. 619 (1.5.1) (i) twice, (iii), (1.5.2), 1.6 (i). The only underlined O is in the footnote of p. 616, 'section donnée de O̲_X(1)' (both scans; crops_616_620/p616_ox_a.png to p616_ox_d.png, wit_p627_half.png)",
    "tex": r"\mathcal O_X in all 16 places (script O), the footnote included",
    "kind": "font",
    "confidence": "medium",
    "fix": None,
    "note": r"CONVENTION, not itemized: the TeX writes \mathcal O for the print's plain typed O, as in SGA 5 Exposé VII (GLOBAL_ISSUES 89 (f)); the footnote's underlined O falls under the pending underlined-O decision. Three examples in the plain form: p. 616 'ample $\mathcal O_X(1)$.' -> 'ample $O_X(1)$.'; p. 618 '\(M\otimes_k\mathcal O_X\)' -> '\(M\otimes_k O_X\)'; p. 619 'engendré par \(H^0(\mathcal O_X(1))\).' -> 'engendré par \(H^0(O_X(1))\).'",
})

# ---------------- p. 617 ----------------
F.append({
    "page": 617,
    "where": "diagram for (ii), bottom row, right-hand term",
    "scan": "H^o(G(n+1) with only one closing parenthesis, nothing after it (both scans; crops_616_620/p617_gn1.png, wit_p628_half.png)",
    "tex": r"H^0(G(n+1) \arrow[d]",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "H^0(G(n+1))",
    "note": "Typing error of the print (unbalanced parenthesis). The diplomatic TeX keeps the printed reading.",
})

# ---------------- p. 618 ----------------
F.append({
    "page": 618,
    "where": "proof of 1.4 (i): 'Donc H^q(F(m-q)) ⥲ H^q(F(m-q+1)) ⥲ H^q(F(m-q+2)) ⥲ ..., mais'",
    "scan": "three typed full stops on the baseline after the last arrow, '..., mais' (both scans; b616_620/page_618_s2.png, crops_616_620/wit_p629_half.png)",
    "tex": r"\xrightarrow{\sim}\cdots\), mais",
    "kind": "symbol",
    "confidence": "medium",
    "fix": {
        "old": r"H^q(F(m-q+2))\xrightarrow{\sim}\cdots",
        "new": r"H^q(F(m-q+2))\xrightarrow{\sim}\ldots",
    },
    "note": r"\cdots sets the dots at mid-height (typed baseline stops written \cdots: the same fix as SGA 6 pp. 49, 79, 80 and the Exposé V item, GLOBAL_ISSUES 87). Same on p. 619.",
})
F.append({
    "page": 618,
    "where": "proof of 1.4 (i): 'les deux groupes extrêmes sont 0 pour q ≥ 2 et n ≥ m-(q-1) par 2.3 (i).'",
    "scan": "par 2.3 (i). (both scans; crops_616_620/p618_ref23.png, wit_p629_half.png)",
    "tex": "par 2.3 (i).",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "1.3 (i)",
    "note": "Wrong reference number of the print: the vanishing of H^{q-1}(G(n)) and H^q(G(n)) for the m-regular G is Proposition 1.3 (i) (G is n-regular for every n ≥ m); Lemme 2.3 (p. 626) is about the coefficients a_r, e_r of Hilbert polynomials. The same slip on p. 619 ('2.3 (ii)' for 1.3 (ii)). The diplomatic TeX keeps the printed reading.",
})

# ---------------- p. 619 ----------------
F.append({
    "page": 619,
    "where": "first line: 'Si n ≥ m, alors β_n est surjectif par 2.3 (ii)'",
    "scan": "par 2.3 (ii) (both scans; crops_616_620/p619_ref23.png, wit_p630_half.png)",
    "tex": "par 2.3 (ii);",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "1.3 (ii)",
    "note": "Wrong reference number of the print: the surjectivity of β_n : H^0(G(n))⊗H^0(O_X(1)) → H^0(G(n+1)) for the m-regular G is Proposition 1.3 (ii); Lemme 2.3 (p. 626) is about Hilbert-polynomial coefficients. As '2.3 (i)' on p. 618. The diplomatic TeX keeps the printed reading.",
})
F.append({
    "page": 619,
    "where": "'Par conséquent, H^1(F(n-1)) ⥲ H^1(F(n)) ⥲ ... ⥲ 0.'",
    "scan": "three typed full stops on the baseline between the arrows (both scans; crops_616_620/p619_dots.png, wit_p630_half.png)",
    "tex": r"\xrightarrow{\sim}\cdots\xrightarrow{\sim}0",
    "kind": "symbol",
    "confidence": "medium",
    "fix": {
        "old": r"\xrightarrow{\sim}\cdots\xrightarrow{\sim}0",
        "new": r"\xrightarrow{\sim}\ldots\xrightarrow{\sim}0",
    },
    "note": r"As p. 618: \cdots sets the dots at mid-height.",
})
F.append({
    "page": 619,
    "where": "'; donc ↦ n^1(F(n)) est strictement décroissant depuis h^1(F(m-1))'",
    "scan": "'donc |—> n^1(F(n))': no variable before the arrow, and n where h is meant (both scans; crops_616_620/p619_mapsto.png, w619_mapsto.png)",
    "tex": r"donc \(\mapsto n^1(F(n))\) est",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"n\mapsto h^1(F(n))",
    "note": "Typing error of the print: the strictly decreasing function is n ↦ h^1(F(n)). The diplomatic TeX keeps the printed reading.",
})
F.append({
    "page": 619,
    "where": "(1.5.2): 'si F_i désigne la restriction de F au schéma des zéros de σ_1,...,σ_i, alors h^o(F_i(-1)) ≤ b_i'",
    "scan": "σ_1,...,σ_i: the last index is a dotted i (as in F_i and b_i on the same line), not 1 (both scans; crops_616_620/p619_sig_a.png, w619_sig_a.png)",
    "tex": r"\sigma_1,\ldots,\sigma_1",
    "kind": "formula",
    "confidence": "high",
    "fix": {
        "old": r"\sigma_1,\ldots,\sigma_1\), alors \(h^0(F_i(",
        "new": r"\sigma_1,\ldots,\sigma_i\), alors \(h^0(F_i(",
    },
    "note": "Transcription error: index 1 for the print's i. The same in 1.6 (i) (next entry).",
})
F.append({
    "page": 619,
    "where": "Proposition 1.6 (i): 'au schéma des zéros de σ_1,...,σ_i, alors h^o(F_{σ,i}(-1)) ≤ b_i'",
    "scan": "σ_1,...,σ_i: the last index is a dotted i, not 1 (both scans; crops_616_620/p619_sig_b.png, w619_sig_b.png)",
    "tex": r"\sigma_1,\ldots,\sigma_1",
    "kind": "formula",
    "confidence": "high",
    "fix": {
        "old": r"\sigma_1,\ldots,\sigma_1\), alors \(h^0(F_{\sigma,i}",
        "new": r"\sigma_1,\ldots,\sigma_i\), alors \(h^0(F_{\sigma,i}",
    },
    "note": "Transcription error: index 1 for the print's i, as in (1.5.2).",
})

# ---------------- p. 620 ----------------
F.append({
    "page": 620,
    "where": "first sentence: 'soient S' l'espace affine A^N_k dont les k-points'",
    "scan": "a double-struck A (the typed A with a doubled left stroke), with N above and k below (both scans; crops_616_620/p620_AN.png, w620_AN.png)",
    "tex": r"\(A_k^N\)",
    "kind": "font",
    "confidence": "high",
    "fix": {"old": r"\(A_k^N\)", "new": r"\(\mathbb A_k^N\)"},
    "note": r"Plain A for the print's double-struck A; \mathbb as in the file's \mathbb Z (p. 616).",
})
F.append({
    "page": 620,
    "where": "first sentence: 'et T l'ouvert de S correspondant aux suites F-régulières'",
    "scan": "'l'ouvert de S' with no prime (both scans; crops_616_620/p620_TS.png, w620_TS.png), in the sentence that defines S' as the affine space of the sequences σ",
    "tex": r"l'ouvert de \(S\) correspondant",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": r"\(S'\)",
    "note": "Typing error of the print: T is the open set of the affine space S' of the sequences σ; no S is defined in § 1. The diplomatic TeX keeps the printed reading.",
})
F.append({
    "page": 620,
    "where": "Lemme 1.7: 'Soit 0 → F(1) → F → G → 0 une suite exacte sur X'",
    "scan": "F(1) without a minus sign (both scans; crops_616_620/p620_F1.png, w620_F1.png)",
    "tex": r"\(0\to F(1)\to F\to G\to0\)",
    "kind": "misprint_in_print",
    "confidence": "high",
    "fix": None,
    "corrected": "F(-1)",
    "note": "Typing error of the print: the proof uses χ(G(n)) = χ(F(n)) − χ(F(n−1)), i.e. the sequence 0 → F(−1) → F → G → 0 of 1.2 and 1.4. The diplomatic TeX keeps the printed reading.",
})

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT, len(F))
