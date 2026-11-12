import sys
sys.stdout.reconfigure(encoding='utf-8')
L = open('C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split(chr(10))
pats = {'Kcirc': 'K^' + chr(92) + 'circ', 'Kprime': "K'", 'Sym': chr(92) + 'Sym', 'Projz': chr(92) + 'Projz', 'mathbfP': chr(92) + 'mathbf P'}
folio = None
rows = {}
for i in range(9153, 10480):
    s = L[i]
    if 'folio' in s and s.startswith('%%%%'):
        folio = int(s.split('folio')[1].split()[0])
    for k, p in pats.items():
        c = s.count(p)
        if c:
            rows.setdefault(k, {}).setdefault(folio, 0)
            rows[k][folio] += c
for k, d in rows.items():
    print(k, sum(d.values()), d)
