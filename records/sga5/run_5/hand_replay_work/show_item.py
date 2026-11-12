"""Show one set-aside replay item: the full finding, misprint records of its page,
and the passage in the diplomatic and corrected layers.
usage: python -I show_item.py IDX [ANCHOR] [WIDTH]
IDX: index into REPLAY_MANUAL_5.json, or 'M' for MANUAL_5_findings_231_235.json item 0.
ANCHOR: a substring to locate in both page regions (default: derived from the item)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
run = root / "run_5"


def regions(text):
    out = {}
    ms = list(re.finditer(r"^%{10}  scan idx (\d+)  \|  folio (\S+)  %{10}$", text, re.M))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.setdefault(m.group(2), (m.start(), end))
    return out


def page_text(layer, page):
    t = (root / "sga5" / layer / "s5.tex").read_text(encoding="utf-8")
    r = regions(t)[str(page)]
    return t[r[0]:r[1]]


idx = sys.argv[1]
if idx == "M":
    it = json.load(open(root / "MANUAL_5_findings_231_235.json", encoding="utf-8"))[0]
    old = it["fix"]["old"]
    src = "findings_231_235.json"
else:
    it = json.load(open(root / "REPLAY_MANUAL_5.json", encoding="utf-8"))[int(idx)]
    old = it["old"]
    src = it["source"]
page = it["page"]
print("ITEM", json.dumps(it, ensure_ascii=False, indent=1))
F = json.load(open(run / src, encoding="utf-8"))
for d in F:
    if d.get("page") == page and d.get("fix") and (d["fix"]["old"] == old or old in d["fix"]["old"] or d["fix"]["old"] in old):
        print("FINDING", json.dumps(d, ensure_ascii=False, indent=1))
for m in json.load(open(root / "MISPRINTS_5.json", encoding="utf-8")):
    if m.get("page") == page:
        print("MISPRINT", json.dumps(m, ensure_ascii=False))
anchor = sys.argv[2] if len(sys.argv) > 2 else old[:12]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 400
for layer in ("diplomatic", "current"):
    pt = page_text(layer, page)
    pos = [m.start() for m in re.finditer(re.escape(anchor), pt)]
    print(f"== {layer} p{page}: anchor {anchor!r} at {pos} (page len {len(pt)})")
    for p in pos[:3]:
        print(pt[max(0, p - width):p + len(anchor) + width])
        print("--")
