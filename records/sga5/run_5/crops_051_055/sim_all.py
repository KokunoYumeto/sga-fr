"""Read-only end-to-end simulation: apply findings_051_055.json (as process_sga.py would: diplomatic layer, then
non-misprint fixes on the corrected layer) and then the three marker moves (as move_marker.py would), in memory on
both layers of s5.tex; print the resulting pages 51-55 of the diplomatic layer and any failure."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
items = json.loads((W / "run_5" / "findings_051_055.json").read_text(encoding="utf-8"))
MOVES = [(52, "De (5.1.3)", True), (54, "\\section*{B", True), (55, "\\section*{A", True)]


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return m.start(), (ms[i + 1].start() if i + 1 < len(ms) else len(t))
    return None


def apply(t, folio, old, new):
    s, e = span(t, folio)
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
        raise SystemExit(f"anchor not found for {folio}")
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


out = {}
for layer in ("diplomatic", "current"):
    t = (W / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")
    n_ok = 0
    for x in items:
        fx = x.get("fix")
        if not fx:
            continue
        if layer == "current" and x["kind"] == "misprint_in_print":
            continue
        t, n = apply(t, int(x["page"]), fx["old"], fx["new"])
        if n != 1:
            print(layer, "FAILED", x["page"], repr(fx["old"][:60]), n)
        else:
            n_ok += 1
    for folio, anchor, before in MOVES:
        t = move(t, folio, anchor, before)
    print(layer, "fixes applied:", n_ok)
    out[layer] = t
t = out["diplomatic"]
s, _ = span(t, 51)
_, e = span(t, 55)
print(t[s:e])
# environments balanced over the whole file?
for layer in out:
    tt = out[layer]
    b = len(re.findall(r"\\begin\{prooftext\}", tt))
    en = tt.count("\\end{prooftext}")
    print(layer, "prooftext begin/end:", b, en, "(the p. 50 label fix of batch 046_050 removes one begin)")
