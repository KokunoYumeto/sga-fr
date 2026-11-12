import re, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
t = open('C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read()
a5 = t.index('|  folio 297  %'); a = t.index('|  folio 365  %')
s5 = t[a5:a]
pat = re.escape(BS + 'underline{') + r'[^{}]{0,25}\}'
c = Counter(re.findall(pat, s5))
print(c.most_common(40))
pat1 = r'.{30}' + re.escape(BS + 'underline{1}') + r'.{20}'
print(re.findall(pat1, s5)[:8])
