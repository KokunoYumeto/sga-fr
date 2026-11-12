import sys; sys.stdout.reconfigure(encoding="utf-8")
import json, glob, sys
keys = sys.argv[1:]
for f in sorted(glob.glob('findings_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if any(k.lower() in s.lower() for k in keys):
            print(f, x.get('page'), x.get('kind'), x.get('confidence'), '|', (x.get('note') or '')[:400])
            print('   fix:', json.dumps(x.get('fix'), ensure_ascii=False)[:300])
