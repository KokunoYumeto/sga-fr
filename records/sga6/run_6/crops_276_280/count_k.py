import re, sys
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
t = open(sys.argv[1], encoding='utf-8').read()
a = t.find('% Exposé IV macros')
b = t.find(BS + 'section*{Exposé V', a + 10)
if b < 0:
    b = t.find('Exposé V', a + 2000)
seg = t[a:b]
print('Exposé IV span chars', a, b, 'lines', t[:a].count('\n') + 1, t[:b].count('\n') + 1)
kp = [m.start() for m in re.finditer(r"K'", seg)]
kprime = seg.count(BS + 'Kprime')
kbul = len(re.findall(r'K\^\{?' + re.escape(BS) + 'bullet', seg))
kdot = len(re.findall(r'K_\{?' + re.escape(BS) + 'bullet', seg))
print("K' occurrences:", len(kp), " \\Kprime uses:", kprime - 1, " K^bullet:", kbul, " K_bullet:", kdot)
folios = [(m.start(), m.group(1)) for m in re.finditer(r'folio (\d+)', seg)]
def folio_at(p):
    f = None
    for s, n in folios:
        if s <= p:
            f = n
    return f
from collections import Counter
c = Counter(folio_at(p) for p in kp)
print(sorted(c.items(), key=lambda x: int(x[0]) if x[0] else 0))
