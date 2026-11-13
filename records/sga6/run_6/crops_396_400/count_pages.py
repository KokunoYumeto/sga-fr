"""Per page file of b396_400: count the strings a scripted D/G/P pass would touch (read only)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b396_400")
pats = {
    "D( (not after a letter or backslash)": re.compile(r"(?<![A-Za-z\\])D\("),
    "D_" + BS + "pi(": re.compile(r"(?<![A-Za-z\\])D_\\pi\("),
    "G_S^{": re.compile(r"(?<![A-Za-z\\])G_S\^\{"),
    BS + "mathbb P": re.compile(r"\\mathbb P"),
    BS + "cdots": re.compile(r"\\cdots"),
    "other capital D": re.compile(r"(?<![A-Za-z\\])D(?![(_'a-z])"),
    "other capital G": re.compile(r"(?<![A-Za-z\\])G(?!_S)"),
}
for f in range(396, 401):
    t = (B / f"page_{f}.tex").read_text(encoding="utf-8")
    body = t.split("\n", 2)[2]
    out = {k: len(p.findall(body)) for k, p in pats.items()}
    print(f, {k: v for k, v in out.items() if v})
    for k in ("other capital D", "other capital G"):
        for m in pats[k].finditer(body):
            print("   ", k, repr(body[max(0, m.start() - 20):m.end() + 20]))
