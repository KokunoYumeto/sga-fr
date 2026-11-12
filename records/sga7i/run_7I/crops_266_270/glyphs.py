import sys
from PIL import Image, ImageOps
import numpy as np
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b266_270/page_270_s2.png'
out = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/crops_266_270/'
im = np.array(Image.open(src).convert('L')).astype(float)
# line containing 'eignalé' : rows ~760-820
band = im[755:825, :]
dark = band < 150
cols = dark.any(axis=0)
# find runs of dark columns (glyphs)
runs = []
start = None
for x, c in enumerate(cols):
    if c and start is None:
        start = x
    elif not c and start is not None:
        runs.append((start, x)); start = None
if start is not None: runs.append((start, len(cols)))
print(runs)
