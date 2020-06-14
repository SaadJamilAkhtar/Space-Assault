import pygame as pg
display = pg.display.set_mode((900,600))
clock = pg.time.Clock()
jump = 10
step = 0
img = 0
left = [pg.image.load('images/character/l1.png'),pg.image.load('images/character/l2.png'),pg.image.load('images/character/l3.png'),pg.image.load('images/character/l4.png'),pg.image.load('images/character/l5.png'),pg.image.load('images/character/l6.png'),pg.image.load('images/character/l7.png'),pg.image.load('images/character/l8.png')]
right = [pg.image.load('images/character/r1.png'),pg.image.load('images/character/r2.png'),pg.image.load('images/character/r3.png'),pg.image.load('images/character/r4.png'),pg.image.load('images/character/r5.png'),pg.image.load('images/character/r6.png'),pg.image.load('images/character/r7.png'),pg.image.load('images/character/r8.png')]
left_stand = pg.image.load('images/character/l.png')   
right_stand = pg.image.load('images/character/r.png')
left_jump = pg.image.load('images/character/4.png')
right_jump = pg.image.load('images/character/3.png')
h1 = pg.image.load('images/character/h1.png')
h2 = pg.image.load('images/character/h2.png')
h3 = pg.image.load('images/character/h3.png')
h4 = pg.image.load('images/character/h4.png')
h5 = pg.image.load('images/character/h5.png')
h6 = pg.image.load('images/character/h6.png')
p  = pg.image.load('images/character/p.png')

class fire(object):
    b = pg.image.load('images/character/b.png')
    eb = pg.image.load('images/enemy/eb.png')
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 17*facing  # Bullets velocity
    def draw(self,display):
        display.blit(self.b,(self.x,self.y))
    def draw2(self,display):
        display.blit(self.eb,(self.x,self.y))





def player(display,xin,yin,change,lm,rm,rs,ls,jump,jump_h,neg,bullet,health):
    global step
    delta = 0
    if lm == True:
        delta = -change
        step+=1
    elif rm == True:
        delta = change
        step+=1
    if jump == True:
        if jump_h >= -10:
            neg = 1
            if jump_h < 0 :
                neg = -1
            yin -= (jump_h**2)*0.30*neg
            jump_h-=1
        else:
            jump = False
            l_jump = False
            r_jump = False
            jump_h = 10
    xin += delta
    img = (step//3)
    if step+1 >= 24:
        step = 0
    if jump:
        if  rs or rm:
            display.blit(right_jump,[xin,yin])
        elif ls or lm:
            display.blit(left_jump,[xin,yin])
    if not jump:
        if lm:
            display.blit(left[img],[xin,yin])
        elif rm:
            display.blit(right[img],[xin,yin])
        elif rs:
            display.blit(right_stand,[xin,yin])
        elif ls:
            display.blit(left_stand,[xin,yin])
    display.blit(p,[50,40])
    for bullets in bullet:
        bullets.draw(display)
    display.blit(h1,[75,50])
    if health == 10 or health == 9:
        display.blit(h6,[75,50])
    if health == 8 or health == 7:
        display.blit(h5,[75,50])
    if health == 6 or health == 5:
        display.blit(h4,[75,50])
    if health == 4 or health == 3:
        display.blit(h3,[75,50])
    if health == 2 or health == 1:
        display.blit(h2,[75,50])
    return xin,yin,jump_h,neg,jump

