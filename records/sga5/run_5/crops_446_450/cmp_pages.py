import re
import sys

# Compare the page snapshots page_NNN.tex with the live diplomatic s5.tex (read only).
sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex", encoding="utf-8", newline="").read()
ms = list(MARK.finditer(t))
spans = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    spans[int(m.group(2))] = t[m.start():end]
for folio in range(446, 452):
    d = "b451_455" if folio >= 451 else "b446_450"
    snap = open(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\{d}\page_{folio}.tex", encoding="utf-8", newline="").read()
    body = snap.split("\n", 1)[1]  # drop the '% from s5.tex' line
    live = spans[folio]
    print(folio, "same" if body.rstrip("\n") == live.rstrip("\n") else "DIFFERENT", len(body), len(live))
