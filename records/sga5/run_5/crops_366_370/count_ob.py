import re, sys
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex", encoding="utf-8").read()
lines = t.split("\n")
pat = re.compile(r"\\Ob(?![A-Za-z])")
hits = [i for i, l in enumerate(lines, 1) if pat.search(l) and "providecommand" not in l]
print("lines using Ob macro:", len(hits), "occurrences:", sum(len(pat.findall(lines[i - 1])) for i in hits))
print("in Expose VIII (11990-12684):", [h for h in hits if 11990 <= h <= 12684])
for i in [101, 163, 226, 269, 300]:
    print(i, lines[i - 1])
