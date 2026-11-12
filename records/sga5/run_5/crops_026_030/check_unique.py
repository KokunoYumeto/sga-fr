import json
B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
F = json.load(open(B + r"\findings_026_030.json", encoding="utf-8"))
ok = True
pages = {}
for i, f in enumerate(F):
    p = f["page"]
    t = pages.setdefault(p, open(rf"{B}\b026_030\page_{p:03d}.tex", encoding="utf-8").read())
    fx = f["fix"]
    if fx is None:
        continue
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, p, n, repr(fx["old"]))
    if "%%%%" in fx["old"]:
        ok = False
        print("crosses marker", i)
# overlap check per page: positions of olds in original text
import itertools
for p, t in pages.items():
    spans = []
    for i, f in enumerate(F):
        if f["page"] == p and f["fix"]:
            k = t.find(f["fix"]["old"]); spans.append((k, k + len(f["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP page", p, a, b)
# apply all fixes sequentially and check each still applies
for p, t in pages.items():
    s = t
    for i, f in enumerate(F):
        if f["page"] == p and f["fix"]:
            if s.count(f["fix"]["old"]) != 1:
                ok = False; print("after earlier edits not unique", i)
            s = s.replace(f["fix"]["old"], f["fix"]["new"], 1)
print("ALL OK" if ok else "PROBLEMS")
from collections import Counter
c = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in sorted(pages):
    print(p, c[(p, False)], "/", c[(p, True)])
