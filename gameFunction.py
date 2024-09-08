import sys
import pygame
import pygame.locals 
from bullet import Bullet
from Aline import Aline
import threading
import time
def keycheckEvent(ship,bullets,setting,screen):
     for bullet in bullets :
         if bullet.rect.top<0:
            bullets.remove(bullet)
            ship.numBullet-=1
     for event in pygame.event.get():
            if event.type==pygame.QUIT:#检测是否需要退出
                pygame.quit()
                sys.exit()
            
            elif  event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_RIGHT:
                    ship.movingRight=True
                if event.key==pygame.K_LEFT:
                    ship.movingLeft=True
                if event.key==pygame.K_SPACE:
                    bullets.append(Bullet(screen,setting,ship))
                    ship.numBullet+=1
            
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    ship.movingRight=False
                if event.key==pygame.K_LEFT:
                    ship.movingLeft=False

def crashEvent(Bullets,Alines,ship):
    for bullet in Bullets:
        for aline in Alines:
            if ship.rect.top<aline.rect.bottom and (aline.rect.bottomleft[0]<ship.rect.centerx and ship.rect.centerx<aline.rect.bottomright[0]):
                ship.life-=1
            if bullet.rect.top<aline.rect.bottom and (aline.rect.bottomleft[0]<bullet.rect.centerx and bullet.rect.centerx<aline.rect.bottomright[0]):
               # print(2)
                aline.produce=False
                if bullet in Bullets:Bullets.remove(bullet)




          
def produceAline(Alines,setting,ship):
    if  Alines[0].produce:
        aline=Aline(setting,Alines[0].screen)
        aline.produce=True
        Alines.append(aline)
        Alines[0].life+=1
        Alines[0].produce=True
        #print(len(Alines))
    if  len(Alines)==11:
        Alines[0].produce=False
    Delete(Alines,setting,ship)



def Delete(Alines,setting,ship):
    if not Alines[0].produce:
        #if  len(Alines)<=1:
        for aline in Alines:
            if aline==Alines[0]:
                continue
            if aline.rect.bottom>setting.height or not aline.produce:
                if not aline.produce:
                    aline_pop=aline
                    Beng = threading.Thread(target=showbeng,args=(aline_pop,))
                    Beng.start()
                else :
                    ship.life-=1
                    if(ship.life==0):
                        print("You are died,Game over")
                        pygame.quit()
                        sys.exit()
                        
                Alines.remove(aline)
    if len(Alines)<=3:
        #print(len(Alines))
        Alines[0].produce=True
       # Alines[0].produce=False

        
def showbeng(aline):
        aline.blitme_beng()
    #print(1)
    


     

def update(setting,screen,ship,bullets,Alines):
    screen.fill(setting.color)
    ship.update()
    ship.blitme()
    produceAline(Alines,setting,ship)
    for bullet in bullets:
        bullet.update()
        bullet.blitme()
    for i in range(1,len(Alines)-1):
        Alines[i].update()
        Alines[i].blitme()
    pygame.display.flip()#更新屏幕
    
