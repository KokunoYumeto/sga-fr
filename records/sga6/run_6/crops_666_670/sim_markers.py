"""Simulate (in memory, no writes) the marker moves proposed for folios 669, 670, 671 on both layers of SGA 6
main.tex, with the logic of move_marker.py and marker_split_word.py; also compare the batch files with main.tex."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
BATCH = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b666_670"


def move(t, folio, anchor, before=False):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]


def split(t, folio, head, tail):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if not t.startswith(head + tail, le):
        return None
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]


def show(t, folio, n=150):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    return repr(t[max(0, m.start() - n):m.start()]) + "  <<MARKER>>  " + repr(t[m.end():m.end() + n])


def strip(s):
    s = MARK.sub("", s)
    s = s.replace("%\n", "")
    return re.sub(r"\s+", " ", s)


for lay in ("diplomatic", "current"):
    t = open(BASE + "\\" + lay + "\\main.tex", encoding="utf-8").read()
    t0 = t
    for folio, how in ((669, ("move", "d'une", True)),
                       (670, ("move", "\\begin{equation}\\tag{3.1}", True)),
                       (671, ("split", "essentielle", "ment"))):
        t2 = move(t, folio, how[1], how[2]) if how[0] == "move" else split(t, folio, how[1], how[2])
        print(lay, folio, how)
        if t2 is None:
            print("   FAILED")
            continue
        print("   ", show(t2, folio))
        print("    text unchanged modulo whitespace, markers and % joins:", strip(t) == strip(t2))
        t = t2
    print()
    # batch files against the current layer
    if lay == "diplomatic":
        ms = list(MARK.finditer(t0))
        for folio in (666, 667, 668, 669, 670):
            i = next(j for j, m in enumerate(ms) if int(m.group(2)) == folio)
            seg = t0[ms[i].start():ms[i + 1].start()]
            bf = open(BATCH + "\\page_%d.tex" % folio, encoding="utf-8").read()
            bf = bf[bf.index("%%%%%%%%%%"):]
            print("batch", folio, "identical to current diplomatic span:", seg.rstrip() == bf.rstrip())
