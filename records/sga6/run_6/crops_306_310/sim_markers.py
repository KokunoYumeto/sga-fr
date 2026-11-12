"""Simulate the proposed marker moves of pp. 306-311 in memory on both layers of SGA 6 main.tex (no file is written)."""
import re
import sys

sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)


def mk(folio, idx):
    return '%%%%%%%%%%  scan idx ' + str(idx) + '  |  folio ' + str(folio) + '  %%%%%%%%%%'


# (folio, old, new) exact replacements, written with BS for the backslash
REPL = [
    (306,
     BS + '((1+X^{(j)}t)_{j=1,' + BS + 'ldots,k}' + BS + ') de ' + BS + '(' + BS + 'bigl(' + BS + 'Ghat(K[(X^{(j)})_j])'
     + BS + 'bigr)^k' + BS + ')~; un\n' + mk(306, 319) + '\n',
     mk(306, 319) + '\n' + BS + '((1+X^{(j)}t)_{j=1,' + BS + 'ldots,k}' + BS + ') de ' + BS + '(' + BS + 'bigl(' + BS
     + 'Ghat(K[(X^{(j)})_j])' + BS + 'bigr)^k' + BS + ')~; un\n'),
    (308,
     'associe sa\n' + mk(308, 321) + '\nvaleur sur',
     'associe\n' + mk(308, 321) + '\nsa valeur sur'),
    (309,
     ', la série ' + BS + '(1+' + BS + 'cdots+' + BS + 'bar a_n+' + BS + 'cdots' + BS + '), où ' + BS + '(' + BS
     + 'bar a_n' + BS + ') est la classe de ' + BS + '(a_n' + BS + ') dans ' + BS + '(' + BS + 'operatorname{Gr}^nA'
     + BS + '). Son\n' + mk(309, 322) + '\nnoyau est',
     ',\n' + mk(309, 322) + '\nla série ' + BS + '(1+' + BS + 'cdots+' + BS + 'bar a_n+' + BS + 'cdots' + BS + '), où '
     + BS + '(' + BS + 'bar a_n' + BS + ') est la classe de ' + BS + '(a_n' + BS + ') dans ' + BS + '(' + BS
     + 'operatorname{Gr}^nA' + BS + '). Son\nnoyau est'),
    (310,
     'homomorphisme de ' + BS + '(K' + BS + ')-\n' + mk(310, 323) + '\nalgèbres filtrées',
     'homomorphisme de\n' + mk(310, 323) + '\n' + BS + '(K' + BS + ')-algèbres filtrées'),
    (311,
     "l'élément " + BS + '(1+X' + BS + ') de ' + BS + '(1+' + BS + 'widehat{K[X]}^+' + BS + ') est\n' + mk(311, 324)
     + '\n',
     "l'élément\n" + mk(311, 324) + '\n' + BS + '(1+X' + BS + ') de ' + BS + '(1+' + BS + 'widehat{K[X]}^+' + BS
     + ') est\n'),
]

for edition in ('diplomatic', 'current'):
    f = files('6', edition)[0]
    t = f.read_text(encoding='utf-8')
    n_before = len(MARK.findall(t))
    for folio, old, new in REPL:
        c = t.count(old)
        print(edition, folio, 'occurrences of old:', c)
        if c == 1:
            t = t.replace(old, new)
    n_after = len(MARK.findall(t))
    print(edition, 'markers', n_before, n_after)
    for folio in (306, 308, 309, 310, 311):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        a = t.rfind('\n', 0, m.start() - 1)
        b = t.find('\n', m.end() + 1)
        print('  ---', folio)
        print('  before:', repr(t[max(a - 160, 0):m.start()][-170:]))
        print('  after :', repr(t[m.end():m.end() + 120]))
