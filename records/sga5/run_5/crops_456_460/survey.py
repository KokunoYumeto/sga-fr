"""survey.py PATTERN [GLOB]: list fixes of earlier findings whose 'new' or 'note' matches PATTERN (regex)."""
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(sys.argv[1])
g = sys.argv[2] if len(sys.argv) > 2 else r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_*.json"
for fn in sorted(glob.glob(g)):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(fn, "ERR", e)
        continue
    for x in d:
        f = x.get("fix") or {}
        s = (f.get("new") or "") + " || " + (x.get("note") or "") + " || " + (x.get("scan") or "")
        if pat.search(s):
            print(fn.split("\\")[-1], x.get("page"), x.get("kind"), "| scan:", (x.get("scan") or "")[:160],
                  "| fix:", json.dumps(f, ensure_ascii=False)[:260], "| note:", (x.get("note") or "")[:260])
            print()
