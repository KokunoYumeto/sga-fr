import re, sys
p = sys.argv[1]
for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
    if l.startswith('\section') or re.search(r'Exposé|EXPOSÉ', l) and len(l) < 120:
        print(i, l[:110])
