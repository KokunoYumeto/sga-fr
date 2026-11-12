"""Apply the fixes of findings_461_465.json in memory, in listed and in reverse order; report any old that is not unique."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5")
items = json.loads((RUN / "findings_461_465.json").read_text(encoding="utf-8"))


def page_file(p):
    for d in RUN.glob("b*_*"):
        f = d / f"page_{p:03d}.tex"
        if f.exists():
            return f


for order in ("listed", "reverse"):
    seq = items if order == "listed" else list(reversed(items))
    texts = {}
    ok = True
    for x in seq:
        fx = x["fix"]
        if not fx:
            continue
        p = x["page"]
        t = texts.setdefault(p, page_file(p).read_text(encoding="utf-8"))
        n = t.count(fx["old"])
        if n != 1:
            ok = False
            print(order, "page", p, "count", n, repr(fx["old"]))
            continue
        texts[p] = t.replace(fx["old"], fx["new"])
    print(order, "ok" if ok else "PROBLEMS")
    if order == "listed":
        for p in sorted(texts):
            (RUN / "crops_461_465" / f"sim_page_{p}.tex").write_text(texts[p], encoding="utf-8", newline="\n")
