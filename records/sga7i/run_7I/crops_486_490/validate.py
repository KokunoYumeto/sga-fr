import json, sys, collections
base = sys.argv[1]
data = json.load(open(base + '/findings_486_490_recheck.json', encoding='utf-8'))
counts = collections.defaultdict(lambda: [0, 0])
for f in data:
    p = f['page']
    tex = open(f'{base}/b486_490/page_{p}.tex', encoding='utf-8', newline='').read()
    if f['kind'] == 'misprint_in_print':
        counts[p][1] += 1
    else:
        counts[p][0] += 1
    n_tex = tex.count(f['tex'])
    fix = f['fix']
    n_old = tex.count(fix['old']) if fix else None
    print(p, f['kind'], 'tex-count', n_tex, 'old-count', n_old, 'corrected' in f)
print({p: f'{a}/{b}' for p, (a, b) in sorted(counts.items())})
