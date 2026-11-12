import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
FOLDER = os.path.join(RUN, "b201_205")
OUT = os.path.join(RUN, "findings_201_205.json")

findings = [
    {
        "page": 203,
        "where": "3rd line of the page: 'Pour un torseur E sous G_P, la donnée d'une tri-'",
        "scan": "G_P (capital P as subscript; same glyph as the G_P subscripts on p. 201, unlike the round-bowled small p of 'λp' on the line)",
        "tex": "$G_p$",
        "kind": "symbol",
        "confidence": "high",
        "fix": {"old": "sous $G_p$", "new": "sous $G_P$"},
        "note": "G_p where the print has G_P.",
    },
    {
        "page": 204,
        "where": "formula (3.6.3), right-hand side",
        "scan": "Ψ̲_{L.(P',Q')}",
        "tex": r"\underline{\Psi}_{L.(P',Q')}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\underline{\Psi}_{L'.(P,Q)}",
        "note": "The print puts the primes on P and Q instead of on L. By (3.6.2), L.(P,Q) -> L'.(P,Q) is an isomorphism in dimensions <= 2, and Théorème 3.6.4 states Ψ_{L.(P,Q)} = Ψ_{L'.(P,Q)}. The TeX keeps the printed reading.",
    },
    {
        "page": 204,
        "where": "'une résolution plate L'.(P) de P, coîncident en dimension ≤ 2 avec le complexe augmenté'",
        "scan": "coîncident",
        "tex": "coïncident",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "coïncidant",
        "note": "A participle with complements is needed (the parallel sentence three lines below prints 'coîncidant avec L.(Q)'); an adjective would have to agree with 'résolution'. The TeX keeps the printed '-ent'. The î/ï accent is the global convention and is not at issue.",
    },
    {
        "page": 205,
        "where": "'Ainsi, une extension de L_o(P×Q) par G s'identifie à un torseur sous G_{P×Q}'",
        "scan": "L_o(P×Q)",
        "tex": r"$L_o(P\times Q)$",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "$L_o(P,Q)$",
        "note": "The sentence goes through the components L_i(P,Q), i=0,1,2 ('L_1(P,Q)', 'L_2(P,Q)', and 'L_o(P,Q)' a few lines later), so P×Q is probably a slip for P,Q. The slip is harmless: L_o(P×Q) = Z[P×Q] = L_o(P,Q) by (3.6.6). The TeX keeps the printed reading.",
    },
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# Check: every fix's "old" occurs exactly once in its page file; misprint "tex" also located once.
ok = True
for f in findings:
    path = os.path.join(FOLDER, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if f["fix"] is not None:
        n = text.count(f["fix"]["old"])
        print(f["page"], "fix.old count =", n, repr(f["fix"]["old"]))
        ok &= (n == 1)
    else:
        n = text.count(f["tex"])
        print(f["page"], "tex count =", n, repr(f["tex"]))
        ok &= (n == 1)

with open(OUT, encoding="utf-8") as fh:
    json.load(fh)
print("JSON valid; all unique:", ok)
