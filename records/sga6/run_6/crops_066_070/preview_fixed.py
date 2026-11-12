"""Apply the findings' fixes in memory to the page files and print the fixed pages (no writes).
usage: python -I preview_fixed.py"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
items = json.loads((RUN / "findings_066_070.json").read_text(encoding="utf-8"))
pages = {p: (RUN / "b066_070" / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(66, 71)}
for x in items:
    if x["fix"]:
        t = pages[x["page"]]
        assert t.count(x["fix"]["old"]) == 1, x
        pages[x["page"]] = t.replace(x["fix"]["old"], x["fix"]["new"])
for p, t in pages.items():
    print("=" * 20, p)
    print(t)
