import sys
p = r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex"
lines = open(p, encoding="utf-8").read().split("\n")
needle = sys.argv[1].replace("BS", chr(92))
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
show = int(sys.argv[4]) if len(sys.argv) > 4 else 0
n = 0
for i, l in enumerate(lines, 1):
    if lo <= i <= hi and needle in l:
        n += 1
        if show:
            print(i, l[:300])
        else:
            print(i)
print("count", n)
