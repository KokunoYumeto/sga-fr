import json, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\MISPRINTS_5.json", encoding="utf-8"))
print(len(d))
for f in d:
    if 170 <= int(f["page"]) <= 186:
        print(json.dumps(f, ensure_ascii=False)[:700]); print()
