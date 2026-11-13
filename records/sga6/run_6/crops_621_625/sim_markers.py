"""Simulate (in memory, read only) the marker edits of pages 624, 625 and 626 on both SGA 6 layers.

usage: python -I sim_markers.py
Prints, for each layer and each edit, how often 'old' occurs and the text around the boundary after the edit.
Also simulates the move_marker.py logic (--before) for the same three markers, after the p. 624 comma fix.
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
B = "\\"
M624 = "%%%%%%%%%%  scan idx 637  |  folio 624  %%%%%%%%%%"
M625 = "%%%%%%%%%%  scan idx 638  |  folio 625  %%%%%%%%%%"
M626 = "%%%%%%%%%%  scan idx 639  |  folio 626  %%%%%%%%%%"
IMP = B + "(" + B + "Rightarrow" + B + ")"
LANG = B + "(" + B + "langle c_1(L_1)" + B + "cdots c_1(L_s)" + B + "cdot Y" + B + "rangle" + B + ")"

COMMA = ("par (i) " + IMP + " (iv),", "par (i) " + IMP + " (iv)")
EDITS = [
    ("624", "Alors, le\n" + M624 + "\nnombre des polynômes",
     "Alors,\n" + M624 + "\nle nombre des polynômes"),
    ("625 (after the comma fix)", "En effet, par (i) " + IMP + " (iv)\n" + M625 + "\nprenons une surjection",
     "En effet,\n" + M625 + "\npar (i) " + IMP + " (iv) prenons une surjection"),
    ("626", "désigne par " + LANG + " le\n" + M626 + "\nnombre d'intersection",
     "désigne par\n" + M626 + "\n" + LANG + " le nombre d'intersection"),
]


def move_before(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for layer in ("diplomatic", "current"):
    t = open(BASE + "\\" + layer + "\\main.tex", encoding="utf-8").read()
    print("=====", layer)
    print("comma fix old count:", t.count(COMMA[0]))
    t1 = t.replace(COMMA[0], COMMA[1], 1)
    for name, old, new in EDITS:
        n = t1.count(old)
        print("--", name, "old count:", n)
        if n == 1:
            t1 = t1.replace(old, new)
            i = t1.find(new)
            print(repr(t1[max(0, i - 60):i + len(new) + 40]))
    # move_marker.py logic, after the comma fix
    t3 = t.replace(COMMA[0], COMMA[1], 1)
    t3 = move_before(t3, 624, "le")
    t3 = move_before(t3, 625, "par (i)")
    t3 = move_before(t3, 626, LANG)
    for mk in (M624, M625, M626):
        i = t3.find(mk)
        print("move_marker sim:", repr(t3[i - 50:i + len(mk) + 60]))
    print("same result as string edits:", t3 == t1)
