"""Search earlier findings files of the SGA 6 run for a regex in any field; print page, kind and a short excerpt.
usage: python -I grep_findings.py REGEX [MAXHITS]"""
import glob
import json
import re
import sys

pat = re.compile(sys.argv[1], re.I)
maxhits = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for f in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f, "unreadable", e)
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=True)
        if pat.search(s):
            n += 1
            if n <= maxhits:
                print(f[-20:], x.get("page"), x.get("kind"), "|", s[:600])
                print()
print("hits:", n)
