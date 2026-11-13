import re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open(r'C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex', encoding='utf-8').read()
lines = t.split('\n')
pat = re.compile(open(sys.argv[1], encoding="utf-8").read().strip())
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
hi = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
width = int(sys.argv[4]) if len(sys.argv) > 4 else 220
n = 0
for i, l in enumerate(lines):
    if lo <= i + 1 <= hi:
        for m in pat.finditer(l):
            s = max(0, m.start() - 60); e = min(len(l), m.end() + 60)
            print(i + 1, '|', l[s:e][:width]); n += 1
print('matches:', n)
