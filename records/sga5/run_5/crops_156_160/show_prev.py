import json, sys
sys.stdout.reconfigure(encoding='utf-8')
keys = sys.argv[1].split('|')
for fn in sys.argv[2:]:
    d = json.load(open(fn, encoding='utf-8'))
    for f in d:
        s = json.dumps(f, ensure_ascii=False)
        if any(k in s for k in keys):
            print(fn.split('/')[-1], f.get('page'), f.get('kind'), '|', (f.get('where') or '')[:90], '|',
                  json.dumps(f.get('fix'), ensure_ascii=False)[:220], '|', (f.get('note') or '')[:260])
