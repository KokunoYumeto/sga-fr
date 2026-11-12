"""Simulate move_marker.py on in-memory copies of both layers (nothing is written), optionally after page edits.
usage: python -I sim_markers.py VOL FOLIO ANCHOR [--before] [--span F1 F2] [--edit OLD NEW]...
Each --edit OLD NEW is applied first, inside the text from the marker of folio F1 to that of F2 (OLD must occur once there); \\n in OLD/NEW means a line break."""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
sys.path.insert(0, str(W))
from sga_config import MARK, files  # noqa: E402

args = sys.argv[1:]
edits = []
while "--edit" in args:
    i = args.index("--edit")
    edits.append((args[i + 1].replace("\\n", "\n"), args[i + 2].replace("\\n", "\n")))
    del args[i:i + 3]
span = (0, 0)
if "--span" in args:
    i = args.index("--span")
    span = (int(args[i + 1]), int(args[i + 2]))
    del args[i:i + 3]
before = "--before" in args
args = [a for a in args if a != "--before"]
vol, folio, anchor = args[0], int(args[1]), args[2]
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        if edits:
            ms = {int(x.group(2)): x for x in MARK.finditer(t)}
            a, b = ms[span[0]].start(), ms[span[1]].start()
            seg = t[a:b]
            for old, new in edits:
                n = seg.count(old)
                if n != 1:
                    print(edition, "edit old occurs", n, "times in the span:", repr(old[:60]))
                    continue
                seg = seg.replace(old, new)
            t = t[:a] + seg + t[b:]
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(edition, "anchor not found")
            continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        p = t2.find(line)
        print("=====", edition)
        print(t2[max(0, p - 200):p + len(line) + 160])
