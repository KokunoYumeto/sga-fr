"""Print a unified diff of the diplomatic and current layers between two folio markers (reads only)."""
import difflib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga6/'
a, b = int(sys.argv[1]), int(sys.argv[2])
def span(layer):
    t = open(base + layer + '/main.tex', encoding='utf-8').read()
    i = t.index('|  folio %d  %%' % a); i = t.rfind('\n', 0, i) + 1
    j = t.index('|  folio %d  %%' % b); j = t.rfind('\n', 0, j) + 1
    return t[i:j].splitlines()
for l in difflib.unified_diff(span('diplomatic'), span('current'), 'diplomatic', 'current', n=0, lineterm=''):
    print(l)
