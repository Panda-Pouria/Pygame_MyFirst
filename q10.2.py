import pygame as pg
pg.init()
img = pg.image.load('input1.jpg')
img2 = pg.image.load('input2.jpg')
W, H = img.get_width(), img.get_height()
sc = pg. display.set_mode((W, H))
a = int(input())
a2 = 100-a
for x in range(W):
    for y in range(H):
        col1 = list(img.get_at((x, y)))
        col2 = list(img2.get_at((x,y)))
        col3 = 3*[0]
        for i in range(3):
            col3[i] += col1[i]*a2 + col2[i]*a
        for i in range(3):
            col3[i]=col3[i]/(a+a2)
        sc.set_at((x, y), col3)
pg.image.save(sc, 'output.png')
pg.quit()