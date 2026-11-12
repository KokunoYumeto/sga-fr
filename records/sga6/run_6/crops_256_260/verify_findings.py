import json, os, re

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
SGA6 = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
F = json.load(open(os.path.join(RUN, "findings_256_260.json"), encoding="utf-8"))

pages = {}
for p in range(256, 261):
    pages[p] = open(os.path.join(RUN, "b256_260", "page_%d.tex" % p), encoding="utf-8").read()

def region(text, p):
    a = text.index("|  folio %d  %%" % p)
    a = text.rindex("\n", 0, a) + 1
    b = text.index("|  folio %d  %%" % (p + 1))
    b = text.rindex("\n", 0, b) + 1
    return text[a:b]

layers = {}
for lay in ("diplomatic", "current"):
    layers[lay] = open(os.path.join(SGA6, lay, "main.tex"), encoding="utf-8").read()

ok = True
bad_chars = re.compile(r"[\x00-\x08\x0b-\x1f\x7f\u00a0]")
for i, f in enumerate(F):
    for key in ("scan", "tex", "note", "where", "corrected"):
        v = f.get(key)
        if isinstance(v, str) and bad_chars.search(v):
            print("CONTROL CHAR in", i, key); ok = False
    fx = f["fix"]
    if fx is None:
        if f["kind"] == "misprint_in_print":
            c = pages[f["page"]].count(f["tex"])
            print(i, f["page"], "misprint tex occurs", c)
        continue
    for key in ("old", "new"):
        if bad_chars.search(fx[key]):
            print("CONTROL CHAR in fix", i, key); ok = False
        if "%%%%" in fx[key]:
            print("MARKER in fix", i); ok = False
    c = pages[f["page"]].count(fx["old"])
    if c != 1:
        print("PAGE COUNT", c, i, f["page"], repr(fx["old"])); ok = False
    for lay, t in layers.items():
        cr = region(t, f["page"]).count(fx["old"])
        if cr != 1:
            print("MAIN", lay, "COUNT", cr, i, f["page"], repr(fx["old"]))

# sequential application per page, in listed order and in reverse order
for order in ("forward", "reverse"):
    for p in range(256, 261):
        t = pages[p]
        fl = [f for f in F if f["page"] == p and f["fix"] is not None]
        if order == "reverse":
            fl = fl[::-1]
        for f in fl:
            c = t.count(f["fix"]["old"])
            if c != 1:
                print(order, "SEQ COUNT", c, p, repr(f["fix"]["old"])); ok = False
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
        if order == "forward":
            with open(os.path.join(RUN, "crops_256_260", "applied_%d.tex" % p), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(t)

from collections import Counter
cnt = Counter((f["page"], f["kind"] == "misprint_in_print") for f in F)
for p in range(256, 261):
    print(p, "normal", cnt[(p, False)], "misprint", cnt[(p, True)])
print("OK" if ok else "PROBLEMS")
