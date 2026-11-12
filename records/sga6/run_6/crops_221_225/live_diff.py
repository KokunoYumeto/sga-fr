"""Compare the page files of this batch with the live SGA 6 diplomatic main.tex spans (read only).
usage: python -I live_diff.py"""
import difflib
import pathlib
import re
import sys

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
t = (W / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8")
ms = list(MARK.finditer(t))
span = {}
for i, m in enumerate(ms):
    end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
    span[int(m.group(2))] = t[m.start():end]
out = sys.stdout.buffer
for folio in range(221, 226):
    page = (W / "run_6" / "b221_225" / f"page_{folio}.tex").read_text(encoding="utf-8")
    body = page.split("\n", 1)[1]  # drop the '% from main.tex' line
    live = span.get(folio, "")
    if body == live:
        out.write(f"{folio}: identical\n".encode())
    else:
        out.write(f"{folio}: DIFFERS\n".encode())
        for l in difflib.unified_diff(body.split("\n"), live.split("\n"), "page", "live", lineterm="", n=1):
            out.write((l + "\n").encode("utf-8"))
