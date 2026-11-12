import json, sys
sys.stdout.reconfigure(encoding="utf-8")
run = sys.argv[1]
d = json.load(open(run + "/findings_341_345_recheck.json", encoding="utf-8"))
ok = True
counts = {}
for i, f in enumerate(d):
    p = f["page"]
    src = open(run + "/b341_345/page_%d.tex" % p, encoding="utf-8").read()
    kind = f["kind"]
    key = "misprint" if kind == "misprint_in_print" else "normal"
    counts.setdefault(p, {"normal": 0, "misprint": 0})[key] += 1
    tex_n = src.count(f["tex"])
    line = "#%d p%d %s tex_count=%d" % (i, p, kind, tex_n)
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = src.count(old)
        line += " old_count=%d" % n
        if n != 1:
            ok = False
        for ln in src.split("\n"):
            if ln.startswith("%%%%%%%%%%") and old in ln:
                ok = False
                line += " TOUCHES MARKER"
    if kind == "misprint_in_print" and "corrected" not in f:
        ok = False
        line += " NO CORRECTED"
    if tex_n == 0:
        line += "  <-- tex snippet not found"
    print(line)
print(counts)
print("ALL OK" if ok else "PROBLEM")
