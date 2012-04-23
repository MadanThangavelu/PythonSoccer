import pygame,os
from helpers import *
from ball import *
import random

class game_engine(pygame.sprite.Sprite):
    
    def __init__(self):
        self.victory = 1
    
    def analyze(self,player1,op2,ball,op1):
        #if (ball.rect.left > player1.rect.left - 2) and (ball.rect.left < player1.rect.left + player1.rect.width + 2) and (ball.rect.top > player1.rect.top) and (ball.rect.top < player1.rect.top + player1.rect.height + 2):
        #    return 1
        #else:
        
        if (op1.rect.top < ball.rect.top):
                op1.rect.top +=1
        
        if op1.rect.top > ball.rect.top:
                op1.rect.top -=1
            
        if op1.rect.left < ball.rect.left:
                op1.rect.left += 1
            
        if op1.rect.left > ball.rect.left:
                op1.rect.left -= 1
        
        if op1.rect.left > 425:
            self.attack = 1
        else:
            self.attack = 0
        
        if op1.rect.colliderect(ball.rect) == 1 :
            if ball.rect.left < 900:
                ball.rect.left +=50
                if ball.rect.top < 300:
                    ball.rect.top += 20
                if ball.rect.top > 268 + 230:
                    ball.rect.top -= 20
                else:
                    if (random.randrange(1,3,1) == 1) or (random.randrange(1,3,1) == 2):
                        ball.rect.top += 50
                    else:
                        ball.rect.top -= 50
            else:
                ball.rect.left -= 15
        
  
        
            