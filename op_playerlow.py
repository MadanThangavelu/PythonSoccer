import pygame,os
from helpers import *
from ball import *
import random
from opponent import *


class op_player_low(Opponent):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('op_foot.gif', -1)
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 1
        self.y_dist = 1
        self.rect.left =45
        self.rect.top = 600
        self.direction = 1
        self.toggle = 1
        self.selected = 0
        self.plno = 0
        self.rand = 1
    

     
    def move(self,destination,d):
        if self.rect.left < 600 and destination[0] < 550 :
            if (self.rect.top < destination[1]) and (destination[1] > 500) and (destination[1] < 700) :
                self.rect.top +=1
            if (destination[0] < 300) and (self.rect.left < 300) and  (self.rect.left < destination[0]):
                self.rect.left +=1
            if (destination[0] > 299) and (self.rect.left > 55):
                self.rect.left -=1
            if(self.rect.left > destination[0]) and (self.rect.left > 55):
                self.rect.left -= 1
         
            if (self.rect.top > destination[1])and (destination[1] > 500) and (destination[1] <700) :
                self.rect.top -=1
            if (destination[0] < 300) and (self.rect.left < 300) and  (self.rect.left < destination[0]):
                self.rect.left +=1
            if ((destination[0] > 299) and (self.rect.left > 55)) :
                self.rect.left -=1
            if(self.rect.left > destination[0]) and (self.rect.left > 55):
                self.rect.left -= 1
            self.toggle = self.toggle ^ 1
            self.ai();
            
            
        else:
            if self.toggle == 1:
                self.rect.left -= 2
            if self.toggle == 0:
                self.rect.left += 2
            self.toggle = self.toggle ^ 1
            self.ai();
      
        
                
            