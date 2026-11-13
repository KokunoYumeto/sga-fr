"""Write run_6/findings_546_550.json (SGA 6, pp. 546-550) and check that every fix's old occurs exactly once on its page."""
import json
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------- page 546 ----------------
add(546, "start of page (folio-546 marker)",
    "p. 546 begins '4.5 On appelle équivalence numérique la relation d'équivalence', the heading number run into "
    "the first line; p. 545 ends '... d'où l'assertion.' (both scans)",
    r"'\subsection*{4.5}' and 'On' are the last two lines of page_545.tex (under the folio-545 marker); "
    r"page_546.tex begins 'appelle équivalence numérique'",
    "marker", "high", None,
    r"Page 546 really begins with the heading 4.5 and 'On' (a heading at the top of a page, which the 10 Nov script "
    r"did not move). Move the folio-546 marker above the heading: python -I move_marker.py 6 546 "
    r"'\subsection*{4.5}' --before (single quotes). Simulated in memory on both layers of the present main.tex "
    r"with crops_546_550/sim_marker.py: '... d'où l'assertion.', blank line, the marker, '\subsection*{4.5}', 'On', "
    r"'appelle équivalence numérique ...'. ALREADY APPLIED: when this check ended, both layers of main.tex "
    r"had the folio-546 marker above '\subsection*{4.5}' (the p. 545 side of the same boundary); nothing "
    r"left to do, do not run the command again.")
add(546, "Définition 4.5.1, first line, '(i ∈ Z)'",
    "(i ∈ Z) with an ordinary typed Z (thin single strokes, serifs), unlike the overstruck double-struck Z of "
    "'Gr_i(X) ⟶ Z', 'n ∈ Z' and '_{i ∈ Z}' on the same page (both scans; crops_546_550/z546.png, w546_iZ.png)",
    r"\((i\in\mathbb Z)\)", "font", "low",
    fx(r"\((i\in\mathbb Z)\)", r"\((i\in Z)\)"),
    "The typist's plain letter for the double-struck Z: the same open question as the typist's plain Q (NOTE_6; "
    "SGA 7 II issue 61; GLOBAL_ISSUES 77(f), 78). Apply only if the diplomatic layer reproduces it.")
add(546, "'Corollaire 4.5.3.' after Proposition 4.5.2 and its formula (4.5.3)",
    "Corollaire 4.5.3. Pic^τ(X) ⊂ Pic^N(X) . : the same number as the formula (4.5.3) five lines above (both scans)",
    r"\textbf{Corollaire 4.5.3.} (printed reading kept)", "misprint_in_print", "medium", None,
    "Numbering slip of the print: Exposé X numbers statements and formulas in one sequence (5.1.1-5.1.3; 5.2.1, "
    "Remarques 5.2.2, (5.2.3), (5.2.4); (5.3.1), Théorème 5.3.2, (5.3.3), Lemme 5.3.4, (5.3.5)), so the corollary "
    "after (4.5.3) is 4.5.4. Nothing in main.tex cites it. The TeX keeps the printed 4.5.3, and so does the "
    "corrected layer.",
    corrected=r"\textbf{Corollaire 4.5.4.}")
add(546, "heading 5.1", "5.1. (trailing full stop; both scans)", r"\subsection*{5.1}", "punctuation", "high",
    fx(r"\subsection*{5.1}", r"\subsection*{5.1.}"),
    "The printed paragraph number ends with a full stop (also 5.2. and 5.3. on pp. 547-548; the heading 4.5 has none).")
add(546, r"K˙ and cl˙ throughout pp. 546-550 (K^\circ: 1, 6, 1, 0, 3 places; \cl^\circ: 0, 1, 1, 1, 3 places on "
    "pp. 546-550)",
    "K and cl with a raised filled dot (K˙, cl˙) in every place (both scans; crops_546_550/k546.png, w546_K.png)",
    r"K^\circ and \cl^\circ (a raised ring)", "symbol", "high", None,
    r"Convention of the Exposé X TeX, as reported for Exposé IX (findings_501_505, findings_506_510): K^\circ for "
    r"the print's K˙ on folios 522-563 (about 50 in main.tex; K^\bullet only from folio 564, and one K^{\bullet} on "
    r"folio 519) and \cl^\circ for cl˙ (28): not itemized. Three examples: p. 546 'l'anneau \(K^\circ(X)\)' -> "
    r"'l'anneau \(K^{\bullet}(X)\)'; p. 547 'l'élément \(\cl^\circ(L)\) de \(K^\circ(X)\)' -> 'l'élément "
    r"\(\cl^{\bullet}(L)\) de \(K^{\bullet}(X)\)'; p. 550 '\((x,y\in K^\circ(X))\)' -> "
    r"'\((x,y\in K^{\bullet}(X))\)'. Same fix as for Exposés IV and VI on 10 Nov (K^\circ -> K^{\bullet}). No old "
    r"string in this file contains K^\circ or \cl^\circ.")
add(546, "statements: Définition 4.5.1 and Proposition 4.5.2 (p. 546), Théorème 5.3.2 (p. 549), Lemme 5.3.4 (p. 550)",
    "each statement underlined word group by word group; math letters (x, y, X, c_1, α) and some small words left "
    "out of the underline (both scans)",
    "the statements set in roman, without underline or emphasis", "underline", "high", None,
    "Exposé X follows the Exposé II pattern of GLOBAL_ISSUES 82 (pending volume decision), as Exposés VII and IX do "
    "(findings_416_420, findings_501_505, findings_506_510): not itemized. The TeX adds no emphasis on defined "
    "terms on these pages; pp. 546-550 have no category letter.")
add(546, "underlined letters throughout pp. 546-550 (about 30 places; first: Définition 4.5.1, 'L_1 et L_2')",
    "the print underlines the letters that name sheaves and sections of sheaves: the invertible modules L_1, L_2, L, "
    "the locally free modules E, E', E'', the rank n (a section of Z_X), the final object e and the e_i, the N of "
    "(5.3.3); classes stay plain (both scans; crops_546_550/d546.png, n547.png, lam547z.png, eq533.png)",
    r"plain letters, except '\underline n' (twice) and '\cl^\circ(\underline E)' on p. 550", "underline", "high",
    None,
    r"Convention of the Exposé X TeX: underlined letters written plain, except where a formula sets the sheaf "
    r"against its class (p. 550 '\underline n=n', 'E=\cl^\circ(\underline E)'; p. 542 'L_i=\cl^\circ(\underline "
    r"L_i)'), as reported for Exposés VI, VII and IX (findings_401_405, findings_441_445, findings_501_505, "
    r"findings_506_510): not itemized, and not a blind script, because the print keeps classes plain (L ∈ Pic(X), "
    r"δ(L) = 1-L^{-1}, L = cl˙(O_S(D)), λ^n(E), γ^i(E-n)). Places on pp. 546-550, to underline if the diplomatic "
    r"layer reproduces the print: p. 546 '\(L_1\) et \(L_2\)', 'inversible \(L\) est', the L of (4.5.3) "
    r"('\chi(L^n'); p. 547 '\cl_P(L)', 'inversible \(L\) l'élément', '\cl^\circ(L)', 'Lorsque \(E\) est', 'de rang "
    r"\(n\), on a', '\det(E)=\bigwedge^n E.' (both E, and the n set above the wedge), E', E and E'' of (5.1.2), "
    r"the three E of '\det(E)\xrightarrow{\sim}(\det(E'))\otimes_{\mathcal O_X}(\det(E''))'; p. 549 'section \(n\) "
    r"du faisceau', 'l'objet final \(e\) de', 'section \(n\) de \(\mathbb Z_X\)' (the page's last line, '... cl˙(E) "
    r"- n, où E est un', is cut off below the x-height in both scans, so its underlines cannot be read); p. 550 'de "
    r"rang \(n\), il suffit', the two E and the N of (5.3.3), 'Comme \(n\) est bornée', 'l'objet final \(e\) de', "
    r"'\(X/e_i\)', 'que \(n\) est constante', the first E of '\det(E)=\lambda^n(E)' (the e_i of '\coprod e_i' is "
    r"plain in the print). Forms: \underline L_1, \underline{E}', \underline n, \underline e_i. On p. 550 the TeX "
    r"writes the same section n̲ plain three times and \underline n twice in one paragraph. The underlined O written "
    r"\mathcal O falls under the pending volume decision.")

# ---------------- page 547 ----------------
add(547, "start of page (folio-547 marker)",
    "p. 547 begins with the display '(5.1.1)  i : Pic(X) ⟶ K˙(X)'; p. 546 ends '... des O_X-modules inversibles. "
    "On dé-signe par' (both scans)",
    r"'\begin{equation}\tag{5.1.1}' is the last line of page_546.tex (under the folio-546 marker); page_547.tex "
    r"begins inside that equation with ' i:\Pic(X)\longrightarrow K^\circ(X)'",
    "marker", "high", None,
    r"Page 547 really begins with the equation (5.1.1). Move the folio-547 marker above its first line: "
    r"python -I move_marker.py 6 547 '\begin{equation}\tag{5.1.1}' --before (single quotes). Simulated in memory "
    r"on both layers with crops_546_550/sim_marker.py: '... On désigne par', the marker, "
    r"'\begin{equation}\tag{5.1.1}', ' i:\Pic(X)\longrightarrow K^\circ(X)', '\end{equation}'. Independent of the "
    r"folio-546 move.")
add(547, "heading 5.2", "5.2. (trailing full stop; both scans)", r"\subsection*{5.2}", "punctuation", "high",
    fx(r"\subsection*{5.2}", r"\subsection*{5.2.}"),
    "The printed paragraph number ends with a full stop.")

# ---------------- page 548 ----------------
add(548, "(5.2.3), 'θ_S(δ(L)) = cl.(O_D)'",
    "a small θ: a barred o at x-height (a typed o overstruck by a hyphen), not a capital: lower than the δ and the "
    "L beside it (both scans; crops_546_550/th548.png)",
    r"\Theta_S(\delta(L))", "symbol", "medium",
    fx(r"\Theta_S(\delta(L))", r"\theta_S(\delta(L))"),
    r"Lower-case theta in the print, capital in the TeX. The same x-height θ is written \Theta on p. 523 "
    r"(θ_X twice, Corollaire 1.3.3) and p. 534 (θ_y, 2.2), seen on b521_525/page_523_s3.png and "
    r"b531_535/page_534_s3.png; these are the only five \Theta of Exposé X.")
add(548, "'où θ_S : K˙(X) ⟶ K.(S) est l'homomorphisme canonique de 1.2.3.'",
    "the same small θ, at the height of the o and u of 'où' (both scans; crops_546_550/th548b.png)",
    r"où \(\Theta_S:K^\circ(X)\to K_\bullet(S)\)", "symbol", "medium",
    fx(r"où \(\Theta_S:", r"où \(\theta_S:"),
    r"As in (5.2.3). The old string stops before K^\circ, so the entry applies before or after the K˙ script.")
add(548, "heading 5.3", "5.3. (trailing full stop; both scans)", r"\subsection*{5.3}", "punctuation", "high",
    fx(r"\subsection*{5.3}", r"\subsection*{5.3.}"),
    "The printed paragraph number ends with a full stop.")

# ---------------- page 549 ----------------
add(549, "'Admettons pour l'instant que' after the display of the proof",
    "'Admettons pour l'instant que' begins a new, indented paragraph (both scans)",
    r"'\]' followed directly by 'Admettons' (the paragraph runs on)", "other", "high",
    fx("\\]\nAdmettons", "\\]\n\nAdmettons"),
    "Missing paragraph break.")

# ---------------- page 550 ----------------
add(550, "start of page (folio-550 marker)",
    "p. 550 begins 'O_X-module localement libre de rang n , il suffit de montrer, ...'; p. 549 ends '... engendré "
    "par les éléments cl˙(E) - n, où E est un' (both scans; that last line is cut off below the x-height in both)",
    r"'\(\mathcal O_X\)-' ends the last line of page_549.tex (under the folio-549 marker); page_550.tex begins "
    r"'module localement libre'",
    "marker", "high", None,
    r"Page 550 really begins with 'O_X-module'. Move the piece across the marker: python -I marker_split_word.py 6 "
    r"550 pull '\(\mathcal O_X\)-' (single quotes). Simulated in memory on both layers with "
    r"crops_546_550/sim_pull.py: '... où \(E\) est un', the marker, '\(\mathcal O_X\)-module localement libre de "
    r"rang \(n\), ...'. This also removes the space that the line end after '\(\mathcal O_X\)-' now puts between "
    r"'O_X-' and 'module' in the output.")
add(550, "'une somme directe finie disjointe'", "finie underlined (both scans; crops_546_550/coprod550.png)",
    "directe finie disjointe", "underline", "high",
    fx("directe finie disjointe", r"directe \emph{finie} disjointe"),
    r"Underlined word. This part of main.tex writes underlined words with \emph (\emph{tout}, \emph{seules}, "
    r"\emph{intègre} in Exposé X).")
add(550, "'transforme sommes directes finies en produits directs finis'",
    "finies underlined; finis not (both scans)", "sommes directes finies en", "underline", "high",
    fx("sommes directes finies en", r"sommes directes \emph{finies} en"),
    "Underlined word, as 'finie' two lines above.")
add(550, "(5.3.3), 'det(cl˙(E)) - cl˙(E) + N - 1 ∈ Filt^2(X)'",
    "an underlined capital N, the height of the E of the formula (both scans; crops_546_550/eq533.png)",
    "+N-1 (printed letter kept)", "misprint_in_print", "high", None,
    "Typing error: the term is the rank n̲ of E ('cl˙(E) - n' at the foot of p. 549, 'de rang n̲' on the line "
    "above; with 5.2.2 b), det(E) - 1 ≡ cl˙(E) - n mod Filt^2). The diplomatic TeX keeps the printed N (its "
    "underline belongs to the underlined-letter convention, entry on p. 546); the corrected layer already reads n.",
    corrected="+n-1")
add(550, "Démonstration of Lemme 5.3.4, 'Alors (6.2.8) et (6.5.8) ci-dessous'",
    "(6.5.8), clearly in both scans (crops_546_550/ref650.png, w550_ref.png); § 6.5 of the print ends with (6.5.5) "
    "on p. 559 (crops_546_550/wit_559_small.png), and no 6.5.8 exists in the exposé",
    "(6.5.8) (printed reading kept)", "misprint_in_print", "low", None,
    "Wrong reference number in the print: (5.3.5) follows by linearity from (6.2.8), det(E_1 ⊗ E_2) = "
    "det(E_1)^{n_2} ⊗ det(E_2)^{n_1}, and 6.5.3 is the remark that makes (6.2.8)-(6.2.10) valid on any ringed "
    "topos ('Donc en particulier les formules (6.2.8),(6.2.9) et (6.2.10) restent valables sur un topos annelé "
    "quelconque', p. 559). Most likely 6.5.3; low because the intended number is inferred. The TeX keeps 6.5.8, "
    "and so does the corrected layer.",
    corrected="(6.5.3)")
add(550, "Démonstration of Lemme 5.3.4, '(6.2.8) et (6.5.8) ci-dessous donne par linéarité la formule'",
    "donne (both scans)", "donne (printed reading kept)", "misprint_in_print", "medium", None,
    "Agreement slip of the print: two subjects joined by 'et'. The TeX keeps the printed reading, and so does the "
    "corrected layer.",
    corrected="donnent")

# ---------------- check and write ----------------
ok = True
for d in F:
    if d["fix"]:
        t = (RUN / "b546_550" / f"page_{d['page']}.tex").read_text(encoding="utf-8")
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
        marker_lines = [ln for ln in t.splitlines() if "scan idx" in ln]
        if any(ml in d["fix"]["old"] for ml in marker_lines) or "scan idx" in d["fix"]["old"]:
            ok = False
            print("TOUCHES MARKER", d["page"])
out = RUN / "findings_546_550.json"
out.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
c = Counter((d["page"], d["kind"] == "misprint_in_print") for d in F)
for p in range(546, 551):
    print(p, f"{c[(p, False)]}/{c[(p, True)]}")
print("entries", len(F), "all unique" if ok else "PROBLEMS")
