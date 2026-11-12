"""Read-only: apply all fixes of findings_211_215.json to copies of the page texts in memory (in both orders) and
print the result; the misprint fixes are applied too (diplomatic layer). Nothing is written."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
F = json.loads((RUN / "findings_211_215.json").read_text(encoding="utf-8"))
for p in range(211, 216):
    t0 = (RUN / "b211_215" / ("page_%d.tex" % p)).read_text(encoding="utf-8")
    fixes = [d["fix"] for d in F if d["page"] == p and d["fix"]]
    results = []
    for order in (fixes, fixes[::-1]):
        t = t0
        for fx in order:
            assert t.count(fx["old"]) == 1, (p, fx["old"])
            t = t.replace(fx["old"], fx["new"])
        results.append(t)
    print("=" * 20, p, "same result in both orders:", results[0] == results[1])
    if "--show" in sys.argv:
        print(results[0])
