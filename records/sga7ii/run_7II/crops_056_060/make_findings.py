import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II")
BATCH = RUN / "b056_060"
OUT = RUN / "findings_056_060.json"

findings = [
    {
        "page": 56,
        "where": "paragraph 'En vertu de 2.4 (ii), et (2.5.2)', index range of the couples (c_i,d_i) before (2.5.4)",
        "scan": "(c_i,d_i) with the subscript range i\u2264i\u2264d: both letters before d are dotted i's, not the digit 1 (checked at 4x)",
        "tex": "(c_i,d_i)_{i \\leqslant i \\leqslant d}",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "(c_i,d_i)_{1 \\leqslant i \\leqslant d}",
        "note": "The lower bound is the digit 1 (the same i-for-1 slip as P\u2282[i,d] on p. 54). The TeX keeps the printed reading. The corrected layer reads (c_i,d_i)_{i\\in P}, the exact range: by 2.4 (ii) the couples and the sum in (2.5.4) run over i in P.",
    },
    {
        "page": 56,
        "where": "last sentence: 'les conditions (2.5.4) se r\u00e9\u00e9crivent, en terme des c_i, n_i, e et f'",
        "scan": "en terme des c_i, n_i, e et f",
        "tex": "en terme des $c_i$, $n_i$, $e$ et $f$",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "en termes des $c_i$, $n_i$, $e$ et $f$",
        "note": "The locution is 'en termes de'. The TeX keeps the printed reading; the corrected layer already reads 'en termes des'.",
    },
    {
        "page": 57,
        "where": "paragraph after (2.5.6): 'Sinon, si a_d \u2260 2, le mieuxqu'on puisse faire'",
        "scan": "mieuxqu'on: no space between mieux and qu'on, the x overtyped (checked at 3x)",
        "tex": "le mieuxqu'on puisse faire",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "le mieux qu'on puisse faire",
        "note": "Missing word space. The TeX keeps the printed reading; the corrected layer already reads 'mieux qu'on'.",
    },
    {
        "page": 58,
        "where": "Corollaire 2.8, 'congru \u00e0 n modulo 2'",
        "scan": "one underline runs from the c of 'congru' to the end of '\u00e0'; n is not underlined (checked at 5x)",
        "tex": "\\underline{congru} \u00e0 $n$",
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": "\\underline{congru} \u00e0", "new": "\\underline{congru \u00e0}"},
        "note": "The TeX leaves '\u00e0' outside the underline.",
    },
    {
        "page": 58,
        "where": "paragraph after D\u00e9finition 2.7: 'est au plus \u00e9gal \u00e0 inf(n,dim(X) - n)'",
        "scan": "inf(n,dim(X) - n) (no 2 before dim; checked at 2.5x)",
        "tex": "\\inf(n,\\dim(X) - n)",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "\\inf(n,2\\dim(X) - n)",
        "note": "h^{pq}(X) \u2260 0 forces p, q \u2264 dim X, so q - p = 2q - n \u2264 2 dim X - n (and q - p \u2264 p + q = n). With dim(X) - n the Hodge level of the middle cohomology (n = dim X) would be \u2264 0, which fails for a curve of genus \u2265 1 and for V_3(3) (level 1 in the table on p. 60). The TeX keeps the printed reading; the corrected layer already reads 2\\dim(X).",
    },
]

# every non-null fix's old must occur exactly once in its page file
for x in findings:
    fix = x.get("fix")
    if fix:
        t = (BATCH / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
        n = t.count(fix["old"])
        print(x["page"], repr(fix["old"]), "occurs", n)
        assert n == 1
    # the quoted tex must be present on the page
    t = (BATCH / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    assert x["tex"] in t, (x["page"], x["tex"])

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
print("written", OUT, len(findings))
