import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__() #initilaise the parent class sprite by calling the constructor of parent class
        self.screen=screen
        self.ai_settings=ai_settings
        #loading the ship icon
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        
        #allocating ship to the right position
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)
    
    def blitme(self):
        #draw the alien at current pos
        self.screen.blit(self.image,self.rect) #blit is a fxm in pygame to draw the image
    
    def update(self):
        #move the fleet to the right
        self.x+=(self.ai_settings.alien_speed_factor* self.ai_settings.fleet_direction)
        self.rect.x=self.x
    
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right :
            return True
        elif self.rect.left<=0:
            return True
       
