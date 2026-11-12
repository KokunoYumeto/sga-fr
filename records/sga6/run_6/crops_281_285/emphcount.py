import re, sys
sys.stdout.reconfigure(encoding='utf-8')
path = sys.argv[1]
a, b = int(sys.argv[2]), int(sys.argv[3])
BS = chr(92)
with open(path, encoding='utf-8') as f:
    lines = f.read().split('\n')
t = '\n'.join(lines[a - 1:b])
for cmd in ['emph', 'underline', 'uline', 'textit', 'textbf']:
    print(cmd, len(re.findall(re.escape(BS + cmd) + r'\{', t)))
for m in list(re.finditer(re.escape(BS) + r'(emph|underline|uline)\{[^}]{0,60}', t))[:60]:
    print(m.group(0))
