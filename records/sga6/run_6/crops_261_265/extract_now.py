"""Extract the present text of folios 261-265 from both layers of SGA 6 main.tex and diff with the batch's page files."""
import difflib, pathlib, sys
sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import MARK, files
sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b261_265")
for edition in ("diplomatic", "current"):
    t = files("6", edition)[0].read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        fo = int(m.group(2))
        if 261 <= fo <= 265:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            now = t[m.start():end]
            (pathlib.Path("now") / f"{edition}_{fo}.tex").write_text(now, encoding="utf-8", newline="")
            old = (B / f"page_{fo}.tex").read_text(encoding="utf-8").split("\n", 1)[1]
            d = list(difflib.unified_diff(old.splitlines(), now.splitlines(), lineterm="", n=0))
            print("==", edition, fo, "diff lines:", len(d))
            for line in d[:40]:
                print("   ", line[:400])
