import json
import os

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
BATCH = os.path.join(RUN, "b301_305")
OUT = os.path.join(RUN, "findings_301_305_recheck.json")

findings = [
    {
        "page": 301,
        "where": "7.1 b), proof: 'La pleine fidèlité du foncteur envisagé équivaut à la relation'",
        "scan": "fidèlité (grave accent on the first e)",
        "tex": "fidèlité",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "fidélité",
        "note": "Spelling slip of the typescript ('fidèlité' for 'fidélité'); the TeX keeps the printed reading.",
    },
    {
        "page": 302,
        "where": "end of the proof of 7.1: 'à Hom(Φ⊗Ψ, Q/ℤ) en vertu de 5.6'",
        "scan": "Hom(Φ⊗Ψ, Q/ℤ ): the Q is a plain typed Q, the ℤ next to it double-struck",
        "tex": r"\Psi, Q/\mathbb{Z})",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": r"\Psi, \mathbb{Q}/\mathbb{Z})",
        "note": "The typist used a plain Q where the rational numbers are meant (double-struck Q in (7.1.6), (7.2.1), (7.3.1.1), (7.3.2.3)); the TeX keeps the printed plain Q.",
    },
    {
        "page": 303,
        "where": "Remarque 7.2, proof of the reduced assertion: 'en utilisant le fait que pourtout S-schéma lisse X'",
        "scan": "pourtout (typed without a space; the r-t gap is a normal letter gap, not a word space)",
        "tex": "pourtout",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "pour tout",
        "note": "Missing word space in the print; the TeX keeps the printed reading.",
    },
    {
        "page": 304,
        "where": "after (7.3.1.1): 'De même, si on des morphismes de schémas en groupes lisses sur S'",
        "scan": "si on des morphismes",
        "tex": "si on des morphismes",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "si on a des morphismes",
        "note": "The verb 'a' is missing in the print; the TeX keeps the printed reading.",
    },
    {
        "page": 305,
        "where": "(7.3.2.3), target of d(E_η)",
        "scan": "Hom(Ψ,ℚ/ℤ )_k)) (Hom underlined): two parentheses opened (after Ker and Hom), three closed",
        "tex": r"(\Psi ,\mathbb{Q}/\mathbb{Z} )_k))",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"(\Psi ,(\mathbb{Q}/\mathbb{Z} )_k))",
        "note": "The opening parenthesis of (ℚ/ℤ)_k is missing in the print (the text just above has Hom(Ψ, (ℚ/ℤ)_k)); the TeX keeps the printed reading.",
    },
]

# uniqueness checks: every fix 'old' and every 'tex' must occur exactly once in its page file
ok = True
for f in findings:
    path = os.path.join(BATCH, "page_%03d.tex" % f["page"])
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    for key, s in (("tex", f["tex"]), ("fix.old", (f["fix"] or {}).get("old"))):
        if s is None:
            continue
        n = text.count(s)
        print(f["page"], key, repr(s), n)
        if n != 1:
            ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("written", OUT, "all unique" if ok else "UNIQUENESS PROBLEM")
