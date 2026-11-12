"""Count each fix's old string in the live s5.tex of both layers, within the page's present marker region
(pages 41-45; text of p. 45 runs to the folio-46 marker). Read-only.
usage: python -I live_check.py"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
F = json.load(open(root / "run_5" / "findings_041_045.json", encoding="utf-8"))
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for ed in ("diplomatic", "current"):
    t = (root / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    ms = {int(m.group(2)): m for m in MARK.finditer(t)}
    for i, d in enumerate(F):
        if not d["fix"]:
            continue
        p = d["page"]
        region = t[ms[p].start():ms[p + 1].start()]
        n = region.count(d["fix"]["old"])
        flag = "" if n == 1 else "  <-- CHECK"
        print(ed, i, p, d["kind"], n, flag)
