import re
p = r'C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex'
t = open(p, encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(t) if l.startswith('\\section*{Exposé X '))
end = next(i for i, l in enumerate(t) if l.startswith('\\section*{Exposé XII}'))
seg = '\n'.join(t[start:end])
print('Exposé X lines', start + 1, end)
pats = [r'\\Ob\b', r'\\et\b', r'\\etG\b', r'\\Mod\b', r'-modules?\b', r'-Modules?\b',
        r'Euler--Poincar', r'Euler-Poincar', r'\\emph\{', r'\\underline\{', r'\\mathbf\{n\}',
        r'\\mathbb\{L\}', r'\\pmod', r'\\longmapsto', '«', r' -- ', r'\\Lambda', r'\\La\b']
for pat in pats:
    print(repr(pat), len(re.findall(pat, seg)))
