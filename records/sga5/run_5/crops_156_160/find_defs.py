import sys
path = sys.argv[1]
needles = sys.argv[2:]
lines = open(path, encoding='utf-8').read().split('\n')
for i, l in enumerate(lines, 1):
    for n in needles:
        if n in l:
            print(i, l[:220])
            break
