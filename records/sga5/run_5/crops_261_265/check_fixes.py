import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
run = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
d = json.load(open(run + r"\findings_261_265.json", encoding="utf-8"))
pages = {}
for p in range(261, 266):
    pages[p] = open(run + r"\b261_265\page_%d.tex" % p, encoding="utf-8").read()
work = dict(pages)
counts = {}
ok = True
for i, f in enumerate(d):
    p = f["page"]
    k = f["kind"]
    c = counts.setdefault(p, [0, 0])
    c[1 if k == "misprint_in_print" else 0] += 1
    for key in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if key not in f:
            print("missing key", key, "in item", i); ok = False
    if k == "misprint_in_print" and "corrected" not in f:
        print("misprint without corrected", i); ok = False
    if k != "misprint_in_print" and "corrected" in f:
        print("corrected on non-misprint", i); ok = False
    fx = f["fix"]
    if fx is None:
        print(i, p, k, "fix null")
        continue
    old, new = fx["old"], fx["new"]
    n = pages[p].count(old)
    if n != 1:
        print("ITEM", i, "page", p, "old occurs", n, "times:", repr(old)); ok = False
    if old == new:
        print("old == new", i); ok = False
    if "%%%%%%%%%%" in old:
        print("old crosses marker", i); ok = False
    m = work[p].count(old)
    if m != 1:
        print("ITEM", i, "after earlier edits old occurs", m, "times:", repr(old)); ok = False
    else:
        work[p] = work[p].replace(old, new)
print("counts (normal, misprint):", counts)
print("ALL OK" if ok else "PROBLEMS")
for p in range(261, 266):
    if p in (261, 264):
        print("=== edited page", p)
        print(work[p])
