import sys, pathlib, difflib
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(__file__).resolve().parent.parent / "b511_515"
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\current\main.tex").read_text(encoding="utf-8")
pt = (B / "page_511.tex").read_text(encoding="utf-8")
body = pt.split("\n", 1)[1]
marker = body.split("\n", 1)[0]
i = t.find(marker)
j = t.find("|  folio 512  ")
j = t.rfind("\n", 0, j) + 1
seg = t[i:j]
sm = difflib.SequenceMatcher(None, body, seg)
for op in sm.get_opcodes():
    if op[0] != "equal":
        a0, a1, b0, b1 = op[1:]
        print(op[0], repr(body[a0-30:a1+30]), "->", repr(seg[b0-30:b1+30]))
