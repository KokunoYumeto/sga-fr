import json, re, sys
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages
sys.stdout.reconfigure(encoding="utf-8")
L = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_251_255.json", encoding="utf-8"))
spans = {}
for layer in ("diplomatic", "current"):
    P = pages("6", layer)
    spans[layer] = {fo: P[fo][0][0].read_text(encoding="utf-8")[P[fo][0][1]:P[fo][0][2]] for fo in range(251, 256)}
bad = re.compile(r"[\x00-\x09\x0b-\x1f]")
counts = {}
for i, x in enumerate(L):
    pg = x["page"]
    k = "m" if x["kind"] == "misprint_in_print" else "n"
    counts.setdefault(pg, {"n": 0, "m": 0})[k] += 1
    for key in ("scan", "tex", "note", "corrected", "where"):
        if key in x and x[key] and bad.search(x[key]):
            print(i, "control char in", key)
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected")
    f = x["fix"]
    if f is None:
        print(i, pg, x["kind"], "fix null"); continue
    page = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b251_255\page_{pg}.tex", encoding="utf-8").read()
    for s in (f["old"], f["new"]):
        if bad.search(s):
            print(i, "control char in fix", repr(s))
    n = page.count(f["old"])
    nd = spans["diplomatic"][pg].count(f["old"]); nc = spans["current"][pg].count(f["old"])
    print(i, pg, x["kind"], "page:", n, "dipl:", nd, "curr:", nc, repr(f["old"])[:60], "->", repr(f["new"])[:60])
print(counts)
