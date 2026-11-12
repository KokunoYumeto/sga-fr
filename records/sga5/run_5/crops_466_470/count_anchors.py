"""Count candidate anchors in s5.tex with the marker line of the folio removed (as move_marker.py searches)."""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files  # noqa: E402

CANDS = [
    (466, "donne\n\\[\nL_F=\\prod_i\\left("),
    (466, "donne\n\\["),
    (466, "donne"),
    (468, "propres.\n\nUtilisons"),
    (468, "propres."),
    (469, "$(\\mathbb E^1,\\R^i_!w(F))$"),
    (469, "$(\\mathbb E^1,"),
    (470, "\\[\n\\sum_{n\\ge1}"),
    (471, "\\[\nf^{-n}_{F_{\\bar x}}"),
]
for ed in ("diplomatic", "current"):
    t = files("5", ed)[0].read_text(encoding="utf-8")
    for folio, a in CANDS:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        before = t2[:m.start()].count(a)
        k = t2.rfind(a, 0, m.start())
        print(ed, folio, repr(a), "total", t2.count(a), "| above marker", before,
              "| last above ends at marker" if k >= 0 and k + len(a) >= m.start() - 1 else "")
