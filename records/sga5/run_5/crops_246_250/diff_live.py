import sys, re, difflib, pathlib
sys.stdout.reconfigure(encoding='utf-8')
W = pathlib.Path('C:/Users/user/Documents/sga_scan_check_20261105')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for edition in ('diplomatic', 'current'):
    t = (W / 'sga5' / edition / 's5.tex').read_text(encoding='utf-8')
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        f = int(m.group(2))
        if 246 <= f <= 250:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            live = t[m.start():end]
            page = (W / 'run_5' / 'b246_250' / f'page_{f}.tex').read_text(encoding='utf-8')
            page = page.split('\n', 1)[1]  # drop '% from s5.tex'
            if live != page:
                print('=====', edition, f, 'DIFFERS')
                for l in difflib.unified_diff(page.splitlines(), live.splitlines(), 'page', 'live', lineterm='', n=0):
                    print(l)
            else:
                print('=====', edition, f, 'same')
