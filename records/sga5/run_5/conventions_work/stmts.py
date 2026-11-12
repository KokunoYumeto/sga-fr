"""List the statements of Exposé XV with their \\emph counts.  usage: stmts.py layer"""
import re, sys
BS = chr(92)
base = 'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
s = open(base + sys.argv[1] + '/s5.tex', encoding='utf-8').read()
a = s.find(BS + 'section*{EXPOSÉ XV}')
b = s.find(BS + 'section*{Index terminologique}')
rx = re.compile(re.escape(BS + 'begin{statement}{') + r'([^}]*)\}(.*?)' + re.escape(BS + 'end{statement}'), re.S)
for m in rx.finditer(s, a, b):
    body = m.group(2)
    line = s[:m.start()].count('\n') + 1
    print(f'L{line} {m.group(1)}: emph={body.count(BS + "emph")} len={len(body)} | {body[:160]!r}')
