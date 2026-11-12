import json, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_171_175.json", encoding="utf-8"))
for f in d:
    if f["page"] >= 175 or f["kind"] == "marker":
        print(json.dumps(f, ensure_ascii=False)); print()
