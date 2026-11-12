import json, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
BS = "\\"
n = 0
for fn in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_1[2-5]*.json")):
    d = json.load(open(fn, encoding="utf-8"))
    for f in d:
        fx = f.get("fix") or {}
        o, nw = fx.get("old", ""), fx.get("new", "")
        if (BS + "lten" in o and BS + "otimes" in nw and BS + "lten" not in nw) or (BS + "uHom" in o and BS + "uHom" not in nw):
            n += 1
            if n < 10:
                print(fn.split("\\")[-1], json.dumps(f, ensure_ascii=False)[:600]); print()
print(n)
