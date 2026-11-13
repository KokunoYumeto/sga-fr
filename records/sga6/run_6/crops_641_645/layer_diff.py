import sys, re, difflib
sys.stdout.reconfigure(encoding='utf-8')
# usage: layer_diff.py FIRST_FOLIO END_FOLIO : word diff of diplomatic vs current between the two markers
base = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
a_f, b_f = sys.argv[1], sys.argv[2]
def seg(layer):
    txt = open(base + "\\" + layer + "\\main.tex", encoding="utf-8").read()
    m1 = re.search(r"\|  folio " + a_f + r"  %", txt)
    m2 = re.search(r"\|  folio " + b_f + r"  %", txt)
    return txt[m1.start():m2.start()]
d = seg("diplomatic"); c = seg("current")
dw = re.findall(r"\S+", d); cw = re.findall(r"\S+", c)
sm = difflib.SequenceMatcher(a=dw, b=cw, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        ctx = " ".join(dw[max(0, i1 - 4):i1])
        print(op, "| ...", ctx, "| DIP:", " ".join(dw[i1:i2]), "| CUR:", " ".join(cw[j1:j2]))
