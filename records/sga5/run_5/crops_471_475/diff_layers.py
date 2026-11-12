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
for folio in map(int, sys.argv[1:]):
    a, b = page("diplomatic", folio), page("current", folio)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(folio, op, repr(a[max(0,i1-40):i2+40]), "->", repr(b[max(0,j1-40):j2+40]))
