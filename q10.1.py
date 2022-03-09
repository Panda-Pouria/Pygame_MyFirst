import pygame as pg
pg.init()
img = pg.image.load('input.jpg')
W, H = img.get_width(), img.get_height()
sc = pg. display.set_mode((W, H))
n = int(input())

for x in range(0,W,n):
    for y in range(0,H,n):
        majmo = 3*[0]
        tedad = 1
        for x1 in range(n):
            for y1 in range(n):
                if x+x1 < W and y+y1 < H:
                    col = img.get_at((x+x1,y+y1))
                    majmo[0] += col[0]
                    majmo[1] += col[1]
                    majmo[2] += col[2]
                    tedad +=1
        miangin_r = majmo[0]/(tedad-1)
        miangin_g = majmo[1]/(tedad-1)
        miangin_b = majmo[2]/(tedad-1)
        for x2 in range(n):
            for y2 in range(n):
                sc.set_at((x+x2, y+y2), (miangin_r,miangin_g,miangin_b))
pg.image.save(sc, 'output.png')
pg.quit()