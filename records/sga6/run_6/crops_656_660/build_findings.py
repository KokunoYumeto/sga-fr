"""Build findings_656_660.json and check that every fix's old occurs exactly once in its page_NNN.tex.
usage: python -I build_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b656_660"
OUT = RUN / "findings_656_660.json"
NL = "\n"


def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 656 ----------------
    F(656, "start of page (folio-656 marker)",
      "p. 656 begins 'De s ≥ 1, résulte G' ≠ 0 ; par suite, F' n'est pas contenu dans F(-1) ;' under the running "
      "head '- 41 -' (both scans; crops_656_660/w656_top.png)",
      r"'De $s\ge1$, r\'' is the last line of page_655.tex, above the folio-656 marker; page_656.tex begins "
      r"'esulte $G'\ne0$': the marker splits r\'esulte between the accent and its e",
      "marker", "high", None,
      r"Page 656 really begins at 'De $s\ge1$, r\'esulte'. Exact edit in main.tex, both layers (the old string "
      r"occurs once in each; simulated in memory on both layers, crops_656_660/sim_markers.py): replace "
      r"'De $s\ge1$, r\'\n%%%%%%%%%%  scan idx 669  |  folio 656  %%%%%%%%%%\nesulte $G'\ne0$' by "
      r"'%%%%%%%%%%  scan idx 669  |  folio 656  %%%%%%%%%%\nDe $s\ge1$, r\'esulte $G'\ne0$' (marker above the "
      r"line, the word rejoined). Equivalent: python -I move_marker.py 6 656 'De $s\ge1$, r' --before, then join "
      r"'r\'' with 'esulte'. Independent of the other page-656 fixes. The same boundary seen from page_655.tex (batch 651-655): apply once."),
    F(656, "after (i) of the proof of 6.5: 'd'où (i).' / 'L'assertion (ii) résulte immédiatement de (i)'",
      "'L'assertion (ii)' starts a new, indented paragraph after the short line 'H^o(F(-1)) ⟶ H^o(F), d'où (i).' "
      "(both scans)",
      r"'d'o\`u (i). L'assertion (ii)' in one paragraph",
      "other", "high",
      {"old": r"d'o\`u (i). L'assertion", "new": r"d'o\`u (i)." + NL + NL + r"L'assertion"},
      "Missing paragraph break. 'Dans (iii), on trouve' further on starts at the margin: the print runs on there, "
      "as the TeX does."),
    F(656, "proof of (iii): 'h^o(G(1-n_o))+...+h^o(G(p-n_o))'",
      "'+...+': three typed full stops on the baseline (both scans)",
      r"+\cdots+",
      "symbol", "medium",
      {"old": r"+\cdots+", "new": r"+\ldots+"},
      r"\cdots sets the dots at mid-height (same kind of fix as pp. 49, 79, 80, 618, 619; for Exposé V a volume "
      r"decision, GLOBAL_ISSUES 87). The only \cdots on pp. 656-660."),
    F(656, "after Proposition 6.6: 'En effet, soit σ une section \"générale\" de O_X(1)'",
      "'En effet, soit σ' starts a new, indented paragraph after a blank line (both scans)",
      r"\emph{...-faisceau.}\nEn effet (single line break: same paragraph as the statement)",
      "other", "high",
      {"old": "-faisceau.}" + NL + "En effet", "new": "-faisceau.}" + NL + NL + "En effet"},
      "Missing paragraph break (pp. 657 and 658 have the blank line before their 'En effet')."),
    F(656, "the structure sheaf O, pp. 656-660 (convention of the Exposé XIII transcription, reported once; 29 "
           "places: p. 656 one, p. 657 one, p. 658 six, p. 659 eight, p. 660 thirteen)",
      "a plain typed capital O, never underlined, on every page: p. 656 'section \"générale\" de O_X(1)' "
      "(crops_656_660/m656_OX.png); p. 657 Théorème 6.7 'F un quotient de O_P(-m)^{⊕M}' (the underline of 'un "
      "quotient de' stops before O); p. 659 'l'injection O_X ⟶ ∐ O_{X_j}' (crops_656_660/m659_coprod.png); the "
      "same on p. 658 (O_X(1) in 6.8 and 6.9, O_{X'_j}(1), χ(O_X(n)), 'Alors O_X est') and p. 660 (O_P, O_X, "
      "O_{X_n}, O_Y, O_Z) (both scans)",
      r"\mathcal O in all 29 places",
      "font", "medium", None,
      r"CONVENTION, not itemized: as reported for pp. 616-619 (findings_616_620) and 631-632 (findings_631_635), "
      r"the Exposé XIII TeX writes \mathcal O for the typist's plain O (as SGA 5, GLOBAL_ISSUES 89 (f)); this "
      r"differs from the underlined O of the pending NOTE_6 decision (\cO / \underline O). One decision for the "
      r"exposé."),
    # ---------------- page 657 ----------------
    F(657, "start of page: 'Supposons q=1.'",
      "'Supposons q=1. Alors ...' is indented: a new paragraph (p. 656 ends with the short line 'fondeur).') "
      "(both scans)",
      r"'(question de profondeur).' (end of page_656.tex), the marker line, then 'Supposons $q=1$.': no blank "
      r"line, so the comment line joins the two paragraphs",
      "other", "high",
      {"old": "Supposons $q=1$.", "new": NL + "Supposons $q=1$."},
      "Missing paragraph break at the page boundary; the fix puts an empty line right after the folio-657 marker "
      "line (the marker line itself is unchanged)."),
    F(657, "first paragraph, 'Alors dim.supp(N_q) = 0'",
      "dim.supp(N_q): a full stop between dim and supp (both scans; witness crops_656_660/w657_a.png)",
      r"$\dim\operatorname{supp}(N_q)=0$ (prints 'dim supp')",
      "punctuation", "high",
      {"old": r"$\dim\operatorname{supp}(N_q)=0$", "new": r"$\operatorname{dim{.}supp}(N_q)=0$"},
      r"The exposé writes the print's dim.supp as \operatorname{dim{.}supp} on pp. 619-621 (four places)."
      r""),
    F(657, "first paragraph, 'h^o(F_q(-1) ≤ h^o(F(-1)) ≤ b_o'",
      "h^o(F_q(-1) ≤ h^o(F(-1)) ≤ b_o: the closing parenthesis after F_q(-1) is missing (both scans)",
      r"$h^0(F_q(-1)\le h^0(F(-1))\le b_0$ (keeps the printed reading)",
      "misprint_in_print", "high", None,
      "Typing error, kept by the TeX.",
      corrected=r"$h^0(F_q(-1))\le h^0(F(-1))\le b_0$"),
    F(657, "remark after Théorème 6.7 (ii), '(Remarquons que a^{(q)}_{q-1} ≤ a_{q-1} et a^{(q)}_q et a^{(q)}_q = "
           "a_q,...'",
      "'a^{(q)}_{q-1} ≤ a_{q-1} et a^{(q)}_q et a^{(q)}_q = a_q,...,a^{(q)}_r = a_r': 'et a^{(q)}_q' typed twice "
      "(both scans; crops_656_660/w657_b.png)",
      r"'$a_{q-1}^{(q)}\le a_{q-1}$ et $a_q^{(q)}$ et $a_q^{(q)}=a_q,\ldots$' (keeps the printed reading)",
      "misprint_in_print", "medium", None,
      "Dittography, kept by the TeX: the remark states a^{(q)}_{q-1} ≤ a_{q-1} and a^{(q)}_i = a_i for i ≥ q "
      "(dim supp N_q ≤ q-1); the first 'et a^{(q)}_q' has no relation.",
      corrected=r"$a_{q-1}^{(q)}\le a_{q-1}$ et $a_q^{(q)}=a_q,\ldots,a_r^{(q)}=a_r$"),
    F(657, "same remark, 'puisque dim.supp(N_q) ≤ q-1)'",
      "dim.supp(N_q): a full stop between dim and supp (both scans)",
      r"$\dim\operatorname{supp}(N_q)\le q-1$ (prints 'dim supp')",
      "punctuation", "high",
      {"old": r"$\dim\operatorname{supp}(N_q)\le q-1$", "new": r"$\operatorname{dim{.}supp}(N_q)\le q-1$"},
      "As the first dim.supp of the page."),
    F(657, "proof of 6.7, 'soit une suite exacte 0 → F(-1 → F → G → 0'",
      "0 → F(-1 → F → G → 0: the closing parenthesis of F(-1) is missing (both scans)",
      r"$0\to F(-1\to F\to G\to0$ (keeps the printed reading)",
      "misprint_in_print", "high", None,
      "Typing error, kept by the TeX.",
      corrected=r"$0\to F(-1)\to F\to G\to0$"),
    # ---------------- page 658 ----------------
    F(658, "Définition 6.9, 'comme image inverse d'un k_j-schéma intègre X'_j'",
      "'intègre' is not underlined, between the underlined 'schéma' and '(muni de' (both scans; "
      "crops_656_660/m658_integre.png, w658_def.png)",
      r"int\`egre inside the statement's \emph (italic), unlike the defined terms the print leaves plain, which "
      r"the TeX sets in a nested \emph",
      "underline", "low",
      {"old": r"sch\'ema int\`egre $X'_j$", "new": r"sch\'ema \emph{int\`egre} $X'_j$"},
      r"The nested \emph prints it upright, as the file already does for '$k$-cycle positif spécial de dimension "
      r"$r$' and 'degré' in the same definition. Low: the typist may simply have missed the word."),
    # ---------------- page 659 ----------------
    F(659, "start of page (folio-659 marker)",
      "p. 659 begins 'En effet, soit X dans ℙ^N_k .' (indented) under the running head '- 44 -'; p. 658 ends "
      "with Lemme 6.10 '... Alors O_X est un (0,...,0,d)-faisceau.' (both scans)",
      r"'En' is the last line of page_658.tex, above the folio-659 marker; page_659.tex begins 'effet, soit $X$'",
      "marker", "high", None,
      r"Page 659 really begins at 'En effet'. Exact edit in main.tex, both layers (once in each; simulated in "
      r"memory, crops_656_660/sim_markers.py): replace '\nEn\n%%%%%%%%%%  scan idx 672  |  folio 659  "
      r"%%%%%%%%%%\neffet, soit $X$' by '\n%%%%%%%%%%  scan idx 672  |  folio 659  %%%%%%%%%%\nEn effet, soit "
      r"$X$'. Equivalent: python -I move_marker.py 6 659 En --before (leaves 'En' and 'effet' on two lines, "
      r"which prints the same)."),
    F(659, "proof of 6.10, 'sont toujours des k-cycles positifs spéciaux de degré d.' / 'Raisonnant par "
           "récurrence sur r'",
      "'Raisonnant par récurrence sur r, il reste donc à noter que' starts a new, indented paragraph (both scans)",
      r"'... de degr\'e $d$. Raisonnant par r\'ecurrence' in one paragraph",
      "other", "high",
      {"old": r"de degr\'e $d$. Raisonnant", "new": r"de degr\'e $d$." + NL + NL + "Raisonnant"},
      "Missing paragraph break."),
    F(659, "proof of 6.10, 'grâce à l'injection O_X ⟶ ∐ O_{X_j}'",
      "a bare coproduct sign (typed 11 on a base line), nothing under it; the j is only the index of X_j (both "
      "scans; crops_656_660/m659_coprod.png, w659_mid.png)",
      r"\coprod_j\mathcal O_{X_j}",
      "extra", "high",
      {"old": r"\coprod_j\mathcal O_{X_j}", "new": r"\coprod\mathcal O_{X_j}"},
      "The TeX adds the summation index (as pp. 190, 635)."),
    # ---------------- page 660 ----------------
    F(660, "start of page (folio-660 marker)",
      "p. 660 begins 'En effet, dans (i), la première assertion résulte de 6.7 (i) ;' (indented) under the "
      "running head '- 45 -'; p. 659 ends with Corollaire 6.11 (ii) '... dans un sens abstrait évident).' (both "
      "scans)",
      r"'En' is the last line of page_659.tex, above the folio-660 marker; page_660.tex begins 'effet, dans (i)'",
      "marker", "high", None,
      r"Page 660 really begins at 'En effet'. Exact edit in main.tex, both layers (once in each; simulated in "
      r"memory, crops_656_660/sim_markers.py): replace '\nEn\n%%%%%%%%%%  scan idx 673  |  folio 660  "
      r"%%%%%%%%%%\neffet, dans (i)' by '\n%%%%%%%%%%  scan idx 673  |  folio 660  %%%%%%%%%%\nEn effet, dans "
      r"(i)'. Equivalent: python -I move_marker.py 6 660 En --before."),
    F(660, "after the display of Corollaire 6.13: 'En effet, soit I = Ker(α)'",
      "'En effet, soit I = Ker(α)' starts a new, indented paragraph after the display (both scans)",
      r"\]\nEn effet (no blank line: the text continues the paragraph of the display, unindented)",
      "other", "high",
      {"old": r"\]" + NL + "En effet, soit $I", "new": r"\]" + NL + NL + "En effet, soit $I"},
      "Missing paragraph break."),
]

ok = True
for x in findings:
    fx = x["fix"]
    if fx is None:
        continue
    t = (B / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("marker line in fix:", x["page"], x["where"])
    print(x["page"], n, repr(fx["old"])[:70])
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(findings), "findings; all olds unique:", ok)
counts = {}
for x in findings:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print(counts)
