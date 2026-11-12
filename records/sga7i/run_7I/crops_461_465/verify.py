import json, sys
F = json.load(open('findings_461_465_recheck.json', encoding='utf-8'))
ok = True
for i, f in enumerate(F):
    src = open(f'b461_465/page_{f["page"]}.tex', encoding='utf-8').read()
    for key in ('tex',):
        n = src.count(f[key])
        print(i, f['page'], key, 'count', n, repr(f[key][:50]))
    if f['fix'] is not None:
        old = f['fix']['old']
        n = src.count(old)
        print(i, f['page'], 'OLD count', n, repr(old))
        if n != 1: ok = False
        # marker line untouched
        for line in src.split('\n'):
            if line.startswith('%%%%%%%%%%') and old in line: ok = False; print('touches marker')
        new_src = src.replace(old, f['fix']['new'])
        print('   after:', repr(new_src[new_src.find(f['fix']['new'])-20:new_src.find(f['fix']['new'])+len(f['fix']['new'])+20]))
    else:
        if src.count(f['tex']) != 1: ok = False; print('tex not unique')
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f: ok = False
print('ALL OK' if ok else 'PROBLEM')
