"""Checks for findings_471_475.json: every fix's old occurs exactly once in its page_NNN.tex, no overlaps,
no control characters, no marker lines; also against the live diplomatic layer before and after the simulated
marker moves (read only, nothing is written)."""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
B = W / "run_5" / "b471_475"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
fs = json.loads((W / "run_5" / "findings_471_475.json").read_text(encoding="utf-8"))

pages = {p: (B / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(471, 476)}
ok = True
spans = {}
for i, x in enumerate(fs):
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in x:
            print("missing key", k, i); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected", i); ok = False
    for k in ("where", "scan", "tex", "note", "corrected"):
        if k in x and x[k] and CTRL.search(x[k]):
            print("control char in", k, i); ok = False
    fx = x["fix"]
    if fx is None:
        continue
    old, new = fx["old"], fx["new"]
    if CTRL.search(old) or CTRL.search(new):
        print("control char in fix", i); ok = False
    if MARK.search(old) or MARK.search(new):
        print("marker in fix", i); ok = False
    t = pages[x["page"]]
    n = t.count(old)
    if n != 1:
        print("COUNT", n, "page", x["page"], repr(old)); ok = False
        continue
    s = t.find(old)
    spans.setdefault(x["page"], []).append((s, s + len(old), i))
for p, lst in spans.items():
    lst.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(lst, lst[1:]):
        if a2 < b1:
            print("OVERLAP page", p, i1, i2); ok = False
print("snapshot check:", "OK" if ok else "FAILED")

# live diplomatic layer, before and after the simulated marker moves
def page_spans(t):
    ms = list(MARK.finditer(t))
    return {int(m.group(2)): t[m.start(): ms[j + 1].start() if j + 1 < len(ms) else len(t)] for j, m in enumerate(ms)}

def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]

def split_word(t, folio, mode, *args):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if mode == "split":
        head, tail = args
        assert t.startswith(head + tail, le)
        return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]
    piece = args[0]
    prev_end = ls - 1
    assert t[:prev_end].endswith(piece)
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]

for ed in ("diplomatic", "current"):
    live = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    t = move(live, 471, "\\[", True)
    t = split_word(t, 472, "pull", "$\\ell$-")
    t = split_word(t, 474, "split", "endo", "morphisme")
    t = move(t, 475, "que", True)
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 475)
    assert t[:m.start()].endswith("en cha\n")
    t = t[:m.start() - 1] + "%" + t[m.start() - 1:]
    rerun476 = move(t, 476, "$\\varphi=h", True)
    print(ed, "476 rerun:", "anchor not found" if rerun476 is None else "WOULD MOVE")
    for label, txt in (("live", live), ("after moves", t)):
        ps = page_spans(txt)
        bad = []
        for i, x in enumerate(fs):
            if x["fix"] is None:
                continue
            c = ps[x["page"]].count(x["fix"]["old"])
            if c != 1:
                bad.append((i, x["page"], c, x["fix"]["old"][:50]))
        print(ed, label, "olds not exactly once on their page:", bad if bad else "none")
    # apply all fixes (diplomatic) on the moved text, page by page, to see they all apply in order
    if ed == "diplomatic":
        ps = page_spans(t)
        for p in range(471, 476):
            body = ps[p]
            for x in fs:
                if x["page"] == p and x["fix"] is not None:
                    o, nw = x["fix"]["old"], x["fix"]["new"]
                    assert body.count(o) == 1, (p, o)
                    body = body.replace(o, nw)
            print("applied page", p, "->", len(body), "chars; '%' joins ok" if p != 474 or body.rstrip().endswith("cha%") else "")
counts = {}
for x in fs:
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", counts)
