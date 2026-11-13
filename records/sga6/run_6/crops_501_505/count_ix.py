"""Count underline/emph markup and a few forms in Exposé IX (diplomatic layer)."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(encoding="utf-8")
a = t.find("Exposé IX. Quelques calculs")
b = t.find("Exposé X. Formalisme")
seg = t[a:b]
BS = "\\"
for key in ("underline", "emph", "textit", "mathcal O", "cO", "mathcal{O}", "textbf", "K^" + BS + "circ", "simeq", "Spec"):
    print(key, seg.count(BS + key) if not key.startswith("K^") else seg.count(key))
print("lines", seg.count("\n"))
