"""Build findings_121_125.json (scan check of SGA 5 pp. 121-125)."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_121_125.json"

R_NOTE = ("Exposé III types the derived-functor R plain (as the R of RHom, which the Exposé III \\uRHom renders "
          "\\mathrm{R}; per-place fixes of pp. 73-79 logged); \\R is \\mathbb{R} in the diplomatic s5.tex (line 47), "
          "\\mathrm{R} only in the current layer.")

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 121
add(121, "top of the page",
    "p. 121 begins 'rappelons qu'on dit que L est parfait rel. à S si L est de tor-dimension finie rel. à S et à "
    "cohomologie cohérente. Nous noterons D(X)_parf/S ...'",
    "'rappelons qu'on dit que $L$ est parfait rel. à $S$ si $L$ est de tor-dimension finie rel. à $S$ et à' ends "
    "s5.tex line 3905, the last line of page_120.tex; the folio-121 marker (line 3906) follows it, so page_121.tex "
    "begins 'cohomologie cohérente.'",
    "marker", "high", None,
    "Page 121 really begins at 'rappelons qu'on dit que' in s5.tex line 3905 (after '$L\\in\\operatorname{ob}D(X)$, "
    "'). Exact fix: python -I move_marker.py 5 121 \"rappelons qu'on dit que\" --before (the anchor occurs once "
    "before the marker; simulated in memory on both layers: the marker then splits line 3905 after "
    "'$L\\in\\operatorname{ob}D(X)$, ', and page 121 begins 'rappelons qu'on dit que $L$ est parfait'). The moved "
    "words agree with the print.")

add(121, "6.2, 'i.e. (SGA 6 III 1.5) si Tor_i^S(O_X,O_Y) = 0 pour i ≠ 0'",
    "Tor underlined (the sheaf Tor), the underline running from T to r",
    "$\\Tor_i^S(\\cO_X,\\cO_Y)=0$ (\\Tor is the plain \\DeclareMathOperator)",
    "underline", "high", {"old": "\\Tor_i^S", "new": "\\underline{\\Tor}_i^S"},
    "Written like the file's \\underline{\\Hom}. The only Tor of these pages.")

add(121, "same formula, 'Tor_i^S(O_X,O_Y)'",
    "O_X , O_Y without indices, in the sentence 'si X_1 et X_2 sont tor-indépendants sur S , i.e. ... si "
    "Tor_i^S(O_X,O_Y) = 0'",
    "\\Tor_i^S(\\cO_X,\\cO_Y) (keeps the printed reading)",
    "misprint_in_print", "medium", None,
    "The schemes of the sentence are X_1 and X_2; the print copies the letters of the cited definition "
    "(SGA 6 III Définition 1.5: 'Soient X et Y deux S-schémas'). The TeX keeps the printed reading. Medium: the "
    "letters may be meant as a quotation of that definition.",
    corrected="(\\cO_{X_1},\\cO_{X_2})")

# ---------------------------------------------------------------- p. 122
add(122, "'Rappelons seulement les formules d'adjonction partielle Hom_f^(1)(L,M) = Hom(M,f_*L) ( pour M ∈ ob "
         "D^-(Y) , L ∈ ob D^+(X))'",
    "the parenthesis begins with 'pour': '( pour M ∈ ob D^-(Y) , L ∈ ob D^+(X))'",
    "\\quad(M\\in\\operatorname{ob}D^{-}(Y),\\ L\\in\\operatorname{ob}D^+(X)),",
    "missing", "high", {"old": "\\quad(M\\in", "new": "\\quad(\\text{pour }M\\in"},
    "Independent of the three display-to-inline edits of this passage (no overlap).")

add(122, "'Hom_f^(3)(L,M) = Hom(f_*L,M) (pour f propre, L ∈ ob D(X)_coh , M ∈ ob D^+(Y)) .'",
    "'(pour f propre, ...'",
    "\\quad(f\\text{ propre},\\ L\\in\\operatorname{ob}D(X)_{\\mathrm{coh}},\\ M\\in\\operatorname{ob}D^+(Y)).",
    "missing", "high", {"old": "\\quad(f\\text{ propre}", "new": "\\quad(\\text{pour }f\\text{ propre}"},
    "Independent of the three display-to-inline edits of this passage (no overlap).")

LAYOUT_SCAN = ("both formulas run in the text: '... seulement les formules d'adjonction partielle Hom_f^(1)(L,M) = "
               "Hom(M,f_*L) ( pour M ∈ ob D^-(Y) , L ∈ ob D^+(X)) , Hom_f^(3)(L,M) = Hom(f_*L,M) (pour f propre, "
               "L ∈ ob D(X)_coh , M ∈ ob D^+(Y)) .'")
LAYOUT_TEX = "two displays \\[ ... \\] \\[ ... \\] after 'partielle', before \\subsection*{6.3}"
add(122, "the two partial adjunction formulas, opening of the first", LAYOUT_SCAN, LAYOUT_TEX,
    "other", "high", {"old": "partielle\n\\[\n", "new": "partielle $"},
    "Edit 1 of 3 (display against inline formula, as the logged fix of p. 44); apply together with the two next "
    "edits: any one alone breaks the LaTeX. The \\quad and the 'pour' of the two 'missing' edits stay inside the "
    "inline formulas.")
add(122, "the two partial adjunction formulas, between them", LAYOUT_SCAN, LAYOUT_TEX,
    "other", "high", {"old": "D^+(X)),\n\\]\n\\[\n", "new": "D^+(X))$, $"},
    "Edit 2 of 3; the comma stands after the closing parenthesis, as printed.")
add(122, "the two partial adjunction formulas, closing of the second", LAYOUT_SCAN, LAYOUT_TEX,
    "other", "high", {"old": "D^+(Y)).\n\\]\n", "new": "D^+(Y))$.\n"},
    "Edit 3 of 3; the full stop is printed.")

add(122, "'avec f propre afin d'éviter les pro-objets dûs à un f_! )'",
    "dûs, with a typed circumflex on the u (clear)",
    "pro-objets dus à un $f_!$",
    "misprint_in_print", "high", {"old": "dus à un", "new": "dûs à un"},
    "Plural of the participle dû is dus (the circumflex only in the masculine singular). The TeX silently "
    "corrects; the fix restores the printed reading (diplomatic layer only).",
    corrected="dus à un")

# ---------------------------------------------------------------- p. 123
add(123, "top of the page",
    "p. 123 begins '2.2.3, 2.2.4 (sous réserve qu'elles soient définies) sont des isomorphismes dès que E_1 et E_2 "
    "sont parfaits'; p. 122 ends '(2.2.3, 2.2.4) sont définies, et les flèches' above its footnote",
    "'2.2.3, 2.2.4 (' ends s5.tex line 3945, the last line of page_122.tex; the folio-123 marker (line 3946) "
    "follows it, so page_123.tex begins 'sous réserve qu'elles soient définies)'",
    "marker", "high", None,
    "Page 123 really begins at '2.2.3, 2.2.4 (' at the end of s5.tex line 3945. Exact fix: python -I "
    "move_marker.py 5 123 \"2.2.3, 2.2.4 (\" --before (the earlier '(2.2.3, 2.2.4) sont' of the same line does not "
    "match the anchor; simulated in memory on both layers: the marker then splits line 3945 after 'et les flèches "
    "', and page 123 begins '2.2.3, 2.2.4 ('). The moved words agree with the print.")

add(123, "'et les flèches de Künneth f_1^!Q_1 ⊗_S Q_2 ⟶ (f_1 x_S Y_2)^!(Q_1 ⊗_S Q_2) , f_1^!Q_1 ⊗_S F_2 ⟶ "
         "(f_1 x_S Y_2)^!(Q_1 ⊗_S F_2) des isomorphismes.'",
    "the two arrows run in the text, on the line that begins 'Künneth'; 'des isomorphismes.' follows on the next "
    "line; a comma between the arrows, nothing after the second",
    "a display \\[ ... ,\\qquad ... \\] between 'Künneth' and 'des isomorphismes'",
    "other", "high",
    {"old": "Künneth\n\\[\nf_1^!Q_1\\otimes_S^{\\mathbf L}Q_2\\to(f_1\\times_SY_2)^!(Q_1\\otimes_S^{\\mathbf L}Q_2),"
            "\\qquad\nf_1^!Q_1\\otimes_S^{\\mathbf L}F_2\\to(f_1\\times_SY_2)^!(Q_1\\otimes_S^{\\mathbf L}F_2)\n"
            "\\]\ndes",
     "new": "Künneth $f_1^!Q_1\\otimes_S^{\\mathbf L}Q_2\\to(f_1\\times_SY_2)^!(Q_1\\otimes_S^{\\mathbf L}Q_2)$, "
            "$f_1^!Q_1\\otimes_S^{\\mathbf L}F_2\\to(f_1\\times_SY_2)^!(Q_1\\otimes_S^{\\mathbf L}F_2)$ des"},
    "Display against inline formula (as p. 44). The derived tensors are left as they stand for the Exposé III "
    "tensor pass.")

add(123, "'d'où, en composant avec l'isomorphisme de Künneth (6.3) q_1^!O_S ⊗_S L_2 ⥲ p_2^!L_2 une flèche'",
    "no comma after p_2^!L_2 (a blank, then 'une')",
    "$q_1^!\\cO_S\\otimes_S^{\\mathbf L}L_2\\xrightarrow{\\sim}p_2^!L_2$, une flèche",
    "punctuation", "high", {"old": "p_2^!L_2$, une flèche", "new": "p_2^!L_2$ une flèche"},
    "The TeX adds the comma.")

# ---------------------------------------------------------------- p. 124
add(124, "'et les éléments de Hom(c_1^*L_1,c_2^!L_2) = H^0(X,c_*c^!RHom(p_1^*L_1,p_2^!L_2)) s'appelleront ...'",
    "the formula runs in the text, on the line that begins 'et les éléments de', followed by 's'appelleront cor-'",
    "a display \\[\\Hom(c_1^*L_1,c_2^!L_2)=H^0(X,c_*c^!\\uRHom(p_1^*L_1,p_2^!L_2))\\]",
    "other", "high",
    {"old": "éléments de\n\\[\n\\Hom(c_1^*L_1,c_2^!L_2)=H^0(X,c_*c^!\\uRHom(p_1^*L_1,p_2^!L_2))\n\\]\ns'appelleront",
     "new": "éléments de $\\Hom(c_1^*L_1,c_2^!L_2)=H^0(X,c_*c^!\\uRHom(p_1^*L_1,p_2^!L_2))$ s'appelleront"},
    "Display against inline formula (as p. 44). No overlap with the underline edit that follows.")

add(124, "'s'appelleront correspondances (cohomologiques) de L_1 à L_2 à support dans C .'",
    "underlined: 'cor-respondances', 'de', 'à', 'à support dans' (not the letters L_1, L_2, C); '(cohomologiques)' is "
    "not underlined",
    "\\emph{correspondances (cohomologiques) de $L_1$ à $L_2$ à support dans $C$}",
    "underline", "high",
    {"old": "\\emph{correspondances (cohomologiques) de", "new": "\\emph{correspondances} (cohomologiques) \\emph{de"},
    "\\emph is the file's command for the print's underline in Exposé III; the closing brace of the old \\emph now "
    "closes the second one.")

add(124, "'d'où, par application de RΓ(Y,-) , un isomorphisme'",
    "a plain typed R (the typeface of the text) before the hand-drawn Γ",
    "$\\R\\Gamma(Y,-)$",
    "font", "high", {"old": "$\\R\\Gamma(Y,-)$", "new": "$\\mathrm{R}\\Gamma(Y,-)$"},
    R_NOTE)

add(124, "'On en déduit un corollaire analogue à 6.5, et, dans le cas où Y_1 = Y_2 = S est le spectre d'un corps'",
    "a comma after 6.5: '6.5, et, dans'",
    "analogue à 6.5 et, dans le cas",
    "punctuation", "high", {"old": "analogue à 6.5 et,", "new": "analogue à 6.5, et,"},
    "The misprint 6.5 (next finding) is left as printed; its correction changes only the number.")

add(124, "same sentence, 'un corollaire analogue à 6.5'",
    "'6.5', the number of the paragraph itself",
    "analogue à 6.5 (keeps the printed reading; the current layer too)",
    "misprint_in_print", "high", None,
    "6.5 transposes § 3 point by point: a diagram analogous to 3.4.1, then the corollary, then a description "
    "analogous to 3.6; that corollary is Corollaire 3.5 (s5.tex line 2720). The TeX keeps the printed reading.",
    corrected="analogue à 3.5")

add(124, "'Etant donné un carré commutatif 3.7.1, avec c propre, on a, pour K ∈ ob D^+(C) une flèche canonique'",
    "no comma after D^+(C)",
    "pour $K\\in\\operatorname{ob}D^+(C)$, une flèche canonique",
    "punctuation", "high", {"old": "D^+(C)$, une flèche", "new": "D^+(C)$ une flèche"},
    "The TeX adds the comma.")

# ---------------------------------------------------------------- p. 125
add(125, "top of the page",
    "p. 125 begins with the displays (6.5.4) and (6.5.5), then 'analogues à 3.7.5, 3.7.6.'; p. 124 ends "
    "'Prenant K = RHom_S(L_1,L_2) , on déduit de 6.5.3 et 6.5.1 des flèches canoniques'",
    "the displays (6.5.4) and (6.5.5) (s5.tex lines 4007-4013) stand in page_124.tex; the folio-125 marker "
    "(line 4014) sits inside the equation environment of (6.5.5), before its \\end{equation}",
    "marker", "high", None,
    "Page 125 really begins at the \\begin{equation} of (6.5.4), s5.tex line 4007. Exact fix (bash): python -I "
    "move_marker.py 5 125 $'\\\\begin{equation}\\n\\\\tag{6.5.4}' --before (the anchor is '\\begin{equation}', a "
    "line break, '\\tag{6.5.4}'; '\\tag{6.5.4}' alone would leave the \\begin{equation} on p. 124; simulated in "
    "memory on both layers: the marker then stands between '... des flèches canoniques' and '\\begin{equation}'). "
    "The two displays agree with the print.")

add(125, "foot of the page: the last line of page_125.tex",
    "p. 125 ends '... s'identifie canoniquement à e_*K_E (resp. H^0(E,K_E)) .'; the rest of the page is blank",
    "page_125.tex ends with the paragraph 'Le théorème 4.4 a l'%' (s5.tex line 4044), which p. 125 does not "
    "print; the folio-126 marker (line 4045) follows it",
    "marker", "high", None,
    "Page 126 begins at 'Le théorème 4.4 a l'' (s5.tex line 4044; p. 126 itself is not in this batch). Exact fix: "
    "python -I move_marker.py 5 126 \"Le théorème 4.4 a l'\" --before (simulated in memory on both layers: the "
    "marker then stands on its own line before line 4044; the % after l' still joins 'l'analogue suivant').")

add(125, "end of display (6.6.2)",
    "no punctuation after '... ⊗ Rd_*O_D,K_X)'",
    "\\uRHom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*\\cO_D,K_X),",
    "punctuation", "high", {"old": "K_X),", "new": "K_X)"},
    "Punctuation added at the end of a display; (6.6.1) and (6.6.3) end with a printed full stop, as the TeX. "
    "No overlap with the R edit of (6.6.2).")

add(125, "'D'après 6.1.1, on a c_*c^!P = RHom(Rc_*O_C,P)'",
    "Rc_*O_C with a plain typed R",
    "c_*c^!P=\\uRHom(\\R c_*\\cO_C,P)",
    "font", "high", {"old": "\\uRHom(\\R c_*\\cO_C,P)", "new": "\\uRHom(\\mathrm{R}c_*\\cO_C,P)"},
    R_NOTE)

add(125, "(6.6.1), 'RHom(Rc_*O_C ⊗ Rd_*O_D , P ⊗ Q)'",
    "both R plain typed",
    "\\uRHom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*\\cO_D,P\\otimes^{\\mathbf L}Q)",
    "font", "high",
    {"old": "\\uRHom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*\\cO_D,P",
     "new": "\\uRHom(\\mathrm{R}c_*\\cO_C\\otimes^{\\mathbf L}\\mathrm{R}d_*\\cO_D,P"},
    "Two signs in one edit. " + R_NOTE)

add(125, "(6.6.2), right-hand side 'RHom(Rc_*O_C ⊗ Rd_*O_D,K_X)'",
    "both R plain typed",
    "\\longrightarrow\\uRHom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*\\cO_D,K_X),",
    "font", "high",
    {"old": "\\longrightarrow\\uRHom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*",
     "new": "\\longrightarrow\\uRHom(\\mathrm{R}c_*\\cO_C\\otimes^{\\mathbf L}\\mathrm{R}d_*"},
    "Two signs in one edit. " + R_NOTE)

add(125, "(6.6.3), right-hand side 'Hom(Rc_*O_C ⊗ Rd_*O_D,K_X)'",
    "both R plain typed",
    "\\longrightarrow\\Hom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*\\cO_D,K_X).",
    "font", "high",
    {"old": "\\longrightarrow\\Hom(\\R c_*\\cO_C\\otimes^{\\mathbf L}\\R d_*",
     "new": "\\longrightarrow\\Hom(\\mathrm{R}c_*\\cO_C\\otimes^{\\mathbf L}\\mathrm{R}d_*"},
    "Two signs in one edit. " + R_NOTE)

add(125, "(6.6.3), the pairing '< , > :'",
    "typed less-than and greater-than signs with a comma between: '<  , > :'",
    "\\langle\\ ,\\ \\rangle:",
    "symbol", "high", None,
    "A typewriter stand-in, like x for the product sign; the TeX writes \\langle ... \\rangle for the pairing "
    "throughout (66 times in s5.tex, e.g. lines 2907, 2970, 3467; only this occurrence is on pp. 121-125). "
    "Reported once as a convention, no edit: add it to the forms handled globally, or change it volume-wide.")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print(len(F), "findings written")
