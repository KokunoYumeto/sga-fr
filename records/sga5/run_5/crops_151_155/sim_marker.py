"""Simulate move_marker.py VOL=5 FOLIO=155 ANCHOR='\\[' --before in memory (no write) on both layers."""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BS = chr(92)
anchor = BS + '['
folio = 155
for edition in ('diplomatic', 'current'):
    p = r'C:\Users\user\Documents\sga_scan_check_20261105\sga5' + '\\' + edition + r'\s5.tex'
    t = open(p, encoding='utf-8', newline='').read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == '\n' else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind('\n', 0, k) + 1
    if t2[ls:k].strip() == '':
        t2 = t2[:ls] + line + '\n' + t2[ls:]
    else:
        t2 = t2[:k] + '\n' + line + '\n' + t2[k:]
    i = t2.find(line)
    print('==', edition)
    print(repr(t2[i - 60:i + len(line) + 90]))
