import json, re, sys
W = r"C:\Users\user\Documents\sga_scan_check_20261105"
t = open(W + r"\sga5\diplomatic\s5.tex", encoding="utf-8").read()
BS = chr(92)
print("underline", t.count(BS + "underline{"), "emph", t.count(BS + "emph{"))
lines = t.split("\n")
# Exposé X range: 12684..13754 (1-based)
seg = "\n".join(lines[12683:13753])
for pat in ["underline{", "emph{", "textit{", "leadsto", "rightsquigarrow", "mapsto", "longmapsto", "pmod", "cdot", "operatorname{Sw}", "check{Sw}", "Hom"]:
    print(pat, seg.count(BS + pat), "| whole file:", t.count(BS + pat))
print("-- in X:", seg.count("--"))
for m in re.finditer(r".{30}--.{30}", seg):
    print("   ", m.group(0))
L = json.load(open(W + r"\run_5\findings_146_150.json", encoding="utf-8"))
n = 0
for r in L:
    if r["kind"] == "underline":
        print(r["page"], json.dumps(r["fix"], ensure_ascii=False)[:220])
        n += 1
        if n > 3:
            break
