import re
import sys

lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
want = {int(x) for x in sys.argv[2].split(',')}
folio = None
for i, l in enumerate(lines, 1):
    m = re.search(r'scan idx \d+\s*\|\s*folio (\d+)', l)
    if m:
        folio = int(m.group(1))
        continue
    if folio not in want or l.lstrip().startswith('%'):
        continue
    for key in ('\\varepsilon', '\\wedge'):
        j = l.find(key)
        if j >= 0:
            print(folio, i, key, '|', l[max(0, j - 45):j + 30])
            break
