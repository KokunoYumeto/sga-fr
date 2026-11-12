"""Build findings_236_240.json and check every fix's old string (page files and current main.tex)."""
import json
import re

W = r"C:\Users\user\Documents\sga_scan_check_20261105"
B = W + r"\run_6\b236_240"
OUT = W + r"\run_6\findings_236_240.json"


def F(page, where, scan, tex, kind, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- p. 236
    F(236, "Corollaire 1.13, the functor O_X (x)^L_Y . = Lf* (opening of the display)",
      "le foncteur O_X ⊗^L_Y · = Lf* : D⁻(Y) ⟶ D⁻(X) induit, pour r ∈ Z ∪{-∞}, un foncteur (formula run into the sentence)",
      "le foncteur \\[ ... \\] induit (formula displayed)",
      "other", "high",
      "le foncteur\n\\[\n  \\mathcal O_X",
      "le foncteur \\(\\mathcal O_X",
      "The print runs this formula in the text line; only the second functor (Lf* : D⁻(g) → D⁻(h)) is displayed. "
      "Two edits that must be applied together: this one opens the inline formula, the next one closes it. "
      "Neither touches the L over the tensor sign (\\mathbf L in this page file, \\mathrm L in main.tex)."),
    F(236, "Corollaire 1.13, the functor O_X (x)^L_Y . = Lf* (closing of the display)",
      "... D⁻(X) induit, pour r ∈ Z ∪{-∞}, un foncteur",
      "D^{-}(X) \\] induit",
      "other", "high",
      "D^{-}(X)\n\\]\ninduit",
      "D^{-}(X)\\) induit",
      "Second half of the previous finding; apply both or neither."),
    F(236, "Corollaire 1.13, placeholder after the derived tensor product",
      "O_X ⊗^L_Y · = Lf* (raised, centred dot after the Y subscript, in both scans)",
      "\\otimes_Y^{\\mathbf L}.=Lf^* (full stop on the baseline)",
      "symbol", "medium",
      "L}.=Lf^*",
      "L}\\cdot=Lf^*",
      "The dot stands at mid-letter height in the main scan and in the witness, not on the line. "
      "The old string also matches main.tex, where the L is now \\mathrm L."),
    F(236, "Théorème 2.2, the cases (i) and (ii)",
      "(i) S est localement noethérien ; / (ii) f est projectif. (two indented lines of text, a list)",
      "a centred gathered display with \\text{(i) } S\\text{ est localement noethérien};\\\\ \\text{(ii) } f\\text{ est projectif}.",
      "other", "low",
      "\\[\n\\begin{gathered}\n  \\text{(i) } S\\text{ est localement noethérien};\\\\\n  \\text{(ii) } f\\text{ est projectif}.\n\\end{gathered}\n\\]",
      "\\begin{enumerate}[label=(\\roman*)]\n\\item \\(S\\) est localement noethérien ;\n\\item \\(f\\) est projectif.\n\\end{enumerate}",
      "Layout only: the print sets the two cases as an indented list of text lines, as the file's own "
      "enumerate[label=(\\roman*)] lists elsewhere in Exposé III; the words and punctuation already agree."),
    F(236, "heading of section 2",
      "2. Le théorème de finitude.",
      "\\section*{2. Le théorème de finitude}",
      "punctuation", "medium",
      "\\section*{2. Le théorème de finitude}",
      "\\section*{2. Le théorème de finitude.}",
      "The typed heading ends with a full stop (both scans), as for the \\subsubsection*{2.2.} fix on p. 3."),
    # ---------------- p. 237
    F(237, "start of the page, proof label of case (i)",
      "Preuve dans le cas (i). (only 'Preuve dans le cas' underlined)",
      "\\emph{Preuve dans le cas (i).}",
      "underline", "high",
      "\\emph{Preuve dans le cas (i).}",
      "\\emph{Preuve dans le cas} (i).",
      "The case number is not underlined; same correction as p. 235 (\\emph{Preuve de} a).)."),
    F(237, "proof label of case (ii)",
      "Preuve dans le cas (ii). (only 'Preuve dans le cas' underlined)",
      "\\emph{Preuve dans le cas (ii).}",
      "underline", "high",
      "\\emph{Preuve dans le cas (ii).}",
      "\\emph{Preuve dans le cas} (ii).",
      "As the previous finding."),
    F(237, "diagram, top vertex",
      "P^r_{Y'} with a typed plain P",
      "\\mathbb P^r_{Y'}",
      "font", "low",
      "\\mathbb P^r_{Y'}",
      "P^r_{Y'}",
      "The typist's ordinary P (same glyph as in P = P(F) on p. 240, which the TeX writes plain); the TeX of "
      "Exposé II writes the typed P^n plain. Low: same family as the plain Q (issue 61/78 decision)."),
    F(237, "diagram, left vertex",
      "P^r_Y with a typed plain P",
      "\\mathbb P^r_Y",
      "font", "low",
      "\\mathbb P^r_Y \\arrow",
      "P^r_Y \\arrow",
      "As the previous finding."),
    # ---------------- p. 238
    F(238, "'i.e. (1.1 (iii)) que j'_*Rf_*(E) est pseudo-cohérent'",
      "que j'_*Rf_*(E) est pseudo-cohérent. Mais on a (formula in the running text, plain R)",
      "que \\[ j'_*\\mathbf Rf_*(E) \\] est pseudo-cohérent.",
      "other", "high",
      "que\n\\[\n  j'_*\\mathbf Rf_*(E)\n\\]\nest pseudo-cohérent.",
      "que \\(j'_*Rf_*(E)\\) est pseudo-cohérent.",
      "The print does not display this formula. The new text also has the print's plain R "
      "(see the message: \\mathbf R for the typed R on pp. 236-240)."),
    F(238, "display j'_*Rf_*(E) ≃ Rp'_*(ji)_*(E)",
      "≃ (typed tilde over a dash, no arrowhead; both scans)",
      "\\xrightarrow{\\sim}",
      "symbol", "high",
      "\\xrightarrow{\\sim}",
      "\\simeq",
      "Same sign and same correction as p. 223 (\\xrightarrow{\\sim}i_*H^n -> \\simeq i_*H^n)."),
    F(238, "Théorème 2.2.2, f : X = P^r_Y -> Y",
      "X = P^r_Y with a typed plain P",
      "X=\\mathbb P^r_Y",
      "font", "low",
      "X=\\mathbb P^r_Y",
      "X=P^r_Y",
      "As p. 237 (typed plain P)."),
    F(238, "proof of 2.2.2, 'd'après (EGA III 1.4.10) et la suite spectrale d'hypercohomologie, R^qf_*(E) = 0 pour i > a+r'",
      "R^qf_*(E) = 0 pour i > a+r (both scans)",
      "\\(R^qf_*(E)=0\\) pour \\(i>a+r\\)",
      "misprint_in_print", "high",
      None, None,
      "Index misprint: the degree is q in R^q but i in the condition. The TeX keeps the printed reading. "
      "Alternative correction: keep R^q and read 'pour q>a+r'.",
      corrected="\\(R^if_*(E)=0\\) pour \\(i>a+r\\)"),
    F(238, "E' = (0 -> E^t -> ... -> E^a -> 0)",
      "E^t → ... → E^a (three dots on the line)",
      "E^t\\to\\cdots\\to E^a",
      "symbol", "high",
      "\\to\\cdots\\to",
      "\\to\\ldots\\to",
      "Baseline dots, as the \\cdots -> \\ldots fixes of Exposés I and II."),
    # ---------------- p. 239
    F(239, "distinguished triangle (*) after 'on obtient un triangle distingué'",
      "a triangle: Rf_*(E\") on top, Rf_*(E') → Rf_*(E) below, Rf_*(E) → Rf_*(E\") and Rf_*(E\") → Rf_*(E') "
      "(this arrow marked with a short bar), no [1]; full stop after the diagram",
      "one line Rf_*(E') → Rf_*(E) → Rf_*(E'') → Rf_*(E')[1], no full stop",
      "formula", "high",
      "\\mathbf Rf_*(E')\\longrightarrow \\mathbf Rf_*(E)\\longrightarrow \\mathbf Rf_*(E'')\\longrightarrow \\mathbf Rf_*(E')[1]",
      "\\begin{tikzcd}\n& Rf_*(E'') \\arrow[dl,\"|\" marking] & \\\\\nRf_*(E') \\arrow[rr] & & Rf_*(E) \\arrow[ul] & .\n\\end{tikzcd}",
      "Issue 84 (small triangles set on one line with an added [1]): drawn as on p. 223, the marked arrow "
      "as \"|\" marking; the printed full stop added; the R plain as printed. Stays inside the existing "
      "equation with \\tag{$*$}."),
    F(239, "'si l'on prouve que Rf_*(E') est parfait. Pour cela, on se ramène'",
      "one paragraph: 'Pour cela' continues on the next line at the margin, no indent, no extra space",
      "est parfait.\\n\\nPour cela (new paragraph)",
      "other", "medium",
      "est parfait.\n\nPour cela",
      "est parfait. Pour cela",
      "The line before is full ('Pour' did not fit); new paragraphs in this typescript are indented or "
      "set off by a blank line. Same kind of join as p. 229."),
    F(239, "display Rf_*(O_X(-n)) ≃ R^rf_*(O_X(-n))[-r]",
      "≃ (typed tilde over a dash, no arrowhead; both scans)",
      "\\xrightarrow{\\sim}",
      "symbol", "high",
      "\\xrightarrow{\\sim}",
      "\\simeq",
      "As p. 238."),
    # ---------------- p. 240
    F(240, "proof of Corollaire 2.3, f : X = P^r_Y -> Y",
      "X = P^r_Y with a typed plain P",
      "X=\\mathbb P^r_Y",
      "font", "low",
      "X=\\mathbb P^r_Y",
      "X=P^r_Y",
      "As p. 237; in the same corollary the TeX writes the typed P of P = P(F) plain."),
    F(240, "display of Corollaire 2.4, Rf_* : D^b(X)_{S-coh} -> D^b(Y)_{S-coh}",
      "no punctuation after the display (both scans)",
      "D^b(Y)_{S\\text{-}\\coh}.",
      "punctuation", "high",
      "D^b(Y)_{S\\text{-}\\coh}.",
      "D^b(Y)_{S\\text{-}\\coh}",
      "Full stop added by the transcription."),
    F(240, "proof of Corollaire 2.3, 'un complexe pseudo-cohérent et acyclique en degré ≥ a'",
      "main scan: > with a thin light stroke under it (not the typed ≥ of 'n ≥ N' at the end of the statement of Cor. 2.3); "
      "witness: a plain > with only a speck where that stroke begins",
      "acyclique en degré \\(\\geq a\\)",
      "misprint_in_print", "low",
      None, None,
      "The hypothesis of Cor. 2.3 and of (2.2.2) is 'acyclique en degré > a'. If the stroke is a mark of the "
      "main scan's copy and not print, the diplomatic text should read \\(>a\\) instead "
      "(fix: '\\(\\geq a\\)' -> '\\(>a\\)').",
      corrected="acyclique en degré \\(>a\\)"),
]

json.dump(findings, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)

# checks: every old exactly once in its page file; also in the page's current main.tex segment
main = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
ms = list(re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", main))
seg = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(main)
    seg[int(m.group(2))] = main[m.start():end]
ok = True
for d in json.load(open(OUT, encoding="utf-8")):
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    pf = open(B + f"\\page_{d['page']}.tex", encoding="utf-8").read()
    n1 = pf.count(old)
    n2 = seg[d["page"]].count(old)
    flag = "OK" if n1 == 1 else "BAD"
    if n1 != 1:
        ok = False
    print(d["page"], flag, n1, "main:", n2, repr(old[:60]))
print("all unique in page files:", ok, "| findings:", len(findings))
