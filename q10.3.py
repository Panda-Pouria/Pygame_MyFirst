import pygame as pg
pg.init()
img = pg.image.load('input.jpg')

n = input().split()
xf = float(n[0])
yf = float(n[1])
W, H = img.get_width(), img.get_height()
W, H = int(W*xf), int(H*yf)
sc = pg. display.set_mode((W, H))
for x in range(W):
    for y in range(H):
        col = img.get_at((int(x//xf), int(y//yf)))
        sc.set_at((x, y), col)
pg.image.save(sc, 'output.png')
pg.quit()