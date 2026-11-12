"""Build findings_221_225.json (SGA 6, Exposé II bibliography end and Exposé III pp. 1-4), check that every fix's
'old' occurs exactly once in its page file, and write patched copies of the pages into this folder (test only).
usage: python -I make_findings.py"""
import json
import pathlib

HERE = pathlib.Path(__file__).parent
RUN = HERE.parent
PAGES = RUN / "b221_225"
OUT = RUN / "findings_221_225.json"


def F(page, where, scan, tex, kind, confidence, fix, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, confidence=confidence, fix=fix)
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


TRI1_OLD = r"E'\longrightarrow E\longrightarrow E''\longrightarrow E'[1]"
TRI1_NEW = "\\begin{tikzcd}\n& E'' \\arrow[dl,\"|\" marking] & \\\\\nE' \\arrow[rr] & & E \\arrow[ul]\n\\end{tikzcd}"
TRI2_OLD = r"i_*(E')\longrightarrow i_*(E)\longrightarrow i_*(E'')\longrightarrow i_*(E')[1]"
TRI2_NEW = ("\\begin{tikzcd}\n& i_*(E'') \\arrow[dl,\"|\" marking] & \\\\\n"
            "i_*(E') \\arrow[rr] & & i_*(E) \\arrow[ul]\n\\end{tikzcd}")
FN2 = (r"\(D(Y)_{n\text{-}\coh}\) = sous-catégorie pleine de \(D(Y)\) formée des objets "
       r"\(n\)-pseudo-cohérents (I~2.15).")
DISP = ("\n\\[\n  E\\in\\Ob D(h)_{n\\text{-}\\coh}\n  \\quad\\Longleftrightarrow\\quad\n"
        "  f_*(E)\\in D(Y)_{n\\text{-}\\coh}")
FN_OLD = "on a\\footnote{" + FN2 + "}" + DISP + ".\n\\]"
FN_NEW = "on a" + DISP + "\\qquad\\mbox{\\footnotemark}\\ .\n\\]\n\\footnotetext{" + FN2 + "}"

findings = [
    # ---------------- p. 221 (Exposé II, end of the bibliography)
    F(221, "start of page",
      "p. 221 begins with item [14] 'Lang, S., Introduction to differentiable manifolds,' (both scans)",
      "the bare '\\item' that makes the label [14] is the last line of page_220.tex, above the folio-221 marker; "
      "page_221.tex begins 'Lang, S.'",
      "marker", "high", None,
      "ALREADY DONE, no action: reported by findings_216_220.json (p. 220, end of page) and applied; the live "
      "main.tex has the folio-221 marker above that '\\item' in both layers (checked against main.tex of 20:34). "
      "Do not run python -I move_marker.py 6 221 '\\item' --before again: it would now put the marker above "
      "'\\item Kiehl'."),
    F(221, "[15] Łojasiewicz",
      "Łojasiewicz: the initial L is crossed by a stroke (Polish Ł), both scans "
      "(crops_221_225/p221_loj.png, w221_loj.png)",
      "Lojasiewicz", "accent", "high", fx("Lojasiewicz", r"\L{}ojasiewicz")),
    F(221, "[16] Palais", "Princeton 1963-64: typed hyphen (both scans)", "Princeton 1963--64",
      "punctuation", "high", fx("1963--64", "1963-64"),
      "En dash added by the transcription, as the bibliography dashes fixed on p. 220 (findings_216_220)."),

    # ---------------- p. 222 (Exposé III, p. 1)
    F(222, "exposé heading and title",
      "EXPOSE III in typed capitals with a single underline and no full stop, on its own line; then the title "
      "CONDITIONS DE FINITUDE RELATIVES in capitals with a double underline (both scans)",
      r"\section*{Exposé III. Conditions de finitude relatives}", "word", "medium",
      fx(r"\section*{Exposé III. Conditions de finitude relatives}",
         r"\section*{\underline{EXPOSÉ III}\\[3pt] \underline{\underline{CONDITIONS DE FINITUDE RELATIVES}}}"),
      "Same form as the applied Exposé II heading (main.tex: \\section*{\\underline{Exposé II}\\\\[3pt] "
      "\\underline{\\underline{EXISTENCE DE RÉSOLUTIONS GLOBALES}}}); here the typescript types EXPOSE in "
      "capitals (É keeps the TeX's accent, rule for typed capitals)."),
    F(222, "author line", "par L. ILLUSIE: the name in capitals, the whole line underlined (both scans)",
      "par L. Illusie", "word", "medium", fx("par L. Illusie", r"\underline{par L. ILLUSIE}"),
      "As the applied author lines of pp. 78 and 160."),
    F(222, "Théorème 1.1 (pattern also in Lemmes 1.1.1, 1.1.3, 1.1.4, pp. 223-225)",
      "the statements are underlined word group by word group: Th. 1.1 'Soit', 'Pour chaque morphisme localement "
      "de type fini de schémas', 'il existe une et une seule sous-catégorie pleine', 'de', 'telle que les "
      "conditions ci-dessous soient satisfaites', items (i)-(iii) likewise; Lemme 1.1.1 'Soit', 'une immersion "
      "fermée de schémas telle que', 'soit pseudo-cohérent', ...; Lemme 1.1.3 'Soit un carré cartésien de "
      "schémas', ... (both scans)",
      "the statements in roman: in Exposé III (main.tex lines 5352-6565) statement text has no \\underline and "
      "one \\emph only (Soit, p. 227)",
      "underline", "high", None,
      "Exposé III follows the Exposé II pattern of GLOBAL_ISSUES 82 (statements in roman where the typescript "
      "underlines their word groups). Not itemized: for the same scripted per-exposé decision. Bold labels and "
      "\\emph{Démonstration.}/\\emph{Preuve.} are the accepted forms."),
    F(222, "Théorème 1.1 (ii), 'Si E ∈ ob D(X)'",
      "ob in small letters (both scans; crops_221_225/p222_ii_ob.png); items (i) and (iii) print Ob with a capital "
      "(p222_i_Ob.png, p222_iii_Ob.png)",
      "\\Ob, which Exposé III's \\renewcommand (page_221.tex) prints as Ob", "word", "high",
      fx(r"\item Si \(E\in\Ob D(X)\)", r"\item Si \(E\in\ob D(X)\)"),
      "\\ob (= \\operatorname{ob}) is defined in the file (\\providecommand, main.tex line 1521). See the message "
      "on \\Ob in Exposé III."),
    F(222, "Théorème 1.1 (ii), 'tel que i^*_α(E) ∈ ob D(fi_α)_{n-coh}'", "ob in small letters (both scans)",
      "\\Ob (prints Ob)", "word", "high", fx(r"\Ob D(fi_\alpha)", r"\ob D(fi_\alpha)")),
    F(222, "Théorème 1.1 (ii), 'alors E ∈ ob D( f)_{n-coh}'",
      "ob in small letters (both scans; crops_221_225/p222_ii_end.png)", "\\Ob (prints Ob)", "word", "high",
      fx(r"alors \(E\in\Ob D(f)", r"alors \(E\in\ob D(f)")),
    F(222, "Théorème 1.1 (iii), call of footnote (2)",
      "the call (²) stands in the display, after 'f_*(E) ∈ D(Y)_{n-coh}' and before the display's final full "
      "stop; 'alors on a' has no call (both scans)",
      "\\footnote{...} after 'alors on a', before the display", "other", "high", fx(FN_OLD, FN_NEW),
      "One edit: takes the footnote off 'on a' and sets its call in the display with \\footnotemark and "
      "\\footnotetext after the display, as the file does for a call in a display (Exposé 0), but in \\mbox: "
      "the file's \\text{\\footnotemark} steps the counter four times (amsmath \\text sets its argument in all four math styles), so the text got number 5 in a test compile; \\mbox gives 2. Footnote text unchanged."),
    F(222, "Démonstration, 'pour chaque α∈A, fi_α se factorise en'", "pour chaque α∈A, (both scans)",
      "pour chaque \\(\\alpha\\),", "missing", "high",
      fx(r"pour chaque \(\alpha\),", r"pour chaque \(\alpha\in A\),")),
    F(222, "Démonstration, 'tels que i'_{α*}i_α^*(E) ∈ ob D(Y_α)_{n-coh}'", "ob in small letters (both scans; "
      "crops_221_225/p222_proof_ob.png)", "\\Ob (prints Ob)", "word", "high",
      fx(r"\in \Ob D(Y_\alpha)", r"\in \ob D(Y_\alpha)")),
    F(222, "Démonstration, first sentence", "L'unicité: 'unicité' underlined (both scans)",
      "L'unicité (plain)", "underline", "high", fx("L'unicité est", r"L'\emph{unicité} est"),
      "\\emph is the file's command for underlined words in Exposé III (\\emph{Preuve.}, \\emph{Soit} p. 227)."),

    # ---------------- p. 223 (Exposé III, p. 2)
    F(223, "start of page",
      "p. 223 begins 'est bien déterminée (puisque c'est une sous-catégorie pleine de D(X))'; p. 222 ends "
      "'; donc D(f)_{n-coh}' (both scans)",
      "'est' is the last word of page_222.tex ('donc \\(D(f)_{n\\text{-}\\coh}\\) est'); page_223.tex begins "
      "'bien déterminée'",
      "marker", "high", None,
      "Page 223 really begins with 'est'. Move the folio-223 marker before it: python -I move_marker.py 6 223 "
      "\"est\" --before (simulated on both layers of the live main.tex: '... donc \\(D(f)_{n\\text{-}\\coh}\\)', "
      "the marker, 'est', 'bien déterminée')."),
    F(223, "Lemme 1.1.1, 'et soit E ∈ ob D(X)'", "ob in small letters (both scans)", "\\Ob (prints Ob)",
      "word", "high", fx(r"\(E\in\Ob D(X)\)", r"\(E\in\ob D(X)\)")),
    F(223, "proof of Lemme 1.1.1, 'on a donc un triangle distingué'",
      "a drawn triangle: E'' above, E' → E below, the arrows E → E'' (↖) and E'' → E' (↙), the last with a "
      "small transverse tick (the degree-one arrow); no E'[1] (both scans; crops_221_225/w223_tri1.png, "
      "w223_tick1.png)",
      "a linear display E'\\longrightarrow E\\longrightarrow E''\\longrightarrow E'[1]", "formula", "high",
      fx(TRI1_OLD, TRI1_NEW),
      "tikzcd as the Exposé I triangles; the tick as a \"|\" marking (tikz-cd style), where Exposé I prints "
      "+1. Exposé III writes the print's drawn triangles linearly with an added [1] term: see the message."),
    F(223, "proof of Lemme 1.1.1, 'on obtient un triangle distingué'",
      "the same drawn triangle: i_*(E'') above, i_*(E') → i_*(E) below, the ticked arrow i_*(E'') → i_*(E') "
      "(both scans; crops_221_225/w223_tri2.png, w223_tick2.png)",
      "a linear display i_*(E')\\longrightarrow i_*(E)\\longrightarrow i_*(E'')\\longrightarrow i_*(E')[1]",
      "formula", "high", fx(TRI2_OLD, TRI2_NEW), "Independent of the next entry (disjoint texts)."),
    F(223, "after the second triangle, '. D'après la première partie de la démonstration'",
      "a full stop after the diagram, then a new sentence 'D'après la première partie' with a capital D; "
      "no 'et,' (both scans; crops_221_225/w223_tri2.png)",
      "no full stop after the display, then 'et, d'après la première partie'", "word", "high",
      fx("\n\\]\net, d'après la première", "\\ .\n\\]\nD'après la première")),
    F(223, "'que H^n(i_*(E'') est de type fini'",
      "H^n(i_*(E\") est de type fini: one closing parenthesis missing (both scans; crops_221_225/w223_Hn.png)",
      "\\(H^n(i_*(E'')\\) (printed reading kept)", "misprint_in_print", "high", None,
      "The TeX keeps the printed reading; the next sentence prints H^n(i_*(E\")) with both parentheses.",
      corrected=r"\(H^n(i_*(E''))\)"),
    F(223, "'Comme H^n(i_*(E'')) ≃ i_*H^n(E'')'",
      "≃: a typed tilde over a straight line, no arrowhead (both scans; crops_221_225/p223_iso.png, "
      "w223_iso.png)",
      "\\xrightarrow{\\sim}", "symbol", "high", fx(r"\xrightarrow{\sim}i_*H^n", r"\simeq i_*H^n"),
      "As the headless ≃ fixed on pp. 110, 118, 150, 153."),
    F(223, "last line, '(et indépendant de l'hypothèse sur i_*(O_X))'",
      "ī_*(O_X): a short typed bar over the i (both scans; crops_221_225/p223_ibar.png, w223_ibar.png)",
      "\\(i_*(\\mathcal O_X)\\) (without the bar: silent correction)", "misprint_in_print", "low",
      fx(r"l'hypothèse sur \(i_*", r"l'hypothèse sur \(\bar i_*"),
      "No ī is defined; the hypothesis meant is the one on i_*(O_X) of Lemme 1.1.1. The bar stands in both "
      "independent scans, so it is in the print (a stray typed stroke, not the scan). If the volume treats such "
      "strokes as marks rather than text, drop this entry.",
      corrected=r"\(i_*(\mathcal O_X)\)"),

    # ---------------- p. 224 (Exposé III, p. 3)
    F(224, "Remarque 1.1.2, 'au cas où i est une immersion régulière'",
      "'immersion régulière' underlined (both scans)", "une immersion régulière (plain)", "underline", "high",
      fx("une immersion régulière (VII", r"une \emph{immersion régulière} (VII")),
    F(224, "Remarque 1.1.2, 'grâce au complexe de Kozsul'", "Kozsul (both scans)",
      "Kozsul (printed reading kept)", "misprint_in_print", "high", None,
      "The TeX keeps the printed reading.", corrected="Koszul"),
    F(224, "Lemme 1.1.3, 'Alors la flèche canonique de changement de base'",
      "no item label (i): 'Alors' ends the line, 'la flèche canonique' begins the next after a blank of about "
      "three typewriter cells, and the statement goes on with '(ii) Posons E' = f*(E)' (both scans; "
      "crops_221_225/p224_li.png)",
      "Alors la flèche canonique ... est un isomorphisme. (ii) Posons ... (printed reading kept)",
      "misprint_in_print", "medium", None,
      "The typist left the room for '(i)' empty. The TeX keeps the printed reading.",
      corrected="Alors (i) la flèche canonique de changement de base"),

    # ---------------- p. 225 (Exposé III, p. 4)
    F(225, "start of page",
      "p. 225 begins 'Lemme 1.1.4. Soit un diagramme commutatif de schémas'; p. 224 ends with 'Preuve. "
      "L'assertion se vérifie trivialement sur les fibres.' and blank space (both scans)",
      "\\textbf{Lemme 1.1.4.} is the last line of page_224.tex (under the folio-224 marker); page_225.tex begins "
      "'Soit un diagramme'",
      "marker", "high", None,
      "Page 225 really begins with the label (a heading at the top of the page). Move the folio-225 marker above "
      "it: python -I move_marker.py 6 225 '\\textbf{Lemme 1.1.4.}' --before (single quotes; simulated on both layers of the live main.tex)."),
    F(225, "Lemme 1.1.4, diagram, the arrows i' and i''",
      "X' ↩ X ↪ X'': both closed immersions are hooked arrows, the hooks at X (both scans; "
      "crops_221_225/w225_lem.png)",
      "plain arrows \\arrow[l,\"i'\"'] and \\arrow[r,\"i''\"]", "symbol", "high",
      fx("X \\arrow[l,\"i'\"'] \\arrow[r,\"i''\"]", "X \\arrow[l,hook',\"i'\"'] \\arrow[r,hook,\"i''\"]"),
      "The file's form for hooked arrows (hook, hook'), as on p. 227."),
    F(225, "Lemme 1.1.4, 'et soit E ∈ ob D(X)'", "ob in small letters (both scans)", "\\Ob (prints Ob)",
      "word", "high", fx(r"\(E\in\Ob D(X)\)", r"\(E\in\ob D(X)\)")),
    F(225, "Lemme 1.1.4, display 'i'_*(E) n-pseudo-cohérent ⟺ i''_* n-pseudo-cohérent'",
      "i\"_* without (E) on the right side (both scans)",
      "i''_*\\ n\\text{-pseudo-cohérent} (printed reading kept)", "misprint_in_print", "high", None,
      "The TeX keeps the printed reading; the left side has i'_*(E).",
      corrected=r"i''_*(E)\ n\text{-pseudo-cohérent}"),
    F(225, "proof, triangle (*), the arrows i and j",
      "X ↪ Z (j) and the oblique X ↪ Y (i) are hooked arrows (both scans; crops_221_225/w225_star.png)",
      "plain arrows \\arrow[r,\"j\"'] \\arrow[ur,\"i\"]", "symbol", "high",
      fx("X \\arrow[r,\"j\"'] \\arrow[ur,\"i\"]", "X \\arrow[r,hook,\"j\"'] \\arrow[ur,hook,\"i\"]")),
    F(225, "proof, factorisation diagram, the arrow i'",
      "Y ↪ Z[T_1,...,T_r]: a hooked arrow (both scans; crops_221_225/w225_fact.png)",
      "plain arrow \\arrow[r,\"i'\"]", "symbol", "high",
      fx("Y \\arrow[r,\"i'\"]", "Y \\arrow[r,hook,\"i'\"]")),
    F(225, "proof, factorisation diagram, end", "a comma after the diagram, level with Z (both scans)",
      "no comma", "punctuation", "high", fx("Z&\n\\end{tikzcd}", "Z{,}&\n\\end{tikzcd}"),
      "As Y{,} and Z{,} in the two diagrams before it."),
]

# ---- checks: each 'old' exactly once in its page, no overlap between fixes of one page; patched copies
ok = True
texts = {p: (PAGES / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(221, 226)}
patched = dict(texts)
spans = {}
for i, f in enumerate(findings):
    if f["fix"] is None:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    t = texts[f["page"]]
    n = t.count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE", f["page"], n, repr(old[:60]))
    if "%%%%%%%%%%" in old:
        ok = False
        print("CROSSES MARKER", f["page"], repr(old[:60]))
    k = t.find(old)
    spans.setdefault(f["page"], []).append((k, k + len(old), i))
for p, ss in spans.items():
    ss.sort()
    for (a, b, i), (c, d, j) in zip(ss, ss[1:]):
        if c < b:
            ok = False
            print("OVERLAP on page", p, i, j)
for f in findings:
    if f["fix"] is None:
        continue
    p = f["page"]
    patched[p] = patched[p].replace(f["fix"]["old"], f["fix"]["new"], 1)
for p, t in patched.items():
    (HERE / f"patched_{p}.tex").write_text(t, encoding="utf-8", newline="\n")
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0])
    c[1 if f["kind"] == "misprint_in_print" else 0] += 1
print("all unique, no overlaps" if ok else "PROBLEMS")
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})
print("written", OUT)
