import json, glob, sys, os
sys.stdout.reconfigure(encoding='utf-8')
n = 0
kind = sys.argv[1] if len(sys.argv) > 1 else 'marker'
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 8
pat = sys.argv[3] if len(sys.argv) > 3 else 'findings_*.json'
base = os.path.join('C:' + os.sep, 'Users', 'user', 'Documents', 'sga_scan_check_20261105', 'run_5')
for f in sorted(glob.glob(os.path.join(base, pat))):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        print(f, 'ERR', e); continue
    for x in d:
        if kind == '*' or x.get('kind') == kind:
            n += 1
            if n <= lim:
                print(os.path.basename(f), json.dumps(x, ensure_ascii=False)[:1500]); print()
print(n)
