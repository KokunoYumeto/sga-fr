"""check_marker_strings.py: count the exact marker-edit strings in both live main.tex layers (read only)."""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
BS = chr(92)
M522 = "%%%%%%%%%%  scan idx 535  |  folio 522  %%%%%%%%%%"
M523 = "%%%%%%%%%%  scan idx 536  |  folio 523  %%%%%%%%%%"
M526 = "%%%%%%%%%%  scan idx 539  |  folio 526  %%%%%%%%%%"
olds = {
    "522 move": BS + "subsection*{1.2}\n" + M522 + "\n",
    "523 move": BS + "subsection*{1.3}\n" + M523 + "\n",
    "526 move": "de $D$ sur $k(e)$, car ces\n" + M526 + "\npoints sont",
    "heading 1.2": BS + "subsection*{1.2}",
    "heading 1.3": BS + "subsection*{1.3}",
}
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    print(layer, {k: t.count(v) for k, v in olds.items()})
