"""Move page markers placed by insert_markers.py to better positions:
(a) a marker that splits a heading or statement command (\\section*{ | Exposé VIII}, \\begin{statement}{ | Lemme ...})
    goes before that command;
(b) when the page's OCR text begins with formula lines (no word of four letters), a marker that follows a display
    closely (at most 80 visible characters after its end) goes before that display.
usage: python -I refine_markers.py VOL [--apply]"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import MARK, W, files  # noqa: E402

vol = sys.argv[1]
apply = "--apply" in sys.argv
DISPLAY_END = re.compile(r"\\end\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|displaymath|tikzcd|CD|xy)\}|\\\]|\$\$")
OPEN = {"\\]": "\\[", "$$": "$$"}


def ocr_starts_with_formula(folio):
    p = W / f"ocr_{vol}" / f"page_{folio:03d}.txt"
    if not p.exists():
        return False
    lines = [ln for ln in p.read_text(encoding="utf-8", errors="replace").splitlines() if ln.strip()]
    for _ in range(3):
        if lines and len(re.sub(r"\s", "", lines[0])) <= 15:
            lines = lines[1:]
    return bool(lines) and not re.search(r"[A-Za-z]{4,}", lines[0])


for edition in ("diplomatic", "current"):
    for f in files(vol, edition):
        t = f.read_text(encoding="utf-8")
        moves = []
        for m in MARK.finditer(t):
            folio = int(m.group(2))
            line_start = t.rfind("\n", 0, m.start() - 1) + 1  # start of the line before the marker line
            before = t[line_start:m.start()].rstrip("\n")
            target = None
            # (a) the line before the marker opens a command argument that the marker splits
            if before.lstrip().startswith("\\") and before.count("{") > before.count("}"):
                target = line_start
            # (b) a display right before the marker, and the page starts with a formula
            elif ocr_starts_with_formula(folio):
                window = t[max(0, m.start() - 600):m.start()]
                ends = list(DISPLAY_END.finditer(window))
                if ends:
                    e = ends[-1]
                    tail = window[e.end():]
                    if len(re.sub(r"\s", "", tail)) <= 80:
                        abs_end = max(0, m.start() - 600) + e.end()
                        tok = e.group(0)
                        if tok.startswith("\\end{"):
                            name = e.group(1)
                            k = t.rfind("\\begin{" + name + "}", 0, abs_end)
                        else:
                            k = t.rfind(OPEN[tok], 0, abs_end - len(tok))
                        if k >= 0:
                            target = t.rfind("\n", 0, k) + 1 if t[t.rfind("\n", 0, k) + 1:k].strip() == "" else k
            if target is not None and target < m.start():
                moves.append((m, target))
        for m, target in reversed(moves):
            line = m.group(0)
            end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
            # remove the marker line, then insert it at target on a line of its own
            t = t[:m.start()] + t[end:]
            pre = "" if target == 0 or t[target - 1] == "\n" else "\n"
            t = t[:target] + pre + line + "\n" + t[target:]
        print(edition, f.name, "moved", len(moves), [int(m.group(2)) for m, _ in moves][:60])
        if apply and moves:
            f.write_text(t, encoding="utf-8", newline="")
