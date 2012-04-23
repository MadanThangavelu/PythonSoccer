import pygame
from helpers import *
from ball import *
import math
import random

class goal_comp(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('goal_comp.bmp', -1)
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 1
        self.y_dist = 1
        self.rect.top = 350
        self.rect.left = 70
        self.direction = 1
        self.toggle = 1
        self.selected = 0
        self.plno = 0
        self.rand = 1
    
    def watch(self,destination):
        if (self.rect.top < destination[1]) and (destination[1] > 200) and (destination[1] < 550) :
                self.rect.top += random.randrange(1,3,1)
        if (self.rect.top > destination[1])and (destination[1] > 200) and (destination[1] <550) :
                self.rect.top -= random.randrange(1,3,1)
    