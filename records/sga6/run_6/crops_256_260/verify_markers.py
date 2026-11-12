import json, os, re

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
SGA6 = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
F = json.load(open(os.path.join(RUN, "findings_256_260.json"), encoding="utf-8"))
raw = open(os.path.join(RUN, "findings_256_260.json"), "rb").read()
print("utf-8 e-acute bytes present:", b"\xc3\xa9" in raw)

MK = re.compile(r"^%%%%%%%%%%  scan idx \d+  \|  folio \d+  %%%%%%%%%%$", re.M)

def body(t):
    return re.sub(r"\s+", "", MK.sub("", t))

layers = {lay: open(os.path.join(SGA6, lay, "main.tex"), encoding="utf-8").read() for lay in ("diplomatic", "current")}
for f in F:
    if f["kind"] != "marker":
        continue
    note = f["note"]
    m = re.search(r"replace '(.*)' by '(.*?)'(?:, so that|\.$)", note, re.S)
    if not m:
        print("cannot parse", f["page"]); continue
    old = m.group(1).replace("\\n", "\n")
    new = m.group(2).replace("\\n", "\n")
    for lay, t in layers.items():
        c = t.count(old)
        t2 = t.replace(old, new, 1)
        print(f["page"], lay, "old count", c, "| text apart from markers kept:", body(t) == body(t2),
              "| marker lines:", len(MK.findall(t)) == len(MK.findall(t2)))
