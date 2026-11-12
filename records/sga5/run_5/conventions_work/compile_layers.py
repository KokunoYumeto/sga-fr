"""Compile both layers of SGA 5 with pdflatex on temporary copies and summarize the logs.

usage: python -I -X utf8 compile_layers.py TAG
The copies go to the session scratchpad: <SCRATCH>/sga5_compile/<TAG>/<layer>/s5.tex.
Reports per layer: exit code, '!' error lines, pages, overfull boxes, undefined control sequences.
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = 'C:/Users/user/Documents/sga_scan_check_20261105/sga5/'
SCRATCH = ('C:/Users/user/AppData/Local/Temp/claude/f2c80a22394db22f/'
           'a90af538-b007-4c2f-88f6-674802824d58/scratchpad/sga5_compile/')
tag = sys.argv[1]
for layer in ('diplomatic', 'current'):
    d = SCRATCH + tag + '/' + layer + '/'
    os.makedirs(d, exist_ok=True)
    shutil.copyfile(ROOT + layer + '/s5.tex', d + 's5.tex')
    p = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error' if False else '-file-line-error',
                        's5.tex'], cwd=d, capture_output=True, text=True, encoding='utf-8', errors='replace')
    log = open(d + 's5.log', encoding='latin-1').read()
    errs = [l for l in log.split('\n') if l.startswith('!') or re.match(r'^\./s5\.tex:\d+:', l)]
    pages = re.search(r'Output written on s5\.pdf \((\d+) pages', log)
    over = len(re.findall(r'^Overfull \\hbox', log, re.M))
    print(f'{tag} {layer}: exit {p.returncode}, errors {len(errs)}, pages {pages.group(1) if pages else "?"}, '
          f'overfull hbox {over}')
    for e in errs[:20]:
        print('    ', e)
