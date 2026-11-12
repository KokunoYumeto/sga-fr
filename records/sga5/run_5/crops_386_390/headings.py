import json, re
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
BS = chr(92)
L = [json.loads(l) for l in open(W + r"\FIXLOG_5.jsonl", encoding="utf-8") if l.strip()]
for r in L:
    o, nw = r.get("old") or "", r.get("new") or ""
    if "subsubsection*{" in o and re.search(r"subsubsection\*\{[0-9.]+\}", o):
        print(r.get("page"), r.get("kind"), repr(o)[:100], "->", repr(nw)[:100])
t = open(W + r"\sga5\diplomatic\s5.tex", encoding="utf-8").read()
lines = t.split("\n")
seg = lines[12683:13753]
for i, l in enumerate(seg):
    if l.startswith(BS + "subsubsection*{") or l.startswith(BS + "subsection*{") or l.startswith(BS + "section*{"):
        print(12684 + i, l[:100])
