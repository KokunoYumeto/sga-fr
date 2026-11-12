import re, sys
path = sys.argv[1]
a, b = int(sys.argv[2]), int(sys.argv[3])
BS = chr(92)
with open(path, encoding='utf-8') as f:
    lines = f.readlines()
seg = ''.join(lines[a-1:b])
pats = {
    "K'": r"(?<![A-Za-z\\])K'",
    "K^bullet": re.escape(BS) + r"?K\^\{?" + re.escape(BS) + r"bullet",
    "K^cdot": r"K\^\{?" + re.escape(BS) + r"cdot",
    "K_bullet": r"K_\{?" + re.escape(BS) + r"bullet",
    "Kdot macro": re.escape(BS) + r"Kdot(?![A-Za-z])",
    "Kprime macro": re.escape(BS) + r"Kprime(?![A-Za-z])",
    "K^circ": r"K\^\{?" + re.escape(BS) + r"circ",
}
for k, p in pats.items():
    print(k, len(re.findall(p, seg)))
# print first few lines with K'
n = 0
for i in range(a-1, b):
    if re.search(pats["K'"], lines[i]):
        n += 1
        if n <= 8:
            print(i+1, lines[i].rstrip()[:160])
