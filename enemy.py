import pygame as pg
from player import fire 



class enemy(object):
    left_motion = [pg.image.load('images/enemy/l1.png'),pg.image.load('images/enemy/l2.png'),pg.image.load('images/enemy/l3.png'),pg.image.load('images/enemy/l4.png'),pg.image.load('images/enemy/l5.png'),pg.image.load('images/enemy/l6.png')]
    right_motion = [pg.image.load('images/enemy/r1.png'),pg.image.load('images/enemy/r2.png'),pg.image.load('images/enemy/r3.png'),pg.image.load('images/enemy/r4.png'),pg.image.load('images/enemy/r5.png'),pg.image.load('images/enemy/r6.png')]
    left_stand = pg.image.load('images/enemy/l.png')
    right_stand = pg.image.load('images/enemy/r.png')
    dead_right = pg.image.load('images/enemy/d1.png')
    dead_left = pg.image.load('images/enemy/d.png')
    
    
    def __init__(self,x,x2,y):
        self.x = x
        self.y = y
        self.x2 = x2
        self.width = 30
        self.height = 50
        self.vel = 3
        self.walk = 0
        self.path = [self.x,self.x2]
        self.bullet_hit = 0
        self.shooting = False
        self.bullets = []
        self.h = 0
        

    def draw(self,display,xin,yin):
        self.h = 0
        if not self.shooting:
            self.move()
            if self.walk+1 > 18:
                self.walk = 0
            if self.vel > 0:
                display.blit(self.right_motion[(self.walk//3)],[self.x,self.y])
                self.walk += 1
            else:
                display.blit(self.left_motion[(self.walk//3)],[self.x,self.y])
                self.walk += 1
        else:
            if self.vel > 0:
                display.blit(self.right_stand,[self.x,self.y])
            if self.vel < 0:
                display.blit(self.left_stand,[self.x,self.y])
        for bullet in self.bullets:
            if bullet.x >= 885 or bullet.x < 15 :
                self.bullets.pop(self.bullets.index(bullet))
            elif xin+30 >= bullet.x+10 >= xin  and self.vel > 0 and yin < (bullet.y-5) < yin+50 or bullet.x <= xin+30 and xin <= bullet.x <= xin+30 and self.vel < 0 and yin < (bullet.y-5) < yin+50:
                if bullet in self.bullets:
                    self.bullets.pop(self.bullets.index(bullet))
                self.h+=1
            
                
            else :
                bullet.x += bullet.vel
        for bullet in self.bullets:
            bullet.draw2(display)
                
    def move(self):
        if self.vel > 0:
            if self.x+self.vel+self.width < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk = 0
        elif self.vel < 0:
            if self.x+self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk = 0
    def hit(self):
        self.bullet_hit += 1
    def dead(self,display):
        if self.vel > 0:
            display.blit(self.dead_right,[self.x,self.y])
        if self.vel < 0:
            display.blit(self.dead_left,[self.x,self.y])
    def shoot(self):
        self.shooting = True
        self.facing = self.vel/3
        if len(self.bullets) < 3:
            if self.facing > 0:
                self.bullets.append(fire(self.x+25,self.y+25,self.facing))
            if self.facing < 0:
                self.bullets.append(fire(self.x-5,self.y+25,self.facing))
        
        
        
