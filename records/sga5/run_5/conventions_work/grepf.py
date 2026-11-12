"""grep a regex with folio and line. usage: grepf.py layer regex fmin fmax [width]"""
import re, sys
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
layer, rx = sys.argv[1], re.compile(sys.argv[2])
fmin, fmax = int(sys.argv[3]), int(sys.argv[4])
w = int(sys.argv[5]) if len(sys.argv) > 5 else 50
mk = re.compile(r'^%{10}  scan idx \d+  \|  folio (\d+)  %{10}$')
cur = 0
for i, l in enumerate(open(base + layer + '/s5.tex', encoding='utf-8').read().split('\n'), 1):
    m = mk.match(l)
    if m: cur = int(m.group(1)); continue
    if fmin <= cur <= fmax:
        for mm in rx.finditer(l):
            print(f'{cur} L{i}: ...{l[max(0,mm.start()-w):mm.end()+w]}...')
