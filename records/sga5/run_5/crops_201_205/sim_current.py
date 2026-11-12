"""In memory only: apply the four proposed moves to the current layer (CRLF) with move_marker.py's logic and show
the text at the markers' old places."""
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_201_205")
sys.stdout.reconfigure(encoding="utf-8")
src = open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_201_205\sim_markers.py",
           encoding="utf-8").read().split("for ed in")[0]
exec(src)
t = open(BASE + r"\current\s5.tex", encoding="utf-8", newline="").read()
for folio, anchor, before in MOVES:
    t = move(t, folio, anchor, before)
for key in ["& K_Y \\arrow[d,", "\\begin{enumerate}[\r", "\\item Ses", "plus familière"]:
    i = t.find(key)
    print(repr(t[i:i + 45]))
