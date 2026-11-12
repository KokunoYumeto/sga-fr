"""Build findings_071_075.json, check every fix's old (exactly once in its page file, no overlaps on a page),
and simulate in memory: the fixes on the diplomatic s5.tex, then the four marker moves on both layers.
Writes only the findings JSON; never writes a .tex file.
usage: python -I build_findings.py [--write]"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
B = W / "run_5" / "b071_075"
OUT = W / "run_5" / "findings_071_075.json"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


RG_NOTE = ("Apply together with the other three \\R g^! -> \\R^!g fixes (p. 71 one, p. 72 three): one notation, "
           "the print raises the shriek right after the double-struck R, before g, every time.")
TOC_NOTE = ("The Sommaire prints leader dots and the exposé's own page numbers (4, 9, 17, 27, 41, 48); the TeX has "
            "neither and ends each entry with a full stop. \\dotfill is standard LaTeX. (The Sommaire of Exposé IV, "
            "s5.tex 'I. Correspondances en position générale', uses a tabular with the page numbers instead.)")

findings = [
    # ---------------- page 71
    F(71, "'D'après ce qu'on a vu au N° 6, la condition (ii) de loc.cit.'",
      "N° with a capital N (p. 72 prints 'du n° 6' with a small n)", "au n\\textsuperscript{o}~6", "word", "high",
      "au n\\textsuperscript{o}~6", "au N\\textsuperscript{o}~6", "Capital against small letter."),
    F(71, "'i : U → Y un ouvert régulier ≠ ∅, et E_U un A_U-Module constant'",
      "régulier ≠ ∅ : the symbols ≠ and ∅ (a slashed zero), no words", "un ouvert régulier non vide, et", "word",
      "high", "régulier non vide", "régulier $\\neq\\emptyset$",
      "The TeX writes the printed symbols out as words."),
    F(71, "commutative diagram, label of the bottom arrow U → Y",
      "i above the arrow (as f above the next arrow)", "\\arrow[r,\"i\"'] (the swap mark sets i below the arrow)",
      "other", "high", "\\arrow[r,\"i\"']", "\\arrow[r,\"i\"]",
      "tikz-cd sets a swapped label below a rightward arrow. i' (upper left of the rising arrow), h (right of the "
      "vertical arrow), g (upper right of the falling arrow) and the full stop after X are right."),
    F(71, "commutative diagram, label of the bottom arrow Y → X", "f above the arrow",
      "\\arrow[r,\"f\"'] (below the arrow)", "other", "high", "\\arrow[r,\"f\"']", "\\arrow[r,\"f\"]",
      "As the label i."),
    F(71, "'pour le couple (i'_!i'^*(E_{Y'}), ℝ^!g(K))' (printed at the top of p. 72; in page_071.tex as the "
          "files stand)",
      "ℝ^!g(K): the shriek raised right after the double-struck R, before g", "\\R g^!(K)", "formula", "high",
      "\\R g^!(K))$", "\\R^!g(K))$",
      RG_NOTE + " Filed under p. 71; its old stays unique on p. 72 after the folio-72 marker move."),
    # ---------------- page 72
    F(72, "top of the page",
      "p. 72 begins '(i'_!i'^*(E_{Y'}), ℝ^!g(K)). Mais, plongeant localement Y' dans un préschéma X''; p. 71 ends "
      "'il suffit de prouver la bidualité pour le couple' (blank below)",
      "'$(i'_!i'^*(E_{Y'}),\\R g^!(K))$. Mais, plongeant localement $Y'$ dans un préschéma $X'$' ends s5.tex line "
      "1904 (as of 17:29), the last line of page_071.tex; the folio-72 marker (line 1905) follows it",
      "marker", "high", None, None,
      "Page 72 really begins at '$(i' in s5.tex line 1904. Exact fix: python -I move_marker.py 5 72 '$(i' --before "
      "(single quotes: the anchor contains $; simulated in memory on both layers: the marker then splits line 1904 "
      "after 'pour le couple'). Text not moved."),
    F(72, "'on trouve que ℝ^!g(K) est localement isomorphe'", "ℝ^!g(K): shriek raised after R, before g",
      "$\\R g^!(K)$", "formula", "high", "que $\\R g^!(K)$ est", "que $\\R^!g(K)$ est", RG_NOTE),
    F(72, "'donc que ℝ^!g(K) ∈ ob D^+_coh(Y')'", "ℝ^!g(K)", "$\\R g^!(K)\\in", "formula", "high",
      "$\\R g^!(K)\\in", "$\\R^!g(K)\\in", RG_NOTE),
    F(72, "'et que ℝ^!g(K)_x̄ est dualisant'", "ℝ^!g(K)_x̄", "$\\R g^!(K)_{\\bar{x}}$", "formula", "high",
      "$\\R g^!(K)_{\\bar{x}}", "$\\R^!g(K)_{\\bar{x}}", RG_NOTE),
    F(72, "'(moyennant le théorème de finitude pour un morphisme propre (SGAA XIV), ce qui soulagera'",
      "(SGAA XIV), : one closing parenthesis; the parenthesis opened before 'moyennant' is never closed (clear at "
      "3x)", "(SGAA XIV)),", "misprint_in_print", "high", "(SGAA XIV)),", "(SGAA XIV),",
      "The TeX silently supplies the missing parenthesis; the fix restores the printed reading (diplomatic layer "
      "only).", corrected="(SGAA XIV)),"),
    F(72, "'dans le laius du n° 6.'", "laius: the i has a single dot, no diaeresis (clean, checked at 8x)", "laïus",
      "misprint_in_print", "medium", "laïus", "laius",
      "The TeX silently supplies the diaeresis. NOTE_5 has no rule for the typescript's plain i for ï; NOTE_6 and "
      "SGA 7 let the TeX's ï stand (not reported there). Drop this finding if SGA 5 follows that rule.",
      corrected="laïus"),
    F(72, "ornament after 'Cela achève la démonstration.'", "-:-:-:- (four dashes, three colons)",
      "$-:\\!-:\\!-$ (three dashes, two colons)", "other", "medium",
      "démonstration.\n\n\\begin{center}\n$-:\\!-:\\!-$", "démonstration.\n\n\\begin{center}\n$-:\\!-:\\!-:\\!-$",
      "The only two ornaments in s5.tex are on this page (see the second); apply both or neither."),
    F(72, "heading of the bibliography", "BIBLIOGRAPHIE: capitals (underlined)", "\\section*{Bibliographie}",
      "word", "high", "\\section*{Bibliographie}", "\\section*{BIBLIOGRAPHIE}",
      "Capitals as printed, as the logged fix of the bibliography of Exposé I (p. 53/54); the underline is the "
      "accepted \\section* setting."),
    F(72, "[1], first author: 'VERDIER, J-L.  Dimension des espaces'",
      "VERDIER in capitals; J-L. with no full stop after J; no comma after J-L.", "\\item Verdier, J.-L., \\emph{...",
      "word", "high", "\\item Verdier, J.-L.,", "\\item VERDIER, J-L.",
      "Capitals, the initial's full stop and the comma in one edit (adjacent). As 'Serre, J-P.' on p. 54."),
    F(72, "[1], title 'Dimension des espaces localement compacts'", "typed plain, not underlined",
      "\\emph{Dimension des espaces localement compacts}", "underline", "high",
      "\\emph{Dimension des espaces localement compacts}", "Dimension des espaces localement compacts",
      "\\emph is the file's command for the print's underline; as the titles of the bibliography of Exposé I (p. 54)."),
    F(72, "[1], 'p. 5293-5296 (1965)'", "typewriter hyphen", "p.~5293--5296 (en dash)", "punctuation", "high",
      "5293--5296", "5293-5296", "En dash added by the transcription (NOTE_5: report each)."),
    F(72, "[1], '(1965). (Voir aussi : VERDIER, J-L., ...'",
      "an opening parenthesis before 'Voir'; it closes at the end of the item ('1965-66).')",
      "(1965). Voir aussi: (no parenthesis)", "missing", "high", "(1965). Voir", "(1965). (Voir",
      "Apply together with the closing parenthesis at the end of the item."),
    F(72, "[1], second author: 'VERDIER, J-L., Dualité'", "VERDIER in capitals; J-L. with no full stop after J",
      "Verdier, J.-L.,", "word", "high", "aussi: Verdier, J.-L.,", "aussi: VERDIER, J-L.,",
      "Capitals and the initial's full stop in one edit; the comma after J-L. is printed here."),
    F(72, "[1], title 'Dualité dans la cohomologie des espaces localement compacts'", "typed plain, not underlined",
      "\\emph{Dualité dans la cohomologie des espaces localement compacts}", "underline", "high",
      "\\emph{Dualité dans la cohomologie des espaces localement compacts}",
      "Dualité dans la cohomologie des espaces localement compacts", "As the first title."),
    F(72, "[1], 'n° 300, 1965-66).'", "typewriter hyphen", "1965--66 (en dash)", "punctuation", "high",
      "1965--66", "1965-66", "En dash added by the transcription."),
    F(72, "[1], end of the item: '1965-66).'", "a closing parenthesis before the final full stop",
      "1965--66. (no parenthesis)", "missing", "high", ".\n\\end{enumerate}", ").\n\\end{enumerate}",
      "Apply together with the opening parenthesis before 'Voir'. Does not overlap the en-dash fix."),
    F(72, "'SGA A = SGA 4' after the bibliography", "no full stop after 4 (clean paper to the right)",
      "SGA A = SGA 4.", "punctuation", "high", "SGA A = SGA 4.", "SGA A = SGA 4", "The TeX adds a full stop."),
    F(72, "ornament after 'SGA A = SGA 4', closing the exposé", "-:-:-:- (four dashes, three colons)",
      "$-:\\!-:\\!-$", "other", "medium",
      "$-:\\!-:\\!-$\n\\end{center}\n\n\\clearpage", "$-:\\!-:\\!-:\\!-$\n\\end{center}\n\n\\clearpage",
      "As the first ornament; apply both or neither."),
    # ---------------- page 73
    F(73, "top of the page: the exposé heading 'Exposé III'",
      "p. 73 begins with 'Exposé III', then 'FORMULE DE LEFSCHETZ' and 'par A. Grothendieck, rédigé par "
      "L. Illusie'; p. 72 ends with 'SGA A = SGA 4' and the ornament",
      "'\\begin{center}' and '{\\Large \\textbf{Exposé III}}\\\\[0.4em]' (s5.tex lines 1929-1930 as of 17:29) end "
      "page_072.tex; the folio-73 marker (line 1931) stands inside the center environment",
      "marker", "high", None, None,
      "Page 73 really begins at s5.tex line 1929 '\\begin{center}'. Exact fix: python -I move_marker.py 5 73 "
      "'\\begin{center}' --before (simulated in memory on both layers: the marker then stands between "
      "'\\clearpage' and '\\begin{center}', and the title block is whole on p. 73). Text not moved; the heading's "
      "words agree with the print."),
    F(73, "'mais les compatibilités réquises n'étaient pas démontrées'",
      "réquises, with an acute accent on the first e (as crisp as the accents around it)", "requises",
      "misprint_in_print", "high", "requises", "réquises",
      "The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
      corrected="requises"),
    F(73, "'distribuée par l'IHES il y a dix ans environs, la formule'", "environs, with a final s",
      "environs (as printed)", "misprint_in_print", "high", None, None,
      "The adverb is invariable ('il y a dix ans environ'). The TeX keeps the printed reading.",
      corrected="environ"),
    F(73, "'elle dit que, sous certaines conditions la trace d'un endomorphisme'",
      "no comma after 'conditions' (clean paper); the comma after 'que' that opens the insertion is printed",
      "sous certaines conditions, la trace", "misprint_in_print", "medium", "conditions, la trace",
      "conditions la trace",
      "The print does not close the insertion 'sous certaines conditions'; the TeX silently supplies the comma. "
      "The fix restores the printed reading (diplomatic layer only).", corrected="conditions, la trace"),
    F(73, "'d'un complexe d'hypercohomologie RΓ(X,L), où L est'",
      "a plain typed R (single stem, the typeface of the text), not double-struck", "$\\R\\Gamma(X,L)$ "
      "(\\R is \\mathbb{R})", "font", "high", "\\R\\Gamma(X,L)", "R\\Gamma(X,L)",
      "Exposé III is typed in another typeface than Exposé II and types the derived-functor R plain (also in "
      "RHom, pp. 74-75); Exposé II on pp. 71-72 has a hand-drawn double-struck R."),
    # ---------------- page 74
    F(74, "top of the page: '(la thèse de Jouanolou n'ayant malheureusement pas été publiée)'",
      "p. 74 begins '(la thèse de Jouanolou n'ayant malheureusement pas été publiée), nous travaillons'; p. 73 "
      "ends 'Faute de disposer d'une bonne catégorie dérivée de faisceaux ℓ-adiques'",
      "'(la thèse de' ends s5.tex line 1940 (as of 17:29), the last line of page_073.tex; the folio-74 marker "
      "(line 1941) follows it",
      "marker", "high", None, None,
      "Page 74 really begins at '(la thèse de' at the end of s5.tex line 1940. Exact fix: python -I move_marker.py "
      "5 74 '(la th' --before (simulated in memory on both layers: the marker then splits line 1940 after "
      "'$\\ell$-adiques'). Text not moved; it agrees with the print."),
    F(74, "'formules de Künneth de (SGA 4^{1/2} Finitude), qui fouent un rôle essentiel'",
      "fouent: an f (tall stem with a crossbar), not a j", "jouent", "misprint_in_print", "high", "jouent", "fouent",
      "The TeX silently corrects; the fix restores the printed reading (diplomatic layer only).",
      corrected="jouent"),
    F(74, "'exprime une compatibilité entre produit tensoriel externe de RHom'",
      "RHom: a plain typed R; the underline runs under Hom only", "$\\uRHom$ (\\underline{\\mathbb{R}\\mathrm{Hom}}: "
      "double-struck R, R underlined too)", "font", "high", "externe de $\\uRHom", "externe de $R\\underline{\\Hom}",
      "Listed before the adjacent misprint fix (missing comma), whose old starts at the closing $. Same form in the "
      "Sommaire on p. 75."),
    F(74, "same sentence, 'de RHom   image directe et changement de base'",
      "no comma after RHom (a blank of about three characters, clean paper)", "$\\uRHom$, image directe",
      "misprint_in_print", "high", "$, image directe", "$ image directe",
      "The enumeration 'produit tensoriel externe de RHom, image directe et changement de base' needs the comma; "
      "the TeX silently supplies it. The fix restores the printed reading (diplomatic layer only); its old does "
      "not overlap the RHom fix.", corrected="$, image directe"),
    F(74, "heading of the summary (printed at the top of p. 75; in page_074.tex as the files stand)",
      "SOMMAIRE. : capitals, underlined, then a full stop", "\\subsection*{Sommaire}", "word", "high",
      "\\subsection*{Sommaire}", "\\subsection*{SOMMAIRE.}",
      "Capitals and full stop as printed (as BIBLIOGRAPHIE, and the heading full stops of pp. 59-60); the "
      "underline is the accepted \\subsection* setting. Filed under p. 74: the anchor of the folio-75 marker move "
      "('\\subsection*{S') matches either spelling."),
    # ---------------- page 75
    F(75, "top of the page: the heading 'SOMMAIRE.'",
      "p. 75 begins with 'SOMMAIRE.' and the six entries; p. 74 ends '... et signalons quelques applications.' "
      "(blank below)",
      "'\\subsection*{Sommaire}', '\\begin{enumerate}[label=\\arabic*.]' and '\\item' (s5.tex lines 1946-1948 as of "
      "17:29) end page_074.tex; the folio-75 marker (line 1949) stands between '\\item' and the text of entry 1",
      "marker", "high", None, None,
      "Page 75 really begins at s5.tex line 1946 '\\subsection*{Sommaire}'. Exact fix: python -I move_marker.py 5 75 "
      "'\\subsection*{S' --before (also matches after the SOMMAIRE fix; simulated in memory on both layers: the "
      "marker then stands after 'applications.' and its blank line; '\\item' and 'Notations et rappels' then "
      "follow each other on two lines of one item). Text not moved."),
    F(75, "Sommaire, entry 2 'Fonctorialité de RHom et produits tensoriels externes'",
      "RHom: a plain typed R; the underline runs under Hom only", "$\\uRHom$", "font", "high",
      "$\\uRHom$", "$R\\underline{\\Hom}$", "As on p. 74."),
    F(75, "Sommaire, entry 1", "'Notations et rappels de formules de Künneth......  4'",
      "Notations et rappels de formules de Künneth.", "missing", "high",
      "formules de Künneth.", "formules de Künneth\\dotfill 4", TOC_NOTE),
    F(75, "Sommaire, entry 2", "'Fonctorialité de RHom et produits tensoriels externes......  9'",
      "... produits tensoriels externes.", "missing", "high",
      "tensoriels externes.", "tensoriels externes\\dotfill 9", "As entry 1."),
    F(75, "Sommaire, entry 3", "'Correspondances cohomologiques......  17'", "Correspondances cohomologiques.",
      "missing", "high", "Correspondances cohomologiques.", "Correspondances cohomologiques\\dotfill 17",
      "As entry 1."),
    F(75, "Sommaire, entry 4", "'Accouplements de correspondances. Formule de Lefschetz......  27'",
      "Accouplements de correspondances. Formule de Lefschetz.", "missing", "high",
      "correspondances. Formule de Lefschetz.", "correspondances. Formule de Lefschetz\\dotfill 27",
      "As entry 1."),
    F(75, "Sommaire, entry 5", "'Compléments......  41'", "Compléments.", "missing", "high",
      "\\item Compléments.", "\\item Compléments\\dotfill 41", "As entry 1."),
    F(75, "Sommaire, entry 6", "'Appendice. Formule de Lefschetz pour les faisceaux cohérents....  48'",
      "Appendice. Formule de Lefschetz pour les faisceaux cohérents.", "missing", "high",
      "faisceaux cohérents.", "faisceaux cohérents\\dotfill 48", "As entry 1."),
]

# ---- checks on the page files
ok = True
pages = {n: (B / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(71, 76)}
spans = {}
for i, f in enumerate(findings):
    if f["fix"] is None:
        continue
    t = pages[f["page"]]
    old = f["fix"]["old"]
    c = t.count(old)
    if c != 1:
        ok = False
        print("NOT UNIQUE", c, f["page"], repr(old))
    if MARK.search(old) or MARK.search(f["fix"]["new"]):
        ok = False
        print("MARKER IN FIX", f["page"], repr(old))
    k = t.find(old)
    spans.setdefault(f["page"], []).append((k, k + len(old), i))
for p, ss in spans.items():
    ss.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(ss, ss[1:]):
        if a2 < b1:
            ok = False
            print("OVERLAP", p, findings[i1]["fix"]["old"], "|", findings[i2]["fix"]["old"])
print("checks ok" if ok else "CHECKS FAILED", len(findings), "findings")

# ---- simulate: fixes on the diplomatic layer (page spans), then the marker moves on both layers
moves = [(72, "$(i"), (73, "\\begin{center}"), (74, "(la th"), (75, "\\subsection*{S")]


def apply_fixes(text):
    for n in range(71, 76):
        ms = list(MARK.finditer(text))
        m = next(m for m in ms if int(m.group(2)) == n)
        nxt = next(x for x in ms if x.start() > m.start())
        seg = text[m.start():nxt.start()]
        for f in findings:
            if f["page"] == n and f["fix"]:
                assert seg.count(f["fix"]["old"]) == 1, (n, f["fix"]["old"])
                seg = seg.replace(f["fix"]["old"], f["fix"]["new"], 1)
        text = text[:m.start()] + seg + text[nxt.start():]
    return text


def move(text, folio, anchor):
    m = next(m for m in MARK.finditer(text) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if text[m.end():m.end() + 1] == "\n" else 0)
    t2 = text[:m.start()] + text[end:]
    k = t2.rfind(anchor, 0, m.start())
    assert k >= 0
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for ed in ("diplomatic", "current"):
    s = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    s2 = apply_fixes(s) if ed == "diplomatic" else s
    for folio, anchor in moves:
        s2 = move(s2, folio, anchor)
    if ed == "diplomatic" and "--show" in sys.argv:
        a = s2.find("folio 71  ")
        b = s2.find("folio 76  ")
        print(s2[a - 40:b + 20])
    # check where each page now begins
    for folio, _ in moves:
        m = next(m for m in MARK.finditer(s2) if int(m.group(2)) == folio)
        print(ed, folio, "begins:", repr(s2[m.end() + 1:m.end() + 70]), "| before:",
              repr(s2[max(0, m.start() - 50):m.start()]))

if "--write" in sys.argv and ok:
    OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
