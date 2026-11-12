# Builds findings_016_020.json (SGA 5, pp. 16-20).
import json
import pathlib

OUT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_016_020.json")
NL = "\n"
HEADLESS = ("hand-drawn tilde over a plain typed bar, no arrowhead")
F = []


def add(page, where, scan, tex, kind, confidence, fix, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


def arrow(page, where, scan_formula, old, new, note="", conf="high"):
    add(page, where, f"{scan_formula}: the isomorphism sign is a {HEADLESS}",
        f"'{old.strip()}'", "symbol", conf, fx(old, new), note)


def uline(page, where, scan_formula, old, new, note=""):
    add(page, where, f"{scan_formula}: the H is not underlined (clean baseline under it)",
        f"'{old}' (\\uH = \\underline{{\\mathrm H}})", "underline", "high", fx(old, new), note)


# ---------------------------------------------------------------- page 16
add(16, "proof of Corollaire 1.15, 'f se factorise en f'i, où i est une immersion ouverte'",
    "f  se factorise en  f'i, où  i  est une: only f'i, no 'f =' before it",
    "$f$ se factorise en $f = f'i$, où", "extra", "high",
    fx("$f = f'i$", "$f'i$"))
add(16, "proof of Corollaire 1.15, 'Comme R^!f ≃ R^!i R^!f''",
    "the middle R (of R^!i) is a plain typewriter R with a single stem; the R of R^!f before it and of R^!f' "
    "after it are double-struck (doubled stem)",
    "\\R^{!}f \\simeq \\R^{!}i \\, \\R^{!}f' (\\R = \\mathbb{R}: three double-struck R)",
    "misprint_in_print", "medium", fx("\\R^{!}i", "\\mathrm{R}^{!}i"),
    "The typist's plain R between two double-struck ones; the TeX silently gives the double-struck R, the fix "
    "restores the printed letter (diplomatic layer only). Reading certain; 'misprint' rather than 'font' as with "
    "the plain Z of pp. 7-8.",
    corrected="\\R^{!}i")
arrow(16, "proof of Corollaire 1.15, 'Mais D_Y f_*(F) ≃ f_*D_X(F) (1.12 a)(i))'", "D_Y f_*(F) ≃ f_*D_X(F)",
      "\\xrightarrow{\\sim} f_{*}\\underline{D}_X(F)", "\\simeq f_{*}\\underline{D}_X(F)",
      "The same sign as in 'R^!f ≃ R^!i R^!f'' three lines above, where the TeX has \\simeq. Every isomorphism "
      "sign in the running text of pp. 16-20 is drawn this way; the 34 that the TeX writes \\xrightarrow{\\sim} "
      "are each listed. The arrows of p. 14 and the two horizontal arrows of the diagram on p. 19 have drawn "
      "heads, so this is not a volume-wide convention.")

# ---------------------------------------------------------------- page 17
add(17, "top of the page: 'alors déterminés à isomorphisme unique près) tels que :'",
    "p. 17 begins with 'alors déterminés à isomorphisme unique près) tels que :'; p. 16 ends with "
    "'... un entier  r  (qui sont'",
    "'alors' is the last word of s5.tex line 602 ('... un entier $r$ (qui sont alors'), the last line of "
    "page_016.tex; the folio-17 marker (line 603) follows it",
    "marker", "high", None,
    "Page 17 really begins with 'alors' at the end of s5.tex line 602. Exact fix: "
    "python -I move_marker.py 5 17 \"alors\" --before (the marker then splits line 602 after 'sont'; simulated "
    "in memory on both layers against the s5.tex of 16:13 today). Text not moved; it agrees with the print.")
arrow(17, "Théorème 2.1, the display 'K' ≃ K ⊗^L L[r] .'", "K' ≃ K ⊗^L L[r]",
      NL + "K' \\xrightarrow{\\sim} K", NL + "K' \\simeq K")
arrow(17, "proof of 2.1, display (*), first sign", "R Hom(F ⊗^L L^∨[-r] , G) ≃ R Hom(F , G ⊗^L L[r])",
      "G) \\xrightarrow{\\sim}", "G) \\simeq")
arrow(17, "proof of 2.1, display (*), second sign", "R Hom(F , G ⊗^L L[r]) ≃ R Hom(F,G) ⊗^L L[r]",
      "L[r]) \\xrightarrow{\\sim}", "L[r]) \\simeq")
arrow(17, "'On en déduit aisément que, si K' ≃ K ⊗^L L[r], K' est dualisant'", "K' ≃ K ⊗^L L[r]",
      "si $K' \\xrightarrow{\\sim}", "si $K' \\simeq")
arrow(17, "'D'F ≃ DF ⊗^L L[r] d'après (*)'", "D'F ≃ DF ⊗^L L[r]",
      "\\underline{D}'F \\xrightarrow{\\sim}", "\\underline{D}'F \\simeq")
arrow(17, "'donc, comme DK ≃ A_X , on a'", "DK ≃ A_X",
      "K \\xrightarrow{\\sim} A_X", "K \\simeq A_X")
arrow(17, "the display 'D'K ≃ L[r] ,'", "D'K ≃ L[r]",
      "K \\xrightarrow{\\sim} L[r],", "K \\simeq L[r],")
arrow(17, "'Nous allons montrer que l'on a', line a)", "a)  K' ≃ K ⊗^L P ,",
      "K' &\\xrightarrow{\\sim}", "K' &\\simeq")
arrow(17, "'Nous allons montrer que l'on a', line b)", "b)  P ≃ L[r] , pour un A_X-Module inversible L",
      "P &\\xrightarrow{\\sim}", "P &\\simeq")
arrow(17, "display (**), 'F ⊗^L P ≃ D'DF .'", "F ⊗^L P ≃ D'DF",
      "P \\xrightarrow{\\sim} \\underline{D}'\\underline{D} F", "P \\simeq \\underline{D}'\\underline{D} F")

# ---------------------------------------------------------------- page 18
arrow(18, "first display, 'K ⊗^L P ≃ D'DK ≃ D'A_X = K'', first sign", "K ⊗^L P ≃ D'DK",
      "P \\xrightarrow{\\sim} \\underline{D}'\\underline{D} K", "P \\simeq \\underline{D}'\\underline{D} K")
arrow(18, "first display, second sign", "D'DK ≃ D'A_X = K'",
      "\\xrightarrow{\\sim} \\underline{D}' A_X", "\\simeq \\underline{D}' A_X")
arrow(18, "second display, 'P' ⊗^L P = D'DDD'A_X ≃ D'D'A_X ≃ A_X .', first sign", "D'DDD'A_X ≃ D'D'A_X",
      "\\xrightarrow{\\sim} \\underline{D}'\\underline{D}'A_X", "\\simeq \\underline{D}'\\underline{D}'A_X")
arrow(18, "second display, second sign", "D'D'A_X ≃ A_X",
      "\\xrightarrow{\\sim} A_X.", "\\simeq A_X.")
arrow(18, "Lemme 2.2, 'tels que P ⊗^L P' ≃ A_X'", "P ⊗^L P' ≃ A_X",
      "P' \\xrightarrow{\\sim} A_X$", "P' \\simeq A_X$")
arrow(18, "Lemme 2.2, display, first sign", "P ≃ L[r]",
      "P \\xrightarrow{\\sim} L[r], \\quad", "P \\simeq L[r], \\quad")
arrow(18, "Lemme 2.2, display, second sign", "P' ≃ L^∨[-r]",
      "P' \\xrightarrow{\\sim} L^{\\vee}[-r]", "P' \\simeq L^{\\vee}[-r]")
add(18, "label of the first step of the proof, '1) Cas particulier : X = Spec(k)'",
    "'1) Cas particulier :' in the ordinary type of the line, not underlined, not bold (run into the text)",
    "\\textbf{1) Cas particulier :} $X = \\Spec(k)$", "font", "medium",
    fx("\\textbf{1) Cas particulier :}", "1) Cas particulier :"),
    "Not an underlined title, so not covered by the accepted \\textbf for underlined titles; drop with the next "
    "finding if the coordinator counts the step labels as headings.")
add(18, "1) Cas particulier, '(EGA 0_I 5.4.3)'",
    "the 0 has a typed double underline under it (=); the I is a subscript. p. 8 prints 'EGA 0_III 12.3.3' "
    "without it",
    "(EGA~$0_{\\mathrm{I}}$~5.4.3)", "underline", "medium",
    fx("$0_{\\mathrm{I}}$", "$\\underline{\\underline{0}}_{\\mathrm{I}}$"),
    "Local to this reference (not the typist's habit for EGA 0: p. 8 has none).")
arrow(18, "1) Cas particulier, 'tels que M ⊗ M' ≃ A'", "M ⊗ M' ≃ A",
      "M' \\xrightarrow{\\sim} A", "M' \\simeq A")
arrow(18, "1) Cas particulier, 'M' ≃ M^∨ ; c'est ici qu'intervient'", "M' ≃ M^∨",
      "M' \\xrightarrow{\\sim} M^{\\vee}", "M' \\simeq M^{\\vee}")
add(18, "label of the second step, '2) Cas général.'",
    "'2) Cas général.' in the ordinary type, not underlined, not bold",
    "\\textbf{2) Cas général.}", "font", "medium",
    fx("\\textbf{2) Cas général.}", "2) Cas général."),
    "As '1) Cas particulier :' above.")
arrow(18, "2) Cas général, 'P_x̄ ≃ A_x̄[r(x)]'", "P_x̄ ≃ A_x̄[r(x)]",
      "\\xrightarrow{\\sim} A_{\\ol{x}}[r(x)]", "\\simeq A_{\\ol{x}}[r(x)]")
arrow(18, "2) Cas général, 'P'_x̄ ≃ A_x̄[-r(x)]'", "P'_x̄ ≃ A_x̄[-r(x)]",
      "\\xrightarrow{\\sim} A_{\\ol{x}}[-r(x)]", "\\simeq A_{\\ol{x}}[-r(x)]")
uline(18, "2) Cas général, 'i.e. H^i(P_x̄) = 0'", "H^i(P_x̄) = 0",
      "\\uH^i(P_{", "\\H^i(P_{",
      "On pp. 18-19 the print never underlines this H; it does in the dévissage of p. 20 (H^0(P), H^{-a}(P)), "
      "where \\uH is right.")
uline(18, "2) Cas général, '(resp. H^i(P'_x̄) = 0)'", "H^i(P'_x̄) = 0",
      "\\uH^i(P'_{", "\\H^i(P'_{")
uline(18, "2) Cas général, 'et H^{-i(x)}(P_x̄) ≃ A_x̄'", "H^{-i(x)}(P_x̄)",
      "\\uH^{-", "\\H^{-")
add(18, "2) Cas général, 'et H^{-i(x)}(P_x̄) ≃ A_x̄'",
    "H^{-i(x)}: the superscript letter is a typed i with its dot, against the r of 'H^{+r(x)}' later in the "
    "line and of 'i ≠ -r(x)' just above",
    "\\uH^{-r(x)}(P_{\\ol{x}})", "misprint_in_print", "high",
    fx("r(x)}(P_{", "i(x)}(P_{"),
    "Wrong index of the print (H^{-r(x)} is meant: P_x̄ ≃ A_x̄[r(x)]). The TeX silently corrects; the fix "
    "restores the printed i. Its old does not overlap the underline fix before it.",
    corrected="\\H^{-r(x)}(P_{\\ol{x}})")
arrow(18, "2) Cas général, 'H^{-i(x)}(P_x̄) ≃ A_x̄'", "H^{-i(x)}(P_x̄) ≃ A_x̄",
      "\\xrightarrow{\\sim} A_{\\ol{x}}$, $", "\\simeq A_{\\ol{x}}$, $")
uline(18, "2) Cas général, 'H^{+r(x)}(P'_x) ≃ A_x̄'", "H^{+r(x)}(P'_x)",
      "\\uH^{+", "\\H^{+")
add(18, "2) Cas général, 'H^{+r(x)}(P'_x) ≃ A_x̄'",
    "(P'_x): no bar over the subscript x (nothing above its top serifs but a 2-pixel speck), while the bars "
    "over the x of P_x̄ and A_x̄ in the same line are full-strength typed strokes",
    "\\uH^{+r(x)}(P'_{\\ol{x}})", "misprint_in_print", "medium",
    fx("}(P'_{\\ol{x}})", "}(P'_{x})"),
    "The typist left out the bar of the geometric point x̄. The TeX silently supplies it; the fix restores the "
    "printed x. Its old does not overlap the underline fix before it or the arrow fix after it.",
    corrected="\\H^{+r(x)}(P'_{\\ol{x}})")
arrow(18, "2) Cas général, end of the same formula", "H^{+r(x)}(P'_x) ≃ A_x̄",
      "\\xrightarrow{\\sim} A_{\\ol{x}}$. Il", "\\simeq A_{\\ol{x}}$. Il")

# ---------------------------------------------------------------- page 19
uline(19, "'On a donc H^i(P) = 0 pour i ≠ -r_0'", "H^i(P) = 0",
      "\\uH^i(P) = 0", "\\H^i(P) = 0")
uline(19, "'H^i(P') = 0 pour i ≠ r_0'", "H^i(P') = 0",
      "\\uH^i(P') = 0", "\\H^i(P') = 0")
uline(19, "'et H^{-r_0}(P) ⊗ H^{r_0}(P') ≃ A', first H", "H^{-r_0}(P) ⊗",
      "et $\\uH^{-r_0}(P)", "et $\\H^{-r_0}(P)")
uline(19, "'et H^{-r_0}(P) ⊗ H^{r_0}(P') ≃ A', second H", "⊗ H^{r_0}(P')",
      "\\otimes \\uH^{r_0}", "\\otimes \\H^{r_0}")
arrow(19, "'H^{-r_0}(P) ⊗ H^{r_0}(P') ≃ A.'", "H^{r_0}(P') ≃ A",
      "(P') \\xrightarrow{\\sim} A", "(P') \\simeq A")
uline(19, "'Posons H^{-r_0}(P) = L'", "H^{-r_0}(P) = L",
      "Posons $\\uH^{-r_0}(P)", "Posons $\\H^{-r_0}(P)")
uline(19, "'H^{r_0}(P') = L''", "H^{r_0}(P') = L'",
      "$\\uH^{r_0}(P') = L'$", "$\\H^{r_0}(P') = L'$")
arrow(19, "'De même L' est inversible, et L' ≃ L^∨'", "L' ≃ L^∨",
      "L' \\xrightarrow{\\sim} L^{\\vee}", "L' \\simeq L^{\\vee}")
arrow(19, "'Donc on a P ≃ L[-r_0]'", "P ≃ L[-r_0]",
      "on a $P \\xrightarrow{\\sim}", "on a $P \\simeq",
      "The old avoids the misprinted '-r_0' (next finding), so it also applies to the corrected edition.")
add(19, "'Donc on a P ≃ L[-r_0] , P' ≃ L^∨[+r_0]', first shift",
    "L[-r_o] (minus sign clearly typed)",
    "L[-r_0] (the printed reading kept)", "misprint_in_print", "high", None,
    "Sign misprint: H^{-r_0}(P) = L is the only cohomology of P, so P ≃ L[r_0] (as in Lemme 2.2: P ≃ L[r]). The "
    "corrected edition (sga5/current) already reads L[r_0]; not yet in MISPRINTS_5.json.",
    corrected="L[r_0]")
arrow(19, "'P' ≃ L^∨[+r_0]'", "P' ≃ L^∨[+r_0]",
      "$P' \\xrightarrow{\\sim}", "$P' \\simeq",
      "The old avoids the misprinted '+r_0' (next finding).")
add(19, "'Donc on a P ≃ L[-r_0] , P' ≃ L^∨[+r_0]', second shift",
    "L^∨[+r_o] (plus sign clearly typed)",
    "L^{\\vee}[+r_0] (the printed reading kept)", "misprint_in_print", "high", None,
    "Sign misprint: H^{r_0}(P') = L' ≃ L^∨ is the only cohomology of P', so P' ≃ L^∨[-r_0] (Lemme 2.2: "
    "P' ≃ L^∨[-r]). The corrected edition already reads L^{\\vee}[-r_0]; not yet in MISPRINTS_5.json.",
    corrected="L^{\\vee}[-r_0]")
uline(19, "'si et seulement si H^m(P')_x̄ ≠ 0'", "H^m(P')_x̄ ≠ 0",
      "\\uH^{m}(P')", "\\H^{m}(P')")

# ---------------------------------------------------------------- page 20
arrow(20, "'Par hypothèse, on a P|U ≃ L[r_0]'", "P|U ≃ L[r_0]",
      "P|U \\xrightarrow{\\sim}", "P|U \\simeq")
arrow(20, "'et l'on a H^0(P) ≃ i_!(L)'", "H^0(P) ≃ i_!(L)",
      "(P) \\xrightarrow{\\sim} i_{!}(L)", "(P) \\simeq i_{!}(L)")
add(20, "'splitte naturellement (grâce à la flèche P → H^0(P)), donc que l'on a'",
    "', donc que l'on a' is printed after the closing parenthesis",
    "the words stand in the TeX, but after the inline comment '% FIX #54 (p20, ...) ... passage.' on the same "
    "line, so they are commented out and do not appear",
    "missing", "high", fx("passage., donc que l'on a", "passage." + NL + ", donc que l'on a"),
    "The fix ends the comment with a line break; the comment's % still swallows the line end, so the output is "
    "'(P)), donc que l'on a' as printed. The comment itself is left as it is.")
arrow(20, "display 'P ≃ i_!(P|U) + j_*j^*P . On en déduit'", "P ≃ i_!(P|U) + j_*j^*P",
      "\\xrightarrow{\\sim} i_{!}(P|U) + j", "\\simeq i_{!}(P|U) + j")
arrow(20, "the aligned display, first line", "P ⊗^L P' ≃ i_!(P|U) ⊗^L P'",
      "&\\xrightarrow{\\sim} i_{!}(P|U) \\mathop", "&\\simeq i_{!}(P|U) \\mathop")
add(20, "the aligned display, first line, second term", "+ j_*j^*(P) ⊗^L P' : the P in parentheses",
    "+ j_{*}j^{*}P \\mathop{\\otimes}\\limits^{\\mathrm{L}} P'", "formula", "high",
    fx("+ j_{*}j^{*}P \\mathop", "+ j_{*}j^{*}(P) \\mathop"))
arrow(20, "the aligned display, second line", "≃ i_!(P|U ⊗^L P'|U) + j_*(j^*P ⊗^L j^*P')",
      "&\\xrightarrow{\\sim} i_{!}(P|U \\mathop", "&\\simeq i_{!}(P|U \\mathop")
arrow(20, "the aligned display, third line", "≃ i_!(A_U) + j_*(A_x) ,",
      "&\\xrightarrow{\\sim} i_{!}(A_U)", "&\\simeq i_{!}(A_U)")
uline(20, "'(déjà les H^0 ne sont pas isomorphes !)'", "déjà les H^0",
      "(déjà les $\\uH^{0}$", "(déjà les $\\H^{0}$",
      "The H^0(P), H^{-a}(P) earlier on the page are underlined in the print and stay \\uH.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + NL, encoding="utf-8", newline="\n")
print(len(F), "findings written")
