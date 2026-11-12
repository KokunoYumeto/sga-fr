"""Print the TeX of folio N (between its marker and the next) for a layer.
usage: python -I page.py current|diplomatic FOLIO [FOLIO2]"""
import re, sys
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
layer, a = sys.argv[1], int(sys.argv[2])
b = int(sys.argv[3]) if len(sys.argv) > 3 else a
lines = open(base + layer + '/s5.tex', encoding='utf-8').read().split('\n')
mk = re.compile(r'^%{10}  scan idx \d+  \|  folio (\d+)  %{10}$')
cur = None
for i, l in enumerate(lines, 1):
    m = mk.match(l)
    if m:
        cur = int(m.group(1))
    if cur is not None and a <= cur <= b:
        print(f'{i}: {l}')
