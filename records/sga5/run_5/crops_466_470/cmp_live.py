"""Compare page_NNN.tex files of this batch with the live s5.tex spans (both layers); read-only."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

RUN = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
for ed in ("diplomatic", "current"):
    pg = pages("5", ed)
    for n in range(465, 472):
        f, s, e = pg[n][0]
        live = f.read_text(encoding="utf-8")[s:e]
        b = (n - 1) // 5 * 5 + 1
        pf = RUN / f"b{b:03d}_{b + 4:03d}" / f"page_{n:03d}.tex"
        if not pf.exists():
            print(ed, n, "no page file")
            continue
        pt = pf.read_text(encoding="utf-8").split("\n", 1)[1]
        same = pt.rstrip() == live.rstrip()
        line = f.read_text(encoding="utf-8")[:s].count("\n") + 1
        print(ed, n, "marker line", line, "same as page file" if same else "DIFFERS")
        if not same:
            import difflib
            for d in difflib.unified_diff(pt.splitlines(), live.splitlines(), lineterm="", n=0):
                print("   ", d[:300])
