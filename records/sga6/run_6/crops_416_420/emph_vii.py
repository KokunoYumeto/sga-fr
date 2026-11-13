import io, re
L = io.open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
start, end = 10490, 11931
folio = None
out = io.open(r'C:/Users/user/Documents/sga_scan_check_20261105/run_6/crops_416_420/emph_vii.txt', 'w', encoding='utf-8')
kcirc = {}
for i in range(start, end):
    l = L[i]
    m = re.search(r'folio (\d+)', l)
    if l.startswith('%%%%%%%%%%') and m:
        folio = int(m.group(1))
    for mm in re.finditer(r'\\emph\{[^}]*\}', l):
        out.write('line %d folio %s: %s\n' % (i + 1, folio, mm.group(0)))
    n = len(re.findall(r'K\^\\circ', l))
    if n:
        kcirc[folio] = kcirc.get(folio, 0) + n
out.write('K^circ by folio: %s\n' % sorted(kcirc.items()))
out.close()
