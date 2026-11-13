"""Write t.tex (pages 476-480 after the fixes of findings_476_480.json, in one run) and t_orig.tex (unfixed)."""
import json

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
F = json.load(open(RUN + r"\findings_476_480.json", encoding="utf-8"))
P = {n: open(RUN + rf"\b476_480\page_{n}.tex", encoding="utf-8", newline="").read() for n in range(476, 481)}
orig = dict(P)
for x in F:
    if x["fix"]:
        assert P[x["page"]].count(x["fix"]["old"]) == 1
        P[x["page"]] = P[x["page"]].replace(x["fix"]["old"], x["fix"]["new"])
HEAD = "\n".join([
    r"\documentclass[11pt]{article}",
    r"\usepackage[T1]{fontenc}",
    r"\usepackage[utf8]{inputenc}",
    r"\usepackage[a4paper,margin=2cm]{geometry}",
    r"\usepackage{amsmath,amssymb}",
    r"\usepackage{tikz-cd}",
    r"\DeclareMathOperator{\Spec}{Spec}",
    r"\begin{document}",
    ""])
for name, pages in (("t", P), ("t_orig", orig)):
    body = "".join(pages[n] for n in range(476, 481))
    open(RUN + rf"\crops_476_480\tikztest\{name}.tex", "w", encoding="utf-8", newline="\n").write(
        HEAD + body + "\n" + r"\end{document}" + "\n")
print("ok")
