import json, glob, sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
pat = re.compile(sys.argv[1], re.I)
files = sys.argv[2:] if len(sys.argv) > 2 else sorted(glob.glob('C:/Users/user/Documents/sga_scan_check_20261105/run_5/findings_*.json'))
for f in files:
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            print(os.path.basename(f), x.get('page'), x.get('kind'), '|', x.get('where'), '|', json.dumps(x.get('fix'), ensure_ascii=False)[:250], '|', (x.get('note') or '')[:350])
