import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_671_675\build_findings.py")
s = p.read_text(encoding="utf-8")
old = 'r"\\arrow[u,"j"\']", r"\\arrow[u,"j"]",'
print("label line found:", s.count(old))
s = s.replace(old, "r'''\\arrow[u,\"j\"']''', r'''\\arrow[u,\"j\"]''',")
old2 = '''    n = t.count(fx["old"])
    if n != 1 or fx["old"] == fx["new"]:'''
new2 = '''    n = t.count(fx["old"])
    if "_after" not in d and work[d["page"]].count(fx["old"]) != 1:
        ok = False
        print("OVERLAP with an earlier fix", i, d["page"], repr(fx["old"][:60]))
    if n != 1 or fx["old"] == fx["new"]:'''
print("check block found:", s.count(old2))
s = s.replace(old2, new2)
p.write_text(s, encoding="utf-8")
