# Checks findings_431_435.json against the page files (uniqueness of every fix's old).
import json, sys, difflib

RUN = 'C:/Users/user/Documents/sga_scan_check_20261105/run_5/'
F = json.load(open(RUN + 'findings_431_435.json', encoding='utf-8'))
show = '--show' in sys.argv
ok = True
pages = []
for f in F:
    if f['page'] not in pages:
        pages.append(f['page'])
for p in pages:
    path = RUN + 'b431_435/page_%03d.tex' % p
    try:
        raw = open(path, 'rb').read()
    except FileNotFoundError:
        print('page', p, ': no tex file; fixes must be null')
        for f in F:
            if f['page'] == p and f['fix'] is not None:
                print('  ERROR fix on a page without tex:', f['where']); ok = False
        continue
    if b'\r' in raw:
        print('page', p, ': CR found in file'); ok = False
    orig = raw.decode('utf-8')
    cur = orig
    for i, f in enumerate(F):
        if f['page'] != p:
            continue
        if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
            print('  ERROR misprint without corrected:', f['where']); ok = False
        if f['kind'] != 'misprint_in_print' and f['fix'] is None:
            print('  ERROR non-misprint without fix:', f['where']); ok = False
        if f['fix'] is None:
            continue
        old, new = f['fix']['old'], f['fix']['new']
        if '%%%%%%%%%%' in old or '%%%%%%%%%%' in new:
            print('  ERROR marker line touched:', f['where']); ok = False
        n0 = orig.count(old)
        n1 = cur.count(old)
        flag = '' if (n0 == 1 and n1 == 1) else '   <-- CHECK'
        if n1 != 1:
            ok = False
        print('p%d #%d orig=%d seq=%d %s%s' % (p, i, n0, n1, repr(old)[:70], flag))
        cur = cur.replace(old, new, 1)
    if show:
        print('---- diff page', p)
        for line in difflib.unified_diff(orig.split('\n'), cur.split('\n'), lineterm='', n=0):
            print(line)
print('ALL OK' if ok else 'PROBLEMS FOUND')
