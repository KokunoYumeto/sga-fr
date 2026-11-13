"""In-memory check of the folio-437 marker edit on both layers of SGA 6 main.tex (writes nothing)."""
import pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[2] / "sga6"
MARK = "%%%%%%%%%%  scan idx 450  |  folio 437  %%%%%%%%%%"
old = r"\(Y'=Y\times_X X'\). On" + "\n" + MARK + "\n" + "sait (EGA II 8.1.8)"
new = r"\(Y'=Y\times_X X'\)." + "\n" + MARK + "\n" + "On sait (EGA II 8.1.8)"
print(repr(old))
for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    n = t.count(old)
    line = t[:t.find(old)].count("\n") + 1 if n else None
    print(layer, "occurrences:", n, "starting line:", line)
    if n == 1:
        t2 = t.replace(old, new)
        k = t2.find(MARK)
        print(repr(t2[k - 60:k + len(MARK) + 40]))
