import re, sys, collections
p = r"C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex"
t = open(p, encoding="utf-8").read()
lines = t.split("\n")
BS = chr(92)
c = collections.Counter(re.findall(re.escape(BS) + r"underline\{" + re.escape(BS) + r"[A-Za-z]+\}", t))
print(c.most_common(20))
a = int(sys.argv[1]) if len(sys.argv) > 1 else 15240
b = int(sys.argv[2]) if len(sys.argv) > 2 else 15700
seg = "\n".join(lines[a:b])
print(collections.Counter(re.findall(re.escape(BS) + r"underline\{[^}]*\}", seg)).most_common(40))
print(collections.Counter(re.findall(re.escape(BS) + r"emph\{[^}]*\}", seg)).most_common(40))
print(collections.Counter(re.findall(re.escape(BS) + r"uline\{[^}]*\}", seg)).most_common(40))
