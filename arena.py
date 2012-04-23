import pygame
from helpers import *
from ball import *

class arena(pygame.sprite.Sprite):
    
    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('arena2.jpg')
        self.ban , self.brect = load_image('top.jpg')
        if rect != None:
            self.rect = rect