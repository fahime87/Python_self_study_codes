"""
 writitng brickout game by pygame library
 tuesday,may 16,2023
"""
__outhor__="Fahime Ameri"
__email__="fahime.ameri87@yahoo.com"

import pygame as pg
import random,sys

class BreakOut():
    def __init__(self):
        self.width=640
        self.height=480
        
        self.clock=pg.time.Clock()
        self.x_speed_init,self.y_speed_init,self.bat_speed=2,2,3
        self.max_live=5
        self.x_ball=30
        self.y_ball=self.height/2
        pg.init()
        self.screen=pg.display.set_mode((self.width,self.height))
        self.bat=pg.image.load("bat.png").convert()
        self.ball=pg.image.load("ball.jpg").convert()
        self.bat_rec=self.bat.get_rect()
        self.ball_rec=self.ball.get_rect()
        self.pong = pg.mixer.Sound('Blip_1-Surround-147.wav')
        self.pong.set_volume(10)
        
        #pg.key.set_repeat(1,30)



    def game_loop(self):
        print("start")
        live=self.max_live
        run=True
        pong=self.pong
        wall=Wall(self)
        wall.make_wall()
        x_speed=self.x_speed_init
        y_speed=self.y_speed_init
        self.score=0
        height=self.height
        width=self.width
        bat_speed=self.bat_speed
        self.bat_rec=self.bat_rec.move(width/2-self.bat_rec.right/2,height-20)
        self.ball_rec=self.ball_rec.move(self.x_ball,self.y_ball)
        bat_sp=0
        while run:
            self.clock.tick(60)
            self.screen.fill((0,0,0))
            for event in pg.event.get():
                if event.type==pg.KEYDOWN:
                    if event.key== pg.K_ESCAPE:
                        run=False
                        break
                    if event.key==pg.K_RIGHT :
                        if self.bat_rec.right<width:
                            bat_sp=bat_speed
                        else:
                            bat_sp=0

                    if event.key==pg.K_LEFT :
                        if self.bat_rec.left >0:
                            bat_sp=-bat_speed
                        else:
                            bat_sp=0

                elif event.type==pg.KEYUP :
                     bat_sp=0
            #hit the ball to right and left side                
            if self.ball_rec.left<=0 or self.ball_rec.right>=width:
                 x_speed=-x_speed
                 pong.play(0)
            #hit the ball to top     
            if self.ball_rec.top<=0:
                y_speed=-y_speed
                pong.play(0)
            #hit the ball to bat    
            if self.ball_rec.bottom>= self.bat_rec.top and self.ball_rec.bottom<=self.bat_rec.bottom and self.ball_rec.left>=self.bat_rec.left and self.ball_rec.right<=self.bat_rec.right:
                y_speed=-self.y_speed_init
                pong.play(0)
            #when ball loss dosnt hit the bat and loos life    
            if self.ball_rec.bottom>=height:
                pong.play(0)
                live-=1
                x=random.randint(0,width)
                if x>width/2:
                    x_speed=-self.x_speed_init
                self.ball_rec.center=x,self.y_ball
            # when ball hit the wall
            index=self.ball_rec.collidelist(wall.brick_list)
            if index>=0:
                self.score+=10
                pong.play(0)
                collid_element=wall.brick_list[index]
                if collid_element.right>self.ball_rec.right and collid_element.left<self.ball_rec.left:
                    y_speed=-y_speed
                else:
                     x_speed=-x_speed
                del wall.brick_list[index]
                if len(wall.brick_list)<=10:
                    win_msg=pg.font.SysFont("calibri",60).render("you win!!",True,(255,0,0))
                    win_rect=win_msg.get_rect()
                    win_rect=win_rect.move(width/2-win_rect.right/2,300)
                    self.screen.blit(win_msg,win_rect)
                    pg.display.update()
                    while 1:
                        restart=False
                        for event in pg.event.get():
                            if event.type==pg.KEYDOWN:
                                if event.key==pg.K_ESCAPE:
                                    sys.exit()
                                if event.key!=pg.K_LEFT and event.key!=pg.K_RIGHT:
                                   restart=True
                                   wall.make_wall()

                        if restart:
                            live=self.max_live
                            x_speed=self.x_speed_init
                            y_speed=self.y_speed_init
                            self.score=0
                            self.screen.fill((0,0,0))
                            pg.display.flip()
                            self.ball_rec.center=self.x_ball,self.y_ball
                            self.bat_rec.center=(width/2,height-20)
                            break
                        
                        
                    
            if live==0:# if game over
                    msg=pg.font.SysFont("calibri",70).render("GAME OVER",True,(255,0,0))
                    msg_rect=msg.get_rect()
                    msg_rect=msg_rect.move(width/2-msg_rect.right/2,height/2)
                    self.screen.blit(msg,msg_rect)
                    pg.display.flip()
                    while 1:
                        restart=False
                        for event in pg.event.get():
                            if event.type==pg.KEYDOWN:
                                if event.key==pg.K_ESCAPE:
                                    sys.exit()
                                if event.key!=pg.K_LEFT and event.key!=pg.K_RIGHT:
                                   restart=True
                                   wall.make_wall()

                        if restart:
                            live=self.max_live
                            x_speed=self.x_speed_init
                            y_speed=self.y_speed_init
                            self.score=0
                            self.screen.fill((0,0,0))
                            pg.display.flip()
                            self.ball_rec.center=self.x_ball,self.y_ball

                            break
                    self.bat_rec.center=(width/2,height-20)    
                    print("restart")   
            score_msg=pg.font.SysFont("calibri",30).render(F"Score: {self.score}",True,(0,0,255))
            score_rec=score_msg.get_rect()
            score_rec=score_rec.move(2*width/3,0)
            self.ball_rec=self.ball_rec.move(x_speed,y_speed)
            self.bat_rec=self.bat_rec.move(bat_sp,0)
            if (self.bat_rec.left<=0 and bat_sp<0)or( self.bat_rec.right>=width and bat_sp>0):
                bat_sp=0
            for element in wall.brick_list:
                self.screen.blit(wall.brick,element)
            for i in range(live):
                pg.draw.circle(self.screen,(100,125,100),(20+i*15,15),5,0)
            self.screen.blit(self.ball,self.ball_rec)
            self.screen.blit(score_msg,score_rec)
            self.screen.blit(self.bat,self.bat_rec)
            pg.display.flip()

        sys.exit()             
            

class Wall():
    def __init__(self,screen):        
        self.brick=pg.image.load("brick.jpg").convert()
        self.screen=screen
    def make_wall(self):    
        brick_rec=self.brick.get_rect()
        self.brick_list=[]
        bricka=brick_rec.right-brick_rec.left
        brickb=brick_rec.bottom-brick_rec.top
        x=0
        y=60
        start=-bricka/2
        shift=bricka/2
        i=0
        row=1
        while row < 4:
            
            self.brick_list.append(self.brick.get_rect())
            self.brick_list[i]=self.brick_list[i].move(x,y)
            i+=1
            if x-bricka<=self.screen.width:
                x+=bricka
            else:
                row+=1
                x=start
                y+=brickb
                start+=shift
                shift=-shift
        
                

        
breakout=BreakOut()
breakout.game_loop()
