"""Write findings_066_070.json and check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
OUT = RUN / "findings_066_070.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 66 ----------------
add(66, "heading of no. 6",
    "'6. Constructibilité de ℝ Hom.' (underlined; a full stop after Hom)",
    "\\subsection*{6. Constructibilité de $\\R\\underline{\\Hom}$} (no full stop)",
    "punctuation", "high",
    {"old": "$\\R\\underline{\\Hom}$}", "new": "$\\R\\underline{\\Hom}$.}"},
    "As the headings of nos. 2, 3 and 5 (pp. 59, 60, 50).")

# ---------------- page 67 ----------------
add(67, "heading of no. 7 (top of the page)",
    "'7. Existence de complexes dualisants.' (underlined; a full stop at the end)",
    "\\subsection*{7. Existence de complexes dualisants} (no full stop)",
    "punctuation", "high",
    {"old": "{7. Existence de complexes dualisants}", "new": "{7. Existence de complexes dualisants.}"},
    "As the heading of no. 6 on p. 66.")
add(67, "Lemme 7.1, first line",
    "'G ∈ ob D^+_coh(X), alors': a comma (with its tail) before 'alors'",
    "$G\\in\\ob\\D^{+}_{\\mathrm{coh}}(X)$; alors",
    "punctuation", "high",
    {"old": "(X)$; alors", "new": "(X)$, alors"},
    "")
add(67, "Lemme 7.1, second line",
    "'ℝ Hom(F,G) ∈ D^+_coh(X) (notations de (1.2)).': no 'ob' after ∈ (the first line has '∈ ob' twice)",
    "\\R\\underline{\\Hom}(F,G)\\in\\ob\\D^{+}_{\\mathrm{coh}}(X)",
    "extra", "high",
    {"old": "(F,G)\\in\\ob\\D^{+}", "new": "(F,G)\\in\\D^{+}"},
    "The TeX adds \\ob where the print has none; the same on p. 68.")

# ---------------- page 68 ----------------
add(68, "Preuve of 7.3, line 3 ('Prouvons que l'on a ...')",
    "'ℝ Hom(F,K) ∈ D^b_coh(X). Soit x̄ ...': no 'ob' after ∈ (the line before has '∈ ob D^+_coh(X)')",
    "\\R\\underline{\\Hom}(F,K)\\in\\ob\\D^{b}_{\\mathrm{coh}}(X)",
    "extra", "high",
    {"old": "(F,K)\\in\\ob\\D^{b}", "new": "(F,K)\\in\\D^{b}"},
    "As in Lemme 7.1 (p. 67).")
add(68, "display after 'D'après (7.2), on a'",
    "ℝ Hom(F,K)_x̄ ⥲ ℝ Hom(F_x̄ , K_x̄ ). : a hand-drawn arrow with an arrowhead and a tilde above it (checked at 2.5x), unlike the plain ≃ (tilde over a bar) of p. 70",
    "\\simeq (no arrow)",
    "symbol", "high",
    {"old": "(F,K)_{\\bar{x}}\\simeq", "new": "(F,K)_{\\bar{x}}\\xrightarrow{\\sim}"},
    "The reverse of the ≃-for-arrow cases of pp. 36-53: here the print has the arrowhead.")
add(68, "commutative square, left vertical (labelled Id)",
    "Id | : a plain vertical line without arrowhead (the right vertical has its arrowhead)",
    "\\arrow[d,\"\\mathrm{Id}\"'] (an arrow)",
    "symbol", "high",
    {"old": "\\arrow[d,\"\\mathrm{Id}\"']", "new": "\\arrow[d,dash,\"\\mathrm{Id}\"']"},
    "tikz-cd's dash key draws the line without heads; a single line, not the double line of equal.")

# ---------------- page 69 ----------------
add(69, "top of the page",
    "p. 69 begins 'de X, et que le théorème de pureté au sens fort (4.4) est vrai sur X.'; p. 68 ends with Lemme 7.4's '... premier aux caractéristiques résiduelles'",
    "'de $X$, et que le théorème de' ends s5.tex line 1849 (as of 17:29), the last line of page_068.tex; the folio-69 marker (line 1850) follows it, so page_069.tex begins 'pureté au sens fort'",
    "marker", "high", None,
    "Page 69 really begins at 'de $X$, et que le théorème de' at the end of s5.tex line 1849 (as of 17:29). Exact fix: "
    "python -I move_marker.py 5 69 'de $X$, et que le théorème de' --before (single quotes keep the $ literal; "
    "simulated in memory on both layers at 17:29: the anchor occurs once before the marker, which then splits line 1849 "
    "after 'caractéristiques résiduelles'). Text not moved; it agrees with the print.")
add(69, "cartesian square of immersions, bottom row",
    "U' —i'→ X: the label i' stands above the arrow (as i'_p above the top arrow)",
    "U' \\arrow[r,\"i'\"'] & X. (the swap mark sets i' below the arrow)",
    "other", "high",
    {"old": "\\arrow[r,\"i'\"']", "new": "\\arrow[r,\"i'\"]"},
    "")
add(69, "'posons ... Y' = V(Σ div(s_i))': index under the Σ",
    "'l≤ i ≤ p-1': the first character is the typewriter's small letter l (foot serif on both sides, small top tick, as the l of 'la', 'langage'), not the digit 1 (flag, no foot: the 1 of 'p-1' in the same index and of 'I = {1,...,p}' just above); checked at 7x",
    "\\sum_{1\\leq i\\leq p-1}",
    "misprint_in_print", "medium",
    {"old": "\\sum_{1\\leq", "new": "\\sum_{l\\leq"},
    "Typing error, letter l for the digit 1 (the typewriter has the digit: same index, same line); the TeX "
    "silently corrects. Medium only because l-for-1 may be wanted under the same rule as the typescript's o for an "
    "index zero.",
    corrected="\\sum_{1\\leq i\\leq p-1}")

# ---------------- page 70 ----------------
add(70, "'Donc ... pour tout point géométrique ȳ de Y,'",
    "'de Y,': no index p (crisp; clean paper under the Y, the comma right after it; the Y_p of D^+_coh(Y_p) earlier in the line has its p)",
    "de $Y_p$,",
    "misprint_in_print", "high",
    {"old": "de $Y_p$, $(", "new": "de $Y$, $("},
    "ℝ j_p^!(K) lives on Y_p, so ȳ must be a point of Y_p. The TeX silently corrects.",
    corrected="de $Y_p$")
add(70, "display 'par le théorème de pureté, on a (4.3)'",
    "j_p^*(K) ⊗ with a plain upright typed capital L standing above the ⊗ (no underline), Z/nZ at its lower right",
    "\\otimes^L_{\\Z/n\\Z} (a math-italic L set as a superscript)",
    "font", "medium",
    {"old": "\\otimes^L_{\\Z/n\\Z}", "new": "\\overset{\\mathrm{L}}{\\otimes}_{\\Z/n\\Z}"},
    "The form the fixes of pp. 37, 45 and 46 gave the plain typed L over ⊗. s5.tex writes \\otimes^L 137 times "
    "and \\otimes^{L} 48 times: see the message.")
add(70, "Théorème 7.5, end of the hypotheses",
    "'(Conditions satisfaites si X est excellent ...': capital C",
    "(conditions satisfaites",
    "word", "high",
    {"old": "(conditions satisfaites", "new": "(Conditions satisfaites"},
    "Capital against small letter.")
add(70, "proof label of Théorème 7.5",
    "'Démonstration.': the rule ends under the n; the full stop is not underlined",
    "\\emph{Démonstration.}",
    "underline", "high",
    {"old": "\\emph{Démonstration.}", "new": "\\emph{Démonstration}."},
    "A proof label of another form than 'Preuve :': the print has 'Démonstration.' with a full stop, no colon.")

# ---------------- write and check ----------------
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

bad = 0
for d in F:
    if d["fix"] is None:
        continue
    page_text = (RUN / "b066_070" / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = page_text.count(old)
    if n != 1 or "%%%%%%%%%%" in old:
        bad += 1
        print("BAD", d["page"], repr(old), n)
print("findings:", len(F), "bad olds:", bad)
for p in range(66, 71):
    normal = sum(1 for d in F if d["page"] == p and d["kind"] != "misprint_in_print")
    mis = sum(1 for d in F if d["page"] == p and d["kind"] == "misprint_in_print")
    print(p, f"{normal}/{mis}")
