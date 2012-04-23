import  os, sys
import pygame
import screenset
import trial
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main(): 
    pygame.init()
    MainWindow = screenset.SoccerMain(width=1280,height=800)
    MainWindow.MainLoop()
    
if __name__ == "__main__": main()
