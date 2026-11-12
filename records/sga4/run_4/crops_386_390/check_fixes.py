import json, sys
run = sys.argv[1]
data = json.load(open(run + '/findings_386_390.json', encoding='utf-8'))
print('entries', len(data))
for i, f in enumerate(data):
    src = open(run + '/b386_390/page_%d.tex' % f['page'], encoding='utf-8').read()
    body = src.split('\n', 1)[1]
    tex_in = f['tex'] in body
    if f['fix'] is None:
        print(i, f['page'], f['kind'], 'fix=None', 'corrected' in f, 'tex-substring:', tex_in)
    else:
        n = src.count(f['fix']['old'])
        nb = body.count(f['fix']['old'])
        print(i, f['page'], f['kind'], 'old count', n, 'in body', nb, 'tex-substring:', tex_in, 'corrected-key:', 'corrected' in f)
