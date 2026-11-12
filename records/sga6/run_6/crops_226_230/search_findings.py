import glob
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
needles = [a.lower() for a in sys.argv[1:]]
root = r"C:\Users\user\Documents\sga_scan_check_20261105"
n = 0
for f in sorted(glob.glob(root + r"\run_6\findings_*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print("ERR", f, e)
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False).lower()
        if all(k in s for k in needles):
            n += 1
            print(f.split("\\")[-1], x.get("page"), x.get("kind"), x.get("confidence"))
            print("  where:", x.get("where", "")[:200])
            print("  scan:", x.get("scan", "")[:300])
            print("  tex:", x.get("tex", "")[:200])
            print("  fix:", json.dumps(x.get("fix"), ensure_ascii=False)[:400])
            print("  note:", x.get("note", "")[:400])
print(n)
