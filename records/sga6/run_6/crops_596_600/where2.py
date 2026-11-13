import sys
# usage: where2.py <layer: diplomatic|current> <needle with BS for backslash> [context lines]
p = r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/%s/main.tex" % sys.argv[1]
lines = open(p, encoding="utf-8").read().split("\n")
needle = sys.argv[2].replace("BS", chr(92))
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 0
n = 0
for i, l in enumerate(lines, 1):
    if needle in l:
        n += 1
        k = l.find(needle)
        print(i, "...", l[max(0, k - 150):k + 150])
print("count", n)
