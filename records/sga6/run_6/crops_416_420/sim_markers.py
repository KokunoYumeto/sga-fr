import io
M417 = '%%%%%%%%%%  scan idx 430  |  folio 417  %%%%%%%%%%'
M418 = '%%%%%%%%%%  scan idx 431  |  folio 418  %%%%%%%%%%'
edits = [
    ('sur $B$. Les\n' + M417 + '\nrelations à prouver', 'sur $B$.\n' + M417 + '\nLes relations à prouver'),
    ('qui applique $T_i$ sur $f_i$;\n' + M418 + '\nnotons', 'qui applique\n' + M418 + '\n$T_i$ sur $f_i$; notons'),
]
for lay in ('diplomatic', 'current'):
    t = io.open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/%s/main.tex' % lay, encoding='utf-8', newline='').read()
    for old, new in edits:
        n = t.count(old)
        print(lay, 'occurrences', n)
        t = t.replace(old, new)
    # show the result around both markers (in memory only)
    for m in (M417, M418):
        i = t.index(m)
        print(repr(t[i - 40:i + len(m) + 50]).encode('ascii', 'replace').decode())
