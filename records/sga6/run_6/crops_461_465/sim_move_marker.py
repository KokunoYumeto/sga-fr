"""Replicate move_marker.py's logic in memory (writes nothing) for folio 461 (anchor 'Enfin, on remarque', after) and
compare with the exact edit of sim_markers.py."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


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


exec(open(pathlib.Path(__file__).with_name("sim_markers.py"), encoding="utf-8").read().split("for layer in")[0])
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    a = move(t, 461, "Enfin, on remarque", False)
    b = t.replace(EDITS[0][0], EDITS[0][1], 1)
    print(layer, "folio 461: move_marker result == exact edit:", a == b)
