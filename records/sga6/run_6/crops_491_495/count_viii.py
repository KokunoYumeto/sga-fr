"""Count some forms per folio in Exposé VIII (diplomatic main.tex, folios 466-?)."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(L) if l.startswith('%%%%') and 'folio 466 ' in l)
end = next(i for i, l in enumerate(L) if 'section*{Exposé IX' in l)
pats = {
    'S(E)': r'S\(E\)',
    'Sym': r'\\Sym\b',
    'mathbb P': r'\\mathbb P',
    'mathbf': r'\\mathbf',
    'bfP': r'\\bfP',
    'cS': r'\\cS\b',
    'underline': r'\\underline',
    'emph': r'\\emph',
    'mathcal O': r'\\mathcal O',
    'cO': r'\\cO\b',
    'Ker': r'\\Ker\b',
}
folio = None
cnt = {}
for l in L[start:end]:
    m = re.search(r'folio (\d+)', l)
    if m and l.startswith('%%%%'):
        folio = int(m.group(1))
        continue
    for name, pat in pats.items():
        n = len(re.findall(pat, l))
        if n:
            cnt.setdefault(name, {})
            cnt[name][folio] = cnt[name].get(folio, 0) + n
for name in pats:
    print(name, cnt.get(name, {}))
print('lines', start + 1, end)
