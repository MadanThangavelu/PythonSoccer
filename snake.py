import pygame
from helpers import *
from ball import *

class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('foot.gif', -1)
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 0.9
        self.y_dist = 0.9
        self.direction = 1
        self.toggle = 1
        self.selected = 0
        self.plno = 0
    
    def premove(self,find,screen):
        self.screen1 = screen
        if find[275] == 1 : # RIGHT
            screen = self.move(275)  
            self.image, self.rect_not = load_image('run_foot_right.gif', -1)         
        if find[276] == 1: # LEFT
            screen =self.move(276)
            self.image, self.rect_not = load_image('run_foot.gif', -1)
                    
        if find[274] == 1: # DOWN
            screen = self.move(274)
            self.image, self.rectno = load_image('foot.gif', -1)
        if find[273] == 1: # UP
            screen =  self.move(273)
            self.image, self.rectno = load_image('foot.gif', -1)
     
        return self.screen1
       
    def move(self,key):
        
        self.xMove = 0;
        self.yMove = 0;
        #if (key == K_RIGHT):
        #    self.xMove = self.x_dist
        #if (key == K_LEFT):
        #    self.xMove = -self.x_dist
        #if (key == K_UP):
        #    self.yMove = -self.y_dist
        #if (key == K_DOWN):
        #    self.yMove = self.y_dist
        
        #right
        if (key == 275):
            if (self.rect.right + self.y_dist < 1010):
                self.xMove = self.x_dist
                self.image, self.rect_notneeded = load_image('footr.gif', -1)
                self.direction = 0
          
            #self.image = pygame.image.load('data/images/footr.gif').convert()       

        #left
        if (key == 276):
            if (self.rect.left + self.y_dist > 0):
                self.xMove = -self.x_dist
                self.image, self.rect_notneeded = load_image('foot.gif', -1)
                self.direction = 1
                
                #self.rect.left = self.rect.left - self.x_dist
                
            #self.image = pygame.image.load('data/images/foot.gif').convert() 
              
        if (key == 274):
            #down
            if(self.rect.bottom + self.y_dist < 750):
                self.yMove = self.y_dist
                # up
        if (key == 273):
            if(self.rect.top + self.y_dist > 35):
                self.yMove = -self.y_dist
        
       
        #self.rect.left += self.xMove
        #print self.yMove
        #self.rect.top += self.yMove
        
        self.rect.move_ip(self.xMove,self.yMove);
        #return self.screen
        
                
            