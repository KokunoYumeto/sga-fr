"""Counts of some forms in Exposé VIII (diplomatic main.tex, from the Exposé VIII heading to the Exposé IX heading)."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
BS = "\\"
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    a = t.find(BS + "section*{Exposé VIII.")
    b = t.find(BS + "section*{Exposé IX.")
    s = t[a:b]
    print("=====", layer, "VIII from line", t[:a].count("\n") + 1, "to", t[:b].count("\n") + 1)
    for key in (BS + "underline", BS + "emph", BS + "textit", BS + "mathbb P", BS + "mathbf", "L^{X/Y}", "L_{" + BS + "bullet}^{X/Y}",
                "L_" + BS + "bullet^{X/Y}", BS + "Omega", BS + "rightsquigarrow", BS + "mapsto", BS + "pmod", BS + "mathcal O",
                BS + "check E", BS + "subsection*{Suite"):
        print(repr(key), s.count(key))
    for key in ("L^{X/Y}", "L_{" + BS + "bullet}", "cotangent"):
        i = s.find(key)
        while i != -1:
            print("   ", key, "|", repr(s[max(0, i - 70):i + 50]))
            i = s.find(key, i + 1)
