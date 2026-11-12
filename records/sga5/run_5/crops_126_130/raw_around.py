"""Print the raw text (repr) around the markers of the given folios in both layers of s5.tex (read-only)."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = r'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
folios = [int(x) for x in sys.argv[1:]]
for edition in ('diplomatic', 'current'):
    t = open(base + edition + '/s5.tex', encoding='utf-8', newline='').read()
    print('==', edition, 'CRLF count', t.count('\r\n'), 'bare LF count', t.count('\n') - t.count('\r\n'))
    for m in MARK.finditer(t):
        if int(m.group(2)) in folios:
            print('-- folio', m.group(2))
            print(repr(t[m.start() - 120:m.end() + 90]))
