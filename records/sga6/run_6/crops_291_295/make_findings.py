"""Build findings_291_295.json and check that every fix's old string occurs exactly once in its page file."""
import io
import json
import pathlib
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
BATCH = RUN / "b291_295"
OUT = RUN / "findings_291_295.json"

M291 = "%%%%%%%%%%  scan idx 304  |  folio 291  %%%%%%%%%%"
M296 = "%%%%%%%%%%  scan idx 309  |  folio 296  %%%%%%%%%%"
TENSOR_L = ("The typescript types the L over the tensor sign with the ordinary typewriter L (both scans); the TeX "
            "writes \\mathbf L. Exposé III's derived-tensor L was set to \\mathrm L globally; Exposé IV still has "
            "\\mathbf L.")
LIM_INDEX = "No index under 'lim' in either scan (the i is X_i's); the TeX adds the summation index _i."


def F(page, where, scan, tex, kind, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


findings = [
    # ---------------- page 291
    F(291, "first line of the page / folio-291 marker",
      "est donc définie, reste à montrer que c'est un isomorphisme.",
      "the marker follows '... La flèche de changement de base est'; the page's TeX starts 'donc définie'",
      "marker", "high", None,
      "Page 291 really begins with 'est' (both scans). In both layers of main.tex replace 'La flèche de changement de "
      "base est\\n" + M291 + "\\ndonc définie' by 'La flèche de changement de base\\n" + M291 + "\\nest donc "
      "définie' (once in each layer). Equivalent: python -I move_marker.py 6 291 \"est\" --before (simulated on both "
      "layers: '... de changement de base ' / marker / 'est' / 'donc définie, ...')."),
    F(291, "display after 'qui s'écrit'", "B ⊗^L_A A' ~⟶ B' , (typed L over the tensor sign)",
      "B\\otimes_A^{\\mathbf L}A'", "font", "high",
      fx("B\\otimes_A^{\\mathbf L}A'", "B\\otimes_A^{\\mathrm L}A'"), TENSOR_L),
    F(291, "display after 'dans D(A')'", "E ⊗^L_A A' ~⟶ E ⊗^L_B B' , (two typed L)",
      "E\\otimes_A^{\\mathbf L}A'\\xrightarrow{\\sim}E\\otimes_B^{\\mathbf L}B'", "font", "high",
      fx("E\\otimes_A^{\\mathbf L}A'\\xrightarrow{\\sim}E\\otimes_B^{\\mathbf L}B'",
         "E\\otimes_A^{\\mathrm L}A'\\xrightarrow{\\sim}E\\otimes_B^{\\mathrm L}B'"),
      "Two \\mathbf L in one display. " + TENSOR_L),
    # ---------------- page 292
    F(292, "heading 3.2", "3.2. Passage à la limite sur K˙_naïf et K (no full stop after the title)",
      "\\textbf{3.2. Passage à la limite sur \\(K'_{\\naif}\\) et \\(K_{\\bullet}\\).}", "punctuation", "medium",
      fx("\\).} Soit", "\\)} Soit"),
      "The TeX adds a full stop after the title (both scans end the heading with 'K'). Independent of the misprint "
      "entry for the same K below (disjoint edits)."),
    F(292, "heading 3.2, last symbol", "et K (the K of K. without its dot, both scans)",
      "et \\(K_{\\bullet}\\)", "misprint_in_print", "medium",
      fx("et \\(K_{\\bullet}", "et \\(K"),
      "The heading names the two groups K˙_naïf and K.; the typist left out the dot of K. (no trace in either scan; "
      "the K. of the statement on the same page has it). The TeX silently corrects to K_{\\bullet}; the diplomatic "
      "reading is a plain K.",
      corrected="et \\(K_{\\bullet}"),
    F(292, "3.2, 'Posons X = lim X_i'", "X = lim← X_i (no index under lim)", "X=\\varprojlim_i X_i", "extra",
      "high", fx("X=\\varprojlim_i X_i", "X=\\varprojlim X_i"), LIM_INDEX),
    F(292, "display (3.2.1.1)", "lim→ K˙(X_i)_naïf ⟶ K˙(X)_naïf . (no index under lim)",
      "\\varinjlim_i K'(X_i)_{\\naif}\\longrightarrow K'(X)_{\\naif}.", "extra", "high",
      fx("\\varinjlim_i K'(X_i)_{\\naif}\\longrightarrow K'(X)_{\\naif}.",
         "\\varinjlim K'(X_i)_{\\naif}\\longrightarrow K'(X)_{\\naif}."), LIM_INDEX),
    F(292, "3.2.1, after the display", "Je dis que l'homomorphisme (3.2.1.1) est un isomorphisme. "
      "('l'homomorphisme' and 'est un isomorphisme' underlined)",
      "Je dis que l'homomorphisme (3.2.1.1) est un isomorphisme.", "underline", "high",
      fx("Je dis que l'homomorphisme (3.2.1.1) est un isomorphisme.",
         "Je dis que \\emph{l'homomorphisme} (3.2.1.1) \\emph{est un isomorphisme}."),
      "Emphasis in running text, not a statement; Exposé IV writes the underline with \\emph (both scans)."),
    F(292, "3.2.1, 'tel que l'on ait E ≃ f_i*(E_i)'",
      "fini E_i tel que l'on ait E ≃ f_i*(E_i). En vertu de ... (inline, in the running text)",
      "displayed: \\[ E\\simeq f_i^*(E_i). \\]", "other", "medium",
      fx("tel que l'on ait\n\\[\n E\\simeq f_i^*(E_i).\n\\]\nEn vertu de",
         "tel que l'on ait \\(E\\simeq f_i^*(E_i)\\). En vertu de"),
      "The print sets the formula inline; the TeX makes it a display (same kind of fix as SGA 6 pp. 21, 34, 42)."),
    F(292, "3.2.1, 'l'image de cl(E_i) dans lim ...'", "dans lim→ K˙(X_i)_naïf ne dépend (no index under lim)",
      "dans \\(\\varinjlim_i K'(X_i)_{\\naif}\\) ne dépend", "extra", "high",
      fx("dans \\(\\varinjlim_i K'(X_i)_{\\naif}\\) ne dépend", "dans \\(\\varinjlim K'(X_i)_{\\naif}\\) ne dépend"),
      LIM_INDEX),
    F(292, "3.2.1, last line 'u : ob Loclib(X) ⟶ lim ...'", "lim K˙(X_i)_naïf (no index)",
      "\\varinjlim_i K'(X_i)_{\\naif}\\) ainsi", "extra", "high",
      fx("_i K'(X_i)_{\\naif}\\) ainsi", " K'(X_i)_{\\naif}\\) ainsi"),
      LIM_INDEX + " Disjoint from the misprint entry that follows (the missing arrow under the same lim)."),
    F(292, "3.2.1, last line 'u : ob Loclib(X) ⟶ lim ...'",
      "u : ob Loclib(X) ⟶ lim K˙(X_i)_naïf : plain 'lim', no arrow under it (both scans)",
      "\\(u:\\Ob\\Loclib(X)\\longrightarrow \\varinjlim_i K'(X_i)_{\\naif}\\)", "misprint_in_print", "medium",
      fx("\\longrightarrow \\varinjlim", "\\longrightarrow \\lim"),
      "Every other lim of 3.2 has its hand-drawn arrow; this one was left without it (the same inductive limit "
      "as in (3.2.1.1)). The TeX silently corrects to \\varinjlim. Apply after or before the index entry above: the "
      "two old strings do not overlap.",
      corrected="\\longrightarrow \\varinjlim"),
    # ---------------- page 293
    F(293, "first line", "K˙(X)_naïf ⟶ lim→ K˙(X_i)_naïf , dont on (no index under lim)",
      "\\longrightarrow \\varinjlim_i K'(X_i)_{\\naif}\\), dont", "extra", "high",
      fx("\\longrightarrow \\varinjlim_i K'(X_i)_{\\naif}\\), dont",
         "\\longrightarrow \\varinjlim K'(X_i)_{\\naif}\\), dont"), LIM_INDEX),
    F(293, "display (3.2.2.1) in 3.2.2", "lim→ K˙(X_i) ⟶ K˙(X) . (no index under lim)",
      "\\varinjlim_i K'(X_i)\\longrightarrow K'(X).", "extra", "high",
      fx("\\varinjlim_i K'(X_i)\\longrightarrow K'(X).", "\\varinjlim K'(X_i)\\longrightarrow K'(X)."), LIM_INDEX),
    F(293, "3.2.2, 'la catégorie Lim des catégories analogues'",
      "Lim with a capital L, arrow → under it (both scans)", "\\(\\varinjlim\\)", "symbol", "high",
      fx("catégorie \\(\\varinjlim\\) des", "catégorie \\(\\mathop{\\underrightarrow{\\mathrm{Lim}}}\\) des"),
      "The 2-limit of categories is typed 'Lim' (capital), unlike the group limits 'lim'. The form "
      "\\mathop{\\underrightarrow{\\mathrm{Lim}}} is the one main.tex already uses (Exposé II)."),
    F(293, "3.2.3, first line", "X_i et X noethériens,et les morphismes f_ij plats ('noethériens' and 'plats' "
      "underlined)", "\\(X\\) noethériens, et les morphismes \\(f_{ij}\\) plats", "underline", "high",
      fx("\\(X\\) noethériens, et les morphismes \\(f_{ij}\\) plats",
         "\\(X\\) \\emph{noethériens}, et les morphismes \\(f_{ij}\\) \\emph{plats}"),
      "Underlined hypotheses in a numbered paragraph (both scans); \\emph is the file's command in Exposé IV."),
    F(293, "display in 3.2.3", "lim→ K.(X_i) ~⟶ K.(X) . (no index under lim)",
      "\\varinjlim_i K_{\\bullet}(X_i)\\xrightarrow{\\sim}K_{\\bullet}(X).", "extra", "high",
      fx("\\varinjlim_i K_{\\bullet}(X_i)\\xrightarrow", "\\varinjlim K_{\\bullet}(X_i)\\xrightarrow"), LIM_INDEX),
    F(293, "display in 3.2.3, equation number", "(3.2.2.1) — the same number as the display of 3.2.2",
      "\\tag{3.2.2.1} (printed reading kept)", "misprint_in_print", "high", None,
      "Two displays carry (3.2.2.1) (both scans); the one in 3.2.3 should be (3.2.3.1). The two later references "
      "'(3.2.1.1) et (3.2.2.1)' in the next paragraph mean this display and follow the printed number. The TeX keeps "
      "the printed reading; the corrected layer already reads \\tag{3.2.3.1} and (3.2.3.1) in both references.",
      corrected="\\tag{3.2.3.1}"),
    F(293, "paragraph 'Comme les structures ...'", "que lim→ K.(X_i) est muni (no index under lim)",
      "que \\(\\varinjlim_i K_{\\bullet}(X_i)\\) est muni", "extra", "high",
      fx("que \\(\\varinjlim_i K_{\\bullet}(X_i)\\) est muni", "que \\(\\varinjlim K_{\\bullet}(X_i)\\) est muni"),
      LIM_INDEX),
    F(293, "paragraph 'Comme les structures ...'", "sur lim→ K˙(X_i)_naïf ; celle-ci (no index under lim)",
      "sur \\(\\varinjlim_i K'(X_i)_{\\naif}\\);", "extra", "high",
      fx("sur \\(\\varinjlim_i K'(X_i)_{\\naif}\\);", "sur \\(\\varinjlim K'(X_i)_{\\naif}\\);"), LIM_INDEX),
    F(293, "diagram, left vertical arrow", "label ≃ (tilde over a bar), to the right of the arrow",
      "\\arrow[d,\"\\sim\"']", "symbol", "medium",
      fx("\\arrow[d,\"\\sim\"']", "\\arrow[d,\"\\simeq\"]"),
      "Both vertical labels are the typed ≃ (as in 'K.(X) ≃ K.(X)_naïf' on this page, which the TeX writes "
      "\\simeq), not the bare tilde set over the arrow of the display above; the print puts this label on the right."),
    F(293, "diagram, right vertical arrow", "label ≃ (tilde over a bar)", "\\arrow[d,\"\\sim\"]", "symbol",
      "medium", fx("\\arrow[d,\"\\sim\"]", "\\arrow[d,\"\\simeq\"]"), "As the left vertical arrow."),
    # ---------------- page 294
    F(294, "heading 3.3", "3.3. Groupes de Grothendieck relatifs (no full stop)",
      "\\textbf{3.3. Groupes de Grothendieck relatifs.}", "punctuation", "medium",
      fx("relatifs.}", "relatifs}"), "The TeX adds a full stop after the title (both scans)."),
    F(294, "3.3.1 and 3.3.2.2 (and p. 295)", "the subscript parf is underlined: D(f)_parf (6 places on p. 294, "
      "8 on p. 295; coh is not underlined)", "D(f)_{\\parf} with \\parf = \\operatorname{parf} (plain)",
      "underline", "high", None,
      "Convention, not itemized (see the coordinator message): \\parf (first defined in Exposé I's macros; the later "
      "\\providecommand are no-ops) prints a plain 'parf'. Examples: p. 294 K'(f)=k(D(f)_{\\parf}); p. 294 "
      "D(f)_{\\parf}\\times D(g)_{\\parf}\\longrightarrow D(h)_{\\parf}; p. 295 D(h)_{\\parf} dans D(g)_{\\parf}."),
    F(294, "3.3.2, after the triangle", "un triangle commutatif de morphisme localement de type fini de schémas.",
      "de morphisme localement (printed reading kept)", "misprint_in_print", "medium", None,
      "Singular 'morphisme' (both scans); the triangle has three morphisms, as 'un triangle commutatif de morphismes' "
      "elsewhere in the volume. The TeX keeps the printed reading; the corrected layer already reads 'morphismes'.",
      corrected="morphismes"),
    F(294, "3.3.2.2", "le foncteur ⊗^L_Y (typed L)", "\\(\\otimes_Y^{\\mathbf L}\\)", "font", "high",
      fx("\\otimes_Y^{\\mathbf L}", "\\otimes_Y^{\\mathrm L}"), TENSOR_L),
    # ---------------- page 295
    F(295, "3.3.2.3, display after 'on déduit la formule'", "f_*(ax) = af_*(x) (no comma; 'pour f propre' follows)",
      "f_*(a x)=a f_*(x),", "punctuation", "high", fx("f_*(a x)=a f_*(x),", "f_*(a x)=a f_*(x)"),
      "The TeX adds a comma at the end of the display (both scans)."),
    F(295, "3.3.3", "le foncteur ⊗^L_S (typed L)", "\\(\\otimes_S^{\\mathbf L}\\)", "font", "high",
      fx("\\otimes_S^{\\mathbf L}", "\\otimes_S^{\\mathrm L}"), TENSOR_L),
    F(295, "end of the page / folio-296 marker",
      "p. 295 ends with the display K˙(f_1) ⊗ K˙(f_2) ⟶ K˙(f) . ; p. 296 begins '(Bien entendu, pour ...'",
      "a lone '(' line stands at the end of page_295.tex, above the folio-296 marker", "marker", "high", None,
      "The '(' is the first character of p. 296 (witness p. 296). In both layers of main.tex replace '(\\n" + M296 +
      "\\nBien entendu' by '" + M296 + "\\n(Bien entendu' (once in each layer). This moves the marker and joins the "
      "'(' to its word in one step; python -I move_marker.py 6 296 \"(\" --before alone would leave '(' on its own "
      "line, printing '( Bien entendu'."),
]

pages = {p: (BATCH / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(291, 296)}
ok = True
for f in findings:
    fixd = f["fix"]
    if fixd is None:
        continue
    n = pages[f["page"]].count(fixd["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], n, repr(fixd["old"]))
    if "%%%%%%%%%%" in fixd["old"]:
        ok = False
        print("MARKER IN OLD", f["page"])
# disjointness of the fixes on each page
for p in pages:
    spans = []
    for f in findings:
        if f["page"] == p and f["fix"]:
            i = pages[p].find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("ok" if ok else "PROBLEMS", len(findings), counts)
