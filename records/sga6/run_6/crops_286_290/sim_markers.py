"""In-memory simulation of move_marker.py for the three marker fixes (nothing is written)."""
import pathlib
import re

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")


def move(t, folio, anchor, before=False):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, (folio, "anchor not found")
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


for layer in ("diplomatic", "current"):
    t = (W / layer / "main.tex").read_text(encoding="utf-8")
    print(layer, "count of 'Cet homomorphisme est \\(K'(Y)\\)-linéaire':",
          t.count("Cet homomorphisme est \\(K'(Y)\\)-linéaire"))
    t = move(t, 287, "Cet homomorphisme est")
    t = move(t, 290, "\\section*{3. Compl")
    t = move(t, 291, "est", before=True)
    for folio in (287, 290, 291):
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        print("--", layer, folio)
        print(repr(t[m.start() - 90:m.start()]))
        print(repr(t[m.start():m.end() + 45]))
