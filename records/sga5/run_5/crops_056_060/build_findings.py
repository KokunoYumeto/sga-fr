"""Build findings_056_060.json and check every fix's 'old' (exactly once in its page_NNN.tex, no overlaps)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b056_060"
OUT = RUN / "findings_056_060.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if fix is None else {"old": fix[0], "new": fix[1]}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 56
add(56, "paragraph number '1.2.' at the top of the page",
    "'1.2.  Soit E ∈ ob D(X).': the number in the ordinary type of the line, not underlined, not bold",
    r"\textbf{1.2.}", "font", "medium",
    (r"\textbf{1.2.}", "1.2."),
    r"Not an underlined title, so not covered by the accepted \textbf for underlined titles; same form as "
    r"'\textbf{1.1.}' on p. 55 (reported there).")

add(56, "1.2, 'que E est pseudo-cohérent si, pour tout i'",
    "'pseudo-' (end of the line) and 'cohérent' (start of the next) underlined: the term being defined",
    "que $E$ est pseudo-cohérent si (no emphasis)", "underline", "high",
    ("est pseudo-cohérent si", r"est \emph{pseudo-cohérent} si"),
    r"\emph is the file's command for the print's underline in the appendix (\emph{Preuve}, \emph{constructible}). "
    "The later 'des objets pseudo-cohérents' is not underlined in the print.")

add(56, "Proposition 1.3, 'Si A_X est constant de valeur A un anneau noethérien à gauche'",
    "'de valeur A  un anneau': no comma after A (clean paper; the comma after 'n > 0' on the next line is crisp)",
    "de valeur $A$, un anneau", "punctuation", "high",
    ("de valeur $A$, un anneau", "de valeur $A$ un anneau"),
    "The TeX adds a comma.")

# ---------------------------------------------------------------- page 57
add(57, "top of the page: 'où l'on suppose en outre Y (resp. U) régulier.'",
    "p. 57 begins 'où l'on suppose en outre Y (resp. U) régulier.'; p. 56 ends '... (resp. (iii)) équivaut à la "
    "condition analogue'",
    "'où l'on' ends s5.tex line 1579 (as of 17:05), the last line of page_056.tex; the folio-57 marker (line 1580) "
    "follows it, so page_057.tex begins 'suppose en outre'",
    "marker", "high", None,
    "Page 57 really begins at 'où l'on' at the end of s5.tex line 1579. Exact fix: python -I move_marker.py 5 57 "
    "\"où l'on\" --before (simulated in memory on both layers: its last occurrence before the marker is this one; "
    "the marker then splits line 1579 after 'la condition analogue'). Text not moved; it agrees with the print.")

add(57, "proof of 1.3, 'Soit E ∈ ob Cons(X), montrons que E ∈ ob C.'",
    "a comma after Cons(X)",
    r"$E\in\ob\Cons(X)$; montrons", "punctuation", "high",
    (r"\Cons(X)$; montrons", r"\Cons(X)$, montrons"),
    "Semicolon of the TeX for the printed comma.")

add(57, "display 'M = ⊕ M_ℓ ,'",
    "⊕ with nothing under it: no summation index (the ℓ is only the subscript of M)",
    r"M=\bigoplus_\ell M_\ell,", "extra", "high",
    (r"\bigoplus_\ell M_\ell", r"\bigoplus M_\ell"),
    "Summation index added by the transcription (NOTE_5: report each); the next line gives the range "
    "('où ℓ parcourt l'ensemble des diviseurs premiers de n').")

add(57, "after the display F → h_*h^*(F): 'est un isomorphisme sur un facteur direct, donc il suffit de prouver que'",
    "'facteur direct, donc il suffit de prouver que': a comma, then 'donc' before 'il suffit'",
    "facteur direct; il suffit donc de prouver que", "word", "high",
    ("direct; il suffit donc de prouver", "direct, donc il suffit de prouver"),
    "Word order and punctuation in one edit.")

add(57, "'En vertu du \"Main Theorem\" (EGA IV 8.12.6)'",
    "\"Main Theorem\" with a capital T",
    "``Main theorem''", "word", "high",
    ("``Main theorem''", "``Main Theorem''"),
    "Capital against small letter. Not reported: in '(EGA IV 8.12.6)' the letters EGA are typed narrower than the "
    "pitch, with a small tick between E and G (a typed correction); the TeX's EGA gives the corrected wording.")

add(57, "commutative square, label of the bottom arrow Z → X",
    "j above the arrow (as i above the top arrow)",
    r"""Z \arrow[r,"j"'] & X, (the swap mark sets j below the arrow)""",
    "other", "high",
    (r"""\arrow[r,"j"']""", r"""\arrow[r,"j"]"""),
    "tikz-cd sets a swapped label below a rightward arrow; the print has j above it. h (left of the left arrow) "
    "and f (right of the right arrow) are right.")

add(57, "commutative square, after its bottom right vertex X",
    "no punctuation after X (clean paper to the right of the diagram)",
    "Z ... & X, (a comma after X)", "punctuation", "high",
    ("& X,\n" + r"\end{tikzcd}", "& X\n" + r"\end{tikzcd}"),
    "The TeX adds a comma; the sentence goes on 'où i est une immersion ouverte' (p. 58).")

# ---------------------------------------------------------------- page 58
add(58, "top of the page: 'où i est une immersion ouverte, et f un morphisme fini.'",
    "p. 58 begins 'où i est une immersion ouverte, et f un morphisme fini. On a'; p. 57 ends with the commutative "
    "square",
    "'où $i$ est une' (s5.tex line 1600 as of 17:05) is the last line of page_057.tex; the folio-58 marker "
    "(line 1601) follows it, so page_058.tex begins 'immersion ouverte'",
    "marker", "high", None,
    "Page 58 really begins at s5.tex line 1600 'où $i$ est une'. Exact fix: python -I move_marker.py 5 58 "
    "'où $i$ est une' --before (single quotes: the anchor contains $; simulated in memory on both layers: the marker "
    r"then stands between the \] of the square and 'où $i$ est une'). Text not moved; it agrees with the print.")

add(58, "'L'implication (iii) ⟹ (ii) résultera donc du lemme suivant :'",
    "a colon after 'suivant' (space before it)",
    "résultera donc du lemme suivant.", "punctuation", "high",
    ("du lemme suivant.", "du lemme suivant :"),
    "Full stop of the TeX for the printed colon (as 'le lemme élémentaire suivant :' on p. 52).")

add(58, "Lemme 1.3.1, 'une filtration finie de M par des sous-H-A-modules tels que les quotients successifs soient'",
    "tels (agreeing with the sous-H-A-modules)",
    "sous-$H$-$A$-modules telle que les quotients successifs", "word", "high",
    ("sous-$H$-$A$-modules telle que les quotients", "sous-$H$-$A$-modules tels que les quotients"),
    "The print has 'tels' here and in the proof ('par des sous-H-A-modules tels que H opère', next finding); "
    "'une filtration finie telle que' (no sous-modules between) has 'telle' in the print and is right in the TeX.")

add(58, "Lemme 1.3.1, 'annulés par ℓ et où H opère trivialement.'",
    "no comma after ℓ",
    r"annulés par $\ell$, et où $H$", "punctuation", "high",
    (r"par $\ell$, et où", r"par $\ell$ et où"),
    "The TeX adds a comma; the same phrase in the proof ('annulés par ℓ et où H opère trivialement') has none in "
    "the print or the TeX.")

add(58, "proof of 1.3.1, 'Montrons qu'alors M admet une filtration finie par des sous-H-A-modules tels que H opère'",
    "tels",
    "sous-$H$-$A$-modules telle que $H$ opère", "word", "high",
    ("sous-$H$-$A$-modules telle que $H$", "sous-$H$-$A$-modules tels que $H$"),
    "As in the statement of the lemma.")

add(58, "proof of 1.3.1, 'Montrons qu'alors'",
    "a new line at the left margin after the short line '... au cas où M est annulé par ℓ .' (an unindented "
    "paragraph break, as before 'Supposons' on p. 57, which the TeX sets as a paragraph)",
    r"annulé par $\ell$. Montrons qu'alors (run on)", "other", "low",
    (r"annulé par $\ell$. Montrons", r"annulé par $\ell$." + "\n\nMontrons"),
    "Paragraph break without indentation or extra space in the print; drop it if paragraphing is left to a "
    "global pass.")

add(58, "proof of 1.3.1, 'M admet donc une filtration finie'",
    "a new line at the left margin after '... ce qui prouve notre assertion.' (unindented paragraph break)",
    "notre assertion. $M$ admet donc (run on)", "other", "low",
    ("notre assertion. $M$ admet", "notre assertion.\n\n$M$ admet"),
    "As the previous finding.")

# ---------------------------------------------------------------- page 59
add(59, "heading of § 2",
    "'2. Dimension quasi-injective.' (underlined; a full stop after 'quasi-injective')",
    r"\subsection*{2. Dimension quasi-injective}", "punctuation", "high",
    ("{2. Dimension quasi-injective}", "{2. Dimension quasi-injective.}"),
    "As the logged heading fixes of p. 21 ('3. Existence de complexes dualisants.') and p. 50.")

add(59, "first paragraph, 'les notions de A_X-Module quasi-injectif, et de dimension quasi-injective'",
    "'quasi-injectif' underlined",
    "$A_X$-Module quasi-injectif, (no emphasis)", "underline", "high",
    ("-Module quasi-injectif,", r"-Module \emph{quasi-injectif},"),
    "")

add(59, "first paragraph, 'et de dimension quasi-injective d'un objet de D(X)'",
    "'dimension' (end of the line) and 'quasi-injective' (start of the next) underlined",
    "et de dimension quasi-injective d'un objet (no emphasis)", "underline", "high",
    ("et de dimension quasi-injective d'un", r"et de \emph{dimension quasi-injective} d'un"),
    "")

add(59, "second paragraph, 'une notion de dimension quasi-injective ponctuelle.'",
    "'dimension quasi-' (end of the line) and 'injective ponctuelle' (start of the next) underlined",
    "une notion de dimension quasi-injective ponctuelle. (no emphasis)", "underline", "high",
    ("dimension quasi-injective ponctuelle.", r"\emph{dimension quasi-injective ponctuelle}."),
    "")

add(59, "'et l'on note dim.q.inj_x̄(K) la borne inférieure des N'",
    "no comma after dim.q.inj_x̄(K) (end of the line, then 'la borne')",
    r"$\dim.\mathrm{q.inj}_{\bar{x}}(K)$, la borne", "punctuation", "high",
    (r"\mathrm{q.inj}_{\bar{x}}(K)$, la borne", r"\mathrm{q.inj}_{\bar{x}}(K)$ la borne"),
    "The TeX adds a comma; the comma after 'en x̄' before 'et l'on note' is printed and right.")

add(59, "display 'dim.q.inj(K) = Sup dim.q.inj_x̄(K) ,'",
    "'Sup' with a capital S and nothing under it (no index x̄)",
    r"\sup_{\bar{x}}", "formula", "high",
    (r"\sup_{\bar{x}}", r"\operatorname{Sup}"),
    r"Capital against small letter (\sup prints 'sup') and an index the print does not have (NOTE_5: summation "
    r"indices added), in one edit; \operatorname{Sup} as the p. 34 fix. The next line gives the range "
    "('où x̄ parcourt l'ensemble des points géométriques de X').")

add(59, "'avec la notion de dimension topologique stricte introduite par VERDIER'",
    "'dimension topologique stricte' underlined",
    "la notion de dimension topologique stricte introduite (no emphasis)", "underline", "high",
    ("notion de dimension topologique stricte introduite",
     r"notion de \emph{dimension topologique stricte} introduite"),
    "")

add(59, "same sentence, 'introduite par VERDIER dans [1]'",
    "VERDIER in capitals",
    "par Verdier dans", "word", "high",
    ("par Verdier dans", "par VERDIER dans"),
    "Capitals as printed (as 'A.~GROTHENDIECK' on p. 1).")

add(59, "'On dit que K ∈ ob D^+(x) est de dimension topologique stricte ⩽ N'",
    "D^+(x) with a small x (compare the capital X of 'de X' on the next line and of 'K ∈ ob D^+(X)' in the "
    "paragraph above)",
    r"$K\in\ob \D^+(X)$ est de dimension", "misprint_in_print", "high",
    (r"\D^+(X)$ est de", r"\D^+(x)$ est de"),
    "K is a complex on the scheme X (as in the definition of the pointwise quasi-injective dimension above); the "
    "small x is a typing error. The TeX silently corrects it; the fix restores the printed reading (diplomatic "
    "layer only).",
    corrected=r"\D^+(X)")

add(59, "'en un point géométrique x̄ de X si pour tout sous-préschéma Y de X, on a'",
    "no comma after 'si'",
    "de $X$ si, pour tout sous-préschéma", "punctuation", "high",
    ("$X$ si, pour tout sous-préschéma", "$X$ si pour tout sous-préschéma"),
    "The TeX adds a comma (the earlier 'si, pour tout A_X-Module constructible F, on a' has it in the print).")

add(59, "'On appelle dimension topologique stricte de K en x̄ et l'on note dimstop_x̄(K)'",
    "no comma after x̄",
    r"stricte de $K$ en $\bar{x}$, et l'on note", "punctuation", "high",
    (r"stricte de $K$ en $\bar{x}$, et", r"stricte de $K$ en $\bar{x}$ et"),
    "The TeX adds a comma (the parallel sentence on dim.q.inj above has it in the print).")

add(59, "same sentence, 'dimstop_x̄(K) la borne inférieure des N'",
    "no comma after dimstop_x̄(K) (end of the line, then 'la borne')",
    r"$\operatorname{dimstop}_{\bar{x}}(K)$, la borne", "punctuation", "high",
    (r"\operatorname{dimstop}_{\bar{x}}(K)$, la", r"\operatorname{dimstop}_{\bar{x}}(K)$ la"),
    r"The TeX adds a comma. The current layer writes \dim.\mathrm{top} for the printed 'dimstop' here and on p. 60.")

add(59, "'Tandis que la dimension quasi-injective dépend a priori de l'Anneau'",
    "a new, indented paragraph after '... vérifiant la condition précédente.'",
    "précédente. Tandis que (run on)", "other", "high",
    ("précédente. Tandis", "précédente.\n\nTandis"),
    "Paragraph break; drop it if paragraphing is left to a global pass.")

# ---------------------------------------------------------------- page 60
add(60, "top of the page: 'de base, la dimension topologique stricte'",
    "p. 60 begins 'de base, la dimension topologique stricte ne dépend que du complexe de faisceaux abéliens "
    "sous-jacent.'; p. 59 ends '... dépend a priori de l'Anneau'",
    "'de base, la' ends s5.tex line 1637 (as of 17:05), the last line of page_059.tex; the folio-60 marker "
    "(line 1638) follows it",
    "marker", "high", None,
    "Page 60 really begins at 'de base, la' at the end of s5.tex line 1637. Exact fix: python -I move_marker.py 5 60 "
    "\"de base, la\" --before (simulated in memory on both layers: the marker then splits line 1637 after "
    "'de l'Anneau'). Text not moved; it agrees with the print.")

add(60, "'On a évidemment :' before the display",
    "a colon after 'évidemment' (space before it)",
    "On a évidemment (no punctuation)", "punctuation", "high",
    ("On a évidemment\n" + r"\[", "On a évidemment :\n" + r"\["),
    "")

add(60, "heading of § 3",
    "'3. Complexes dualisants : définition et propriétés formelles.' (underlined; a full stop at the end)",
    r"\subsection*{3. Complexes dualisants: définition et propriétés formelles}", "punctuation", "high",
    ("propriétés formelles}", "propriétés formelles.}"),
    "As the heading of § 2 (p. 59).")

add(60, "last line of the page: '(SGA 4^{1/2} Cycle 2.2).'",
    "a full stop after the closing parenthesis (clear; 'SGA 4^{1/2}' and 'Cycle 2.2).' are in a different type, a "
    "later insertion); the sentence goes on after the display (4.1) at the top of p. 61: '... est un isomorphisme.'",
    "(SGA $4^{1/2}$ Cycle 2.2) (no full stop)", "misprint_in_print", "high",
    ("Cycle 2.2)", "Cycle 2.2)."),
    "Stray full stop inside the sentence 'Dire que ... signifie ... que l'homomorphisme ... (4.1) est un "
    "isomorphisme.' The TeX silently drops it; the fix restores the printed reading (diplomatic layer only).",
    corrected="Cycle 2.2)")

add(60, "display (4.1), printed at the top of p. 61 (in page_060.tex as the files stand)",
    "(4.1)  (μ_n)_Y^{⊗-d} [-2d] → ℝ i^!(Z/nZ)_X : the parenthesis closes after μ_n; Y is a subscript and ⊗-d a "
    "superscript after it",
    r"(\mu_n^{\otimes -d})_Y[-2d]", "formula", "high",
    (r"(\mu_n^{\otimes -d})_Y[-2d]", r"(\mu_n)_Y^{\otimes -d}[-2d]"),
    "Checked on a render of p. 61 (scan idx 72). Filed under p. 60 because the display stands in page_060.tex: "
    "the old stays unique on p. 61 after the folio-61 marker move. The rest of the display and 'est un' agree with "
    "the print (double-struck R, no punctuation after the display).")

add(60, "end of the page: the display (4.1) and 'est un' (folio-61 marker)",
    "p. 60 ends '... (SGA 4^{1/2} Cycle 2.2).' (blank below); p. 61 begins with the display (4.1), then "
    "'est un isomorphisme.'",
    r"\begin{equation}\tag{4.1} ... \end{equation} and 'est un' (s5.tex lines 1654-1657 as of 17:05) end "
    "page_060.tex; the folio-61 marker (line 1658) follows them",
    "marker", "high", None,
    r"Page 61 really begins at s5.tex line 1654 '\begin{equation}\tag{4.1}'. Exact fix: python -I move_marker.py 5 61 "
    r"'\begin{equation}\tag{4.1}' --before (simulated in memory on both layers: the marker then stands between "
    r"'Cycle 2.2)' and \begin{equation}; 'est un' and 'isomorphisme.' then follow each other on two lines of p. 61). "
    "Text not moved. Move it before the batch of pp. 61-65 is prepared.")

# ---------------------------------------------------------------- checks
errors = 0
spans = {}
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = t.count(old)
    if n != 1:
        print("NOT UNIQUE/NOT FOUND", d["page"], n, repr(old))
        errors += 1
        continue
    if "%%%%%%%%%%" in old:
        print("crosses marker", repr(old))
        errors += 1
    k = t.index(old)
    spans.setdefault(d["page"], []).append((k, k + len(old), old))
for p, sp in spans.items():
    sp.sort()
    for a, b in zip(sp, sp[1:]):
        if a[1] > b[0]:
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
            errors += 1
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("findings", len(F), "errors", errors)
print(" | ".join(f"p.{p} {c[0]}/{c[1]}" for p, c in sorted(counts.items())))
