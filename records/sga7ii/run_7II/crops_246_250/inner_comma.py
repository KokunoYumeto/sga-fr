"""Count \\underline{...} spans with a comma inside (not at the end) in the SGA 7 II diplomatic files."""
import pathlib
import re
import sys

d = pathlib.Path(sys.argv[1])
pat = re.compile(r"\\underline\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")
tot = 0
for f in sorted(d.glob("expose_*_body.tex")):
    t = f.read_text(encoding="utf-8")
    hits = [m.group(1) for m in pat.finditer(t) if re.search(r",\s*\S", m.group(1))]
    tot += len(hits)
    print(f.name, len(hits), [h[:45] for h in hits[:3]])
print("total", tot)
