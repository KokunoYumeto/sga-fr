import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
names = sys.argv[2:]
BS = chr(92)
for n in names:
    pat = (re.escape(BS) + r'(?:provide|new|renew)command\*?\{?' + re.escape(BS) + n + r'(?![A-Za-z])\}?(?:\[\d\])?\{[^\n]*'
           + '|' + re.escape(BS) + r'DeclareMathOperator\*?\{' + re.escape(BS) + n + r'(?![A-Za-z])\}\{[^\n]*'
           + '|' + re.escape(BS) + 'def' + re.escape(BS) + n + r'(?![A-Za-z])[^\n]*')
    for m in re.finditer(pat, t):
        ln = t.count('\n', 0, m.start()) + 1
        print(n, ln, m.group(0)[:100])
