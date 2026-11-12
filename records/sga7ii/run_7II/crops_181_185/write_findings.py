import json
import sys

BATCH = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b181_185"
OUT = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_181_185.json"

findings = [
    {
        "page": 181,
        "where": "tag of the two-row diagram at the top of the page",
        "scan": "(2.1 7.1)",
        "tex": "\\tag{2.1 7.1}",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\tag{2.1.7.1}",
        "note": "The display belongs to paragraph 2.1.7 (page 180). The print leaves the character slot between '1' and '7' blank, with no trace of a dot, whereas the other dots of the tag are fully inked. The TeX keeps the printed reading."
    },
    {
        "page": 181,
        "where": "number of the lemma before 2.2 (Lemme 2.7.8.)",
        "scan": "Lemme 2.7.8.",
        "tex": "\\underline{Lemme} 2.7.8.",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{Lemme} 2.1.8.",
        "note": "Wrong number in the print: the lemma follows 2.1.7 and precedes 2.2, and the proof of 2.2.7 cites it as 'Appliquons 2.1.8.' (page 187). The TeX keeps the printed reading."
    },
    {
        "page": 182,
        "where": "first display, Q(x) = ...",
        "scan": "Q(x) with the x in bold type and underlined",
        "tex": "Q(\\underline{x})",
        "kind": "font",
        "confidence": "medium",
        "fix": {"old": "Q(\\underline{x})", "new": "Q(\\underline{\\mathbf{x}})"},
        "note": "The underlined x is visibly heavier than the plain x's of the same line (about 133 dark pixels against 88-103 for x_i, x_j). The TeX gives the underline but not the bold."
    },
    {
        "page": 182,
        "where": "Si E^{n+1}_S est le complement ..., alors X se deduit de la quadratique X_1",
        "scan": "de la quadratique X_1 de P^{n+1}_S",
        "tex": "de la quadratique $X_1$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "de la quadrique $X_1$",
        "note": "The print says 'quadratique' as a noun for the projective quadric X_1; the same page calls these objects 'quadrique' ('Y est une quadrique lisse', 'la quadrique X'_s'). Probably a slip for 'quadrique'. The TeX keeps the printed reading."
    },
    {
        "page": 182,
        "where": "hypothesis (b): la quadrique X'_s est singuliere",
        "scan": "X'_s (typed apostrophe after X)",
        "tex": "$X'_s$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "$X_s$",
        "note": "The apostrophe is really typed. No X' is defined in 2.1-2.2, and the next sentence speaks of 'le point singulier de X_s'. It is probably a stray keystroke for X_s. The TeX keeps the printed reading."
    },
    {
        "page": 184,
        "where": "item 1): on a psi(Lambda) = Lambda  De plus, ...",
        "scan": "= Λ   De plus, (no full stop)",
        "tex": "= \\Lambda$    De plus",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "= \\Lambda$ .    De plus",
        "note": "The full stop ending the sentence is missing in the print; the gap between 'Λ' and 'De' is blank with no trace of a dot. The TeX keeps the printed reading."
    },
    {
        "page": 184,
        "where": "heading B (B  Cohomologie a support dans x_o .)",
        "scan": "B   Cohomologie à support dans (no full stop after B)",
        "tex": "\\underline{B\\quad",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\underline{B.\\quad",
        "note": "The other headings read 'A.', 'C.', 'D.', 'E.', 'F.'; after 'B' the print has a blank slot with no trace of a dot. The TeX keeps the printed reading."
    },
    {
        "page": 184,
        "where": "end of C (Il resulte de la dualite de Poincare ...): second module of the perfect pairing",
        "scan": "H^n_{x_o}(X_s,Rψ_η̄(Λ(n)) .  (only two closing parentheses)",
        "tex": "(\\Lambda(n))$ .",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "(\\Lambda(n)))$ .",
        "note": "The print omits the parenthesis that closes (X_s, ...; the same group earlier on the page is written with three closing parentheses. The TeX keeps the printed reading."
    },
    {
        "page": 184,
        "where": "D: Soit phi l'application naturelle",
        "scan": "φ (open looped form)",
        "tex": "$\\phi$",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "$\\phi$", "new": "$\\varphi$"},
        "note": "The print has the looped φ, the same glyph that the transcription writes \\varphi on page 178 ('φ : f^*L → K'). Pages 184-185 alone write \\phi."
    },
    {
        "page": 185,
        "where": "formula (2.2.5.3)",
        "scan": "φ(δ) = (-1)^m.2.δ' (looped φ)",
        "tex": "\\phi(\\delta) = (-1)^m",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "\\phi(\\delta) = (-1)^m", "new": "\\varphi(\\delta) = (-1)^m"},
        "note": "Same looped φ as on page 184 and page 178 (where the TeX has \\varphi)."
    },
    {
        "page": 185,
        "where": "formula (2.2.5.8)",
        "scan": "φ(δ) = 0 (looped φ)",
        "tex": "\\phi(\\delta) = 0",
        "kind": "symbol",
        "confidence": "medium",
        "fix": {"old": "\\phi(\\delta) = 0", "new": "\\varphi(\\delta) = 0"},
        "note": "Same looped φ as in (2.2.5.3)."
    },
]

ok = True
for f in findings:
    path = "%s\\page_%03d.tex" % (BATCH, f["page"])
    with open(path, "r", encoding="utf-8", newline="") as fh:
        text = fh.read()
    checks = []
    if f["fix"] is not None:
        checks.append(("fix.old", f["fix"]["old"]))
    if f["kind"] == "misprint_in_print":
        checks.append(("tex", f["tex"]))
    for label, s in checks:
        n = text.count(s)
        # make sure the string does not cross a marker line
        crosses = "%%%%%%%%%%" in s
        status = "OK" if (n == 1 and not crosses) else "PROBLEM"
        if status != "OK":
            ok = False
        print("p%d %-8s count=%d %s  %r" % (f["page"], label, n, status, s))

if not ok:
    print("NOT WRITTEN: fix the problems first")
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("written", OUT, len(findings), "findings")
