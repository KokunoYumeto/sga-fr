import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# usage: count_cmds.py <tex file> <first line> <last line> [show]
fn, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
show = len(sys.argv) > 4
L = open(fn, encoding='utf-8').read().split('\n')
seg = '\n'.join(L[a - 1:b])
for cmd in ['underline', 'emph', 'textit', 'textbf', 'mathbb', 'mathbf', 'wt', 'widetilde', 'pmod', 'longmapsto']:
    print(cmd, len(re.findall(r'\\' + cmd + r'\{', seg)))
if show:
    for m in re.finditer(r'\\(underline|emph)\{[^}]{0,50}', seg):
        print('  ', m.group(0))
