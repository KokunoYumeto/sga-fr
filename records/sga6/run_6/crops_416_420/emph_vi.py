import io, re, collections
L = io.open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
c = collections.Counter()
for i in range(8000, 10490):
    for m in re.finditer(r'\\(underline|emph)\{([^}]*)\}', L[i]):
        c[(m.group(1), m.group(2)[:40])] += 1
out = io.open(r'C:/Users/user/Documents/sga_scan_check_20261105/run_6/crops_416_420/emph_vi.txt', 'w', encoding='utf-8')
tot = collections.Counter()
for (k, s), v in c.items():
    tot[k] += v
out.write('totals %s\n' % dict(tot))
for k, v in c.most_common(40):
    out.write('%d %s\n' % (v, k))
out.close()
