import json, os, sys

FOLDER = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b126_130'
OUT = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_126_130.json'

F = []

def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 126 ----------------
add(126,
    "proof of 6.2, 'It follows that ... -> A/I_A(A|R) is an isomorphism'",
    "Â → A/I_A(A|R) (caret over the first A, checked in a crop)",
    r"$\hat{A} \rightarrow A/I_A(A|R)$",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed reading. The argument runs Λ → Â/I_Â(Â|R) iso (previous line), hence Λ → A/I_A(A|R) iso, hence Λ → R/I_R(A|R) iso, which is 6.2(1) (J_X(X|R) → J_R(X|R) → Spec(Λ) isomorphisms); Â does not map to A/I_A(A|R).",
    corrected=r"$\Lambda \rightarrow A/I_A(A|R)$")

add(126,
    "Corollary 6.3 (1), 'as R-adic formal schemes if and only if'",
    "'as' underlined, then ' R-' not underlined, then 'adic formal schemes if / and only if' underlined",
    r"\underline{as R-adic formal schemes if and only if}",
    "underline", "high",
    {"old": r"\underline{as R-adic formal schemes if and only if}",
     "new": r"\underline{as} $R$-\underline{adic formal schemes if and only if}"},
    "The TeX underlines the R and the hyphen with the words; the print breaks the underline there (the file writes $R$-adic in the proof below).")

add(126,
    "proof of 6.3 (1), first display 'X_(x^) ≃ Spf(R[[X_1,...,X_n]]/(R - a))'",
    "(R - a)",
    r"/(R - a))",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed R. The second display has (F - b), and p. 127 uses R[[X_1,...,X_n]]/(F - a).",
    corrected=r"/(F - a))")

# ---------------- page 127 ----------------
add(127,
    "first line, 'Then a = ab for some unit u in R'",
    "a = ab",
    r"$a = ab$",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed b. u is the unit being introduced; the next line writes u = v^2 and a = v^2 b.",
    corrected=r"$a = ub$")

add(127,
    "proof of 6.3 (1), 'R[[X_1,...,X_n]]/(F - a) --~-- R[[X_1,...,X_n]]/(F - b)'",
    "a plain rule with ~ above it and no arrowhead; the rule ends cleanly (checked in a crop)",
    r"(F - a) \;\overset{\sim}{\relbar\relbar\relbar}\; R[[",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed headless rule (handled as on p. 41). 'corrected' replaces the 'tex' substring.",
    corrected=r"(F - a) \;\xrightarrow{\ \sim\ }\; R[[")

add(127,
    "Theorem 6.4, first line, 'be a k-scheme of finite type with isolated non-smooth'",
    "'be a' underlined, then ' k-' not underlined, then 'scheme of finite type with isolated non-smooth / points only, and let' underlined",
    r"\underline{be a k-scheme of finite type with isolated non-smooth points only, and let}",
    "underline", "high",
    {"old": r"\underline{be a k-scheme of finite type with isolated non-smooth points only, and let}",
     "new": r"\underline{be a} $k$-\underline{scheme of finite type with isolated non-smooth points only, and let}"},
    "The print breaks the underline at 'k-' (form as in Theorem 4.11, p. 107: \\underline{be a} ... $k$-\\underline{scheme ...}). In Corollary 6.3 (p. 126) the underline runs through 'k-scheme' and the TeX is right there.")

add(127,
    "Theorem 6.4 (2), 'J_X(z_i)(X(z_i)|R) --~-- J_R(X(z_i)|R) is an isomorphism'",
    "a plain rule with ~ above it and no arrowhead; the rule ends cleanly (checked in a crop)",
    r"|R) \;\overset{\sim}{\relbar\relbar\relbar}\; J_R(",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed headless rule (handled as on p. 41). 'corrected' replaces the 'tex' substring.",
    corrected=r"|R) \;\xrightarrow{\ \sim\ }\; J_R(")

add(127,
    "Theorem 6.4 (3), '(as formal power-series ring over Λ ).'",
    "the underline starts under 'as'; the opening parenthesis is not underlined",
    r"\underline{(as formal power-series ring over}",
    "underline", "low",
    {"old": r"\underline{(as formal power-series ring over}",
     "new": r"(\underline{as formal power-series ring over}"},
    "Typographic only (one character). In '(disjoint union), and' of (2) the underline does start under the parenthesis, so that one is right.")

add(127,
    "Theorem 6.4 (4), 'is smooth, i.e. J_X(X|Λ) = φ .'",
    "= φ (the Greek phi of φ(t), not the slashed-zero empty set)",
    r"J_{\mathfrak{X}}(\mathfrak{X}|\Lambda) = \varphi",
    "misprint_in_print", "medium", None,
    "The TeX keeps the printed φ. J_X(X|Λ) is the non-smooth locus, so the empty set is meant; the typewriter has a slashed-zero empty set, used on p. 107 (U_0^j ∩ X_0^Sing = ∅, TeX \\emptyset).",
    corrected=r"J_{\mathfrak{X}}(\mathfrak{X}|\Lambda) = \emptyset")

# ---------------- page 128 ----------------
ZNOTE = ("The subscript is a typed z with a caret struck over it, built like the x^ of 6.3 on pp. 126-127 "
         "(TeX \\widehat{x} there), not a Fraktur z: X_(z^_i) is the completion at z_i, compared with the "
         "localisation X_(z_i) in the displays. Same in all six places on this page and in two on p. 129 "
         "(TeX \\mathcal{Z}_i there).")

add(128,
    "proof of 6.4 (1)-(3), 'Since (R, X_(z^_i)) is a deformation of Spec(Ô_{X_0,z_i})'",
    "X_(ẑ_i): typed z with an overstruck caret",
    r"(R, \mathfrak{X}_{(\mathfrak{z}_i)})",
    "accent", "high",
    {"old": r"(R, \mathfrak{X}_{(\mathfrak{z}_i)})",
     "new": r"(R, \mathfrak{X}_{(\widehat{z}_i)})"},
    ZNOTE)

add(128,
    "cartesian diagram, top-left node",
    "X_(ẑ_i): typed z with an overstruck caret",
    r"\mathfrak{X}_{(\mathfrak{z}_i)} \arrow[r] \arrow[d]",
    "accent", "high",
    {"old": r"\mathfrak{X}_{(\mathfrak{z}_i)} \arrow[r]",
     "new": r"\mathfrak{X}_{(\widehat{z}_i)} \arrow[r]"},
    ZNOTE + " The STRUCTURE comment under the diagram (three lines) still calls it a 'hand-drawn script z' ($\\mathfrak{X}_{(\\mathfrak{z}_i)}$); update it with the node if wanted.")

add(128,
    "first display after the diagram, 'J_X(z_i)(X(z_i)|R) = J_X(z^_i)(X(z^_i)|R) ≃ ...'",
    "J_{X_(ẑ_i)}(X_(ẑ_i)|R): typed z with an overstruck caret, twice",
    r"J_{\mathfrak{X}_{(\mathfrak{z}_i)}}(\mathfrak{X}_{(\mathfrak{z}_i)}|R)",
    "accent", "high",
    {"old": r"J_{\mathfrak{X}_{(\mathfrak{z}_i)}}(\mathfrak{X}_{(\mathfrak{z}_i)}|R)",
     "new": r"J_{\mathfrak{X}_{(\widehat{z}_i)}}(\mathfrak{X}_{(\widehat{z}_i)}|R)"},
    ZNOTE)

add(128,
    "second display, 'J_R(X(z_i)|R) = J_R(X(z^_i)|R) ≃ ...'",
    "J_R(X_(ẑ_i)|R): typed z with an overstruck caret",
    r"J_R(\mathfrak{X}_{(\mathfrak{z}_i)}|R)",
    "accent", "high",
    {"old": r"J_R(\mathfrak{X}_{(\mathfrak{z}_i)}|R)",
     "new": r"J_R(\mathfrak{X}_{(\widehat{z}_i)}|R)"},
    ZNOTE)

add(128,
    "second display, lower subscript of the fibre product",
    "Spf(R_i) under the ×: the letter is an f whose hook did not print: its stem rises above the cross-bar and the ball terminal stands detached at the upper right (contrast-enhanced crop); a typed r has neither",
    r"\underset{\mathrm{Spr}(R_i)}{\times}",
    "formula", "medium",
    {"old": r"\underset{\mathrm{Spr}(R_i)}{\times}",
     "new": r"\underset{\mathrm{Spf}(R_i)}{\times}"},
    "Broken type, not a typed r. If the coordinator reads a typed r instead, this becomes a misprint the TeX keeps (fix null, corrected \\mathrm{Spf}(R_i)).")

add(128,
    "proof of 6.4, 'local Λ-algebra maps φ_i = R_i → R with a cartesian diagram'",
    "φ_i = R_i → R (an equals sign, checked in a crop)",
    r"$\varphi_i = R_i \to R$",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed '='; a map φ_i : R_i → R is meant (cf. φ : R_0 = Λ[[t]] → R on p. 127).",
    corrected=r"$\varphi_i : R_i \to R$")

add(128,
    "third display, 'I_R(X(z_i)|R) = I_R(X(z^_i)|R) = (t_i)'",
    "I_R(X_(ẑ_i)|R): typed z with an overstruck caret",
    r"I_R(\mathfrak{X}_{(\mathfrak{z}_i)}|R)",
    "accent", "high",
    {"old": r"I_R(\mathfrak{X}_{(\mathfrak{z}_i)}|R)",
     "new": r"I_R(\mathfrak{X}_{(\widehat{z}_i)}|R)"},
    ZNOTE)

add(128,
    "'and therefore I_R(X|R) = ∏_{1≤i≤m} I_R(X(z_i)|R) = (∏_{i=1}^n t_i)'",
    "upper limit n on the second product",
    r"\prod_{i=1}^{n} t_i",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed n; i runs over the m non-smooth points (the first product has 1 ≤ i ≤ m).",
    corrected=r"\prod_{i=1}^{m} t_i")

add(128,
    "last paragraph, 'M_X0 → M_X0,(z^_1) × ... × M_X0,(z^_m)'",
    "(ẑ_1), (ẑ_m): typed z with an overstruck caret",
    r"\underline{M}_{X_0,(\mathfrak{z}_1)} \times \ldots \times \underline{M}_{X_0,(\mathfrak{z}_m)}",
    "accent", "high",
    {"old": r"\underline{M}_{X_0,(\mathfrak{z}_1)} \times \ldots \times \underline{M}_{X_0,(\mathfrak{z}_m)}",
     "new": r"\underline{M}_{X_0,(\widehat{z}_1)} \times \ldots \times \underline{M}_{X_0,(\widehat{z}_m)}"},
    ZNOTE)

add(128,
    "last paragraph, '... is smooth by and therefore R_1 ⊗^ ... → R is formally smooth by 4.13'",
    "'is smooth by  and therefore': no reference after 'by' (ordinary word space, no gap for a number)",
    r"is smooth by and therefore",
    "misprint_in_print", "low", None,
    "The TeX keeps the printed gap. The smoothness of M_X0 → Π M_Spec(Ô_X0,z_i) under H^2(X_0, D^0) = 0 is Corollary 4.13(a) (p. 108); the reference is a suggestion only, review before using it in the corrected edition.",
    corrected=r"is smooth by 4.13(a) and therefore")

# ---------------- page 129 ----------------
add(129,
    "proof of 6.4 (4), 'The projection morphism X_(z^_i) ≃> Y_i ×_Spf(R_i) Spf(R) → Y_i'",
    "Fraktur X (as on pp. 126-128) with subscript (ẑ_i): typed z with an overstruck caret",
    r"\mathcal{X}_{(\mathcal{Z}_i)} \overset{\sim}{\rightarrow}",
    "font", "high",
    {"old": r"\mathcal{X}_{(\mathcal{Z}_i)} \overset{\sim}{\rightarrow}",
     "new": r"\mathfrak{X}_{(\widehat{z}_i)} \overset{\sim}{\rightarrow}"},
    "Fraktur X typed as \\mathcal; the subscript is the ẑ_i of p. 128 (small z with caret), not a script capital Z.")

add(129,
    "proof of 6.4 (4), same formula, 'Y_i ×_Spf(R_i)'",
    "Fraktur Y with subscript i, and Spf(R_i) with subscript i: both subscripts have the dot fused to the stem and the left serif below the top (the i of Spf(R_i) and Spf(φ_i) on the next line); the digit 1 (z_1 three lines below) has its flag at the very top",
    r"\mathcal{Y}_1 \times_{\mathrm{Spf}(R_1)}",
    "number", "medium",
    {"old": r"\mathcal{Y}_1 \times_{\mathrm{Spf}(R_1)}",
     "new": r"\mathfrak{Y}_i \times_{\mathrm{Spf}(R_i)}"},
    "Two changes in one edit: 1 -> i (twice) and the Fraktur Y typed as \\mathcal. Mathematically i is meant (fibre product with Y_i over Spf(R_i) via Spf(φ_i)); if the coordinator reads the digit 1, the 1 -> i part becomes a misprint the TeX keeps.")

add(129,
    "proof of 6.4 (4), same formula, '... Spf(R) → Y_i'",
    "Fraktur Y",
    r"\mathrm{Spf}(R) \rightarrow \mathcal{Y}_i",
    "font", "high",
    {"old": r"\mathrm{Spf}(R) \rightarrow \mathcal{Y}_i",
     "new": r"\mathrm{Spf}(R) \rightarrow \mathfrak{Y}_i"},
    "Fraktur Y typed as \\mathcal (\\mathfrak{Y}_i on p. 128).")

add(129,
    "proof of 6.4 (4), 'since Spf(R) --Spf(φ_i)-- Spf(R_i) is formally smooth'",
    "a plain rule with Spf(φ_i) above it and no arrowhead; the rule ends cleanly before Spf(R_i) (checked in a crop)",
    r"\xrightarrow{\ \mathrm{Spf}(\varphi_i)\ }",
    "misprint_in_print", "medium",
    {"old": r"\xrightarrow{\ \mathrm{Spf}(\varphi_i)\ }",
     "new": r"\overset{\ \mathrm{Spf}(\varphi_i)\ }{\relbar\joinrel\relbar\joinrel\relbar\joinrel\relbar}"},
    "The head was never typed (the other arrows of the paragraph have theirs). The TeX silently supplies it; the fix restores the printed headless rule in the form of the earlier headless rules of this exposé (pp. 38, 85, 99). 'corrected' is the current TeX.",
    corrected=r"\xrightarrow{\ \mathrm{Spf}(\varphi_i)\ }")

add(129,
    "proof of 6.4 (4), 'On the other hand, Y_i → Spec(Λ) is formally smooth by 6.2(3)'",
    "Fraktur Y",
    r"$\mathcal{Y}_i \rightarrow \mathrm{Spec}(\Lambda)$",
    "font", "high",
    {"old": r"$\mathcal{Y}_i \rightarrow \mathrm{Spec}(\Lambda)$",
     "new": r"$\mathfrak{Y}_i \rightarrow \mathrm{Spec}(\Lambda)$"},
    "Fraktur Y typed as \\mathcal.")

add(129,
    "proof of 6.4 (4), 'and therefore X_(z^_i) → Spec(Λ) is formally smooth'",
    "Fraktur X with subscript (ẑ_i): typed z with an overstruck caret",
    r"\mathcal{X}_{(\mathcal{Z}_i)} \rightarrow \mathrm{Spec}(\Lambda)",
    "font", "high",
    {"old": r"\mathcal{X}_{(\mathcal{Z}_i)} \rightarrow \mathrm{Spec}(\Lambda)",
     "new": r"\mathfrak{X}_{(\widehat{z}_i)} \rightarrow \mathrm{Spec}(\Lambda)"},
    "Fraktur X typed as \\mathcal; ẑ_i as on p. 128, not a script capital Z.")

add(129,
    "proof of 6.4 (4), 'Consequently X → Spec(Λ) is formally smooth'",
    "Fraktur X",
    r"$\mathcal{X} \rightarrow \mathrm{Spec}(\Lambda)$",
    "font", "high",
    {"old": r"$\mathcal{X} \rightarrow \mathrm{Spec}(\Lambda)$",
     "new": r"$\mathfrak{X} \rightarrow \mathrm{Spec}(\Lambda)$"},
    "Fraktur X typed as \\mathcal.")

add(129,
    "proof of 6.4 (5), first line, 'Since R is formally smooth over Λ'",
    "a plain R, overtyped (heavy) with a small stray spike at its upper right; no bar over it (contrast-enhanced crop)",
    r"$\overline{R}$",
    "symbol", "high",
    {"old": r"$\overline{R}$",
     "new": r"$R$"},
    "The R of 6.4(1) (formally smooth over Λ) is meant; the spike is a typing trace, not an overline.")

add(129,
    "proof of 6.4 (5), 'Since λ(D^0_X0) does not change when one replaces the base field k'",
    "λ(D^0_{X_0}) (lambda, checked in a crop; the χ of the lines above is a different glyph)",
    r"\lambda(\underline{D}^0_{X_0})",
    "misprint_in_print", "high", None,
    "The TeX keeps the printed λ; the Euler characteristic χ just defined is meant.",
    corrected=r"\chi(\underline{D}^0_{X_0})")

# ---------------- page 130 ----------------
add(130,
    "display 'χ(D^0_X0) = χ(D^0_X'0) - ℓ(O_X'0/C) = 3 - 3(g-m) - 2m = 3 - 3g + m'",
    "the first D^0 has its subscript X_0 set half a line low with an extra 0 at the upper right of the X (where the prime stands in the next term D^0_{X'_0}): D^0_{X^0_0}",
    r"\chi(\underline{D}^0_{X_0})",
    "misprint_in_print", "medium",
    {"old": r"\chi(\underline{D}^0_{X_0})",
     "new": r"\chi(\underline{D}^0_{X^0_0})"},
    "Stray typed 0 (not a prime: the left side is χ(D^0_{X_0}) of p. 129). The TeX silently drops it; the fix gives the printed reading; 'corrected' is the current TeX.",
    corrected=r"\chi(\underline{D}^0_{X_0})")

add(130,
    "last paragraph, 'if char k = 2'",
    "'char k' typed upright like the text",
    r"$char k = 2$",
    "font", "low",
    {"old": r"$char k = 2$",
     "new": r"$\mathrm{char}\, k = 2$"},
    "Operator name in math italic (c·h·a·r as a product of variables); same family as the known italic ob/Ker/Hom of Exposé VI; listed because the global item names only those three.")

# ---------------- checks ----------------
pages = {}
for p in (126, 127, 128, 129, 130):
    with open(os.path.join(FOLDER, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        pages[p] = fh.read()

ok = True
for d in F:
    t = pages[d['page']]
    if d['fix'] is not None:
        n = t.count(d['fix']['old'])
        if n != 1:
            ok = False
            print('OLD COUNT', n, d['page'], d['fix']['old'])
        if '%%%%%%%%%%' in d['fix']['old']:
            ok = False
            print('MARKER IN OLD', d['page'])
    else:
        n = t.count(d['tex'])
        if n != 1:
            ok = False
            print('TEX COUNT', n, d['page'], d['tex'])

# sequential application per page: every old must still be found once when its turn comes
for p in pages:
    t = pages[p]
    for d in [x for x in F if x['page'] == p and x['fix'] is not None]:
        n = t.count(d['fix']['old'])
        if n != 1:
            ok = False
            print('SEQ COUNT', n, p, d['fix']['old'])
        t = t.replace(d['fix']['old'], d['fix']['new'], 1)

print('checks ok' if ok else 'CHECKS FAILED')
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
from collections import Counter
c = Counter((d['page'], d['kind'] == 'misprint_in_print') for d in F)
for p in sorted(pages):
    sys.stdout.write('%d: normal %d, misprint %d\n' % (p, c[(p, False)], c[(p, True)]))
print('written', OUT, len(F))
