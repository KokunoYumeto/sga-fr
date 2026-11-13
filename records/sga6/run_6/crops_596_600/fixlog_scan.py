import json, sys, re
# usage: fixlog_scan.py <regex on note/where/kind text> [max]
p = r"C:/Users/user/Documents/sga_scan_check_20261105/FIXLOG_6.jsonl"
rx = re.compile(sys.argv[1], re.I)
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for line in open(p, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    try:
        d = json.loads(line)
    except Exception:
        continue
    s = json.dumps(d, ensure_ascii=False)
    if rx.search(s):
        n += 1
        if n <= mx:
            print(s[:700])
            print("--")
print("matches", n)
