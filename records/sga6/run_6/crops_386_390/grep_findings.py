import json, glob, sys
sys.stdout.reconfigure(encoding="utf-8")
pats = sys.argv[1:]
for fn in sorted(glob.glob(r"C:/Users/user/Documents/sga_scan_check_20261105/run_6/findings_*.json")):
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception as e:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if any(p in s for p in pats):
            print(fn.split("/")[-1].split("\\")[-1], x.get("page"), "|", x.get("kind"), "|", s[:600])
            print()
