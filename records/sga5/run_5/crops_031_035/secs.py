import re, sys
BS = chr(92)
t = open(sys.argv[1], encoding='utf-8').read().split('\n')
pat = re.compile(re.escape(BS) + r'(part|chapter|section|subsection|subsubsection)(\*?)' + re.escape('{'))
for i, l in enumerate(t, 1):
    if i > int(sys.argv[2]):
        break
    for m in pat.finditer(l):
        if m.group(2) == '':
            print(i, l[:120])
