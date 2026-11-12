"""Compare page_NNN.tex snapshots with the live diplomatic main.tex text between the same markers (read only)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b296_300")
t = M.read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
for folio in range(296, 301):
    i = next(k for k, m in enumerate(ms) if int(m.group(2)) == folio)
    live = t[ms[i].start():ms[i + 1].start()]
    snap = (B / f"page_{folio}.tex").read_text(encoding="utf-8")
    snap = snap[snap.index("%%%%%%%%%%"):]
    print(folio, "same" if live.rstrip() == snap.rstrip() else "DIFFERENT", len(live), len(snap))
    print("   line above marker:", repr(t[t.rfind("\n", 0, ms[i].start() - 1) + 1:ms[i].start()][-80:]))
