"""usage: python -I searchfind.py SUBSTRING [SUBSTRING2]  -- search earlier findings_*.json of run_6 for entries containing all substrings"""
import json, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
subs = sys.argv[1:]
for fn in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json")):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if all(u in s for u in subs):
            f = x.get("fix") or {}
            print(fn[-20:], x.get("page"), x.get("kind"), repr(f.get("old"))[:100], "=>", repr(f.get("new"))[:100], "|", (x.get("note") or "")[:260])
