"""Count and list underline/emph markup in Expose III B of s5.tex (read-only helper)."""
import re
import sys

SRC = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/diplomatic/s5.tex"
lines = open(SRC, encoding="utf-8").read().split("\n")
seg = "\n".join(lines[4327:6876])
pat = sys.argv[1] if len(sys.argv) > 1 else r"\\(underline|emph)\{[^}]{0,60}\}"
hits = list(re.finditer(pat, seg))
print(len(hits))
for m in hits[:80]:
    print(repr(m.group(0)))
