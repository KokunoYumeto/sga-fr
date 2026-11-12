import json, re, sys, glob, os
sys.stdout.reconfigure(encoding='utf-8')

# usage: python grep_findings.py PATTERN [file globs...]
pat = re.compile(sys.argv[1])
files = sys.argv[2:] or sorted(glob.glob(os.path.join(os.path.dirname(__file__), '..', 'findings_*.json')))
for fn in files:
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception as e:
        continue
    for f in d:
        s = json.dumps(f, ensure_ascii=False)
        if pat.search(s):
            print(os.path.basename(fn), f.get('page'), json.dumps({k: f.get(k) for k in ('where', 'scan', 'tex', 'kind', 'fix', 'note')}, ensure_ascii=False))
