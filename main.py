from enemy import enemy
import stage
import player
import pygame as pg
from player import fire
import time
from screen import *
from Game import Game
start = True
width = 900
height = 600
score = 0
display = pg.display.set_mode((width,height))
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

# -----------------------Game--------------------------------------------
def level1(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    score1 = 0
    while state == 'retry':
        enemy_list = [enemy(315,515,535),enemy(270,510,275)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score1,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score = score+score1
    return score
def level2(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(315,515,535),enemy(270,510,275)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level3(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(0,170,450),enemy(770,900,450),enemy(0,260,290),enemy(620,900,290)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level4(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(315,465,535),enemy(750,900,430),enemy(310,460,320),enemy(0,150,210)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level5(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(315,465,535),enemy(750,900,420),enemy(150,300,300),enemy(495,695,300),enemy(361,511,200)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level6(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(430,580,535),enemy(0,182,323),enemy(640,890,395),enemy(545,645,237),enemy(230,380,237)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level7(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(135,315,535),enemy(135,315,535),enemy(310,560,375),enemy(20,255,450),enemy(315,415,200),enemy(15,265,300),enemy(15,165,105)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level8(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(315,465,160),enemy(15,150,450),enemy(585,800,450),enemy(30,230,275),enemy(600,800,275)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level9(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(315,515,160),enemy(515,815,535),enemy(330,440,160),enemy(400,500,350),enemy(215,350,450),enemy(525,715,450),enemy(30,230,275),enemy(600,800,275)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score
def level10(key_x,key_y,enemy_list,score,bg):
    state = 'retry'
    while state == 'retry':
        enemy_list = [enemy(15,115,450),enemy(785,885,450),enemy(640,740,375),enemy(130,230,375),enemy(175,275,300),enemy(15,365,160),enemy(535,880,160),enemy(560,740,300)]
        score1,state = Game(display,enemy_list,block_list,key_x,key_y,score,bg)
        if state == 'retry':
            score1 = 0
            score_screen(display,score)
    score =score1
    return score

#-------------------------------- Start ---------------------------------
while start:
    intro = pg.mixer.music.load('audio/Opening.mp3')
    pg.mixer.music.play(-1)
    gameintro(display)
    start = False
#------------------------------------------------------------------------

#-------------------------------lvl 1 -----------------------------------

    

block_list = [[0,150,500],[0,250,250],[250,600,420],[600,960,250],[270,520,325]]
enemy_list = [enemy(315,515,535),enemy(270,510,275)]

score = level1(300,300,enemy_list,score,1)
score_screen(display,score)
#-------------------------------------------------------------------------

#----------------------------------------lvl 2----------------------------
enemy_list = [enemy(0,350,370),enemy(290,640,270)]
block_list = [[290,640,500],[0,350,420],[290,640,320],[0,350,210]]

score = level2(80,185,enemy_list,score,2)
score_screen(display,score)

#----------------------------------------lvl 3----------------------------
enemy_list = [enemy(0,170,450),enemy(770,885,450),enemy(0,260,290),enemy(620,885,290)]
block_list = [[0,150,500],[290,640,500],[770,920,500],[370,520,410],[0,250,340],[620,885,340],[370,520,240]]

score = level3(445,205,enemy_list,score,2)
score_screen(display,score)

#----------------------------------------lvl 4----------------------------
enemy_list = [enemy(315,465,535),enemy(750,900,430),enemy(310,460,320),enemy(0,150,210)]
block_list = [[150,300,480],[310,460,370],[450,600,260],[610,760,150],[750,900,480],[0,150,260]]

score = level4(635,115,enemy_list,score,1)
score_screen(display,score)

#----------------------------------------lvl 5----------------------------
enemy_list = [enemy(315,465,535),enemy(750,900,420),enemy(150,300,300),enemy(495,695,300),enemy(361,511,200)]
block_list = [[0,150,470],[150,300,350],[0,150,250],[750,900,470],[361,511,250],[650,900,172],[495,695,350]]

score = level5(775,137,enemy_list,score,4)
score_screen(display,score)

#----------------------------------------lvl 6----------------------------
enemy_list = [enemy(430,580,535),enemy(0,182,323),enemy(640,890,395),enemy(545,645,237),enemy(230,380,237)]
block_list = [[215,365,480],[0,150,373],[430,580,373],[640,890,445],[545,645,287],[385,535,180],[230,380,287]]


score = level6(255,252,enemy_list,score,2)
score_screen(display,score)

#----------------------------------------lvl 7----------------------------
enemy_list = [enemy(135,315,535),enemy(135,315,535),enemy(310,560,375),enemy(20,255,450),enemy(315,415,200),enemy(15,265,300),enemy(15,165,105)]
block_list = [[15,265,500],[635,885,500],[310,560,425],[15,265,350],[635,885,350],[435,535,300],[315,415,250],[195,295,200],[15,165,150]]


score = level7(55,115,enemy_list,score,4)
score_screen(display,score)

#----------------------------------------lvl 8----------------------------
enemy_list = [enemy(315,465,160),enemy(15,150,450),enemy(585,800,450),enemy(30,230,275),enemy(600,800,275)]
block_list = [[15,365,500],[535,885,500],[400,500,400],[15,265,325],[585,885,325],[325,525,210]]

score = level8(420,285,enemy_list,score,3)
score_screen(display,score)

#----------------------------------------lvl 9----------------------------
enemy_list = [enemy(315,515,160),enemy(515,815,535),enemy(330,440,160),enemy(400,500,350),enemy(215,350,450),enemy(525,715,450),enemy(30,230,275),enemy(600,800,275)]
block_list = [[215,715,500],[400,500,400],[15,265,325],[585,885,325],[325,525,210]]


score = level9(425,185,enemy_list,score,2)
score_screen(display,score)

#----------------------------------------lvl 10----------------------------
enemy_list = [enemy(15,115,450),enemy(785,885,450),enemy(640,740,375),enemy(130,230,375),enemy(175,275,300),enemy(15,365,160),enemy(535,880,160),enemy(560,740,300)]
block_list = [[15,115,500],[310,610,500],[785,885,500],[130,280,425],[640,740,425],[410,510,425],[175,275,350],[270,370,350],[15,365,210],[440,490,280],[540,740,350],[535,885,210],[440,490,110]]

score = level10(475,85,enemy_list,score,3)
score_screen(display,score)

