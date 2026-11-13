"""Build findings_396_400.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
NL = "\n"
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b396_400"
OUT = RUN / "findings_396_400.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 396
add(396,
    "Lemme 4.3 ii), end of the statement at the top of the page: '(c_i et c_i^{(j)} étant effectués du poids i)'",
    "'étant effectués du poids i' (both scans)",
    r"'étant effectués du poids \(i\)' (the printed reading)",
    "misprint_in_print", "medium", None,
    r"Wrong word for 'affectés' (the c_i and c_i^{(j)} are given the weight i), as Exposé V writes '\(\gamma^k X\) étant affecté du poids \(k\)' (main.tex line 8205). The diplomatic layer is right; the current layer also still reads 'effectués' (current line 9955), so the corrected edition needs the change.",
    corrected="affectés")

add(396,
    "Corollaire 4.4, display 'ξ_1^{α_1} ... ξ_{n-1}^{α_{n-1}},  0 ≤ α_i ≤ n-i ,'",
    "the three dots are typed on the baseline (both scans; crops_396_400/c396_xi.png, w396_xi.png)",
    r"\cdots (dots at mid-height)",
    "symbol", "medium",
    {"old": r"\xi_1^{\alpha_1}\cdots\xi_{n-1}", "new": r"\xi_1^{\alpha_1}\ldots\xi_{n-1}"},
    r"Same kind of fix as pp. 389-390 (findings_386_390: \cdots -> \ldots for typed baseline dots).")

add(396,
    "heading 4.5",
    "'4.5.' with a full stop, run into the text",
    r"\subsection*{4.5} (no full stop)",
    "punctuation", "low",
    {"old": r"\subsection*{4.5}", "new": r"\subsection*{4.5.}"},
    r"Only the stop is at issue (the new paragraph and the bold number are covered by the global rule and the pending bold-number decision). §1 writes \subsection*{1.2.} with the stop (main.tex line 9165); \subsection*{4.1}, {4.9}, {5.1}, {5.2} lack it. Drop if the stops are settled with the bold-number decision.")

add(396,
    "letters of sheaves and Modules on pp. 396-400",
    "underlined in the print: p. 396 E (4 times: 'E un O_S-Module', D_π(E), f^*(E), 'la classe de E.'), L_i (twice), L_o, L_k, L_{i-1}, F_i, F_j ('la classe de F_j', Λ^i(F_j)); p. 397 E (Corollaire 4.7 twice, g^*(E), and the E of every P(E), D(E)), F_1,...,F_n (Corollaire 4.7), F (the exact sequence, every D(F)); p. 398 F_j (3 times) and the E of every D(E), D_π(E); p. 399 E ('l'image inverse de E') and the E of D(E) (twice); p. 400 F_1, F_2 ('Soient F_1, F_2 les faisceaux canoniques'). Plain in the print: the classes F_j ('On note F_j'), E ('où E est'), F_1,...,F_k, F_i, F'_i, the F_1, F_2 of 'leur classe', the E, F_j, F_1, F_2 inside λ_t, λ^i, γ_t, γ^i, and S, X, A, B, C, f, g, h (both scans)",
    "all plain",
    "underline", "high", None,
    r"Convention of the Exposé VI transcription, reported for pp. 366-390 (findings_381_385, findings_386_390): not itemized. On these pages the underline is what tells a sheaf from its class: 'On note \(F_j\) la classe de \(F_j\)' and 'où \(E\) est la classe de \(E\)' (p. 396), '\(F_1,F_2\) les faisceaux canoniques ... et \(F_1,F_2\) leur classe' (p. 400). Three examples, in the form to use if the diplomatic layer reproduces it: p. 396 'la classe de \(F_j\), et' -> 'la classe de \(\underline{F}_j\), et'; p. 396 'la classe de \(E\). Enfin' -> 'la classe de \(\underline{E}\). Enfin'; p. 400 'Soient \(F_1,F_2\) les faisceaux' -> 'Soient \(\underline{F}_1,\underline{F}_2\) les faisceaux'. The underlined structure sheaf O stays \mathcal O (pending volume decision).")

add(396,
    "flag bundles D(E), D(F), D_π(E) (pp. 396-399) and grassmannians G_S^{n,r}, G_S^{n,r+1}, G_S^{n,∞} (pp. 399-400): 28 places",
    "D and G doubly underlined in every place (both scans), the print's mark for a bold letter, as for the P of P(E) and the S of Sym",
    "plain D (p. 396: 1, p. 397: 4, p. 398: 7, p. 399: 2) and plain G (p. 399: 5, p. 400: 9)",
    "font", "high", None,
    r"""Convention of the § 4 transcription, reported once (the three D of Proposition 3.1, p. 390, were itemized and are now \mathbf D, main.tex line 9843). One scripted pass on folios 396-400, both layers (diplomatic lines 9947-10058, current 9953-10064): 'D(' and 'D_\pi(' not preceded by a letter or a backslash -> '\mathbf D(' and '\mathbf D_\pi(' (14), 'G_S^{' -> '\mathbf G_S^{' (14, including the index of \mathcal O_{G_S^{n,r}}); counted on the page files: 396 D 1; 397 D 4; 398 D 7; 399 D 2, G 5; 400 G 9. Three examples: p. 396 '\(X=D_\pi(E)\)' -> '\(X=\mathbf D_\pi(E)\)'; p. 397 'D(E)=D(F) \arrow[r,"h"]' -> '\mathbf D(E)=\mathbf D(F) \arrow[r,"h"]'; p. 400 'sera noté \(G_S^{n,\infty}\)' -> 'sera noté \(\mathbf G_S^{n,\infty}\)'. Folios 392, 394 (D_\pi(E), D(E), G_{r,n}(E) in 4.1-4.2) and 401 (G_S) are for those batches. No other fix in this file contains a D( or a G_S, so the pass can run before or after them.""")

add(396,
    "statements on pp. 396-400: end of Lemme 4.3 ii), Corollaire 4.4, Théorème 4.6 (p. 396), Corollaire 4.7 (p. 397), Corollaire 4.8 (p. 399), Proposition 4.10 (p. 400)",
    "underlined word groups (both scans): Lemme 4.3 ii) 'et' (between c_i and c_i^{(j)}), 'étant effectués du poids', 'et ces', 'relations engendrent / l'idéal des relations entre les'; Corollaire 4.4 'Les éléments de', 'de la forme', 'forment une base de', 'considéré comme module sur'; Théorème 4.6 'Avec les hypothèses et les notations de', 'la', 'algè-/bre', 'est engendrée par les', 'l'idéal des relations entre les', 'est engendré par les relations déduites de'; Corollaire 4.7 'Soient', 'un schéma quasi', 'compact' (the hyphen left out), 'un', '-Module locale-/ment de rang', 'le fibré en drapeaux de', 'les classes des / faisceaux inversibles', 'notation de', 'Alors', 'est la', 'algèbre engendrée par les', 'soumis aux relations'; Corollaire 4.8 'Avec les hypothèses et les notations de', 'posons', 'alors la', 'algèbre', 'est engendrée par les', 'l'idéal des / relations entre les', 'est engendré par les relations déduites de'; Proposition 4.10 'Soit', 'un schéma quasi', 'compact' (the hyphen left out), 'Alors', 'avec les notations / de', 'on a un isomorphisme'. Plain: the letters and formulas (c_i, n, C, A, S, X, K'(S)-, K'(X), λ_i^{(j)}, ξ_i, c_i^{(j)}), the numbers 4.5, 3.5), 4.9, the commas, ';', ':', '.:' and the displays; E, O_S, F_1,...,F_n carry their own underlines; the labels underline only 'Corollaire', 'Théorème', 'Proposition'",
    r"the statements in roman (no \underline, no \emph)",
    "underline", "high", None,
    "Exposé VI follows the Exposé II pattern of GLOBAL_ISSUES 82 (as on pp. 367-390): not itemized; the word groups are listed for the scripted pass. No emphasized defined terms and no category L on pp. 396-400.")

# ---------------------------------------------------------------- page 397
add(397,
    "Corollaire 4.7: 'E un O_S-Module locale-ment de rang n'",
    "'localement de rang n' (both scans): 'libre' is left out",
    r"'-Module localement de rang \(n\)' (the printed reading)",
    "misprint_in_print", "high", None,
    "The corollary is the case p_i = 1 of 4.5, whose E is 'localement libre de rang n'. The diplomatic layer is right; the current layer already reads 'localement libre de rang' (current line 9983).",
    corrected="localement libre de rang")

add(397,
    "P(E) on p. 397 (9 places: text, the index of O_{P(E)}(1) in the exact sequence, the diagram)",
    "P doubly underlined in every place (both scans), the same mark as the D and G of the page-396 entry and the S of Sym",
    r"\mathbb P (double-struck)",
    "font", "low", None,
    r"""Sections 1-2 of the exposé write the same printed P as \mathbf P (Théorème 1.1, Théorème 2.1, Proposition 2.6: main.tex lines 9143, 9567, 9727); sections 3-4 switch to \mathbb P (folios 391, 394 once each, 397 nine times). One decision for the exposé; if bold, '\mathbb P' -> '\mathbf P' on p. 397 (9 places). Three examples: 'on considère alors \(\mathbb P(E)\)' -> 'on considère alors \(\mathbf P(E)\)'; '\mathcal O_{\mathbb P(E)}(1)' -> '\mathcal O_{\mathbf P(E)}(1)'; '& \mathbb P(E) \arrow[d,"g"]' -> '& \mathbf P(E) \arrow[d,"g"]'. Low: a double-struck P may be kept for the print's doubly underlined P.""")

add(397,
    "diagram after 'Le diagramme :', bottom vertex 'S,'",
    "'S,' with a comma (both scans; crops_396_400/c397_diag.png)",
    "'& S' without the comma",
    "punctuation", "high",
    {"old": "& S" + NL + r"\end{tikzcd}", "new": "& S," + NL + r"\end{tikzcd}"},
    "The sentence goes on after the diagram ('montre que ...'); the TeX drops the printed comma. Labels h, f, g and the arrows agree with the print.")

add(397,
    "display 'ξ_2^{α_2}...ξ_{n-1}^{α_{n-1}},  avec 0 ≤ α_i ≤ n-i ;'",
    "the three dots are typed on the baseline (both scans; crops_396_400/c397_xi2.png)",
    r"\cdots",
    "symbol", "medium",
    {"old": r"\xi_2^{\alpha_2}\cdots", "new": r"\xi_2^{\alpha_2}\ldots"},
    "As the display of Corollaire 4.4 (p. 396).")

add(397,
    "display at the top of printed p. 398 'ξ_1^{α_1}...ξ_{n-1}^{α_{n-1}},  avec 0 ≤ α_i ≤ n-i.' (its first three TeX lines stand in page_397.tex: see the marker entry of p. 398)",
    "the three dots are typed on the baseline (both scans; crops_396_400/c398_xi1.png)",
    r"\cdots",
    "symbol", "medium",
    {"old": r"\xi_1^{\alpha_1}\cdots", "new": r"\xi_1^{\alpha_1}\ldots"},
    r"Printed on p. 398. The marker edit of p. 398 contains this \cdots: move the marker first (or use move_marker.py, which does not depend on it); after the move the old string is found under the folio-398 marker, still once.")

add(397,
    "'soumis aux relations (cf. V 4.6) : i) ... ; ii) ...'",
    "'i) λ^p(F_i) = 0 pour p > p_i ;' and 'ii) Σ_i F_i = E.' each on its own indented line (a displayed list, the i under the Σ), both scans",
    "both relations run into the paragraph",
    "other", "low",
    {"old": r"(cf. V 4.6)~: i) \(\lambda^p(F_i)=0\) pour \(p>p_i\) ; ii) \(\sum_i F_i=E\).",
     "new": r"(cf. V 4.6)~:" + NL + r"\begin{enumerate}[label=\textup{\roman*)}]" + NL
            + r"\item \(\lambda^p(F_i)=0\) pour \(p>p_i\) ;" + NL + r"\item \(\sum_i F_i=E\)." + NL
            + r"\end{enumerate}"},
    "Layout of the list only (the words and formulas agree); the environment is the one the file uses for Lemme 4.3 (main.tex line 9937). Low: drop if run-in lists are accepted.")

# ---------------------------------------------------------------- page 398
add(398,
    "start of page (folio-398 marker)",
    "p. 397 ends 'donc K'(X) admet pour base sur K'(S) les éléments :' and blank space; p. 398 begins with the display 'ξ_1^{α_1}...ξ_{n-1}^{α_{n-1}},  avec 0 ≤ α_i ≤ n-i.' (both scans)",
    r"the folio-398 marker stands inside that display: its first three lines ('\[', '  \xi_1^{\alpha_1}\cdots\xi_{n-1}^{\alpha_{n-1}},', '  \qquad') end page_397.tex; page_398.tex begins '\text{avec } 0\le\alpha_i\le n-i.'",
    "marker", "high", None,
    r"Page 398 really begins at the display's '\['. Move the marker up three lines: python -I move_marker.py 6 398 '\[' --before (simulated in memory: the last '\[' before the marker is this display's, diplomatic line 9999, current 10005). Exact edit in main.tex, both layers (diplomatic lines 9998-10002, current 10004-10008): replace 'les éléments~:\n\[\n  \xi_1^{\alpha_1}\cdots\xi_{n-1}^{\alpha_{n-1}},\n  \qquad\n%%%%%%%%%%  scan idx 411  |  folio 398  %%%%%%%%%%\n' by 'les éléments~:\n%%%%%%%%%%  scan idx 411  |  folio 398  %%%%%%%%%%\n\[\n  \xi_1^{\alpha_1}\cdots\xi_{n-1}^{\alpha_{n-1}},\n  \qquad\n' (once in each layer; crops_396_400/sim_marker398.py). Apply it before the \cdots entry of page_397 for this display, or write \ldots in both strings.")

add(398,
    "'Si C est la K'(S)-algèbre engendrée par des générateurs ξ_i, soumis aux relations :'",
    "a new indented paragraph after 'et les relations du corollaire sont vérifiées.' (both scans)",
    r"'... sont vérifiées. Si \(C\) est' in one paragraph",
    "other", "high",
    {"old": "vérifiées. Si", "new": "vérifiées." + NL + NL + "Si"},
    "Missing paragraph break.")

# ---------------------------------------------------------------- page 399
add(399,
    "'D'après 4.6, c'est homomorphisme est surjectif.'",
    "'c'est homomorphisme' (both scans; crops_396_400/c399_Fi.png)",
    "'c'est homomorphisme' (the printed reading)",
    "misprint_in_print", "high", None,
    "Typing slip for 'cet' (the next sentence: 'cet homomorphisme est aussi injectif'). The diplomatic layer is right; the current layer still reads 'c'est' (current line 10025), so the corrected edition needs the change.",
    corrected="cet homomorphisme")

add(399,
    "4.9: 'la grassmanienne de type (n,r-n)'",
    "'grassmanienne' with one n before -ienne (both scans)",
    "'grassmanienne' (the printed reading)",
    "misprint_in_print", "medium", None,
    "The current layer already reads 'grassmannienne' (current line 10039), as for the same word in 4.1 (folio 394, current line 9913).",
    corrected="grassmannienne")

add(399,
    "'Ce n'est qu'un autre énoncé de 4.6.' after the second display of Corollaire 4.8",
    "a new indented paragraph (both scans)",
    r"'\]' followed directly by 'Ce n'est' (same paragraph)",
    "other", "high",
    {"old": r"\]" + NL + "Ce n'est", "new": r"\]" + NL + NL + "Ce n'est"},
    "Missing paragraph break.")

add(399,
    "heading 4.9",
    "'4.9.' with a full stop, run into the text",
    r"\subsection*{4.9} (no full stop)",
    "punctuation", "low",
    {"old": r"\subsection*{4.9}", "new": r"\subsection*{4.9.}"},
    "As heading 4.5 (p. 396).")

# ---------------------------------------------------------------- page 400
add(400,
    "'Soient F_1, F_2 les faisceaux canoniques sur G_S^{n,r} (4.5)', after (4.9.1)",
    "a new indented paragraph (both scans)",
    r"'\end{equation}' followed directly by 'Soient' (same paragraph)",
    "other", "high",
    {"old": r"\end{equation}" + NL + "Soient", "new": r"\end{equation}" + NL + NL + "Soient"},
    "Missing paragraph break.")

add(400,
    "'et F_1, F_2 leur classe dans K'(G_S^{n,r})'",
    "'leur classe' (both scans)",
    "'leur classe' (the printed reading)",
    "misprint_in_print", "medium", None,
    "Two classes (F_1, F_2). The current layer already reads 'leurs classes' (current line 10048).",
    corrected="leurs classes")

add(400,
    "Proposition 4.10: 'on a un isomorphisme.:'",
    "a full stop before the colon, right after the underline (both scans; crops_396_400/c400_prop.png, w400_prop.png)",
    r"'isomorphisme.~:' (the printed reading)",
    "misprint_in_print", "high", None,
    "Stray full stop. The diplomatic layer is right; the current layer already reads 'isomorphisme~:' (current line 10050).",
    corrected=r"isomorphisme~:")

add(400,
    "Proposition 4.10, display K'(G_S^{n,∞}) ⥲ K'(S)[[c_1,...,c_n]] .",
    "a tilde over a right arrow (⥲), both scans (crops_396_400/c400_iso_z.png, w400_iso.png)",
    r"\simeq",
    "symbol", "high",
    {"old": r"\simeq K^{\bullet}(S)[[", "new": r"\xrightarrow{\sim} K^{\bullet}(S)[["},
    r"\xrightarrow{\sim} is the file's form for the printed ⥲ (as pp. 367, 381).")

add(400,
    "display 'γ_t(F_1-n).γ_t(F_2-r+n) = γ_t(r-r) = 1 ,'",
    "the product is a typed full stop on the baseline (witness crops_396_400/w400_gdot.png; the main scan agrees)",
    r"\cdot",
    "symbol", "medium",
    {"old": r"(F_1-n)\cdot\gamma_t", "new": r"(F_1-n).\gamma_t"},
    r"\cdot raises the typed stop to mid-height (as '1.u' p. 321 and 'λ^n(x).t^n' p. 325, findings_321_325). The speck before the second '=' in the main scan is not in the witness: a defect.")

add(400,
    "'Cette relation permet d'exprimer les γ^j(F_2-r+n) en fonction des c_i', after the display 'γ_t(F_2-r+n) = 1/γ_t(F_1-n) .'",
    "a new indented paragraph (both scans)",
    r"'\]' followed directly by 'Cette relation' (same paragraph)",
    "other", "high",
    {"old": r"\]" + NL + "Cette relation", "new": r"\]" + NL + NL + "Cette relation"},
    "Missing paragraph break.")

# ---------------------------------------------------------------- checks
bad = 0
ctrl = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
for d in F:
    for k, v in d.items():
        vals = [v] if isinstance(v, str) else (list(v.values()) if isinstance(v, dict) else [])
        for s in vals:
            if isinstance(s, str) and ctrl.search(s):
                print("CONTROL CHAR in", d["page"], k, repr(s[:60]))
                bad += 1
    fx = d["fix"]
    if fx is None:
        continue
    t = (B / f"page_{d['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    marker_cross = "%%%%%%%%%%" in fx["old"]
    status = "OK" if n == 1 and not marker_cross else "BAD"
    if status == "BAD":
        bad += 1
    print(status, d["page"], d["kind"], n, repr(fx["old"][:70]))
    # the new text applied must not create a second copy problem: check the edit result keeps the marker line
    t2 = t.replace(fx["old"], fx["new"], 1)
    assert t2.split("\n")[1] == t.split("\n")[1]

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts)
print("entries:", len(F), "bad:", bad)
if bad == 0:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("written", OUT)
