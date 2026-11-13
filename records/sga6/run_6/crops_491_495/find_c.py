"""List bare c(...) (no tilde, no exponent) in Exposé VIII of the diplomatic main.tex, with folio."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(L) if l.startswith('%%%%') and 'folio 466 ' in l)
end = next(i for i, l in enumerate(L) if 'section*{Exposé IX' in l)
folio = None
pat = re.compile(r'(?<![A-Za-z\\])c(\(|_\{?t)')
for l in L[start:end]:
    m = re.search(r'folio (\d+)', l)
    if m and l.startswith('%%%%'):
        folio = int(m.group(1)); continue
    for mm in pat.finditer(l):
        s = max(0, mm.start() - 50)
        print(folio, '|', l[s:mm.end() + 40])
