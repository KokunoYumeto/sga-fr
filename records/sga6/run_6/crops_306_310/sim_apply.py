"""Apply the fixes of findings_306_310.json in memory, in JSON order, to the live page spans of both layers (as
process_sga.py would, without writing), and print the changed lines."""
import json
import sys

sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import pages  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
items = json.load(open(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_306_310.json', encoding='utf-8'))
for edition in ('diplomatic', 'current'):
    P = pages('6', edition)
    f = P[306][0][0]
    t = f.read_text(encoding='utf-8')
    for x in items:
        fx = x.get('fix')
        if not fx:
            continue
        if edition == 'current' and x['kind'] == 'misprint_in_print':
            continue
        # recompute the page span on the modified text
        import re
        from sga_config import MARK
        ms = list(MARK.finditer(t))
        span = None
        for i, m in enumerate(ms):
            if int(m.group(2)) == x['page']:
                span = (m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t))
        s, e = span
        hits = []
        k = t.find(fx['old'], s, e)
        while k >= 0 and k + len(fx['old']) <= e:
            hits.append(k)
            k = t.find(fx['old'], k + 1, e)
        if len(hits) != 1:
            print(edition, x['page'], 'FAIL', len(hits), repr(fx['old'])[:60])
            continue
        k = hits[0]
        t = t[:k] + fx['new'] + t[k + len(fx['old']):]
        a = t.rfind('\n', 0, k) + 1
        b = t.find('\n', k + len(fx['new']))
        print(edition, x['page'], 'ok', repr(t[max(a, k - 60):min(b if b > 0 else len(t), k + len(fx['new']) + 40)]))
