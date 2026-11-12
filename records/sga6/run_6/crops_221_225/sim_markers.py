"""Simulate move_marker.py (read only): show the text around the marker of FOLIO after moving it before ANCHOR
(searching backwards with --before), in both SGA 6 layers. Writes nothing.
usage: python -I sim_markers.py FOLIO ANCHOR [--before]"""
import pathlib
import re
import sys

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
folio, anchor = int(sys.argv[1]), sys.argv[2]
before = "--before" in sys.argv
out = sys.stdout.buffer
for edition in ("diplomatic", "current"):
    f = W / edition / "main.tex"
    t = f.read_text(encoding="utf-8")
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        out.write(f"{edition}: marker not found\n".encode())
        continue
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        out.write(f"{edition}: anchor not found\n".encode())
        continue
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t3 = t2[:ls] + line + "\n" + t2[ls:]
        pos = ls
    else:
        t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        pos = k
    out.write(f"===== {edition}: before (around old marker)\n".encode())
    out.write(t[max(0, m.start() - 200):m.end() + 120].encode("utf-8"))
    out.write(f"\n===== {edition}: after the move\n".encode())
    out.write(t3[max(0, pos - 200):pos + len(line) + 160].encode("utf-8"))
    out.write(b"\n\n")
