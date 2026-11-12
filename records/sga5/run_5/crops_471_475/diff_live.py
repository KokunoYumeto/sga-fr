import pathlib, re, sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
def page(ed, folio):
    t = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return t[m.start(): ms[i+1].start()]
for ed in ("diplomatic", "current"):
    for folio in map(int, sys.argv[1:]):
        a = (W / "run_5" / "b471_475" / f"page_{folio}.tex").read_text(encoding="utf-8").split("\n", 1)[1] if folio <= 475 else ""
        b = page(ed, folio)
        if folio > 475:
            print(ed, folio, repr(b[:400])); continue
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                print(ed, folio, op, repr(a[max(0,i1-60):i2+60]), "->", repr(b[max(0,j1-60):j2+60]))
