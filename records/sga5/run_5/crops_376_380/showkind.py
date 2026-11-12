import json, sys
sys.stdout.reconfigure(encoding='utf-8')
kind = sys.argv[1]
for f in sys.argv[2:]:
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        if kind == '*' or x.get('kind') == kind:
            print(f.split('/')[-1], x.get('page'), '|', (x.get('where') or '')[:70], '|', json.dumps(x.get('fix'), ensure_ascii=False)[:260], '|', (x.get('note') or '')[:200])
