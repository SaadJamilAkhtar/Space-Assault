from enemy import enemy
import stage
import player
import pygame as pg
from player import fire
import time
from screen import *



r = (255,0,0)


pg.init()
display = pg.display.set_mode((900,600))
clock = pg.time.Clock()
bullet1 = pg.mixer.Sound('audio/1.wav')
bullet2 = pg.mixer.Sound('audio/2.wav')
damage1 = pg.mixer.Sound('audio/pd.wav')
damage2 = pg.mixer.Sound('audio/ed.wav')
k = pg.mixer.Sound('audio/key.wav')







def Game(display,enemy_list,block_list,key_x,key_y,score,bg):
    

    # Initial variables
#-----------------------------------------------------------------------
    
    music = pg.mixer.music.load('audio/dvs.mp3')
    key = False
    key_appear = True
    pg.mixer.music.play(-1)
    
    xin = 50        #---------Initial X-Position
    
    yin = 585       #---------Initial Y-Position
    
    change = 8      #----------Motion
    
    lm = False      #----------Left Motion
    
    rm = False      #----------Right Motion
    
    ls = False      #----------Left Stand
    
    rs = True       #----------Right Stand
    
    jump = False
    
    jump_h = 10     #--------Jump Height
    neg = 1
    bullet = []
    fall = 1
    fall_state = True
    health = 10
    health_list = []
    block_rect = []
    for block in block_list:
        block_rect.append(pg.Rect(int(block[0]),int(block[2]),int(block[1]-block[0]),25))
    gameExit = False

    # Main Game Loop
#------------------------------------------------------------------------------
    
    while not gameExit:
        
        clock.tick(24)


        
              # Player Bullets
#------------------------------------------------------------------------------
              
        for bullets in bullet:
            if bullets.x > xin+200 or bullets.x < xin-200:  # player bullets max range
                if bullets in bullet:
                    bullet.pop(bullet.index(bullets))
                
            else :
                bullets.x += bullets.vel
                
            for enemy in enemy_list:
                if bullets.x+10 >= enemy.x and bullets.x+10 <= enemy.x+30:
                    if bullets.y+10 >= enemy.y and bullets.y <= enemy.y+50:
                        if bullets in bullet:
                            enemy.hit()
                            damage2.play()
                            bullet.pop(bullet.index(bullets))
                            

            # Enemy Damage
#-----------------------------------------------------------------------------
            
        for enemy in enemy_list:
            if enemy.bullet_hit >= 3:# enemy life
                enemy.dead(display)
                enemy_list.pop(enemy_list.index(enemy))
                score += 50

                
            # Enemy Shooting
#-----------------------------------------------------------------------------
            
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

                
            # Player health
#------------------------------------------------------------------------------
            
        for enemy in enemy_list:
            health_list.append(enemy.h)
        if len(health_list) > len(enemy_list):
            health_list.pop(0)
        if sum(health_list) > 0 :
            health -= int(sum(health_list))
            damage1.play()
        health_list.clear()


        # Event Handeling
#-----------------------------------------------------------------------------
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
                # Key Pressed:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause_screen()

                    
                if event.key == pg.K_SPACE:
                    bullet1.play()
                    if lm or ls:
                        facing = -1
                    elif rm or rs:
                        facing = 1
                    if len(bullet) < 4: # max number of bullets of player at a time
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

                # Key Released
                
            if event.type == pg.KEYUP:
                if event.key == pg.K_c:
                    if rm:
                        rs = True
                        rm = False
                        ls = False
                    elif lm:
                        ls = True
                        lm = False
                        rs = False
                if event.key == pg.K_RIGHT:
                    rs = True
                    rm = False
                    ls = False
                elif event.key == pg.K_LEFT:
                    ls = True
                    lm = False
                    rs = False


                    # Animations Background and stuff
#------------------------------------------------------------------------------------------------------------------
                    
        stage.bg(display,bg)  #background
        stage.bottom(display,900,600,250,400)
        stage.border(display,900,600)
        for block in block_list:    
            stage.tile1(display,block[0],block[1],block[2])
        for enemy in enemy_list:
            enemy.draw(display,xin,yin)
        xin,yin,jump_h,neg,jump = player.player(display,xin,yin,change,lm,rm,rs,ls,jump,jump_h,neg,bullet,health)
        player_block = pg.Rect(xin+15,yin+4,20 ,46)

        
                    # Player motion restrictions
#-----------------------------------------------------------------------------------------------------------------------
        
        for block in block_rect:
            if player_block.colliderect(block):
                if player_block.right >= block.left and player_block.left < block.left:
                    player_block.right = block.left
                if player_block.left <= block.right:
                    player_block.left = block.right
                if player_block.bottom >= block.top and player_block.top < block.top:
                    player_block.bottom = block.top
                    jump = False
                    jump_h = 10
                    fall_state = False
                if player_block.top <= block.bottom:
                   player_block.top = block.bottom
                   jump = False
                   jump_h = 10
                   player_block.top = block.bottom
                    
##        if fall_state:
##            jump = False
        if fall_state and not jump:
            yin += (fall**2)*0.30
            fall +=1
        if yin+50 >= 580:
            fall = 1
            jump = False
            jump_h = 10
            yin = 535
        fall_state = True
        if xin<=15:
            xin = 15
        elif xin >= 835:
            xin = 835
        if yin <= 15:
            yin = 15


        #  Key and score
#----------------------------------------------------------------------------------------------------------------------------

        if not (key_x <= xin+25 <= key_x+35 and yin <= key_y+12 <= yin+50 ):
            if key_appear:
                stage.key(display,key_x,key_y)
        else:
            if key_appear:
                k.play()
            key_appear = False
            key = True
        message_to_screen1("Score: "+str(score),white,-250,'small',350)
        pg.display.update()


        # Stage Ending
#----------------------------------------------------------------------------------------------------------------------------
        
        if len(enemy_list) == 0 and key:
            time.sleep(0.5)
            gameExit = True
            state = 'next'
        if health < 1:
            time.sleep(0.5)
            gameExit = True
            state = 'retry'
    return score,state
