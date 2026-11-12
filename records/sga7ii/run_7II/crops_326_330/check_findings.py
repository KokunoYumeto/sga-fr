import json, io
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
F = json.load(io.open(base + r"\findings_326_330_recheck.json", encoding="utf-8"))
from collections import Counter
cnt = Counter()
for d in F:
    src = io.open(base + r"\b326_330\page_%03d.tex" % d["page"], encoding="utf-8", newline="").read()
    n_tex = src.count(d["tex"])
    msg = ""
    if d["fix"] is not None:
        n_old = src.count(d["fix"]["old"])
        msg = " fix.old count=%d" % n_old
    else:
        assert d["kind"] == "misprint_in_print"
    cnt[(d["page"], d["kind"] == "misprint_in_print")] += 1
    print(d["page"], d["kind"], "tex count=%d" % n_tex, msg, "|", d["tex"])
for p in range(326, 331):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
