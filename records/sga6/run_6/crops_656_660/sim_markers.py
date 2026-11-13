"""Simulate, in memory only, the marker fixes of pages 656, 659, 660 on both layers of SGA 6 main.tex.
Writes nothing to the TeX files; prints the text around each marker after the edit.
usage: python -I sim_markers.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = "\n"
M656 = "%%%%%%%%%%  scan idx 669  |  folio 656  %%%%%%%%%%"
M659 = "%%%%%%%%%%  scan idx 672  |  folio 659  %%%%%%%%%%"
M660 = "%%%%%%%%%%  scan idx 673  |  folio 660  %%%%%%%%%%"

# exact replacements (old -> new), one per page; each old must occur once per layer
EDITS = {
    656: (r"De $s\ge1$, r\'" + NL + M656 + NL + r"esulte $G'\ne0$",
          M656 + NL + r"De $s\ge1$, r\'esulte $G'\ne0$"),
    659: (NL + "En" + NL + M659 + NL + r"effet, soit $X$",
          NL + M659 + NL + r"En effet, soit $X$"),
    660: (NL + "En" + NL + M660 + NL + r"effet, dans (i)",
          NL + M660 + NL + r"En effet, dans (i)"),
}


def move_marker(t, folio, anchor, before):
    """The logic of move_marker.py, on a string."""
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def around(t, folio, n=120):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    return t[max(0, m.start() - n):m.end() + n]


for layer in ("diplomatic", "current"):
    f = W / layer / "main.tex"
    t = f.read_text(encoding="utf-8")
    print("#####", layer, f)
    for folio, (old, new) in EDITS.items():
        c = t.count(old)
        print(f"--- folio {folio}: exact old occurs {c} time(s)")
        if c == 1:
            t2 = t.replace(old, new)
            print(around(t2, folio))
    for folio, anchor in ((656, r"De $s\ge1$, r"), (659, "En"), (660, "En")):
        t3 = move_marker(t, folio, anchor, True)
        print(f"--- move_marker.py 6 {folio} {anchor!r} --before:")
        print("anchor not found" if t3 is None else around(t3, folio))
