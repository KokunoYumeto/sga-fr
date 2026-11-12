p = "C:/Users/user/Documents/sga_scan_check_20261105/run_5/crops_146_150/build_findings.py"
t = open(p, encoding="utf-8").read()
reps = [
    ("a'^{}_{2!}", "a'_{2!}"),
    ("b'^{}_{1!}", "b'_{1!}"),
    ('    if MARKER := ("%%%%%%%%%%" in old):\n', '    if "%%%%%%%%%%" in old:\n'),
]
for a, b in reps:
    n = t.count(a)
    print(repr(a), n)
    t = t.replace(a, b)
open(p, "w", encoding="utf-8", newline="\n").write(t)
