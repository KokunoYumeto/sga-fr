"""Write findings_041_045.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b041_045"


def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 41
    F(41, "(2.8), condition on i",
      "C^i(L(D)) = 0   (i ≥ 1)  (both scans)",
      "C^i(L(D))=0\\quad (i\\geq 1)  (printed reading kept)",
      "misprint_in_print", "high", None,
      "Misprint of the print: with C^1(L(D)) = ℓ(D) the vanishing holds only for i > 1. The TeX keeps the printed "
      "reading; the corrected layer already reads (i>1).",
      corrected="(i>1)"),
    F(41, "(2.10), end of the display",
      "f^! : K(Y) ⟶ K(X)        (*)  : no comma after K(X) (only a speck in the main scan; the witness is clean)",
      "\\underline{K}(X),\\footnote{...}",
      "punctuation", "high",
      {"old": "\\underline{K}(X),\\footnote{", "new": "\\underline{K}(X)\\footnote{"},
      "The TeX adds a comma at the end of the display."),
    F(41, "after (2.10): '(on écrit ici K(X) au lieu de K(X))'",
      "(on écrit ici K̲(X) au lieu de K̲(X)), both K underlined (both scans)",
      "(on écrit ici $\\underline{K}(X)$ au lieu de $\\underline{K}(X)$)  (printed reading kept)",
      "misprint_in_print", "medium", None,
      "The remark names the same symbol twice. The group was introduced as K(ξ(X)) in (2.5)-(2.6) "
      "(\\underline{K}(\\xi(X))), so the intended reading is 'K(X) au lieu de K(ξ(X))'; another possible reading is "
      "'K(X) [plain, as in the diagram] au lieu de K̲(X)'. The TeX keeps the printed reading (so does the corrected "
      "layer).",
      corrected="(on écrit ici $\\underline{K}(X)$ au lieu de $\\underline{K}(\\xi(X))$)"),
    F(41, "diagram after (2.10), bottom arrow A(Y) -> A(X)",
      "label f* above the bottom arrow (both scans)",
      "\\arrow[r,\"f^*\"'] (the ' sets the label below the arrow)",
      "formula", "medium",
      {"old": "\\arrow[r,\"f^*\"']", "new": "\\arrow[r,\"f^*\"]"},
      "Label on the wrong side of the arrow (the other three labels are placed as printed)."),
    F(41, "footnote (*), 'R. Hartshorne, Residues and Duality'",
      "Residues and Duality: not underlined (both scans)",
      "\\emph{Residues and Duality} (this file's command for the print's underline)",
      "underline", "high",
      {"old": "\\emph{Residues and Duality}", "new": "Residues and Duality"},
      "The book title is typed plain in the print."),
    # ---------------- page 42
    F(42, "Corollaire (to Prop. 2.3): 'est combinaisons linéaire'",
      "est combinaisons linéaire",
      "est combinaisons linéaire (printed reading kept)",
      "misprint_in_print", "high", None,
      "Agreement slip of the print; the TeX keeps it; the corrected layer already reads 'combinaison linéaire'.",
      corrected="combinaison linéaire"),
    F(42, "Corollaire (to Prop. 2.3), end",
      "... si Y est irréductible)  : no full stop after the parenthesis (both scans)",
      "irréductible)}.",
      "punctuation", "high",
      {"old": "irréductible)}.", "new": "irréductible)}"},
      "The TeX adds a final full stop."),
    F(42, "§2, first paragraph: 'éléments de la forme (E) - (E') - (E\"), où E'",
      "(E) - (E') - (E\"), inline in the running text: 'de la forme (E) - (E') - (E\"), où E est une extension'",
      "\\[ (E)-(E')-(E''), \\] (a display)",
      "other", "medium",
      {"old": "de la forme\n\\[\n(E)-(E')-(E''),\n\\]\noù $E$", "new": "de la forme $(E)-(E')-(E'')$, où $E$"},
      "The print sets the expression inline; the TeX makes it a display (same kind of fix as SGA 6 p. 21)."),
    F(42, "§2, first paragraph: 'et l'on omet l'indicé'",
      "l'indicé (main scan: a clear typed acute accent on the final e); the witness reads 'l'indice' without accent",
      "l'indicé (printed reading kept)",
      "misprint_in_print", "medium", None,
      "The noun is 'indice'. The main scan shows a typed é (same accent as the line's other é's); the 300-dpi "
      "witness has no accent there at all (no stray pixels), so the two copies differ at this spot (a later "
      "printing retouched, or a mark on one copy). The TeX follows the main scan; the corrected layer still reads "
      "'l'indicé'.",
      corrected="l'indice"),
    F(42, "§2, second paragraph: 'tels que pour tout A ∈ C_o, les R^qF(A)'",
      "pour tout A ∈ ℂ_o, les R^qF(A)  (comma after ℂ_o)",
      "pour tout $A\\in\\cC_0$ les $R^qF(A)$",
      "punctuation", "high",
      {"old": "pour tout $A\\in\\cC_0$ les", "new": "pour tout $A\\in\\cC_0$, les"},
      "The TeX drops the printed comma."),
    F(42, "throughout pp. 42-45 (here: 'Soit C une catégorie abélienne, et soit C_o une sous-classe de C')",
      "ℂ, ℂ_o, ℂ', ℂ_1, ℂ_2: the typewriter's double-struck C (the same glyph as the print's ℂ elsewhere)",
      "\\cC, defined in the preamble as \\mathcal C (calligraphic)",
      "font", "high", None,
      "Convention of the transcription, not a page fix: the print's double-struck category letter is written "
      "\\cC = \\mathcal C (81 occurrences on pp. 42-45, e.g. p. 42 'Soit $\\cC$ une catégorie abélienne, et soit "
      "$\\cC_0$', p. 43 '$\\cC_0\\subset\\cC_1$ deux sous-classes', p. 44 'sous-classe $\\cC_2$ de $\\cC$'). Not "
      "covered by the \\mathbf rule. One decision: redefine \\cC as \\mathbb C (first check the other uses of \\cC "
      "in main.tex, lines 1826, 3402-3403, 3737-3738, 7198, against their scans)."),
    # ---------------- page 43
    F(43, "start of page",
      "p. 43 begins 'tel que pour tout E ∈ ℂ_o les F^i(E) soient dans ℂ'_o'",
      "'tel que' is the end of the last line of page_042.tex (under the folio-42 marker); page_043.tex begins "
      "'pour tout'",
      "marker", "high", None,
      "Page 43 really begins with 'tel que'. Move the folio-43 marker before 'tel que': python -I move_marker.py 6 "
      "43 \"tel que\" --before (simulated on both layers: '... de $\\cC$ dans $\\cC'$ ', marker line, 'tel que', "
      "'pour tout ...')."),
    F(43, "Théorème 2.3, '(à isomorphisme près)'",
      "telles que les classes [underlined] (à isomorphisme près) [not underlined, heavier type] d'objets de "
      "[underlined]  (both scans)",
      "inside the \\emph block of the statement",
      "underline", "medium",
      {"old": "les classes (à isomorphisme près) d'objets",
       "new": "les classes} (à isomorphisme près) \\emph{d'objets"},
      "A whole parenthetical word group that the typist left out of the underline, not a formula or punctuation "
      "(beyond the one-block volume decision). Small words inside formula groups (resp. in (i), 'et' between the "
      "two maps in (ii)) are left to that decision."),
    F(43, "Théorème 2.3 (iii), 'pour toute résolution gauche L de A'",
      "résolution gauche L de A: plain L, no underline (both scans); later in the same line Z_d(L̲) is underlined",
      "résolution gauche $\\underline{L}$",
      "misprint_in_print", "medium",
      {"old": "résolution gauche $\\underline{L}$", "new": "résolution gauche $L$"},
      "The complex is L̲ everywhere else (Z_d(L̲), 'résolution finie L̲', p. 44); the print drops the underline here "
      "and the TeX silently restores it. Diplomatic layer: plain L.",
      corrected="résolution gauche $\\underline{L}$"),
    F(43, "Théorème 2.3 (iii), '(Z_d désigne les cycles de dimension d).'",
      "(Z_d désigne les cycles de dimension d).  not underlined (both scans)",
      "inside the \\emph of item (iii)",
      "underline", "medium",
      {"old": "\\in\\cC_0$ ($Z_d$ désigne les cycles de dimension $d$).}",
       "new": "\\in\\cC_0$} ($Z_d$ désigne les cycles de dimension $d$)."},
      "A parenthetical sentence the typist left out of the underline (as '(à isomorphisme près)' above)."),
    F(43, "Théorème 2.3, conclusion 'de K(C_o) dans K(C_1) est un isomorphisme'",
      "K(ℂ_o) dans K(ℂ_1): plain K, not underlined (both scans)",
      "$\\underline{K}(\\cC_0)$ dans $\\underline{K}(\\cC_1)$",
      "formula", "high",
      {"old": "de $\\underline{K}(\\cC_0)$ dans $\\underline{K}(\\cC_1)$ est un",
       "new": "de $K(\\cC_0)$ dans $K(\\cC_1)$ est un"},
      "The print uses plain K here, as in the definition on p. 42 ('On désigne par K(ℂ_o)', which the TeX keeps "
      "plain) and in (2.12)."),
    # ---------------- page 44
    F(44, "proof of Th. 2.3, 'avec des homomorphismes surjectifs de L\" dans L et L''",
      "surjectifs underlined",
      "homomorphismes surjectifs de (no underline)",
      "underline", "high",
      {"old": "homomorphismes surjectifs de", "new": "homomorphismes \\emph{surjectifs} de"},
      "Missing underline."),
    F(44, "proof of Th. 2.3, '(ce qui est possible grâce à (i) et (ii) ;'",
      "(ce qui est possible grâce à (i) et (ii) ; on est alors ramené ...  : the parenthesis opened before 'ce qui' "
      "is never closed (both scans)",
      "(ce qui est possible grâce à (i) et (ii)~; (printed reading kept)",
      "misprint_in_print", "low", None,
      "Unbalanced parenthesis in the print; the TeX keeps it (so does the corrected layer).",
      corrected="(ce qui est possible grâce à (i) et (ii))~;"),
    F(44, "proof of Th. 2.3, 'd'où E_C_o(N) = 0'",
      "d'où E_{ℂ_o}(N̲) = 0: plain E, no underline (both scans), while E̲ is underlined four times in the paragraph",
      "d'où $\\underline{E}_{\\cC_0}(\\underline{N})=0$",
      "misprint_in_print", "medium",
      {"old": "d'où $\\underline{E}_{\\cC_0}(\\underline{N})=0$", "new": "d'où $E_{\\cC_0}(\\underline{N})=0$"},
      "The typist dropped the underline of the Euler characteristic E̲; the TeX silently restores it. Diplomatic "
      "layer: plain E.",
      corrected="d'où $\\underline{E}_{\\cC_0}(\\underline{N})=0$"),
    F(44, "before 'On prouve de façon analogue'",
      "'On prouve de façon analogue ...' starts a new, indented paragraph",
      "de $\\underline{L}$).\\nOn prouve (single line break: same paragraph)",
      "other", "medium",
      {"old": "de $\\underline{L}$).\nOn prouve", "new": "de $\\underline{L}$).\n\nOn prouve"},
      "Missing paragraph break."),
    F(44, "'ainsi construite est additive, donc définit'",
      "additive underlined",
      "construite est additive, (no underline)",
      "underline", "high",
      {"old": "construite est additive,", "new": "construite est \\emph{additive},"},
      "Missing underline."),
    F(44, "throughout p. 44 (here: 'deuxième résolution L'', 'troisième résolution L\"')",
      "L̲', L̲\": the underline stops under the L; the primes stand after it",
      "\\underline{L'} (3 times), \\underline{L''} (4 times): the primes inside the underline",
      "underline", "low", None,
      "Extent of the underline, for one decision: a diplomatic reading is \\underline{L}' and \\underline{L}'' "
      "(e.g. 'deuxième résolution $\\underline{L'}$', 'troisième résolution $\\underline{L''}$', "
      "'$\\underline{E}_{\\cC_0}(\\underline{L''})$'); replace all 7 on the page if adopted."),
    # ---------------- page 45
    F(45, "start of page",
      "p. 44 ends with the first five lines of the Corollaire ('Soit X un espace algébrique quasi-projectif. "
      "Soient F(X) ... F_x soit un O_x-module'); p. 45 begins 'de dimension cohomologique finie (on a donc ...'",
      "page_045.tex begins '\\emph{Soit $X$ un espace algébrique quasi-projectif. Soient ...' (the folio-45 marker "
      "stands right after '\\textbf{Corollaire~:}')",
      "marker", "high", None,
      "Page 45 really begins with 'de dimension cohomologique finie'. Move the folio-45 marker down, inside the "
      "\\emph group: python -I move_marker.py 6 45 \"de dimension cohomologique finie\" (forward search; simulated "
      "on both layers: '... soit un $\\cO_x$-module ', marker line, 'de dimension cohomologique finie (on a "
      "donc ...'). The comment line inside the group does not change the output."),
    F(45, "Corollaire (printed on p. 44), '(équivalente à la catégorie des fibrés vectoriels sur X)'",
      "(équivalente à la catégorie des fibrés vectoriels sur X), not underlined (both scans)",
      "inside the \\emph block of the Corollaire",
      "underline", "medium",
      {"old": "localement libres (équivalente à la catégorie des fibrés vectoriels sur $X$), $\\cF_0(X)$",
       "new": "localement libres} (équivalente à la catégorie des fibrés vectoriels sur $X$), \\emph{$\\cF_0(X)$"},
      "A parenthetical clause the typist left out of the underline. This text belongs to p. 44 (see the marker "
      "finding); the edit is the same before or after the marker move."),
    F(45, "(2.12)",
      "K(ξ(X)) ⟶ K(F_o(X))",
      "K(\\xi(X)\\longrightarrow K(\\cF_0(X))  (one closing parenthesis missing)",
      "formula", "high",
      {"old": "K(\\xi(X)\\longrightarrow", "new": "K(\\xi(X))\\longrightarrow"},
      "Transcription slip; the corrected layer already has K(\\xi(X))."),
    F(45, "throughout this appendix (here: 'soit un O_x-module', 'l'anneau local noethérien O_x', 'un quotient de "
          "O(-n)^k')",
      "O̲_x, O̲(-n)^k: a typed O with an underline",
      "\\cO_x, \\cO(-n)^k: \\cO is defined as \\mathcal O",
      "font", "medium", None,
      "Convention for one decision, not a page fix: in this appendix the TeX writes the print's underlined O as "
      "\\cO (= \\mathcal O): '$\\cO_x$-module' (printed on p. 44), 'noethérien $\\cO_x$', '$\\cO(-n)^k$' (p. 45); "
      "the main text of Exposé 0 writes the same typed form as \\underline O (main.tex lines 262, 397, 401). The "
      "appendix continues with \\cO (main.tex 1077, 1081, 1087, ...)."),
]

out = RUN / "findings_041_045.json"
out.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

bad = 0
for d in findings:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1 or "%%%%%%%%%%" in d["fix"]["old"]:
        bad += 1
        print("BAD", d["page"], n, repr(d["fix"]["old"]))
counts = {}
for d in findings:
    k = "misprint" if d["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(d["page"], {"normal": 0, "misprint": 0})[k] += 1
print("bad fixes:", bad)
print(counts)
print("total", len(findings))
