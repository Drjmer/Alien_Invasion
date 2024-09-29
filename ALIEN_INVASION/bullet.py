import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__ (self, ai_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen=screen

        #create bullet at (0,0) ans then set at correct position.
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
        ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #stores bullet postion as a decimal
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
    
    def update(self):
        #moving bullet upthe screen
        self.y-=self.speed_factor
        #update its y value
        self.rect.y=self.y

    def draw_bullet(self):
        #draw the bullet ont the screens
        pygame.draw.rect(self.screen,self.color,self.rect)