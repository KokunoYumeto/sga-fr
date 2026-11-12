import re, collections, sys
BS = chr(92)
L = open(sys.argv[1], encoding='utf-8').read().split('\n')
names = sys.argv[2].split(',')
pat = re.compile(r'(provide|new|renew)command\*?\{' + re.escape(BS) + '(' + '|'.join(names) + r')\}')
for i, l in enumerate(L, 1):
    if pat.search(l):
        print(i, l)
a, b = int(sys.argv[3]), int(sys.argv[4])
seg = '\n'.join(L[a-1:b])
c = collections.Counter(re.findall(re.escape(BS) + '[A-Za-z]+', seg))
print(c.most_common(90))
