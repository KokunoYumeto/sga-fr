import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b101_105"
pats = {
    101: [r"over \u02d9\$k\$", r"\[\\underline\{M\}\(k[^$]*\$"],
    102: [r"X \\arrow\[d,[^\]]*\]", r"\"\\text\{flat\}\"'?\]"],
    103: [r"form \$\(k\[\\epsilon\]; X [^$]*\$", r"\\arrow\[d, \"j_Y\"\]"],
    104: [r"\\underline\{be [^}]*\}", r"\\underline\{D\}\^1_\{Y_0\|X\}\)", r"\\mathrm\{Aut\}_R\([^\n]*"],
    105: [r"and  ?\$\\underline\{M\}_\{X_0\} \\to [^$]*\$  ?by",
          r"and +\$\(R,\\ \\mathfrak\{X\}_\{\(x_0\)\}\)\$ +respectively",
          r"\\mathfrak\{X\}_\{\(\\hat\{x\}_0\)\}",
          r"[^\n]{0,60}\\nu[^\n]{0,40}"],
}
for n, plist in pats.items():
    s = open(f"{base}/page_{n}.tex", encoding="utf-8").read()
    for p in plist:
        ms = [m.group(0) for m in re.finditer(p, s)]
        print(n, p, len(ms))
        for m in ms:
            print("   ", repr(m))
