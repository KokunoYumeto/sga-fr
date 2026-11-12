import sys, re
path = sys.argv[1]
t = open(path, encoding='utf-8').read().split('\n')
start = 6866
end = None
for i in range(start + 5, len(t)):
    if t[i].startswith(r'\section*{Expos') or 'renewenvironment{statement}' in t[i]:
        end = i
        break
print('Expose V lines', start + 1, 'to', end)
seg = t[start:end]
u = sum(l.count(r'\underline{') for l in seg)
e = sum(l.count(r'\emph{') for l in seg)
print('underline', u, 'emph', e)
mode = sys.argv[2] if len(sys.argv) > 2 else 'list'
if mode == 'list':
    for i, l in enumerate(seg):
        if r'\underline{' in l or (r'\emph{' in l and 'Preuve' not in l):
            print(start + i + 1, l[:220])
elif mode == 'grep':
    pat = sys.argv[3]
    for i, l in enumerate(seg):
        if re.search(pat, l):
            print(start + i + 1, l[:300])
