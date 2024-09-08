import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
import gameFunction as GF
from Aline import Aline
def run_game(): 
    pygame.init() 
    setting=Settings()
    screen=pygame.display.set_mode((setting.width,setting.height))
    ship=Ship(screen,setting)
    bullets=[]
    Alines=[]

    #总外星人，记录一些特殊的数据
    Aline_F=Aline(setting,screen)
    Aline_F.life=0
    Alines.append(Aline_F)
    pygame.display.set_caption("ALine Invasion")

 
 #主循环
    while True: 
        GF.update(setting,screen,ship,bullets,Alines)
        GF.keycheckEvent(ship,bullets,setting,screen)#进行事件检查
        GF.crashEvent(bullets,Alines,ship)
        
        

   

run_game()

