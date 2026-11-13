"""Simulate the three marker moves of pp. 471-473 in memory on both layers (reads main.tex, writes nothing)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
M471 = "%%%%%%%%%%  scan idx 484  |  folio 471  %%%%%%%%%%"
M472 = "%%%%%%%%%%  scan idx 485  |  folio 472  %%%%%%%%%%"
M473 = "%%%%%%%%%%  scan idx 486  |  folio 473  %%%%%%%%%%"
DIAG = ("\\[\n\\begin{tikzcd}[column sep=large,row sep=large]\n"
        "U \\arrow[r,\"i\"] \\arrow[dr,\"f\"'] & V \\arrow[d,\"g\"]\\\\\n"
        "& Y,\n\\end{tikzcd}\n\\]\n")
EDITS = [
    ("471", "par un idéal régulier, c'est un\n" + M471 + "\nanneau d'intersection",
            "par un idéal régulier,\n" + M471 + "\nc'est un anneau d'intersection"),
    ("472", "\\[\n\\begin{tikzcd}[column sep=large,row sep=\n" + M472 + "\nlarge]\n",
            M472 + "\n\\[\n\\begin{tikzcd}[column sep=large,row sep=large]\n"),
    ("473", "et une factorisation :\n" + DIAG + M473 + "\n",
            "et une factorisation :\n" + M473 + "\n" + DIAG),
]
for layer in ("diplomatic", "current"):
    p = rf"C:\Users\user\Documents\sga_scan_check_20261105\sga6\{layer}\main.tex"
    t = open(p, encoding="utf-8", newline="").read()
    assert "\r\n" not in t, "CRLF"
    for name, old, new in EDITS:
        n = t.count(old)
        pos = t.find(old)
        line = t[:pos].count("\n") + 1 if pos >= 0 else None
        nlines = old.count("\n") + 1
        print(f"{layer} marker {name}: old occurs {n}x, lines {line}-{line + nlines - 1 if line else None}")
        if n == 1:
            t = t.replace(old, new)
    # show result around the moved markers
    for m in (M471, M472, M473):
        i = t.find(m)
        print("----", layer, m[18:40])
        print(t[max(0, i - 160):i + len(m) + 120])
    print("=" * 60)
