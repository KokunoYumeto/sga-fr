import re, sys
path = sys.argv[1]
names = sys.argv[2:]
BS = chr(92)
with open(path, encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    for n in names:
        pat1 = r'(newcommand|renewcommand|providecommand|DeclareMathOperator)\*?\s*\{?' + re.escape(BS + n) + r'(?![A-Za-z])'
        pat2 = re.escape(BS + 'def' + BS + n) + r'(?![A-Za-z])'
        if re.search(pat1, line) or re.search(pat2, line):
            print(i, line.rstrip()[:300])
