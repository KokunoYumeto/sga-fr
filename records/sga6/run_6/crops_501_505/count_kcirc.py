"""Count K^circ (and other raised-dot forms) in Exposé IX of both layers and on the five page files."""
import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b501_505")
KC = "K^" + "\\" + "circ"
for layer in ("diplomatic", "current"):
    lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(lines) if "Exposé IX. Quelques calculs" in l)
    end = next(i for i, l in enumerate(lines) if "Exposé X. Formalisme" in l)
    seg = "\n".join(lines[start:end])
    print(layer, "Exposé IX lines", start + 1, "-", end, ": K^circ", seg.count(KC),
          " K^{circ}", seg.count("K^{" + "\\" + "circ}"), " K^bullet", seg.count("K^" + "\\" + "bullet") + seg.count("K^{" + "\\" + "bullet}"),
          " K' ", len(re.findall(r"K'", seg)))
    # also Exposés VII, VIII, X totals for context
    for a, b in (("Exposé VII.", "Exposé VIII."), ("Exposé VIII.", "Exposé IX."), ("Exposé X.", "Exposé XI.")):
        try:
            s = next(i for i, l in enumerate(lines) if a in l and "section" in l)
            e = next(i for i, l in enumerate(lines) if b in l and "section" in l)
            print("   ", a, "lines", s + 1, "-", e, "K^circ", "\n".join(lines[s:e]).count(KC))
        except StopIteration:
            print("   ", a, "not found")
for p in range(501, 506):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    print(p, "K^circ", t.count(KC), "mathcal O", t.count("\\mathcal O"), "underline", t.count("\\underline"), "emph", t.count("\\emph"))
