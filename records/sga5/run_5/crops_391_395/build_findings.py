"""Assemble findings_391_395.json and check every fix's old (exactly once in its page file, also after the
marker moves of pp. 392 and 395; no overlapping olds on a page except the declared ordered pair)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = "C:/Users/user/Documents/sga_scan_check_20261105/run_5"
OUT = RUN + "/findings_391_395.json"
NL = "\u23ce"  # placeholder for a line break inside raw strings


def n(s):
    return s.replace(NL, "\n") if s is not None else None


F = []


def add(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": n(old), "new": n(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = n(corrected)
    d["note"] = note
    F.append(d)


R_NOTE = ("On pp. 391-392 the print's R of RΓ is a plain typewriter R 12 times and double-struck twice (tr(cl(ℝΓ...)) "
          "on p. 391, 'pour g = e' on p. 392, where the TeX agrees); \\RG = \\R\\Gamma gives ℝ (\\R = \\mathbb{R} in "
          "Exposé X).")

# ---------------------------------------------------------------- page 391
add(391, "top of the page: 'formule' and display (5.2.1)",
    "p. 391 begins 'où σ'_y est le caractère de Sw'_y ((4.2.7) et (4.2.3)), r_G la représen-'; p. 390 ends with "
    "'for-/mule' and the display (5.2.1) σ_2 = EP(C)r_G - Σ_{y∈Y} σ'_y ,",
    "'formule' and the display (5.2.1) (s5.tex lines 13243-13247 of the 15:52 snapshot) stand under the folio-391 "
    "marker (line 13242), at the top of page_391.tex",
    "marker", "high", None, None,
    "Page 391 really begins at 'où $\\sigma'_y$ est le caractère' (snapshot line 13248). Exact fix: python -I "
    "move_marker.py 5 391 'où $\\sigma' (simulated in memory on both layers). ALREADY DONE in the live s5.tex "
    "(16:17): the folio-391 marker now stands just before 'où $\\sigma'_y$' (diplomatic line 13262, current 13258); "
    "the page files of this batch predate it. Nothing else of pp. 391-395 differs between the snapshot and the live "
    "file. 'formule' and (5.2.1) agree with the print of p. 390 except the double-struck EP (convention, see p. 393).")

add(391, "display after 'On a évidemment', right-hand side",
    "𝓕(G,ℤ_ℓ) = lim←n (G,ℤ/ℓ^nℤ) . : no script F before '(G,'; blank paper between 'lim' and '(' (pixel check: "
    "white from x=790 to 839 in strip 2)",
    "\\varprojlim_n\\mathcal F(G,\\mathbb Z/\\ell^n\\mathbb Z).",
    "misprint_in_print", "high",
    r"\varprojlim_n\mathcal F(G,", r"\varprojlim_n(G,",
    "The space left for the hand-drawn script F was never filled (the three other script F of the two displays are "
    "drawn). The TeX silently supplies \\mathcal F; the fix restores the printed reading (diplomatic layer only).",
    corrected=r"\varprojlim_n\mathcal F(G,")

add(391, "'Il suffit donc de démontrer qu'on a, quel que soit n'",
    "quel que soit n (no comma; the display follows)", "quel que soit $n$,",
    "punctuation", "high", r"quel que soit $n$,", r"quel que soit $n$", "The TeX adds a comma.")

add(391, "'Le premier membre est égal à tr(λ*_n(μ_ν(S_1)) , or'",
    "tr(λ*_n(μ_ν(S_1))  , or : three opening parentheses, two closing",
    "$\\operatorname{tr}(\\lambda_n^*(\\mu_\\nu(S_1)))$, or",
    "misprint_in_print", "high", r"(S_1)))$, or", r"(S_1))$, or",
    "The parenthesis of tr( is not closed in the print; the TeX silently adds it.",
    corrected=r"(S_1)))$, or")

add(391, "display λ*_n(μ_ν(S_1)) = cl_{K•(Λ_ν[G])}(R Γ_{C'}(Λ_{ν,U',C'})) ,",
    "R Γ_{C'}: a plain typewriter R (one stem), set apart from the hand-drawn Γ",
    "\\bigl(\\RG_{C'}(\\Lambda_{n,U',C'})\\bigr)",
    "font", "high", r"\bigl(\RG_{C'}", r"\bigl(\mathrm{R}\Gamma_{C'}",
    R_NOTE + " Independent of the two Λ_ν misprint fixes of this display (olds do not overlap).")

add(391, "same display, index of the class map",
    "cl_{K•(Λ_ν[G])}: Greek ν (the glyph of μ_ν), not n",
    "\\clKstar{\\Lambda_n[G]}",
    "misprint_in_print", "high", r"=" + NL + r"\clKstar{\Lambda_n[G]}", r"=" + NL + r"\clKstar{\Lambda_\nu[G]}",
    "λ*_n(μ_ν(S_1)) lies in K•(Λ_n[G]); the Künneth formula that follows lifts RΓ_{C'}(Λ_{ν,U',C'}) to "
    "RΓ_{C'}(Λ_{n,U',C'}), and the display after it has Λ_n in both places. The TeX silently corrects both ν of this "
    "display: apply this and the next fix together (both or neither).",
    corrected=r"=" + NL + r"\clKstar{\Lambda_n[G]}")

add(391, "same display, argument of RΓ",
    "Λ_{ν,U',C'}: Greek ν, not n",
    "(\\Lambda_{n,U',C'})\\bigr),",
    "misprint_in_print", "high", r"(\Lambda_{n,U',C'})\bigr),", r"(\Lambda_{\nu,U',C'})\bigr),",
    "As the previous finding (apply both or neither).",
    corrected=r"(\Lambda_{n,U',C'})\bigr),")

add(391, "Künneth display, left-hand RΓ",
    "RΓ_{C'}(Λ_{n,U',C'}) ⊗ Λ_ν : plain R (one stem)",
    "\\RG_{C'}(\\Lambda_{n,U',C'})\\otimes",
    "font", "high", r"\RG_{C'}(\Lambda_{n,U',C'})\otimes", r"\mathrm{R}\Gamma_{C'}(\Lambda_{n,U',C'})\otimes",
    R_NOTE + " Does not overlap the L fix of the same display.")

add(391, "Künneth display, the derived tensor",
    "a double-struck L (doubled stem) above ⊗, Λ_n below it",
    "\\otimes_{\\Lambda_n}^{L} (math-italic L)",
    "font", "high", r"_{\Lambda_n}^{L}", r"_{\Lambda_n}^{\mathbb{L}}",
    "Outside Exposé III no global form of the derived tensor applies; the print's L is double-struck.")

add(391, "Künneth display, right-hand RΓ",
    "≃ RΓ_{C'}(Λ_{ν,U',C'}) : plain R (one stem)",
    "\\simeq \\RG_{C'}(\\Lambda_{\\nu,U',C'})",
    "font", "high", r"\simeq \RG", r"\simeq \mathrm{R}\Gamma", R_NOTE)

add(391, "'On est donc ramené à prouver l'égalité :'",
    "an indented new paragraph (the line starts 140 px right of the margin of 'Désignons' below; the display "
    "after it starts at the same place)",
    "runs on after the Künneth display (no blank line after \\])",
    "other", "medium", r"\]" + NL + r"On est donc", r"\]" + NL + NL + r"On est donc", "Paragraph break.")

add(391, "end of 'On est donc ramené à prouver l'égalité'",
    "l'égalité :", "prouver l'égalité, then the display",
    "punctuation", "high", r"prouver l'égalité" + NL, r"prouver l'égalité:" + NL,
    "The TeX drops the colon (the file writes the print's ' :' as ':').")

add(391, "display tr(cl_{K•(Λ_n[G])}(ℝΓ_{C'}(Λ_{n,U',C'}))) = λ_n(σ_2) .",
    "λ_n with the hand-drawn ♮ sign above the n (as in λ♮_n(tr(...)) = λ♮_n(σ_2) above), not the typed asterisk "
    "of λ*_n",
    "\\lambda_n^*(\\sigma_2)",
    "symbol", "high", r"=" + NL + r"\lambda_n^*(\sigma_2)", r"=" + NL + r"\lambda_n^\natural(\sigma_2)",
    "The R of ℝΓ in this display is double-struck, as the TeX's \\RG.")

add(391, "end of 'L'élément g induit évidemment un endomorphisme du triangle distingué'",
    "du triangle distingué :", "triangle distingué, then the display",
    "punctuation", "high", r"triangle distingué" + NL, r"triangle distingué:" + NL,
    "The TeX drops the colon. Last line of the printed p. 391.")

P392 = " (printed at the top of p. 392; in page_391.tex as the files stand)"
add(391, "triangle diagram, top vertex" + P392,
    "R Γ_{Y'}(Λ_{n,Y'}) : plain R (one stem)", "& \\RG_{Y'}(\\Lambda_{n,Y'})",
    "font", "high", r"& \RG_{Y'}", r"& \mathrm{R}\Gamma_{Y'}",
    R_NOTE + " Old stays unique on p. 392 after the folio-392 marker move.")

add(391, "triangle diagram, bottom left vertex" + P392,
    "RΓ_{C'}(Λ_{n,U',C'}) : plain R", "\\RG_{C'}(\\Lambda_{n,U',C'}) \\arrow[rr]",
    "font", "high", r"\RG_{C'}(\Lambda_{n,U',C'}) \arrow", r"\mathrm{R}\Gamma_{C'}(\Lambda_{n,U',C'}) \arrow",
    R_NOTE)

add(391, "triangle diagram, bottom right vertex" + P392,
    "RΓ_{C'}(Λ_{n,C'}) : plain R", "&& \\RG_{C'}(\\Lambda_{n,C'})",
    "font", "high", r"&& \RG_{C'}", r"&& \mathrm{R}\Gamma_{C'}", R_NOTE)

add(391, "end of the triangle diagram" + P392,
    "RΓ_{C'}(Λ_{n,C'})  . : a full stop after the right-hand vertex", "no full stop",
    "punctuation", "high", r"(\Lambda_{n,C'})" + NL + r"\end{tikzcd}", r"(\Lambda_{n,C'})." + NL + r"\end{tikzcd}",
    "The TeX drops the full stop. Adjacent to, not overlapping, the R fix of this vertex.")

add(391, "triangle diagram, right-hand arrow" + P392,
    "the right-hand arrow goes from RΓ_{Y'}(Λ_{n,Y'}) down to RΓ_{C'}(Λ_{n,C'}) (arrowhead at the bottom), like the "
    "left-hand one",
    "\\arrow[dr] from the top vertex (the printed direction)",
    "misprint_in_print", "medium", None, None,
    "In the distinguished triangle RΓ_{C'}(Λ_{n,U',C'}) → RΓ_{C'}(Λ_{n,C'}) → RΓ_{Y'}(Λ_{n,Y'}) → (+1) the right-hand "
    "arrow is the restriction to Y' and points up to the top vertex. The TeX keeps the printed direction; corrected "
    "layer: replace '\\arrow[dr]' (unique) by '\\arrow[dr, leftarrow]'.",
    corrected=r"\arrow[dr, leftarrow]")

add(391, "'On a donc :'" + P392,
    "On a donc :", "On a donc, then the display",
    "punctuation", "high", r"On a donc" + NL, r"On a donc:" + NL, "The TeX drops the colon.")

add(391, "τ(g) display, first member" + P392,
    "τ(g) = Tr* g_{RΓ_{C'}(Λ_{n,U',C'})} : plain R", "\\tau(g)=\\Tr^*g_{\\RG_{C'}(\\Lambda_{n,U',C'})}",
    "font", "high", r"\tau(g)=\Tr^*g_{\RG", r"\tau(g)=\Tr^*g_{\mathrm{R}\Gamma", R_NOTE)

add(391, "τ(g) display, second member" + P392,
    "= Tr* g_{RΓ_{C'}(Λ_{n,C'})} : plain R", "=\\Tr^*g_{\\RG_{C'}(\\Lambda_{n,C'})}",
    "font", "high", r"=\Tr^*g_{\RG_{C'}(\Lambda_{n,C'})}", r"=\Tr^*g_{\mathrm{R}\Gamma_{C'}(\Lambda_{n,C'})}",
    R_NOTE + " Old stays unique on p. 392 after the marker move.")

add(391, "τ(g) display, third member" + P392,
    "- Tr* g_{RΓ_{Y'}(Λ_{n,Y'})} : plain R", "-\\Tr^*g_{\\RG_{Y'}(\\Lambda_{n,Y'})}",
    "font", "high", r"-\Tr^*g_{\RG", r"-\Tr^*g_{\mathrm{R}\Gamma", R_NOTE)

# ---------------------------------------------------------------- page 392
add(392, "top of the page: the triangle diagram, 'On a donc :' and the τ(g) display",
    "p. 392 begins with the triangle RΓ_{Y'}(Λ_{n,Y'}) / RΓ_{C'}(Λ_{n,U',C'}) → RΓ_{C'}(Λ_{n,C'}) . , then "
    "'On a donc :' and τ(g) = ...; p. 391 ends with 'L'élément g induit évidemment un endomorphisme du triangle "
    "distingué :' and blank paper",
    "the diagram display, 'On a donc' and the τ(g) display are the last 12 lines of page_391.tex; the folio-392 "
    "marker follows them",
    "marker", "high", None, None,
    "Page 392 really begins at the display '\\[' followed by '\\begin{tikzcd}' (live s5.tex at 16:17: diplomatic line "
    "13296, current 13292, marker at 13308/13304; snapshot: 13281, marker 13293). Exact fix: python -I "
    "move_marker.py 5 392 \"$(printf '%s\\n%s' '\\[' '\\begin{tikzcd}')\" --before (simulated in memory on both "
    "layers of the live file: the marker lands on its own line just before '\\['; a plain '\\begin{tikzcd}' anchor "
    "would put it inside the display). Text not moved; the differences of that text are filed under p. 391, and their "
    "olds stay unique on p. 392 after the move.")

add(392, "first sentence: '(Pour abréger on a écrit Tr* au lieu de Tr*_{Λ_n}) .'",
    "the sentence is in parentheses; the full stop follows the closing parenthesis",
    "Pour abréger on a écrit $\\Tr^*$ au lieu de $\\Tr^*_{\\Lambda_n}$.",
    "punctuation", "high",
    r"Pour abréger on a écrit $\Tr^*$ au lieu de $\Tr^*_{\Lambda_n}$.",
    r"(Pour abréger on a écrit $\Tr^*$ au lieu de $\Tr^*_{\Lambda_n}$).",
    "The TeX drops both parentheses.")

add(392, "'Or on a, en appliquant'",
    "runs on in the same line after '(Pour abréger ... Tr*_{Λ_n}) .'",
    "a blank line before 'Or on a' (new paragraph)",
    "other", "high", NL + NL + r"Or on a,", r" Or on a,", "The TeX adds a paragraph break.")

add(392, "'une \"formule de Lefschetz\" triviale'",
    "une \"formule de Lefschetz\" triviale (typewriter double quotes)", "une formule de Lefschetz triviale",
    "punctuation", "high", r"une formule de Lefschetz triviale", r"une ``formule de Lefschetz'' triviale",
    "The TeX drops the quotes.")

add(392, "display after 'lequel g opère :', first member",
    "Tr* g_{RΓ_{Y'}(Λ_{n,Y'})} : plain R", "\\Tr^*g_{\\RG_{Y'}(\\Lambda_{n,Y'})}",
    "font", "high", r"\begin{aligned}" + NL + r"\Tr^*g_{\RG_{Y'}", r"\begin{aligned}" + NL + r"\Tr^*g_{\mathrm{R}\Gamma_{Y'}",
    R_NOTE + " The old includes \\begin{aligned} so that it stays unique after the folio-392 marker move.")

add(392, "'nous donne, si g ≠ e :'",
    "si g ≠ e : (colon before the display)", "si $g\\ne e$,",
    "punctuation", "high", r"donne, si $g\ne e$,", r"donne, si $g\ne e$:", "The TeX has a comma for the colon.")

add(392, "Lefschetz display, first member",
    "Tr* g_{RΓ_{C'}(Λ_{n,y'})} : plain R", "\\Tr^*g_{\\RG_{C'}(\\Lambda_{n,C'})} (before '=' and the sum)",
    "font", "high",
    r"\Tr^*g_{\RG_{C'}(\Lambda_{n,C'})}" + NL + r"=", r"\Tr^*g_{\mathrm{R}\Gamma_{C'}(\Lambda_{n,C'})}" + NL + r"=",
    R_NOTE + " Apply before the next (misprint) fix, whose old lies inside this one.")

add(392, "Lefschetz display, first member, coefficient index",
    "Λ_{n,y'}: a small y with a prime (the y descends below the line), not C'",
    "\\Lambda_{n,C'}",
    "misprint_in_print", "high", r"{n,C'})}" + NL + r"=", r"{n,y'})}" + NL + r"=",
    "The coefficients are Λ_{n,C'} (as in the τ(g) display and in the case g = e below); the TeX silently corrects. "
    "Its old lies inside the old of the previous (R) fix and occurs exactly once both before and after that fix: "
    "apply the R fix first.",
    corrected=r"{n,C'})}" + NL + r"=")

add(392, "Lefschetz display, the summand",
    "ν_{y'}(g): Greek ν (round, no serifs; as μ_ν, Λ_ν on p. 391), not the serifed typed v of 'via' below",
    "v_{y'}(g)",
    "symbol", "high", r"Y'} v_{y'}", r"Y'} \nu_{y'}",
    "Convention of the TeX in Exposé X: the print's ν_{y'} is written v_{y'} (also (4.2.2) on p. 384 and (5.2.2) on "
    "p. 393).")

add(392, "Lefschetz display, after ν_{y'}(g)",
    "Σ_{y'∈Y'} ν_{y'}(g) = la somme des multiplicités des points fixes de l'application g_{C'}: C' → C', : an equals "
    "sign before 'la somme' (the words stand in the display); no comma after (g)",
    "\\sum_{y'\\in Y'} v_{y'}(g),\\n\\]\\nla somme des multiplicités ...",
    "missing", "high", r"(g)," + NL + r"\]" + NL + r"la somme", r"(g)" + NL + r"\]" + NL + r"$=$ la somme",
    "The words inside or outside the display are layout; the equals sign is missing and the comma is the TeX's own.")

add(392, "'et on a :'",
    "et on a : (colon before the display)", "et on a, then the display",
    "punctuation", "high", r"et on a" + NL + r"\[", r"et on a:" + NL + r"\[", "The TeX drops the colon.")

# ---------------------------------------------------------------- page 393
add(393, "'Künneth (SGA 4 XVII) .' and 'Il en résulte donc la formule suivante pour τ :'",
    "'Il en résulte' begins a new line at the left margin after the short line 'Künneth (SGA 4 XVII) .' (an "
    "unindented paragraph break)",
    "run on: 'Künneth (SGA 4 XVII). Il en résulte'",
    "other", "low", r"XVII). Il en", r"XVII)." + NL + NL + r"Il en",
    "Paragraph break without indentation (as p. 58); drop it if such breaks are left to a global pass.")

add(393, "(5.2.2), first case, the summand",
    "(ν_{y'}(g)-1): Greek ν", "\\bigl(v_{y'}(g)-1\\bigr)",
    "symbol", "high", r"(v_{y'}", r"(\nu_{y'}", "As p. 392 (convention of the TeX in Exposé X).")

add(393, "(5.2.2), first case, the condition",
    "(ν_{y'}(g)-1)   si g ≠ e  : 'si' before the condition, no comma after either part",
    "\\bigl(v_{y'}(g)-1\\bigr),& g\\ne e,\\\\[0.8em]",
    "missing", "high", r"\bigr),& g\ne e,\\[0.8em]", r"\bigr)& \text{si } g\ne e\\[0.8em]",
    "The TeX drops 'si' and adds two commas (the same in (4.2.2) on p. 384: '1 - ν_{y'}(s)  si s ≠ e').")

add(393, "(5.2.2), second case, the condition",
    "EP(C') - card(Y')   si g = e   .", "& g=e.",
    "missing", "high", r"& g=e.", r"& \text{si } g=e.", "The TeX drops 'si'.")

add(393, "'Comparant avec (6.2.1) on trouve facilement'",
    "Comparant avec (6.2.1) : 6, not 5", "Comparant avec (5.2.1),",
    "misprint_in_print", "high", r"avec (5.2.1", r"avec (6.2.1",
    "Wrong reference: the formula compared is (5.2.1) σ_2 = EP(C) r_G - Σ σ'_y (p. 390); (6.2.1) is defined on "
    "p. 395. The TeX silently corrects. Independent of the comma fix (adjacent olds).",
    corrected=r"avec (5.2.1")

add(393, "same sentence, after (6.2.1)",
    "(6.2.1) on trouve (no comma)", "(5.2.1), on trouve",
    "punctuation", "high", r"), on trouve", r") on trouve", "The TeX adds a comma.")

add(393, "'on trouve facilement τ = λ_n(σ_2) .'",
    "λ_n with the hand-drawn ♮ sign above the n", "$\\tau=\\lambda_n^*(\\sigma_2)$",
    "symbol", "high", r"$\tau=\lambda_n^*(\sigma_2)$", r"$\tau=\lambda_n^\natural(\sigma_2)$",
    "As the right-hand side of the display at the foot of p. 391.")

add(393, "'En effet si g ≠ e l'égalité ...'",
    "'En effet' begins a new line at the left margin after the short line 'Comparant avec (6.2.1) ... τ = λ_n(σ_2) .' "
    "(an unindented paragraph break)",
    "run on: '$. En effet'",
    "other", "low", r". En effet", r"." + NL + NL + r"En effet",
    "Paragraph break without indentation (as p. 58); drop it if such breaks are left to a global pass.")

add(393, "'En effet si g ≠ e l'égalité'",
    "En effet si g ≠ e l'égalité (no commas)", "En effet, si $g\\ne e$, l'égalité",
    "punctuation", "high", r", si $g\ne e$, l'égalité", r" si $g\ne e$ l'égalité", "The TeX adds two commas.")

add(393, "'l'égalité entre τ(g) et λ_n(σ_2) est immédiate'",
    "λ_n with a heavy, ink-filled hand-drawn sign above the n (not the typed six-pointed asterisk of λ*_n on "
    "p. 391); read as the ♮ of the line above",
    "et $\\lambda_n^*(\\sigma_2)$ est",
    "symbol", "medium", r"et $\lambda_n^*(\sigma_2)$ est", r"et $\lambda_n^\natural(\sigma_2)$ est",
    "The sign is blotted, but its outline is the ♮ of the line above, and the claim is the equality τ = λ♮_n(σ_2) "
    "just stated.")

add(393, "'est immédiate (4.5.2) .'",
    "est immédiate (4.5.2) . (no 'par')", "est immédiate par (4.5.2).",
    "extra", "high", r"immédiate par", r"immédiate", "The TeX adds 'par'.")

add(393, "'Si g = e la formule à vérifier s'écrit :'",
    "an indented new paragraph", "run on: '(4.5.2). Si $g=e$'",
    "other", "high", r"(4.5.2). Si", r"(4.5.2)." + NL + NL + r"Si", "Paragraph break.")

add(393, "same sentence, after 'Si g = e'",
    "Si g = e la formule (no comma)", "Si $g=e$, la formule",
    "punctuation", "high", r"$g=e$, la formule", r"$g=e$ la formule", "The TeX adds a comma.")

add(393, "end of 'la formule à vérifier s'écrit'",
    "s'écrit :", "s'écrit, then the display",
    "punctuation", "high", r"s'écrit" + NL, r"s'écrit:" + NL, "The TeX drops the colon.")

add(393, "display 'EP(C') - card(Y') = N EP(C) - Σ σ'_y(ℓ), où N = card(G) ,'",
    "σ'_y(ℓ): a hand-drawn script ℓ, as tall as the parentheses (like the ℓ of 'ℓ distinct' below), not e",
    "\\sigma'_y(e)",
    "misprint_in_print", "high", r"\sigma'_y(e)", r"\sigma'_y(\ell)",
    "The formula is (5.2.1) at g = e, so the characters are evaluated at e; the TeX silently corrects.",
    corrected=r"\sigma'_y(e)")

add(393, "same display, before N = card(G)",
    "σ'_y(ℓ), où N = card(G) ,", "\\sigma'_y(e),\\n\\qquad N=\\operatorname{card}(G),",
    "missing", "high", r"\qquad N=", r"\qquad\text{où } N=", "The TeX drops 'où'.")

add(393, "'c'est-à-dire (4.5.2) :'",
    "c'est-à-dire (4.5.2) : (no comma, no 'par'; a colon before the display)", "c'est-à-dire, par (4.5.2),",
    "extra", "high", r"c'est-à-dire, par (4.5.2),", r"c'est-à-dire (4.5.2):",
    "The TeX adds 'par' and a comma, and has a comma for the print's colon.")

add(393, "number of no. 6.1",
    "'6.1.' with a full stop", "\\subsubsection*{6.1}",
    "punctuation", "high", r"\subsubsection*{6.1}", r"\subsubsection*{6.1.}", "As p. 140 '1.1.'.")

add(393, "6.1 i), 'on a F_x̄ ∈ (Δ) .'",
    "F_x̄ ∈   (Δ) : nothing between ∈ and (Δ) (blank paper about two characters wide: white from x=1198 to 1239 in "
    "strip 4)",
    "F_{\\bar x}\\in\\Ob(\\Delta)",
    "misprint_in_print", "medium", r"\in\Ob(\Delta)", r"\in(\Delta)",
    "The print has no 'Ob'; the TeX silently supplies \\Ob (which prints 'ob' in this file: \\providecommand{\\Ob}"
    "{\\operatorname{ob}} comes first). Diplomatic layer only.",
    corrected=r"\in\Ob(\Delta)")

add(393, "EP on these pages: (5.2.1) (printed on p. 390, in page_391.tex), 'pour g = e' on p. 392, (5.2.2) and "
    "the two displays of the case g = e on p. 393",
    "EP is double-struck every time (both letters with doubled stems): 𝔼ℙ(C)r_G, 𝔼ℙ(C').1_Λ, 𝔼ℙ(C') - card(Y'), "
    "N 𝔼ℙ(C)",
    "\\EP = \\operatorname{EP} (roman): '\\EP(C)r_G', '\\EP(C')\\cdot1_\\Lambda', '\\EP(C')-\\operatorname{card}(Y')', "
    "'N\\EP(C)'",
    "font", "high", None, None,
    "Convention of Exposé X, not itemized: one decision for the exposé (for example \\EP as \\mathbb{E}\\mathbb{P} "
    "inside Exposé X).")

# ---------------------------------------------------------------- page 394
add(394, "condition ii): 'soit \"localement constant\", ou ce qui revient au même'",
    "soit \"localement constant\", ou : typewriter quotes, then a comma", "soit localement constant; ou",
    "punctuation", "high", r"soit localement constant;", r"soit ``localement constant'',",
    "The TeX drops the quotes and has a semicolon for the comma.")

add(394, "condition ii): 'alors F'|U est constant'",
    "F'|U : U without a prime", "$F'|U'$ est constant",
    "misprint_in_print", "high", r"$F'|U'$ est constant", r"$F'|U$ est constant",
    "F' lives on C'; it is restricted to U' = p^{-1}(U), defined in the same line. The TeX silently corrects.",
    corrected=r"$F'|U'$ est constant")

add(394, "'Le faisceau F|U est donc défini par un complexe M'",
    "Le faisceau F|U (no primes), as in 'qui trivalise F|U' below", "Le faisceau $F'|U'$",
    "formula", "high", r"Le faisceau $F'|U'$", r"Le faisceau $F|U$",
    "Not a misprint: the locally constant F|U, trivialised by the Galois covering, is the G-module M. The TeX "
    "changes the printed reading.")

add(394, "'le point générique de C(resp. C') et par'",
    "(resp. C') et par (no comma)", "(resp. $C'$), et par",
    "punctuation", "high", r"(resp. $C'$), et par", r"(resp. $C'$) et par", "The TeX adds a comma.")

add(394, "'un point géométrique sur η(resp.η') on a :'",
    "(resp.η') on a : (no comma)", "(resp. $\\eta'$), on a:",
    "punctuation", "high", r"(resp. $\eta'$), on a:", r"(resp. $\eta'$) on a:", "The TeX adds a comma.")

add(394, "(6.1.1), first line",
    "p(η') = η (no comma)", "p(\\eta')=\\eta,\\qquad",
    "punctuation", "high", r"=\eta,\qquad", r"=\eta\qquad", "The TeX adds a comma inside the display.")

add(394, "(6.1.1), second line, the middle term",
    "F!_{η̄'}: after the F a tall stroke over a dot (an exclamation mark), not the short wedge prime of F'|U or of η̄'",
    "F'_{\\bar\\eta'}",
    "misprint_in_print", "medium", r"F'_{\bar\eta'}", r"F^{!}_{\bar\eta'}",
    "A typed '!' for the prime of F' (the stalk of F' = p*F at η̄'); the TeX silently gives the prime. Diplomatic "
    "layer only; adjacent to, not overlapping, the next fix.",
    corrected=r"F'_{\bar\eta'}")

add(394, "(6.1.1), end",
    "= M (no full stop)", "=M.",
    "punctuation", "high", r"=M." + NL, r"=M" + NL, "The TeX adds a full stop at the end of the display.")

add(394, "'Comme complexe de A-modules M est isomorphe'",
    "A-modules  M (no comma)", "$A$-modules, $M$ est isomorphe",
    "punctuation", "high", r"modules, $M$ est isomorphe", r"modules $M$ est isomorphe", "The TeX adds a comma.")

add(394, "'à F_η̄ , et grâce à la condition i) c'est un objet de Δ'",
    "F_η̄ , et grâce à la condition i) c'est : comma before 'et', none after 'et' or 'i)'",
    "$F_{\\bar\\eta}$ et, grâce à la condition i), c'est",
    "punctuation", "high", r"$F_{\bar\eta}$ et, grâce à la condition i), c'est",
    r"$F_{\bar\eta}$, et grâce à la condition i) c'est",
    "The TeX moves the comma after 'et' and adds one after 'i)'.")

add(394, "'du revêtement galoisien C' --p--> C qui trivalise F|U'",
    "C' --p--> C : the arrow carries p", "$C'\\to C$ qui",
    "missing", "high", r"$C'\to C$ qui", r"$C'\xrightarrow{p}C$ qui", "The TeX drops the arrow's label p.")

add(394, "same sentence, the verb",
    "qui trivalise F|U", "qui trivialise",
    "misprint_in_print", "high", r"trivialise", r"trivalise",
    "Typing error (one i missing); the TeX silently corrects.", corrected=r"trivialise")

add(394, "display φ : Z_ℓ[G'] → Z_ℓ[G]",
    "both Z are plain typewriter Z (one clean diagonal), unlike the double-struck Z of Z_ℓ on p. 390 and of "
    "Λ = Z/ℓ^νZ on p. 393",
    "\\varphi:\\mathbb Z_\\ell[G']\\longrightarrow \\mathbb Z_\\ell[G]",
    "misprint_in_print", "medium",
    r"\varphi:\mathbb Z_\ell[G']\longrightarrow \mathbb Z_\ell[G]", r"\varphi:Z_\ell[G']\longrightarrow Z_\ell[G]",
    "Treated as the plain Z of pp. 7-8: the TeX silently gives the double-struck Z (diplomatic layer only). Apply "
    "with the plain Z's of the Swan relation (p. 395, filed below): both or neither.",
    corrected=r"\varphi:\mathbb Z_\ell[G']\longrightarrow \mathbb Z_\ell[G]")

P395 = " (printed at the top of p. 395; in page_394.tex as the files stand)"
add(394, "Swan relation, first member" + P395,
    "Sw_{G,n} ≃ Sw_{G',x} ⊗ ... : the first index is G,n (typed n)", "Sw_{G,x}\\simeq",
    "misprint_in_print", "high", r"Sw_{G,x}\simeq", r"Sw_{G,n}\simeq",
    "Both Swan modules are at the point x; the TeX silently corrects. Old stays unique on p. 395 after the folio-395 "
    "marker move.",
    corrected=r"Sw_{G,x}\simeq")

add(394, "Swan relation, the two Z" + P395,
    "⊗_{Z_ℓ[G']} Z_ℓ[G] : both Z plain typewriter Z (one clean diagonal)",
    "\\otimes_{\\mathbb Z_\\ell[G']}\\mathbb Z_\\ell[G],",
    "misprint_in_print", "medium",
    r"\otimes_{\mathbb Z_\ell[G']}\mathbb Z_\ell[G],", r"\otimes_{Z_\ell[G']}Z_\ell[G],",
    "As the display φ above (both or neither).",
    corrected=r"\otimes_{\mathbb Z_\ell[G']}\mathbb Z_\ell[G],")

# ---------------------------------------------------------------- page 395
add(395, "top of the page: the Swan relation Sw_{G,n} ≃ Sw_{G',x} ⊗_{Z_ℓ[G']} Z_ℓ[G] ,",
    "p. 395 begins with this display; p. 394 ends 'Les modules de Swan sont alors liés / par la relation' and blank "
    "paper",
    "the display is the last three lines of page_394.tex; the folio-395 marker follows it",
    "marker", "high", None, None,
    "Page 395 really begins at the display '\\[' followed by 'Sw_{G,x}\\simeq' (live s5.tex at 16:17: diplomatic line "
    "13387, current 13383, marker at 13390/13386; snapshot: 13372, marker 13375). Exact fix: python -I move_marker.py "
    "5 395 \"$(printf '%s\\n%s' '\\[' 'Sw_{G,x}')\" --before (simulated in memory on both layers of the live file). "
    "Text not moved; the two differences of the display are filed under p. 394.")

add(395, "'D'autre part on a un isomorphisme de complexes de A[G']-modules :'",
    "A[G']-modules : (colon before the display)", "$A[G']$-modules, then the display",
    "punctuation", "high", r"-modules" + NL + r"\[", r"-modules:" + NL + r"\[", "The TeX drops the colon.")

add(395, "display after 'de complexes de A-modules entre', first Hom",
    "Hom•_{Λ[G]}(Sw^Λ_{G,x}, F_{η̄'}): one prime after η̄ (two in the F_{η̄''} of the second Hom)",
    "(Sw_{G,x}^\\Lambda,F_{\\bar\\eta})",
    "formula", "medium", r"(Sw_{G,x}^\Lambda,F_{\bar\eta})", r"(Sw_{G,x}^\Lambda,F_{\bar\eta'})",
    "The raised mark after x in both Hom's (the shape of a prime) is read as the argument comma, as the TeX has it; "
    "not reported.")

add(395, "number of no. 6.2",
    "'6.2.' with a full stop", "\\subsubsection*{6.2}",
    "punctuation", "high", r"\subsubsection*{6.2}", r"\subsubsection*{6.2.}", "As p. 140 '1.1.'.")

add(395, "(6.2.1), end of the display",
    "... (Sw^Λ_x , F_η̄)) (no comma)", "F_{\\bar\\eta})\\bigr),",
    "punctuation", "high", r"F_{\bar\eta})\bigr),", r"F_{\bar\eta})\bigr)",
    "The TeX adds a comma at the end of the display.")

add(395, "'Bien entendu dans la formule (6.2.1) F_η̄ est muni'",
    "(6.2.1)  F_η̄ (no comma)", "(6.2.1), $F_{\\bar\\eta}$",
    "punctuation", "high", r"(6.2.1), $F", r"(6.2.1) $F", "The TeX adds a comma.")

add(395, "'on aura (4.6) Sw_x = 0 donc'",
    "Sw_x = 0 / donc (no comma)", "$Sw_x=0$, donc",
    "punctuation", "high", r"$Sw_x=0$, donc", r"$Sw_x=0$ donc", "The TeX adds a comma.")

add(395, "'donc α_x(Δ) = 0 , donc dans ce cas'",
    "α_x(Δ) = 0 : α with the index x only and the argument Δ", "\\alpha_x^\\Delta(F)=0",
    "misprint_in_print", "high", r"\alpha_x^\Delta(F)=0", r"\alpha_x(\Delta)=0",
    "The term of (6.2.1) is α^Δ_x(F); the TeX silently corrects.", corrected=r"\alpha_x^\Delta(F)=0")

add(395, "'(en conformité avec Ogg-Chafarévitch) :'",
    "Chafarévitch with é", "Ogg-Chafarevitch",
    "accent", "high", r"Ogg-Chafarevitch", r"Ogg-Chafarévitch", "The TeX drops the accent.")

# ---------------------------------------------------------------- checks
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
pages = {p: open(f"{RUN}/b391_395/page_{p}.tex", encoding="utf-8", newline="").read() for p in range(391, 396)}
ok = True
ORDERED = {(392, "{n,C'})}\n=")}  # misprint old inside the preceding R fix's old (apply the R fix first)
for d in F:
    if d["fix"] is None:
        continue
    t = pages[d["page"]]
    c = t.count(d["fix"]["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", d["page"], c, repr(d["fix"]["old"]))
    if d["fix"]["old"] == d["fix"]["new"]:
        ok = False
        print("NO CHANGE", d["page"], repr(d["fix"]["old"]))
    if MARK.search(d["fix"]["old"]) or MARK.search(d["fix"]["new"]):
        ok = False
        print("MARKER IN FIX", d["page"])
# overlaps between olds on the same page
for p in range(391, 396):
    spans = []
    for d in F:
        if d["fix"] and d["page"] == p:
            k = pages[p].find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1] and (p, b[2]) not in ORDERED and (p, a[2]) not in ORDERED:
            ok = False
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
# the ordered pair: misprint old exactly once after the R fix
t = pages[392]
rfix = next(d["fix"] for d in F if d["page"] == 392 and d["fix"] and d["fix"]["old"].startswith("\\Tr^*g_{\\RG_{C'}"))
t2 = t.replace(rfix["old"], rfix["new"], 1)
print("ordered pair after R fix:", t2.count("{n,C'})}\n="))
# all fixes applied in list order on each page (diplomatic layer)
for p in range(391, 396):
    t = pages[p]
    for d in F:
        if d["fix"] and d["page"] == p:
            if t.count(d["fix"]["old"]) != 1:
                ok = False
                print("SEQUENTIAL FAIL", p, repr(d["fix"]["old"]))
            t = t.replace(d["fix"]["old"], d["fix"]["new"], 1)
# uniqueness after the marker moves (391 done live; 392 and 395 pending)
whole = "".join(pages[p].split("\n", 1)[1] for p in range(391, 396))
whole = whole.replace("formule\n\\[\n\\sigma_2=\\EP(C)r_G-\\sum_{y\\in Y}\\sigma'_y,\n\\tag{5.2.1}\n\\]\n", "", 1)
m392 = next(m for m in MARK.finditer(whole) if m.group(2) == "392")
line392 = m392.group(0)
whole = whole[:m392.start()] + whole[m392.end() + 1:]
k = whole.rfind("\\[\n\\begin{tikzcd}")
whole = whole[:k] + line392 + "\n" + whole[k:]
m395 = next(m for m in MARK.finditer(whole) if m.group(2) == "395")
line395 = m395.group(0)
whole = whole[:m395.start()] + whole[m395.end() + 1:]
k = whole.rfind("\\[\nSw_{G,x}")
whole = whole[:k] + line395 + "\n" + whole[k:]
ms = list(MARK.finditer(whole))
newpages = {}
for i, m in enumerate(ms):
    newpages[int(m.group(2))] = whole[m.start():ms[i + 1].start() if i + 1 < len(ms) else len(whole)]
for d in F:
    if not d["fix"]:
        continue
    hits = [p for p, s in newpages.items() if d["fix"]["old"] in s]
    cnt = sum(s.count(d["fix"]["old"]) for s in newpages.values())
    if cnt != 1:
        ok = False
        print("AFTER MOVES", d["page"], cnt, repr(d["fix"]["old"]))
print("checks ok" if ok else "CHECKS FAILED")
cnt = {}
for d in F:
    c = cnt.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", cnt, "total", len(F))
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(F, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("written", OUT)
