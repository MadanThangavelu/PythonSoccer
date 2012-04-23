import pygame
from trial import *
from helpers import *

class menu(pygame.sprite.Sprite):
    def __init__(self):
        self.greet = 1
        self.count = 1
        self.crowd = load_sound1("cheer.wav");
        self.refwhis = load_sound1("start.wav");
        self.high = load_sound1("high.wav");
        self.beep = load_sound1("BEEP1B.WAV");
        self.screen = pygame.display.set_mode((1024, 768),pygame.FULLSCREEN)
   
    def greetr(self):
        self.wel, self.welrec = load_image('options.jpg')
        self.wel = self.wel.convert()
        self.button1 = Rect(50, 400, 150, 50)
        self.button2 = Rect(50, 520, 150, 50)
        self.button3 = Rect(50, 460, 150, 50)
        pygame.draw.rect(
                             self.screen,
                             (0,0,0),
                             self.button1,
            )
        pygame.draw.rect(
                             self.screen,
                             (0,0,0),
                             self.button2,
            )
        pygame.draw.rect(
                             self.screen,
                             (0,0,0),
                             self.button3,
            )
        
        self.screen.blit(self.wel,(0,0))
        font1 = pygame.font.Font(None,55)
        self.menu = font1.render("Menu",1,(255,255,255))
        
        
        while self.greet:
            self.crowd.set_volume(0.4)
            self.crowd.play();
            font1 = pygame.font.Font(None,40)         
            self.gret = font1.render("Quick Start",1,(255,255,255))
            self.out = font1.render("Quit",1,(255,255,255))
            self.event = pygame.event.poll()
            if self.event.type == KEYDOWN:
                    if self.event.key == K_ESCAPE:
                        self.greet = 0
            
            if self.event.type == MOUSEBUTTONDOWN:
                if (self.button1.collidepoint(pygame.mouse.get_pos())):
                    self.greet = 0
                    self.running = 1
                    return self.running
                    return self.greet
                if (self.button2.collidepoint(pygame.mouse.get_pos())):
                    self.greet = 0
                    self.running = 0
                    return self.running
                if (self.button3.collidepoint(pygame.mouse.get_pos())):
                    self.trys = SoccerTrial()
                    self.trys.MainLoop();
                
            if (self.button1.collidepoint(pygame.mouse.get_pos())):
                    self.gret = font1.render("Play Now",1,(0,0,0))
                    self.screen.blit(self.gret,(50,400))
                    self.gret = font1.render("Play Now",1,(255,255,255))
                    self.screen.blit(self.gret,(50,400))
                    self.count = 2
                        
                    
            else:
                    self.gret = font1.render("Play Now",1,(255,255,255))
                    self.screen.blit(self.gret,(50,400))
                    self.gret = font1.render("Play Now",1,(0,0,0))
                    self.screen.blit(self.gret,(50,400))
                    self.count = 1 
                   
            
            if (self.button2.collidepoint(pygame.mouse.get_pos())):
                    self.out = font1.render("Quit",1,(0,0,0))
                    self.screen.blit(self.out,(50,520))
                    self.out = font1.render("Quit",1,(255,255,255))
                    self.screen.blit(self.out,(50,520))
                    self.count = 2
            else:
                    self.out = font1.render("Quit",1,(255,255,255))
                    self.screen.blit(self.out,(50,520))
                    self.out = font1.render("Quit",1,(0,0,0))
                    self.screen.blit(self.out,(50,520))
                    self.count = 1
                    
            if (self.button3.collidepoint(pygame.mouse.get_pos())):
                    self.trials = font1.render("Trial",1,(0,0,0))
                    self.screen.blit(self.trials,(50,460))
                    self.trials = font1.render("Trial",1,(255,255,255))
                    self.screen.blit(self.trials,(50,460))
               
            else:
                    self.trials = font1.render("Trial",1,(255,255,255))
                    self.screen.blit(self.trials,(50,460))
                    self.trials = font1.render("Trial",1,(0,0,0))
                    self.screen.blit(self.trials,(50,460))
                    self.count = 1
                    
            #self.trys = SoccerTrial()
            #self.trys.MainLoop();
            self.screen.blit(self.wel,(0,0))
            self.screen.blit(self.gret,(50,400))
            self.screen.blit(self.out,(50,520))
            self.screen.blit(self.trials,(50,460))
            self.screen.blit(self.menu,(50,300))
            pygame.display.update();
        