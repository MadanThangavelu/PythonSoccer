#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *

def load_sound1(name):
        class NoneSound:
            def play(self): pass
        if not pygame.mixer or not pygame.mixer.get_init():
            return NoneSound()
        folder = os.path.abspath(__file__).split(os.sep)[:-1]
        fullname = folder + ['data', 'sound']
        fullname1 = os.sep.join(os.path.join(fullname))
        try:
            sound = pygame.mixer.Sound(fullname1)
        except pygame.error, message:
            print 'Cannot load sound:',fullname1
            raise SystemExit, message
        return sound

def load_image(name, colorkey=None):
    folder = os.path.abspath(__file__).split(os.sep)[:-1]
    fullname = folder + ['data', 'images', name]
    fullname = os.sep.join(os.path.join(fullname))
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()



     

    
    
    