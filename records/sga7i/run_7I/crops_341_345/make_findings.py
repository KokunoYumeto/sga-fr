import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
OUT = os.path.join(RUN, "findings_341_345_recheck.json")

findings = [
    {
        "page": "341",
        "where": "first line after the diagram (2.5.4)",
        "scan": "où les entiers 2α, 2λ, μ désignent les rangs du quotients de deux modules consécutifs",
        "tex": "désignent les rangs du quotients de deux modules",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "les rangs des quotients",
        "note": "Typing error in the print: singular 'du' before plural 'quotients' (checked in a crop). The TeX keeps the printed reading. 'des quotients' agrees with 'les rangs'; 'du quotient' would also be grammatical.",
    },
    {
        "page": "341",
        "where": "formula (2.5.5)",
        "scan": "rang V/V ∩ V^⊥ = rang V/W = 2λ ,",
        "tex": "\\mathrm{rang}\\ V/V \\cap V^{\\perp} \\;=\\; \\mathrm{rang}\\ V/W = 2\\lambda",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\mathrm{rang}\\ V^{\\perp}/V \\cap V^{\\perp} \\;=\\; \\mathrm{rang}\\ V^{\\perp}/W = 2\\lambda",
        "note": "As printed, (2.5.5) contradicts the sentence just above ('V/W soit de rang 2α') and the diagram (2.5.4), where W→V is labelled 2α and W→V^⊥ is labelled 2λ. The formula still to be derived from (2.1.10) and the rank of U is rang V^⊥/W = 2λ (its dual being rang W^⊥/V = 2λ): the hand-added ⊥ is missing on both numerators V (checked in a crop). The TeX keeps the printed reading.",
    },
    {
        "page": "341",
        "where": "end of the parenthesis after (2.5.5)",
        "scan": "compte tenu de (2.1.10) et de rang U = n.)",
        "tex": "et de rang $U = n$.)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "rang $U = 2n$",
        "note": "U = T_ℓ(A(K̄)) has rank 2 dim A_K = 2n, n = dim A_K being fixed in (2.1.9): the four steps of (2.5.4) give μ + 2α + 2λ + μ = 2n by (2.1.10), and rang V^⊥/W = 2λ follows from (2.1.10) only with rang U = 2n. The print has 'n' with no 2 (checked in a crop); the TeX keeps the printed reading.",
    },
    {
        "page": "343",
        "where": "Proposition 3.1, last sentence of the hypotheses",
        "scan": "Soient s ∈ S, t ∈ S une générisation de S, p l'exposant",
        "tex": "\\underline{une générisation de} $S$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\underline{une générisation de} $s$",
        "note": "t is a generization of the point s (cf. (3.1.1), (3.1.2) and e): 'S irréductible de point générique t'); the print has a capital S (checked in a crop). The TeX keeps the printed reading.",
    },
    {
        "page": "344",
        "where": "Démonstration a), 'qui est retrocompact dans _nG'",
        "scan": "qui est retrocompact dans _nG",
        "tex": "qui est retrocompact dans",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "rétrocompact",
        "note": "Accent missing on the EGA term 'rétrocompact' (the typescript types é everywhere else on the page). The TeX keeps the printed spelling.",
    },
    {
        "page": "345",
        "where": "Démonstration b), fourth line",
        "scan": "(3.1.1) s'obtiennent en élévant n respectivement",
        "tex": "s'obtiennent en élévant $n$ respectivement",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "élevant",
        "note": "Spelling error in the print (élever gives élevant); the second accent is clear in a crop. The TeX keeps the printed reading.",
    },
    {
        "page": "345",
        "where": "Démonstration c), first line",
        "scan": "Comme l'hypothèse (K_t̄)^o_s unipotent équivaut",
        "tex": "$(K_{\\overline{t}})^{o}_{s}$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "$(K_{\\overline{t}})^{o}_{\\mathrm{red}}$",
        "note": "Subscript s typed where 'red' is meant: the hypothesis of 3.1 c) is '(K_t̄)^o_red est unipotent', and d) below writes (K_s̄)^o_red. The print has a single letter s (checked in a crop); the TeX keeps it.",
    },
    {
        "page": "345",
        "where": "Démonstration e), first line",
        "scan": "Pour la premier assertion",
        "tex": "Pour la premier assertion",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Pour la première assertion",
        "note": "Agreement error in the print; the TeX keeps the printed reading.",
    },
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# checks: every non-null fix 'old' occurs exactly once; every 'tex' occurs in its page file
problems = 0
for f in findings:
    path = os.path.join(RUN, "b341_345", "page_%s.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    if f["fix"] is not None:
        n = text.count(f["fix"]["old"])
        if n != 1:
            problems += 1
            print("FIX OLD count", n, f["page"], f["where"])
    if f["tex"] not in text:
        problems += 1
        print("TEX not found", f["page"], f["where"])
    if text.count(f["tex"]) != 1:
        print("note: tex occurs", text.count(f["tex"]), "times on", f["page"], f["where"])
print("written", OUT, "entries", len(findings), "problems", problems)
