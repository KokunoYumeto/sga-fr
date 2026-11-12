import sys
sys.stdout.reconfigure(encoding="utf-8")
pats = sys.argv[1:]
base = r"C:\Users\user\Documents\sga_scan_check_20261105"
for fn in ["FIXLOG_5.jsonl", "FIXLOG_5_CURRENT.jsonl"]:
    n = 0
    for line in open(base + "\\" + fn, encoding="utf-8"):
        if any(p in line for p in pats):
            print(fn, line.strip()[:420]); n += 1
    print(fn, "count", n)
for lay in ["diplomatic", "current"]:
    t = open(base + "\sga5\\" + lay + "\s5.tex", encoding="utf-8").read()
    for p in pats:
        print(lay, repr(p), t.count(p))
