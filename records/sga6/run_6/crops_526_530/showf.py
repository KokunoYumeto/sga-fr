import json, sys
sys.stdout.reconfigure(encoding='utf-8')
# usage: python -I showf.py KINDS(comma list or all) FILE...
kinds = sys.argv[1].split(',')
for fn in sys.argv[2:]:
    d = json.load(open(fn, encoding='utf-8'))
    print(fn, len(d))
    for f in d:
        if 'all' in kinds or f.get('kind') in kinds:
            print(json.dumps(f, ensure_ascii=False)[:1500])
            print()
