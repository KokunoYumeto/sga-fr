"""Read-only check: the findings JSON parses and every fix's 'old' occurs exactly once in its page_NNN.tex."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
items = json.loads((run / "findings_036_040.json").read_text(encoding="utf-8"))
counts = {}
for it in items:
    p = it["page"]
    k = "misprint" if it["kind"] == "misprint_in_print" else "normal"
    counts.setdefault(p, {"normal": 0, "misprint": 0})[k] += 1
    if it["kind"] == "misprint_in_print" and "corrected" not in it:
        print("missing corrected", p, it["where"])
    if it.get("fix"):
        tex = (run / "b036_040" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
        old = it["fix"]["old"]
        n = tex.count(old)
        print(p, repr(old), "count", n, "OK" if n == 1 else "PROBLEM", "| marker in old:", "scan idx" in old)
print(counts)
