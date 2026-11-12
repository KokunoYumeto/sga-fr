"""Write findings_056_060.json and check that every fix's old text occurs exactly once in its page file.
usage: python -I make_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
B = RUN / "b056_060"
OUT = RUN / "findings_056_060.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 56
add(56, "start of page: display (2.30)",
    "p. 56 begins with the display '(2.30)  K(Y) → K(X) → K(U) → 0', followed by 'est exacte.'; p. 55 ends "
    "'Alors la suite d'homomorphismes naturels :' (both scans; DjVu witness p. 67)",
    "the equation \\tag{2.30} is the last item of page_055.tex (under the folio-55 marker); page_056.tex begins "
    "'\\emph{est exacte.}'",
    "marker", "high", None,
    "Page 56 really begins with the display (2.30). Move the folio-56 marker up 3 lines, above "
    "'\\begin{equation}\\tag{2.30}': python -I move_marker.py 6 56 '\\begin{equation}\\tag{2.30}' --before "
    "(single quotes; simulated on both layers: '... d'homomorphismes naturels~:}' / marker / "
    "'\\begin{equation}\\tag{2.30}' / ...). The checker of pp. 51-55 may report the same move from the other side.")

add(56, "throughout pp. 56-57 (here: 'où P'_i|U ≃ Q'_i|U', 'tels que R|U ≃ S|U', 'de (R×S)|U')",
    "R|U: a tall bar followed by U at full size on the baseline; G|U_i with the index i on that U "
    "(both scans)",
    "R|_U: the open set as a subscript; \\overline{G|_{U_i}}",
    "formula", "medium", None,
    "Convention of the transcription, not a page fix: the restriction is written with the open set as a "
    "subscript where the typescript writes it on the line. On these pages (11 places): p. 56 "
    "'$P'_i|_U\\simeq Q'_i|_U$', '$R|_U\\simeq S|_U$', 'de $R|_U$ sur $S|_U$', '$(R\\times S)|_U$'; p. 57 "
    "'cohérent de $F|_U$' (Lemme 2.11), '$\\overline{G|_{U_i}}$', 'alors $F|_U$ est défini', "
    "'de $F|_U$ est alors'. The p. 46 display (\\overline F|_{U_i} in the TeX) has the same printed form. "
    "Diplomatic form: R|U, \\overline{G|U_i}; one pass in the diplomatic layer if adopted.")

# ---------------- page 57
add(57, "start of page",
    "p. 57 begins 'noté encore T, de R x S.'; p. 56 ends 'c'est la restriction à U d'un sous-faisceau "
    "cohérent,' (both scans)",
    "'noté' is the last word of page_056.tex (under the folio-56 marker); page_057.tex begins 'encore $T$'",
    "marker", "high", None,
    "Page 57 really begins with 'noté'. Move the folio-57 marker before it: python -I move_marker.py 6 57 "
    "'noté' --before (the last 'noté' before the marker is that word; simulated on both layers: "
    "'... d'un sous-faisceau cohérent, ' / marker / 'noté' / 'encore $T$, de ...').")

add(57, "proof of Lemme 2.11, 'dont la restriction à U ∩ V est une section de V'",
    "est une section de V. (both scans)",
    "est une section de $V$ (printed reading kept)",
    "misprint_in_print", "high", None,
    "The sections of Ḡ over V are the sections of F over V whose restriction to U ∩ V is a section of G; "
    "V is the open set itself. The TeX keeps the printed reading; the corrected layer still reads "
    "'de $V$'.",
    corrected="est une section de $G$")

add(57, "label 'Corollaire 1 à la proposition 2.10'",
    "Corollaire 1 à la proposition 2.10 : Soit x ∈ K(X). (a colon after 2.10, both scans)",
    "\\textbf{Corollaire 1 à la proposition 2.10.}",
    "punctuation", "medium",
    {"old": "\\textbf{Corollaire 1 à la proposition 2.10.}",
     "new": "\\textbf{Corollaire 1 à la proposition 2.10~:}"},
    "The TeX turns the label's colon into a full stop (the bold setting itself is accepted). Same on p. 59 "
    "(Corollaires 1 and 2) and p. 60 (Proposition 2.13), separate entries.")

# ---------------- page 58
add(58, "exact sequence before Théorème 2.12",
    "0 → O_X(L(-D)) → O_X → O_D → 0: a typed O with an underline (both scans)",
    "\\cO_X(L(-D)), \\cO_X, \\cO_D (\\cO = \\mathcal O)",
    "font", "low", None,
    "Not a page fix: the convention already reported for p. 45 (findings_041_045: the print's underlined O "
    "written \\cO in this appendix), pending one decision for the volume.")

# ---------------- page 59
add(59, "start of page",
    "p. 59 begins 'X x k (n est la dimension de X), et deux points'; p. 58 ends 'on peut trouver un cycle Y "
    "de dimension n - p + 1 sur' (both scans)",
    "'$X\\times k$ ($n$ est la' ends the last line of page_058.tex (under the folio-58 marker); "
    "page_059.tex begins 'dimension de $X$)'",
    "marker", "high", None,
    "Page 59 really begins with '$X\\times k$'. Move the folio-59 marker before it: python -I move_marker.py "
    "6 59 '$X\\times k$ ($n$ est la' --before (single quotes, so that the shell leaves $X and $n alone; "
    "simulated on both layers: '... de dimension $n-p+1$ sur ' / marker / '$X\\times k$ ($n$ est la' / "
    "'dimension de $X$), ...').")

add(59, "'Il suffit alors de prouver que f_a^! = f_{a'}^!'",
    "f^!_a = f^!_a: both indices a, no prime on the second (both scans; the prime of f_{a'}^{-1}(Y) in the "
    "display above is clear in both)",
    "$f_a^!=f_{a'}^!$ (silently corrected)",
    "misprint_in_print", "high",
    {"old": "f_a^!=f_{a'}^!", "new": "f_a^!=f_a^!"},
    "The argument needs f_a^! = f_{a'}^! (Z = f_a^{-1}(Y), Z' = f_{a'}^{-1}(Y)); the typist dropped the "
    "prime. Diplomatic layer: the printed f_a^! twice; the corrected layer reads f_{a'}^!.",
    corrected="f_a^!=f_{a'}^!")

add(59, "label 'Corollaire 1' (of Théorème 2.12)",
    "Corollaire 1 : La filtration de K(X) ... (colon, both scans)",
    "\\textbf{Corollaire 1.}",
    "punctuation", "medium",
    {"old": "\\textbf{Corollaire 1.}", "new": "\\textbf{Corollaire 1~:}"},
    "As p. 57: the label's colon became a full stop.")

add(59, "(2.34), target G(K(X))",
    "φ: A(X) ⟶ G(K(X)): this K is not underlined (both scans), unlike K(X) in the next line and "
    "G(K(Y)), G(K(X)) in the diagram of Corollaire 2",
    "G(\\underline K(X)) (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "\\longrightarrow G(\\underline K(X))", "new": "\\longrightarrow G(K(X))"},
    "The typist dropped the underline of K (as the L of p. 43 and the E of p. 44); the TeX silently "
    "restores it. The corrected layer reads \\underline K.",
    corrected="\\longrightarrow G(\\underline K(X))")

add(59, "Corollaire 1, '... (K(X)^i)_{i≥0}) défini par la condition :'",
    "'défini par la condition' underlined (the statement resumes after the parenthesis); the colon and the "
    "parenthesis '(où le deuxième membre ... i≥0)' are not (both scans)",
    "plain 'défini par la condition~:' (the \\emph of the statement closes at 'gradués~:}')",
    "underline", "high",
    {"old": "$) défini par la condition~:", "new": "$) \\emph{défini par la condition}~:"},
    "Missing underline.")

add(59, "label 'Corollaire 2' (of Théorème 2.12)",
    "Corollaire 2 : Soient X et Y ... (colon; a faint erased character stands before the 2, both scans)",
    "\\textbf{Corollaire 2.}",
    "punctuation", "medium",
    {"old": "\\textbf{Corollaire 2.}", "new": "\\textbf{Corollaire 2~:}"},
    "As p. 57: the label's colon became a full stop. The faint mark before '2' is an erased character of "
    "the typescript, not part of the label.")

add(59, "Corollaire 2, 'l'homomorphisme f^! de K(Y) dans K(X)'",
    "dans K(X): this K is not underlined (both scans); K(Y) just before it is",
    "dans $\\underline K(X)$ (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "dans $\\underline K(X)$ est compatible", "new": "dans $K(X)$ est compatible"},
    "Dropped underline of K, as in (2.34) above; the corrected layer reads \\underline K.",
    corrected="dans $\\underline K(X)$ est compatible")

add(59, "diagram of Corollaire 2, labels f* and φ_Y",
    "f* above the bottom arrow A(Y) ⟶ A(X); φ_Y to the right of the left vertical arrow, as φ_X to the "
    "right of the right one (both scans)",
    "\\arrow[r,\"f^*\"'] (label below the arrow) and \\arrow[u,\"\\varphi_Y\"] (label to the left of an "
    "upward arrow)",
    "formula", "medium",
    {"old": "\\arrow[r,\"f^*\"'] \\arrow[u,\"\\varphi_Y\"]", "new": "\\arrow[r,\"f^*\"] \\arrow[u,\"\\varphi_Y\"']"},
    "Labels on the wrong side of their arrows (the f* of the p. 41 diagram was reported the same way). "
    "Independent of the next entry.")

add(59, "diagram of Corollaire 2, end",
    "a full stop to the right of A(X) (both scans)",
    "tikzcd without punctuation",
    "punctuation", "high",
    {"old": "\\arrow[u,\"\\varphi_X\"']", "new": "\\arrow[u,\"\\varphi_X\"'] ."},
    "Punctuation printed after a diagram; set in the last cell, as on p. 7 ('& K \\arrow[ul] .').")

# ---------------- page 60
add(60, "label 'Proposition 2.13 (\"décomposition cellulaire\")'",
    "Proposition 2.13 (\"décomposition cellulaire\") : Soit P ... (colon, no full stop, both scans)",
    "\\textbf{Proposition 2.13 (``décomposition cellulaire'').}",
    "punctuation", "medium",
    {"old": "cellulaire'').}", "new": "cellulaire'')~:}"},
    "As p. 57: the label's colon became a full stop.")

add(60, "N.B. after Proposition 2.13, 'j'ignore si les γ_P(V_{i,α}) forment une base'",
    "γ_P(V_{i;α}): a semicolon between i and α (both scans); b) of the statement has the comma",
    "$\\gamma_P(V_{i,\\alpha})$ (silently corrected)",
    "misprint_in_print", "medium",
    {"old": "ignore si les $\\gamma_P(V_{i,\\alpha})$", "new": "ignore si les $\\gamma_P(V_{i;\\alpha})$"},
    "Typing slip ; for , in the index; the corrected layer reads V_{i,\\alpha}.",
    corrected="ignore si les $\\gamma_P(V_{i,\\alpha})$")

add(60, "end of page: statement of Théorème 2.14",
    "p. 60 ends with the first five lines of the statement of Théorème 2.14, up to 'lorsque l'on substitue "
    "dans R aux x_i des éléments ξ_i et aux E_j des éléments η_j de'; p. 61 begins 'Ã soumis aux "
    "restrictions' (both scans; DjVu witness pp. 71-72)",
    "page_060.tex ends with '\\textbf{Théorème 2.14.}' and the folio-61 marker follows it, so the statement "
    "'\\emph{Soient $x_i$ ... des éléments $\\eta_j$ de' stands under the folio-61 marker",
    "marker", "high", None,
    "Page 61 really begins with '$\\Atil$ soumis aux restrictions'. Move the folio-61 marker down, inside "
    "the \\emph group: python -I move_marker.py 6 61 '$\\Atil$ soumis aux restrictions' (forward search; "
    "simulated on both layers: '... aux $E_j$ des éléments $\\eta_j$ de ' / marker / '$\\Atil$ soumis aux "
    "restrictions ...'). The moved text agrees with the print of p. 60 (checked here).")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (B / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1 or "%%%%%%%%%%" in d["fix"]["old"]:
        ok = False
    print(d["page"], n, repr(d["fix"]["old"]))
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("ALL UNIQUE" if ok else "PROBLEM", counts, len(F))
json.loads(OUT.read_text(encoding="utf-8"))
