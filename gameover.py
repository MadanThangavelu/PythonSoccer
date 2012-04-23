import pygame
from screenset import *
from helpers import *

class game_over(pygame.sprite.Sprite):
    def __init__(self):
        self.greet = 1
        self.crowd = load_sound1("cheer.wav");
        self.refwhis = load_sound1("start.wav");
        self.high = load_sound1("high.wav");
        self.screen = pygame.display.set_mode((1024, 768),pygame.FULLSCREEN)
   
    def gover(self,player,computer):
        self.result = " "
        self.wel, self.welrec = load_image('options.jpg')
        self.wel = self.wel.convert()
        self.button1 = Rect(250, 300, 150, 50)
        self.button2 = Rect(250, 360, 150, 50)
 
        self.restart = 2
        """ DECIDE WINNER """
        if player > computer:
            self.result = "YOU WON !! "
        elif computer > player:
            self.result = "YOU LOST !!"
        else:
            self.result = " THERE WAS A TIE "
        
        self.fscore = "Scores : C - " + str(computer) + " P - " + str(player)
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
     
        self.screen.blit(self.wel,(0,0))
        font1 = pygame.font.Font(None,55)
        self.menu = font1.render("Menu",1,(0,0,0))
        self.res = font1.render(self.result,1,(255,255,255))
        self.fsco = font1.render(self.fscore,1,(255,255,255))
        while self.greet:
            font1 = pygame.font.Font(None,40)         
            self.gret = font1.render("Play Again",1,(0,0,0))
            self.out = font1.render("Quit",1,(0,0,0))
            self.cont = font1.render("Continue",1,(0,0,0))
            self.event = pygame.event.poll()
            if self.event.type == KEYDOWN:
                    if self.event.key == K_ESCAPE:
                        self.greet = 0
            
            if self.event.type == MOUSEBUTTONDOWN:
                if (self.button1.collidepoint(pygame.mouse.get_pos())):
                    self.restart = 1
                    return self.restart
                    
                if (self.button2.collidepoint(pygame.mouse.get_pos())):
                    self.restart = 0
                    return self.restart
                
                if (self.button3.collidepoint(pygame.mouse.get_pos())):
                    self.restart = 3
                    return self.restart
            
            if (self.button1.collidepoint(pygame.mouse.get_pos())):
                    self.gret = font1.render("Play Again",1,(0,0,0))
                    self.screen.blit(self.gret,(250,300))
                    self.gret = font1.render("Play Again",1,(255,255,255))
                    self.screen.blit(self.gret,(250,300))
                    
            else:
                    self.gret = font1.render("Play Again",1,(255,255,255))
                    self.screen.blit(self.gret,(250,300))
                    self.gret = font1.render("Play Again",1,(0,0,0))
                    self.screen.blit(self.gret,(250,300))
            
            if (self.button2.collidepoint(pygame.mouse.get_pos())):
                    self.out = font1.render("Quit",1,(0,0,0))
                    self.screen.blit(self.out,(250,360))
                    self.out = font1.render("Quit",1,(255,255,255))
                    self.screen.blit(self.out,(250,360))
                    
            else:
                    self.out = font1.render("Quit",1,(255,255,255))
                    self.screen.blit(self.out,(250,360))
                    self.out = font1.render("Quit",1,(0,0,0))
                    self.screen.blit(self.out,(250,360))

            
            self.screen.blit(self.out,(250,360))
            #self.screen.blit(self.cont,(250,460))
            self.screen.blit(self.res,(250,230))
            self.screen.blit(self.fsco,(250,130))
            pygame.display.update();
        
            pygame.event.get()

        
        
        return self.restart