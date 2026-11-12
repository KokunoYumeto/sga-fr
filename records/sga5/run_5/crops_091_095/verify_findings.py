"""Read-only checks of findings_091_095.json: (1) every fix's old occurs exactly once in its page_NNN.tex;
(2) sequential application in list order (as process_sga.py) on the live diplomatic and current s5.tex, in memory;
(3) the marker moves simulated in memory on both layers, before and after the fixes. Nothing is written."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
RUN = W / "run_5"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
items = json.loads((RUN / "findings_091_095.json").read_text(encoding="utf-8"))

# (1) uniqueness in the page files
bad = 0
for i, x in enumerate(items):
    fx = x.get("fix")
    if not fx:
        continue
    t = (RUN / "b091_095" / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1 or MARK.search(fx["old"]) or MARK.search(fx["new"]):
        bad += 1
        print("UNIQUENESS", i, x["page"], n, repr(fx["old"][:60]))
print("uniqueness problems:", bad)


def spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for j, m in enumerate(ms):
        end = ms[j + 1].start() if j + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


def apply_fixes(t, label):
    probs = 0
    for i, x in enumerate(items):
        fx = x.get("fix")
        if not fx:
            continue
        if label == "current" and x["kind"] == "misprint_in_print":
            continue
        sp = spans(t).get(int(x["page"]))
        s, e = sp
        hits = []
        k = t.find(fx["old"], s, e)
        while k >= 0 and k + len(fx["old"]) <= e:
            hits.append(k)
            k = t.find(fx["old"], k + 1, e)
        if len(hits) != 1:
            probs += 1
            print(label, "APPLY FAIL", i, x["page"], len(hits), repr(fx["old"][:60]))
            continue
        k = hits[0]
        t = t[:k] + fx["new"] + t[k + len(fx["old"]):]
    print(label, "apply problems:", probs)
    return t


def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


MOVES = [(92, r"$\H^{2r}_\Delta", False), (94, "d'un", True), (95, r"\[", False)]


def show_moves(t, label):
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    for folio, _, _ in MOVES:
        m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
        a = t[max(0, m.start() - 90):m.start()].replace("\n", "\u23ce")
        b = t[m.end():m.end() + 90].replace("\n", "\u23ce")
        print(f"  [{label}] folio {folio}: ...{a}<<MARKER>>{b}...")
    return t


for ed in ("diplomatic", "current"):
    t0 = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    print("=====", ed, "fixes then moves")
    t1 = apply_fixes(t0, ed)
    t2 = show_moves(t1, ed)
    print("=====", ed, "moves then fixes")
    t3 = show_moves(t0, ed + "-moved")
    apply_fixes(t3, ed + "-moved")
    if ed == "diplomatic" and "--show" in sys.argv:
        sp = spans(t2)
        print(t2[sp[91][0] - 120:sp[96][0] + 200])
