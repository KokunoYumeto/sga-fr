from PIL import Image

base = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\b111_115"
out = r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I\crops_111_115"

im = Image.open(base + r"\page_115_s3.png").convert("L")

# zoomed crops of the two subscripts, same scale, combined side by side
boxes = [(600, 590, 700, 675), (950, 610, 1050, 695), (500, 590, 600, 675)]
crops = [im.crop(b).resize(((b[2] - b[0]) * 5, (b[3] - b[1]) * 5), Image.LANCZOS) for b in boxes]
W = sum(c.width for c in crops) + 40 * (len(crops) - 1)
H = max(c.height for c in crops)
canvas = Image.new("L", (W, H), 255)
x = 0
for c in crops:
    canvas.paste(c, (x, 0))
    x += c.width + 40
canvas.save(out + r"\zoom_X_vs_x_p115.png")
print(canvas.size)
