"""Show the live text around the markers of folios 306-311 in both layers (read only)."""
import sys

sys.path.insert(0, r'C:\Users\user\Documents\sga_scan_check_20261105')
from sga_config import MARK, files  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
for edition in ('diplomatic', 'current'):
    t = files('6', edition)[0].read_text(encoding='utf-8')
    for m in MARK.finditer(t):
        if 306 <= int(m.group(2)) <= 311:
            print(edition, m.group(2), repr(t[m.start() - 70:m.start()]), '||', repr(t[m.end():m.end() + 60]))
