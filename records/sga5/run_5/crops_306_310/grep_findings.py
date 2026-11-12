import json, sys, glob, re, os
sys.stdout.reconfigure(encoding='utf-8')
pat = re.compile(sys.argv[1])
globs = sys.argv[2:]
for g in globs:
    for fn in sorted(glob.glob(g)):
        try:
            d = json.load(open(fn, encoding='utf-8'))
        except Exception as e:
            print('ERR', fn, e); continue
        for f in d:
            s = json.dumps(f, ensure_ascii=False)
            if pat.search(s):
                print(os.path.basename(fn), f.get('page'), f.get('kind'), '|', (f.get('where') or '')[:90], '|', (f.get('note') or '')[:350])
                print('   fix:', json.dumps(f.get('fix'), ensure_ascii=False)[:350])
