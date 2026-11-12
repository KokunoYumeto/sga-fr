import json, os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
BATCH = os.path.join(RUN, "b356_360")
OUT = os.path.join(RUN, "findings_356_360.json")

CAP_NOTE = ("The superscript of the identity component is a small o in the print "
            "(x-height, same glyph as the subscript o); the TeX has a capital O. "
            "Elsewhere the file writes this superscript as a small o (pp. 356, 360).")


def cap(page, where, scan, tex, old, new):
    return {"page": page, "where": where, "scan": scan, "tex": tex,
            "kind": "symbol", "confidence": "high",
            "fix": {"old": old, "new": new}, "note": CAP_NOTE}


findings = [
    {"page": 356,
     "where": "4.2, sentence after the diagram (4.2.4): 'critère galoisien de réduction semi-stable (4.5)'",
     "scan": "critère galoisien de réduction semi-stable (4.5),",
     "tex": "critère galoisien de réduction semi-stable (4.5),",
     "kind": "misprint_in_print", "confidence": "high", "fix": None,
     "corrected": "(3.5)",
     "note": "Wrong reference number: the Galois criterion of semi-stable reduction is Proposition 3.5 "
             "(cited as (3.5) on p. 355 and as 3.5 in 5.2.6); 4.5 is the paragraph on the conductor. "
             "The TeX keeps the printed reading."},

    cap(357, "first paragraph, 'donc sur A*^o par automorphisme'", "A*^o (small o)", "$A^{*O}$",
        "donc sur} $A^{*O}$", "donc sur} $A^{*o}$"),
    cap(357, "first paragraph, 'U^ef = T_ℓ(A*^o)^f(K̄)'", "T_ℓ(A*^o)^f(K̄) (small o)", "T_{\\ell}(A^{*O})^{f}",
        "= T_{\\ell}(A^{*O})^{f}", "= T_{\\ell}(A^{*o})^{f}"),
    {"page": 357,
     "where": "first paragraph, 'l'action de π' sur U^ef ... est déduit par transport de structure'",
     "scan": "est déduit par transport de structure",
     "tex": "\\underline{est déduit par transport de structure de l'action de}",
     "kind": "misprint_in_print", "confidence": "medium", "fix": None,
     "corrected": "est déduite",
     "note": "Agreement error of the print: the subject is 'l'action'. The TeX keeps the printed reading."},
    cap(357, "first paragraph, '(A*^o/K', K̃')'", "(A*^o/K',K̃') (small o)", "(A^{*O}/K',\\widetilde{K}')",
        "(A^{*O}/K'", "(A^{*o}/K'"),
    {"page": 357,
     "where": "first paragraph, ', π' équivaut sur A* via G.'",
     "scan": "π' équivaut sur A* via G",
     "tex": "$\\pi'$ \\underline{équivaut sur} $A^*$ \\underline{via} $G$",
     "kind": "misprint_in_print", "confidence": "low", "fix": None,
     "corrected": "\\underline{opérant sur}",
     "note": "'équivaut sur A* via G' makes no sense; the clause says that π' acts on A* through its quotient G "
             "(absolute participle 'π' opérant sur A* via G', or 'opère'). The TeX keeps the printed reading. "
             "The emendation is conjectural."},
    cap(357, "(4.2.6)", "T_ℓ(A*^o)^f(K̄) ≃ T_ℓ(A*^o_o)(k̄) (small o twice)",
        "T_{\\ell}(A^{*O})^{f}(\\overline{K}) \\simeq T_{\\ell}(A^{*O}_{o})",
        "(A^{*O})^{f}(\\overline{K}) \\simeq T_{\\ell}(A^{*O}_{o})",
        "(A^{*o})^{f}(\\overline{K}) \\simeq T_{\\ell}(A^{*o}_{o})"),
    cap(357, "'On considère le schéma en groupes lisse connexe A*^o_o'", "A*^o_o (small o)", "$A^{*O}_{o}$",
        "connexe $A^{*O}_{o}$", "connexe $A^{*o}_{o}$"),
    cap(357, "'Le groupe quotient G de π' opère sur A*^o_o de façon compatible'", "A*^o_o (small o)", "$A^{*O}_{o}$",
        "$A^{*O}_{o}$ de façon", "$A^{*o}_{o}$ de façon"),
    cap(357, "'la situation (A*^o_o/k', k̄)'", "(A*^o_o/k',k̄) (small o)", "(A^{*O}_{o}/k',\\overline{k})",
        "(A^{*O}_{o}/k'", "(A^{*o}_{o}/k'"),
    cap(357, "unnumbered display 'U^ef = T_ℓ(A*^o_o)(k̄) ,'", "T_ℓ(A*^o_o)(k̄) (small o)", "T_{\\ell}(A^{*O}_{o})",
        "U^{ef} = T_{\\ell}(A^{*O}_{o})", "U^{ef} = T_{\\ell}(A^{*o}_{o})"),
    cap(357, "'opère sur A*^o_o par k'-automorphismes'", "A*^o_o (small o)", "$A^{*O}_{o}$",
        "$A^{*O}_{o}$ par $k'$", "$A^{*o}_{o}$ par $k'$"),
    cap(357, "'de Γ = I/I' sur T_ℓ(A*^o_o)(k̄) est la représentation'", "T_ℓ(A*^o_o)(k̄) (small o)", "$T_{\\ell}(A^{*O}_{o})(\\overline{k})$",
        "$T_{\\ell}(A^{*O}_{o})(\\overline{k})$ est", "$T_{\\ell}(A^{*o}_{o})(\\overline{k})$ est"),
    cap(357, "(4.2.7)", "U^ef ≃ T_ℓ(A*^o_o)(k̄) (small o)", "T_{\\ell}(A^{*O}_{o})",
        "\\subset U^{ef} \\simeq T_{\\ell}(A^{*O}_{o})", "\\subset U^{ef} \\simeq T_{\\ell}(A^{*o}_{o})"),

    cap(358, "first line, 'le plus grand sous-tore de A*^o_o'", "A*^o_o (small o)", "$A^{*O}_{o}$",
        "sous-tore de $A^{*O}_{o}$", "sous-tore de $A^{*o}_{o}$"),
    cap(358, "(4.2.8)", "B*_o = A*^o_o/T*_o (small o)", "A^{*O}_{o}/T^{*}_{o}",
        "= A^{*O}_{o}/T^{*}_{o}", "= A^{*o}_{o}/T^{*}_{o}"),
    cap(358, "'pour la partie abélienne de A*^o_o'", "A*^o_o (small o)", "$A^{*O}_{o}$",
        "abélienne de $A^{*O}_{o}$", "abélienne de $A^{*o}_{o}$"),
    cap(358, "'l'opération de G sur A*^o_o induit séparément'", "A*^o_o (small o)", "$A^{*O}_{o}$",
        "$A^{*O}_{o}$ induit", "$A^{*o}_{o}$ induit"),
    {"page": 358,
     "where": "after (4.2.11), '- caractère qui est trivial sur Γ^o .'",
     "scan": "Γ^o (small o superscript)",
     "tex": "$\\Gamma^{O}$",
     "kind": "symbol", "confidence": "high",
     "fix": {"old": "\\Gamma^{O}", "new": "\\Gamma^{o}"},
     "note": "The superscript is a small o in the print (x-height); the TeX has a capital O."},
    {"page": 358,
     "where": "after (4.2.11), '- caractère qui est trivial sur Γ^o .'",
     "scan": "trivial sur Γ^o",
     "tex": "trivial sur $\\Gamma^{O}$ (after the preceding fix: $\\Gamma^{o}$)",
     "kind": "misprint_in_print", "confidence": "low", "fix": None,
     "corrected": "$\\Gamma$",
     "note": "χ_ℓ factors through π_o = π'/Γ, so it is trivial on Γ; Γ = I/I' is finite, so a superscript o "
             "(identity component) gives nothing. The o looks like a stray. The TeX keeps the printed superscript."},

    {"page": 359,
     "where": "Théorème 4.3 b), 'la trace (et plus généralement tout coefficients du polynôme caractéristique) de'",
     "scan": "la trace underlined; '(' not underlined; 'et plus généralement tout coefficients du polynôme caractéristique' underlined; ')' not underlined; 'de' underlined",
     "tex": "\\underline{la trace (et plus généralement tout coefficients du polynôme caractéristique) de}",
     "kind": "underline", "confidence": "high",
     "fix": {"old": "\\underline{la trace (et plus généralement tout coefficients du polynôme caractéristique) de}",
             "new": "\\underline{la trace} (\\underline{et plus généralement tout coefficients du polynôme caractéristique}) \\underline{de}"},
     "note": "Neither parenthesis is underlined in the print (the underline stops after 'trace', restarts at 'et', "
             "stops after 'caractéristique' and restarts at 'de'); elsewhere the file keeps parentheses outside \\underline."},
    {"page": 359,
     "where": "Théorème 4.3 b), 'tout coefficients du polynôme caractéristique'",
     "scan": "tout coefficients",
     "tex": "tout coefficients",
     "kind": "misprint_in_print", "confidence": "medium", "fix": None,
     "corrected": "tout coefficient",
     "note": "Agreement error of the print ('tout' with a plural noun). The TeX keeps the printed reading."},
]

# verify every fix's "old" occurs exactly once in its page file, and does not touch a marker line
ok = True
for f in findings:
    if f["fix"] is None:
        continue
    path = os.path.join(BATCH, "page_%d.tex" % f["page"])
    text = open(path, encoding="utf-8").read()
    old = f["fix"]["old"]
    n = text.count(old)
    if n != 1 or "%%%%%%%%%%" in old:
        ok = False
    print(f["page"], n, repr(old))

# check that fixes on the same page do not overlap
from collections import defaultdict
spans = defaultdict(list)
for f in findings:
    if f["fix"] is None:
        continue
    text = open(os.path.join(BATCH, "page_%d.tex" % f["page"]), encoding="utf-8").read()
    i = text.find(f["fix"]["old"])
    spans[f["page"]].append((i, i + len(f["fix"]["old"])))
for p, s in spans.items():
    s.sort()
    for a, b in zip(s, s[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP on page", p, a, b)

# apply fixes to in-memory copies and confirm no capital-O superscripts remain
for p in (357, 358):
    text = open(os.path.join(BATCH, "page_%d.tex" % p), encoding="utf-8").read()
    for f in findings:
        if f["page"] == p and f["fix"] is not None:
            text = text.replace(f["fix"]["old"], f["fix"]["new"], 1)
    print(p, "remaining ^{*O}:", text.count("^{*O}"), "remaining ^{O}:", text.count("^{O}"))

print("ALL UNIQUE AND DISJOINT" if ok else "PROBLEM")
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
print("wrote", OUT, len(findings))
