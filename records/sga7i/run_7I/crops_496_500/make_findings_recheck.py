import json
import sys
from pathlib import Path

RUN = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
BATCH = RUN / "b496_500"
OUT = RUN / "findings_496_500_recheck.json"

findings = [
    {
        "page": 496,
        "where": "(13.4.14), middle term of the exact sequence 0 -> F(B) -> ... -> Lie(B) -> 0",
        "scan": "0 \u2192 F(B) \u2192 (B) \u2192 Lie(B) \u2192 0 , : a clean blank before (B), no handwritten script E (checked in a crop)",
        "tex": r"\longrightarrow (B) \longrightarrow",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": r"\longrightarrow \mathcal{E}(B) \longrightarrow",
        "note": "The handwritten script E was never added: the term is \u2130(B), as in the first line of (13.4.15) on the same page. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 497,
        "where": "Proposition 13.4.17, 'les filtrations sur \u2130 = R\u2297O_S \"de Hodge\" et \"par le poids\" :'",
        "scan": "\"de Hodge\" with only the words underlined: measured in the scan, the opening quotation mark ends at x=395 and the rule starts at x=399; the rule ends at x=590 and the closing mark starts at x=591",
        "tex": r'\underline{"de Hodge"}',
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": r'\underline{"de Hodge"}', "new": r'"\underline{de Hodge}"'},
        "note": "Quotation marks inside the underline; the print underlines only the words.",
    },
    {
        "page": 497,
        "where": "Proposition 13.4.17, same line, '\"par le poids\" :'",
        "scan": "\"par le poids\" with only the words underlined: the opening quotation mark ends at x=723 and the rule starts at x=727; the rule ends at x=1012 and the closing mark starts at x=1014",
        "tex": r'\underline{"par le poids"}',
        "kind": "underline",
        "confidence": "high",
        "fix": {"old": r'\underline{"par le poids"}', "new": r'"\underline{par le poids}"'},
        "note": "Quotation marks inside the underline; the print underlines only the words.",
    },
    {
        "page": 497,
        "where": "Paragraph before 13.4.17: 'ses relations avec la \"filtration de Hodge\" (13.4.6) de \u2130 d\u00e9fini par le sous-Module F de \u2130'",
        "scan": "de \u2130 d\u00e9fini par le sous-Module F",
        "tex": r"de $\mathcal{E}$ défini par",
        "kind": "misprint_in_print",
        "confidence": "low",
        "fix": None,
        "corrected": r"de $\mathcal{E}$ définie par",
        "note": "Agreement slip: what the sub-Module F defines is the Hodge filtration (13.4.6), whose Fil^0 is F, so 'd\u00e9finie'. Low: possibly the author's own wording. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 498,
        "where": "Remarque 13.4.18, last line: 'Il y a cependant un trait impcrtant de la th\u00e9orie alg\u00e9brique'",
        "scan": "impcrtant: the letter after p has the shape of the typed c of 'cependant' on the same line, open on the right with its upper terminal (checked in a crop)",
        "tex": "impcrtant",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "important",
        "note": "Typing error (c for o). The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 498,
        "where": "Remarque 13.4.18: 'La situation qu'on vient d'expliciter, a servie de mod\u00e8le aux conjectures de DELIGNE'",
        "scan": "a servie de mod\u00e8le",
        "tex": "a servie de",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "a servi de",
        "note": "The past participle of servir with avoir and no preceding direct object does not agree: 'a servi'. The TeX keeps the printed reading. 'corrected' replaces the 'tex' substring.",
    },
    {
        "page": 500,
        "where": "'ce qui est le cas en particulier si S est normal en s et A quasi-projectif sur S (7.1.5) on obtient donc un sch\u00e9ma en groupes'",
        "scan": "(7.1.5) followed by a wide blank and then 'on': no comma. Measured in the scan: between the closing parenthesis and 'on', from cap height down to 10 px below the baseline, there is no ink at all (darkest pixel 209 against a background of 211); the only mark is a speck of 6 x 4 px (19 dark px) lying 12-15 px below the baseline. The typed comma after Spec(\u00d4) at the end of the same line measures 9 x 16 px (96 dark px) and reaches only 8 px below the baseline.",
        "tex": "(7.1.5), on obtient",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": {"old": "(7.1.5), on obtient", "new": "(7.1.5) on obtient"},
        "corrected": "(7.1.5), on obtient",
        "note": "The speck is dust, not a comma (it is a fifth of the size of a typed comma and lies below the lowest point a comma reaches), so the comma now in the TeX is not printed. The sentence needs it to close the clause 'ce qui est le cas ... (7.1.5)'. The TeX silently corrects; the fix restores the printed reading. 'corrected' is the current TeX.",
    },
]

# Validation: every fix 'old' occurs exactly once in its page file; every 'tex' occurs in its page file.
ok = True
for f in findings:
    page_tex = (BATCH / f"page_{f['page']:03d}.tex").read_bytes().decode("utf-8")
    if "\r" in page_tex:
        print("CR found in", f["page"])
    if f["tex"] not in page_tex:
        print("TEX NOT FOUND", f["page"], repr(f["tex"]))
        ok = False
    if f["fix"] is not None:
        n = page_tex.count(f["fix"]["old"])
        if n != 1:
            print("OLD COUNT", n, f["page"], repr(f["fix"]["old"]))
            ok = False
        if "%%%%%%%%%%" in f["fix"]["old"]:
            print("OLD crosses marker", f["page"])
            ok = False
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
    else:
        assert "corrected" not in f
    for k, v in f.items():
        if isinstance(v, str) and any(ord(c) < 32 for c in v):
            print("CONTROL CHAR in", f["page"], k)
            ok = False
    if f["fix"]:
        for k, v in f["fix"].items():
            if any(ord(c) < 32 for c in v):
                print("CONTROL CHAR in fix", f["page"], k)
                ok = False

if not ok:
    sys.exit(1)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("written", OUT, len(findings))
