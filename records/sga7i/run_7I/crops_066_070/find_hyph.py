import re
import sys

path = sys.argv[1]
t = open(path, encoding="utf-8").read()
pat = re.compile(r"[A-Za-z]-\}\s*\\underline\{[a-z]")
ms = list(pat.finditer(t))
print(len(ms))
for m in ms[:80]:
    ln = t.count("\n", 0, m.start()) + 1
    print(ln, repr(t[max(0, m.start() - 25):m.end() + 12]))
# also a hyphen followed by space and a lowercase continuation outside underline
pat2 = re.compile(r"[a-z]{2}- [a-z]{2}")
ms2 = list(pat2.finditer(t))
print("plain:", len(ms2))
for m in ms2[:40]:
    ln = t.count("\n", 0, m.start()) + 1
    print(ln, repr(t[max(0, m.start() - 25):m.end() + 12]))
