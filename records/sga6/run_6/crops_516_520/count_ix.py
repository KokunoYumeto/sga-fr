"""Count some forms in Exposé IX (and the head of X) of both layers of SGA 6 main.tex, and in the page files."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b516_520")
BS = "\\"
PATS = {
    "K^circ": re.escape(BS + "circ"),
    "K^{bullet}/K^bullet": r"K\^\{?\\bullet",
    "K_bullet": r"K_\\bullet",
    "underline": re.escape(BS + "underline"),
    "emph": re.escape(BS + "emph"),
    "mathbb D": r"\\mathbb\s*\{?D",
    "mathbf D": r"\\mathbf\s*\{?D",
    "D(": r"(?<![A-Za-z\\])D\(",
    "coprod": re.escape(BS + "coprod"),
    "bigoplus": re.escape(BS + "bigoplus"),
    "mathcal O": r"\\mathcal\s*\{?O",
    "pmod": re.escape(BS + "pmod"),
}
for layer in ("diplomatic", "current"):
    lines = (ROOT / layer / "main.tex").read_text(encoding="utf-8").split("\n")
    a = next(i for i, l in enumerate(lines) if "Exposé IX. Quelques calculs" in l)
    b = next(i for i, l in enumerate(lines) if "Exposé X. Formalisme" in l)
    seg = "\n".join(lines[a:b])
    print(layer, "Exposé IX lines", a + 1, "-", b)
    for k, p in PATS.items():
        print("   ", k, len(re.findall(p, seg)))
for p in range(516, 521):
    t = (B / f"page_{p}.tex").read_text(encoding="utf-8")
    print(p, {k: len(re.findall(v, t)) for k, v in PATS.items() if re.findall(v, t)})
