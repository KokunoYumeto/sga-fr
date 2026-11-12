"""Insert the two paragraph-break findings after displays (pp. 306, 308) into findings_306_310.json, recheck all fixes."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6')
B = RUN / 'b306_310'
P = RUN / 'findings_306_310.json'
NL = '\n'
items = json.loads(P.read_text(encoding='utf-8'))
if any('Le lecteur' in (x.get('where') or '') for x in items):
    sys.exit('already inserted')

a = dict(
    page=306, where=r"after the display i), ii), before 'Le lecteur se convaincra aisément'",
    scan=r"'Le lecteur' is indented: a new paragraph after the display (both scans)",
    tex=r"'Le lecteur se convaincra ...' follows '\]' with no blank line: the paragraph runs on",
    kind='other', confidence='medium',
    fix={'old': r'\]' + NL + 'Le lecteur', 'new': r'\]' + NL + NL + 'Le lecteur'},
    note="Paragraph break of the print missing (as reported after a display on p. 285, findings_281_285.json).")
b = dict(
    page=308, where=r"after the display i), ii), before 'Le théorème résulte immédiatement du théorème 1.6'",
    scan=r"'Le théorème résulte' is indented: a new paragraph after the display (both scans; crops_306_310/c308_letheoreme.png)",
    tex=r"'Le théorème résulte ...' follows '\]' with no blank line: the paragraph runs on",
    kind='other', confidence='medium',
    fix={'old': r'\]' + NL + 'Le théorème résulte', 'new': r'\]' + NL + NL + 'Le théorème résulte'},
    note="As on p. 306.")

out = []
for x in items:
    out.append(x)
    if x['page'] == 306 and x['kind'] == 'misprint_in_print':
        out.append(a)
    if x['page'] == 308 and x['kind'] == 'marker':
        out.append(b)

ok = True
for x in out:
    fx = x.get('fix')
    if fx:
        t = (B / f"page_{x['page']}.tex").read_text(encoding='utf-8')
        n = t.count(fx['old'])
        ok = ok and n == 1 and '%%%%%%%%%%  scan idx' not in fx['old'] + fx['new']
        print(x['page'], x['kind'], n, repr(fx['old'])[:60])
from collections import Counter
c = Counter((x['page'], x['kind'] == 'misprint_in_print') for x in out)
print('ok', ok, len(out), {p: (c[(p, False)], c[(p, True)]) for p in range(306, 311)})
if ok:
    P.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')
    print('written')
