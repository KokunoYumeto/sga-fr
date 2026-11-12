import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
for pat in sys.argv[2:]:
    ms = list(re.finditer(pat, t))
    print(len(ms), 'x', pat)
    for m in ms[:6]:
        ln = t.count('\n', 0, m.start()) + 1
        print('   line', ln, repr(t[max(0, m.start()-30):m.end()+30]))
