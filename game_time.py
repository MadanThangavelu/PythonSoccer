import pygame
from helpers import *
from ball import *
import math
import random
import time

class game_time(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.asec = time.strftime("%S")
        self.amin = int(time.strftime("%M"))
    
    def times(self):
        self.out = time.strftime("%M:%S")
        #setup font for stuffs to be written
        font = pygame.font.Font(None,36)
        self.text = font.render(self.out,1,(10,10,10))
        self.minutes = time.strftime("%M")
        self.value = time.strftime("%S")
        return self.value,self.minutes