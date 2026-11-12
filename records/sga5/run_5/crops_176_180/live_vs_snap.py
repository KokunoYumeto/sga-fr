"""Compare the live page spans of s5.tex (read only) with the batch snapshots page_176..180.tex."""
import sys, pathlib, difflib
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b176_180")
for edition in ("diplomatic", "current"):
    P = pages("5", edition)
    for folio in range(176, 181):
        live = "".join(f.read_text(encoding="utf-8")[s:e] for f, s, e in P[folio])
        snap = (B / f"page_{folio}.tex").read_text(encoding="utf-8")
        snap = snap.split("\n", 1)[1]  # drop '% from s5.tex'
        if live.rstrip("\n") == snap.rstrip("\n"):
            print(edition, folio, "identical")
        else:
            print(edition, folio, "DIFFERS")
            for l in difflib.unified_diff(snap.splitlines(), live.splitlines(), "snap", "live", n=0, lineterm=""):
                print("   ", l[:300])
