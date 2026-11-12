import re, sys, difflib, pathlib
sys.stdout.reconfigure(encoding='utf-8')
main = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex').read_text(encoding='utf-8').split('\n')
b = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\b241_245')
idx = {}
for i, l in enumerate(main):
    m = re.search(r'folio (\d+)\s', l)
    if l.startswith('%%%%%%%%%%') and m:
        idx[int(m.group(1))] = i
for p in range(241, 246):
    s, e = idx[p], idx[p + 1]
    live = main[s:e]
    snap = (b / f'page_{p}.tex').read_text(encoding='utf-8').split('\n')[1:]
    while snap and snap[-1] == '':
        snap.pop()
    while live and live[-1] == '':
        live.pop()
    d = list(difflib.unified_diff(snap, live, 'snapshot', 'live', lineterm='', n=0))
    print(p, 'identical' if not d else '')
    for x in d:
        print('   ', x[:300])
