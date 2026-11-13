import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
BS = chr(92)
lines = t.split("\n")
def show(label, pat, limit=8):
    hits = [(i + 1, ln) for i, ln in enumerate(lines) if re.search(pat, ln)]
    print(label, len(hits))
    for n, ln in hits[:limit]:
        print("   ", n, ln[:150].encode("ascii", "backslashreplace").decode())
show("wr:", re.escape(BS + "wr"))
show("vertical arrow with sim:", re.escape(BS + "arrow[") + r"[du][^\]]*" + re.escape(BS + "sim"))
show("vertical arrow with wr:", re.escape(BS + "arrow[") + r"[du][^\]]*" + re.escape(BS + "wr"))
