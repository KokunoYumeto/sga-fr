"""Search earlier findings files of this run for a regex (helper for consistency)."""
import glob
import json
import re
import sys

pat = re.compile(sys.argv[1], re.I)
kind = sys.argv[2] if len(sys.argv) > 2 else None
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 8
n = 0
for f in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for x in d:
        if kind and x.get("kind") != kind:
            continue
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            n += 1
            if n <= limit:
                print(f.split("\\")[-1], "|", s[:700])
                print()
print("total", n)
