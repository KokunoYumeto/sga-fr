"""In-memory check of the marker moves for folios 351, 352, 353 on both layers of SGA 6 main.tex (writes nothing).
Literal replacements, and the same moves done as move_marker.py would do them (anchor, --before)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
M351 = "%%%%%%%%%%  scan idx 364  |  folio 351  %%%%%%%%%%"
M352 = "%%%%%%%%%%  scan idx 365  |  folio 352  %%%%%%%%%%"
M353 = "%%%%%%%%%%  scan idx 366  |  folio 353  %%%%%%%%%%"
BS = "\\"
REPL = [
    ("dans le cas où " + BS + "(A" + BS + ") est l'%\n" + M351 + "\nanneau",
     "dans le cas\n" + M351 + "\noù " + BS + "(A" + BS + ") est l'anneau"),
    (" " + BS + "((" + BS + "Ch A)_n" + BS + ") est un " + BS + "(" + BS + "lambda" + BS + ")-idéal.\n\n" + M352 + "\nSoit alors",
     "\n" + M352 + "\n" + BS + "((" + BS + "Ch A)_n" + BS + ") est un " + BS + "(" + BS + "lambda" + BS + ")-idéal.\n\nSoit alors"),
    (" " + BS + "(x-" + BS + "gamma^n(x')" + BS + "in(" + BS + "Ch A)_{n+1}" + BS + "). En\n" + M353 + "\nitérant",
     "\n" + M353 + "\n" + BS + "(x-" + BS + "gamma^n(x')" + BS + "in(" + BS + "Ch A)_{n+1}" + BS + "). En itérant"),
]
ANCHORS = [(351, "où " + BS + "(A" + BS + ") est"),
           (352, BS + "((" + BS + "Ch A)_n" + BS + ") est un " + BS + "(" + BS + "lambda" + BS + ")-idéal."),
           (353, BS + "(x-" + BS + "gamma^n(x')" + BS + "in")]


def move(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


for layer in ("diplomatic", "current"):
    t = (ROOT / layer / "main.tex").read_text(encoding="utf-8")
    lit = t
    for old, new in REPL:
        n = lit.count(old)
        print(layer, "literal count", n, repr(old[:40]))
        if n == 1:
            lit = lit.replace(old, new)
    mv = t
    for folio, anchor in ANCHORS:
        mv = move(mv, folio, anchor)
    # compare rendered text (newlines/spaces collapsed, % joins) between the two methods
    def norm(s):
        s = re.sub(r"%\n", "", s)
        return re.sub(r"\s+", " ", s)
    print(layer, "literal == move_marker (after whitespace normalisation):", norm(lit) == norm(mv))
    for f in (351, 352, 353):
        m = next(m for m in MARK.finditer(lit) if int(m.group(2)) == f)
        print("   ", f, repr(lit[m.start() - 70:m.end() + 70]))
