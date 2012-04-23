import pygame
from helpers import *
from ball import *

class refree(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('refree.bmp', -1)
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 0.9
        self.y_dist = 0.9
        self.direction = 1
        self.toggle = 1
        self.selected = 0
        self.plno = 0
        
    def track(self,ball):
        if ball[1] < 400:
            self.rect.left = ball[0]  +  150
            self.rect.top = 40
        if ball[1] > 400:
            self.rect.left = ball[0]  +  150
            self.rect.top = 700
    
        
