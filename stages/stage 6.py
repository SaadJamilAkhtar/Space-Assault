from enemy import enemy
import stage
import player
import pygame as pg
from player import fire
pg.init()
r = (255,0,0)
display = pg.display.set_mode((900,600))
clock = pg.time.Clock()
bullet1 = pg.mixer.Sound('audio/1.wav')
bullet2 = pg.mixer.Sound('audio/2.wav')

#sound.play()
music = pg.mixer.music.load('audio/dvs.mp3')
pg.mixer.music.play(-1)
xin = 50
yin = 585
change = 8
lm = False
rm = False
ls = False
rs = True
jump = False
jump_h = 10
neg = 1
bullet = []
enemy_list = [enemy(315,465,535),enemy(750,900,430),enemy(310,460,320),enemy(0,150,210)]
block_list = [[150,300,480],[310,460,370],[450,600,260],[610,760,150],[750,900,480],[0,150,260]]
fall = 1
fall_state = True
health = 10
health_list = []

gameExit = False
while not gameExit:
    clock.tick(24)

    for bullets in bullet:
        if bullets.x > 885 or bullets.x < 15:
            if bullets in bullet:
                bullet.pop(bullet.index(bullets))
            
        else :
            bullets.x += bullets.vel
        for enemy in enemy_list:
            if bullets.x+10 >= enemy.x and bullets.x+10 <= enemy.x+30:
                if bullets.y+10 >= enemy.y and bullets.y <= enemy.y+50:
                    if bullets in bullet:
                        enemy.hit()
                        bullet.pop(bullet.index(bullets))
    for enemy in enemy_list:
        if enemy.bullet_hit >= 3:# enemy life
            enemy.dead(display)
            enemy_list.pop(enemy_list.index(enemy))

    for enemy in enemy_list:
        if enemy.y+25 > yin and enemy.y < yin+50 :
            if xin > enemy.x and enemy.vel > 0:
                enemy.shoot()
                bullet2.play()
            elif xin < enemy.x and enemy.vel < 0:
                enemy.shoot()
                bullet2.play()
        else:
            enemy.shooting = False
    for enemy in enemy_list:
        health_list.append(enemy.h)
    if len(health_list) > len(enemy_list):
        health_list.pop(0)
    health -= int(sum(health_list))
    health_list.clear()  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bullet1.play()
                if lm or ls:
                    facing = -1
                elif rm or rs:
                    facing = 1
                if len(bullet) < 8:
                    if rs or rm:
                        bullet.append(fire(xin+35,yin+16,facing))
                    elif ls or lm:
                        bullet.append(fire(xin-5,yin+16,facing))
            if event.key == pg.K_LEFT:
                lm = True
                ls = False
                rs = False
                if not jump:
                    ls = True
            if event.key == pg.K_RIGHT:
                rm = True
                ls = False
                rs = False
                if not jump:
                    rs = True
            if event.key == pg.K_UP:
                jump = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                rs = True
                rm = False
                ls = False
            elif event.key == pg.K_LEFT:
                ls = True
                lm = False
                rs = False
    stage.bg(display,4)
    stage.bottom(display,900,600,250,400)
    stage.border(display,900,600)
    for block in block_list:    
        stage.tile1(display,block[0],block[1],block[2])
    for enemy in enemy_list:
        enemy.draw(display,xin,yin)
    xin,yin,jump_h,neg,jump = player.player(display,xin,yin,change,lm,rm,rs,ls,jump,jump_h,neg,bullet,health)
    player_block = pg.Rect(xin+15,yin+4,20 ,46)
    for block in block_list:
        if pg.Rect(int(block[0]),int(block[2]),int(block[1]-block[0]),20).colliderect(player_block):
                if player_block.bottom > pg.Rect(int(block[0]),int(block[2]),int(block[1]-block[0]),20).top and player_block.top < pg.Rect(int(block[0]),int(block[2]),int(block[1]-block[0]),20).top:
                    jump = False
                    jump_h = 10
                    fall_state = False
                if player_block.top < pg.Rect(int(block[0]),int(block[2]),int(block[1]-block[0]),20).bottom:
                    jump = False
                    jump_h = 10
                    player_block.top = pg.Rect(int(block[0]),int(block[2]),int(block[1]-block[0]),20).bottom
    if fall_state and not jump:
        yin += (fall**2)*0.30
        fall +=1
    if yin+50 >= 580:
        fall = 1
        jump = False
        jump_h = 10
        yin = 535
    fall_state = True
    pg.display.update()
    if len(enemy_list) == 0:
        pg.quit()
        quit()
    if health < 1:
       pg.quit()
       quit()
