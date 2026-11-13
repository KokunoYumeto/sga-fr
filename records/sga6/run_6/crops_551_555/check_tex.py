import json, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
run = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6')
d = json.load(open(run / 'findings_551_555.json', encoding='utf-8'))
for i, x in enumerate(d):
    if x['kind'] == 'misprint_in_print':
        t = (run / 'b551_555' / f"page_{x['page']}.tex").read_text(encoding='utf-8')
        print(i, x['page'], repr(x['tex']), 'count', t.count(x['tex']), '| corrected', repr(x['corrected']))
