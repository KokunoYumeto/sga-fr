"""Check line numbering of the folio markers 501-506 in both layers (split on LF only) and look for CR / other separators."""
import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
for layer in ("diplomatic", "current"):
    raw = (ROOT / layer / "main.tex").read_bytes()
    print(layer, "bytes", len(raw), "LF", raw.count(b"\n"), "CR", raw.count(b"\r"), "FF", raw.count(b"\x0c"), "VT", raw.count(b"\x0b"))
    t = raw.decode("utf-8")
    print("   U+2028", t.count("\u2028"), "U+2029", t.count("\u2029"), "U+0085", t.count("\u0085"), "U+001C-1E", sum(t.count(c) for c in "\x1c\x1d\x1e"))
    lines = t.split("\n")
    for f in range(500, 507):
        key = f"|  folio {f}  %"
        hits = [i + 1 for i, l in enumerate(lines) if key in l]
        print("   folio", f, "marker lines (LF count):", hits)
