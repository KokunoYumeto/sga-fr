import json
import re
import sys

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
OUT = BASE + r"\findings_086_090.json"


def tex(p):
    with open(rf"{BASE}\b086_090\page_{p:03d}.tex", encoding="utf-8", newline="") as f:
        return f.read()


T = {p: tex(p) for p in range(86, 91)}

# p. 86: the (2) display, all nine bars missing
seq2_tex = (
    "0 \\to D^0(A\\;R, M) \\to D^0(A\\;S, M) \\to D^0(R\\;S, M) \\to D^1(A\\;R, M) \\to\\\\\n"
    "D^1(A\\;S, M) \\to D^1(R\\;S, M) \\to\\; ........ \\;\\to D^n(A\\;R, M) \\to\\\\\n"
    "D^n(A\\;S, M) \\to D^n(R\\;S, M) \\to \\;...."
)
seq2_corr = seq2_tex.replace("A\\;R", "A|R").replace("A\\;S", "A|S").replace("R\\;S", "R|S")

# p. 87: the speck after (7), exact run of spaces taken from the file
m = re.search(r"type\}\.( +)\.", T[87])
dot_old = m.group(0)

F = [
    {
        "page": 86,
        "where": "Theorem 3.12 (2), the exact sequence of S -> R -> A (all three lines of the display)",
        "scan": "0 -> D^0(A R, M) -> D^0(A S, M) -> D^0(R S, M) -> D^1(A R, M) -> ... -> D^n(R S, M) -> ....: no vertical bar in any of the nine terms, only a blank (clean gaps in a crop); the bars in the display of (1) and in (3)-(5) are drawn",
        "tex": seq2_tex,
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": seq2_corr,
        "note": "The inked bars were never drawn in this display. The terms are D^n(A|R, M), D^n(A|S, M), D^n(R|S, M), as in (1) and in the exact sequence of 3.7(c) that the proof of (2) on p. 87 applies. The TeX keeps the printed gaps (A\\;R). 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 87,
        "where": "Theorem 3.12 (7), 'then D^i(A|R, M) is A-module of finite type for all i'",
        "scan": "is A-module (no article)",
        "tex": "\\underline{is} $A$-\\underline{module of finite type for all}",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "\\underline{is an} $A$-\\underline{module of finite type for all}",
        "note": "Article missing; the same sentence ends 'provided M is an A-module of finite type'. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 87,
        "where": "Theorem 3.12 (7), end of the line 'an A-module of finite type.'",
        "scan": "a speck near the right margin, about a quarter of the size of the typed full stop after 'type' (5 x 4 px against 9 x 10 px in the scan, measured in a crop)",
        "tex": dot_old,
        "kind": "extra",
        "confidence": "medium",
        "fix": {"old": dot_old, "new": "type}."},
        "note": "The TeX sets the speck as a second full stop after a run of spaces. The sentence ends with the typed full stop after 'type'.",
    },
    {
        "page": 87,
        "where": "Theorem 3.12 (8), display, first line 'D^1(A|R, M) = Coker(Der_R(P, M) -> Hom_A(I/I^2, M)'",
        "scan": "Hom_A(I/I^2, M) and nothing after it: one closing parenthesis, so the parenthesis opened after Coker is never closed (checked in a crop)",
        "tex": "\\mathrm{Hom}_A(I/I^2, \\ M))",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "(I/I^2, \\ M))", "new": "(I/I^2, \\ M)"},
        "corrected": "(I/I^2, \\ M))",
        "note": "The D^2 line of the same display and the same cokernel in the proof of (8) on p. 89 close both parentheses. The TeX silently corrects it; the fix restores the printed reading. 'corrected' is the current TeX.",
    },
    {
        "page": 89,
        "where": "Proof of 3.12 (8), 'where I -> M is uniquely determined by the extensions A' up to Der_R(P, M)'",
        "scan": "by the extensions A'",
        "tex": "by the extensions  $A'$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "by the extension  $A'$",
        "note": "A' is the single extension 0 -> M -> A' -> A -> 0 of the sentence before. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 89,
        "where": "Proof of 3.12 (8), 'Two P-linear maps I => M which differ by Der_R(P, M) is trivially seen to yield isomorphic extensions'",
        "scan": "Two P-linear maps ... is trivially seen",
        "tex": "is trivially seen to yield",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "are trivially seen to yield",
        "note": "Verb agreement slip (plural subject). Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 89,
        "where": "Proof of 3.12 (8), last line 'It is straightforward to verify that Phi, Psi are inverse process to each other.'",
        "scan": "are inverse process to each other",
        "tex": "are inverse process to each other",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "are inverse processes to each other",
        "note": "Number slip (two maps, singular noun). Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 89,
        "where": "Corollary 3.13 (a), '(a) R-algebra A is formally smooth over R'",
        "scan": "(a)  R-algebra  A : no article ('algebra' underlined)",
        "tex": "(a)  R-\\underline{algebra}",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "(a)  \\underline{An} R-\\underline{algebra}",
        "note": "Article missing at the start of the statement. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 89,
        "where": "Corollary 3.13 (c), last line 'D^i(S^-1 A|R, S^-1 M) ~-> S^-1 D^i(A|R, M) for all i >= 0 .'",
        "scan": "for all : two underlined words",
        "tex": "\\underline{for all} inside equation*",
        "kind": "font",
        "confidence": "high",
        "fix": {"old": "\\underline{for all}", "new": "\\underline{\\text{for all}}"},
        "note": "In math mode the words become the italic letters f, o, r, a, l, l with the space dropped ('forall'). The file's own form for underlined words in a display is \\underline{\\text{...}} (p. 87, display of (8)).",
    },
    {
        "page": 90,
        "where": "Proof of 3.13 (b), 'is surjective for all A-module M'",
        "scan": "for all A-module M",
        "tex": "is surjective for all A-module",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "is surjective for all A-modules",
        "note": "Number slip; the sentence before reads 'for every A-module M'. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 90,
        "where": "Proof of 3.13 (d), display 'D^i(A R, A^ (x)_A E) ~-> A^ (x)_A D^i(A|R, E)'",
        "scan": "D^i(A R, ...: a blank between A and R, no bar (clean in a crop)",
        "tex": "D^i(A R, \\ \\hat{A}",
        "kind": "other",
        "confidence": "low",
        "fix": {"old": "D^i(A R, \\ \\hat{A}", "new": "D^i(A\\;R, \\ \\hat{A}"},
        "note": "In math mode the space is dropped, so the TeX sets 'AR' where the print has a gap. p. 86 writes the same printed gaps as A\\;R. Goes with the next entry: its 'tex' is the text after this fix.",
    },
    {
        "page": 90,
        "where": "Proof of 3.13 (d), same display, first term",
        "scan": "D^i(A R, A^ (x)_A E): the bar between A and R is missing; the right-hand D^i(A|R, E) has its inked bar",
        "tex": "D^i(A\\;R, \\ \\hat{A}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "D^i(A|R, \\ \\hat{A}",
        "note": "3.12(6) with the flat A-module A^ gives A^ (x)_A D^i(A|R, E) ~-> D^i(A|R, A^ (x)_A E). The TeX keeps the printed gap. 'corrected' replaces the 'tex' substring after the previous entry's fix; before that fix the substring reads D^i(A R, \\ \\hat{A}.",
    },
]

ok = True
for e in F:
    t = T[e["page"]]
    if e["fix"] is not None:
        n = t.count(e["fix"]["old"])
        if n != 1:
            ok = False
            print("OLD NOT UNIQUE", e["page"], n, repr(e["fix"]["old"]))
        if "%%%%%%%%%%" in e["fix"]["old"]:
            ok = False
            print("OLD CROSSES MARKER", e["page"])
    # descriptive tex substrings present in the file (except post-fix ones)
    probe = e["tex"].replace(" inside equation*", "")
    if probe not in t and not (e["page"] == 90 and "A\\;R" in probe):
        print("TEX not found (descriptive)", e["page"], repr(probe))

if not ok:
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
print("written", len(F))
