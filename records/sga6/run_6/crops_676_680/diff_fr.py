"""Token diff of pages 676-680 (diplomatic snapshot) against the fr_r1 second reading (read-only)."""
import difflib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
B = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b676_680"
F = (r"C:\Users\user\Documents\interlanguage_parts\03_projects\language_management\english_germanic"
     r"\03_working_translations\sga6_fr_r1\src\fr.tex")
ours = ""
for p in range(676, 681):
    t = open(B + "\\page_%d.tex" % p, encoding="utf-8").read()
    t = "\n".join(l for l in t.split("\n") if not l.startswith("%"))
    ours += " PAGE%d " % p + t
fr = open(F, encoding="utf-8").read()
a = fr.find("satisfaisante la question soulev")
b = fr.find("par J.P. SERRE.", a) + 15
fr = fr[a - 20:b]
fr = "\n".join(l for l in fr.split("\n") if not l.lstrip().startswith("%"))


def norm(s):
    s = s.replace("\\operatorname{Gr}'_{\\mathrm{top}}", "\\Gtop^\\bullet").replace("\\Gtop^\\bullet", "GTOP")
    s = s.replace("K'", "K^\\bullet")
    return s


tok = re.compile(r"\\[A-Za-z]+|[A-Za-zÀ-ÿ0-9]+|\S")
A = tok.findall(norm(ours))
Bt = tok.findall(norm(fr))
sm = difflib.SequenceMatcher(a=A, b=Bt, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        continue
    ctx = " ".join(A[max(0, i1 - 6):i1])
    print("%s | ...%s | OURS: %s | FR: %s" % (op, ctx, " ".join(A[i1:i2])[:120], " ".join(Bt[j1:j2])[:120]))
