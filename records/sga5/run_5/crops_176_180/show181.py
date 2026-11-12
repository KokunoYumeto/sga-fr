import json, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\findings_181_185.json", encoding="utf-8"))
for f in d:
    if f["kind"] == "marker" or f["page"] == 181:
        print(json.dumps(f, ensure_ascii=False)[:1500]); print()
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex", encoding="utf-8").read()
k = t.find("folio 181  %")
print(repr(t[k-400:k+120]))
