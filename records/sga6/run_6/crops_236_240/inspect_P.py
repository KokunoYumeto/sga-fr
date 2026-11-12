"""How projective space P is written in the TeX around Exposé III, and earlier fixes touching mathbb P."""
import json
import re

W = r"C:\Users\user\Documents\sga_scan_check_20261105"
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
ms = list(re.finditer(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%", t))
for i, m in enumerate(ms):
    f = int(m.group(2))
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    seg = t[m.start():end]
    a = seg.count(r"\mathbb P")
    b = seg.count(r"\mathbf P")
    c = len(re.findall(r"(?<![A-Za-z\\])P\^", seg))
    if (a or b or c) and 200 <= f <= 280:
        print(f, "mathbbP", a, "mathbfP", b, "plain P^", c)

print("---- fixes touching P")
for line in open(W + r"\FIXLOG_6.jsonl", encoding="utf-8"):
    d = json.loads(line)
    o, n = d.get("old") or "", d.get("new") or ""
    if (r"\mathbb P" in o) != (r"\mathbb P" in n) or (r"\mathbb{P}" in o) != (r"\mathbb{P}" in n):
        print(d.get("page"), d.get("kind"), repr(o[:90]), "=>", repr(n[:90]))
