"""Count emph and underline commands in the diplomatic main.tex between folios 540 and 600 (read only)."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
BS = chr(92)
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(encoding="utf-8")
def pos(f):
    m = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + str(f) + r"  %%%%%%%%%%", t)
    return m.start()
s = t[pos(540):pos(600)]
print("emph", s.count(BS + "emph{"), "underline", s.count(BS + "underline{"))
for m in list(re.finditer(re.escape(BS + "underline{") + r"[^}]*\}", s))[:10]:
    print("  U", m.group(0))
for m in list(re.finditer(re.escape(BS + "emph{") + r"[^}]*\}", s))[:6]:
    print("  E", m.group(0))
