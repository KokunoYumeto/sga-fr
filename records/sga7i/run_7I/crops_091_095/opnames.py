import re
import sys

path = sys.argv[1]
lines = open(path, encoding='utf-8').read().split('\n')
folio = None
fol = {}
for i, l in enumerate(lines, 1):
    m = re.search(r'folio (\d+)', l)
    if m and l.startswith('%%%%'):
        folio = int(m.group(1))
    fol[i] = folio

pats = [
    r'\\operatorname\{Supp\}',
    r'\\mathrm\{Supp\}',
    r'\\mathrm\{Sing\}',
    r'\\underline\{\\mathrm\{Hom',
    r'\\underline\{Hom\}',
    r'(?<![a-zA-Z{\\])ob\(',
    r'(?<![a-zA-Z{\\])Ker\(',
    r'(?<![a-zA-Z{\\])Supp',
    r'\^\{Sing\}',
]
for pat in pats:
    hits = []
    for i, l in enumerate(lines, 1):
        if l.startswith('%'):
            continue
        n = len(re.findall(pat, l))
        if n:
            hits.append((i, fol[i], n))
    print(pat, hits)
