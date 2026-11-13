import sys
path = r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex'
lines = open(path, encoding='utf-8').read().split('\n')
start, end = int(sys.argv[1]), int(sys.argv[2])
t = '\n'.join(lines[start - 1:end])
pats = sys.argv[3:]
for p in pats:
    print(repr(p), t.count(p))
