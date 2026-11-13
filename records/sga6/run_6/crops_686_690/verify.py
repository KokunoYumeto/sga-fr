"""Verify findings_686_690.json against the page files (read-only).

Checks: every fix 'old' occurs exactly once in its page_NNN.tex; applying a page's fixes one after another, each 'old'
still occurs exactly once at its turn (no overlaps); no 'old' or 'new' touches a marker line; misprints carry
'corrected'; null-fix misprints have a 'tex' that occurs in the page; no control characters in the JSON strings.
"""
import collections
import json
import pathlib
import re

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = json.loads((RUN / "findings_686_690.json").read_text(encoding="utf-8"))
pages = {n: (RUN / "b686_690" / f"page_{n}.tex").read_text(encoding="utf-8") for n in (686, 687, 688, 689)}
ok = True
work = dict(pages)
counts = collections.Counter()
ctrl = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
for i, f in enumerate(F):
    pg = f["page"]
    kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
             "misprint_in_print", "marker", "other"}
    if f["kind"] not in kinds or f["confidence"] not in {"high", "medium", "low"}:
        print("BAD kind/confidence", i, f["kind"], f["confidence"]); ok = False
    for k, v in f.items():
        if isinstance(v, str) and ctrl.search(v):
            print("CONTROL CHAR", i, k); ok = False
    counts[(pg, "misprint" if f["kind"] == "misprint_in_print" else "normal")] += 1
    if f["kind"] == "misprint_in_print" and not f.get("corrected"):
        print("MISSING corrected", i); ok = False
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print("corrected on non-misprint", i); ok = False
    fx = f["fix"]
    if fx is None:
        if f["kind"] == "misprint_in_print" and pages[pg].count(f["tex"]) < 1:
            print("tex of null-fix misprint not found", i, repr(f["tex"])); ok = False
        continue
    old, new = fx["old"], fx["new"]
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
        print("MARKER TOUCHED", i); ok = False
    c0 = pages[pg].count(old)
    c1 = work[pg].count(old)
    if c0 != 1 or c1 != 1:
        print(f"COUNT page {pg} #{i}: original {c0}, sequential {c1}: {old!r}"); ok = False
    else:
        work[pg] = work[pg].replace(old, new, 1)
for pg in sorted(pages):
    print(pg, "normal", counts[(pg, "normal")], "misprint", counts[(pg, "misprint")])
print("total", len(F), "ALL OK" if ok else "PROBLEMS")
