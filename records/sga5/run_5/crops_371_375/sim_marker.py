"""Read-only simulation of move_marker.py 5 375 '\\[' --before on both editions (nothing is written)."""
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor, before = 375, '\\[', True
for edition in ('diplomatic', 'current'):
    p = r'C:\Users\user\Documents\sga_scan_check_20261105\sga5\%s\s5.tex' % edition
    t = open(p, encoding='utf-8', newline='').read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == '\n' else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind('\n', 0, k) + 1
    if t2[ls:k].strip() == '':
        t2 = t2[:ls] + line + '\n' + t2[ls:]
    else:
        t2 = t2[:k] + '\n' + line + '\n' + t2[k:]
    i = t2.index(line)
    print('==', edition)
    print(t2[i - 160:i + len(line) + 120])
