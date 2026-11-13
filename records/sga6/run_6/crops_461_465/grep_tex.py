"""grep_tex.py LAYER PATTERN [FROM_LINE TO_LINE] -- literal substring search in sga6/<LAYER>/main.tex.
Prints line number and context. Use 'lit:' prefix for a literal string, otherwise a regex."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
layer, pat = sys.argv[1], sys.argv[2]
lo = int(sys.argv[3]) if len(sys.argv) > 3 else 1
hi = int(sys.argv[4]) if len(sys.argv) > 4 else 10**9
lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
if pat.startswith("lit:"):
    s = pat[4:]
    rx = re.compile(re.escape(s))
else:
    rx = re.compile(pat)
n = 0
for i, l in enumerate(lines, 1):
    if i < lo or i > hi:
        continue
    for m in rx.finditer(l):
        n += 1
        print(i, "|", l[max(0, m.start() - 70):m.end() + 40])
print("count", n)
