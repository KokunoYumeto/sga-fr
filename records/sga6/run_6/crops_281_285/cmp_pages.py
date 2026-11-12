"""Compare the batch page files with the current spans of main.tex (diplomatic), print differences."""
import difflib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
main = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
batch = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b281_285"
t = open(main, encoding="utf-8", newline="").read()
ms = list(MARK.finditer(t))
pos = {int(m.group(2)): (m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t)) for i, m in enumerate(ms)}
for folio in range(280, 287):
    s, e = pos[folio]
    span = t[s:e]
    try:
        page = open(batch + "\\page_%03d.tex" % folio, encoding="utf-8", newline="").read()
        page = page.split("\n", 1)[1]  # drop '% from main.tex'
    except FileNotFoundError:
        print("== folio", folio, "span starts:", repr(span[:160]), "ends:", repr(span[-160:]))
        continue
    if span == page:
        print("== folio", folio, "identical")
    else:
        print("== folio", folio, "DIFFERS")
        for l in difflib.unified_diff(page.split("\n"), span.split("\n"), "batch", "main", lineterm="", n=1):
            print(l[:300])
