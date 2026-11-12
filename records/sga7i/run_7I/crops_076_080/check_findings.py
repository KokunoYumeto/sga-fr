import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
F = json.load(open(BASE + r"\findings_076_080.json", encoding="utf-8"))
pages = {}
for p in range(76, 81):
    with open(BASE + rf"\b076_080\page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read()
    if "\r\n" in pages[p]:
        print("CRLF in page", p)

ok = True
counts = {}
applied = dict(pages)
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
    if k != "misprint_in_print" and "corrected" in f:
        print("corrected on non-misprint", i)
        ok = False
    if f["fix"] is not None:
        old, new = f["fix"]["old"], f["fix"]["new"]
        n = t.count(old)
        if n != 1:
            print("FIX OLD NOT UNIQUE IN ORIGINAL", i, p, n, repr(old))
            ok = False
        if "%%%%%%%%%%" in old or "%%%%%%%%%%" in new:
            print("MARKER IN FIX", i)
            ok = False
        # sequential application
        m = applied[p].count(old)
        if m != 1:
            print("FIX OLD NOT UNIQUE AFTER EARLIER FIXES", i, p, m, repr(old))
            ok = False
        else:
            applied[p] = applied[p].replace(old, new)
    else:
        n = t.count(f["tex"])
        if n != 1:
            print("TEX NOT UNIQUE", i, p, n, repr(f["tex"]))
            ok = False
for i, f in enumerate(F):
    # the 'tex' of entries with a fix should also be found in the original page
    if f["tex"] and pages[f["page"]].count(f["tex"]) < 1:
        print("TEX NOT FOUND", i, f["page"], repr(f["tex"]))
        ok = False
print("counts (normal, misprint):", counts)
print("OK" if ok else "PROBLEMS")
