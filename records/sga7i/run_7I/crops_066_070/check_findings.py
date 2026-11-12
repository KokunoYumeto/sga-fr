import json

BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
F = json.load(open(BASE + r"\findings_066_070.json", encoding="utf-8"))
pages = {}
for p in range(66, 71):
    with open(BASE + rf"\b066_070\page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        pages[p] = fh.read()

ok = True
for i, f in enumerate(F):
    t = pages[f["page"]]
    if f.get("fix"):
        old = f["fix"]["old"]
        n = t.count(old)
        if n != 1:
            ok = False
        print(i, f["page"], f["kind"], "fix-old count", n, "|", old)
        if "%%%%%%%%%%" in old or "\n%" in old:
            print("   !! touches a marker/comment line")
    if f.get("tex"):
        n = t.count(f["tex"])
        print("   tex count", n, "|", f["tex"])
    if f["kind"] == "misprint_in_print":
        if "corrected" not in f:
            print("   !! misprint without corrected")
print("ALL FIX OLDS UNIQUE:", ok)

# simulate applying all fixes in order and check each later old is still unique
import copy
sim = copy.deepcopy(pages)
for i, f in enumerate(F):
    if f.get("fix"):
        old, new = f["fix"]["old"], f["fix"]["new"]
        c = sim[f["page"]].count(old)
        if c != 1:
            print("SEQUENTIAL PROBLEM at", i, c, old)
        sim[f["page"]] = sim[f["page"]].replace(old, new, 1)
# reverse order too
sim = copy.deepcopy(pages)
for i, f in reversed(list(enumerate(F))):
    if f.get("fix"):
        old, new = f["fix"]["old"], f["fix"]["new"]
        c = sim[f["page"]].count(old)
        if c != 1:
            print("REVERSE PROBLEM at", i, c, old)
        sim[f["page"]] = sim[f["page"]].replace(old, new, 1)
print("done")
