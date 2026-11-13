"""grep_tex.py LAYER START END REGEX [MAXCHARS]  -> lines of main.tex (1-based, START..END) matching REGEX.
In REGEX, the character @ stands for a literal backslash (to avoid shell escaping)."""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
layer, a, b, rx = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 300
p = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex"
lines = open(p, encoding="utf-8").read().split("\n")
r = re.compile(rx.replace("@", r"\\"))
for i in range(a - 1, min(b, len(lines))):
    L = lines[i]
    for m in r.finditer(L):
        s = max(0, m.start() - mx // 2)
        print(f"{i+1}: ...{L[s:m.end() + mx // 2]}...")
