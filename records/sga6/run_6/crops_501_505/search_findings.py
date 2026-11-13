"""search_findings.py REGEX [LIMIT]: print findings (all run_6 findings files) whose JSON matches REGEX."""
import json, sys, glob, re, os
sys.stdout.reconfigure(encoding='utf-8')
pat = re.compile(sys.argv[1])
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for fn in sorted(glob.glob(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for f in d:
        s = json.dumps(f, ensure_ascii=False)
        if pat.search(s):
            n += 1
            if n <= lim:
                print(os.path.basename(fn), f.get('page'), f.get('kind'), '|', (f.get('where') or '')[:150], '|',
                      json.dumps(f.get('fix'), ensure_ascii=False)[:200], '|', (f.get('note') or '')[:400])
                print()
print(n)
