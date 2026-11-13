"""Simulate, in memory only (nothing is written), the marker moves proposed for folios 591 and 592 on both layers
of SGA 6 main.tex: (a) the exact replacements given in findings_591_595.json, (b) the equivalent commands
move_marker.py / marker_split_word.py, re-implemented here as in those scripts."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MK591 = "%%%%%%%%%%  scan idx 604  |  folio 591  %%%%%%%%%%"
MK592 = "%%%%%%%%%%  scan idx 605  |  folio 592  %%%%%%%%%%"


def move_marker(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def split_word(t, folio, head, tail):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    assert t.startswith(head + tail, le), repr(t[le:le + 40])
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]


def show(t, folio, before=90, after=70):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    return t[m.start() - before:m.end() + after]


def rendered(t):
    """Crude TeX reading: drop comment lines and '%'+newline, collapse whitespace."""
    t = re.sub(r"%[^\n]*\n[ \t]*", "", t)
    return re.sub(r"\s+", " ", t)


old591 = "nous cherchons des critères\n" + MK591 + "\npour que"
new591 = "nous cherchons des cri%\n" + MK591 + "\ntères pour que"
old592 = "\\item\n" + MK592 + "\n"
new592 = MK592 + "\n\\item\n"
for layer in ("diplomatic", "current"):
    t = (W / layer / "main.tex").read_text(encoding="utf-8")
    print("=====", layer, "| occurrences of the two exact old strings:", t.count(old591), t.count(old592))
    a = t.replace(old591, new591).replace(old592, new592)
    b = split_word(move_marker(t, 591, "critères", True), 591, "cri", "tères")
    b = move_marker(b, 592, "\\item", True)
    print("exact replacements and commands render the same:", rendered(a) == rendered(b))
    print("unchanged text apart from markers:", rendered(a) == rendered(t))
    print("--- 591:\n" + show(a, 591))
    print("--- 592:\n" + show(a, 592))
