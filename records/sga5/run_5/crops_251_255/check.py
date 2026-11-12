"""Check findings_251_255.json: every fix's old occurs exactly once (sequentially, in list order) in its page file;
then simulate in memory (no file is written) the fixes on both s5.tex layers, page by page as process_sga.py does,
and the two marker commands, in both orders."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
W = RUN.parent
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
items = json.loads((RUN / "findings_251_255.json").read_text(encoding="utf-8"))

# 1. page files, sequential
texts = {}
for p in range(250, 256):
    folder = "b246_250" if p == 250 else "b251_255"
    texts[p] = (RUN / folder / f"page_{p:03d}.tex").read_text(encoding="utf-8")
bad = 0
for i, x in enumerate(items):
    fx = x.get("fix")
    if not fx:
        continue
    old, new = fx["old"], fx["new"]
    if MARK.search(old) or MARK.search(new):
        print("MARKER IN FIX", i)
        bad += 1
    n = texts[x["page"]].count(old)
    if n != 1:
        print(f"item {i} page {x['page']}: old occurs {n} times: {old!r}")
        bad += 1
        continue
    texts[x["page"]] = texts[x["page"]].replace(old, new, 1)
print("page-file check:", "OK" if not bad else f"{bad} problems")


# 2. s5.tex layers
def spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    for k, m in enumerate(ms):
        s = m.end()
        e = ms[k + 1].start() if k + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (s, e)
    return out


def apply_fixes(t, edition):
    res = []
    for i, x in enumerate(items):
        fx = x.get("fix")
        if not fx:
            continue
        if edition == "current" and x["kind"] == "misprint_in_print":
            continue
        s, e = spans(t)[x["page"]]
        seg = t[s:e]
        n = seg.count(fx["old"])
        if n != 1:
            res.append((i, x["page"], n))
            continue
        k = s + seg.find(fx["old"])
        t = t[:k] + fx["new"] + t[k + len(fx["old"]):]
    return t, res


def move_marker(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0
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
    assert t[:prev_end].endswith(piece), "line before the marker does not end with the piece"
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]


def show(t, folio, before=6, after=6):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    a = t.rfind("\n", 0, m.start())
    for _ in range(before):
        a = t.rfind("\n", 0, a)
    b = m.end()
    for _ in range(after):
        b = t.find("\n", b + 1)
    print(t[a + 1:b])
    print("-----")


for edition in ("diplomatic", "current"):
    src = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    print("=====", edition, "fixes first, then markers")
    t, res = apply_fixes(src, edition)
    print("fixes not applied (index, page, count):", res)
    t = move_marker(t, 251, "\\section*{E", True)
    t = pull(t, 252, "\\(\\ell\\)-")
    show(t, 251, 6, 5)
    show(t, 252, 2, 3)
    show(t, 253, 2, 2)
    print("=====", edition, "markers first, then fixes")
    t = move_marker(src, 251, "\\section*{E", True)
    t = pull(t, 252, "\\(\\ell\\)-")
    t, res = apply_fixes(t, edition)
    print("fixes not applied (index, page, count):", res)
