"""Search earlier findings files of run_6 for a regex (read only).
usage: python -I search_findings.py REGEX [MAX]"""
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
rx = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for f in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f, "ERR", e)
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if rx.search(s):
            n += 1
            if n <= mx:
                print(f.split("\\")[-1], s[:700])
                print()
print("matches:", n)
