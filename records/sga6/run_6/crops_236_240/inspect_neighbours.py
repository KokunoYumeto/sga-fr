"""Show how R is written on neighbouring Exposé III pages and which fixes were applied there."""
import json
import re

W = r"C:\Users\user\Documents\sga_scan_check_20261105"
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
ms = list(re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", t))
pat = re.compile(r".{14}(?:R ?f_\*|\\mathbb R|\\mathrm R|\\R\b).{8}")
for i, m in enumerate(ms):
    f = int(m.group(2))
    if 228 <= f <= 246 and not 236 <= f <= 240:
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        seg = t[m.start():end]
        print(f, [h for h in pat.findall(seg)][:4])

print("---- applied fixes pp. 221-235, 241-246")
for line in open(W + r"\FIXLOG_6.jsonl", encoding="utf-8"):
    d = json.loads(line)
    p = d.get("page")
    if isinstance(p, int) and (221 <= p <= 235 or 241 <= p <= 246):
        print(p, d.get("kind"), repr((d.get("old") or "")[:100]), "=>", repr((d.get("new") or "")[:160]))
