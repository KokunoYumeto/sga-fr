from PIL import Image, ImageDraw

base = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\b371_375\page_%s_s%s.png'
out = r'C:\Users\user\Documents\sga_scan_check_20261105\run_5\crops_371_375\montage_r.png'
# (label, page, strip, x0, y0, x1, y1)
spots = [
    ('A 374 L2.1 Rf*', 374, 1, 470, 575, 560, 630),
    ('B 374 P2.2 RGx', 374, 2, 920, 585, 1010, 645),
    ('C 374 disp 1st', 374, 3, 340, 300, 420, 375),
    ('D 374 disp 2nd', 374, 3, 615, 300, 695, 375),
    ('E 374 disp Rp*', 374, 3, 700, 300, 790, 375),
    ('F 374 text Rp*', 374, 3, 1100, 410, 1190, 475),
    ('G 374 R^q p*', 374, 3, 735, 565, 815, 625),
    ('H 375 top Rp*', 375, 1, 460, 150, 540, 215),
    ('I 375 ParCons', 375, 2, 480, 315, 570, 375),
    ('J 375 disp 1st', 375, 2, 85, 545, 160, 610),
    ('K 375 disp 2nd', 375, 2, 335, 545, 410, 610),
    ('L 375 disp Rp*', 375, 2, 420, 545, 510, 610),
    ('M 375 conclure', 375, 2, 540, 650, 615, 715),
    ('N 375 verifier', 375, 3, 990, 130, 1070, 195),
    ('O 375 cl(R', 375, 3, 260, 540, 330, 605),
]
scale = 4
tiles = []
for lab, p, s, x0, y0, x1, y1 in spots:
    im = Image.open(base % (p, s)).convert('L').crop((x0, y0, x1, y1))
    im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    t = Image.new('L', (im.width, im.height + 30), 255)
    t.paste(im, (0, 30))
    ImageDraw.Draw(t).text((4, 4), lab, fill=0)
    tiles.append(t)
cols = 5
w = max(t.width for t in tiles)
h = max(t.height for t in tiles)
rows = (len(tiles) + cols - 1) // cols
M = Image.new('L', (cols * (w + 10), rows * (h + 10)), 255)
for i, t in enumerate(tiles):
    M.paste(t, ((i % cols) * (w + 10), (i // cols) * (h + 10)))
M.save(out)
print(M.size)
