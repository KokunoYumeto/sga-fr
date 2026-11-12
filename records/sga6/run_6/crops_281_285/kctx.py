import re, sys
sys.stdout.reconfigure(encoding='utf-8')
path = sys.argv[1]
a, b = int(sys.argv[2]), int(sys.argv[3])
with open(path, encoding='utf-8') as f:
    lines = f.readlines()
pat = re.compile(r"(?<![A-Za-z\\])K'(?!')")
folio = None
counts = {}
for i in range(a - 1, b):
    line = lines[i]
    m = re.search(r'folio (\d+)', line)
    if m and line.startswith('%%%'):
        folio = int(m.group(1))
    n = len(pat.findall(line))
    if n:
        counts[folio] = counts.get(folio, 0) + n
    # contexts where K' is followed by something other than ( _ \ ) or ^
    for mm in pat.finditer(line):
        nxt = line[mm.end():mm.end() + 3]
        if not re.match(r"[(_\\)\s^,.]", nxt):
            print('odd', i + 1, folio, line[max(0, mm.start() - 40):mm.end() + 40].rstrip())
print(counts)
