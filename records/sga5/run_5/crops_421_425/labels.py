import sys

src = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex"
lines = open(src, encoding="utf-8").read().split("\n")
lo, hi = int(sys.argv[1]), int(sys.argv[2])
out = []
for i, l in enumerate(lines, 1):
    if lo <= i <= hi:
        s = l.lstrip()
        if s.startswith("\\begin{statement}") or s.startswith("\\textbf{") or "prooftext" in s or s.startswith("\\section"):
            nxt = lines[i] if i < len(lines) else ""
            out.append("%d %s || %s" % (i, l[:120], nxt[:100]))
sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
