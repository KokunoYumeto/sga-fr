"""Write findings_116_120.json and check that every fix's old occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
PAGES = RUN / "b116_120"
OUT = RUN / "findings_116_120.json"


def F(page, where, scan, tex, kind, confidence, old=None, new=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- p. 116 ----------------
    F(116, "lines 1-2, end of Corollaire 3.5 b): 'En particulier, pour que F soit pseudo-cohérent, ... pour tout n.'",
      "underlined by word groups: 'En particulier', 'pour que', 'soit pseudo-cohérent', 'il faut et il suffit que', "
      "'soit cohérent pour tout' (both scans)",
      "no emphasis: the sentence is in roman",
      "underline", "high",
      r"En" "\n" r"particulier, pour que \(F\) soit pseudo-cohérent, il faut et il suffit que \(\Ho^n(F)\) soit cohérent pour tout \(n\).",
      r"\emph{En" "\n" r"particulier, pour que \(F\) soit pseudo-cohérent, il faut et il suffit que \(\Ho^n(F)\) soit cohérent pour tout \(n\).}",
      "End of the statement 3.5 b) begun on p. 115; block \\emph as the file's other statements (Corollaire 3.7.2, Lemme 4.1)."),
    F(116, "Proposition 3.7 a), statement before the display",
      "underlined: 'Soit', 'un morphisme de topos annelés.', 'On suppose', 'plat à droite', 'que le foncteur', "
      "'est exact.', 'Il existe', 'pour', 'une flèche canonique', 'fonctorielle' (both scans)",
      "no emphasis: the statement is in roman",
      "underline", "high",
      r"Soit \(f:(S',A')\to(S,A)\) un morphisme de topos annelés. On suppose \(f\) plat à droite, i.e. que le foncteur \(f^*=A'\otimes_A\cdot\) est exact. Il existe, pour \(F\in\Ob\Dpx(_A S)\), \(G\in\Ob\Dpx^+(_A S)\), une flèche canonique fonctorielle :",
      r"\emph{Soit \(f:(S',A')\to(S,A)\) un morphisme de topos annelés. On suppose \(f\) plat à droite, i.e. que le foncteur \(f^*=A'\otimes_A\cdot\) est exact. Il existe, pour \(F\in\Ob\Dpx(_A S)\), \(G\in\Ob\Dpx^+(_A S)\), une flèche canonique fonctorielle :}",
      "The statement goes on after the display on p. 117 ('Celle-ci est un isomorphisme ...', entry there)."),
    F(116, "Proposition 3.7 a), display 'f* RHom(F,G) --> RHom(f*(F), f*(G))'",
      "both terms ℝ Hom̲: double-struck R (doubled stem) and Hom underlined (sheaf Hom) (both scans; "
      "crops_116_120/p116_display.png)",
      r"\RHom twice (= \mathrm R\!\operatorname{Hom}: plain R, Hom not underlined)",
      "font", "high",
      r"f^*\RHom(F,G)\longrightarrow\RHom(f^*(F),f^*(G)).",
      r"f^*\mathbb{R}\underline{\Hom}(F,G)\longrightarrow\mathbb{R}\underline{\Hom}(f^*(F),f^*(G)).",
      "The same edit underlines Hom as printed. \\mathbb{R} as already applied on p. 83 (\\mathbb{R}f_*); "
      "\\underline{\\Hom} is the file's form (p. 121). See the message."),
    F(116, "Exemples 3.6, the three list items",
      "each item begins with a typed hyphen '-' (both scans)",
      r"\begin{itemize}[label=--] (en dash)",
      "punctuation", "low",
      r"\begin{itemize}[label=--]",
      r"\begin{itemize}[label=-]",
      "The typewriter has only the hyphen key; the TeX's label adds an en dash (the only label=-- of main.tex)."),
    F(116, "pp. 116-120 throughout: the site / topos S",
      "S underlined (S̲) where it names the site or topos, plain where it names an object or a scheme: p. 116 "
      "'(S̲,A) un topos annelé', 'les S̲-catégories', 'S̲ est le topos des faisceaux d'ensembles ... sur un schéma "
      "localement noethérien S', '(S̲',A') → (S̲,A)'; p. 118 '(S̲,A)', 'un point de S̲', 'de S̲ tel que'; p. 119 "
      "'S̲ désigne un site, S un objet de S̲, C̲ une S̲-catégorie'; p. 120 'fibrée sur S̲/S' (both scans)",
      r"plain S for both: p. 116 '\(S\) est le topos ... localement noethérien \(S\)'; p. 118 '\(s\) un point de "
      r"\(S\)'; p. 119 '\(S\) désigne un site, \(S\) un objet de \(S\)'",
      "underline", "high", None, None,
      "Convention of the transcription, as reported for pp. 84-100: one decision for the exposé, not a page fix."),
    # ---------------- p. 117 ----------------
    F(117, "line 1, end of Proposition 3.7 a): 'Celle-ci est un isomorphisme lorsque F est pseudo-cohérent.'",
      "underlined: 'Celle-ci', 'est un isomorphisme lorsque', 'est pseudo-cohérent' (both scans)",
      "no emphasis",
      "underline", "high",
      r"Celle-ci est un isomorphisme lorsque \(F\) est pseudo-cohérent.",
      r"\emph{Celle-ci est un isomorphisme lorsque \(F\) est pseudo-cohérent.}",
      "End of the statement 3.7 a) (p. 116 entry)."),
    F(117, "Proposition 3.7 b), statement: opening of the emphasis",
      "underlined by word groups from 'Supposons' to 'il en est de même de' (both scans)",
      "no emphasis: the statement is in roman",
      "underline", "high",
      r"\textbf{b)} Supposons",
      r"\textbf{b)} \emph{Supposons",
      "Opens the block; the next entry closes it: apply both or neither. Independent of the H and Ext entries below "
      "(disjoint texts)."),
    F(117, "Proposition 3.7 b), statement: close of the emphasis",
      "the statement ends 'de Ext^i(F,G).' (both scans)",
      "no emphasis",
      "underline", "high",
      r"(F,G)\)." "\n\n" r"\emph{Preuve.}",
      r"(F,G)\).}" "\n\n" r"\emph{Preuve.}",
      "Closes the block opened by the previous entry: apply both or neither."),
    F(117, "Proposition 3.7 b), 'Si H^i(F) et H^i(G) sont cohérents'",
      "each H has a short underline of its own (H̲^i(F), H̲^i(G)), apart from the statement's underline: 'Si' and "
      "'sont cohérents' are underlined, 'et' and the letters F, G, i are not (both scans; crops_116_120/p117_b_stmt.png)",
      r"\(\Ho^i(F)\) et \(\Ho^i(G)\) (plain H)",
      "underline", "high",
      r"Si \(\Ho^i(F)\) et \(\Ho^i(G)\) sont",
      r"Si \(\underline{\Ho}^i(F)\) et \(\underline{\Ho}^i(G)\) sont",
      "Notation underline (cohomology sheaves; the statement is about coherent sheaves); the statement's word-group "
      "underlining skips formulas. The proof's H^i(G) = 0 (same page) is printed without underline."),
    F(117, "Proposition 3.7 b), 'il en est de même de Ext^i(F,G)'",
      "Ext underlined (Ext̲^i, the sheaf Ext), (F,G). not underlined (both scans)",
      r"\(\Ext^i(F,G)\) (plain Ext)",
      "underline", "high",
      r"\(\Ext^i",
      r"\(\underline{\Ext}^i",
      "As \\underline{\\Hom} and \\underline{\\Tor} of the file."),
    F(117, "Preuve of 3.7 a), display 'f* Hom(F,G) --> Hom(f*F,f*G) --> RHom(f*F,f*G)'",
      "f* Hom̲(F,G) → Hom̲(f*F,f*G) → ℝ Hom̲(f*F,f*G) . : all three Hom underlined, R double-struck (both scans)",
      r"f^*\Hom(F,G)\longrightarrow\Hom(f^*F,f^*G)\longrightarrow\RHom(f^*F,f^*G). (plain Hom, plain R)",
      "underline", "high",
      r"f^*\Hom(F,G)\longrightarrow\Hom(f^*F,f^*G)\longrightarrow\RHom(f^*F,f^*G).",
      r"f^*\underline{\Hom}(F,G)\longrightarrow\underline{\Hom}(f^*F,f^*G)\longrightarrow\mathbb{R}\underline{\Hom}(f^*F,f^*G).",
      "The same edit sets the double-struck R of the third term (as p. 116)."),
    F(117, "Preuve of 3.7 a), 'le foncteur f* RHom(.,G)'",
      "f* ℝ Hom̲(.,G): double-struck R, Hom underlined (both scans; crops_116_120/p117_dots_zoom.png, w117_dots.png)",
      r"\(f^*\RHom(\cdot,G)\)",
      "font", "high",
      r"\(f^*\RHom(",
      r"\(f^*\mathbb{R}\underline{\Hom}(",
      "Also underlines Hom. Independent of the low-confidence dot entry below (disjoint texts)."),
    F(117, "Preuve of 3.7 a), '(resp. RHom(f*.,f*G))'",
      "ℝ Hom̲(f*.,f*G): double-struck R, Hom underlined (both scans)",
      r"\(\RHom(f^*\cdot,f^*G)\)",
      "font", "high",
      r"(resp. \(\RHom(",
      r"(resp. \(\mathbb{R}\underline{\Hom}(",
      "Also underlines Hom. Independent of the dot entry below."),
    F(117, "Preuve of 3.7 a), the place-holder in 'RHom(.,G)'",
      "a typed full stop on the baseline, at the height of the stop of 'resp.' (both scans); the dot of "
      "'A' ⊗_A .' on p. 116 is raised, this one is not",
      r"(\cdot,G)",
      "symbol", "low",
      r"\cdot,G)",
      r".,G)",
      "\\cdot raises the typed stop to mid-height (as the p. 89 entry for Hom(P,.))."),
    F(117, "Preuve of 3.7 a), the place-holder in 'RHom(f*.,f*G)'",
      "a typed full stop on the baseline after f* (both scans)",
      r"f^*\cdot,f^*G",
      "symbol", "low",
      r"f^*\cdot,",
      r"f^*.,",
      "As the previous entry."),
    # ---------------- p. 118 ----------------
    F(118, "Remarque 3.7.1, 'de RHom avec Lf*'",
      "ℝ Hom̲: double-struck R, Hom underlined (both scans; crops_116_120/p118_rem371.png)",
      r"\(\RHom\) (plain R, Hom not underlined)",
      "font", "high",
      r"\(\RHom\) avec",
      r"\(\mathbb{R}\underline{\Hom}\) avec",
      "Also underlines Hom (as pp. 116-117)."),
    F(118, "Remarque 3.7.1, 'avec Lf*'",
      "double-struck L (doubled stem), 𝕃f* (both scans)",
      r"\(\mathrm Lf^*\) (plain L)",
      "font", "high",
      r"\(\mathrm Lf^*\)",
      r"\(\mathbb{L}f^*\)",
      "The print's derived-functor L is double-struck here, like its R."),
    F(118, "Corollaire 3.7.2, 'Si E_s ≃ F_s'",
      "≃: a tilde over a straight line, no arrowhead (both scans; crops_116_120/p118_Es_Fs.png, w118_Es_Fs.png), "
      "while the arrows ⥲ of the display below and of p. 117 have heads",
      r"\(E_s\qis F_s\) (\qis = \xrightarrow{\sim}, an arrow)",
      "symbol", "high",
      r"\(E_s\qis F_s\)",
      r"\(E_s\simeq F_s\)",
      ""),
    F(118, "Corollaire 3.7.2, 'tel que E|U ≃ F|U'",
      "≃ without arrowhead (both scans; crops_116_120/p118_EU_FU.png, w118_EU_FU.png)",
      r"\(E|U\qis F|U\)",
      "symbol", "high",
      r"\(E|U\qis F|U\)",
      r"\(E|U\simeq F|U\)",
      ""),
    F(118, "Preuve of 3.7.2, display 'Hom(E,F)_s ⥲ Hom(E_s,F_s)  (resp. Hom(F,E)_s ⥲ Hom(F_s,E_s))'",
      "Hom̲(E,F)_s and Hom̲(F,E)_s underlined (sheaf Hom, stalk at s); Hom(E_s,F_s) and Hom(F_s,E_s) not underlined "
      "(both scans)",
      r"\Hom four times, none underlined",
      "underline", "high",
      r"\Hom(E,F)_s\qis\Hom(E_s,F_s)" "\n" r"  \qquad" "\n" r"  (\text{resp. }\Hom(F,E)_s",
      r"\underline{\Hom}(E,F)_s\qis\Hom(E_s,F_s)" "\n" r"  \qquad" "\n" r"  (\text{resp. }\underline{\Hom}(F,E)_s",
      ""),
    F(118, "Preuve of 3.7.2, 'une section u (resp. v) de Hom(E,F) (resp. Hom(F,E))'",
      "Hom̲(E,F) and Hom̲(F,E) underlined (both scans)",
      r"\(\Hom(E,F)\) (resp. \(\Hom(F,E)\))",
      "underline", "high",
      r"de \(\Hom(E,F)\) (resp. \(\Hom(F,E)\))",
      r"de \(\underline{\Hom}(E,F)\) (resp. \(\underline{\Hom}(F,E)\))",
      ""),
    F(118, "Preuve of 3.7.2, 'D'après (2.22 a)), on a'",
      "(2.22 a)) (both scans)",
      r"(2.22 a)) (printed reading kept)",
      "misprint_in_print", "medium", None, None,
      "Exposé I has no 2.22: § 2 ends with Exercice 2.16.2, § 3 begins at 3.0. The isomorphism Hom̲(E,F)_s ⥲ "
      "Hom(E_s,F_s) for E pseudo-coherent (D(_A S)_coh, 2.15) is Proposition 3.7 a) applied to the point s "
      "(an exact s^*), taking H^0. The TeX keeps the printed reading (both layers).",
      corrected=r"(3.7 a))"),
    # ---------------- p. 119 ----------------
    F(119, "Corollaire 4.2, 'Soit' before the diagram",
      "'Soit' underlined (both scans); the statement goes on, underlined, on p. 120",
      r"\textbf{Corollaire 4.2.} Soit (roman)",
      "underline", "high",
      r"\textbf{Corollaire 4.2.} Soit",
      r"\textbf{Corollaire 4.2.} \emph{Soit}",
      "Opening word of the statement continued on p. 120 (entries there)."),
    F(119, "label of Lemme 4.1 with its footnote call",
      "'Lemme 4.1 (*).': the footnote call stands before the full stop (both scans)",
      r"\textbf{Lemme 4.1.}\footnote{...}: the stop before the call",
      "punctuation", "low",
      r"4.1.}\footnote{Ce lemme a été communiqué au rédacteur par D. Ferrand.}",
      r"4.1}\footnote{Ce lemme a été communiqué au rédacteur par D. Ferrand.}.",
      "Order of call and stop only; the bold label itself is accepted."),
    # ---------------- p. 120 ----------------
    F(120, "Corollaire 4.2, statement before the diagram: opening of the emphasis",
      "underlined by word groups: 'un diagramme de', 'où', 'est strictement', '-parfait et', 'un quasi-isomorphisme.', "
      "'L'ensemble des', 'au-dessus de', 'tels qu'il existe une flèche', 'telle que le diagramme' (both scans)",
      "no emphasis",
      "underline", "high",
      r"un" "\n" r"diagramme",
      r"\emph{un" "\n" r"diagramme",
      "Opens the block; the next entry closes it before the diagram: apply both or neither. Independent of the "
      "comma entry (disjoint texts)."),
    F(120, "Corollaire 4.2, statement before the diagram: close of the emphasis",
      "'telle que le diagramme' underlined (both scans)",
      "no emphasis",
      "underline", "high",
      r"le diagramme" "\n" r"\[",
      r"le diagramme}" "\n" r"\[",
      "Closes the block opened by the previous entry: apply both or neither."),
    F(120, "Corollaire 4.2, 'u : P_X → E_X de C(C_X) telle que le diagramme'",
      "no comma after C(C̲_X) (both scans; crops_116_120/p120_CX_comma.png)",
      r"de \(\Cpx(\mathcal C_X)\), telle que",
      "punctuation", "high",
      r"\(\Cpx(\mathcal C_X)\), telle",
      r"\(\Cpx(\mathcal C_X)\) telle",
      "The TeX adds a comma."),
    F(120, "Corollaire 4.2, the triangle P_X, E_X, F_X",
      "the diagonal arrow u goes from P_X down to E_X, its head at E_X (u : P_X → E_X, as the text says; both scans, "
      "crops_116_120/p120_diag.png)",
      'E_X \\arrow[ur,"u"]: an arrow from E_X to P_X',
      "formula", "high",
      r"\arrow[d,\"v_X\"]\\" "\n" r"E_X \arrow[r,\"f_X\"] \arrow[ur,\"u\"] & F_X".replace('\\"', '"'),
      r"\arrow[d,\"v_X\"] \arrow[dl,\"u\"']\\" "\n" r"E_X \arrow[r,\"f_X\"] & F_X".replace('\\"', '"'),
      "The TeX reverses the arrow u."),
    F(120, "Corollaire 4.2, statement after the diagram",
      "underlined: 'soit commutatif dans', 'est un raffinement de' (both scans)",
      "no emphasis",
      "underline", "high",
      r"soit commutatif dans \(\Kpx(\mathcal C_X)\) est un raffinement de \(S\).",
      r"\emph{soit commutatif dans \(\Kpx(\mathcal C_X)\) est un raffinement de \(S\).}",
      "End of the statement (Corollaire 4.3 on the same page has its \\emph)."),
    F(120, "Scholie 4.4, 'une catégorie (Qis/F) fibrée sur S/S'",
      "Qis/F underlined inside the parentheses, (Q̲i̲s̲/̲F̲), the fibred category; the fibre (Qis/F_X)° on the next "
      "line is not underlined (both scans; crops_116_120/p120_qis_SS.png, w120_qis_SS.png)",
      r"\((\Qis/F)\) (no underline)",
      "underline", "high",
      r"\((\Qis/F)\) fibrée",
      r"\((\underline{\Qis/F})\) fibrée",
      "Notation underline, as S̲ and C̲ for fibred categories; p. 121 prints (Q̲i̲s̲/̲F̲) too (witness)."),
    F(120, "Scholie 4.4, 'fibrée sur S/S'",
      "S̲ with '/S' lowered as an index, S_{/S} (both scans)",
      r"\(S/S\)",
      "formula", "high",
      r"sur \(S/S\)",
      r"sur \(S_{/S}\)",
      "As the p. 90 fix (\\Ob S_{/S}). The underline of S̲ is the convention entry (p. 116)."),
    F(120, "end of page / start of p. 121",
      "p. 120 ends '... On peut alors exprimer (4.3) en disant que,'; p. 121 begins 'si F est strictement parfait, "
      "la flèche Id_F est localement cofinale dans (Qis/F).' (main scan p. 120; witness pp. 120-121, "
      "crops_116_120/w121_top.png)",
      r"page_120.tex ends 'en disant que, si \(F\) est' (under the folio-120 marker); page_121.tex begins "
      r"'strictement parfait'",
      "marker", "high", None, None,
      r"Page 121 really begins with 'si \(F\) est'. python -I move_marker.py 6 121 'si \(F\) est' --before "
      r"(single quotes; dry run and simulation on both layers: '... en disant que, ', the marker, 'si \(F\) est', "
      r"'strictement parfait, ...'; the anchor is unaffected by this file's p. 120 fixes)."),
]

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")

bad = 0
for f in findings:
    if f["fix"] is None:
        continue
    t = (PAGES / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(f["fix"]["old"])
    marker_cross = "%%%%%%%%%%" in f["fix"]["old"]
    if n != 1 or marker_cross:
        bad += 1
        print("BAD", f["page"], n, repr(f["fix"]["old"][:80]))
print("findings", len(findings), "bad", bad)
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in findings)
for p in range(116, 121):
    print(p, c[(p, False)], c[(p, True)])
