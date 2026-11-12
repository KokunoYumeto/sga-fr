"""Read-only: check each fix's old against the live diplomatic layer's page segments (applied in order)."""
import json
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
L = json.loads((W / "run_5" / "findings_316_320.json").read_text(encoding="utf-8"))
t = (W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
seg = {}
for k, m in enumerate(ms):
    f = int(m.group(2))
    if 316 <= f <= 320:
        seg[f] = t[m.start():ms[k + 1].start()]
bad = 0
for i, d in enumerate(L):
    if not d["fix"]:
        continue
    p, o, n = d["page"], d["fix"]["old"], d["fix"]["new"]
    c = seg[p].count(o)
    if c != 1:
        bad += 1
        print("live layer count", c, "item", i, "page", p, repr(o[:70]))
    seg[p] = seg[p].replace(o, n, 1)
print("items checked against the live diplomatic layer; not exactly once:", bad)
