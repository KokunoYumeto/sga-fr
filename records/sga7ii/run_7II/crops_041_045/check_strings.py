import sys
from pathlib import Path

folder = Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7II\b041_045")
pages = {n: (folder / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(41, 46)}

s = pages[44]
i = s.find("Alors, on a")
print(repr(s[i - 12:i + 60]))
print("alors block count:", s.count("\\underline{Alors, on a} :\n\n\\begin{equation*}"))
for p in (44, 45):
    print(p, "O_Y count:", pages[p].count("\\underline{O}_Y"))
print("n-i+1)) count:", pages[43].count("(n-i+1))"))
print("CRLF present:", any("\r" in t for t in pages.values()))
