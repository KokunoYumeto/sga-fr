import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M526 = "%%%%%%%%%%  scan idx 539  |  folio 526  %%%%%%%%%%"
M529 = "%%%%%%%%%%  scan idx 542  |  folio 529  %%%%%%%%%%"
D529 = ("\\[\nD_Y(x)-D_Y(y)=\\dimdot\\mathcal O_{S,y'}-\\dimdot\\mathcal O_{S,x'}"
        "+\\degtr_{k(x')}k(x)-\\degtr_{k(y')}k(y).\n\\]\n")
EDITS = [
    ("de $D$ sur $k(e)$, car ces\n" + M526 + "\npoints sont",
     "de $D$\n" + M526 + "\nsur $k(e)$, car ces points sont"),
    ("On déduit\n" + M529 + "\nalors de (1.5.2) et (1.5.1) :\n" + D529 + "Puisque $S$ est caténaire, on a\n\\[\n",
     "On déduit\nalors de (1.5.2) et (1.5.1) :\n" + D529 + "Puisque $S$ est caténaire, on a\n" + M529 + "\n\\[\n"),
]
for layer in ("diplomatic", "current"):
    p = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex")
    t = p.read_text(encoding='utf-8')
    for old, new in EDITS:
        n = t.count(old)
        line = t[:t.find(old)].count('\n') + 1 if n else None
        print(layer, 'count', n, 'starting line', line)
        if n == 1:
            t = t.replace(old, new)
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        f = int(m.group(2))
        if f in (525, 526, 528, 529):
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            seg = t[m.end():end]
            print('  ', layer, f, 'BEGINS', repr(seg[:90]))
            print('  ', layer, f, 'ENDS  ', repr(seg[-110:]))
