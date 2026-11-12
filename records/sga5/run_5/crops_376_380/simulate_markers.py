"""Simulate (in memory only, nothing is written) the marker moves proposed for folios 378, 379, 380, 381 of SGA 5
on both layers, and compare the page files of the batch with the diplomatic and current layers."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BATCH = W / "run_5" / "b376_380"


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            ls = t.rfind("\n", 0, m.start()) + 1
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            end = t.rfind("\n", 0, end) + 1
            return t[ls:end]
    return None


def move_marker(t, folio, anchor, before=True):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


def pull(t, folio, piece):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    if not t[:prev_end].endswith(piece):
        return None
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]


layers = {e: (W / "sga5" / e / "s5.tex").read_text(encoding="utf-8") for e in ("diplomatic", "current")}
for folio in range(376, 381):
    pf = (BATCH / f"page_{folio}.tex").read_text(encoding="utf-8")
    body = pf.split("\n", 1)[1]
    for e, t in layers.items():
        s = span(t, folio)
        print(folio, e, "page file equals layer span:", s == body, "| span in layer:", s is not None)

for e, t in layers.items():
    print("=====", e)
    t1 = move_marker(t, 378, "\\[", before=True)
    s = span(t1, 378)
    print("--- 378 after move: head", repr(s[:160]))
    print("--- 377 after move: tail", repr(span(t1, 377)[-160:]))
    t2 = pull(t1, 379, "$C=A\\otimes_{\\Lambda}B$. Les $C$-")
    print("pull 379 ok:", t2 is not None)
    if t2:
        print("--- 379 after pull: head", repr(span(t2, 379)[:200]))
        print("--- 378 after pull: tail", repr(span(t2, 378)[-160:]))
    t3 = move_marker(t2 or t1, 380, "\\subsubsection*{3.7}", before=True)
    print("--- 380 after move: head", repr(span(t3, 380)[:120]))
    print("--- 379 after move: tail", repr(span(t3, 379)[-120:]))
    t4 = move_marker(t3, 381, "$K^{\\bullet}(\\Lambda[G])$ et", before=True)
    print("--- 381 after move: head", repr(span(t4, 381)[:200]))
    print("--- 380 after move: tail", repr(span(t4, 380)[-160:]))
