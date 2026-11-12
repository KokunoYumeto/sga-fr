"""Read-only check: compare the batch page files with the live s5.tex, then simulate the marker moves in memory
on both layers (the logic of move_marker.py, nothing is written) and print the text around each moved marker."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
B = W / "run_5"


def page_spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


def move(t, folio, anchor, before):
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


MOVES = [(456, "et $\\varphi_F(U)", True), (457, "\\item", True), (460, "\\[\n\\resizebox", True),
         (461, "\\[\n\\overline{\\fr}_X", True)]

if __name__ == "__main__":
    for layer in ("diplomatic", "current"):
        t = (W / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")
        sp = page_spans(t)
        if layer == "diplomatic":
            for n in range(455, 462):
                d = B / ("b451_455" if n <= 455 else "b456_460" if n <= 460 else "b461_465") / f"page_{n:03d}.tex"
                f = d.read_text(encoding="utf-8")
                body = f.split("\n", 1)[1]  # drop '% from s5.tex'
                s, e = sp[n]
                live = t[s:e]
                print(layer, n, "page file == live span:", body == live, "| live line",
                      t[:s].count("\n") + 1)
        t2 = t
        for folio, anchor, before in MOVES:
            r = move(t2, folio, anchor, before)
            if r is None:
                print(layer, folio, "ANCHOR NOT FOUND")
                continue
            t2 = r
            m = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
            a = t2[max(0, m.start() - 160):m.start()]
            b = t2[m.end():m.end() + 160]
            print(f"--- {layer} folio {folio}: marker now at line {t2[:m.start()].count(chr(10)) + 1}")
            print("   before:", repr(a[-160:]))
            print("   after :", repr(b[:160]))
