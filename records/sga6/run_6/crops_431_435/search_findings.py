import json, sys, glob, re, os
sys.stdout.reconfigure(encoding='utf-8')
pat1 = re.compile(sys.argv[1], re.I)
pat2 = re.compile(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else None
lim = int(sys.argv[3]) if len(sys.argv) > 3 else 15
n = 0
for fn in sorted(glob.glob(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for f in d:
        s = json.dumps(f, ensure_ascii=False)
        if pat1.search(s) and (pat2 is None or pat2.search(s)):
            n += 1
            if n <= lim:
                print(os.path.basename(fn), f.get('page'), f.get('kind'), '|', f.get('scan', '')[:220], '|',
                      json.dumps(f.get('fix'), ensure_ascii=False)[:220], '|', (f.get('note') or '')[:300])
                print()
print(n)
