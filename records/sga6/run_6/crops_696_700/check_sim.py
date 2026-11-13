"""Check findings_696_700.json against the live SGA 6 editions and simulate it on in-memory copies:
1. every fix's old occurs exactly once in its page's span of the live diplomatic and current main.tex (marker to
   next marker, as process_sga.py looks it up), and touches no marker line; also report the snapshot page_NNN.tex count;
2. apply the fixes by page span (diplomatic: all; current: all but misprints);
3. move marker 698 as move_marker.py does, insert markers 699 and 700 after the given lines;
4. print, for folios 695-700, the first and last lines of each page span; write the simulated tails here."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
B = W / "run_6" / "b696_700"
HERE = pathlib.Path(__file__).parent
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
items = json.loads((W / "run_6" / "findings_696_700.json").read_text(encoding="utf-8"))


def spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


def count_on_page(t, page, old):
    if page not in spans(t):
        return None
    s, e = spans(t)[page]
    return t[s:e].count(old)


live = {ed: (W / "sga6" / ed / "main.tex").read_text(encoding="utf-8") for ed in ("diplomatic", "current")}
ok = True
for i, x in enumerate(items):
    fix = x.get("fix")
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("MISSING corrected", i)
        ok = False
    if not fix:
        continue
    page = int(x["page"])
    snap = B / f"page_{page:03d}.tex"
    ns = snap.read_text(encoding="utf-8").count(fix["old"]) if snap.exists() else None
    nd = count_on_page(live["diplomatic"], page, fix["old"])
    nc = count_on_page(live["current"], page, fix["old"])
    bad = nd != 1 or (x["kind"] != "misprint_in_print" and nc != 1) or MARK.search(fix["old"]) or MARK.search(
        fix["new"])
    if bad or ns != 1:
        print(("BAD " if bad else "note ") + f"item {i} page {page}: live dipl {nd}, live current {nc}, snapshot {ns}:",
              repr(fix["old"]))
    ok = ok and not bad
print("old-uniqueness on the live page spans:", "ok" if ok else "FAILED")


def apply(t, page, old, new):
    s, e = spans(t)[page]
    k = t.find(old, s, e)
    assert k >= 0 and t.find(old, k + 1, e) < 0, (page, old)
    return t[:k] + new + t[k + len(old):]


def move(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.find(anchor, m.start())
    assert k >= 0, (folio, anchor)
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def insert_after(t, after_line, marker):
    assert t.count(after_line + "\n") == 1, after_line
    k = t.find(after_line + "\n") + len(after_line) + 1
    return t[:k] + marker + "\n" + t[k:]


for edition in ("diplomatic", "current"):
    t = live[edition]
    for x in items:
        fix = x.get("fix")
        if not fix or (edition == "current" and x["kind"] == "misprint_in_print"):
            continue
        t = apply(t, int(x["page"]), fix["old"], fix["new"])
    t = move(t, 698, r"\(\operatorname{Gr}^{\bullet}_{\num}")
    t = insert_after(t, r"\(\Mod(U)\) & II & 2.0\\", "%%%%%%%%%%  scan idx 712  |  folio 699  %%%%%%%%%%")
    t = insert_after(t, r"\(\nabla\) & V & 3.5\\", "%%%%%%%%%%  scan idx 713  |  folio 700  %%%%%%%%%%")
    sp = spans(t)
    order = [int(m.group(2)) for m in MARK.finditer(t)]
    print("==", edition, "markers in order:", order == sorted(order), order[-7:])
    for f in range(695, 701):
        s, e = sp[f]
        lines = t[s:e].rstrip("\n").split("\n")
        print(f"  {f}: {len(lines) - 1} lines | first: {lines[1][:72]!r} | last: {lines[-1][:72]!r}")
    a = t.rfind("%%%%%%%%%%  scan idx 708")
    (HERE / f"sim_tail_{edition}.tex").write_text(t[a:], encoding="utf-8", newline="")
