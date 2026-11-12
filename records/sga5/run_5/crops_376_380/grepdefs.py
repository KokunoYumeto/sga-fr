import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
t = open(sys.argv[1], encoding="utf-8").read()
BS = chr(92)
for name in sys.argv[2:]:
    pats = [BS + "newcommand{" + BS + name + "}", BS + "renewcommand{" + BS + name + "}", BS + "providecommand{" + BS + name + "}",
            BS + "let" + BS + name, BS + "def" + BS + name, BS + "newcommand" + BS + name, BS + "renewcommand" + BS + name]
    for p in pats:
        start = 0
        while True:
            k = t.find(p, start)
            if k < 0:
                break
            nxt = t[k + len(p):k + len(p) + 1]
            if p.endswith(name) and nxt.isalpha():
                start = k + 1
                continue
            ln = t.count("\n", 0, k) + 1
            line = t[t.rfind("\n", 0, k) + 1:t.find("\n", k)]
            print(name, ln, line[:160])
            start = k + 1
