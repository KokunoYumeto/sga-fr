import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
pat = re.compile(r'(\\mathbb\{[A-Z]\}|\\underline\{[A-Z]\}|\\mathcal\{[A-Z]\}|(?<![A-Za-z\\])[A-Z])\^\{?\\?(\*|ast)\}?')
for fn in sorted(glob.glob(root + '/b*/page_*.tex')):
    pg = int(fn[-7:-4])
    if not (150 <= pg <= 300):
        continue
    t = open(fn, encoding='utf-8').read()
    for m in pat.finditer(t):
        s = t[max(0, m.start() - 80):m.end() + 80].replace('\n', ' ')
        print(fn[-12:], '|', s)
