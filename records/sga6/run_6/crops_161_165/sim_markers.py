import re, sys, io, pathlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")

def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    assert k >= 0
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]

def split(t, folio, head, tail):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    assert t.startswith(head + tail, le), repr(t[le:le+40])
    return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]

def show(t, folio, n=160):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    print(repr(t[m.start()-n:m.end()+n]))

for ed in ("diplomatic", "current"):
    t = (base / ed / "main.tex").read_text(encoding="utf-8")
    print("==", ed)
    a = split(t, 161, "com", "plexes"); show(a, 161, 80)
    b = move(t, 162, "hypothèses (1.1", True); b = split(b, 162, "hypo", "thèses"); show(b, 162, 80)
    c = move(t, 164, "\[", True); show(c, 164, 60)
