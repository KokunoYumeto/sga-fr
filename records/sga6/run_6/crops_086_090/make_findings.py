import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b086_090"
OUT = RUN / "findings_086_090.json"

F = []


def add(page, where, scan, tex, kind, confidence, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


COMMA = "The TeX adds a comma between the two indices (the print's C_oX / C_oU, as on p. 85, fixed there)."
BOLD = ("The print has a plain 'a)' etc., not underlined (both scans), so the accepted bold-label convention "
        "does not cover it (as for \\textbf{N.B.}, pp. 66 and 76).")

# ---------------- p. 86
add(86, "1st paragraph, 'avec E et F ∈ ob C_oX , le noyau de u'",
    "C_oX without a comma between the indices (both scans)", r"\mathcal C_{0,X}",
    "punctuation", "high", r"\(F\in\Ob\mathcal C_{0,X}\), le noyau", r"\(F\in\Ob\mathcal C_{0X}\), le noyau", COMMA)
add(86, "1st paragraph, 'tels que f^*Ker(u) ∈ ob C_oU'",
    "C_oU without a comma (both scans)", r"\mathcal C_{0,U}",
    "punctuation", "high", r"\mathcal C_{0,U}", r"\mathcal C_{0U}", COMMA)
add(86, "display (*)",
    "0 → E^o → E^1 → ... → E^n → 0 with the three dots on the baseline (both scans)",
    r"E^1\longrightarrow\cdots\longrightarrow E^n",
    "symbol", "medium", r"E^1\longrightarrow\cdots\longrightarrow E^n", r"E^1\longrightarrow\ldots\longrightarrow E^n",
    "\\cdots sets the dots at mid-height (same kind of fix as pp. 49, 79, 80).")
add(86, "after (*), 'avec E^i ∈ ob C_oX pour 1 ≤ i ≤ n'",
    "C_oX without a comma (both scans)", r"\mathcal C_{0,X}",
    "punctuation", "high", r"E^i\in\Ob\mathcal C_{0,X}", r"E^i\in\Ob\mathcal C_{0X}", COMMA)
add(86, "'localement relevable', 'avec F ∈ ob C_oX admet localement une section'",
    "C_oX without a comma (both scans)", r"\mathcal C_{0,X}",
    "punctuation", "high", r"\mathcal C_{0,X}\) admet", r"\mathcal C_{0X}\) admet", COMMA)
add(86, "second diagram (the commutative triangle over U)",
    "label 'u' beside the diagonal arrow H_U → E_U and label 'U' above the horizontal arrow E_U → F_U "
    "(both scans; the U stands right under the u)",
    r"""\arrow[dl,"u"'] ... E_U \arrow[r,"U"] & F_U (printed reading kept)""",
    "misprint_in_print", "medium", None, None,
    "The horizontal arrow is u_U (as in the diagram of quasi-relevabilité on p. 87) and the diagonal arrow is the "
    "local lifting, which has no name; the typist's u_U came apart, its u one line up beside the diagonal. "
    "The TeX keeps the printed reading (both layers).",
    corrected="\\begin{tikzcd}\n& H_U \\arrow[d] \\arrow[dl]\\\\\nE_U \\arrow[r,\"u_U\"] & F_U\n\\end{tikzcd}")
add(86, "pp. 86-90 throughout: the site S",
    "S underlined (S̲) where it names the site: p. 86 'pour tout X ∈ ob S̲', 'de S̲/X'; p. 88 'S̲ le site des "
    "ouverts de S'; p. 89 'Soient S ∈ ob S̲'; p. 90 'X ∈ ob S̲/S'",
    r"plain S: '\(X\in\Ob S\)', '\(S\) le site des ouverts de \(S\)', 'Soient \(S\in\Ob S\)'",
    "underline", "medium", None, None,
    "Convention of the transcription, not a page fix (reported for pp. 84-85 in findings_081_085.json): the TeX "
    "drops the underline of S̲ while it writes C̲ as \\mathcal C and O̲ as \\mathcal O, so 'S ∈ ob S̲' (an object of "
    "the site) becomes \\(S\\in\\Ob S\\). One decision for the exposé.")

# ---------------- p. 87
add(87, "1st paragraph, 'avec F ∈ ob C_oX, l'ensemble des f'",
    "C_oX without a comma (both scans; the comma after X is the sentence's)", r"\mathcal C_{0,X}",
    "punctuation", "high", r"\mathcal C_{0,X}", r"\mathcal C_{0X}", COMMA)
add(87, "1st paragraph, 'avec F' ∈ ob C_oU tel que'",
    "C_oU without a comma (both scans)", r"\mathcal C_{0,U}",
    "punctuation", "high", r"\mathcal C_{0,U}", r"\mathcal C_{0U}", COMMA)
add(87, "'Cette condition équivaut à la suivante'",
    "new indented paragraph after '... est un raffinement de X.' (both scans)",
    r"run on in the same paragraph: 'raffinement de \(X\). Cette condition'",
    "other", "high", r"raffinement de \(X\). Cette condition", "raffinement de \\(X\\).\n\nCette condition",
    "The TeX joins two paragraphs of the print.")
add(87, "second diagram (G → H_U over E_U → F_U)",
    "a comma after F_U, right of the diagram (both scans), as after the first diagram ('F ,')",
    r"""E_U \arrow[r,"u_U"] & F_U (no comma)""",
    "punctuation", "high", "\"u_U\"] & F_U", "\"u_U\"] & F_U ,",
    "The comma is set inside the cell, as the TeX does for 'F ,' in the first diagram of the page.")
add(87, "1.3 Exemples, label 'a)'",
    "plain a) (not underlined, not bold)", r"\textbf{a)}",
    "font", "medium", r"\textbf{a)}", "a)", BOLD)

# ---------------- p. 88
add(88, "Example b), label", "plain b)", r"\textbf{b)}",
    "font", "medium", r"\textbf{b)}", "b)", BOLD)
add(88, "Example c), label", "plain c)", r"\textbf{c)}",
    "font", "medium", r"\textbf{c)}", "c)", BOLD)
add(88, "Example c), 'S le topos des G-ensembles (SGA 4 V 3.11) k un corps'",
    "no comma after '(SGA 4 V 3.11)' (both scans)", r"(SGA 4 V 3.11) \(k\) un corps (printed reading kept)",
    "misprint_in_print", "medium", None, None,
    "The enumeration 'Soient G un groupe, S le topos ..., k un corps (...), C la ...' lacks its comma before k. "
    "The TeX keeps the printed reading.",
    corrected=r"(SGA 4 V 3.11), \(k\) un corps")

# ---------------- p. 89
add(89, "Example d), label", "plain d)", r"\textbf{d)}",
    "font", "medium", r"\textbf{d)}", "d)", BOLD)
add(89, "label of Lemme 1.3.1",
    "'Lemme 1.3.1,' with a comma after the number (a tailed comma in both scans; the stops between the digits "
    "are round)",
    r"\textbf{Lemme 1.3.1.}",
    "misprint_in_print", "high", r"\textbf{Lemme 1.3.1.}", r"\textbf{Lemme 1.3.1,}",
    "The typist's comma for the label's full stop (cf. '7,1' on p. 84); the TeX silently corrects it (the bold "
    "label itself is accepted).",
    corrected=r"\textbf{Lemme 1.3.1.}")
add(89, "Lemme 1.3.1, 'Soit P un O_S-Module, Conditions équivalentes :'",
    "comma after 'Module', then a capital C (both scans)",
    r"\(\mathcal O_S\)-Module, Conditions équivalentes (printed reading kept)",
    "misprint_in_print", "medium", None, None,
    "The capital C shows that a full stop was meant ('Soit P un O_S-Module. Conditions équivalentes :'). "
    "The TeX keeps the printed reading.",
    corrected=r"\(\mathcal O_S\)-Module. Conditions équivalentes")
add(89, "Lemme 1.3.1 (i), 'le foncteur Hom(P,.) est exact'",
    "Hom underlined by its own short, close underline (Hom̲, the sheaf Hom), apart from the underline of the "
    "words and with '(P,.)' not underlined (both scans)",
    r"\(\Hom(P,\cdot)\) inside the \emph of the item (prints a plain Hom)",
    "underline", "high", r"\Hom(P", r"\underline{\Hom}(P",
    "The statement's underlining skips its formulas (P, M → P, (P,.)), so the underline of Hom is the notation "
    "Hom̲; the lemma needs the sheaf Hom for (i) ⇔ (iii). The file writes \\underline{\\Hom} elsewhere (6 times).")
add(89, "Lemme 1.3.1 (i), the place-holder in 'Hom(P,.)'",
    "a typed full stop on the baseline (both scans)", r"(P,\cdot)",
    "symbol", "low", r"(P,\cdot)", "(P,.)",
    "\\cdot raises the typed stop to mid-height (as the \\cdots fixes of pp. 49, 79, 80). Independent of the "
    "underline fix of the same formula (either order).")
add(89, "Proposition 1.4.1, the statement (opening)",
    "the statement is underlined by word groups from 'Soient S un site' to 'on suppose que H^n(G) est' on p. 89 "
    "(both scans)",
    r"\textbf{Proposition 1.4.1.} Soient \(S\) un site, ... (no \emph at all)",
    "underline", "high", r"\textbf{Proposition 1.4.1.} Soient", r"\textbf{Proposition 1.4.1.} \emph{Soient",
    "The underline of the whole statement is missing (block \\emph, as Lemme 1.3.1 on the same page). Goes with "
    "the next entry and with the p. 90 entry that closes the group: apply all three or none.")
add(89, "Proposition 1.4.1, the statement (end of p. 89)",
    "p. 89 ends '... on suppose que H^n(G) est' (underlined); 'de C_o-type fini (1.2)' is the first line of p. 90",
    r"on suppose que \(\Ho^n(G)\) est de \(\mathcal C_0\)-",
    "underline", "high", r"\(\Ho^n(G)\) est de \(\mathcal C_0\)-", "\\(\\Ho^n(G)\\) est}\n\\emph{de \\(\\mathcal C_0\\)-%",
    "Closes the group at the end of p. 89 and opens a second one that runs on into p. 90 (prints the same), so "
    "that the folio-90 marker can stand between the two groups (marker entry of p. 90). The % keeps 'C_0-type' "
    "one word: the line break after the hyphen now prints 'C_0- type'.")
add(89, "Proposition 1.4.1, 'Soient S un site, C une S-catégorie'",
    "plain C, not underlined (both scans), while C_o and C_S of the same statement keep their underline",
    r"\(\mathcal C\) une \(S\)-catégorie",
    "misprint_in_print", "medium", r"un site, \(\mathcal C\) une", r"un site, \(C\) une",
    "The typist left the category letter C (and the site S) unmarked in this statement; the TeX silently writes "
    "\\mathcal C. Independent of the underline edits.",
    corrected=r"un site, \(\mathcal C\) une")
add(89, "Proposition 1.4.1, 'strictement pleine de C; on suppose'",
    "plain C (both scans)", r"strictement pleine de \(\mathcal C\);",
    "misprint_in_print", "medium", r"pleine de \(\mathcal C\);", r"pleine de \(C\);",
    "As above.", corrected=r"pleine de \(\mathcal C\);")
add(89, "Proposition 1.4.1, 'localement quasi-relevable dans C (1.2)'",
    "plain C (both scans)", r"quasi-relevable dans \(\mathcal C\) (1.2)",
    "misprint_in_print", "medium", r"quasi-relevable dans \(\mathcal C\) (1.2)", r"quasi-relevable dans \(C\) (1.2)",
    "As above.", corrected=r"quasi-relevable dans \(\mathcal C\) (1.2)")

# ---------------- p. 90
add(90, "start of page",
    "p. 90 begins 'de C_o-type fini (1.2). Alors l'ensemble des X ∈ ob S/S ...'; p. 89 ends '... on suppose que "
    "H^n(G) est' (both scans)",
    r"'de \(\mathcal C_0\)-' ends the last line of page_089.tex (under the folio-89 marker); page_090.tex begins "
    r"'type fini (1.2).'",
    "marker", "high", None, None,
    "Page 90 really begins with 'de \\(\\mathcal C_0\\)-'. After the three underline edits of Proposition 1.4.1 "
    "(p. 89 opening and end, p. 90 closing): python -I move_marker.py 6 90 '\\emph{de \\(\\mathcal C_0\\)-' "
    "--before (single quotes; simulated on both layers: '... on suppose que \\(\\Ho^n(G)\\) est}' / marker / "
    "'\\emph{de \\(\\mathcal C_0\\)-%' / 'type fini (1.2). Alors ... raffinement de \\(S\\)}.'). Without those "
    "edits: python -I move_marker.py 6 90 'de \\(\\mathcal C_0\\)-' --before, then write a % after that hyphen in "
    "both layers ('de \\(\\mathcal C_0\\)-%'), as the line break prints 'C_0- type'.")
add(90, "Proposition 1.4.1, the statement (p. 90 part)",
    "'de C_o-type fini (1.2). Alors l'ensemble des X ∈ ob S/S vérifiant la propriété (P) ci-dessous est un "
    "raffinement de S.' underlined by word groups (both scans); '(P) : il existe ...' and the rest are not",
    r"no \emph", "underline", "high", r"raffinement de \(S\).", r"raffinement de \(S\)}.",
    "Closes the group opened at the end of p. 89 (see there); apply the three edits together, before the "
    "folio-90 marker move.")
add(90, "Proposition 1.4.1, 'l'ensemble des X ∈ ob S/S'",
    "S̲ with '/S' lowered as an index, S_{/S} (both scans), as S_{/X} on pp. 86-87",
    r"\(X\in\Ob S/S\)", "formula", "high", r"\Ob S/S", r"\Ob S_{/S}", "")
add(90, "(P), 'il existe un objet M de C_oX'",
    "C_oX without a comma (both scans)", r"\mathcal C_{0,X}",
    "punctuation", "high", r"\mathcal C_{0,X}", r"\mathcal C_{0X}", COMMA)
add(90, "'Démonstration. La marche est la suivante'",
    "only the word is underlined; the full stop stands after the underline (both scans)",
    r"\emph{Démonstration.}", "underline", "medium", r"\emph{Démonstration.}", r"\emph{Démonstration}.",
    "main.tex has \\emph{Démonstration.} 9 times and \\emph{Preuve.} 132 times and never the stop outside; "
    "SGA 5 (global item 75) moved it out ('\\emph{Preuve} :'). One decision for the volume may cover it.")
# The end of p. 90 ('que l'' belongs to p. 91) was reported in findings_091_095.json and that marker move is
# already in main.tex (17:36, both layers): not repeated here.

# ---------------- checks
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1 or "%%%%%%%%%%" in d["fix"]["old"]:
        ok = False
        print("BAD", d["page"], n, repr(d["fix"]["old"]))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "NOT OK", len(F), counts)
