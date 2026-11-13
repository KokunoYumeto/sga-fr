"""Compare the batch page files b591_595/page_NNN.tex with the same pages in the live diplomatic main.tex, and
count each fix's old string in the live page (read only)."""
import difflib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
LIVE = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = LIVE.read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
live = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    live[int(m.group(2))] = t[m.start():end]
for p in range(591, 596):
    batch = (RUN / "b591_595" / f"page_{p}.tex").read_text(encoding="utf-8")
    batch = batch.split("\n", 1)[1]  # drop the '% from main.tex' line
    d = list(difflib.unified_diff(batch.splitlines(), live[p].splitlines(), "batch", "live", lineterm="", n=0))
    print(f"===== page {p}: {'identical' if not d else 'differs'}")
    for line in d[:40]:
        print(line[:220])
E = json.loads((RUN / "findings_591_595.json").read_text(encoding="utf-8"))
for e in E:
    if e["fix"]:
        print(e["page"], live[e["page"]].count(e["fix"]["old"]), repr(e["fix"]["old"][:50]))
