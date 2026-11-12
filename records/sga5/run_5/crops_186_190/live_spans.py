"""Compare the live s5.tex page spans (both layers) of folios 185-191 with the batch snapshots (read-only)."""
import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105")
RUN = W / "run_5"


def spans(path):
    t = path.read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = t[m.start():end]
    return out


live = spans(W / "sga5" / "diplomatic" / "s5.tex")
for p in range(185, 191):
    snap = (RUN / ("b181_185" if p == 185 else "b186_190") / f"page_{p}.tex").read_text(encoding="utf-8")
    snap = snap.split("\n", 1)[1]  # drop the '% from s5.tex' line
    cur = live[p]
    if snap.rstrip("\n") == cur.rstrip("\n"):
        print(p, "identical")
        continue
    print("=====", p, "differs")
    for l in difflib.unified_diff(snap.split("\n"), cur.split("\n"), "snapshot", "live", lineterm="", n=1):
        print(l)
if "--current" in sys.argv:
    cur = spans(W / "sga5" / "current" / "s5.tex")
    for p in range(186, 191):
        print("##### current", p)
        print(cur[p])
