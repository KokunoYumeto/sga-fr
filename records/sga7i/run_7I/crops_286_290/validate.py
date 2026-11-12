import json, sys
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I"
F = json.load(open(base + r"\findings_286_290_recheck.json", encoding="utf-8"))
ok = True
counts = {}
for i, f in enumerate(F):
    p = f["page"]
    txt = open(base + r"\b286_290\page_%03d.tex" % p, encoding="utf-8", newline="").read()
    mis = f["kind"] == "misprint_in_print"
    counts.setdefault(p, [0, 0])[1 if mis else 0] += 1
    n_tex = txt.count(f["tex"])
    msg = "tex x%d" % n_tex
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = txt.count(old)
        msg += " | old x%d" % n
        if n != 1 or "%%%%%%%%%%" in old: ok = False
        new_txt = txt.replace(old, f["fix"]["new"])
        msg += " | after: " + new_txt[new_txt.find(f["fix"]["new"])-20:new_txt.find(f["fix"]["new"])+len(f["fix"]["new"])+3].replace("\n","\n")
    if mis and n_tex != 1: ok = False
    if mis and "corrected" not in f: ok = False
    if (not mis) and "corrected" in f: ok = False
    sys.stdout.buffer.write(("%d p%d %s %s\n" % (i, p, f["kind"], msg)).encode("utf-8"))
print("counts", counts, "OK" if ok else "PROBLEM")
