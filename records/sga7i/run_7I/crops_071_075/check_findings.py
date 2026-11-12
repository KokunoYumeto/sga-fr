import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
F = json.load(open(BASE + r"\findings_071_075.json", encoding="utf-8"))
pages = {}
for p in range(71, 76):
    pages[p] = open(BASE + rf"\b071_075\page_{p:03d}.tex", encoding="utf-8").read()

ok = True
counts = {}
for i, f in enumerate(F):
    p = f["page"]
    t = pages[p]
    k = f["kind"]
    c = counts.setdefault(p, [0, 0])
    c[1 if k == "misprint_in_print" else 0] += 1
    for key in ["page", "where", "scan", "tex", "kind", "confidence", "fix", "note"]:
        if key not in f:
            print("MISSING KEY", i, key)
            ok = False
    if k == "misprint_in_print" and "corrected" not in f:
        print("MISSING corrected", i)
        ok = False
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = t.count(old)
        if n != 1:
            print("FIX OLD NOT UNIQUE", i, p, n, repr(old))
            ok = False
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in f["fix"]["new"]:
            print("MARKER IN FIX", i)
            ok = False
    elif k == "misprint_in_print":
        n = t.count(f["tex"])
        if n != 1:
            print("TEX NOT UNIQUE", i, p, n, repr(f["tex"]))
            ok = False
    else:
        print("fix null, non-misprint (convention entry):", i, p, f["where"][:60])
print("counts (normal, misprint):", counts)
print("OK" if ok else "PROBLEMS")
