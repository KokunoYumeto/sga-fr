import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
pat = re.compile(r"mathcal\s*\{?[HE]\}?\s*(\\!)?\s*(om|xt)|\\cH\s*om|\\cE\s*xt|\\uHom|\\uExt|\\SheafHom|\\SheafExt")
hits = []
for f in sorted(glob.glob(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json")):
    try:
        L = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for x in L:
        t = (x.get("tex") or "") + " " + json.dumps(x.get("fix"), ensure_ascii=False)
        if pat.search(t):
            hits.append((f.split("\\")[-1], x.get("page"), x.get("kind"), (x.get("scan") or "")[:100],
                         (x.get("tex") or "")[:100], (x.get("note") or "")[:220]))
print(len(hits))
for h in hits[:40]:
    print(h)
