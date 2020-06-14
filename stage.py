
# tile width = 60
import pygame as pg
bg1 = pg.image.load('images/bg/1.jpg')
bg2 = pg.image.load('images/bg/2.png')
bg3 = pg.image.load('images/bg/3.jpg')
bg4 = pg.image.load('images/bg/4.jpg')
b1 = pg.image.load('images/ends/1.png')
b2 = pg.image.load('images/ends/2.png')
b3 = pg.image.load('images/ends/3.png')
b4 = pg.image.load('images/ends/4.png')
b5 = pg.image.load('images/ends/5.png')
b6 = pg.image.load('images/ends/6.png')
t1 = pg.image.load('images/Tiles/2.png')
t2 = pg.image.load('images/Tiles/1.png')
k = pg.image.load('images/key.png')
def bg(display,a):
    if a == 1:
        display.blit(bg1,[0,0])
    elif a == 2:
        display.blit(bg2,[0,0])
    elif a == 3:
        display.blit(bg3,[0,0])
    elif a == 4:
        display.blit(bg4,[0,0])
def border(display,width,height):
    distance = 60
    for i in range(0,round(height/distance)+1):
        display.blit(b5,[width-15,i*distance])
    for i in range(0,round(height/distance)+1):
        display.blit(b5,[0,i*distance])
    for i in range(0,round(width/distance)+1):
        display.blit(b6,[i*distance,0])
    for i in range(0,round(width/distance)+1):
        display.blit(b6,[i*distance,height-15])
    display.blit(b2,[width-70,0])
    display.blit(b1,[0,0])
    display.blit(b3,[width-70,height-70])
    display.blit(b4,[0,height-70])
def semi_border(display,width,height):
    distance = 60
    for i in range(0,round(height/distance)+1):
        display.blit(b5,[width-15,i*distance])
    for i in range(0,round(height/distance)+1):
        display.blit(b5,[0,i*distance])
    for i in range(0,round(width/distance)+1):
        display.blit(b6,[i*distance,0])
    display.blit(b2,[width-70,0])
    display.blit(b1,[0,0])
    display.blit(b3,[width-70,height-70])
    display.blit(b4,[0,height-70])
def bottom(display,width,height,x1,x2):
    distance = 60
    for i in range(0,round(x1/100)):
        display.blit(b6,[i*distance,height-15])
    for i in range(0,round((width-x2)/distance)):
        display.blit(b6,[x2+i*distance,height-15])
def tile1(display,x1,x2,h):
    distance = 50
    for i in range(0,round((x2-x1)/distance)):
        display.blit(t1,[i*50+x1,h])
def tile2(display,x1,x2,h):
    distance = 50
    for i in range(0,round((x2-x1)/distance)):
        display.blit(t2,[i*50+x1,h])
def key(display,x,y):
    display.blit(k,[x,y])
    
