import json, io, sys
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
F = json.load(io.open(base + r"\findings_381_385_recheck.json", encoding="utf-8"))
ok = True
texts = {}
for p in (381, 382, 383, 384, 385):
    texts[p] = io.open(base + r"\b381_385\page_%d.tex" % p, encoding="utf-8", newline="").read()
counts = {}
for i, f in enumerate(F):
    p = f["page"]
    k = "m" if f["kind"] == "misprint_in_print" else "n"
    counts.setdefault(p, {"n": 0, "m": 0})[k] += 1
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print(i, "misprint without corrected"); ok = False
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print(i, "corrected on a non-misprint"); ok = False
    fx = f["fix"]
    if fx is None:
        # kept misprint: the printed reading must be in the TeX
        if f["tex"] not in texts[p]:
            print(i, "tex text not found on page", p); ok = False
        continue
    n = texts[p].count(fx["old"])
    print(i, p, f["kind"], "old count =", n)
    if n != 1:
        ok = False
    if "%%%%%%%%%%" in fx["old"]:
        print(i, "old crosses a marker"); ok = False
# apply all fixes per page in order and check braces and uniqueness after each
for p in texts:
    t = texts[p]
    for f in F:
        if f["page"] == p and f["fix"]:
            if t.count(f["fix"]["old"]) != 1:
                print("after earlier fixes, old not unique/absent:", p, f["fix"]["old"]); ok = False
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
    if t.count("{") != t.count("}"):
        print("brace imbalance on", p, t.count("{"), t.count("}")); ok = False
    orig = texts[p]
    print(p, "braces", orig.count("{") - orig.count("}"), "->", t.count("{") - t.count("}"))
print("counts", counts)
print("OK" if ok else "PROBLEMS")
