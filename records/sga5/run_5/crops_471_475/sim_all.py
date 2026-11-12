"""Simulate in memory (no writes) the marker fixes of batch 471-475 on both live layers of s5.tex."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")

def move(t, folio, anchor, before):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        print("anchor not found", folio); return t
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:]
    return t2[:k] + "\n" + line + "\n" + t2[k:]

def split_word(t, folio, mode, *args):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    if mode == "split":
        head, tail = args
        assert t.startswith(head + tail, le), "split: text after marker"
        return t[:ls] + head + "%\n" + t[ls:le] + t[le + len(head):]
    piece = args[0]
    prev_end = ls - 1
    assert t[:prev_end].endswith(piece), "pull: line end"
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:]

def show(t, folio, n=110):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    print("   ", folio, repr(t[m.start() - n:m.end() + n]))

out = {}
for ed in ("diplomatic", "current"):
    t = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    t = move(t, 471, "\[", True)
    t = split_word(t, 472, "pull", "$\ell$-")
    t = split_word(t, 474, "split", "endo", "morphisme")
    t = move(t, 475, "que", True)
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 475)
    assert t[:m.start()].endswith("en cha\n")
    t = t[:m.start() - 1] + "%" + t[m.start() - 1:]
    print(ed)
    for f in (471, 472, 474, 475, 476):
        show(t, f)
    out[ed] = t
# second run of the 471 move would go further back: show where
t = out["diplomatic"]
m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 471)
t3 = move(t, 471, "\[", True)
m3 = next(m for m in MARK.finditer(t3) if int(m.group(2)) == 471)
print("second 471 run would move the marker back by", m.start() - m3.start(), "chars")
# 476: re-running the (already applied) move finds nothing before the marker?
t4 = move(out["diplomatic"], 476, "$\varphi=h", True)
print("476 rerun changed text:", t4 != out["diplomatic"])
import pickle
(pathlib.Path(__file__).parent / "sim_after_moves.pkl").write_bytes(pickle.dumps(out))
