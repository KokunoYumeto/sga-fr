import sys

sys.stdout.reconfigure(encoding="utf-8")
base = r"C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b101_105"
for n in range(101, 106):
    s = open(f"{base}/page_{n}.tex", encoding="utf-8").read()
    for i, line in enumerate(s.split("\n"), 1):
        for j, ch in enumerate(line):
            if ord(ch) > 127:
                print(n, i, j, hex(ord(ch)), repr(line[max(0, j - 30):j + 30]))
