import pygame
from snake import *
from helpers import *


class low_player(Snake):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('foot.gif', -1)
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 2
        self.y_dist = 2
        self.toggle = 2
        self.selected = 0
        self.plno = 0
        self.rect.top = 500
        self.rect.left = 400
    
    def sync(self,player1,direction):
        self.tillx = abs(self.rect.left  - player1[0])
        for self.i in range (1,self.tillx - 100):
            if player1[0] < self.rect.left - 150:
                self.rect.left -= 1
                
            elif player1[0] > self.rect.left + 150:
                self.rect.left += 1
                
                
        self.tilly = abs(self.rect.top - player1[1])
        """ ADJUST Y DIRECTION RELATIVE MOVEMENT """
       
        
        if self.tilly > 180 and self.rect.top > player1[1] and self.rect.top + 1 > 0 and self.rect.top + 1 > 430:
            self.rect.top -= 1
        else:
            if(self.rect.top + 1 < 550) and self.rect.top < 510:
                self.rect.top += 1
        
        