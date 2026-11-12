"""Print the lines of a TeX file that contain a literal string: python -I grep_tex.py FILE STRING [MAX] [WIDTH]"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
f, s = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 40
w = int(sys.argv[4]) if len(sys.argv) > 4 else 160
n = 0
for i, line in enumerate(open(f, encoding="utf-8").read().split("\n"), 1):
    if s in line:
        n += 1
        if n <= mx:
            k = line.find(s)
            print(i, line[max(0, k - 20):k + w])
print("total lines:", n)
