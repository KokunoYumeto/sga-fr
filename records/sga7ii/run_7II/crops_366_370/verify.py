import json, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II"
d = json.load(open(base + r"\findings_366_370_recheck.json", encoding="utf-8"))
from collections import Counter
cnt = Counter()
for i, f in enumerate(d):
    p = f["page"]
    txt = open(base + rf"\b366_370\page_{p}.tex", encoding="utf-8", newline="").read()
    assert "\r" not in txt
    tex_n = txt.count(f["tex"])
    line = f"{i:2d} p{p} {f['kind']:18s} tex-count={tex_n}"
    if f["fix"] is not None:
        old = f["fix"]["old"]
        n = txt.count(old)
        line += f" old-count={n}"
        # check old not crossing marker line
        assert "%%%%%%%%%%" not in old
        new_txt = txt.replace(old, f["fix"]["new"])
        assert new_txt != txt
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f
        cnt[(p, "m")] += 1
    else:
        assert "corrected" not in f
        cnt[(p, "n")] += 1
    print(line)
for p in range(366, 371):
    print(p, f"{cnt[(p,'n')]}/{cnt[(p,'m')]}")
