import sys
sys.stdout.reconfigure(encoding="utf-8")
t = open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_546_550\expX_dipl.txt", encoding="utf-8").read()
key = sys.argv[1]
i = t.find(key)
while i >= 0:
    print(t.count("\n", 0, i) + 13383, t[max(0, i - 70):i + len(key) + 40].replace("\n", " | "))
    i = t.find(key, i + 1)
