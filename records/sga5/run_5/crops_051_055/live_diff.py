"""Read-only: diff the live s5.tex page spans (both layers) against the snapshot page_NNN.tex files of this batch."""
import difflib
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

for layer in ("diplomatic", "current"):
    pg = pages("5", layer)
    for n in range(50, 57):
        f, s, e = pg[n][0]
        live = f.read_text(encoding="utf-8")[s:e]
        p = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b051_055\page_{n:03d}.tex")
        if not p.exists():
            print(layer, n, "live first lines:", live[:200].replace("\n", " | "))
            continue
        snap = p.read_text(encoding="utf-8").split("\n", 1)[1]
        if live.rstrip() == snap.rstrip():
            print(layer, n, "same")
            continue
        print(layer, n, "DIFF")
        for d in difflib.unified_diff(snap.rstrip().split("\n"), live.rstrip().split("\n"), lineterm="", n=0):
            print("   ", d[:260])
