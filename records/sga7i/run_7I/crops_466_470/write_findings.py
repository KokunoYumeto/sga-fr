import json

B = chr(92)  # backslash; written as @ in the strings below


def t(s):
    return s.replace("@", B)


out = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/findings_466_470_recheck.json"
base = "C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b466_470"

findings = [
    {
        "page": 467,
        "where": "NB in b): 'ce qui donne un sens à O_X(X_i^o)'",
        "scan": "O_X(X^o_i): superscript o, subscript i",
        "tex": t("$@underline{O}_X(X_i^o)$"),
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": t("@underline{O}_X(X_o^i)"),
        "note": "The print swaps the indices of the component X_o^i, which the same sentence writes twice just before (O_X(X_o^i), les cycles X_o^i). The TeX keeps the printed reading.",
    },
    {
        "page": 467,
        "where": "c): 'i.e. satisfait la propriété universelle (1.1.2) en termes de sa fibre spéciale'",
        "scan": "en termes de sa fibre spéciale",
        "tex": t("@underline{en termes de sa fibre spéciale}"),
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": t("@underline{en termes de sa fibre générique}"),
        "note": "(1.1.2) is Hom_S(S',A) = Hom_K(S'_eta,A_K), the universal property in terms of the generic fibre (cf. d): 'un modèle de Néron de A_eta'). A slip of the text, not of the transcription; the TeX keeps the printed reading.",
    },
    {
        "page": 469,
        "where": "end of 12.2: 'c'est le cas envisagé dans 12.5.4, auquel nous nous bornons'",
        "scan": "12.5.4",
        "tex": "12.5.4",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "10.5.4",
        "note": "Exposé IX has no 12.5.4 (Théorème 12.5 has no subparagraphs). The case meant (X regular, special geometric fibre with only ordinary quadratic singular points) is the one set up in 10.5.4 (p. 446: 'Dans ce cas, nous prouverons 10.4 a) dans 12.5 plus bas'). Less likely intended reading: 12.5. The TeX keeps the printed reading.",
    },
    {
        "page": 470,
        "where": "end of the first paragraph: 'donc de Pic^o_{X/k}'",
        "scan": "Pic^o_{X/k}",
        "tex": t("$@underline{@mathrm{Pic}}^o_{X/k}$"),
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": t("@underline{@mathrm{Pic}}^o_{C/k}"),
        "note": "12.3 concerns the curve C over k (the maximal torus of Pic^o_{C/k} lies in N); there is no X over k here. The TeX keeps the printed reading.",
    },
]

ok = True
for f in findings:
    with open("%s/page_%03d.tex" % (base, f["page"]), encoding="utf-8", newline="") as fh:
        p = fh.read()
    if f["fix"] is not None:
        n = p.count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("FIX OLD COUNT", f["page"], n, repr(f["fix"]["old"]))
    print("page", f["page"], "tex snippet occurs", p.count(f["tex"]), "time(s):", f["tex"])

with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
with open(out, encoding="utf-8") as fh:
    back = json.load(fh)
print("written", len(back), "findings; valid JSON; fixes ok:", ok)
