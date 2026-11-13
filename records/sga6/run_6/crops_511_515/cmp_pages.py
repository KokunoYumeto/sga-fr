import sys, pathlib, re
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(__file__).resolve().parent.parent / "b511_515"
for layer in ("diplomatic", "current"):
    t = pathlib.Path(rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex").read_text(encoding="utf-8")
    for p in range(511, 516):
        pt = (B / f"page_{p}.tex").read_text(encoding="utf-8")
        body = pt.split("\n", 1)[1]  # from the marker line on
        marker = body.split("\n", 1)[0]
        i = t.find(marker)
        j = t.find("|  folio %d  " % (p + 1))
        j = t.rfind("\n", 0, j) + 1
        seg = t[i:j]
        print(layer, p, "same" if seg.rstrip("\n") == body.rstrip("\n") else "DIFFERENT", len(seg), len(body))
