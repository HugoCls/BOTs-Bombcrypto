import matchtemplate as templ
import class_heroes as H
from PIL import ImageGrab
import clavier_souris as cs
import random as rd
import detects as dt
import colors
import cv2
import os
import time
#TIME TESTS
def time_test():
    #screen_gray=templ.screen_img()
    for i in range(20):
        t=time.time()
        #initialise_heroes(screen_gray)
        update_heroes()
        print(time.time()-t)

#IMAGES
work_on = cv2.imread(os.getcwd()+'\\images\\work_on.png',0)
work_off = cv2.imread(os.getcwd()+'\\images\\work_off.png',0)
home_on =   cv2.imread(os.getcwd()+'\\images\\home_on.png',0)
home_off =  cv2.imread(os.getcwd()+'\\images\\home_off.png',0)
home_full = cv2.imread(os.getcwd()+'\\images\\home_full.png',0)
rest_on = cv2.imread(os.getcwd()+'\\images\\rest_on.png',0)
rest_off =  cv2.imread(os.getcwd()+'\\images\\rest_off.png',0)

##LOOPS
def heroes_entirely():
    i=0
    """
    for k in range(2):
        next_heroes()
    """
    while i<3:
        heroes_on_screen()
        if i<=1:
            next_heroes()
            #previous_heroes()
        i+=1
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)

def all_to_sleep():
    screen_gray=templ.screen_img()
    heroes_to_sleep(screen_gray)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)

def all_to_work():
    for k in range(2):
        next_heroes()
    cs.random_sleep(0.3)
    screen_gray=templ.screen_img()
    heroes_to_work(screen_gray)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)

##INFORMATIVE FUNCTIONS
def initialise_heroes(screen_gray):
    HEROES=[]
    for i in range(5):
        HEROES.append(H.Hero())
    L=work_toplefts(screen_gray)
    #print(len(L))
    t=time.time()
    while len(L)<5 and time.time()-t<1:
        screen_gray=templ.screen_img()
        L=work_toplefts(screen_gray)
    #print(L)
    for i,hero in enumerate(HEROES):
        if len(L)>=(i+1):
            hero.work_topleft=L[i]
    return(HEROES,screen_gray)

def update_heroes():
    screen_gray=templ.screen_img()
    HEROES,screen_gray=initialise_heroes(screen_gray)
    Lw,w,h=templ.matchtemplate_fast_cibled(screen_gray,work_on,0.94)
    #print(Lw)
    working_heroes=[]
    for i in range(len(Lw)):
        working_heroes.append(hero_number(HEROES,Lw[i]))
    Lr,w,h=templ.matchtemplate_fast_cibled(screen_gray,rest_on,0.94)
    #print(Lr)
    resting_heroes=[]
    for i in range(len(Lr)):
        resting_heroes.append(hero_number(HEROES,Lr[i]))
    Lh,w,h=templ.matchtemplate_fast_cibled(screen_gray,home_on,0.98)
    #print(Lh)
    in_house_heroes=[]
    for i in range(len(Lh)):
        in_house_heroes.append(hero_number(HEROES,Lh[i]))
    for i,hero in enumerate(HEROES):
        if i in working_heroes:
            hero.set_work(True)
        if i in resting_heroes:
            hero.set_rest(True)
        if i in in_house_heroes:
            hero.set_home(True)
    #HPS
    for i,hero in enumerate(HEROES):
        (x0,y0)=hero.work_topleft
        x0-=75
        y0+=16
        hero.set_hp_percentage(check_lifebar(x0, y0))

    for i,hero in enumerate(HEROES):
        infos=hero.infos()
        print(infos)

    return(HEROES)

def hero_number(HEROES,point):
    coordonates=[]
    for i,hero in enumerate(HEROES):
        coordonates.append(hero.work_topleft)
    return(templ.closer_number(point[0],point[1],coordonates))

def check_lifebar(x0,y0):
    dx,dy=templ.width('lifebar')[1:3]
    x,y=x0,y0
    j=0
    found=False
    image = ImageGrab.grab()
    while found==False:
        RGB=image.getpixel((x, y))
        if RGB[2]>70 or j>=dx-1:
            found=True
        x+=1
        j+=1
        lifepercentage=j/dx
    return(lifepercentage)

def work_toplefts(screen_gray):
    Lon,w,h=templ.matchtemplate_fast_cibled(screen_gray,work_on,0.98)
    Loff,w,h=templ.matchtemplate_fast_cibled(screen_gray,work_off,0.98)
    for i in range(len(Loff)):
        Lon.append(Loff[i])
    return(templ.points(Lon))
##ACTIVE FUNCTIONS
def heroes_on_screen():
    HEROES=update_heroes()
    t=time.time()
    while True and time.time()-t<=90:
        (result,HEROES)=all_well_placed(HEROES)
        if result==True:
            #print('broke')
            break

def heroes_to_sleep(screen_gray):
    HEROES,screen_gray=initialise_heroes(screen_gray)
    hero=HEROES[0]
    (x,y)=hero.work_topleft
    xr=x+57
    xh=x+97
    y+=18
    for i in range(20):
        hero.send_to_home(True)
        cs.random_sleep(0.3)
        if colors.beige(xh,y):
            t=time.time()
            while colors.beige(xh,y) and time.time()-t<=10:
                cs.random_sleep(0.5)
            if time.time()-t>=10:
                break
        if colors.gray(xh,y) and colors.yellow(xr,y):
            cs.random_sleep(0.5)
            if colors.gray(xh,y) and colors.yellow(xr,y):
                break

def heroes_to_work(screen_gray):
    HEROES,screen_gray=initialise_heroes(screen_gray)
    hero=HEROES[len(HEROES)-1]
    (x,y)=hero.work_topleft
    xw=x+17
    y+=18
    for i in range(15):
        if colors.light_green(xw,y):
            break
        hero.send_to_work(True)
        cs.random_sleep(0.3)
        if colors.beige(xw,y):
            t=time.time()
            while colors.beige(x+5,y) and time.time()-t<=10:
                cs.random_sleep(0.5)
            if time.time()-t>=10:
                break

def all_well_placed(HEROES):
    N=len(HEROES)
    j=0
    if N>=1:
        for i in range(N):
            hero_state=well_placed(HEROES[N-1-i])
            if hero_state==False:
                cs.random_sleep(0.3)
                HEROES=update_heroes()
                j+=1
                break
        return(j==0,HEROES)

def well_placed(hero):
    (x,y)=hero.work_topleft
    if colors.beige(x+5,y+5):
        return(True)
    if 0.40<=hero.hp_percentage:
        if hero.work_state==False:
            hero.send_to_work(True)
            return(False)
        else:
            return(True)
    else:
        if hero.rest_state==False and hero.hp_percentage<=0.05:
            hero.send_to_rest(True)
        else:
            return(True)

def next_heroes():
    L,w,h=templ.matchtemplate('swords')
    dx=rd.randint(1,w-1)
    dy=rd.randint(1,h-1)
    if len(L)>=1:
        (x,y)=L[0][0]+dx,L[0][1]+dy+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(20):
            cs.scroll(-1)
            cs.random_sleep(0.01)
    cs.random_sleep(0.05)

def previous_heroes():
    L,w,h=templ.matchtemplate('swords')
    dx=rd.randint(1,w-1)
    dy=rd.randint(1,h-1)
    if len(L)>=1:
        (x,y)=L[0][0]+dx,L[0][1]+dy+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(20):
            cs.scroll(+1)
            cs.random_sleep(0.01)
    cs.random_sleep(0.05)