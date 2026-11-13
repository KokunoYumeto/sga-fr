"""Count literal notation forms in the Expose X part of the diplomatic main.tex (lines 13409-15269).
Arguments: literal strings in which '@' stands for a backslash (so no escaping is needed)."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
B = chr(92)
t = open(r'C:/Users/user/Documents/sga_scan_check_20261105/sga6/diplomatic/main.tex', encoding='utf-8').read().split('\n')
x = '\n'.join(t[13408:15269])
default = ['@cl^@circ', '@cl^{@circ}', '@clo', '@cl^@bullet', '@cl^{@bullet}', 'K^@circ', 'K^{@circ}', 'K^@bullet',
           'K^{@bullet}', '@cl_P', '@cl_@bullet', '@emph{', '@underline{', '@mathcal O', '@cO', '@mathbb Z', '@mathbb Q',
           '@Pic_{X/k}', '@rightsquigarrow', '@mapsto', '@longmapsto', '@mathbf']
for p in (sys.argv[1:] or default):
    lit = p.replace('@', B)
    print(f'{lit:30s} {x.count(lit)}')
