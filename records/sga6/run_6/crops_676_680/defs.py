import re, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open(sys.argv[1], encoding='utf-8').read()
BS = chr(92)
for name in sys.argv[2:]:
    pat = (re.escape(BS) + r'(?:re)?(?:newcommand|providecommand|DeclareMathOperator|def)\*?\s*\{?'
           + re.escape(BS + name) + r'(?![A-Za-z])\}?[^\n]*')
    for m in re.finditer(pat, t):
        ln = t.count('\n', 0, m.start()) + 1
        print(name, ln, m.group(0)[:140])
