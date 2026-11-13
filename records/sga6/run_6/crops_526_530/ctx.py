import re, sys

# usage: python -I ctx.py FILE PATTERN [WIDTH]
path = sys.argv[1]
pat = sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 300
text = open(path, encoding='utf-8').read()
n = 0
for m in re.finditer(pat, text):
    s = max(0, m.start() - width)
    e = min(len(text), m.end() + width)
    print(repr(text[s:e]))
    print('====')
    n += 1
    if n > 40:
        break
print('matches:', len(re.findall(pat, text)))
