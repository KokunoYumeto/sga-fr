"""Compare the page files of this batch with the live diplomatic main.tex spans (read only)."""
import pathlib
import sys

sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import pages  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
B = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\run_6\b306_310')
P = pages('6', 'diplomatic')
for folio in range(305, 312):
    spans = P.get(folio, [])
    live = ''.join(f.read_text(encoding='utf-8')[s:e] for f, s, e in spans)
    pf = B / f'page_{folio}.tex'
    if not pf.exists():
        print(folio, 'live span length', len(live), repr(live[-200:]))
        continue
    snap = pf.read_text(encoding='utf-8')
    snap_body = snap.split('\n', 1)[1]  # drop the '% from main.tex' line
    print(folio, 'same' if snap_body.rstrip() == live.rstrip() else 'DIFFERENT', len(snap_body), len(live))
    if snap_body.rstrip() != live.rstrip():
        import difflib
        for l in difflib.unified_diff(snap_body.splitlines(), live.splitlines(), lineterm='', n=0):
            print('   ', l[:300])
