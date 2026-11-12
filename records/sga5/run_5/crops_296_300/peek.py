import sys
sys.stdout.reconfigure(encoding="utf-8")
p, s = sys.argv[1], sys.argv[2].encode("utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b296_300\page_%s.tex" % p, encoding="utf-8").read()
print("count", t.count(s))
i = t.find(s)
while i >= 0:
    print(repr(t[max(0, i - 30):i + len(s) + 30]))
    i = t.find(s, i + 1)
