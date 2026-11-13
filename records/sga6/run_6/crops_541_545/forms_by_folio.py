import re, sys
path = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex'
lines = open(path, encoding='utf-8').read().split('\n')
start, end = int(sys.argv[1]), int(sys.argv[2])
pats = sys.argv[3:]
folio = None
counts = {}
for ln in lines[start - 1:end]:
    m = re.search(r'folio (\d+)', ln)
    if ln.startswith('%%%%') and m:
        folio = int(m.group(1))
        continue
    for p in pats:
        c = ln.count(p)
        if c:
            counts.setdefault(folio, {}).setdefault(p, 0)
            counts[folio][p] += c
for f in sorted(k for k in counts if k is not None):
    print(f, counts[f])
if None in counts:
    print('before first marker', counts[None])
