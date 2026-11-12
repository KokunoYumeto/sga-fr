"""Build findings_036_040.json and check that every fix's old string occurs exactly once in its page file.
TeX snippets are written as raw strings; the character ⏎ stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
PAGES = RUN / "b036_040"
OUT = RUN / "findings_036_040.json"


def t(s):
    return None if s is None else s.replace("⏎", "\n")


def fx(old, new):
    return {"old": t(old), "new": t(new)}


F = []


def add(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = t(corrected)
    d["note"] = note
    F.append(d)


DL = r"\underline{\underline{L}}"

# ---------------- page 36 ----------------
add(36, "4.2, reference after 'formule d'induction complémentaire'", "(1.12. b) (ii))", "(1.12 b) (ii))",
    "punctuation", "high", fx(r"(1.12 b)", r"(1.12. b)"),
    "The print has a full stop after 1.12.")
add(36, "(4.2.1)", "i^* D_X(F) ≃ D_Y ℝ^!i(F) : tilde over a bar, no arrowhead", r"\xrightarrow{\sim}",
    "symbol", "high", fx(r"i^*\underline{D}_X(F)\xrightarrow{\sim}", r"i^*\underline{D}_X(F)\simeq"),
    "Headless isomorphism sign, as listed on pp. 16-35. The signs with a drawn head (p. 37 (*), p. 40 the last three "
    "of the calculation and (4.5.3)) are right as \\xrightarrow{\\sim}.")
add(36, "(4.2.2), sign", "D_X(F)_x ≃ Hom˙(...) : tilde over a bar, no arrowhead", r"\xrightarrow{\sim}",
    "symbol", "high", fx(r"\underline{D}_X(F)_x\xrightarrow{\sim}", r"\underline{D}_X(F)_x\simeq"),
    "As (4.2.1).")
add(36, "(4.2.2), right-hand side", "Hom˙(ℝ^!i(F),A) with Hom underlined and a raised typed dot",
    r"\Hom^*(\R^{!}i(F),A)", "symbol", "high",
    fx(r"\Hom^*(\R^{!}i(F),A)", r"\underline{\Hom}^{\bullet}(\R^{!}i(F),A)"),
    "Two differences in one edit: the print underlines Hom, and its superscript is the typed raised dot of the Hom "
    "complex, not a star (written \\bullet; the volume's \\bullet / ^\\circ decision for this dot applies).")
add(36, "line after (4.2.2): 'un accouplement parfait dans (D(A) :'", "dans (D(A) :", r"dans $\D(A)$:",
    "misprint_in_print", "high", fx(r"dans $\D(A)$:", r"dans $(\D(A)$:"),
    "The print types an unmatched opening parenthesis before D(A) (a full-height typed parenthesis, like the one of "
    "'(A)'); the TeX silently drops it. The fix restores the printed reading.",
    corrected=r"dans $\D(A)$:")
add(36, "(4.2.2)'''", "Ext underlined (sheaf Ext), as the H of the same display", r"\Ext^{2d-i}",
    "underline", "high", fx(r"\Ext^{2d-i}", r"\underline{\Ext}^{2d-i}"),
    "\\Ext is \\DeclareMathOperator{\\Ext}{Ext}, not underlined.")
add(36, "(4.2.2)'''", "(F,μ_n)^{⊗d}_X)_x : no opening parenthesis before the hand-drawn μ",
    r"(F,(\mu_n)_X^{\otimes d})_x", "misprint_in_print", "medium", fx(r"(F,(\mu_n)", r"(F,\mu_n)"),
    "Two closing parentheses follow one opening one in the print; the TeX silently supplies the missing '('. Nothing "
    "curved is visible after the comma (compare the typed '(' before the μ on the first line of the page), but the "
    "μ's doubled descender stands where a typed '(' would be, so a parenthesis under it cannot be fully excluded.",
    corrected=r"(F,(\mu_n)")
add(36, "first paragraph, 'en vertu du théorème de pureté (SGA XVI 3, ...)'", "SGA XVI 3", r"SGA~XVI~3",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading. The purity theorem is SGA 4 XVI 3; the volume writes SGA 4 as 'SGAA' "
    "(59 times in s5.tex, e.g. pp. 37-40) or 'SGA 4'; 'SGA XVI' occurs only here.",
    corrected=r"SGAA~XVI~3")

# ---------------- page 37 ----------------
add(37, "Exercice 4.2.3, second sentence", "Soit K un complexe dualisant sur X , normalisé en x. Notons",
    "the sentence stands after an inline comment ('% SGA→SGAA restauré ... FIX #57, 2026-07-03)') on the same line, "
    "so LaTeX drops it", "missing", "high",
    fx(r"2026-07-03) Soit $K$", r"2026-07-03)⏎Soit $K$"),
    "A line break after the comment restores the sentence in the output. The same defect stands at s5.tex line 1235 "
    "(p. 44: '...de point fermé $x$.% SGA→SGAA restauré ... FIX #57, 2026-07-03) Soit $Y$ un fermé non vide ...').")
add(37, "first display", "L̿ i_? : D^b(A) ⟶ D^-(X) : typed L with a double underline", r"\mathbf L\, i_?",
    "font", "high", fx(r"\mathbf L\, i_? :", DL + r"\, i_? :"),
    "The print's derived-functor L is a typed L doubly underlined, here and in the four places below; the TeX writes "
    "bold \\mathbf L (270 in s5.tex; this is its first occurrence in the volume). The fix gives the printed form, as the "
    "double-underlined 0 of p. 18; the volume decision on bold L (GLOBAL_ISSUES item 77 (c)) may replace it.")
add(37, "second display, left side", "L̿i_?(M) (double underline)", r"\mathbf L\, i_?(M)", "font", "high",
    fx(r"\mathbf L\, i_?(M)=M", DL + r"\, i_?(M)=M"), "As the first display.")
add(37, "second display, tensor sign", "M ⊗^L_A K : the L above the tensor sign is a plain typed L",
    r"\overset{\mathbf L}{\otimes}", "font", "low",
    fx(r"\overset{\mathbf L}{\otimes}", r"\overset{\mathrm{L}}{\otimes}"),
    "No double underline is visible under this L, but its foot touches the top of the hand-drawn ⊗, so an underline "
    "hidden by the ⊗ cannot be excluded. \\mathrm L as in the preamble's \\lten.")
add(37, "parenthesis after the second display", "(Si K ... L̿ i_? s'étend ...", r"$\mathbf L\, i_?$ s'étend",
    "font", "high", fx(r"$\mathbf L\, i_?$ s'étend", "$" + DL + r"\, i_?$ s'étend"), "As the first display.")
add(37, "end of the same parenthesis", "D^+(A) dans D(X)).", r"dans $\D(X)$.)", "punctuation", "high",
    fx(r"dans $\D(X)$.)", r"dans $\D(X)$)."),
    "The print closes the parenthesis before the full stop.")
add(37, "(*)", "ℝ Hom(L, L̿ i_?(M)) (double underline)", r"(L,\mathbf L\, i_?(M))", "font", "high",
    fx(r"(L,\mathbf L\, i_?(M))", r"(L," + DL + r"\, i_?(M))"), "As the first display.")
add(37, "Hint, label", "Hint : with only 'Hint' underlined", r"\emph{Hint:}", "underline", "medium",
    fx(r"\emph{Hint:}", r"\emph{Hint} :"),
    "The colon is outside the underline, as in 'Preuve :' (the global \\emph{Preuve} : form).")
add(37, "Hint, first sentence", "un morphisme \"trace\" : ℝ^!i L̿i_?(M) ⟶ M", r"``trace'' $\R^{!}i...",
    "punctuation", "high", fx(r"``trace'' $\R", r"``trace'': $\R"),
    "The print has a colon after \"trace\".")
add(37, "Hint, first sentence", "ℝ^!i L̿i_?(M) (double underline)", r"\R^{!}i\,\mathbf L\, i_?(M)", "font", "high",
    fx(r"i\,\mathbf L\, i_?(M)", r"i\," + DL + r"\, i_?(M)"), "As the first display.")
add(37, "Hint, last sentence", "(\"dualité locale\" cf.[H] V 6.2) : with 'dualité locale' underlined",
    r"(``dualité locale'' cf.~[H]~V~6.2)", "underline", "high",
    fx(r"(``dualité locale'' cf.", r"(``\emph{dualité locale}'' cf."),
    "Underlined in the print; this page writes the underline as \\emph.")
add(37, "Hint, last sentence", "... V 6.2) : (colon before the display)", r"V~6.2) (no colon)", "punctuation", "high",
    fx(r"V~6.2)⏎\[", r"V~6.2):⏎\["), "The print ends the sentence with a colon.")

# ---------------- page 38 ----------------
add(38, "proof of Lemme 4.3, label", "Preuve : (Preuve underlined)",
    r"\begin{prooftext}[Preuve] (the environment prints 'Preuve.')", "other", "high",
    fx(r"\begin{prooftext}[Preuve]⏎", r"\emph{Preuve} : "),
    "Apply together with the removal of the first \\end{prooftext} on p. 39 (LaTeX fails otherwise). Same form as the "
    "global '\\emph{Preuve} :' and the \\begin{proof}[Preuve] fixes of pp. 10-15; the global pass did not reach the "
    "44 \\begin{prooftext} of s5.tex.")
add(38, "cartesian square, bottom arrow", "X ←f— X' with f above the arrow (as g above the top arrow)",
    "X' \\arrow[l,\"f\"] (label below a leftward arrow)", "other", "high",
    fx(r'\arrow[l,"f"]', r'\arrow[l,"f"' + "']"),
    "tikz-cd sets an unswapped label below a leftward arrow; the print has f above it.")
add(38, "cartesian square", "full stop to the right of the diagram's bottom row", "no punctuation", "punctuation",
    "high", fx(r"\end{tikzcd}", r"\end{tikzcd}\quad ."), "Form as the p. 31 fix for punctuation after diagrams.")
add(38, "first of the two isomorphisms (SGAA XVIII 3.1.10)", "ℝ Hom(F,G) ⟵~ ℝ i_* i^*G (no punctuation)",
    r"\R i_* i^*G,", "extra", "high", fx(r"\R i_* i^*G,", r"\R i_* i^*G"),
    "The TeX adds a comma; the second line ends with the full stop, as in the TeX.")
add(38, "second of the two isomorphisms", "R i'_* g^*i^*G : plain R (one stem)", r"\R i'_* g^*i^*G",
    "misprint_in_print", "high", fx(r"\R i'_* g^*", r"\mathrm{R} i'_* g^*"),
    "The R's of the line above and of the last display have two stems; this one has one. The TeX silently gives the "
    "double-struck R; treated as the plain R of p. 16.",
    corrected=r"\R i'_* g^*")
add(38, "line before the last display", "(SGAA XVII  (the line ends; no closing parenthesis, no number)",
    r"(SGAA~XVII)", "misprint_in_print", "high", fx(r"(SGAA~XVII)", r"(SGAA~XVII"),
    "The TeX silently closes the parenthesis; the fix restores the printed reading.",
    corrected=r"(SGAA~XVII)")

# ---------------- page 39 ----------------
add(39, "end of the proof of Lemme 4.3", "(no label end; the text runs on to Lemme 4.4)", r"\end{prooftext}", "extra",
    "high", fx(r"5.11).⏎\end{prooftext}⏎", r"5.11).⏎"),
    "Apply together with the p. 38 label fix (\\begin{prooftext}[Preuve] -> \\emph{Preuve} : ).")
add(39, "Lemme 4.4", "f : X̄(x̄) ⟶ X̄,  f^*K : the target X carries a bar", r"\to X$, $f^*K", "misprint_in_print",
    "high", fx(r"\to X$, $f^*K", r"\to \ol{X}$, $f^*K"),
    "The strict localization maps to X; the print's bar over the target is a typing error. The TeX silently drops it; "
    "the fix restores the printed reading.",
    corrected=r"\to X$, $f^*K")
add(39, "proof of Lemme 4.4, label", "Preuve : (Preuve underlined)",
    r"\begin{prooftext}[Preuve] (prints 'Preuve.')", "other", "high",
    fx(r"\begin{prooftext}[Preuve]⏎", r"\emph{Preuve} : "),
    "Apply together with the next finding (its \\end{prooftext}).")
add(39, "end of the proof of Lemme 4.4", "(no label end)", r"\end{prooftext}", "extra", "high",
    fx(r"(4.3).⏎\end{prooftext}⏎", r"(4.3).⏎"), "Apply together with the previous finding.")
add(39, "cartesian square of 4.5, bottom arrow", "x̄ —i'→ X' with i' above the arrow (as i above the top one)",
    "\\arrow[r,\"i'\"'] (label below)", "other", "high",
    fx(r"\arrow[r," + '"' + "i'" + '"' + "']", r"\arrow[r," + '"' + "i'" + '"' + "]"),
    "The swap mark puts the label below; the print has it above.")
add(39, "cartesian square of 4.5", "comma to the right of the diagram's bottom row", "no punctuation", "punctuation",
    "high", fx(r"\end{tikzcd}", r"\end{tikzcd}\quad ,"), "As the full stop after the diagram of p. 38.")

# ---------------- page 40 ----------------
add(40, "(4.5.2)", "ℝΓ_x̄ ≃ ℝ^!i' f^* : tilde over a bar, no arrowhead", r"\xrightarrow{\sim}", "symbol", "high",
    fx(r"\xrightarrow{\sim}\R^{!}i' f^*", r"\simeq\R^{!}i' f^*"), "As (4.2.1) on p. 36.")
add(40, "'Soit K_X ∈ ob D^+(X), et posons K_Y = ...'", "K_Y = ℝ^! j(K_X)", r"K_Y=\R^{!}j(K_X)",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed j. Y is the closed subscheme with i : Y → X; j : U → X is its open complement (first "
    "line of the page), and 4.2 has K_Y = R^!i(K_X).",
    corrected=r"K_Y=\R^{!}i(K_X)")
add(40, "same sentence", "K_x̄ = ℝΓ_x̄(K_X) attention, K_x̄ n'est pas la fibre de K_X en x̄ !).",
    r"$ (attention,", "misprint_in_print", "high", fx(r"$ (attention,", r"$ attention,"),
    "The print has no opening parenthesis before 'attention' (the closing one after '!' stands). The curved stroke "
    "before ℝ in '= ℝΓ' is the second stem of the double-struck R (cap height only, unlike the typed parentheses). "
    "The TeX silently supplies the parenthesis; the fix restores the printed reading.",
    corrected=r"$ (attention,")
add(40, "calculation of (D_XF)_x̄, first line", "(D_XF)_x̄ ≃ g^* i^* D_XF : tilde over a bar, no arrowhead",
    r"&\xrightarrow{\sim}g^*i^*", "symbol", "high", fx(r"&\xrightarrow{\sim}g^*i^*", r"&\simeq g^*i^*"),
    "Only this first sign of the calculation is headless; the next two and (4.5.3) have drawn heads.")
add(40, "last line / marker of folio 41", "p. 40 ends '... un calcul analogue en passant par'; p. 41 begins "
    "'X' au lieu de Y , on aurait alors ...'", r"'$X'$ au' stands above the folio 41 marker", "marker", "high", None,
    "Page 41 really begins at '$X'$ au' (s5.tex line 1135). Exact fix: python -I move_marker.py 5 41 \"\\$X'\\$ au\" "
    "--before (bash quoting; simulated in memory on both layers: the marker then splits line 1135 after 'en passant "
    "par'). No fix of this report touches the anchor.")

# ---------------- checks ----------------
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    page_tex = (PAGES / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    old = d["fix"]["old"]
    n = page_tex.count(old)
    marker_hit = "%%%%%%%%%%" in old
    if n != 1 or marker_hit:
        bad += 1
        print("BAD", d["page"], repr(old), n)
# overlapping olds on the same page
for p in sorted({d["page"] for d in F}):
    page_tex = (PAGES / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            k = page_tex.find(d["fix"]["old"])
            spans.append((k, k + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP", p, a, b)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("written", len(F), "findings; problems:", bad)
print({p: f"{c[0]}/{c[1]}" for p, c in sorted(counts.items())})
