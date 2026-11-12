"""In-memory simulation of the marker moves for folios 372, 373, 374 (reads both layers, writes nothing).
Checks (1) that each exact old string occurs once, (2) that the move_marker.py logic with the proposed
anchor gives the same page split."""
import sys

sys.stdout.reconfigure(encoding="utf-8")
NL = "\n"
base = "C:/Users/user/Documents/sga_scan_check_20261105/sga6/"
M = {
    372: "%%%%%%%%%%  scan idx 385  |  folio 372  %%%%%%%%%%",
    373: "%%%%%%%%%%  scan idx 386  |  folio 373  %%%%%%%%%%",
    374: "%%%%%%%%%%  scan idx 387  |  folio 374  %%%%%%%%%%",
}
EDITS = {
    372: ("Par suite, si \\(M\\) a une" + NL + M[372] + NL + "résolution partielle globale~:",
          "Par suite, si" + NL + M[372] + NL + "\\(M\\) a une résolution partielle globale~:"),
    373: ("base homogène de \\(L\\)" + NL + M[373] + NL + "aient des degrés",
          "base homogène" + NL + M[373] + NL + "de \\(L\\) aient des degrés"),
    374: ("On en déduit une" + NL + M[374] + NL + "suite exacte :" + NL + "\\[",
          "On en déduit une suite exacte :" + NL + M[374] + NL + "\\["),
}
ANCHORS = {372: ("\\(M\\) a une", True), 373: ("de \\(L\\)", True), 374: ("\\[", False)}


def move(t, folio, anchor, before):
    """The logic of move_marker.py, on a string."""
    line = M[folio]
    s = t.index(line)
    e = s + len(line) + (1 if t[s + len(line):s + len(line) + 1] == NL else 0)
    t2 = t[:s] + t[e:]
    k = t2.rfind(anchor, 0, s) if before else t2.find(anchor, s)
    ls = t2.rfind(NL, 0, k) + 1
    if t2[ls:k].strip() == "":
        return t2[:ls] + line + NL + t2[ls:]
    return t2[:k] + NL + line + NL + t2[k:]


for layer in ("diplomatic", "current"):
    t = open(base + layer + "/main.tex", encoding="utf-8").read()
    t_exact, t_script = t, t
    for f in (372, 373, 374):
        old, new = EDITS[f]
        print(layer, f, "exact old count", t.count(old), "marker count", t.count(M[f]))
        t_exact = t_exact.replace(old, new)
        t_script = move(t_script, f, *ANCHORS[f])
    for f in (372, 373, 374):
        for name, tt in (("exact", t_exact), ("script", t_script)):
            i = tt.index(M[f])
            print("  ", name, f, repr(tt[i - 45:i]), "|MARK|", repr(tt[i + len(M[f]):i + len(M[f]) + 45]))
    # the two results differ only in whitespace
    norm = lambda x: " ".join(x.split())
    print(layer, "exact == script up to whitespace:", norm(t_exact) == norm(t_script))
