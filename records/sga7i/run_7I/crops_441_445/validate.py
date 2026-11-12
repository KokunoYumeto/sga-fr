import json, sys, os, unicodedata
run = sys.argv[1]
F = json.load(open(os.path.join(run, "findings_441_445_recheck.json"), encoding="utf-8"))
ok = True
counts = {}
for i, f in enumerate(F):
    p = f["page"]
    tex = open(os.path.join(run, "b441_445", "page_%d.tex" % p), encoding="utf-8").read()
    # control characters anywhere?
    for k, v in f.items():
        if isinstance(v, str) and any(unicodedata.category(c) == "Cc" for c in v):
            print("CONTROL CHAR in", i, k); ok = False
    n_tex = tex.count(f["tex"])
    msg = "tex x%d" % n_tex
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n_old = tex.count(old)
        msg += ", fix.old x%d" % n_old
        if n_old != 1: ok = False
        # old must not cross a marker line
        if "%%%%%%%%%%" in old: ok = False; msg += " MARKER!"
    if f["kind"] == "misprint_in_print" and "corrected" not in f: ok = False; msg += " NO CORRECTED"
    mis = f["kind"] == "misprint_in_print"
    c = counts.setdefault(p, [0, 0]); c[1 if mis else 0] += 1
    print(p, f["kind"], f["confidence"], msg, "|", f["tex"].encode("unicode_escape").decode("ascii"))
print("counts", {p: "%d/%d" % tuple(v) for p, v in sorted(counts.items())})
print("ALL OK" if ok else "PROBLEMS")
