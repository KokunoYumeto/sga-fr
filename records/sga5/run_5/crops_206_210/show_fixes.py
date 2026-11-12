import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'run_5')
d = json.load(open(os.path.join(RUN, 'findings_206_210.json'), encoding='utf-8'))
for x in d:
    if x['fix']:
        print(x['page'], x['kind'], repr(x['fix']['old']), '=>', repr(x['fix']['new']))
    else:
        print(x['page'], x['kind'], 'fix null', x.get('corrected', ''))
