r"""Apply every fix of findings_201_205.json to the page files in memory and write t.tex (pages 201-205, with the
display opening of p. 201 restored) to check that the edited LaTeX compiles."""
import json

RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
with open(RUN + r"\findings_201_205.json", encoding="utf-8") as fh:
    d = json.load(fh)
pages = {}
for n in range(201, 206):
    with open(RUN + r"\b201_205\page_%03d.tex" % n, encoding="utf-8", newline="") as fh:
        pages[n] = fh.read()
for e in d:
    if e["fix"]:
        t = pages[e["page"]]
        o = e["fix"]["old"]
        k = t.find(o)
        pages[e["page"]] = t[:k] + e["fix"]["new"] + t[k + len(o):]
body = "\n".join(pages[n].split("\n", 1)[1] for n in range(201, 206))
pre = r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools}\usepackage[normalem]{ulem}
\providecommand{\cO}{\mathcal O}\providecommand{\R}{\mathbb R}\providecommand{\N}{\mathbb N}
\providecommand{\Diff}{\operatorname{Diff}}\providecommand{\Homop}{\operatorname{Hom}}
\providecommand{\pr}{\operatorname{pr}}
\begin{document}
\[
  \begin{aligned}
  P^0_{X/S}&\simeq\cO_X,
"""
with open(RUN + r"\crops_201_205\texcheck\t.tex", "w", encoding="utf-8", newline="\n") as fh:
    fh.write(pre + body + "\n\\end{document}\n")
