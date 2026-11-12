"""usage: python -I grep_s5.py WORD LO HI  -> lines of s5.tex (diplomatic and current) in LO..HI containing WORD,
with the printed page (folio) each line belongs to."""
import re
import sys

word, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
out = []
for layer in ("diplomatic", "current"):
    src = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\%s\s5.tex" % layer
    lines = open(src, encoding="utf-8").read().split("\n")
    cur = None
    for i, l in enumerate(lines, 1):
        m = re.match(r"%%%%%%%%%%  scan idx \d+  \|  folio (\d+)", l)
        if m:
            cur = int(m.group(1))
        if lo <= i <= hi and word in l:
            j = l.find(word)
            out.append("%s %d p%s ... %s" % (layer, i, cur, l[max(0, j - 60): j + 80]))
sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
