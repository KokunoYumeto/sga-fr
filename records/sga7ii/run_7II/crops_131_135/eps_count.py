"""Count \\varepsilon and \\epsilon per folio: python -I eps_count.py <file.tex>"""
import re
import sys

t = open(sys.argv[1], encoding="utf-8").read()
fol = "pre"
counts = {}
order = []
for line in t.split("\n"):
    m = re.search(r"%{10}\s+scan idx \d+\s+\|\s+folio (\d+)", line)
    if m:
        fol = m.group(1)
        continue
    v = line.count("\\varepsilon")
    e = len(re.findall(r"\\epsilon(?![a-zA-Z])", line))
    if v or e:
        if fol not in counts:
            counts[fol] = [0, 0]
            order.append(fol)
        counts[fol][0] += v
        counts[fol][1] += e
tv = sum(c[0] for c in counts.values())
te = sum(c[1] for c in counts.values())
for k in order:
    print("folio", k, "varepsilon", counts[k][0], "epsilon", counts[k][1])
print("total varepsilon", tv, "epsilon", te)
