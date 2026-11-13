"""layers.py: compare the folio 531-536 segment of sga6/diplomatic and sga6/current main.tex and
check that given strings occur exactly once in each layer (read only).
usage: python -I layers.py diff
       python -I layers.py count <file with one JSON string per line>"""
import difflib, json, pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def segment(layer, lo=530, hi=537):
    lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
    start = end = None
    for i, l in enumerate(lines):
        m = MARK.search(l)
        if m:
            f = int(m.group(2))
            if f == lo and start is None:
                start = i
            if f == hi:
                end = i
                break
    return lines[start:end + 1]


mode = sys.argv[1]
if mode == "diff":
    a, b = segment("diplomatic"), segment("current")
    for l in difflib.unified_diff(a, b, "diplomatic", "current", lineterm="", n=0):
        print(l[:300])
    print("segment lengths", len(a), len(b))
else:
    strings = [json.loads(s) for s in pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").splitlines() if s.strip()]
    for layer in ("diplomatic", "current"):
        txt = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
        for s in strings:
            print(layer, txt.count(s), repr(s[:90]))
