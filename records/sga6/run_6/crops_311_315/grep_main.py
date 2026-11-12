"""grep_main.py PATTERN [LINE_FROM LINE_TO] [CTX]: regex occurrences in the diplomatic main.tex with their folio."""
import bisect
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
P = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex"
t = open(P, encoding="utf-8").read()
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]
pos = [p for p, _ in marks]


def folio(i):
    k = bisect.bisect_right(pos, i) - 1
    return marks[k][1] if k >= 0 else None


pat = re.compile(re.escape(sys.argv[1]) if "--lit" in sys.argv else sys.argv[1])
sys.argv = [a for a in sys.argv if a != "--lit"]
lines = t.split("\n")
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
hi = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
ctx = int(sys.argv[4]) if len(sys.argv) > 4 else 40
start = sum(len(l) + 1 for l in lines[:lo - 1])
end = sum(len(l) + 1 for l in lines[:hi])
n = 0
for m in pat.finditer(t, start, end):
    i = m.start()
    n += 1
    print(folio(i), repr(t[max(0, i - ctx):i + ctx]))
print("total", n)
