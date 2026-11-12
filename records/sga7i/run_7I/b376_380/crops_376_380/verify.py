import json, sys, os
fj, folder = sys.argv[1], sys.argv[2]
F = json.load(open(fj, encoding="utf-8"))
ok = True
for i, f in enumerate(F):
    src = open(os.path.join(folder, "page_%03d.tex" % f["page"]), encoding="utf-8").read()
    ntex = src.count(f["tex"])
    line = "#%d p%d %s tex_count=%d" % (i, f["page"], f["kind"], ntex)
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = src.count(old)
        line += " old_count=%d" % n
        if n != 1:
            ok = False
        # marker safety
        if "%%%%%%%%%%" in old or "\n%%%" in old:
            ok = False; line += " MARKER!"
        if f["kind"] == "misprint_in_print":
            ok = False; line += " misprint-with-fix?"
    else:
        if f["kind"] != "misprint_in_print":
            ok = False; line += " fix null on non-misprint!"
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False; line += " no corrected!"
    if ntex < 1:
        ok = False; line += " TEX NOT FOUND"
    print(line)
print("ALL OK" if ok else "PROBLEMS")
