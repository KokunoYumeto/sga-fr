"""count a regex per folio in a layer.  usage: count.py layer regex [fmin fmax]"""
import re, sys, collections
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
layer, rx = sys.argv[1], re.compile(sys.argv[2])
fmin = int(sys.argv[3]) if len(sys.argv) > 3 else 0
fmax = int(sys.argv[4]) if len(sys.argv) > 4 else 10**6
mk = re.compile(r'^%{10}  scan idx \d+  \|  folio (\d+)  %{10}$')
cur = 0; c = collections.Counter()
for l in open(base + layer + '/s5.tex', encoding='utf-8').read().split('\n'):
    m = mk.match(l)
    if m: cur = int(m.group(1)); continue
    if fmin <= cur <= fmax:
        n = len(rx.findall(l))
        if n: c[cur] += n
print(sum(c.values()), dict(sorted(c.items())))
