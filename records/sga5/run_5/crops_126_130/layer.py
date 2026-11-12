import sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:/Users/user/Documents/sga_scan_check_20261105/'
bdir = base + 'run_5/b126_130/'
layers = {L: open(base + 'sga5/' + L + '/s5.tex', encoding='utf-8').read() for L in ['diplomatic', 'current']}
for p in range(126, 131):
    t = open(bdir + 'page_%03d.tex' % p, encoding='utf-8').read()
    body = t.split('\n', 1)[1]  # drop the "% from s5.tex" line
    for L, s in layers.items():
        print(p, L, 'contained' if body.rstrip('\n') in s else 'NOT contained')
