"""Darkest small blob between two digits: python -I gapdot.py FILE X0 Y0 X1 Y1
prints the min grey value and the 5x5 mean minimum inside the box, and the background median."""
import sys
import numpy as np
from PIL import Image
f = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
a = np.array(Image.open(f).convert('L')).astype(float)
box = a[y0:y1, x0:x1]
from numpy.lib.stride_tricks import sliding_window_view as sw
m = sw(box, (5, 5)).mean(axis=(2, 3))
i, j = np.unravel_index(m.argmin(), m.shape)
print('min', box.min(), '5x5 min mean', round(m.min(), 1), 'at', (x0 + j + 2, y0 + i + 2), 'bg median', np.median(box))
