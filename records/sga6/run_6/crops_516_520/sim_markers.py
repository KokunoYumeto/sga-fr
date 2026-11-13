"""Simulate in memory (writes nothing) the move of the folio-516 marker in both layers of SGA 6 main.tex:
(a) move_marker.py's logic with anchor '\\[' and --before; (b) the exact two-part edit given in the findings.
Prints line numbers and whether (a) == (b)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M516 = "%%%%%%%%%%  scan idx 529  |  folio 516  %%%%%%%%%%"
BS = "\\"


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


EDITS = [
    (BS + "]\n" + M516 + "\nLe\ngroupe", BS + "]\nLe\ngroupe"),
    ("défini par l'algèbre :\n" + BS + "[\n", "défini par l'algèbre :\n" + M516 + "\n" + BS + "[\n"),
]
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    mpos = t.find(M516)
    print(layer, "marker 516 at line", t[:mpos].count("\n") + 1)
    tb = t
    for old, new in EDITS:
        n = tb.count(old)
        pos = tb.find(old)
        print("   edit count", n, "at line", tb[:pos].count("\n") + 1)
        tb = tb.replace(old, new, 1)
    ta = move(t, 516, BS + "[", True)
    print("   move_marker('\\[', --before) == exact edits:", ta == tb)
    p = tb.find(M516)
    print("   new marker line", tb[:p].count("\n") + 1)
    print("   context after move:\n" + tb[p - 120:p + 300])
