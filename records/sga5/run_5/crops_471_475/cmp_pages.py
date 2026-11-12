import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for ed in ("diplomatic", "current"):
    t = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        f = int(m.group(2))
        if 471 <= f <= 475:
            body = t[m.start(): ms[i+1].start()]
            p = (W / "run_5" / "b471_475" / f"page_{f}.tex").read_text(encoding="utf-8")
            p2 = p.split("\n", 1)[1]
            print(ed, f, "same" if p2 == body else "DIFF", len(p2), len(body))
