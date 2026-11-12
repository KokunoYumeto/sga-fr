import sys, re
sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import pages
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
PATS = {
    'Cg': re.escape(BS + 'mathcal C_g'),
    'Abfil': re.escape(BS + 'Abfil'),
    'G': re.escape(BS + 'cG') + '|' + re.escape(BS + 'mathcal G') + '|' + re.escape(BS + 'mathcal{G}'),
    'Grdot': re.escape(BS + 'operatorname{Gr}(' + BS + ',' + BS + 'cdot' + BS + ',)'),
    'hatdot': re.escape(BS + 'widehat{' + BS + ',' + BS + 'cdot' + BS + ',}'),
    'cdots': re.escape(BS + 'cdots'),
}
lo, hi = int(sys.argv[2]), int(sys.argv[3])
pat = re.compile(PATS[sys.argv[1]])
for ed in ('diplomatic', 'current'):
    P = pages('6', ed)
    tot = 0
    out = []
    for folio in sorted(P):
        if not lo <= folio <= hi:
            continue
        for f, s, e in P[folio]:
            t = f.read_text(encoding='utf-8')[s:e]
            n = len(pat.findall(t))
            if n:
                out.append((folio, n)); tot += n
    print(sys.argv[1], ed, tot, out)
