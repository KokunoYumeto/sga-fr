import pathlib
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5\diplomatic\s5.tex").read_text(encoding="utf-8").split("\n")
ex = t[1928:4400]
ov = r"\overset{\mathrm{L}}{\otimes}"
bf = "^{\mathbf L}"
a = [i + 1929 for i, l in enumerate(ex) if ov in l]
b = [i + 1929 for i, l in enumerate(ex) if bf in l]
print("overset lines", len(a), a[:2], a[-2:])
print("mathbf L lines", len(b), b[:2], b[-2:])
