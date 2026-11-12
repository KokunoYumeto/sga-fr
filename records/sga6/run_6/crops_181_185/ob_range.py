"""For the \\Ob uses governed by the \\renewcommand{\\Ob}{\\operatorname{Ob}} of p. 183 (diplomatic main.tex),
list the folio of each use and the ob/Ob forms in that page's OCR (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read()
BS = chr(92)
ren = BS + "renewcommand{" + BS + "Ob}"
m183 = next(m for m in MARK.finditer(t) if int(m.group(2)) == 183)
start = t.find(ren, m183.start())
nxt = t.find(ren, start + 1)
print("renewcommand at char", start, "->", t[start:start + 45])
print("next renewcommand at char", nxt, "->", t[nxt:nxt + 45])
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]


def folio_at(pos):
    f = None
    for p, fo in marks:
        if p <= pos:
            f = fo
        else:
            break
    return f


uses = {}
for m in re.finditer(re.escape(BS + "Ob") + r"(?![A-Za-z])", t[start + 10:nxt]):
    fo = folio_at(start + 10 + m.start())
    uses[fo] = uses.get(fo, 0) + 1
for fo in sorted(uses):
    try:
        o = open(W + rf"\ocr_6\page_{fo:03d}.txt", encoding="utf-8").read()
    except OSError:
        o = ""
    lo = len(re.findall(r"\bob\b", o))
    up = len(re.findall(r"\bOb\b", o))
    print(f"folio {fo}: TeX \\Ob x{uses[fo]}; OCR 'ob' x{lo}, 'Ob' x{up}")
