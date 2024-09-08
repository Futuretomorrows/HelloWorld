import pygame
import random
class Aline:
    def __init__(self,setting,screen):
        self.setting=setting
        self.screen=screen
        self.image=pygame.image.load('images/Aline.bmp')
        self.image_beng=pygame.image.load('images/beng.bmp')
        self.rect=self.image.get_rect()
        self.width=self.rect.bottomright[0]-self.rect.bottomleft[0]
        #设置外星人出生范围
        self.rect.top=random.randint(0,20)
        self.rect.left=random.randint(0,self.setting.width-self.width)
        #外星人的生命
        self.life=5
        self.produce=True
        self.grade=0



    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def update(self):
        self.rect.bottom+=self.setting.alineSpeed


    def blitme_beng(self):
        self.screen.blit(self.image_beng,self.rect)
        



