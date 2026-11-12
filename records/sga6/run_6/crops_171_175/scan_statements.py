import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
t = pathlib.Path(r'C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex').read_text(encoding='utf-8')
L = t.split('\n')
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for i in range(lo, hi):
    l = L[i]
    if l.startswith(r'\textbf{') or r'\uline' in l or r'\underline{' in l or r'\emph{' in l:
        print(i + 1, l[:260])
