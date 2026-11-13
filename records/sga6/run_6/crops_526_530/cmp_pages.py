import re, sys, difflib, pathlib
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b526_530")
for layer in ("diplomatic", "current"):
    t = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex").read_text(encoding='utf-8')
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        folio = int(m.group(2))
        if 525 <= folio <= 531:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            seg = t[m.start():end]
            p = B / f"page_{folio}.tex"
            if not p.exists():
                continue
            pt = p.read_text(encoding='utf-8')
            pt = pt.split('\n', 1)[1]  # drop '% from main.tex'
            if seg == pt:
                print(layer, folio, 'identical')
            else:
                print(layer, folio, 'DIFFERS')
                for l in difflib.unified_diff(pt.split('\n'), seg.split('\n'), 'page_file', 'main', lineterm='', n=0):
                    print('   ', l[:300])
