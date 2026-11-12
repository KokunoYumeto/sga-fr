import re, sys
BS = chr(92)
path = sys.argv[1]
names = sys.argv[2].split(',')
lines = open(path, encoding='utf-8').read().split('\n')
kw = ['newcommand', 'renewcommand', 'providecommand', 'DeclareMathOperator', 'def', 'let']
for i, l in enumerate(lines, 1):
    if l.lstrip().startswith('%'):
        continue
    for k in kw:
        for n in names:
            for form in (BS + k + '{' + BS + n + '}', BS + k + BS + n, BS + k + '*{' + BS + n + '}'):
                j = l.find(form)
                if j >= 0:
                    end = j + len(form)
                    if end < len(l) and l[end].isalpha():
                        continue
                    print(i, l[:240])
                    break
