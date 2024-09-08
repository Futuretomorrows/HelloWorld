import pygame
class Bullet:
    def __init__(self,screen,setting,ship):
        self.screen=screen
        self.setting=setting
        self.ship=ship
        
        self.image=pygame.image.load('images/bullet.bmp')
        self.rect=self.image.get_rect()
        self.rect.centerx=self.ship.center
        self.rect.bottom=self.ship.rect.top


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.rect.top-=self.setting.bulletSpeed

        



        
