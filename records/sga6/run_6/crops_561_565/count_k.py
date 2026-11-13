import re, sys
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
t = open(r'C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex', encoding='utf-8').read()
M = re.compile(r'%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%')
ms = list(M.finditer(t))
lo, hi = int(sys.argv[1]), int(sys.argv[2])
tot = [0, 0]
circ = 'K^' + BS + 'circ'
bul_re = re.compile(r'K\^\{?\\bullet')
kb = 'K_' + BS + 'bullet'
for i, m in enumerate(ms):
    f = int(m.group(2))
    if lo <= f <= hi:
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        s = t[m.start():end]
        a = s.count(circ); b = len(bul_re.findall(s)); c = s.count(kb)
        tot[0] += a; tot[1] += b
        if a or b:
            print(f, 'K^circ', a, 'K^bullet', b, 'K_bullet', c)
print('total K^circ, K^bullet', tot)
