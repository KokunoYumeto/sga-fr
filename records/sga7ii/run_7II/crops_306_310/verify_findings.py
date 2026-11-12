import json, re, sys, os

run = sys.argv[1]
findings_path = os.path.join(run, "findings_306_310_recheck.json")
pages_dir = os.path.join(run, "b306_310")
out_dir = os.path.join(run, "crops_306_310", "fixed")
os.makedirs(out_dir, exist_ok=True)

F = json.load(open(findings_path, encoding="utf-8"))
ctrl = re.compile(r"[\x00-\x08\x0b-\x1f\x7f]")
ok = True
texts = {}
for p in (306, 307, 308, 309, 310):
    b = open(os.path.join(pages_dir, "page_%d.tex" % p), "rb").read()
    assert b"\r" not in b, "CR in page %d" % p
    texts[p] = b.decode("utf-8")

applied = {p: texts[p] for p in texts}
for i, f in enumerate(F):
    for k, v in f.items():
        if isinstance(v, str) and ctrl.search(v):
            print("CONTROL CHAR in finding", i, k, repr(v)); ok = False
    page = f["page"]
    t = texts[page]
    if f.get("fix"):
        old, new = f["fix"]["old"], f["fix"]["new"]
        for s in (old, new):
            if ctrl.search(s):
                print("CONTROL CHAR in fix", i); ok = False
        n = t.count(old)
        marker = "%%%%%%%%%%" in old
        print("finding %2d p%d fix old count=%d marker=%s" % (i, page, n, marker))
        if n != 1 or marker:
            ok = False
        applied[page] = applied[page].replace(old, new, 1)
    if f["kind"] == "misprint_in_print":
        n = t.count(f["tex"])
        print("finding %2d p%d misprint tex count=%d" % (i, page, n))
        if n != 1:
            ok = False
        if "corrected" not in f:
            print("missing corrected", i); ok = False

for p, s in applied.items():
    with open(os.path.join(out_dir, "page_%d.tex" % p), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(s)
print("ALL OK" if ok else "PROBLEMS")
