"""For each fix of findings_271_275.json, count its old in the page's span of both layers (diplomatic, current)."""
import json
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
F = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_271_275.json", encoding="utf-8"))
P = {ed: pages("6", ed) for ed in ("diplomatic", "current")}
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    out = []
    for ed in ("diplomatic", "current"):
        n = 0
        for f, a, b in P[ed][d["page"]]:
            n += f.read_text(encoding="utf-8")[a:b].count(fx["old"])
        out.append(f"{ed}={n}")
    print(d["page"], d["kind"], " ".join(out), repr(fx["old"][:60]))
