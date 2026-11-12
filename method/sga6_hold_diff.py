"""SGA 6: the corrections of 23 August were written into the HOLD tree (sga6/corrected/main.tex), not into the corrected
layer (split_r2/corr/main.tex). List every difference between the two, with the SGA-SRC comment nearest to it, so that
each correction can be checked against the scan and then moved into the corrected layer.
Output: sga6/HOLD_VS_CORR.json and a readable sga6/HOLD_VS_CORR.md."""
import difflib
import json
import pathlib
import re

R = pathlib.Path(r"C:\Users\user\Documents\interlanguage\03_projects\language_management\english_germanic"
                 r"\03_working_translations\sga_french_canonical_corpus_20260804_r1\sga6")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
hold = (R / "corrected" / "main.tex").read_text(encoding="utf-8").splitlines()
corr = (R / "split_r2" / "corr" / "main.tex").read_text(encoding="utf-8").splitlines()
orig = (R / "split_r2" / "orig" / "main.tex").read_text(encoding="utf-8").splitlines()
sm = difflib.SequenceMatcher(None, corr, hold, autojunk=False)
out = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    a, b = corr[i1:i2], hold[j1:j2]
    src = [ln for ln in b if "SGA-SRC" in ln]
    near = None
    for k in range(j1, max(-1, j1 - 15), -1):
        if k < len(hold) and "SGA-SRC" in hold[k]:
            near = hold[k].strip()
            break
    out.append(dict(corr_lines=[i1 + 1, i2], hold_lines=[j1 + 1, j2], corr=a, hold=b,
                    src=[re.search(r"SGA-SRC-\d+[^.]*", s).group(0) for s in src] or ([near] if near else []),
                    orig_same_as_corr=orig[i1:i2] == a))
(W / "HOLD_VS_CORR.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
md = ["# SGA 6: differences between the HOLD tree and the corrected layer", ""]
for n, d in enumerate(out, 1):
    md.append(f"## {n}. corr lines {d['corr_lines']}, HOLD lines {d['hold_lines']} {'; '.join(x for x in d['src'] if x)}")
    md.append("corrected layer:")
    md += ["    " + x for x in d["corr"]] or ["    (nothing)"]
    md.append("HOLD tree:")
    md += ["    " + x for x in d["hold"]] or ["    (nothing)"]
    md.append("")
(W / "HOLD_VS_CORR.md").write_text("\n".join(md), encoding="utf-8")
print(len(out), "differences;", sum(1 for d in out if any("SGA-SRC" in (x or "") for x in d["src"])), "with an SGA-SRC note")
