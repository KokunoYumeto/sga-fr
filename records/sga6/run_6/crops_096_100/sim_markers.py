"""Simulate (in memory, nothing written) the p. 98 fixes of b) Soit and the two marker moves of pp. 99-100 on both
layers of SGA 6 main.tex, with the logic of move_marker.py; print the text around the moved markers.
usage: python -I sim_markers.py"""
import pathlib
import re
import sys

W = pathlib.Path(__file__).resolve().parents[2]
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return m.start(), (ms[i + 1].start() if i + 1 < len(ms) else len(t))
    raise SystemExit(f"no folio {folio}")


def fix_on_page(t, folio, old, new):
    s, e = span(t, folio)
    seg = t[s:e]
    n = seg.count(old)
    if n != 1:
        print("  fix", repr(old[:40]), "occurs", n, "times on", folio)
        return t
    return t[:s] + seg.replace(old, new) + t[e:]


def move(t, folio, anchor, before=True):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print("  anchor not found", repr(anchor))
        return t
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


sys.stdout.reconfigure(encoding="utf-8")
for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    print("==", edition)
    t = fix_on_page(t, 98, r"\textbf{b)}", "b)")
    t = fix_on_page(t, 98, "Soit\n", "\\emph{Soit}\n")
    t = move(t, 99, r"b) \emph{Soit}")
    t = move(t, 100, "«")
    for f in (99, 100):
        s, _ = span(t, f)
        print(f"-- folio {f}:")
        print(t[s - 160:s + 120])
