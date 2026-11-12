import json
import sys

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
BATCH = RUN + r"\b351_355"
OUT = RUN + r"\findings_351_355.json"

findings = [
    {
        "page": 352,
        "where": "proof of 3.6, 'on voit que T = S-U est un ensemble fini de point fermés de S'",
        "scan": "un ensemble fini de point fermés de S",
        "tex": "de point fermés de $S$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "de points fermés de $S$",
        "note": "Print misprint ('point' for 'points'); the TeX keeps the printed reading.",
    },
    {
        "page": 352,
        "where": "proof of 3.6, 'D'autre part, comme de groupe Gal(K'/K) permute'",
        "scan": "comme de groupe Gal(K'/K) permute",
        "tex": "comme de groupe",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "comme le groupe",
        "note": "Print misprint ('de' for 'le'); the TeX keeps the printed reading.",
    },
    {
        "page": 352,
        "where": "same sentence, 'permute entre eux les points de S_i au-dessus du point fermé s de S'",
        "scan": "les points de S_i au-dessus du point fermé s de S",
        "tex": "les points de $S_i$ au-dessus du point fermé",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "les points de $S'$ au-dessus du point fermé",
        "note": "Gal(K'/K) permutes the points of the normalisation S' of S in K' (the sentence ends 'en un point du normalisé S''); S_i is right only when K' is one of the K_i. The TeX keeps the printed reading.",
    },
    {
        "page": 352,
        "where": "Corollaire 3.7, 'tel que l'action I' = I∩π' sur U'",
        "scan": "tel que l'action I' = I∩π' sur U",
        "tex": "\\underline{tel que l'action} $I'",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "\\underline{tel que l'action de} $I'",
        "note": "'de' omitted (cf. 4.1 'tel que l'action de I' sur U'); the TeX keeps the printed reading.",
    },
    {
        "page": 353,
        "where": "proof of Corollaire 3.8, 'pour prouver que (v) implique (vi)'",
        "scan": "pour prouver que (v) implique (vi)",
        "tex": "(v) implique (vi)",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "(vi) implique (v)",
        "note": "The argument (I acts unipotently and the open subgroup of 3.7 has échelon 2, so I has échelon 2) proves (vi) => (v); (v) => (vi) is immediate. The print's '(vi)' is overtyped (bold) but reads (vi). The TeX keeps the printed reading.",
    },
    {
        "page": 354,
        "where": "footnote (*) to 4.1",
        "scan": "(*) Le cas ℓ ≠ p sera étudié dans les §§ 5 et 6 ci-dessous.",
        "tex": "Le cas $\\ell \\neq p$",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Le cas $\\ell = p$",
        "note": "The footnote hangs on 'avec ℓ ≠ p (*)' in 4.1 and announces the excluded case ℓ = p; the handwritten sign in the print is clearly ≠. The TeX keeps the printed reading.",
    },
    {
        "page": 355,
        "where": "'telle que A_{K̃'} ait une réduction semi-stable'",
        "scan": "telle que A_{K̃'} ait une réduction semi-stable, with A not underlined",
        "tex": "\\underline{telle que} $\\underline{A}_{\\tilde{K}'}$ \\underline{ait une réduction semi-stable}",
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": "$\\underline{A}_{\\tilde{K}'}$", "new": "$A_{\\tilde{K}'}$"},
        "note": "Only 'telle que' and 'ait une réduction semi-stable' are underlined; the stroke just under the A is the tilde of the subscript K̃'.",
    },
    {
        "page": 355,
        "where": "'où le (1) désigne le twist de Tate par Z_ℓ(1) = T_ℓ(K̄*)'",
        "scan": "T_ℓ(K̄*) with the asterisk raised as an exponent after K̄",
        "tex": "T_\\ell(\\bar{K}*)",
        "kind": "formula",
        "confidence": "low",
        "fix": {"old": "T_\\ell(\\bar{K}*)", "new": "T_\\ell(\\bar{K}^*)"},
        "note": "Same raised asterisk as on p. 351, where the TeX writes T_\\ell(\\overline{k}^*); a bare * in math mode is set as a centred operator.",
    },
    {
        "page": 355,
        "where": "'En vertu du critère galoisien ... (3.5), ce sous-groupe de I' correspond à'",
        "scan": "ce sous-groupe de I' correspond",
        "tex": "ce sous-groupe de $I'$ correspond",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": "ce sous-groupe de $I$ correspond",
        "note": "The subgroup I' of I corresponds to K̃'/K̃; read 'de I' (or 'ce sous-groupe I' de I', as in the next sentence). The TeX keeps the printed reading.",
    },
    {
        "page": 355,
        "where": "superscript labels ef, et (9 times on the page)",
        "scan": "U^ef, U/U^ef, (U'^et)^∨ with the labels typed upright",
        "tex": "$U^{ef}$, $U/U^{ef}$, $({U'}^{et})^{\\vee}$ in math italic",
        "kind": "font",
        "confidence": "low",
        "fix": None,
        "note": "Convention, not a misprint: this page (and pp. 356-358) sets ef/et in math italic, while p. 354 writes $U^{\\mathrm{ef}}$, $U^{\\mathrm{et}}$; the print types the labels upright like text. Left to a global decision.",
    },
]


def page_text(n):
    with open(BATCH + "\\page_%03d.tex" % n, encoding="utf-8", newline="") as f:
        return f.read()


ok = True
for f in findings:
    t = page_text(f["page"])
    if f["fix"] is not None:
        c = t.count(f["fix"]["old"])
        print(f["page"], "fix.old count", c, repr(f["fix"]["old"]))
        ok &= c == 1
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("  marker inside old!")
            ok = False
    if f["kind"] == "misprint_in_print":
        c = t.count(f["tex"])
        print(f["page"], "misprint tex count", c, repr(f["tex"]))
        ok &= c == 1
    elif f["kind"] == "underline":
        c = t.count(f["tex"])
        print(f["page"], "tex count", c, repr(f["tex"]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
print("written", OUT, "all unique:", ok)
sys.exit(0 if ok else 1)
