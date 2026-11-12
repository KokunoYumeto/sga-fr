"""Write findings_021_025.json for the SGA 6 pp. 21-25 check and verify that every fix's old string occurs exactly
once in its page_NNN.tex.
usage: python -I make_findings.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(__file__).resolve().parent.parent
BATCH = RUN / "b021_025"
OUT = RUN / "findings_021_025.json"

F = []


def add(page, where, scan, tex, kind, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "confidence": confidence, "fix": fix}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 21
add(21, "chapter title line under 'CHAPITRE I'",
    "λ-Anneaux (Préliminaires formels), the word 'Anneaux' underlined (not the λ-), both scans",
    r"$\lambda$-Anneaux (Préliminaires formels)",
    "underline", "medium",
    {"old": r"$\lambda$-Anneaux (Préliminaires formels)",
     "new": r"$\lambda$-\underline{Anneaux} (Préliminaires formels)"},
    "The centred title line has no underline in the TeX. \\underline as in the applied Exposé 0 heading fix "
    "(this exposé's running text writes its underlines \\emph).")

add(21, "heading '§ 1. Définitions'",
    "§ 1. Définitions, the word 'Définitions' underlined, both scans",
    r"\subsection*{\S 1. Définitions}",
    "underline", "low",
    {"old": r"\subsection*{\S 1. Définitions}", "new": r"\subsection*{\S 1. \underline{Définitions}}"},
    "Same question as the Exposé 0 heading of p. 1 (applied): the print underlines the title word of its § headings "
    "(also § 2. Exemples, p. 24); none of the 7 \\subsection*{\\S ...} of main.tex has an underline. Apply with the "
    "volume's decision on underlined headings.")

add(21, "line before (1.3)",
    "Posons, pour tout x ∈ K (no punctuation after K, both scans)",
    r"Posons, pour tout $x\in K$,",
    "punctuation", "high",
    {"old": r"Posons, pour tout $x\in K$,", "new": r"Posons, pour tout $x\in K$"},
    "The TeX adds a comma before the display (1.3).")

add(21, "end of the paragraph after (1.3), 'relevant l'homomorphisme canonique ...'",
    "nique 1 + Σ_{i>0} x_i t^i ⟶ x_1. in the running text, on the same line as 'nique' (both scans)",
    r"\[ 1+\sum_{i>0}x_it^i\longrightarrow x_1. \] (a display)",
    "other", "medium",
    {"old": "canonique\n\\[\n1+\\sum_{i>0}x_it^i\\longrightarrow x_1.\n\\]",
     "new": "canonique $1+\\sum_{i>0}x_it^i\\longrightarrow x_1$."},
    "The print sets the map inline at the end of the sentence; the TeX makes it a display (same kind of fix as "
    "7 II p. 414, applied). The paragraph break before 'Ainsi' stays.")

add(21, "footnote (*), last line",
    "de la page 3 (cf V 2.4). (no full stop after cf, both scans)",
    r"(cf. V 2.4)",
    "punctuation", "high",
    {"old": r"(cf. V 2.4)", "new": r"(cf V 2.4)"},
    "The TeX adds the abbreviation's full stop. The footnotes of pp. 24-25 print 'cf.' with it.")

# ---------------------------------------------------------------- page 22
add(22, "start of page",
    "p. 22 begins with the display '(1.4) λ_t(1) = 1 + t .', then 'On a alors' (both scans); p. 21 ends with "
    "'sa structure d'anneau et telle que' and the footnote",
    "the display (1.4) (\\begin{equation}\\tag{1.4} ... \\end{equation}) is the end of page_021.tex, under the "
    "folio-21 marker; page_022.tex begins 'On a alors'",
    "marker", "high", None,
    "Page 22 really begins with the display (1.4). Move the folio-22 marker above it: "
    "python -I move_marker.py 6 22 \"\\begin{equation}\\tag{1.4}\" --before (simulated on both layers: "
    "'... et telle que', marker, \\begin{equation}\\tag{1.4}, ..., 'On a alors'). fix_markers_ocr.py could not "
    "catch it: the line before the marker is \\end{equation}.")

add(22, "end of the paragraph after (1.7), before 'De même, les λ^i(f)'",
    "'De même, les λ^i(f) sont déterminés ...' starts at the margin, not indented (both scans): the print runs on; "
    "the line before ends at '(b_i).' because 'De même,' did not fit",
    "blank line (new paragraph) before 'De même'",
    "other", "low",
    {"old": "$b=(b_i)$.\n\nDe même", "new": "$b=(b_i)$. De même"},
    "The typescript indents its new paragraphs (p. 22 'La notion', 'Pour définir'); same case as the pilot's p. 3 "
    "'Une première filtration' (applied).")

# ---------------------------------------------------------------- page 23
add(23, "start of page",
    "p. 23 begins 'les coefficients c_n(λ^i(f)) = c_n de λ^i(f) se calculent' (both scans)",
    "'les' is the last word of page_022.tex ('... par la condition que les', under the folio-22 marker); "
    "page_023.tex begins 'coefficients'",
    "marker", "high", None,
    "Page 23 really begins with 'les'. Move the folio-23 marker before that word: "
    "python -I move_marker.py 6 23 \"les\" --before (it takes the last 'les' before the marker, the line's final "
    "word; simulated on both layers: '... par la condition que ', marker, 'les', 'coefficients ...').")

add(23, "(1.7 bis)",
    "(1 + at) ∘ f = f(at) (no full stop, both scans)",
    r"(1+at)\circ f=f(at).",
    "punctuation", "high",
    {"old": r"(1+at)\circ f=f(at).", "new": r"(1+at)\circ f=f(at)"},
    "The TeX adds a full stop at the end of the display.")

add(23, "'si l'homomorphimse additif λ_t de K dans 1 + K[[t]]^+'",
    "homomorphimse (both scans)",
    "homomorphimse (printed reading kept)",
    "misprint_in_print", "high", None,
    "Transposed letters in the print; the TeX keeps them; the corrected layer already reads 'homomorphisme'.",
    corrected="homomorphisme")

add(23, "(1.10), third formula",
    "λ_t(λ^i(x)) = λ^i(λ_t(x) , (one closing parenthesis missing, both scans)",
    r"\lambda_t(\lambda^i(x))=\lambda^i(\lambda_t(x), (printed reading kept)",
    "misprint_in_print", "high", None,
    "Unbalanced parentheses in the print; the TeX keeps them; the corrected layer already closes them.",
    corrected=r"\lambda_t(\lambda^i(x))=\lambda^i(\lambda_t(x))")

add(23, "(1.11), end of the first row",
    "λ^i(1) = 0   si i ⩾ 1 (no punctuation, both scans)",
    r"\text{si }i>1,\\",
    "punctuation", "high",
    {"old": ",\\\\\n\\lambda^n(xy)", "new": "\\\\\n\\lambda^n(xy)"},
    "The TeX adds a comma at the end of the first row of the cases. Listed before the misprint fix of the same row; "
    "the two old strings do not overlap.")

add(23, "(1.11), first row, condition",
    "si i ⩾ 1 (a slanted greater-or-equal sign, unlike the typed > of 'pour i > 1' before (1.9); both scans)",
    r"\text{si }i>1",
    "misprint_in_print", "high",
    {"old": r"\text{si }i>1", "new": r"\text{si }i\geq 1"},
    "λ_t(1) = 1 + t gives λ^1(1) = 1, so the condition is i > 1 (as for (1.9)); the print has ⩾ and the TeX "
    "silently corrects. The corrected layer already reads i>1.",
    corrected=r"\text{si }i>1")

add(23, "(1.11), end of the second row",
    "λ^n(xy) = P_n(λ^1x,...,λ^nx;λ^1y,...,λ^ny) (no punctuation, both scans); only the third row ends with a comma",
    r"\lambda^n y),\\",
    "punctuation", "high",
    {"old": "\\lambda^n y),\\\\", "new": "\\lambda^n y)\\\\"},
    "The TeX adds a comma at the end of the second row of the cases.")

add(23, "(1.11), third row, last argument",
    "λ^n(λ^i(x)) = P_{i,n}(λ^1x,...,λ^nx) (exponent n on the last λ, both scans)",
    r"P_{i,n}(\lambda^1x,\ldots,\lambda^n x) (printed reading kept)",
    "misprint_in_print", "medium", None,
    "By (1.8), c_n(λ^i(f)) = P_{i,n}(a_1,...,a_{in}); with f = λ_t(x), a_j = λ^j x, so the last argument is "
    "λ^{in} x. The TeX keeps the printed reading; the corrected layer still has \\lambda^n x.",
    corrected=r"P_{i,n}(\lambda^1x,\ldots,\lambda^{in} x)")

# ---------------------------------------------------------------- page 24
add(24, "heading '§ 2. Exemples'",
    "§ 2. Exemples, the word 'Exemples' underlined, both scans",
    r"\subsection*{\S 2. Exemples}",
    "underline", "low",
    {"old": r"\subsection*{\S 2. Exemples}", "new": r"\subsection*{\S 2. \underline{Exemples}}"},
    "As § 1 (p. 21): apply with the volume's decision on underlined headings.")

add(24, "example 1), 'où ρ est une présentation extension de ρ' par ρ''",
    "présentation (both scans)",
    "présentation (printed reading kept)",
    "misprint_in_print", "high", None,
    "The print drops the 're' of 'représentation'; the TeX keeps it; the corrected layer already reads "
    "'représentation'.",
    corrected="représentation")

add(24, "paragraph 'Lorsque k est un corps ...', first 'spécial'",
    "est un λ-anneau spécial ; with 'spécial' underlined (both scans)",
    r"est un $\lambda$-anneau spécial~;",
    "underline", "high",
    {"old": r"est un $\lambda$-anneau spécial~;", "new": r"est un $\lambda$-anneau \emph{spécial}~;"},
    "The second 'spécial' of the paragraph ('est encore un λ-anneau spécial.') is not underlined, as in the TeX.")

add(24, "'mais cependant si k est algébriquement clos (*), K_r(G) est encore'",
    "a second call (*) of the same footnote after 'algébriquement clos' (both scans)",
    r"si $k$ est algébriquement clos, $\underline{K}_r(G)$ est encore",
    "missing", "high",
    {"old": r"algébriquement clos, $\underline{K}_r(G)$ est encore",
     "new": r"algébriquement clos\footnotemark[\value{footnote}], $\underline{K}_r(G)$ est encore"},
    "The footnote 'Il est inutile que k soit algébriquement clos ...' is called twice on the page; the TeX has only "
    "the first call. \\footnotemark[\\value{footnote}] repeats the mark of the last footnote (a form main.tex "
    "already uses).")

# ---------------------------------------------------------------- page 25
add(25, "footnote (1), 'l'ensemble des classes de représentations d'une algébre de Lie'",
    "algébre with an acute accent ('théorème' two lines below has the grave; both scans)",
    "algébre (printed reading kept)",
    "misprint_in_print", "high", None,
    "Wrong accent in the print; the TeX keeps it; the corrected layer still reads 'algébre'.",
    corrected="algèbre")

# ---------------------------------------------------------------- checks
ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = (BATCH / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", d["page"], n, repr(d["fix"]["old"]))
    if "%%%%%%%%%%" in d["fix"]["old"]:
        ok = False
        print("CROSSES A MARKER", d["page"], repr(d["fix"]["old"]))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0])
    c[1 if d["kind"] == "misprint_in_print" else 0] += 1
print("written", OUT, len(F), "findings; all olds unique" if ok else "CHECK FAILED")
print({p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})
