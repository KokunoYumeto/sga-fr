"""Build findings_016_020.json for the SGA 6 pp. 16-20 scan check and verify every fix's old (exactly once per page)."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b016_020"
OUT = RUN / "findings_016_020.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 16
add(16, "§6, paragraph 'Dans le point de vue proposé dans le Séminaire', first underlined run",
    "five separately underlined phrases: 'Dans le point de vue proposé dans le Séminaire', 'une théorie des "
    "intersections maniable', 'sur les schémas noethériens', 'pas nécessairement réguliers', 'doit consister en "
    "l'étude combinée des invariants contravariants'; the commas and the letter X are not underlined (both scans)",
    "one \\uline{...} running through the commas and $X$",
    "underline", "high",
    {"old": "\\uline{Dans le point de vue propos\\'e dans le S\\'eminaire, une th\\'eorie des intersections maniable, "
            "sur les sch\\'emas noeth\\'eriens $X$ pas n\\'ecessairement r\\'eguliers, doit consister en l'\\'etude "
            "combin\\'ee des invariants contravariants}",
     "new": "\\uline{Dans le point de vue propos\\'e dans le S\\'eminaire}, \\uline{une th\\'eorie des intersections "
            "maniable}, \\uline{sur les sch\\'emas noeth\\'eriens} $X$ \\uline{pas n\\'ecessairement r\\'eguliers}, "
            "\\uline{doit consister en l'\\'etude combin\\'ee des invariants contravariants}"},
    "The typescript stops the underline at each comma and at X and restarts it after (as SGA 7 II global items "
    "48/73).")

add(16, "same paragraph, last underlined run",
    "'qui jouent des rôles de nature essentiellement différente', 'et dont les propriétés se complètent "
    "mutuellement' underlined separately; the comma between them and the final full stop are not underlined",
    "\\uline{qui jouent ... diff\\'erente, et dont ... mutuellement.} (comma and full stop inside)",
    "underline", "high",
    {"old": "\\uline{qui jouent des r\\^oles de nature essentiellement diff\\'erente, et dont les propri\\'et\\'es se "
            "compl\\`etent mutuellement.}",
     "new": "\\uline{qui jouent des r\\^oles de nature essentiellement diff\\'erente}, \\uline{et dont les "
            "propri\\'et\\'es se compl\\`etent mutuellement}."},
    "Same form as the previous finding.")

add(16, "after (6.4), 'induisant sur le sous-groupe Gr_o(X) = Filt_o K.(X)'",
    "Filt_o K.(X) (both scans)",
    "\\Fil_0K_\\bullet(X) (\\Fil is \\operatorname{Fil}: prints 'Fil')",
    "word", "high",
    {"old": "\\Fil_0K_\\bullet(X)", "new": "\\operatorname{Filt}_0K_\\bullet(X)"},
    "The print types Filt; the file writes \\operatorname{Filt} on pp. 3-5. Page 15 has the same \\Fil for the "
    "print's Filt (main.tex lines 480, 482: \\Fil_iK_\\bullet(X), (6.1) \\Fil^i, \\Fil_j, \\Fil_{j-i}; read on the "
    "DjVu witness p. 26).")

# ---------------------------------------------------------------- p. 17
add(17, "§7, 'théorèmes de finitude pour le groupe de Picard (annoncés sans démonstration dans [6])'",
    "dans [6]) (both scans)",
    "[6] (printed reading kept)",
    "misprint_in_print", "medium", None,
    "Wrong reference number: in the printed bibliography (p. 19) [6] is W. Shih, Séminaire de Topologie à l'IHES; "
    "the finiteness theorems were announced without proof in FGA, which is [5] ('Technique de descente ...', "
    "'dans Fondements de la Géométrie Algébrique'), as the same paragraph's 'se rattachant à [5]'. Exp. XIII cites "
    "the same commentaries of FGA 'p. C 07--C 11' (main.tex line 15180). Corrected layer still has [6].",
    corrected="[5]")

add(17, "§7, 'Le seul résultat réfractaire aux méthodes de Kleiman ... est [6, C-07 (i)]'",
    "[6, C-07 (i)] (both scans)",
    "[6, C-07 (i)] (printed reading kept)",
    "misprint_in_print", "medium", None,
    "C-07 is a page of FGA's commentaries, i.e. bibliography item [5], not [6] (W. Shih). Correct together with the "
    "previous finding and the offset citations of p. 14 (see the coordinator message).",
    corrected="[5, C-07 (i)]")

add(17, "§7, 'dont la démonstration et certains raffinements (...) occupe l'exposé XII'",
    "occupe",
    "occupe (printed reading kept)",
    "misprint_in_print", "low", None,
    "Agreement slip: the subject 'la démonstration et certains raffinements' is plural. The corrected layer also "
    "has 'occupe'; decide whether the corrected edition mends the grammar.",
    corrected="occupent")

# ---------------------------------------------------------------- p. 18
add(18, "start of page",
    "p. 18 begins 'posé est logiquement indépendant de tous les autres.' (second half of 'ex-posé', hyphenated "
    "across the page break)",
    "'cet expos\\'e est' is the last line of page_017.tex (under the folio-17 marker); page_018.tex begins "
    "'logiquement'",
    "marker", "high", None,
    "Page 18 really begins with 'posé est'. Split the word at the marker: python -I move_marker.py 6 18 "
    "\"pos\\'e est\" --before, then in both layers replace 'cet ex\\n%%%%%%%%%%  scan idx 31' by "
    "'cet ex%\\n%%%%%%%%%%  scan idx 31' so that 'exposé' stays one word (as isomor%|phisme, SGA 7 I). Simulated on "
    "both layers: '... se rattachant \\`a [5]~; cet ex%' / marker / 'pos\\'e est' / 'logiquement ...'.")

add(18, "(7.2)",
    "det*: Parfis(X) ⟶ Inv(X): 'Parfis' typed on the line and underlined as one word (both scans)",
    "\\underline{\\Parf_{\\mathrm{is}}}(X) ('is' as a subscript)",
    "formula", "high",
    {"old": "\\underline{\\Parf_{\\mathrm{is}}}", "new": "\\underline{\\operatorname{Parfis}}"},
    "The letters 'is' stand on the baseline at full size, unlike the lowered indices of the same page (L_i).")

add(18, "(7 3), left side",
    "det*(L.) ≃ ... : a typed full stop after L, in its own character cell before ')' (both scans; the same "
    "position as in 'pour un complexe L.' of the line before)",
    "\\det^*(L)",
    "symbol", "medium",
    {"old": "\\det^*(L)\\simeq", "new": "\\det^*(L_\\bullet)\\simeq"},
    "The file writes the print's K. as K_\\bullet. The dot touches the end of the L's foot in both scans, but it "
    "takes the cell between L and the parenthesis. The running text 'pour un complexe $L$. born\\'e' prints the same "
    "'L.' and may stay (or become $L_\\bullet$ for consistency).")

add(18, "equation number (7 3)",
    "(7 3): no full stop between 7 and 3 (both scans; the space is there)",
    "\\tag{7 3} (printed reading kept)",
    "misprint_in_print", "medium", None,
    "The corrected layer also has \\tag{7 3}; the correct number is (7.3).",
    corrected="\\tag{7.3}")

add(18, "heading of the bibliography (printed at the top of p. 19; the TeX has it under the folio-18 marker)",
    "BIBLIOGRAPHIE: capitals, single underline (both scans)",
    "\\section*{Bibliographie}",
    "word", "medium",
    {"old": "\\section*{Bibliographie}", "new": "\\section*{\\underline{BIBLIOGRAPHIE}}"},
    "Filed under p. 18 because the line now stands in page_018.tex: apply before the marker move of p. 19. Same "
    "form as the applied p. 1 fix \\section*{\\underline{Exposé 0}}.")

# ---------------------------------------------------------------- p. 19
add(19, "start of page",
    "p. 19 begins with the heading BIBLIOGRAPHIE; p. 18 ends '... dans les exposés I à XI.'",
    "\\section*{Bibliographie}, \\begin{enumerate}[...] and '\\item M.' are the last lines of page_018.tex (under "
    "the folio-18 marker); page_019.tex begins 'Atiyah et F. Hirzebruch'",
    "marker", "high", None,
    "Page 19 really begins with the heading. Move the folio-19 marker above it: python -I move_marker.py 6 19 "
    "\"\\section*{Bibliographie}\" --before (simulated on both layers: marker after 'expos\\'es I \\`a XI.' and its "
    "blank line; '\\item M.' and 'Atiyah' then follow each other on two lines of the same item).")

for title in ["Vector bundles and homogeneous spaces",
              "Le th\\'eor\\`eme de Riemann--Roch",
              "Ein Theorem der analytischen Garbentheorie",
              "Classes de faisceaux et th\\'eor\\`eme de Riemann--Roch",
              "Technique de descente et th\\'eor\\`emes d'existence en G\\'eom\\'etrie Alg\\'ebrique",
              "Fondements de la G\\'eom\\'etrie Alg\\'ebrique",
              "The Riemann--Roch theorem for analytic embeddings"]:
    add(19, "bibliography, title '" + title.replace("\\'e", "é").replace("\\`e", "è") + "'",
        "title typed plain, not underlined (both scans)",
        "\\emph{" + title + "}",
        "font", "high",
        {"old": "\\emph{" + title + "}", "new": title},
        "The bibliography of p. 19 underlines none of its titles; the TeX sets all seven in italics.")

add(19, "[1], 'vol. 3, Différential Geometry p. 7-38, 1961.'",
    "Différential Geometry p. 7-38 (no comma after Geometry, at the line end; both scans)",
    "Diff\\'erential Geometry, p. 7--38",
    "punctuation", "high",
    {"old": "Geometry, p.", "new": "Geometry p."},
    "The TeX adds a comma.")

add(19, "[1], 'Différential Geometry'",
    "Différential (accented é in the English title; both scans)",
    "Diff\\'erential (printed reading kept)",
    "misprint_in_print", "high", None,
    "The AMS volume is 'Differential Geometry' (Proc. Sympos. Pure Math. 3, 1961).",
    corrected="Differential")

add(19, "[2], 'A. Borel et J.P. Serre'",
    "J.P. Serre (no hyphen; both scans)",
    "J.-P. Serre",
    "punctuation", "high",
    {"old": "J.-P. Serre", "new": "J.P. Serre"},
    "The TeX adds a hyphen to the initials.")

add(19, "[2], 'Bull. Soc. math France'",
    "Bull. Soc. math France (no full stop after 'math', at the line end; both scans)",
    "Bull. Soc. math. France (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "Soc. math. France", "new": "Soc. math France"},
    "The abbreviation 'math' lacks its full stop in the print; the TeX supplies it.",
    corrected="Soc. math. France")

add(19, "bibliography (throughout): page and year ranges",
    "typewriter hyphen: p. 7-38, p. 97-136, p. 5-64, 1957-1962, p. 151 - 166",
    "p. 7--38, p. 97--136, p. 5--64, 1957--1962, p. 151--166",
    "punctuation", "medium", None,
    "Convention of the transcription, not a page fix: number ranges are written with an en dash (--) where the "
    "typescript has a hyphen; main.tex has 28 digit--digit ranges (e.g. the p. 220 bibliography: 1963--64, "
    "p. 2974--2976). Same question as the joint-name dash (handled globally): one pass in the diplomatic layer.")

add(19, "end of page_019.tex: heading 'Appendice à l'Exposé 0 : RRR'",
    "not printed: p. 20 has only the running head '0 App : RRR' at the top right; p. 19 ends with item [7]",
    "\\section*{Appendice à l'Exposé 0 : RRR}",
    "extra", "low",
    {"old": "\\section*{Appendice à l'Exposé 0 : RRR}\n", "new": ""},
    "Editorial heading made from the running head (running heads are not transcribed elsewhere). Apply only if the "
    "diplomatic layer drops headings the print does not have (as the 'SGA 5 --- ' prefixes, global issue 75); if it "
    "is kept, it belongs under the folio-20 marker (see p. 20). Filed under p. 19 because the line now stands in "
    "page_019.tex: apply before the marker move.")

# ---------------------------------------------------------------- p. 20
add(20, "start of page",
    "p. 20 begins with the title block 'CLASSES DE FAISCEAUX ET THEOREME DE RIEMANN-ROCH' (running head "
    "'0 App : RRR')",
    "\\section*{Appendice à l'Exposé 0 : RRR} and \\begin{center} stand at the end of page_019.tex, above the "
    "folio-20 marker",
    "marker", "high", None,
    "Move the folio-20 marker above the heading: python -I move_marker.py 6 20 \"\\section*{Appendice\" --before "
    "(simulated on both layers: the marker follows \\clearpage and its blank lines). If the heading is deleted "
    "(p. 19 finding), use the anchor \"\\begin{center}\" instead (the nearest one before the marker).")

add(20, "title",
    "CLASSES DE FAISCEAUX ET THEOREME DE RIEMANN-ROCH: capitals, double underline (both scans)",
    "{\\Large Classes de faisceaux et théorème de Riemann--Roch}",
    "word", "medium",
    {"old": "{\\Large Classes de faisceaux et théorème de Riemann--Roch}",
     "new": "{\\Large \\underline{\\underline{CLASSES DE FAISCEAUX ET THÉORÈME DE RIEMANN--ROCH}}}"},
    "Capitals and two parallel underlines as the p. 1 title; THÉORÈME keeps the TeX's accents (accent rule for "
    "typed capitals), the joint-name dash is left to the global pass.")

add(20, "author line",
    "par A. GROTHENDIECK (*): 'par A. GROTHENDIECK' in capitals, underlined (both scans)",
    "par A. Grothendieck\\footnote{...}",
    "word", "medium",
    {"old": "par A. Grothendieck\\footnote{", "new": "\\underline{par A. GROTHENDIECK}\\footnote{"},
    "The footnote mark (*) is not underlined. For the mark itself see the footnote finding.")

add(20, "contents, CHAP. I",
    "CHAP.I - λ-Anneaux (préliminaires formels): 'Anneaux' and 'préliminaires formels' underlined (both scans)",
    "\\subsection*{CHAP. I -- $\\lambda$-Anneaux (préliminaires formels)} (no underline)",
    "underline", "high",
    {"old": "$\\lambda$-Anneaux (préliminaires formels)}",
     "new": "$\\lambda$-\\uline{Anneaux} (\\uline{préliminaires formels})}"},
    "λ- and the parentheses are not underlined.")

add(20, "contents, CHAP. II",
    "CHAP.II - Classes de faisceaux algébriques cohérents et classes de Chern ....... 18: the title underlined and "
    "followed by the dotted leader and page number 18 (both scans)",
    "\\subsection*{CHAP. II -- Classes de faisceaux algébriques cohérents et classes de Chern} (no underline, no "
    "page number)",
    "missing", "high",
    {"old": "\\subsection*{CHAP. II -- Classes de faisceaux algébriques cohérents et classes de Chern}",
     "new": "\\subsection*{CHAP. II -- \\uline{Classes de faisceaux algébriques cohérents et classes de Chern}"
            "\\hfill 18}"},
    "The chapter line carries its own page number 18 (CHAP. I has none); the underline covers the whole title. "
    "\\uline because the title breaks over two lines.")

add(20, "footnote to 'par A. GROTHENDIECK' (and throughout)",
    "footnote mark (*) in the text and before the note (the note itself speaks of 'signes (*), (**)')",
    "\\footnote{...}: LaTeX's automatic number",
    "symbol", "low", None,
    "Convention of the transcription, not a page fix: the 90 \\footnote (and 5 \\footnotemark) of main.tex print "
    "LaTeX numbers where the typescript marks (*), (**) (also p. 15, note to 'cap-produit', seen on the witness). "
    "One decision for the volume (e.g. a symbol counter per page in the diplomatic layer).")

# ---------------------------------------------------------------- checks
bad = 0
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    t = (PAGES / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        bad += 1
        print("BAD", x["page"], n, repr(fx["old"][:60]))
counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("findings", len(F), "bad", bad, {k: f"{v[0]}/{v[1]}" for k, v in sorted(counts.items())})
if not bad:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
