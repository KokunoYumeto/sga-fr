import json
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
L = [json.loads(l) for l in open(W + r"\FIXLOG_5.jsonl", encoding="utf-8") if l.strip()]
n = 0
for r in L:
    o, nw = r.get("old") or "", r.get("new") or ""
    if (" - " in nw and " - " not in o) or (" -- " in nw and " -- " not in o) or ("---" in nw and "---" not in o):
        print(r.get("page"), r.get("kind"), repr(o)[:110], "->", repr(nw)[:110])
        n += 1
print("total", n)
m = 0
for r in L:
    o, nw = r.get("old") or "", r.get("new") or ""
    if "rightsquigarrow" in nw or "leadsto" in nw or ("\\cdot" in nw and "\\cdot" not in o):
        print("ARROW/CDOT", r.get("page"), r.get("kind"), repr(o)[:90], "->", repr(nw)[:90])
        m += 1
        if m > 12:
            break
