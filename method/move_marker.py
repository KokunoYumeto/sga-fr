"""Move the marker of printed page FOLIO so that it stands on its own line just before the first occurrence of
ANCHOR found after (or before, with --before) the marker's present place, in both editions of the volume.
usage: python -I move_marker.py VOL FOLIO ANCHOR [--before] [--dry]"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import MARK, files  # noqa: E402

vol, folio, anchor = sys.argv[1], int(sys.argv[2]), sys.argv[3]
before = "--before" in sys.argv
dry = "--dry" in sys.argv
for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        if not m:
            continue
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        if k < 0:
            print(edition, f.name, "anchor not found")
            continue
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        print(edition, f.name, "moved page", folio, "to before", repr(anchor[:40]))
        if not dry:
            f.write_text(t2, encoding="utf-8", newline="")
