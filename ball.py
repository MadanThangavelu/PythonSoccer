import pygame
from helpers import *
from snake import *
import time
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.xmove = 5
        self.ymove = 5
        self.image, self.rect = load_image('footbol.png', -1)
        self.image = self.image.convert()
        self.rect.left = 300
        self.rect.top = 400

    def inertia(self):
        self.rand = random.randrange(1,2,1)
        if (self.rand == 1):
            self.rect.left += 1
        if (self.rand == 2):
            self.ract.left -= 1
        
    def hit(self,player,ball,key):
        self.pressed = key
        self.pack = [275,6,0,0,0]
        #right
        if self.pressed[275] == 1 :
            self.pack = [275,6,1,0,0]
        #Left
        if self.pressed[276] == 1 :
            self.pack = [276,6,-1,0,0]
        #down
        if self.pressed[274] == 1 :
                if(player[0] < ball [0]):
                    self.pack = [274,5,1,1,0]
                if(player[0] > ball[0]):
                    self.pack = [274,5,-1,1,0]
        #up
        if self.pressed[273] == 1 :
                if(player[0] < ball [0]):
                    self.pack = [273,5,1,-1,0]
                if(player[0] > ball[0]):
                    self.pack = [273,5,-1,-1,0]
        if self.pressed[32] == 1 :
                if(player[0] < ball [0]):
                    self.pack = [0,0,0,0,1]
                if(player[0] > ball[0]):
                    self.pack = [0,0,0,0,-1]
                            
        return self.pack

    def kick(self,kickby,side,kikx,kiky):
        self.kickx = kikx
        self.kicky = kiky
        self.kickby = kickby

        for self.i in range (1,self.kickby):
            """ MOVE RIGHT PLAIN """
            if((self.kickx == 1) and (self.kicky == 0)):
                if((self.rect.left + (4 * self.kickx)) < 1000):
                    for self.i in range (1,2):
                        self.rect.left += self.kickx
                        pygame.display.update()
                else:
                    self.rect.move_ip(-self.kickx * 70 ,self.kicky)
            
            """ MOVE TOP """        
            if((self.kickx == 1) and (self.kicky == -1)) or ((self.kickx == -1) and (self.kicky == -1)):      
                if ((self.rect.top + (4 * self.kicky)) > 50) and ((self.rect.left + (4 * self.kickx)) > 30) and ((self.rect.left + (4 * self.kickx)) < 1000):
                    for self.i in range (1,3):
                        self.rect.left += self.kickx
                        self.rect.top += self.kicky
                else:
                    self.rect.move_ip(self.kickx ,-self.kicky * 35)
                    
            """ MOVE LEFT """
            if((self.kickx == -1) and (self.kicky == 0)):
                if((self.rect.left + (4 * self.kickx)) > 30):
                    for self.i in range (1,2):
                        self.rect.left += self.kickx
                        pygame.display.update()
                else:
                    self.rect.move_ip(-self.kickx * 70 ,self.kicky)
            
            """ MOVE DOWN """
            if((self.kickx == 1) and (self.kicky == 1)) or ((self.kickx == -1) and (self.kicky == 1)):      
                if ((self.rect.top + (4 * self.kicky)) < 750) and ((self.rect.left + (4 * self.kickx)) > 30) and ((self.rect.left + (4 * self.kickx)) < 1000):
                    for self.i in range (1,3):
                        self.rect.left += self.kickx
                        self.rect.top += self.kicky
                    
                else:
                    self.rect.move_ip(-self.kickx  ,self.kicky)
                    

            
       
        