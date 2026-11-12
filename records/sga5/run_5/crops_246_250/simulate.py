"""In-memory simulation on the live s5.tex (both layers): apply findings_246_250.json as process_sga.py would, then the
marker moves of the marker findings (move_marker.py logic), in both orders for folio 248. Nothing is written to s5.tex.
Writes the simulated diplomatic span 246..250 to sim_dipl_246_250.tex for a compile test."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
HERE = W / "run_5" / "crops_246_250"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
items = json.loads((W / "run_5" / "findings_246_250.json").read_text(encoding="utf-8"))


def spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


def apply(t, page, old, new):
    s, e = spans(t)[page]
    hits = []
    k = t.find(old, s, e)
    while k >= 0 and k + len(old) <= e:
        hits.append(k)
        k = t.find(old, k + 1, e)
    if len(hits) != 1:
        return t, len(hits)
    k = hits[0]
    return t[:k] + new + t[k + len(old):], 1


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return t, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, "moved"


def region(t, a, b):
    sp = spans(t)
    return t[sp[a][0]:sp[b][0]]


texts = {ed: (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8") for ed in ("diplomatic", "current")}
for ed in texts:
    t = texts[ed]
    for x in items:
        fx = x.get("fix")
        if not fx:
            continue
        if ed == "current" and x["kind"] == "misprint_in_print":
            continue
        t, n = apply(t, int(x["page"]), fx["old"], fx["new"])
        if n != 1:
            print(ed, "FAILED", x["page"], n, repr(fx["old"][:60]))
    texts[ed] = t

A1 = "\\[\nE^{(n)}_r(X)"
A2 = "\\[\n\\mathcal E_r^{(n)}(X)"
for order in ((A1, A2), (A2, A1)):
    res = {}
    for ed in texts:
        t = texts[ed]
        for a in order:
            t, r = move(t, 248, a, True)
            print("order", "A1,A2" if order[0] == A1 else "A2,A1", ed, "248", repr(a), r)
        t, r = move(t, 249, "\\[", True)
        print(ed, "249", r)
        res[ed] = t
    if order[0] == A1:
        first = res
    else:
        print("reverse order gives the same texts:", all(first[e] == res[e] for e in res))

for ed in ("diplomatic", "current"):
    t = first[ed]
    sp = spans(t)
    for f in (248, 249, 251):
        s = sp[f][0]
        print(f"----- {ed}: around folio {f}")
        print(t[max(0, s - 260):s + 200])
(HERE / "sim_dipl_246_250.tex").write_text(region(first["diplomatic"], 246, 251), encoding="utf-8", newline="")
(HERE / "sim_curr_246_250.tex").write_text(region(first["current"], 246, 251), encoding="utf-8", newline="")
