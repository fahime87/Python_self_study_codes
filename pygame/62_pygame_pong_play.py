"""
 the pong play by pygame
 the yellow side is user and the red side is computer
 monday,May 8,2023
"""
__outhor__="Fahime Ameri"
__email__="fahime.ameri87@yahoo.com"
import pygame as pg
from pygame.locals import *
def predict(x,y,sx,sy):
    pass
pg.init()
screen=pg.display.set_mode((640,480))
bar1x,bar1y=5,240
bar2x,bar2y=625,290
circlex,circley=30,30
speedx,speedy,speedcir=200,200,200
s1,s2=0,0
bar1s,bar2s=0,0
run=True
clock=pg.time.Clock()
print(clock)
font=pg.font.SysFont("calibri",40)
while run:
    #player bar move
    for event in pg.event.get():
        if event.type==pg.KEYDOWN and event.key==K_UP:
            bar1s=-ai_speed
        elif event.type==pg.KEYDOWN and event.key==K_DOWN:
            bar1s=ai_speed
        elif event.type==pg.KEYUP and (event.key==K_UP or event.key==K_DOWN):
            bar1s=0         
    #draw the the element of pong play in its location   
    screen.fill((0,0,0))
    pg.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    pg.draw.line(screen,(255,255,255),(310,5),(310,470),2)
    pg.draw.rect(screen,(255,255,0)  ,(bar1x,bar1y,10,50),0)
    pg.draw.rect(screen,(255,0,0)    ,(bar2x,bar2y,10,50),0)
    pg.draw.circle(screen,(255,255,255),(circlex,circley),7.5,0)
    score1=font.render(str(s1),True,(255,255,255))
    score2=font.render(str(s2),True,(255,255,255))
    screen.blit(score1,(250,210))
    screen.blit(score2,(380,210))

    #clac the location of ball and bars
    time_pass=clock.tick(40)
    time_sec=time_pass/1000
    circlex+=speedx*time_sec
    circley+=speedy*time_sec
    ai_speed=speedcir*time_sec
    bar1y+=bar1s
    bar2y+=bar2s
    #limit the movement of bars in the ground
    if bar1y>=420 or bar1y<=10:
       bar1s=0
    if bar2y>=420 or bar2y<=10:
       bar2s=0
    #the mirror movement in up and down borders   
    if circley>=470 or circley<=5:
        speedy=-speedy
        
    #robot bar move alg    
    if speedx>0 and circlex>=310:
        #y=predict(circlex,circley,speedx,speedy)
        if bar2y>circley:
            bar2s=-ai_speed
        elif bar2y<circley:
            bar2s=ai_speed
        else:
            bar2s=0
    #calc the scores base on balls hit to borders or bars        
    if circlex>=620:
        if circley>bar2y-7.5 and circley< bar2y+57.5:
            speedx=-speedx
        else :
            s1+=1
            circlex,circley=10,240
    if circlex <= 5:
        if circley>bar1y-7.5 and circley< bar1y+57.5:
            speedx=-speedx
        else :
            circlex,circley=610,240
            s2+=1 
    pg.display.update()
    if s1>=10 or s2>=10 :
        run=False
