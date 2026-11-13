import sys, re
sys.stdout.reconfigure(encoding='utf-8')
# usage: marker_ctx.py FOLIO [FOLIO ...] : shows the tail of the text before and head after each marker, both layers
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
for layer in ("diplomatic", "current"):
    txt = open(base + "\\" + layer + "\\main.tex", encoding="utf-8").read()
    for f in sys.argv[1:]:
        m = re.search(r"%%%%%%%%%%  scan idx \d+  \|  folio " + f + r"  %%%%%%%%%%", txt)
        if not m:
            print(layer, f, "NO MARKER"); continue
        before = txt[max(0, m.start() - 220):m.start()]
        after = txt[m.end():m.end() + 160]
        print("==", layer, f, "count", len(re.findall(r"\|  folio " + f + r"  %", txt)))
        print(repr(before))
        print("   [MARKER]")
        print(repr(after))
