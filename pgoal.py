import pygame
from helpers import *
from ball import *
import math
import random

class pgoal(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('pgoal.bmp')
        self.image = self.image.convert()
        self.pellets = 0
        self.x_dist = 1
        self.y_dist = 1
        self.rect.top = 268
        self.rect.left = 940
        self.direction = 1
        self.toggle = 1
        self.selected = 0
        self.plno = 0
        self.rand = 1
    