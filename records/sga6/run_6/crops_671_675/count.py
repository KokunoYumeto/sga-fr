import sys
# usage: count.py FILE STRING...   (count occurrences of each literal STRING in FILE)
t = open(sys.argv[1], encoding="utf-8", newline="").read()
for s in sys.argv[2:]:
    print(repr(s), t.count(s.replace("\\n", "\n")))
