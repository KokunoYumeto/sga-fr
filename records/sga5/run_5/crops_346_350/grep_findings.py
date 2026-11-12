import json, sys, glob, re, os
sys.stdout.reconfigure(encoding='utf-8')
run = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5'
pat = re.compile(sys.argv[1])
lo, hi = int(sys.argv[2]), int(sys.argv[3])
for fn in sorted(glob.glob(os.path.join(run, 'findings_*.json'))):
    b = os.path.basename(fn)
    if 'orig' in b:
        continue
    m = re.match(r'findings_(\d+)_(\d+)\.json', b)
    if not m:
        continue
    a = int(m.group(1))
    if a < lo or a > hi:
        continue
    d = json.load(open(fn, encoding='utf-8'))
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            print(b, x.get('page'), x.get('kind'), x.get('confidence'), '|', x.get('where'), '|', (x.get('scan') or '')[:140])
            print('   tex:', (x.get('tex') or '')[:140])
            print('   note:', (x.get('note') or '')[:350])
            print('   fix:', json.dumps(x.get('fix'), ensure_ascii=False)[:300])
