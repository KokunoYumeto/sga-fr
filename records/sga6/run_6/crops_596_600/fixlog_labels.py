import json
p = r"C:/Users/user/Documents/sga_scan_check_20261105/FIXLOG_6.jsonl"
n = 0
for line in open(p, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    try:
        d = json.loads(line)
    except Exception:
        continue
    o, w = d.get("old") or "", d.get("new") or ""
    if "arrow[" in o and ("\"'" in o) != ("\"'" in w):
        n += 1
        if n <= 12:
            print(d.get("page"), repr(o)[:200], "=>", repr(w)[:200])
print("label-swap fixes:", n)
