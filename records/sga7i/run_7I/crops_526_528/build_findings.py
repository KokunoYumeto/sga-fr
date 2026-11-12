import json
import sys
from pathlib import Path

RUN = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
PAGES = RUN / "b526_528"
OUT = RUN / "findings_526_528_recheck.json"

RULE = "\\noindent\\rule{\\linewidth}{0.4pt}"

findings = [
    # ---------------- page 526 ----------------
    {
        "page": 526,
        "where": "throughout: the price closing each of the 68 entries, e.g. Vol. 178 (left column), Vol. 181 (left column), Vol. 245 (right column)",
        "scan": "DM 18,\u2013 / DM 16.\u2013 / DM 16,\u2013 (en dash)",
        "tex": "DM 18,- / DM 16.- / DM 16,- (hyphen)",
        "kind": "punctuation",
        "confidence": "medium",
        "fix": None,
        "note": "Page-wide convention, reported once; no single edit can carry it. At full resolution the price dash is about 16 px long, like the spaced dash in 'Bourbaki \u2013 vol.' (TeX --) and the en dash of 382\u2013399 (TeX --), and like the price dash on page 527, which that page's TeX writes DM 40,--; a hyphen (347-363, 17-23, '(Suisse)-') is about 7 px. Replace the final '-' of every 'DM <n>,-' and 'DM <n>.-' on this page by '--' (68 entries; Vols. 181, 186 and 198 keep their full stop: 'DM 16.--'). Page 525's TeX uses the same hyphen form (seen in its TeX, not checked against its scan).",
    },
    {
        "page": 526,
        "where": "top of the page, above both columns",
        "scan": "a horizontal rule across the page above Vols. 178 and 212",
        "tex": "no rule; the page begins with 'Vol. 178:'",
        "kind": "other",
        "confidence": "low",
        "fix": {"old": "Vol. 178: Th.", "new": RULE + "\n\nVol. 178: Th."},
        "note": "Page 527 prints the same pair of rules and its TeX gives them as \\noindent\\rule{\\linewidth}{0.4pt}; page 526 omits both (bottom rule: next finding). Drop both findings if rules count as layout.",
    },
    {
        "page": 526,
        "where": "bottom of the page, below both columns",
        "scan": "a horizontal rule across the page below Vols. 211 and 245",
        "tex": "no rule; the page ends with Vol. 245",
        "kind": "other",
        "confidence": "low",
        "fix": {
            "old": "Dimension One. V, 99 pages. 1972. DM 16,-\n",
            "new": "Dimension One. V, 99 pages. 1972. DM 16,-\n\n" + RULE + "\n",
        },
        "note": "Companion of the top-rule finding. Its old ends in 'DM 16,-' plus a line break, so apply it before the page-wide price-dash replacement (afterwards it no longer matches and must be re-anchored on 'DM 16,--').",
    },
    {
        "page": 526,
        "where": "left column, Vol. 179",
        "scan": "Seminaire Bourbaki \u2013 vol. 1968/69",
        "tex": "Seminaire Bourbaki",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "S\u00e9minaire Bourbaki",
        "note": "The acute accent is missing (Vols. 180 and 244 print S\u00e9minaire). The TeX keeps the printed reading. The separator slips of the publisher's list (here 'IV.' for 'IV,'; 'DM 16.\u2013' in Vols. 181, 186, 198; 'Sigrist, V,'; 'Grothendieck XXII,'; '1971, DM 20'; on page 527 'Goldsmith VI,' and 'T\u00f6rnig, VI,') are likewise kept by the TeX and are not itemized.",
    },
    {
        "page": 526,
        "where": "left column, Vol. 200",
        "scan": "Vol. 2 00: U. Neri",
        "tex": "Vol. 2 00:",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "Vol. 200:",
        "note": "The print sets a space inside the volume number. The TeX keeps it.",
    },
    {
        "page": 526,
        "where": "left column, Vol. 209",
        "scan": "Proceedings of Liverpool Singularities [wide gap, no dash] Symposium II.",
        "tex": "Singularities \\quad Symposium II.",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "Singularities -- Symposium II.",
        "note": "The dash is missing: the print leaves only a gap, with no trace of a dash at full resolution (cf. Vol. 192 'Singularities \u2013 Symposium I.'). The TeX keeps the gap as \\quad.",
    },
    {
        "page": 526,
        "where": "right column, Vol. 218",
        "scan": "IV, 212.Seiten 1971. DM 20,\u2013",
        "tex": "212.Seiten 1971.",
        "kind": "misprint_in_print",
        "confidence": "medium",
        "fix": None,
        "corrected": "212 Seiten. 1971.",
        "note": "The full stop is set after 212 instead of after Seiten. The TeX keeps the printed reading.",
    },
    {
        "page": 526,
        "where": "right column, Vol. 224",
        "scan": "Rev\u00e8tements Etales et Groupe Fondamental",
        "tex": "Rev\u00e8tements",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Rev\u00eatements",
        "note": "A grave accent is printed for the circumflex (SGA 1: Rev\u00eatements \u00e9tales et groupe fondamental). The TeX keeps the printed reading. The unaccented capital of 'Etales' is the list's normal practice (also 'Etale' in Vols. 269, 270) and is not reported.",
    },
    # ---------------- page 527 ----------------
    {
        "page": 527,
        "where": "right column, Vol. 283",
        "scan": "L. Illusie (the full stop is kerned into the foot of the L)",
        "tex": "L Illusie",
        "kind": "punctuation",
        "confidence": "medium",
        "fix": {"old": "L Illusie", "new": "L. Illusie"},
        "note": "At full resolution the foot of this L runs on to about 22 px and ends in a raised dot-sized bump, exactly like the kerned 'L.' of 'R. L. Lipsman' (Vol. 266), which the TeX gives with its full stop; a bare L (Lipsman, Lectures, Lie) is about 16 px wide. The print reads 'L. Illusie', as in Vol. 239 on page 526.",
    },
    {
        "page": 527,
        "where": "left column, Vol. 274",
        "scan": "Edited by. F. W. Lawvere",
        "tex": "Edited by. F. W.",
        "kind": "misprint_in_print",
        "confidence": "high",
        "fix": None,
        "corrected": "Edited by F. W.",
        "note": "Stray full stop after 'by'. The TeX keeps the printed reading.",
    },
]

ok = True
texts = {}
for f in findings:
    p = f["page"]
    if p not in texts:
        texts[p] = (PAGES / f"page_{p}.tex").read_text(encoding="utf-8")
    t = texts[p]
    fx = f["fix"]
    if fx is not None:
        n = t.count(fx["old"])
        if n != 1:
            ok = False
            print(f"FIX OLD COUNT {n} on page {p}: {fx['old']!r}")
        # the old must not touch a marker line
        if "%%%%%%%%%%" in fx["old"]:
            ok = False
            print(f"FIX OLD crosses marker on page {p}")
    if f["kind"] == "misprint_in_print":
        n = t.count(f["tex"])
        if n != 1:
            ok = False
            print(f"MISPRINT TEX COUNT {n} on page {p}: {f['tex']!r}")
        if "corrected" not in f:
            ok = False
            print("missing corrected", f)
    elif "corrected" in f:
        ok = False
        print("corrected on non-misprint", f)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
# re-read to confirm the JSON parses
back = json.loads(OUT.read_text(encoding="utf-8"))
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in back)
print("written", OUT, len(back), "findings; valid fixes:", ok)
for p in (526, 527, 528):
    print(p, "normal", c[(p, False)], "misprint", c[(p, True)])
sys.exit(0 if ok else 1)
