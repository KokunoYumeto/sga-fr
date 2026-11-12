import sys, re
sys.stdout.reconfigure(encoding='utf-8')
path, pat = sys.argv[1], sys.argv[2]
lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0
hi = int(sys.argv[4]) if len(sys.argv) > 4 else 10**9
width = int(sys.argv[5]) if len(sys.argv) > 5 else 300
t = open(path, encoding='utf-8').read().split('\n')
rx = re.compile(pat)
for i, l in enumerate(t):
    if lo <= i + 1 <= hi and rx.search(l):
        m = rx.search(l)
        s = max(0, m.start() - width // 2)
        print(i + 1, l[s:s + width])
