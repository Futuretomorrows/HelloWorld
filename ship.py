import pygame
class Ship:
    def __init__(self,screen,setting):
        self.screen=screen
        self.setting=setting
        self.image=pygame.image.load('images/ship.bmp')
        #获得界面矩形与飞机矩形
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #设置飞机位置为最下面
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #判断左右移动
        self.movingRight=False
        self.movingLeft=False
        #中间位置
        self.center=(float)(self.rect.centerx)
        #子弹数量
        self.numBullet=0
        #飞船生命
        self.life=10


    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def update(self):
        if self.movingRight==True:
            self.center+=self.setting.speed
        if self.movingLeft==True:
            self.center-=self.setting.speed
        
        self.rect.centerx=self.center
        if self.rect.right>self.setting.width:
            self.rect.left=0
            self.center=self.rect.centerx
            
        if self.rect.left<0:
            self.rect.right=self.setting.width
            self.center=self.rect.centerx



