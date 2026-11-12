"""For the \\Ob uses after the \\renewcommand{\\Ob}{\\operatorname{Ob}} at main.tex line 4366 (p. 183), list per folio
the number of \\Ob uses and the 'ob'/'Ob' words in that page's OCR (read only)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
lines = open(W + r"\sga6\diplomatic\main.tex", encoding="utf-8").read().split("\n")
BS = chr(92)
start, end = 4366, 5338
folio = None
uses = {}
for i, l in enumerate(lines, 1):
    m = MARK.search(l)
    if m:
        folio = int(m.group(2))
    if start <= i < end:
        n = len(re.findall(re.escape(BS + "Ob") + r"(?![A-Za-z])", l))
        if n:
            uses[folio] = uses.get(folio, 0) + n
print("line", start, lines[start - 1][:80])
print("line", end, lines[end - 1][:80])
for fo in sorted(uses):
    try:
        o = open(W + rf"\ocr_6\page_{fo:03d}.txt", encoding="utf-8").read()
    except OSError:
        o = ""
    lo = len(re.findall(r"\bob\b", o))
    up = len(re.findall(r"\bOb\b", o))
    print(f"folio {fo}: TeX \\Ob x{uses[fo]}; OCR 'ob' x{lo}, 'Ob' x{up}")
