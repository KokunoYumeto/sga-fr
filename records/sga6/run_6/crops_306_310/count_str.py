import sys
sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import files  # noqa: E402
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
S = [
    '_{j=1,' + BS + 'ldots,k}' + BS + ') de ' + BS + '(' + BS + 'bigl(' + BS + 'Ghat',
    '_{j=1,' + BS + 'ldots,k}',
]
for edition in ('diplomatic', 'current'):
    t = files('6', edition)[0].read_text(encoding='utf-8')
    for s in S:
        print(edition, t.count(s), repr(s))
