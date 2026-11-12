import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_331_335\build_findings.py")
s = p.read_text(encoding="utf-8")
BS = chr(92)
reps = [
    ('"(4.5)  (no commas)", r"),&' + BS + 'text{(4.5)},' + BS + BS + '"',
     '"(4.5)  (no commas)", r",&' + BS + 'text{(4.5)},' + BS + BS + '"'),
    ('"..., dans C(N^)  (comma before ' + "'dans'; 'dans' underlined)" + '"',
     '"..., dans C' + chr(176) + '(N^).  (comma before ' + "'dans'; 'dans' underlined)" + '"'),
    ('"y c_r(N-check) , dans  (comma; ' + "'dans' underlined)" + '"',
     '"y c_r(N-check) , dans C' + chr(176) + '(S).  (comma; ' + "'dans' underlined)" + '"'),
]
for a, b in reps:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
print("patched")
