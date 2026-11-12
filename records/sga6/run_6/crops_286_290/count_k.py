import re
import sys

t = open(sys.argv[1], encoding='utf-8').read()
s = t.index('\\section*{Exposé IV.')
e = t.index('\\section*{Exposé V.')
iv = t[s:e]
print("Expose IV: K' =", iv.count("K'"),
      "| K^bullet forms =", len(re.findall(r"K\^\{?\\bullet", iv)),
      "| K_bullet forms =", len(re.findall(r"K_\{?\\bullet", iv)),
      "| \\mathbf L =", iv.count("\\mathbf L"), "| \\mathrm L =", iv.count("\\mathrm L"),
      "| \\parf =", len(re.findall(r"\\parf\b", iv)), "| \\uparf =", iv.count("\\uparf"))
print("whole file: K^bullet forms =", len(re.findall(r"K\^\{?\\bullet", t)), "| K'( =", t.count("K'("))
for m in list(re.finditer(r"K\^\{?\\bullet", t))[:6]:
    print('  K^bullet at', m.start(), repr(t[m.start() - 40:m.start() + 30]))
