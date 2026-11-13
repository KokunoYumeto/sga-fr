import json, sys
sys.stdout.reconfigure(encoding='utf-8')
# usage: fixlog_search.py FIXLOG substring [substring ...]
# prints fixes whose old contains the substring and whose new does not (removed), and vice versa (added)
path = sys.argv[1]
subs = sys.argv[2:]
rows = []
for line in open(path, encoding='utf-8'):
    line = line.strip()
    if line:
        rows.append(json.loads(line))
for s in subs:
    rem = [r for r in rows if s in (r.get('old') or '') and s not in (r.get('new') or '')]
    add = [r for r in rows if s not in (r.get('old') or '') and s in (r.get('new') or '')]
    print('=== %r removed %d added %d' % (s, len(rem), len(add)))
    for r in rem[:8]:
        print('  REM', r.get('page'), r.get('kind'), '|', repr(r.get('old'))[:140], '->', repr(r.get('new'))[:140])
    for r in add[:8]:
        print('  ADD', r.get('page'), r.get('kind'), '|', repr(r.get('old'))[:140], '->', repr(r.get('new'))[:140])
