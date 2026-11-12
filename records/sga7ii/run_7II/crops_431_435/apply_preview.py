import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
BATCH = r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b431_435'
F = json.load(open(r'C:\Users\user\Documents\sga_scan_check_20261105\run_7II\findings_431_435.json', encoding='utf-8'))
mode = sys.argv[1] if len(sys.argv) > 1 else 'diplomatic'  # or 'corrected' (skips misprint fixes)
pages = sorted({f['page'] for f in F})
for p in pages:
    t = open(os.path.join(BATCH, 'page_%d.tex' % p), encoding='utf-8', newline='').read()
    for f in F:
        if f['page'] != p or f['fix'] is None:
            continue
        if mode == 'corrected' and f['kind'] == 'misprint_in_print':
            continue
        if t.count(f['fix']['old']) != 1:
            print('!! not unique/absent on', p, repr(f['fix']['old']))
            continue
        t = t.replace(f['fix']['old'], f['fix']['new'], 1)
    depth = 0
    bad = False
    i = 0
    while i < len(t):
        c = t[i]
        if c == '\\':
            i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth < 0:
                bad = True
        i += 1
    print('=' * 20, p, 'brace depth', depth, 'bad' if bad else '')
    print(t)
