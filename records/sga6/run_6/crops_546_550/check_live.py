"""Check every fix's old string against the present page spans of main.tex (both layers), read-only."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

F = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_546_550.json", encoding="utf-8"))
for edition in ("diplomatic", "current"):
    pg = pages("6", edition)
    for d in F:
        if not d["fix"]:
            continue
        spans = pg.get(d["page"], [])
        n = 0
        for f, s, e in spans:
            n += f.read_text(encoding="utf-8")[s:e].count(d["fix"]["old"])
        print(edition, d["page"], n, repr(d["fix"]["old"])[:50])
