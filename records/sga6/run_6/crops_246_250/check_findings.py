"""Check findings_246_250.json: JSON parses, every fix's old occurs exactly once in its page_NNN.tex,
and report its count in the live page span of both layers of main.tex (after the edit of the old)."""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
R = r'C:/Users/user/Documents/sga_scan_check_20261105/'
d = json.load(open(R + 'run_6/findings_246_250.json', encoding='utf-8'))
MARK = re.compile(r'^%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%$', re.M)
live = {}
for layer in ('diplomatic', 'current'):
    t = open(R + f'sga6/{layer}/main.tex', encoding='utf-8').read()
    ms = list(MARK.finditer(t))
    for k, m in enumerate(ms):
        f = int(m.group(2))
        if 246 <= f <= 250:
            live[(layer, f)] = t[m.start():ms[k + 1].start()]
ok = True
for i, x in enumerate(d):
    keys = set(x)
    need = {'page', 'where', 'scan', 'tex', 'kind', 'confidence', 'fix', 'note'}
    if not need <= keys:
        print(i, 'missing keys', need - keys); ok = False
    if x['kind'] == 'misprint_in_print' and 'corrected' not in x:
        print(i, 'misprint without corrected'); ok = False
    if x['kind'] != 'misprint_in_print' and 'corrected' in x:
        print(i, 'corrected on a non-misprint'); ok = False
    p = x['page']
    page = open(R + f'run_6/b246_250/page_{p}.tex', encoding='utf-8').read()
    if x['kind'] == 'misprint_in_print':
        s = x['tex'].replace(' (printed reading kept)', '')
        print(i, p, 'misprint tex substring count in page:', page.count(s))
    fx = x['fix']
    if fx:
        old = fx['old']
        if '%%%%%%%%%%' in old:
            print(i, 'old crosses a marker'); ok = False
        c = page.count(old)
        cl = [live[(l, p)].count(old) for l in ('diplomatic', 'current')]
        print(i, p, x['kind'], 'count in page:', c, '| live dipl/cur:', cl, '|', repr(old)[:60])
        if c != 1:
            ok = False
print('OK' if ok else 'PROBLEM')
# earlier "d'une" before the folio-251 marker (for the note on a second run)
t = open(R + 'sga6/diplomatic/main.tex', encoding='utf-8').read()
m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 251)
pos = t.rfind("d'une", 0, m.start())
pos2 = t.rfind("d'une", 0, pos)
before = [mm for mm in MARK.finditer(t) if mm.start() < pos2]
print("previous d'une before the boundary one: folio", before[-1].group(2), repr(t[pos2 - 40:pos2 + 20]))
