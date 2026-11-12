"""Write findings_176_180.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b176_180"


def F(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- p. 176
    F(176, "start of page (folio-176 marker)",
      "p. 175 ends '... dont l'image essentielle est'; p. 176 begins 'la sous-catégorie triangulée' (both scans)",
      "page_176.tex (extracted 19:59) begins 'sous-catégorie triangulée'; 'la' ended page_175.tex",
      "marker", "high", None,
      "Already reported by batch 171-175 (findings_171_175, p. 175 'end of the page') and already applied: in the "
      "current main.tex (both layers, 20:09) the folio-176 marker stands before 'la'. No action; do not run the move "
      "again (a second run would take an earlier 'la', in 'si l'on note $\\Mod(A)$ la catégorie', as simulated)."),
    F(176, "first diagram, right vertical arrow D^b(S)_coh -> D^b(A)_coh",
      "𝕉Γ_S: the derived-functor R double-struck (both scans)",
      r'\arrow[d,"R\Gamma_S"] (plain R)',
      "font", "high",
      {"old": r'\mathrm D^b(S)_{\coh} \arrow[d,"R\Gamma_S"]',
       "new": r'\mathrm D^b(S)_{\coh} \arrow[d,"\mathbb R\Gamma_S"]'},
      "Same form as the p. 175 entry of batch 171-175 ($\\mathbb R\\Gamma_S$, applied)."),
    F(176, "second diagram, right vertical arrow D(S)_parf -> D(A)_parf",
      "𝕉Γ_S: the derived-functor R double-struck (both scans)",
      r'\arrow[d,"R\Gamma_S"] (plain R)',
      "font", "high",
      {"old": r'\mathrm D(S)_{\parf} \arrow[d,"R\Gamma_S"]',
       "new": r'\mathrm D(S)_{\parf} \arrow[d,"\mathbb R\Gamma_S"]'},
      "As the first diagram."),
    F(176, "Remarque 2.2.10 b)",
      "un complexe de O_S-Modules pseudo-cohérent et à cohomologique bornée",
      "pseudo-cohérent et à cohomologique bornée",
      "misprint_in_print", "high", None,
      "Typing error of the print (both scans); the diplomatic TeX keeps the printed reading, the current layer "
      "already reads 'à cohomologie bornée'.",
      corrected="à cohomologie bornée"),
    F(176, "2.3.1, first line",
      "Rappelons quelques définitions et résultats de [T.F]. Soit X",
      "résultats de [T.F.]. Soit $X$",
      "punctuation", "high",
      {"old": "[T.F.]", "new": "[T.F]"},
      "No stop after F inside the hand-drawn brackets (both scans); the stop follows the bracket. The TeX keeps the "
      "print's dotless 'T.F II 3.7.1' on p. 177."),
    # ---------------- p. 177
    F(177, "start of page (folio-177 marker)",
      "p. 176 ends '... I = H^o(X,F) est un épimorphisme.'; p. 177 begins 'D'autre part, si A est mou' (both scans)",
      "page_176.tex ends 'est un épimorphisme. D'%'; page_177.tex begins 'autre part, si $A$ est mou'",
      "marker", "high", None,
      "Page 177 really begins with 'D'autre part'. Move the folio-177 marker above 'D'%': "
      "python -I move_marker.py 6 177 \"D'%\" --before (simulated in memory on both layers with "
      "crops_176_180/sim_markers.py: '... est un épimorphisme. ' / the marker / 'D'%' / 'autre part, si $A$ est mou "
      "...', which still renders 'D'autre part'). Not marker_split_word.py pull \"D'%\": it would set the % before "
      "'autre part' and comment out the line."),
    F(177, "pp. 177-180, the statements of Proposition 2.3.2, Définition 2.4.1 and Lemme 2.4.3",
      "statements underlined by word groups: p. 177 'Soit S un espace compact, muni d'un faisceau d'anneaux mou A. "
      "On note Mod(S) la catégorie des A-Modules à gauche' (Soit / un espace compact / muni d'un faisceau d'anneaux / "
      "mou / On note / la catégorie des / Modules à gauche); p. 178 'les notions de pseudo-cohérence (resp. "
      "perfection) dans D(A(S)) étant entendues ...' (end of 2.3.2 d)); p. 180 'Posons A = Γ(S,O_S), et notons "
      "Mod(A) la catégorie des A-modules, D(A) la catégorie dérivée correspondante' (Lemme 2.4.3 c))",
      "all in roman: Exposé II §§ 1-3 of main.tex contain no \\underline, and \\emph only for 'Preuve' and a few "
      "terms (mou, famille ample, divisoriel, Stein, théorème A/B, espace pseudo-analytique complexe)",
      "underline", "high", None,
      "Convention of the transcription for Exposé II, not page fixes; the same convention as batch 171-175's p. 171 "
      "entry (one decision, not itemized): the print underlines every statement word group by word group (here Prop. "
      "2.3.2, Déf. 2.4.1, Lemme 2.4.3; also Prop. 1.1 c) on p. 160, seen on the scan), the TeX never does. Decide: "
      "restore \\emph on the underlined word groups (as the Exposé I statements) or accept roman statements. The "
      "p. 178 entries (\\emph{Stein}, \\emph{théorème A}, \\emph{théorème B}) are where the TeX's own emphasis "
      "contradicts the print; apply them with this decision, with \\emph{famille ample} and \\emph{divisoriel} of "
      "p. 171 (same inversion)."),
    F(177, "Proposition 2.3.2 c), first reference",
      "Pour que E soit d'amplitude parfaite contenue dans [m,n] (4.8) il faut et il suffit",
      "contenue dans $[m,n]$ (4.8) il faut",
      "misprint_in_print", "medium", None,
      "Wrong reference: Exposé II has no 4.8; perfect amplitude is Exemple I 4.8, cited '(I 4.8)' in the parallel "
      "2.2.9 b) (p. 175) and on p. 182. The TeX keeps the printed reading ('(4.8)' is unique on the page).",
      corrected="(I 4.8)"),
    F(177, "Proposition 2.3.2 c), second reference",
      "est pleinement fidèle et a pour image essentielle D(S)_parf (4.9).",
      r"$\mathrm D(S)_{\parf}$ (4.9).",
      "misprint_in_print", "medium", None,
      "Wrong reference: D_parf is Notation I 4.9, cited '(I 4.9)' in the parallel 2.2.9 b) (p. 175). The TeX keeps "
      "the printed reading ('(4.9)' is unique on the page).",
      corrected="(I 4.9)"),
    # ---------------- p. 178
    F(178, "start of page (folio-178 marker)",
      "p. 177 ends 'En outre, il définit des'; p. 178 begins 'équivalences de catégories :' (both scans)",
      "page_178.tex begins 'définit des équivalences de catégories :'",
      "marker", "high", None,
      "'définit des' is printed on p. 177; the marker stands two words too early. Move it down: "
      "python -I move_marker.py 6 178 'équivalences de catégories :' (no --before; simulated in memory on both "
      "layers: '... En outre, il' / 'définit des ' / the marker / 'équivalences de catégories :' / '\\[')."),
    F(178, "Proposition 2.3.2 d), after the display",
      "étant entendues relativement à la catégories des modules libres (resp. projectifs) de type fini",
      "relativement à la catégories des modules libres",
      "misprint_in_print", "high", None,
      "Typing error of the print (both scans), kept by the TeX (both layers).",
      corrected="à la catégorie des modules libres"),
    F(178, "Preuve of 2.3.2, last sentence",
      "transforme Modules libres (resp.) facteurs directs de libres) de type fini",
      "transforme Modules libres (resp.) facteurs directs de libres)",
      "misprint_in_print", "high", None,
      "Stray closing parenthesis after 'resp.' in the print (both scans), kept by the TeX (both layers).",
      corrected="Modules libres (resp. facteurs directs de libres) de type fini"),
    F(178, "Définition 2.4.1, 'On dit que S est de Stein si'",
      "'On dit que', 'S', 'est' and 'si le faisceau structural' underlined; 'de Stein' plain (the defined term left "
      "out of the underline)",
      r"On dit que $S$ est de \emph{Stein} si",
      "underline", "high",
      {"old": r"\emph{Stein}", "new": "Stein"},
      "The TeX sets the statement in roman and emphasizes 'Stein', the one word the print leaves plain (the inverse "
      "of the print, as \\emph{famille ample} and \\emph{divisoriel} on p. 171, which batch 171-175 left to the "
      "statement decision). The print has no underline on 'Stein' under either decision: apply with the decision "
      "(p. 177 entry)."),
    F(178, "Définition 2.4.1, 'théorème A'",
      "\"théorème A\" : only 'théorème' underlined, the letter A plain (both scans)",
      r"«~\emph{théorème A}~»",
      "underline", "high",
      {"old": r"\emph{théorème A}", "new": r"\emph{théorème} A"},
      "The underline stops before A; 'théorème' is underlined as one of the statement's word groups. The fix follows "
      "the print; if the Exposé II statements stay roman (p. 177 entry), 'théorème A' becomes plain instead."),
    F(178, "Définition 2.4.1, 'théorème B'",
      "\"théorème B\" : only 'théorème' underlined, the letter B plain (both scans)",
      r"«~\emph{théorème B}~»",
      "underline", "high",
      {"old": r"\emph{théorème B}", "new": r"\emph{théorème} B"},
      "As 'théorème A'."),
    # ---------------- p. 179
    F(179, "Remarque 2.4.1.1, 'Comme on a H^o(S,F/m_sF) ≃ F_s/m_sF_s'",
      "F_s/m_sF_s with a plain typed m (no underline, both scans), against the underlined m̲_s of F/m̲_sF before it",
      r"F_s/\mathfrak m_sF_s",
      "font", "high",
      {"old": r"F_s/\mathfrak m_sF_s", "new": r"F_s/m_sF_s"},
      "The print keeps the maximal ideal m_s of O_{S,s} plain and underlines only the Ideal m̲_s of S; the TeX "
      "writes \\mathfrak m for both."),
    F(179, "Remarque 2.4.1.1, 'où m_s est l'idéal maximal de O_{S,s}'",
      "où m_s est l'idéal maximal (plain m, both scans)",
      r"où $\mathfrak m_s$ est l'idéal maximal",
      "font", "high",
      {"old": r"où $\mathfrak m_s$ est", "new": r"où $m_s$ est"},
      "As F_s/m_sF_s."),
    F(179, "footnote (2)",
      "l'idéal maximal m_s de O_{S,s} (plain m, both scans)",
      r"l'idéal maximal $\mathfrak m_s$ de",
      "font", "high",
      {"old": r"maximal $\mathfrak m_s$ de", "new": r"maximal $m_s$ de"},
      "As F_s/m_sF_s."),
    F(179, "Remarque 2.4.1.1, the Ideal m̲_s (6 places: l'Idéal m̲_s, the display twice, où F/m̲_sF, H^o(S,F/m̲_sF) twice)",
      "m̲_s: typed m underlined (both scans)",
      r"\mathfrak m_s",
      "font", "low", None,
      "The typescript marks the Ideal (a sheaf) by the underline, as O̲_S. main.tex writes \\mathfrak m 32 times and "
      "never \\underline{m}: decide with the pending O̲ decision (\\cO or \\underline O); with \\underline O these "
      "six become \\underline{m}_s. No page fix meanwhile."),
    F(179, "Remarque 2.4.1.1, before 'Le rédacteur ignore si'",
      "new indented paragraph 'Le rédacteur ignore si l'implication précédente ...' (both scans)",
      "runs on: 'on conclut par Nakayama. Le rédacteur ignore si'",
      "other", "high",
      {"old": "par Nakayama. Le rédacteur", "new": "par Nakayama.\n\nLe rédacteur"},
      "Missing paragraph break (the typescript indents its new paragraphs)."),
    F(179, "Remarque 2.4.1.1, before 'Le rédacteur ignore également'",
      "new indented paragraph 'Le rédacteur ignore également si la relation ...' (both scans)",
      "runs on: 'd'anneaux locaux). Le rédacteur ignore également'",
      "other", "high",
      {"old": "anneaux locaux). Le rédacteur", "new": "anneaux locaux).\n\nLe rédacteur"},
      "Missing paragraph break."),
    # ---------------- p. 180
    F(180, "start of page (folio-180 marker)",
      "p. 179 ends 'sont des équivalences de catégories.' and its footnotes; p. 180 begins 'c) Posons A = Γ(S,O_S)'",
      "the '\\item' that prints c) is the last line of page_179.tex; page_180.tex begins 'Posons'",
      "marker", "high", None,
      "Page 180 really begins with the item label c). Move the marker above the \\item: "
      "python -I move_marker.py 6 180 '\\item' --before (simulated in memory on both layers: '... sont des "
      "équivalences de catégories.' / the marker / '\\item' / 'Posons $A=\\Gamma(S,\\mathcal O_S)$ ...'). A label at "
      "the top of a page, which the 10 Nov script did not move."),
    F(180, "Preuve of 2.4.3, 'alors Hom(G,E) est cohérent'",
      "Hom̲(G,E): Hom underlined (both scans)",
      r"$\operatorname{Hom}(G,E)$",
      "underline", "high",
      {"old": r"\operatorname{Hom}(G,E)", "new": r"\underline{\operatorname{Hom}}(G,E)"},
      "Sheaf Hom underlined in the print, plain in the TeX."),
    F(180, "end of page (marker of p. 181)",
      "p. 180 ends with the display 'K^-(Lib(S)) -(*)-> K^-(Lib(A)) -(**)-> D(A) ,' and footnote (1); p. 181 begins "
      "'où Lib(A) désigne la catégorie des A-modules libres' (both scans)",
      "page_180.tex ends with the line 'où $\\Lib(A)$', above the folio-181 marker",
      "marker", "high", None,
      "Page 181 really begins with 'où Lib(A)'. Move the folio-181 marker above it: "
      "python -I move_marker.py 6 181 'où $\\Lib(A)$' --before (single quotes; simulated in memory on both layers: "
      "'\\]' / the marker / 'où $\\Lib(A)$' / 'désigne la catégorie ...'). Apply once: the checker of p. 181 may "
      "report the same break."),
]

out = RUN / "findings_176_180.json"
out.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

ok = True
for x in findings:
    if x["fix"]:
        t = (B / f"page_{x['page']}.tex").read_text(encoding="utf-8")
        n = t.count(x["fix"]["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", x["page"], n, repr(x["fix"]["old"]))
        if "%%%%%%%%%%" in x["fix"]["old"]:
            ok = False
            print("CROSSES MARKER", x["page"])
counts = {}
for x in findings:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("all old strings unique" if ok else "PROBLEMS", counts, len(findings))
json.loads(out.read_text(encoding="utf-8"))
