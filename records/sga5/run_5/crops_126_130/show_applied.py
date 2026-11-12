"""Apply the findings of findings_126_130.json (or the in-memory list from make_findings) to copies of the page files and print the result."""
import sys, runpy, io, contextlib
sys.stdout.reconfigure(encoding='utf-8')
here = r'C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_126_130/'
buf = open(here + "show_applied.log", "w", encoding="utf-8")
with contextlib.redirect_stdout(io.TextIOWrapper(io.BytesIO(), encoding="utf-8")):
    g = runpy.run_path(here + 'make_findings.py')
F, pages = g['F'], g['pages']
for p in [int(x) for x in sys.argv[1:]]:
    t = pages[p]
    for f in F:
        if f['page'] == p and f['fix']:
            t = t.replace(f['fix']['old'], f['fix']['new'])
    print('=' * 30, p)
    print(t)
