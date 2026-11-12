import glob, re, sys

root = sys.argv[1]
files = sorted(glob.glob(root + '/b*/page_*.tex'))
seq = []
pat = re.compile(r'(\\tag\{([0-9.]+)\})|(^(?:\\underline\{[^}]*\}\s*)?(\d+\.\d+(?:\.\d+)*)\.?\s)', re.M)
for f in files:
    t = open(f, encoding='utf-8').read()
    if 'expose_IX_body' not in t.split('\n', 1)[0]:
        continue
    pg = int(re.search(r'page_(\d+)', f).group(1))
    for m in pat.finditer(t):
        if m.group(2):
            seq.append((pg, 'tag', m.group(2)))
        else:
            seq.append((pg, 'par', m.group(4)))
prev_par = None
for pg, kind, num in seq:
    if kind == 'par':
        prev_par = num
    else:
        if num == prev_par:
            print('dup', pg, num)
print(len(seq))
for s in seq:
    if s[2].startswith('12.') or s[2].startswith('11.'):
        print(s)
