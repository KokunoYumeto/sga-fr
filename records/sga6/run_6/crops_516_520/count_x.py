"""Count some forms in Exposé X of SGA 6 main.tex (diplomatic) and locate Exposé IX's single underline."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
BS = "\\"
L = (ROOT / "diplomatic" / "main.tex").read_text(encoding="utf-8").split("\n")
a = next(i for i, l in enumerate(L) if "Exposé X. Formalisme" in l)
b = next((i for i, l in enumerate(L) if l.startswith(BS + "section*{Exposé XI")), len(L))
print("Exposé X lines", a + 1, "-", b)
seg = "\n".join(L[a:b])
for k, p in [("K^circ", re.escape("K^" + BS + "circ")), ("K^{circ}", re.escape("K^{" + BS + "circ")),
             ("K^bullet", r"K\^\{?" + re.escape(BS + "bullet")), ("underline", re.escape(BS + "underline")),
             ("emph", re.escape(BS + "emph")), ("mathcal K", re.escape(BS + "mathcal K")),
             ("mathcal O", re.escape(BS + "mathcal O"))]:
    print("  ", k, len(re.findall(p, seg)))
a9 = next(i for i, l in enumerate(L) if "Exposé IX. Quelques calculs" in l)
for i in range(a9, a):
    if BS + "underline" in L[i]:
        print("IX underline at line", i + 1, ":", L[i][:200])
