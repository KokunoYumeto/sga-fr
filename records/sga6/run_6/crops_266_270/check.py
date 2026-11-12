"""check.py: every fix's old occurs exactly once in its page file; apply all fixes in memory and show the results."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
d = json.loads((run / "findings_266_270.json").read_text(encoding="utf-8"))
pages = {p: (run / "b266_270" / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(266, 271)}
applied = dict(pages)
ok = True
for i, x in enumerate(d):
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in x:
            print(i, "missing key", k); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected"); ok = False
    f = x["fix"]
    if f is None:
        continue
    t = pages[x["page"]]
    n = t.count(f["old"])
    bad = [c for c in f["old"] + f["new"] if ord(c) < 32 and c != "\n"]
    print(i, x["page"], x["kind"], "count", n, "ctrl", bad, "marker in old", "%%%%%%%%%%" in f["old"])
    if n != 1 or bad:
        ok = False
    applied[x["page"]] = applied[x["page"]].replace(f["old"], f["new"], 1)
for p in range(266, 271):
    if applied[p] != pages[p]:
        print("==== page", p, "after fixes")
        a, b = pages[p].splitlines(), applied[p].splitlines()
        import difflib
        for line in difflib.unified_diff(a, b, lineterm="", n=0):
            print(line)
print("ALL OK" if ok else "PROBLEMS")
