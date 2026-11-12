"""Compare the page files of this batch with the current text between the markers in both layers of s5.tex,
and check each fix's old string against the current page text of the diplomatic layer."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:/Users/user/Documents/sga_scan_check_20261105")
RUN = W / "run_5"
for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    ms = {int(m.group(2)): m for m in MARK.finditer(t)}
    for p in range(271, 276):
        cur = t[ms[p].start():ms[p + 1].start()]
        page = (RUN / "b271_275" / f"page_{p}.tex").read_text(encoding="utf-8")
        body = page.split(chr(10), 1)[1]
        same = body == cur
        print(edition, p, "same" if same else "DIFFERENT", len(body), len(cur))
        if not same and edition == "diplomatic":
            for i, (a, b) in enumerate(zip(body, cur)):
                if a != b:
                    print("   first difference at", i, repr(body[max(0, i - 60):i + 60]), "|", repr(cur[max(0, i - 60):i + 60]))
                    break
    if edition == "diplomatic":
        F = json.loads((RUN / "findings_271_275.json").read_text(encoding="utf-8"))
        for it in F:
            if it["fix"]:
                p = it["page"]
                cur = t[ms[p].start():ms[p + 1].start()]
                n = cur.count(it["fix"]["old"])
                if n != 1:
                    print("   old not unique in current page text:", p, repr(it["fix"]["old"]), n)
    else:
        F = json.loads((RUN / "findings_271_275.json").read_text(encoding="utf-8"))
        for it in F:
            if it["fix"]:
                p = it["page"]
                cur = t[ms[p].start():ms[p + 1].start()]
                n = cur.count(it["fix"]["old"])
                if n != 1:
                    print("   current layer: old occurs", n, "times on", p, repr(it["fix"]["old"]))
