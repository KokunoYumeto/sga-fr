import re, sys
BS = chr(92)
t = open(sys.argv[1], encoding='utf-8').read()
L = t.split('\n')
for cmd in ('underline', 'emph'):
    pat = re.compile(re.escape(BS + cmd) + r'\{([^{}$]*)\}')
    found = []
    for i, l in enumerate(L, 1):
        for m in pat.finditer(l):
            found.append((i, m.group(1)))
    print(cmd, len(found))
    # show a sample of text-like ones (with letters, length > 3)
    sample = [f for f in found if len(f[1]) > 3][:30]
    for s in sample:
        print('   ', s)
