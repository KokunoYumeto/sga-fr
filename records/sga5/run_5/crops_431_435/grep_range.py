import sys
path = sys.argv[1]
start, end = int(sys.argv[2]), int(sys.argv[3])
pats = sys.argv[4:]
L = open(path, encoding='utf-8').read().split('\n')
for i in range(start - 1, min(end, len(L))):
    l = L[i]
    if any(p in l for p in pats):
        print(i + 1, l[:200])
