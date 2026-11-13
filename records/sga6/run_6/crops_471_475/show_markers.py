import json, glob, sys, os
sys.stdout.reconfigure(encoding="utf-8")
pat = sys.argv[1] if len(sys.argv) > 1 else "findings_4*.json"
kind = sys.argv[2] if len(sys.argv) > 2 else "marker"
lim = int(sys.argv[3]) if len(sys.argv) > 3 else 6
fs = sorted(glob.glob(os.path.join(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6", pat)))
n = 0
for f in fs:
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print(f, e)
        continue
    for x in d:
        if x.get("kind") == kind:
            print(os.path.basename(f), json.dumps(x, ensure_ascii=False)[:1500])
            print()
            n += 1
    if n >= lim:
        break
