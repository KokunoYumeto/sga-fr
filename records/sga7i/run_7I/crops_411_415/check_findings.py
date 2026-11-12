import json, sys, os
fj, d = sys.argv[1], sys.argv[2]
F = json.load(open(fj, encoding="utf-8"))
ok = True
for i, x in enumerate(F):
    p = os.path.join(d, "page_%03d.tex" % x["page"])
    t = open(p, encoding="utf-8").read()
    tc = t.count(x["tex"])
    line = "#%d p%d %s tex-count=%d" % (i, x["page"], x["kind"], tc)
    if x["fix"] is not None:
        old, new = x["fix"]["old"], x["fix"]["new"]
        c = t.count(old)
        marker_hit = any("%%%%%%%%%%" in l for l in old.split("\n"))
        line += " old-count=%d marker=%s" % (c, marker_hit)
        if c != 1 or marker_hit:
            ok = False
        t2 = t.replace(old, new)
        line += " applied-len-change=%d" % (len(t2) - len(t))
    else:
        if x["kind"] != "misprint_in_print":
            ok = False
            line += " NULL FIX ON NON-MISPRINT"
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        ok = False
        line += " MISSING corrected"
    if tc == 0:
        line += " (tex not found verbatim)"
    print(line)
print("ALL OK" if ok else "PROBLEMS")
