"""Apply the fixes of findings_056_060.json to the page texts in memory (nothing is written) and print the result."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((RUN / "findings_056_060.json").read_text(encoding="utf-8"))
for p in range(56, 61):
    t = (RUN / "b056_060" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for d in F:
        if d["page"] == p and d["fix"]:
            assert t.count(d["fix"]["old"]) == 1, d
            t = t.replace(d["fix"]["old"], d["fix"]["new"])
    print(f"===== page {p}")
    print(t)
