import pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_246_250\simulate.py")
lines = p.read_text(encoding="utf-8").split("\n")
out = [l for l in lines if 'move(t, 251' not in l and 'print(ed, "251", r)' not in l]
p.write_text("\n".join(out), encoding="utf-8")
print(len(lines) - len(out), "lines removed")
