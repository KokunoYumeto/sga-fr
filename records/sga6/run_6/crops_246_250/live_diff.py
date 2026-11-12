"""Compare the page snapshots page_NNN.tex with the live spans of main.tex (diplomatic) for folios 246-250."""
import difflib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r'^%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%$', re.M)
root = r'C:/Users/user/Documents/sga_scan_check_20261105/'
t = open(root + 'sga6/diplomatic/main.tex', encoding='utf-8').read()
ms = list(MARK.finditer(t))
for folio in range(246, 251):
    i = next(k for k, m in enumerate(ms) if int(m.group(2)) == folio)
    live = t[ms[i].start():ms[i + 1].start()]
    snap = open(root + f'run_6/b246_250/page_{folio}.tex', encoding='utf-8').read()
    snap = snap.split('\n', 1)[1]  # drop '% from main.tex'
    if live == snap:
        print(folio, 'identical')
    else:
        print(folio, 'DIFFERS')
        for l in difflib.unified_diff(snap.split('\n'), live.split('\n'), 'snapshot', 'live', lineterm='', n=0):
            print('   ', l[:300])
