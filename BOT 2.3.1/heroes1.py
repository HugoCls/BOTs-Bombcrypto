import matchtemplate as templ
import class_heroes as H
from PIL import ImageGrab
import clavier_souris as cs
import random as rd
import detects as dt
import colors
import time
#TIME TESTS
def time_test():
    for i in range(20):
        t=time.time()
        A=update_heroes()
        print(time.time()-t)

##LOOPS
def heroes_entirely():
    i=0

    for k in range(2):
        next_heroes()

    while i<3:
        heroes_on_screen()
        if i<=1:
            #next_heroes()
            previous_heroes()
        i+=1
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)

def all_to_sleep():
    i=0
    for k in range(2):
        next_heroes()
    while i<3:
        heroes_to_sleep()
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

def all_to_work():
    for k in range(2):
        next_heroes()
    heroes_to_work()
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)

##INFORMATIVE FUNCTIONS
def initialise_heroes():
    HEROES=[]
    for i in range(5):
        HEROES.append(H.Hero())
    L,w,h=templ.matchtemplate_personalized('work_off',0.8)
    for i,hero in enumerate(HEROES):
        if len(L)>=i+1:
            hero.work_topleft=L[i]
    return(HEROES)

def update_heroes():
    HEROES=initialise_heroes()

    Lw,w,h=templ.matchtemplate_personalized('work_on',0.94)
    working_heroes=[]
    for i in range(len(Lw)):
        working_heroes.append(hero_number(HEROES,Lw[i]))

    Lr,w,h=templ.matchtemplate_personalized('rest_on',0.94)
    resting_heroes=[]
    for i in range(len(Lr)):
        resting_heroes.append(hero_number(HEROES,Lr[i]))

    Lh,w,h=templ.matchtemplate_personalized('home_on',0.94)
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
        x0-=114
        y0+=23
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

##ACTIVE FUNCTIONS
def heroes_on_screen():
    HEROES=update_heroes()
    while True:
        if all_well_placed(HEROES):
            #print('broke')
            break
        else:
            #print('updating')
            HEROES=update_heroes()

def heroes_to_sleep():
    HEROES=update_heroes()
    for i,hero in enumerate(HEROES):
        if hero.home_state==False and hero.rest_state==False:
            hero.send_to_home(True)

def heroes_to_work():
    HEROES=initialise_heroes()
    hero=HEROES[len(HEROES)-1]
    (x,y)=hero.work_topleft
    x+=26
    y+=25
    for i in range(15):
        hero.send_to_work(True)
        cs.random_sleep(0.3)
        if colors.light_green(x,y):
            break

def all_well_placed(HEROES):
    N=len(HEROES)
    if N>=1:
        for i in range(N):
            hero_state=well_placed(HEROES[N-1-i])
            """
            if hero_state==False:
                return(False)
            """
        return(True)

def well_placed(hero):
    if 0.25<=hero.hp_percentage:
        if hero.work_state==False:
            hero.send_to_work(True)
            return(False)
        else:
            return(True)
    else:
        if hero.home_state==False:
            (x,y)=hero.work_topleft
            x+=146
            y+=25
            home_full=colors.gray(x,y)
            if home_full==False:
                hero.send_to_home(True)
                return(False)
            else:
                if hero.rest_state==False:
                    hero.send_to_rest
                    return(False)
                else:
                    return(True)
            return(True)
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