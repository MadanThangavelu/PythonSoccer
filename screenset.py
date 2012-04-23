"""""""""""""""""""""""""""""""""
Author: Madan Kumar Thangavelu  
Language: Python 2.4.1 + Pygame
Email : madankumar.t@gmail.com 
"""""""""""""""""""""""""""""""""

import pygame,os
from pygame.locals import * 
import os
from snake import *
from top_player import *
from low_player import *
from middle_player import *
from ball import *
from arena import *
from Tkinter import *
from helpers import *
from op_playertop import *
from op_playerlow import *
from refree import *
from goalkeep import *
from goalkeeper_player import *
from cgoal import *
from pgoal import *
from game_engine import *
import random
import time
from game_time import *
from menu import *
from gameover import *
from trial import *

#setup font for stuffs to be written
direction = 1


class SoccerMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self,width=1024,height=768):
        """intitializing variables"""
        self.running =1
        self.value = 0
        self.pscore =0
        self.cscore = 0
        self.control = 0
        self.toggle = 1 # To swirch between the players
        self.indicator = 0
        self.decide = 2
        
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        self.greet = 1
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
        self.crowd = self.load_sound("cheer.wav");
        
        self.refwhis = self.load_sound("start.wav");
        self.high = self.load_sound("high.wav");
           
        """ IMPORT GREET """
        self.greet = menu()     
        self.over = game_over() 
        self.clock = game_time()
            
    def start_game(self):
        """SET INITIAL POSITION OF PLAYERS AND BALL """
        self.ball.rect.top = 410
        self.ball.rect.left = 500
        self.player1.rect.left = 550
        self.player1.rect.top = 350
        self.player2.rect.left = 600
        self.player3.rect.left = 600
        self.op1.rect.left = 350
        self.op2.rect.left = 250
        self.op2.rect.top = 350
        self.op3.rect.left = 250
        self.op3.rect.top = 500
        self.ref.rect.top = 390
        self.ref.rect.left = 500
        self.neram = self.font1.render(" ",1,(255,255,255))
        """DISPLAY THE FIELD """
        self.god_display();
        self.crowd.stop();
        """ HOLD SCENE FOR 2 SECONDS """
        time.sleep(2)
        """REFREE WHSTLE """
        self.refwhis.play();
        
        
        
    
    def load_sound(self,name):
        """ FUNCTION TO LOAD REQQIRED WAV FILE """
        class NoneSound:
            def play(self): pass
        if not pygame.mixer or not pygame.mixer.get_init():
            return NoneSound()
        folder = os.path.abspath(__file__).split(os.sep)[:-1]
        fullname = folder + ['data', 'sound', name]
        fullname1 = os.sep.join(os.path.join(fullname))
        self.fullname = fullname1
        try:
            sound = pygame.mixer.Sound(self.fullname)
        except pygame.error, message:
            print 'Cannot load sound:', self.fullname
            raise SystemExit, message
        return sound

    def god_display(self):
        """ MAIN DISPLAY ELEMENT OF ALL THE SPRITES """
        self.arena_sprite.draw(self.screen)
        self.ball_sprite.draw(self.screen)
        self.op_sprite1.draw(self.screen)
        self.op_sprite2.draw(self.screen)
        self.op_sprite3.draw(self.screen)
        self.player_sprite1.draw(self.screen);
        self.player_sprite2.draw(self.screen);
        self.player_sprite3.draw(self.screen);
        self.refree_sprite.draw(self.screen);
        self.goal_sprite.draw(self.screen);
        self.goalc_sprite.draw(self.screen);
        self.pgoal_sprite.draw(self.screen);
        self.goalp_sprite.draw(self.screen);
        self.screen.blit(self.neram,(50,5));
        self.screen.blit(self.scores1,(450,5))
        
        self.screen.blit(self.text1,(self.player1.rect.left + 20  , self.player1.rect.top - 25 ))
        self.screen.blit(self.text2,(self.player2.rect.left + 20 , self.player2.rect.top - 25))
        self.screen.blit(self.text3,(self.player3.rect.left + 20 , self.player3.rect.top  - 25))
        pygame.display.update()
    
    """  MANAGE THE PASSSING AND SIAPLY """                
    def same_pass1(self,destination):
        self.once = 1
        """ TO PASS TO A PLAYER ABOVE CURRENT PLAYER"""
        while self.ball.rect.top < destination[1] + 19:
            if self.once == 1:
                if (self.op1.rect.colliderect(self.ball.rect) == 0) and (self.op2.rect.colliderect(self.ball.rect) == 0) and (self.op3.rect.colliderect(self.ball.rect) == 0):
                    self.ball.rect.top +=3
                    if self.ball.rect.left <destination[0]:
                        self.ball.rect.left +=2
                    if self.ball.rect.left > destination[0]:
                        self.ball.rect.left -=2
                    self.god_display();
                else:
                    self.ball.rect.left +=50
                    return
        """ TO PASS TO A PLAYER BELOW CURRENT PLAYER """
        while self.ball.rect.top > destination[1] + 19:
            if self.once == 1:
                if (self.op1.rect.colliderect(self.ball.rect) == 0) and (self.op2.rect.colliderect(self.ball.rect) == 0) and (self.op3.rect.colliderect(self.ball.rect) == 0):
                    self.ball.rect.top -=3
                    if self.ball.rect.left <destination[0]:
                        self.ball.rect.left +=2
                    if self.ball.rect.left > destination[0]:
                        self.ball.rect.left -=2
                    self.god_display();
            
                else:
                    self.ball.rect.left +=50
                    return
    
    """  DECIDE IF ITS A VALID PASS AND CALL PASS FUNCTION TO DESTINATION PLAYER """
    def god_pass(self,destination):
        self.midx = self.ball.rect[0] + self.ball.rect[2]/2
        self.midy = self.ball.rect[1] + self.ball.rect[3]/2
        if (self.midx > self.player1.rect.left - 20) and (self.midx < self.player1.rect.left + self.player1.rect.width + 20) and (self.midy > self.player1.rect.top) and (self.midy < self.player1.rect.top + self.player1.rect.height + 20):
            self.indicator = 1
            self.same_pass1(destination.rect)
        elif (self.midx > self.player2.rect.left - 20) and (self.midx < self.player2.rect.left + self.player2.rect.width + 20) and (self.midy > self.player2.rect.top) and (self.midy < self.player2.rect.top + self.player2.rect.height + 20):
            self.indicator = 1
            self.same_pass1(destination.rect)
        elif (self.midx > self.player3.rect.left - 20) and (self.midx < self.player3.rect.left + self.player3.rect.width + 20) and (self.midy > self.player3.rect.top) and (self.midy < self.player3.rect.top + self.player3.rect.height + 20):
            self.indicator = 1
            self.same_pass1(destination.rect)            
        else:
            self.conf = 0
            
        
        
              
        
    """ CREATE AN INSTANCE OF THE BALL """
    def Loadball(self):
        self.ball = Ball()
        self.ball_sprite = pygame.sprite.RenderPlain((self.ball))
        
    """ CREATE INSTANCES OF MANUAL PLAYERS """   
    def loadplayer(self):
        self.fordir = Snake()
        self.player1 = middle_player()
        self.player_sprite1 = pygame.sprite.RenderPlain((self.player1))
        self.player2 = low_player()
        self.player_sprite2 = pygame.sprite.RenderPlain((self.player2))
        self.player3 = top_player()
        self.player_sprite3 = pygame.sprite.RenderPlain((self.player3))
    
    """ CREATE INSTANCES OF OPPONENTS AND GOAL AND REFEREE """
    def opponents(self):
        self.op1 = Opponent()
        self.op_sprite1 = pygame.sprite.RenderPlain((self.op1))
        self.op2 = op_player_top()
        self.op_sprite2 = pygame.sprite.RenderPlain((self.op2))
        self.op3 = op_player_low()
        self.op_sprite3 = pygame.sprite.RenderPlain((self.op3))    
        self.ref = refree()
        self.refree_sprite = pygame.sprite.RenderPlain((self.ref))
        self.goal_c = goal_comp()
        self.goalc_sprite = pygame.sprite.RenderPlain((self.goal_c))
        self.goal_p = goal_player()
        self.goalp_sprite = pygame.sprite.RenderPlain((self.goal_p))
        self.goal = goal()
        self.goal_sprite = pygame.sprite.RenderPlain((self.goal))
        self.pgoal = pgoal()
        self.pgoal_sprite = pygame.sprite.RenderPlain((self.pgoal))
        self.win = game_engine()
        
     
    """ INSTANCE OF THE BACKGROUND ARENA """   
    def loadarena(self):
        self.arena = arena()
        self.arena_sprite = pygame.sprite.RenderPlain((self.arena))
      
    
    """ MAIN GAME LOOP """
    def MainLoop(self):       
        self.font1 = pygame.font.Font(None,72)  
        self.scores = "C :" +  str(self.cscore) + "    "  + " P :"+  str(self.pscore)
        self.scores1 = self.font1.render(self.scores,1,(0,0,0))  
        """ INITIAL SOUND OF CROWD """
        self.high.play();
        """ FONT FOR CLOCK """
        
        
        """ FONT FOR PLAYER NUMBER """
        font = pygame.font.Font(None,22)
        self.text1 = font.render("1",1,(255,255,255))
        self.text2 = font.render("2",1,(0,0,0))
        self.text3 = font.render("3",1,(0,0,0))
                
        """ SHOW MENU AND GREETER """
        self.running = self.greet.greetr();

        
        """ LOAD OBJECTS INTO THE GAME """
        if self.running == 1:
            self.opponents();
            self.Loadball();
            self.loadarena();        
            self.loadplayer();
            self.start_game();
       
       
        """ INTITIALIZE STARTING TIME OF THE GAME """
        self.gsec,self.gmin = self.clock.times()
        self.gmin = int(self.gmin)
        self.gsec = int(self.gsec)
        self.gmin += 4   # SET THE GAME TIME TO 2 MINUTES
        self.gsec = 59  
        
        """ START THE GAME LOOP """
        while self.running:
            """ UPDATE SCORE BOARD """
            self.scores = "Scores |  " + "C :  " +  str(self.cscore) + "    "  + " P :  "+  str(self.pscore)
            self.scores1 = self.font1.render(self.scores,1,(255,255,255))
            """ KEEP THE CROWD SOUND AT BACKGROUND """
            self.crowd.play();
            
            pygame.event.pump()
            self.pressed = pygame.key.get_pressed()           
            
            """ SET WHICH PLAYER IS CONTROl """
            if self.pressed[49] == 1:
                    self.toggle = 1                    
                    self.player1.selected = 1
                    self.player2.selected = 0
                    self.player3.selected = 0
                    self.player1.x_dist = 2
                    self.player1.y_dist = 2
                    self.player2.x_dist = 2
                    self.player2.y_dist = 2
                    self.player3.x_dist = 2
                    self.player3.y_dist = 2
                    self.text1 = font.render("1",1,(255,255,255))
                    self.text2 = font.render("2",1,(0,0,0))
                    self.text3 = font.render("3",1,(0,0,0))
                    self.god_pass(self.player1);
                    
            if self.pressed[50] == 1:
                    self.toggle = 2
                    self.player1.selected = 0
                    self.player2.selected = 1
                    self.player3.selected = 0
                    self.player1.x_dist = 1
                    self.player1.y_dist = 1
                    self.player2.x_dist = 2
                    self.player2.y_dist = 2
                    self.player3.x_dist = 3
                    self.player3.y_dist = 3
                    self.text2 = font.render("2",1,(255,255,255))
                    self.text1 = font.render("1",1,(0,0,0))
                    self.text3 = font.render("3",1,(0,0,0))    
                    self.god_pass(self.player2);
                    
            if self.pressed[51] == 1:
                    self.toggle = 3
                    self.player1.selected = 0
                    self.player2.selected = 0
                    self.player3.selected = 1
                    self.player1.x_dist = 2
                    self.player1.y_dist = 2
                    self.player2.x_dist = 1
                    self.player2.y_dist = 1
                    self.player3.x_dist = 2
                    self.player3.y_dist = 2
                    self.text3 = font.render("3",1,(255,255,255))
                    self.text2 = font.render("2",1,(0,0,0))
                    self.text1 = font.render("1",1,(0,0,0))
                    self.god_pass(self.player3);
                
            
           
            """MOVE APPROPRIATE  PLAYER"""
            if(self.toggle == 1):
                self.player3.sync(self.player1.rect,self.fordir.direction)
                self.player2.sync(self.player1.rect,self.fordir.direction)              
                self.screen = self.player1.premove(self.pressed,self.screen)
                
            if(self.toggle == 2):
                self.player3.sync(self.player2.rect,self.fordir.direction)
                self.player1.sync(self.player2.rect,self.fordir.direction)
                self.screen = self.player2.premove(self.pressed,self.screen)
            if(self.toggle == 3):
                self.player1.sync(self.player3.rect,self.fordir.direction)
                self.player2.sync(self.player3.rect,self.fordir.direction)
                self.screen = self.player3.premove(self.pressed,self.screen)
            
            """ ON COLLISION OF MANUAL PLAYER WITH THE BALL """
            if self.player1.rect.colliderect(self.ball.rect) == 1 :
                self.result = self.ball.hit(self.player1.rect,self.ball.rect,self.pressed)
                if (self.result[4] == 1):
                    self.ball.rect.left -= 50
                if  self.result[4] == -1:
                    self.ball.rect.left += 50
                self.player1.move(self.result[0]) 
                for self.i in (1,4):
                    self.ball.kick(self.result[1],119,self.result[2],self.result[3])
            
                

            if self.player2.rect.colliderect(self.ball.rect) == 1 :
                self.result = self.ball.hit(self.player2.rect,self.ball.rect,self.pressed)
                if (self.result[4] == 1):
                    self.ball.rect.left -= 50
                if  self.result[4] == -1:
                    self.ball.rect.left += 50
                self.player2.move(self.result[0])  
                self.ball.kick(self.result[1],119,self.result[2],self.result[3]) 
            
                         
            
            if self.player3.rect.colliderect(self.ball.rect) == 1 :
                self.result = self.ball.hit(self.player3.rect,self.ball.rect,self.pressed)
                if (self.result[4] == 1):
                    self.ball.rect.left -= 50
                if  self.result[4] == -1:
                    self.ball.rect.left += 50
                self.player3.move(self.result[0])
                self.ball.kick(self.result[1],119,self.result[2],self.result[3])
            
                
            """ OPPONENT COLLISION WITH THE BALL """
            """ MAIN PLAYER OF OPPONENT """
            if self.op1.rect.colliderect(self.ball.rect) == 1 :
                if self.ball.rect.left + 50 < 1000:
                    self.ball.rect.left +=50
                    self.control = 1
                else:
                    self.ball.rect.left -= 15
                    self.control = 1
               
            
            if self.op2.rect.colliderect(self.ball.rect) == 1 :
                self.ball.rect.left +=50
                self.control = 1
                
                
            if self.op3.rect.colliderect(self.ball.rect) == 1 :
                self.ball.rect.left +=50
                self.control = 1
                
            
            """ COLLISION OF AUTOMATIC COMPUTER GOALKEEPER WITH BALL """
            if self.goal_c.rect.colliderect(self.ball.rect) == 1 :
                self.ball.rect.left +=250
                
            """ COLLISION OF PLAYER SIDE GOALKEEPER WITH BALL """
            if self.goal_p.rect.colliderect(self.ball.rect) == 1 :
                self.ball.rect.left -=150
                self.ball.rect.top -= 5


            """ DETECT GOAL  BY MANUAL PLAYER"""
            if self.goal.rect.colliderect(self.ball.rect) == 1 :
                #print "THERE WAS A GOAL"
                self.crowd.stop()
                self.refwhis.play();
                self.screen.fill((0,0,0))
                self.pscore += 1
                #self.start_game();
                self.god_display();
                pygame.display.update();
                time.sleep(2)
                self.start_game();
              
            
            """ DETECT GOAL BY COMPUTER """
            if self.pgoal.rect.colliderect(self.ball.rect) == 1 :
                #print "BAD GOAL"
                self.crowd.stop()
                self.refwhis.play();
                self.cscore += 1
               
                self.god_display();
                pygame.display.update();
                time.sleep(2)
                self.start_game();
         
            
           
            """ CHANGE THE DIFFICULTY LEVELS """
            
            if  self.ball.rect.left < 375:
                self.op1.move(self.ball.rect,1);
                self.op2.move(self.ball.rect,1);
                self.op3.move(self.ball.rect,1);
            
            self.win.analyze(self.player1,self.op2,self.ball,self.op1)
            
            """ MOVE THE OTHER PLAYERS """
            
            if self.win.attack == 1:
                #print "attack"
                if self.op2.rect.left < 600:
                    self.op2.rect.left += 2
                    self.op3.rect.left += 1
            if self.win.attack == 0:
                if self.op2.rect.left > 200:
                    self.op2.rect.left -= 5
                    self.op3.rect.left -= 5
                    #print "deffence"
            
            """ MAKE REFREE TRACK ALONG WITH THE BALL """
            self.ref.track(self.ball.rect);
            
            
            """ BOTH GOALKEEPRES TRACK THE BALL'S Y MOVEMENTS """
            self.goal_c.watch(self.ball.rect);
            self.goal_p.watch(self.ball.rect);
            
            """ THE GAME TIMING CLOCK """
            self.value,self.minutes = self.clock.times()
            self.ori = self.value
            self.minutes = int(self.minutes)
            self.value = int(self.value)
            self.minutes = self.gmin - self.minutes
            self.value = self.gsec - self.value
            self.dis = "Time |  " + str(self.minutes) + ":" + str(self.value)
            self.neram = self.font1.render(self.dis,1,(255,255,255))
            
            """ QUIT ON CLOCK RUN OUT """
            if ((int(self.minutes) == 0) and (int(self.value) == 0)) or (self.minutes < 0):
                self.decide = self.over.gover(self.pscore,self.cscore);
                self.over.restart = 2
            
            if self.decide == 1:
                self.pscore = 0
                self.cscore = 0
                self.gsec,self.gmin = self.clock.times()
                self.gmin = int(self.gmin)
                self.gsec = int(self.gsec)
                self.gmin += 4   # SET THE GAME TIME TO 2 MINUTES
                self.gsec = 59
                self.start_game();
                time.sleep(2)
                self.decide = 2
            
            if self.decide == 0:
                self.running = 0
            
            
            
            """ MAKE THE BALL MOVE AROUND DURING STILL SITUATIONS """
            self.rand = random.randrange(1,40,1)
            if (self.rand == 3) or self.rand == 16 or self.rand ==30 or self.rand == 40:
                self.ball.rect.left -= 1
            if (self.rand == 7) or self.rand == 28 or self.rand == 25 or self.rand == 36:
                self.ball.rect.left += 1
            """ DISPLAY THE CHANGE IN BALL POSITIONS """
            self.god_display();
            
            """ QUIT THE GAME ON ESC CHARACTER """
            if self.pressed[27] == 1:
                 self.decide = self.over.gover(self.pscore,self.cscore);
                

            self.event = pygame.event.poll()
            if self.event.type == pygame.QUIT:
                 self.decide = self.over.gover(self.pscore,self.cscore);

                   
            
         
                    
                    
                    
