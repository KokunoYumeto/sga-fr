"""Simulate (in memory only, nothing is written) move_marker.py VOL FOLIO ANCHOR [--before] on both layers of SGA 5
and print the text around the marker after the move.
usage: python -I sim_marker.py FOLIO ANCHOR [--before]"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
base = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'sga5')
MARK = re.compile(r'%{10}\s+scan idx (\d+)\s+\|\s+folio (\d+)\s+%{10}')
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = '--before' in sys.argv
for edition in ('diplomatic', 'current'):
    t = open(os.path.join(base, edition, 's5.tex'), encoding='utf-8', newline='').read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        print(edition, 'marker not found'); continue
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == '\n' else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(edition, 'anchor not found'); continue
    ls = t2.rfind('\n', 0, k) + 1
    if t2[ls:k].strip() == '':
        t3 = t2[:ls] + line + '\n' + t2[ls:]
    else:
        t3 = t2[:k] + '\n' + line + '\n' + t2[k:]
    j = t3.find(line)
    print('==', edition, 'moved by', k - m.start(), 'chars')
    print(t3[max(0, j - 160):j + len(line) + 120])
    print()
