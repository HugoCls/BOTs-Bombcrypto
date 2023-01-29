import clavier_souris as cs
import matchtemplate as templ
from time import sleep
import detects as dt
import anticheat_numbers
from PIL import ImageGrab
import colors
import errors

def loop(i):
    working_heroes=0
    if dt.find('new map'):
       sleep(0.5)
    if dt.check('robot_numbers'):
        anticheat_numbers.all_captcha()
        sleep(0.5)
    if dt.find_the_one('arrow',i):
        sleep(0.5)
    if dt.check('robot_numbers'):
        
        anticheat_numbers.all_captcha()
        sleep(0.5)
    if dt.find('heroes'):
        sleep(0.5)
    if dt.check('robot_numbers'):
        
        anticheat_numbers.all_captcha()
        sleep(2)
    #Vérifie si le serveur a crash
    if dt.check('connect')==False and dt.check('ok')==False:
        working_heroes=little_team_all_heroes()
        sleep(0.5)
    if dt.find('close'):
        sleep(0.5)
    if dt.find('treasure hunt'):
        sleep(0.5)
    if dt.check('robot_numbers'):
        
        anticheat_numbers.all_captcha()
        sleep(2)
    return(working_heroes)

def little_team_all_heroes():
    i=0
    working_heroes=0
    while i<3:
        if i==0:
            working_heroes+=working_count()
        working_heroes+=little_team_work(0.4)
        if i<=1:
            next_heroes()
        i+=1
    return(working_heroes)

def little_team_work(percentage):
    count=0
    while all_hight_health_working(percentage)==False:# and dt.check('overload')==False:
        L,w,h=templ.matchtemplate('work_off')
        L=work_images()
        N=len(L)
        i=0
        if N>=1:
            while i<N:
                (x,y)=L[i]
                x0,y0=x-114,y+23
                xw,yw=x+w/2,y+3*h/4
                lifepercentage=check_lifebar(x0,y0)
                working=colors.light_green(xw,yw)
                if lifepercentage>=percentage and not working:
                    cs.move(xw,yw)
                    cs.clic_gauche()
                    count+=1
                    sleep(0.5)
                i+=1
    return(count)

def all_hight_health_working(percentage):
    L,w,h=templ.matchtemplate('work_off')
    L=work_images()
    N=len(L)
    count=0
    for i in range(N):
        (x,y)=L[i]
        x0,y0=x-114,y+23
        lifepercentage=check_lifebar(x0,y0)
        xw,yw=x+w/2,y+3*h/4
        #print('HPs | '+str(lifepercentage))
        working=colors.light_green(xw,yw)
        if lifepercentage<=percentage or working:
            count+=1
            """
            if not working:
                cs.move(xw,yw)
                cs.clic_gauche()
                sleep(0.5)
            """
    return(count==N)

def working_count():
    L,w,h=templ.matchtemplate('work_off')
    L=work_images()
    N=len(L)
    count=0
    for i in range(N):
        (x,y)=L[i]
        xw,yw=x+w/2,y+3*h/4
        working=(colors.light_green(xw,yw)==True)
        if working:
            count+=1
    return(count)

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

def next_heroes():
    L,w,h=templ.matchtemplate('swords')
    if len(L)>=1:
        (x,y)=L[0][0]+w/2,L[0][1]+h/2+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(20):
            cs.scroll(-1)
            sleep(0.01)
    sleep(0.05)
            
def work_images():
    L_off,w,h=templ.matchtemplate('work_off')
    N=len(L_off)
    D=[]
    if N>=1:
        xmin=L_off[0][0]
        for i in range(N):
            if L_off[i][0]<=xmin:
                xmin=L_off[i][0]
        for i in range(N):
            if L_off[i][0]>xmin:
                D.append(i)
        m=len(D)
        for i in range(m):
            del(L_off[D[m-1-i]])
    return(L_off)