"""Simulate move_marker.py in memory (no file is written) for the moves proposed by batch 466-470."""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

MOVES = [
    (466, "donne", True),
    (468, "propres.", True),
    (469, "$(\\mathbb E^1,", True),
    (470, "\\[\n\\sum_{n\\ge1}", False),
    (471, "\\[", True),
]


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    if not m:
        return t, "no marker"
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return t, "anchor not found"
    dist = m.start() - k
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, f"moved ({'back' if before else 'forward'} {abs(dist)} chars)"


for ed in ("diplomatic", "current"):
    f = files("5", ed)[0]
    t = f.read_text(encoding="utf-8")
    for folio, anchor, before in MOVES:
        t, msg = move(t, folio, anchor, before)
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        a = t[max(0, m.start() - 90):m.start()].replace("\n", " | ")
        b = t[m.end():m.end() + 90].replace("\n", " | ")
        print(f"{ed} {folio}: {msg}\n   before: ...{a}\n   after : {b}...")
    # second run of each backward move must not find a further anchor that makes sense: report what it would do
    print()
