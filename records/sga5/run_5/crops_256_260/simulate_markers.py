"""Read-only simulation of two marker moves on both layers of SGA 5 (nothing is written).
258: move_marker.py 5 258 '\\(\\GL(M/\\ell^{n+1}M)\\). Ces' --before
261: marker_split_word.py 5 261 pull '\\begin{prooftext}['"""
import pathlib
import re

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move_before(t, folio, anchor):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    assert k >= 0, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + "\n" + t2[ls:], k
    return t2[:k] + "\n" + line + "\n" + t2[k:], k


def pull(t, folio, piece):
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == folio)
    ls = t.rfind("\n", 0, m.start()) + 1
    le = t.find("\n", m.end()) + 1
    prev_end = ls - 1
    assert t[:prev_end].endswith(piece), "line before the marker does not end with the piece"
    return t[:prev_end - len(piece)].rstrip(" ") + t[prev_end:le] + piece + t[le:], prev_end - len(piece)


for layer in ("diplomatic", "current"):
    t = (W / layer / "s5.tex").read_text(encoding="utf-8")
    t258, k = move_before(t, 258, r"\(\GL(M/\ell^{n+1}M)\). Ces")
    print("==", layer, "258 ==")
    print(repr(t258[k - 60:k + 160]))
    t261, k = pull(t258, 261, "\\begin{prooftext}[")
    print("==", layer, "261 ==")
    print(repr(t261[k - 40:k + 140]))
