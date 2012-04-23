import pygame
from helpers import *
from ball import *
import math
import random


class Opponent(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('op_foot.gif', -1)
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 1
        self.y_dist = 1
        self.rect.top = 350
        self.rect.left = 250
        self.direction = 1
        self.toggle = 1
        self.selected = 0
        self.plno = 0
        self.rand = 1
        self.attack = 1
    
 
    def ai(self):
        self.rand = random.randrange(1,8,1)
        #if self.rect.left < 250 and self.rect.top > 300 and self.rect.top <450 and self.rect.left > 55:
        if 1 == 1:
            if self.rand == 4:
                    self.rect.left -= 1
            if self.rand == 5:
                    self.rect.left += 1
            if self.rand == 3:
                    self.rect.top -= 1
            if self.rand == 7:
                    self.rect.top += 1
            if self.rand == 1:
                    self.rect.left -=1
                    self.rect.top += 1
            if self.rand == 6:
                    self.rect.left += 1
                    self.rect.top  += 1
            if self.rand == 2:
                    self.rect.left += 1
                    self.rect.top -= 1

        
    def move(self,destination,d):
        if (self.rect.left < 1000) and destination[0] < 900 :
            if (self.rect.top < destination[1]) and (destination[1] > 230) and (destination[1] < 500) :
                self.rect.top +=1
            if (destination[0] < 350) and (self.rect.left < 400) and  (self.rect.left < destination[0]):
                self.rect.left +=1
            if (destination[0] > 299) and (self.rect.left > 200):
                self.rect.left -=1
            if(self.rect.left > destination[0]) and (self.rect.left > 55):
                self.rect.left -=1
            if (self.rect.top > destination[1])and (destination[1] > 230) and (destination[1] <500) :
                self.rect.top -=1
            if (destination[0] < 350) and (self.rect.left < 400) and  (self.rect.left < destination[0]):
                self.rect.left +=1
            if ((destination[0] > 299) and (self.rect.left > 200)) :
                self.rect.left -=1
            if(self.rect.left > destination[0]) and (self.rect.left > 155):
                self.rect.left -=1
            self.ai();          
            
        else:
            self.rand = random.randrange(1,8,1)
            if self.rect.left < 250 and self.rect.top > 250 and self.rect.top <450:
                self.ai();
            else:
                if (self.rect.left > 45) and (self.rect.top < 450) and self.rect.top > 250:
                    self.rect.left -= 10
                    self.rect.top -= 10
            
        
      
        
                
            
