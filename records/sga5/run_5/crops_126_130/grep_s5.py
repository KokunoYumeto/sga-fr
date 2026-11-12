"""usage: python -I grep_s5.py PATTERN [maxhits] [lo] [hi]
regex search in the diplomatic s5.tex; '@' in PATTERN stands for a literal backslash. Prints line numbers."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
pat = re.compile(sys.argv[1].replace('@', r'\\'))
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 40
lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0
hi = int(sys.argv[4]) if len(sys.argv) > 4 else 10**9
lines = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga5/diplomatic/s5.tex', encoding='utf-8').read().split('\n')
n = 0
for i, l in enumerate(lines, 1):
    if lo <= i <= hi and pat.search(l):
        n += 1
        if n <= mx:
            m = pat.search(l)
            s = max(0, m.start() - 80)
            print(i, '...', l[s:m.end() + 80])
print('hits:', n)
