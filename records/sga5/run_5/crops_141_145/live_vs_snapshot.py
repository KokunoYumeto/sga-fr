"""Read-only: compare the live page spans of pp. 140-145 (both layers) with the batch snapshot files."""
import difflib
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
for edition in ("diplomatic", "current"):
    pg = pages("5", edition)
    for folio in range(140, 147):
        live = "".join(f.read_text(encoding="utf-8")[s:e] for f, s, e in pg.get(folio, []))
        snap_dir = RUN / ("b136_140" if folio <= 140 else "b141_145" if folio <= 145 else "b146_150")
        snap_file = snap_dir / f"page_{folio}.tex"
        snap = snap_file.read_text(encoding="utf-8") if snap_file.exists() else ""
        snap_body = snap.split("\n", 1)[1] if snap.startswith("% from") else snap
        if live.rstrip("\n") == snap_body.rstrip("\n"):
            print(edition, folio, "same as snapshot")
            continue
        print(edition, folio, "DIFFERS from snapshot")
        for l in difflib.unified_diff(snap_body.split("\n"), live.split("\n"), lineterm="", n=0):
            print("   ", l[:220])
