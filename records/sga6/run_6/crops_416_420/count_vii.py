import io, re
L = io.open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
start, end = 10490, 11931
txt = '\n'.join(L[start:end])
pats = {
    'underline': r'\\underline\{',
    'emph': r'\\emph\{',
    'K^circ': r'K\^\\circ',
    'K^{bullet}': r'K\^\{\\bullet\}',
    'K^bullet': r'K\^\\bullet',
    'K_bullet': r'K_\\bullet',
    'cO': r'\\cO',
    'emph Demonstration': r'\\emph\{D.monstration',
    'emph Preuve': r'\\emph\{Preuve',
    'Demonstration.': r'D.monstration\.',
}
for k, p in pats.items():
    print(k, len(re.findall(p, txt)))
for m in re.finditer(r'\\underline\{[^}]*\}', txt):
    print('U:', m.group(0))
