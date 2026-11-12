import json, glob, os, sys
key_old = sys.argv[1]
key_new = sys.argv[2] if len(sys.argv) > 2 else None
hits = 0
for f in sorted(glob.glob('MANUAL_*.json')) + sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    if isinstance(d, dict):
        d = d.get('findings', [])
    for x in d:
        fx = x.get('fix') or {}
        if key_old in fx.get('old', '') and (key_new is None or key_new in fx.get('new', '')):
            hits += 1
            if hits <= 8:
                print(os.path.basename(f), '|', x.get('kind'), '|', json.dumps(fx, ensure_ascii=False)[:200], '|', x.get('note', '')[:160])
print('total', hits)
