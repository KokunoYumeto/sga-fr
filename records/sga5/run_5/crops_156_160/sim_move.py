"""Read-only simulation of move_marker.py (VOL FOLIO ANCHOR [--before]) on both layers; prints the context."""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = '--before' in sys.argv
print('anchor:', repr(anchor))
for edition in ('diplomatic', 'current'):
    t = open(base + edition + '/s5.tex', encoding='utf-8', newline='').read()
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == '\n' else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print(edition, 'anchor not found')
        continue
    ls = t2.rfind('\n', 0, k) + 1
    if t2[ls:k].strip() == '':
        t3 = t2[:ls] + line + '\n' + t2[ls:]
    else:
        t3 = t2[:k] + '\n' + line + '\n' + t2[k:]
    j = t3.find(line)
    print('==', edition, 'occurrences of anchor after old marker:', t2.count(anchor, m.start()))
    print(repr(t3[j - 160:j + len(line) + 80]))
    print('old place now reads:', repr(t2[m.start() - 60:m.start() + 30]))
