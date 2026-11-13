import json
import pathlib
import sys

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b651_655"
OUT = RUN / "findings_651_655.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- p. 651
add(651, "En effet, ...: the étale cohomology H^*(X,Q_l) =_dfn [lim H^*(X,Z/l^nu Z)] (x)_{Z_l} Q_l",
    "'[lim H*(X,Z / l^v Z)]': 'lim' with the left arrow under it and nothing below the arrow, no index "
    "(both scans; crops_651_655/c651_lim.png, c651_lim2.png, w662_bot.png)",
    r"\left[\varprojlim_\nu H^*(X,\Z/\ell^\nu\Z)\right]",
    "extra", "high",
    {"old": r"\varprojlim_\nu", "new": r"\varprojlim"},
    "The TeX adds an index under the inverse limit that the print does not have.")

add(651, "'elle satisfait à la dualité de Poincaré et à la formule de Künneth'",
    "'la formule de KUnneth': the u typed as a capital U at cap height, no diaeresis visible (it would fall on "
    "the arms of the capital) (both scans; crops_651_655/c651_kun.png, w651_kun.png)",
    r'K\"unneth (silently corrected)',
    "misprint_in_print", "low",
    {"old": r'K\"unneth', "new": r'K\"Unneth'},
    "Same printed form as p. 75 'conséquences de KÜnneth', which was applied as a misprint record "
    "(findings_071_075.json; main.tex line 1720 'KÜnneth'); p. 70 (main.tex line 1553) still reads 'Künneth'. "
    "If the capital Ü is taken as the typewriter's only ü, drop this entry with p. 75 (one volume decision).",
    corrected=r'K\"unneth')

add(651, "'défini par alpha(b) = (<b.a_1>,...,<b,a_m>)'",
    "'(<b.a1>,...,<b,am>)': a full stop in the first bracket, a comma in the last (both scans; "
    "b651_655/page_651_s4.png, crops_651_655/w662_bot.png)",
    r"(\langle b.a_1\rangle,\ldots,\langle b,a_m\rangle) (as printed)",
    "misprint_in_print", "low",
    None,
    "Typing inconsistency of the print: the intersection number is written with the dot of the intersection "
    "product (<b.a_1>; also <lambda.Y_i> in 5.4, p. 652). The diplomatic TeX keeps the printed comma.",
    corrected=r"\langle b.a_m\rangle")

# ---------------- p. 652
add(652, "Remarque 5.3: 'L'inégalité rang(C^1_num(X)) <= b^2(X)'",
    "'rang(C^1_mum(X))': the subscript reads mum (both scans; crops_651_655/c652_mum.png, w663_top.png)",
    r"\rang(C^1_{\rm num}(X)) (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"C^1_{\rm num}", "new": r"C^1_{\rm mum}"},
    "Typing error of the print (num, as C^p_num in Proposition 5.2).",
    corrected=r"C^1_{\rm num}")

add(652, "Remarque 5.3: 'dans cette forme pour car(k) > 0 est due (avant la cohomologie étale)'",
    "'est dûe (avant': u with a circumflex (both scans; crops_651_655/c652_mum.png, w663_top.png)",
    "est due (silently corrected)",
    "misprint_in_print", "high",
    {"old": "est due", "new": r"est d\^ue"},
    "Spelling error of the print: the feminine participle is 'due' (no circumflex).",
    corrected="est due")

add(652, "Théorème 5.4: 'le rang du groupe de Néron-Severi'",
    "'Néron-Severi': accent on Néron only, none on Severi (both scans; crops_651_655/c652_severi.png, "
    "w663_top.png)",
    r"N\'eron-S\'everi",
    "accent", "high",
    {"old": r"S\'everi", "new": "Severi"},
    "The TeX adds an accent that the print (and the name Severi) does not have.")

add(652, "proof of 5.4: 'l'espace vectoriel [Pic_{X/k}(k)/Pic^tau_{X/k}(k)] (x) Q soit fini'",
    "'] (x) Q soit fini': the tensor sign has no subscript (both scans; crops_651_655/c652_otimes.png)",
    r"\otimes_{\Z}\Q",
    "extra", "high",
    {"old": r"\otimes_{\Z}\Q", "new": r"\otimes\Q"},
    "The TeX adds the subscript Z.")

# ---------------- p. 653
add(653, "heading '6. Appendice : Etude des (b)-faisceaux sur P = P^N_k.'",
    "P^N_k: a P with a doubled stem (double-struck), like the double-struck Z and Q of the exposé (both scans; "
    "crops_651_655/c653_head.png, w664_top.png)",
    r"$P=\mathbf P^N_k$ (bold)",
    "font", "medium",
    {"old": r"faisceaux sur $P=\mathbf P^N_k$", "new": r"faisceaux sur $P=\mathbb P^N_k$"},
    r"P is not in the handled list of double-struck letters (Z, Q, F, C, A); \mathbb as the file's \Z, \Q. "
    r"Not for a blind pass: \mathbf P stands for the doubly underlined P in Exposé VI. Same in 6.1 (next entry); "
    "apply both or neither.")

add(653, "6.1: 'Soient k un corps algébriquement clos, et P = P^N_k.'",
    "P^N_k with the double-struck P, as in the heading (both scans; crops_651_655/c653_PN.png, w664_top.png)",
    r"$P=\mathbf P^N_k$ (bold)",
    "font", "medium",
    {"old": r"clos, et $P=\mathbf P^N_k$", "new": r"clos, et $P=\mathbb P^N_k$"},
    "Together with the heading entry.")

add(653, "the structure sheaf O_P, O_Y, O_X on pp. 653-655 (convention of the Exposé XIII transcription, "
         "reported once; 12 places: p. 653 four, p. 654 six, p. 655 two)",
    "a plain typed capital O, not underlined, in every place: Lemme 6.2 display, proof of 6.2, the display of "
    "Prop. 6.3 (twice); p. 654 display, Théorème 6.4, 'section sigma de O_P(1)', the diagram's middle row "
    "(three); p. 655 H^q(O_P^{(+)M}(p)) and F' = O_X.sigma (both scans)",
    r"\mathcal O in all 12 places (script O)",
    "font", "medium",
    None,
    r"CONVENTION, not itemized (as for pp. 616-619 in findings_616_620.json): the TeX writes \mathcal O for "
    r"the print's plain typed O. Three examples in the plain form: p. 653 'En effet, $\mathcal O_P$ est' -> "
    r"'En effet, $O_P$ est'; p. 654 'section $\sigma$ de $\mathcal O_P(1)$' -> 'section $\sigma$ de $O_P(1)$'; "
    r"p. 655 '\(H^q(\mathcal O_P^{\oplus M}(p))' -> '\(H^q(O_P^{\oplus M}(p))'.")

# ---------------- p. 654
add(654, "start of the page: 'En effet, on prend m = P_{r-1}(c_o,...,c_{r-1})'",
    "p. 654 begins with the indented 'En effet, on prend m = ...' (both scans; b651_655/page_654_s1.png, "
    "crops_651_655/w665_top.png)",
    "the word 'En' is the last line of page_653.tex (main.tex line 16444), above the folio-654 marker; "
    "page_654.tex begins 'effet, on prend'",
    "marker", "high",
    None,
    "Page 654 begins at 'En'. Move the folio-654 marker line up before 'En': python -I move_marker.py 6 654 "
    "\"En\" --before (it takes the last 'En' before the marker, which stands on a line of its own). Not "
    "marker_split_word.py pull, which would join 'Eneffet'.")

add(654, "proof of 6.3: 'et M = Sum a_i (m+i choose i), de sorte qu'on a'",
    "'M = Σ a_i(m+i i)': a bare sum sign, no index (both scans; crops_651_655/c654_M.png, w665_top.png)",
    r"M=\sum_i a_i\binom{m+i}{i}",
    "extra", "high",
    {"old": r"M=\sum_i a_i\binom{m+i}{i}", "new": r"M=\sum a_i\binom{m+i}{i}"},
    "The TeX adds a summation index.")

add(654, "proof of 6.3: 'et M_1 = M.(p+N choose N) - ...'",
    "after M a small raised mark (a short stroke and a dot at cap height) in both scans "
    "(crops_651_655/c654_Mdot2.png, w654_mark_zoom.png); not an asterisk (compare H* on p. 651, "
    "w651_star_zoom.png); M(n+N choose N) in the proof of 6.2 (p. 653) has no mark",
    r"M_1=M\binom{p+N}{N}: nothing between M and the binomial",
    "symbol", "low",
    {"old": r"M_1=M\binom{p+N}{N}", "new": r"M_1=M\cdot\binom{p+N}{N}"},
    "Read as a raised multiplication dot; if it is judged a stray mark, drop this entry. Independent of the "
    "neighbouring entries (no overlap).")

add(654, "proof of 6.3: '... - Sum a_i (m_1+i choose i) (= chi(I(p))).'",
    "'- Σ a_i(m_1+i i)': a bare sum sign, no index (both scans; crops_651_655/c654_M1.png, w654_M1.png)",
    r"-\sum_i a_i\binom{m_1+i}{i}",
    "extra", "high",
    {"old": r"-\sum_i a_i\binom{m_1+i}{i}", "new": r"-\sum a_i\binom{m_1+i}{i}"},
    "The TeX adds a summation index (as for M on the line above).")

add(654, "proof of 6.3: the closing '(= chi(I(p)).'",
    "'(= χ(I(p)).': three opening parentheses, two closing, then the full stop (both scans; "
    "crops_651_655/c654_M1.png, w654_M1.png)",
    r"\quad(=\chi(I(p)))$. (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"(=\chi(I(p)))", "new": r"(=\chi(I(p))"},
    "Typing error of the print: the parenthesis opened before '=' is never closed.",
    corrected=r"(=\chi(I(p)))")

add(654, "after the 3x5 diagram of the proof of 6.4",
    "a typed full stop to the right of the diagram's bottom row of zeros (both scans; "
    "b651_655/page_654_s3.png, crops_651_655/w665_bot.png), as after the display of Prop. 6.3 on p. 653",
    "no punctuation in or after the tikzcd",
    "punctuation", "high",
    {"old": "&0&0&0&\n\\end{tikzcd}", "new": "&0&0&0&.\n\\end{tikzcd}"},
    "The TeX leaves out the full stop printed after the diagram (GLOBAL_ISSUES 2).")

# ---------------- p. 655
add(655, "'... montre alors que F(m) est (b_1-1)-régulier ; d'où (i). L'assertion (i) implique que ...'",
    "'L'assertion (i) implique que' begins a new, indented paragraph (both scans; b651_655/page_655_s1.png, "
    "crops_651_655/w666_a.png)",
    "the sentence runs on in the same paragraph",
    "other", "medium",
    {"old": r"d'o\`u (i). L'assertion", "new": "d'o\\`u (i).\n\nL'assertion"},
    "Paragraph break missing in running text (not after a display, so not GLOBAL_ISSUES 53).")

add(655, "end of the proof of 6.4: 'd'où (iii) grâce à 1.6.2.'",
    "'graĉe à 1.6.2': the circumflex stands over the c, the a has none (both scans; "
    "crops_651_655/c655_grace.png, w666_a.png)",
    r"gr\^ace (silently corrected)",
    "misprint_in_print", "high",
    {"old": r"gr\^ace \`a 1.6.2", "new": r"gra\^ce \`a 1.6.2"},
    "Typing error of the print: the circumflex struck on the wrong letter.",
    corrected=r"gr\^ace \`a 1.6.2")

add(655, "proof of 6.5: 'un sous-faisceau non nul F' = O_X.sigma de F'",
    "'O_X.σ': a typed full stop on the baseline between O_X and sigma (both scans; "
    "crops_651_655/c655_OXsigma.png, w666_b.png)",
    r"\mathcal O_X\cdot\sigma (centred dot)",
    "symbol", "medium",
    {"old": r"_X\cdot\sigma", "new": r"_X.\sigma"},
    r"The TeX keeps the typed full stop elsewhere on the page (n_0.h^0(G) in 6.5 (iii)). The old string leaves "
    r"\mathcal O out (convention entry of p. 653).")

add(655, "proof of 6.5: 'donc s=dim.supp(F') est >= 1'",
    "'s=dim.supp(F')': a full stop after dim (both scans; crops_651_655/c655_dimsupp.png, w666_b.png)",
    r"s=\dim\operatorname{supp}(F')",
    "punctuation", "high",
    {"old": r"s=\dim\operatorname{supp}(F')", "new": r"s=\dim.\operatorname{supp}(F')"},
    "The TeX drops the full stop of the abbreviation.")

add(655, "after the 3x5 diagram of the proof of 6.5",
    "a typed full stop to the right of the bottom row 0 -> F(-1) -> F -> G -> 0 (both scans; "
    "b651_655/page_655_s4.png, crops_651_655/w666_b.png)",
    "no punctuation after the tikzcd",
    "punctuation", "high",
    {"old": "&G \\arrow[r]&0\n\\end{tikzcd}", "new": "&G \\arrow[r]&0 & .\n\\end{tikzcd}"},
    "The TeX leaves out the full stop printed after the diagram (GLOBAL_ISSUES 2).")

add(655, r"end of the page: last line of page_655.tex 'De $s\ge1$, r\''",
    "p. 655 ends with the diagram and its full stop (both scans; b651_655/page_655_s4.png); "
    "'De s >= 1, résulte G' != 0 ;' is the first line of p. 656 (witness, DjVu page 667: "
    "crops_651_655/w667_top.png)",
    r"page_655.tex ends with 'De $s\ge1$, r\'' (main.tex line 16491); the folio-656 marker (line 16492) "
    r"splits the word r\'|esulte",
    "marker", "high",
    None,
    r"Page 656 begins at 'De $s\ge1$'. Move the folio-656 marker up before that line: python -I move_marker.py 6 "
    r'656 "De $s\ge1$" --before; then rejoin the split word (r\'esulte on one line, or r\'% at the line end), '
    "both layers.")

# ---------------- checks
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    mk = "%%%%%%%%%%" in fx["old"]
    if n != 1 or mk:
        bad += 1
        print("BAD", d["page"], ascii(fx["old"]), n, mk)
# overlaps between fixes on the same page
for p in sorted({d["page"] for d in F}):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            k = t.find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, ascii(a[2]), ascii(b[2]))
print("findings", len(F), "bad", bad)
for p in sorted({d["page"] for d in F}):
    n = sum(1 for d in F if d["page"] == p and d["kind"] != "misprint_in_print")
    m = sum(1 for d in F if d["page"] == p and d["kind"] == "misprint_in_print")
    print(p, f"{n}/{m}")
if bad == 0 and "--write" in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
