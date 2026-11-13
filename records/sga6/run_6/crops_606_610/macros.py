"""Resolve the effective definition (at the folio-606 marker) of every macro used in page_606..610.tex (read only).
\\providecommand defines only when the macro is undefined; \\newcommand and \\renewcommand (re)define."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b606_610")
t = ROOT.read_text(encoding="utf-8")
m = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio 606  %%%%%%%%%%", t)
pos606 = m.start()
used = set()
for f in range(606, 611):
    s = (B / f"page_{f}.tex").read_text(encoding="utf-8")
    used |= set(re.findall(r"\\([A-Za-z]+)", s))
defre = re.compile(r"\\(newcommand|renewcommand|providecommand|DeclareMathOperator)\*?\s*\{?\\([A-Za-z]+)\}?\s*(\[[^\]]*\])?\s*\{(.*)$", re.M)
eff = {}
for d in defre.finditer(t[:pos606]):
    kind, name, _, body = d.group(1), d.group(2), d.group(3), d.group(4)
    line = t[:d.start()].count("\n") + 1
    if kind == "providecommand":
        if name not in eff:
            eff[name] = (line, kind, body[:80])
    else:
        eff[name] = (line, kind, body[:80])
for n in sorted(used):
    if n in eff:
        print(n, eff[n])
later = {}
for d in defre.finditer(t[pos606:]):
    name = d.group(2)
    if name in used:
        line = t[:pos606 + d.start()].count("\n") + 1
        later.setdefault(name, []).append((line, d.group(1), d.group(4)[:60]))
print("--- definitions after folio 606 of macros used on these pages:")
for n, v in later.items():
    print(n, v[:3])
