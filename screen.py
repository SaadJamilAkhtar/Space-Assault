import pygame as pg
import time
import random

from pygame.locals import *


pg.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
green = (0,155,0)
light_green = (0,255,0)
light_yellow = (255,255,0)
blue = (107,177,241)
grey = (192,192,192)
display_width = 900
display_height = 600
gcont = False


score_s = pg.image.load('images/dialog.PNG')
button_pressed = pg.image.load('images/button_p.png')

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption("Space Assault")

story1 = pg.image.load('images/movie/1.jpg')
story2 = pg.image.load('images/movie/2.png')
story3 = pg.image.load('images/movie/3.jpg')


gameExit = False

lead_x = display_width/2
lead_y = display_height/2
Area = display_width * display_height
lead_x_change = 10
lead_y_change = 0
intro = False
clock = pg.time.Clock()
block_size = 20
FPS = 120
score = False
smallfont = pg.font.SysFont('Bank Gothic Lt Bt',30)
mediumfont = pg.font.SysFont('Bank Gothic Lt Bt',50)
largefont = pg.font.SysFont('Bank Gothic Lt Bt',80)

def pause_screen():
    paused = True
    message_to_screen("PAUSED",
                          white,
                          -100,
                          size ='large')
    message_to_screen("Press C to continue or Q to quit",
                          white,
                          25,
                          size='medium')
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    paused = False
                elif event.key == pg.K_q:
                    pg.quit()
                    quit()


        pg.display.update()
        clock.tick(200)
        
                    



backimg = pg.image.load('images/1.jpg')   
img = pg.image.load('images/background.jpg')

def gameintro(gameDisplay):
    global intro
    intro = True
    while intro:
        clock.tick(200)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    intro = False
                if event.key == pg.K_q:
                    pg.quit()
                    quit()

        gameDisplay.blit(backimg,[0,0])
            

        
        

        button("CONTROLS", 400,500,200,30,blue, action = 'controls')
        button("QUIT", 600,500,200,30,blue,action = 'quit')

        button("PLAY", 200,500,200,30, blue,action = 'play')
        
        pg.display.update()
        
    return 0
                          
                          
def text_objects(text,color,size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    if size == 'medium':
        textSurface = mediumfont.render(text, True, color)
    if size == 'large':
        textSurface = largefont.render(text, True, color)    




    return textSurface, textSurface.get_rect()


def score_screen(display,scores):
    global score
    score = True
    
    while score:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    score = False
        gameDisplay.blit(score_s,[200,150])
        button1(display,"", 616,330,action = 'next')
        message_to_screen('Score         :',
                          white,
                          -30,
                          'medium',
                          -80)
        message_to_screen(str(scores),
                          white,
                          -25,
                          'medium',
                          140)

        pg.display.update()

        
        




def text_to_button(msg,color,x,y,width,height,size = 'small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((x + width / 2),(y + height / 2))
    gameDisplay.blit(textSurf, textRect)


    
    
def game_movie(display):
    display.blit(img,[0,0])
    pg.display.update()
    display.blit(story1,[25,25])
    time.sleep(1)
    pg.display.update()
    message = 'During your journey to a distant galaxy'
    text = ''
    for i in range(len(message)):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 0
        display.blit(img,[0,0])
        display.blit(story1,[25,25])
        text += message[i]
        message_to_screen(text,white,-170,'medium',115)
        pg.display.update()
        pg.time.wait(70)
    time.sleep(1)
    display.blit(story2,[575,225])
    pg.display.update()
    message = 'You encountered a ship full of alien predators'
    text = ''
    for i in range(len(message)):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 0
        display.blit(img,[0,0])
        display.blit(story1,[25,25])
        display.blit(story2,[575,225])
        text += message[i]
        message_to_screen(text,white,75,'medium',-65)
        pg.display.update()
        pg.time.wait(70)
    time.sleep(1)
    message = 'The aliens attack your ship'
    text = ''
    for i in range(len(message)):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        display.blit(img,[0,0])
        display.blit(story1,[25,25])
        display.blit(story2,[575,225])
        text += message[i]
        message_to_screen(text,white,75,'medium',-65)
        pg.display.update()
        pg.time.wait(70)
    time.sleep(1)
    display.blit(story3,[50,275])
    pg.display.update()
    message = 'Now you must fight them in order to survive'
    text = ''
    for i in range(len(message)):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 0
        display.blit(img,[0,0])
        display.blit(story1,[25,25])
        display.blit(story2,[575,225])
        display.blit(story3,[50,275])
        text += message[i]
        message_to_screen(text,white,170,'medium',85)
        pg.display.update()
        pg.time.wait(70)
    time.sleep(1)
    return 0



def message_to_screen(msg,color,y_displace=0,size = 'small',x_displace=0):
    textSurf, textRect = text_objects(msg,color,size)

    textRect.center = (int(display_width / 2)+ x_displace),(int((display_height / 2)+ y_displace))
    gameDisplay.blit(textSurf,textRect)

def message_to_screen1(msg,color,y_displace=0,size = 'small',x_displace=0):
    textSurf, textRect = text_objects(msg,color,size)

    textRect.center = (int(display_width / 2)+ x_displace),(int((display_height / 2)+ y_displace))
    gameDisplay.blit(textSurf,textRect)
    

def game_controls(gameDisplay):
    global gcont
    gcont = True
    while gcont:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        gameDisplay.blit(img,[0,0])
        message_to_screen("* CONTROLS *",
                          yellow,
                          -100,
                          "large")
        message_to_screen("Fire :   Spacebar  ",
                          light_yellow,
                          -30,
                          "small")
        message_to_screen("Jump :  Up arrow",
                          light_yellow,
                          10,
                          "small")
        message_to_screen("Move Left and Right :  Left and Right arrows",
                          light_yellow,
                          50,
                          "small")
        message_to_screen("Pause : P Continue: C",
                          light_yellow,
                          100,
                          "small")

        button("Main Menu", 350,500,200,30,blue,action = 'main')


        pg.display.update()






def button(text,x,y,width,height,active_color,action = None):
    global intro
    global score
    global gcont
    cur = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x <= cur[0] <= x + width and y <= cur[1] <= y + height:
        pg.draw.rect(gameDisplay, active_color,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pg.quit()
                quit()
            if action == 'controls':
                game_controls(gameDisplay)
            elif action == 'play':
                game_movie(gameDisplay)
                intro = False
                return 0
            elif action == 'main':
                gcont = False
                gameintro(gameDisplay)
            elif action == 'next':
                score = False
            
            

    text_to_button(text,grey,x,y,width,height)


def button1(display,text,x,y,action = None):
    global score
    cur = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x <= cur[0] <= x+100 and y <= cur[1] <= y+100:
        display.blit(button_pressed,[x,y])
        if click[0] == 1 and action != None:
            if action == 'next':
                score = False


