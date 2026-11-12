import json

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
with open(RUN + r"\findings_026_030.json", encoding="utf-8") as fh:
    F = json.load(fh)

ok = True
counts = {}
for i, f in enumerate(F):
    p = f["page"]
    with open(RUN + r"\b026_030\page_%03d.tex" % p, encoding="utf-8", newline="") as fh:
        t = fh.read()
    key = "misprint" if f["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(p, {"normal": 0, "misprint": 0})[key] += 1
    n_tex = t.count(f["tex"])
    msg = "tex x%d" % n_tex
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n_old = t.count(old)
        msg += ", old x%d" % n_old
        if n_old != 1 or "%%%%%%%%%%" in old:
            ok = False
            msg += "  <-- PROBLEM"
        # apply and make sure the result differs
        if t.replace(old, f["fix"]["new"], 1) == t:
            ok = False
            msg += "  <-- NO CHANGE"
    if n_tex != 1:
        msg += "  (tex not unique)"
        if f["kind"] == "misprint_in_print" and f["fix"] is None:
            ok = False
            msg += "  <-- PROBLEM"
    print(i, p, f["kind"], msg)

print("counts", counts)
print("ALL OK" if ok else "PROBLEMS FOUND")
