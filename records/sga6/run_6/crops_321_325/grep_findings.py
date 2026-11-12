"""Print earlier findings whose fix 'old' matches a regex (argument 1), at most N (argument 2)."""
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(sys.argv[1])
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 8
n = 0
for fn in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json")):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for f in d:
        fx = f.get("fix")
        old = fx.get("old", "") if isinstance(fx, dict) else ""
        new = fx.get("new", "") if isinstance(fx, dict) else ""
        if pat.search(old) or pat.search(new):
            print(fn.split("\\")[-1], json.dumps(f, ensure_ascii=False)[:500])
            print()
            n += 1
            if n >= limit:
                sys.exit()
