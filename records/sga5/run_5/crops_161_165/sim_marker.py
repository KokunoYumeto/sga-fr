"""Read-only: compare batch page files with the live s5.tex, and simulate move_marker.py in memory (no writes)."""
import io
import pathlib
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
B = W / "run_5" / "b161_165"


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            return m.start(), end
    return None


def simulate(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "ok"


mode = sys.argv[1]
if mode == "compare":
    t = (W / "sga5" / "diplomatic" / "s5.tex").read_text(encoding="utf-8")
    for folio in range(161, 166):
        a, b = span(t, folio)
        live = t[a:b]
        pf = (B / f"page_{folio}.tex").read_text(encoding="utf-8")
        body = pf.split("\n", 1)[1]  # drop '% from s5.tex'
        print(folio, "same" if body.rstrip("\n") == live.rstrip("\n") else "DIFFERENT",
              "line", t[:a].count("\n") + 1)
elif mode == "sim":
    folio, anchor = int(sys.argv[2]), sys.argv[3]
    before = "--before" in sys.argv
    for edition in ("diplomatic", "current"):
        t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
        t2, status = simulate(t, folio, anchor, before)
        print("==", edition, status)
        if t2 is None:
            continue
        m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
        print("marker now at line", t2[:m.start()].count("\n") + 1)
        print(t2[max(0, m.start() - 250):m.end() + 200])
