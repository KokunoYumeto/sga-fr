"""List every use and definition of the coker macro with its folio, in both layers of main.tex (read only)."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
BS = "\\"
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"%%%%%%%%%%  scan idx \d+  \|  folio (\d+)  %%%%%%%%%%", t)]
    print("==", layer, len(t))
    for m in re.finditer(re.escape(BS + "coker") + r"(?![A-Za-z])", t):
        f = [fo for (p, fo) in marks if p < m.start()]
        f = f[-1] if f else None
        ln = t[:m.start()].count("\n") + 1
        print(ln, "folio", f, repr(t[max(0, m.start() - 50):m.start() + 45]))
