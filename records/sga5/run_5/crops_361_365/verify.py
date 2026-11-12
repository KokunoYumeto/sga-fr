import json, pathlib, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
R = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((R / "findings_361_365.json").read_text(encoding="utf-8"))
ok = True
counts = collections.defaultdict(lambda: [0, 0])
texts = {}
for f in F:
    p = f["page"]
    counts[p][1 if f["kind"] == "misprint_in_print" else 0] += 1
    if p not in texts:
        texts[p] = (R / "b361_365" / f"page_{p}.tex").read_text(encoding="utf-8")
    fx = f["fix"]
    if fx is None:
        continue
    t = texts[p]
    n = t.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        ok = False
        print("BAD", p, n, repr(fx["old"]))
# apply all fixes per page in listed order; each old must still occur exactly once at its turn
for p in sorted(texts):
    t = texts[p]
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        o, nw = f["fix"]["old"], f["fix"]["new"]
        if t.count(o) != 1:
            ok = False
            print("SEQUENTIAL BAD", p, repr(o))
            continue
        t = t.replace(o, nw)
    print("----- page", p, "after all fixes:")
    print(t)
print("counts (normal/misprint):", dict(counts))
print("ALL OK" if ok else "PROBLEMS")
