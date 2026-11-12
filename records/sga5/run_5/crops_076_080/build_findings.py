"""Build findings_076_080.json and check that every fix's old occurs exactly once in its page file.
usage: python -I build_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
B = RUN / "b076_080"
OUT = RUN / "findings_076_080.json"

PLAIN_R = ("Exposé III types the derived-functor R plain (as R\\Gamma on p. 73 and RHom on pp. 74-75); "
           "\\R is \\mathbb{R}.")

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 76 ----------------
add(76, "heading of § 1, top of the page",
    "'1. Notations et rappels de formules de Künneth.': the number 1. and a full stop after Künneth (the rule runs from 1. to Künneth)",
    "\\section*{Notations et rappels de formules de Künneth} (no number, no full stop)",
    "number", "high",
    {"old": "\\section*{Notations et rappels de formules de Künneth}",
     "new": "\\section*{1. Notations et rappels de formules de Künneth.}"},
    "The headings carry the print's own numbers (global '\\section{' -> '\\section*{' pass; cf. '\\section*{5. Dualité locale sur les courbes.}', whose full stop was restored on p. 50). The underline is the accepted \\section* setting.")

add(76, "every derived tensor product of pp. 76-80 (27 signs), first 1.1 'E ⊗ F ∈ ob D_ctf(X)'",
    "a plain upright typed capital L standing directly above the hand-drawn ⊗, S (where present) at its lower right",
    "\\otimes^{L} (a math-italic L set as a superscript): p. 76 'E \\otimes^{L} F', p. 77 (1.6.1) 'f_1^{*}M_1\\otimes^{L}_{S}f_2^{*}M_2', p. 80 (1.7.6) 'K_{X_1}\\otimes^{L}_{S}K_{X_2}'",
    "font", "high", None,
    "Convention of the Exposé III transcription, not listed per occurrence: s5.tex (lines 1929-4364) writes \\otimes^{L} 48 times (27 of them on pp. 76-80, every one printed with the stacked L) and \\otimes^L 116 times. The fixes of pp. 37, 45, 46 and 70 gave this sign as \\overset{\\mathrm{L}}{\\otimes} (the file's \\lten): one scoped pass '\\otimes^{L}' / '\\otimes^L' -> '\\overset{\\mathrm{L}}{\\otimes}' (subscripts stay), once the later pages of Exposé III confirm the stacked form. See the message.")

add(76, "1.1, 'on a aussi RHom(E,F) ∈ ob D_ctf(X)'",
    "RHom: a plain typed R; the underline runs under Hom only",
    "$\\uRHom(E,F)$ (\\underline{\\mathbb{R}\\mathrm{Hom}}: double-struck R, R underlined too)",
    "font", "high",
    {"old": "aussi $\\uRHom(E,F)", "new": "aussi $R\\underline{\\Hom}(E,F)"},
    "As the RHom fixes of pp. 74-75. " + PLAIN_R)

add(76, "1.2, display, 'Rf_*D_ctf(X) ⊂ D_ctf(Y) ,'",
    "a plain typed R (the typeface of the text)",
    "\\R f_{*}D_{\\ctf}(X)",
    "font", "high",
    {"old": "\\R f_{*}D", "new": "Rf_{*}D"},
    PLAIN_R)

add(76, "1.2, display, 'Rf_!D_ctf(X) ⊂ D_ctf(Y) ,'",
    "a plain typed R",
    "\\R f_{!}D_{\\ctf}(X)",
    "font", "high",
    {"old": "\\R f_{!}D", "new": "Rf_{!}D"},
    PLAIN_R + " The print sets the three inclusions on three display lines (layout, not reported).")

add(76, "1.2, display, 'Rf^!D_ctf(Y) ⊂ D_ctf(X) ,'",
    "a plain typed R",
    "\\R f^{!}D_{\\ctf}(Y)",
    "font", "high",
    {"old": "\\R f^{!}D", "new": "Rf^{!}D"},
    PLAIN_R)

add(76, "1.2, '(l'inclusion relative à Rf_! n'utilise que'",
    "a plain typed R",
    "$\\R f_{!}$",
    "font", "high",
    {"old": "relative à $\\R f_{!}$", "new": "relative à $Rf_{!}$"},
    PLAIN_R)

add(76, "1.2, 'nous écrirons parfois f_* , f_! , f^! au lieu de Rf_* , Rf_! , Rf^! ;'",
    "three plain typed R",
    "$\\R f_{*}$, $\\R f_{!}$, $\\R f^{!}$",
    "font", "high",
    {"old": "au lieu de $\\R f_{*}$, $\\R f_{!}$, $\\R f^{!}$",
     "new": "au lieu de $Rf_{*}$, $Rf_{!}$, $Rf^{!}$"},
    PLAIN_R + " Three adjacent signs in one edit.")

add(76, "1.3, 'et noterons D_X (ou D ) le foncteur RHom(-,K_X)'",
    "RHom: a plain typed R; the underline runs under Hom only",
    "$\\uRHom(-,K_X)$",
    "font", "high",
    {"old": "foncteur $\\uRHom(-,K_X)", "new": "foncteur $R\\underline{\\Hom}(-,K_X)"},
    "As the RHom fixes of pp. 74-75. Does not touch the anchor of the folio-77 marker move.")

# ---------------- page 77 ----------------
add(77, "top of the page",
    "p. 77 begins '4.3), le complexe K_X est dualisant'; p. 76 ends 'et noterons ... RHom(-,K_X) . D'après (SGA 4^{1/2} Th. Finitude'",
    "'4.3), le' ends s5.tex line 1987 (both layers, as of 19:03), the last line of page_076.tex; the folio-77 marker (line 1988) follows it",
    "marker", "high", None,
    "Page 77 really begins at '4.3), le' at the end of s5.tex line 1987. Exact fix: python -I move_marker.py 5 77 '4.3), le' --before (single quotes; the anchor occurs once in s5.tex; simulated in memory on both layers: the marker then splits line 1987 after 'Th.~Finitude ', and page 77 begins '4.3), le' + 'complexe $K_X$ est dualisant'). No other fix of this batch touches the anchor.")

add(77, "1.4, display, 'Hom_f^(1)(L,M) = Hom(f^*M,L) ( ≃ Hom(M,f_*L) )'",
    "no punctuation after the closing parenthesis (clean paper)",
    "\\Hom(M,f_{*}L)), (a comma added)",
    "punctuation", "high",
    {"old": "\\Hom(M,f_{*}L)),", "new": "\\Hom(M,f_{*}L))"},
    "Punctuation added at the end of a display. Only the fourth line of the definition ends with a printed full stop.")

add(77, "1.4, display, 'Hom_f^(2)(L,M) = Hom(L,f*M)'",
    "no punctuation at the end of the line",
    "=\\Hom(L,f^{*}M), (a comma added)",
    "punctuation", "high",
    {"old": "=\\Hom(L,f^{*}M),", "new": "=\\Hom(L,f^{*}M)"},
    "Punctuation added at the end of a display.")

add(77, "1.4, display, 'Hom_f^(3)(L,M) = Hom(f_!L,M) ( ≃ Hom(L,f^!M) )'",
    "no punctuation after the closing parenthesis",
    "\\Hom(L,f^{!}M)), (a comma added)",
    "punctuation", "high",
    {"old": "\\Hom(L,f^{!}M)),", "new": "\\Hom(L,f^{!}M))"},
    "Punctuation added at the end of a display.")

# ---------------- page 78 ----------------
add(78, "'Prenant M_i = f_i*L_i , et u_i , de type 1, donné par l'identité de f_i*L_i ,'",
    "a comma after u_i (before 'de type 1')",
    "et $u_i$ de type~1, (no comma after u_i)",
    "punctuation", "high",
    {"old": "et $u_i$ de type~1,", "new": "et $u_i$, de type~1,"},
    "The print sets 'de type 1' off by two commas.")

add(78, "'1.6.2 fournit une flèche de Künneth (cf. (SGA 4 XVII 5.4.1.4))'",
    "(cf. (SGA 4 XVII 5.4.1.4)): the reference in its own parentheses inside the cf. parentheses",
    "(cf.~SGA~4~XVII~5.4.1.4)",
    "punctuation", "high",
    {"old": "(cf.~SGA~4~XVII~5.4.1.4)", "new": "(cf.~(SGA~4~XVII~5.4.1.4))"},
    "As '(cf. (loc. cit. 5.2.4))' on the same page, which the TeX has.")

add(78, "'D'après (SGA 4^{1/2} Th. Finitude 1.9), 1.6.4 est un isomorphisme : par 1.6.3'",
    "'est un isomorphisme' underlined (not 1.6.4, not the colon)",
    "1.6.4 est un isomorphisme : (no underline)",
    "underline", "high",
    {"old": "1.6.4 est un isomorphisme :", "new": "1.6.4 \\emph{est un isomorphisme} :"},
    "\\emph is this file's command for the print's underline in § 1 (\\emph{flèches de type ...}, \\emph{flèche de Künneth}).")

add(78, "'Quant f_1 et f_2 sont propres, il n'est pas nécessaire d'invoquer (loc. cit.)'",
    "Quant, with a final t (crisp at 3x)",
    "Quand $f_1$",
    "misprint_in_print", "high",
    {"old": "Quand $f_1$", "new": "Quant $f_1$"},
    "The conjunction is 'Quand'; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only). The line above prints '(loc. cit. App.          ).' with a blank left for a reference that was never filled in (spacing only, not reported, as on p. 26).",
    corrected="Quand $f_1$")

add(78, "1.7, 'on obtient un isomorphisme de Künneth (SGA 4 XVII 5.4.3)'",
    "'isomorphisme de Künneth' underlined (across the line break)",
    "un isomorphisme de Künneth (no underline)",
    "underline", "high",
    {"old": "un isomorphisme de Künneth", "new": "un \\emph{isomorphisme de Künneth}"},
    "As \\emph{flèche de Künneth}. The earlier 'l'isomorphisme de Künneth (SGA 4 XVII 5.4.3)' at the end of 1.6 is not underlined (right as it stands).")

# ---------------- page 79 ----------------
add(79, "label of Proposition 1.7.4",
    "'Proposition 1.7.4 - La flèche ...': 'Proposition' underlined, then the number and a typewriter dash, the statement run in",
    "\\subsection*{Proposition 1.7.4} (no dash)",
    "punctuation", "high",
    {"old": "\\subsection*{Proposition 1.7.4}", "new": "\\subsection*{Proposition 1.7.4 -}"},
    "Exposé III's label form ('Proposition 1.7.4 -') differs from the 'Définition 1.1. :' form handled globally; drop this edit if the global label decision is meant to cover the dash as well. The run-in and the label's underline are the accepted \\subsection* setting.")

add(79, "statement of Proposition 1.7.4",
    "'La flèche 1.7.3 est un isomorphisme' underlined; the rule stops before the full stop",
    "La flèche 1.7.3 est un isomorphisme. (no underline)",
    "underline", "high",
    {"old": "La flèche 1.7.3 est un isomorphisme.", "new": "\\emph{La flèche 1.7.3 est un isomorphisme}."},
    "Underlined statement (as the statement of p. 62).")

add(79, "proof of 1.7.4, 'Par localisation sur X_2 , on peut supposer d'autre part que f_1 = g_1j_1'",
    "X_2 (clear)",
    "Par localisation sur $X_2$ (as printed)",
    "misprint_in_print", "high", None,
    "The factorization f_1 = g_1j_1 (closed immersion, then smooth) exists locally on the source X_1 of f_1; after the reduction to X_2 = Y_2, f_2 = 1, localizing on X_2 does nothing for f_1. The TeX keeps the printed reading; the corrected layer already has X_1 (Codex SGA-SRC-001843, FIXLOG_5_CURRENT).",
    corrected="Par localisation sur $X_1$")

add(79, "proof of 1.7.4, the two cases 'a) f_1 = g_1' and 'b) f_1 = j_1 .'",
    "no punctuation after g_1 (two lines; a full stop after j_1)",
    "\\text{a) } f_1=g_1,\\qquad \\text{b) } f_1=j_1. (a comma added after g_1)",
    "punctuation", "high",
    {"old": "f_1=g_1,\\qquad", "new": "f_1=g_1\\qquad"},
    "Punctuation added in a display. The two cases on one line is layout (not reported).")

add(79, "case a), 'un isomorphisme f_1^*M_1(n_1)[2n_1] ⟶~ f_1^!M_1 : celui-ci est compatible'",
    "a colon after f_1^!M_1 (two dots)",
    "f_1^{!}M_1; (a semicolon)",
    "punctuation", "high",
    {"old": "f_1^{!}M_1;", "new": "f_1^{!}M_1 :"},
    "The print runs the formula into the text (the TeX's display is layout, not reported); only the sign differs.")

add(79, "case b), 'on a une suite exact'",
    "exact, without a final e (clean paper after the t)",
    "une suite exacte",
    "misprint_in_print", "high",
    {"old": "une suite exacte", "new": "une suite exact"},
    "Agreement with 'suite'; the TeX silently corrects. The fix restores the printed reading (diplomatic layer only).",
    corrected="une suite exacte")

add(79, "case b), display '0 ⟶ j_1*Rj_1^!M_1 ⟶ M_1 ⟶ Ri_1*i_1^*M_1 ⟶ 0 ,', first R",
    "a plain typed R",
    "j_{1*}\\R j_1^{!}M_1",
    "font", "high",
    {"old": "j_{1*}\\R j_1^{!}M_1", "new": "j_{1*}Rj_1^{!}M_1"},
    PLAIN_R)

add(79, "same display, second R, 'Ri_1*i_1^*M_1'",
    "a plain typed R",
    "\\R i_{1*}i_1^{*}M_1",
    "font", "high",
    {"old": "\\R i_{1*}i_1^{*}M_1", "new": "Ri_{1*}i_1^{*}M_1"},
    PLAIN_R)

add(79, "'et la compatibilité de Ri_1* au changement de base'",
    "a plain typed R",
    "$\\R i_{1*}$",
    "font", "high",
    {"old": "compatibilité de $\\R i_{1*}$", "new": "compatibilité de $Ri_{1*}$"},
    PLAIN_R)

add(79, "'Grâce à 1.7.3, on peut définir, pour u_i ∈ Hom_f^(4)(L_i,M_i) ,'",
    "Hom_f^(4): index f alone, no i below it (clean paper; compare Hom_{f_i}^(3)(L_i,M_i) on p. 78)",
    "$u_i\\in\\Hom_f^{(4)}(L_i,M_i)$ (as printed)",
    "misprint_in_print", "high", None,
    "u_i is an f_i-arrow from L_i to M_i, as in 1.6.2 and 1.7.2 (Hom_{f_i}^(1), Hom_{f_i}^(3)). The TeX keeps the printed reading; the corrected layer already has f_i (Codex SGA-SRC-001844, FIXLOG_5_CURRENT).",
    corrected="$u_i\\in\\Hom_{f_i}^{(4)}(L_i,M_i)$")

# ---------------- page 80 ----------------
DMINUS = ("A short stroke at cap height squeezed between D and the parenthesis, far above the typewriter hyphen: a raised "
          "minus typed in afterwards (D(X), D(Y), D(S') all three have it; the D(X), D(Y) of 1.4 on p. 77 have none). "
          "The external products of 1.5-1.7.5, which 1.8.1 applies, are defined for complexes in D^-. A typist's "
          "insertion: both layers.")
add(80, "1.8, 'L ∈ ob D^-(X)'",
    "D^-(X): a raised minus after D, squeezed against the parenthesis",
    "$L\\in\\ob D(X)$",
    "formula", "high",
    {"old": "$L\\in\\ob D(X)$", "new": "$L\\in\\ob D^{-}(X)$"},
    DMINUS)

add(80, "1.8, 'M ∈ ob D^-(Y)'",
    "D^-(Y): the same raised minus",
    "$M\\in\\ob D(Y)$",
    "formula", "high",
    {"old": "$M\\in\\ob D(Y)$", "new": "$M\\in\\ob D^{-}(Y)$"},
    "As L ∈ ob D^-(X).")

add(80, "1.8, 'P ∈ ob D^-(S')'",
    "D^-(S'): the same raised minus",
    "$P\\in\\ob D(S')$",
    "formula", "high",
    {"old": "$P\\in\\ob D(S')$", "new": "$P\\in\\ob D^{-}(S')$"},
    "As L ∈ ob D^-(X).")

add(80, "1.8, 'au-dessus de la flèche identique de S' : pour u ∈ Hom_f^(i)(L,M)'",
    "a colon after S'",
    "de $S'$; pour (a semicolon)",
    "punctuation", "high",
    {"old": "$S'$; pour", "new": "$S'$ : pour"},
    "")

# ---------------- write and check ----------------
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
bad = 0
for x in F:
    if not x["fix"]:
        continue
    t = (B / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    old, new = x["fix"]["old"], x["fix"]["new"]
    n = t.count(old)
    if n != 1 or "%%%%%%%%%%" in old:
        bad += 1
        print("NOT UNIQUE", x["page"], n, repr(old))
# apply all fixes of each page in order on a copy, to catch overlaps
for p in range(76, 81):
    t = (B / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for x in F:
        if x["page"] == p and x["fix"]:
            if t.count(x["fix"]["old"]) != 1:
                bad += 1
                print("OVERLAP", p, repr(x["fix"]["old"]))
            t = t.replace(x["fix"]["old"], x["fix"]["new"], 1)
from collections import Counter
c = Counter((x["page"], x["kind"] == "misprint_in_print") for x in F)
print("written", OUT, len(F), "findings; problems:", bad)
for p in range(76, 81):
    print(p, c[(p, False)], "/", c[(p, True)])
