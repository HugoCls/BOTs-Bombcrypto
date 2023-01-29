import clavier_souris as cs
import matchtemplate as templ
import detects as dt
from PIL import ImageGrab
from time import sleep
import colors
import anticheat_numbers

def home_heroes():
    p=0
    while all_enought_health(0.25)==False:# and dt.check('overload')==False:
        L,w,h=templ.matchtemplate('work_off')
        L=work_images()
        N=len(L)
        i=0
        if N>=1:
            while i<N:
                (x,y)=L[N-1-i]
                x0,y0=x-114,y+23
                lifepercentage=check_lifebar(x0,y0)
                if lifepercentage<=0.25:
                    #dt.checking if home is full
                    if colors.gray(x+128,y) or colors.gray(x+128,y+30):
                        i=N
                        p=1
                    #dt.checking if he is already home
                    if colors.yellow(x+128,y+30) or colors.yellow(x+128,y+5):
                        None
                    #else just clic home
                    else:
                        cs.move(x+128,y+8)
                        cs.clic_gauche()
                        cs.move(x+123,y+30)
                        cs.clic_gauche()
                        cs.random_sleep(0.2)
                else:
                    None
                i+=1
    return(p==1)

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

def rest_on_work_coordonates():
    L,w,h=templ.matchtemplate('work_off')
    L=work_images()
    D=[]
    for i in range(len(L)):
        x,y=L[i][0]+w/2+40,L[i][1]+10
        cs.move(x,y)
        (R,G,B)=cs.pixelRGB(x,y)
        if R<=220:
            D.append(i)
    for i in range(len(D)):
        del(L[len(D)-1-i])
    return(L)

def resting_heroes_to_work(percentage):
    L=rest_on_work_coordonates()
    N=len(L)
    for i in range(N):
        (x,y)=L[i]
        x0,y0=x-114,y+23
        lifepercentage=check_lifebar(x0,y0)
        #print(lifepercentage)
        if lifepercentage>=percentage:
            cs.move(x+10,y+10)
            cs.clic_gauche()
            cs.random_sleep(0.8)


def all_enought_health(percentage):
    L,w,h=templ.matchtemplate('work_off')
    L=work_images()
    N=len(L)
    count=0
    for i in range(N):
        (x,y)=L[i]
        x0,y0=x-114,y+23
        lifepercentage=check_lifebar(x0,y0)
        print('HPs | '+str(lifepercentage))
        if lifepercentage>=percentage or colors.yellow(x+128,y+30) or colors.yellow(x+128,y+5)or colors.gray(x+128,y+30) or colors.gray(x+128,y):
            count+=1
    return(count==N)

def next_hero():
    L,w,h=templ.matchtemplate('swords')
    if len(L)>=1:
        (x,y)=L[0][0]+w/2,L[0][1]+h/2+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(5):
            cs.scroll(1)
            cs.random_sleep(0.01)

def next_heroes():
    L,w,h=templ.matchtemplate('swords')
    if len(L)>=1:
        (x,y)=L[0][0]+w/2,L[0][1]+h/2+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(20):
            cs.scroll(1)
            cs.random_sleep(0.01)

def home_all_heroes():
    i=0
    while i<3:
        home_full=home_heroes()
        if home_full==True :#or dt.check('overload')==True:
            i=3
        if i<=2:
            next_heroes()
            i+=1
    home_heroes()

def heroes_entirely():
    work_all_heroes()
    resting_heroes_to_work(0.25)
    home_all_heroes()
    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)

def work_all_heroes():
    L,w,h=templ.matchtemplate('swords')
    if len(L)>=1:
        (x,y)=L[0][0]+w/2,L[0][1]+h/2+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(70):
            cs.scroll(-1)
            cs.random_sleep(0.01)
        cs.random_sleep(0.5)
        L,w,h=templ.matchtemplate('work_off')
        N=len(L)
        all_to_work=False
        if N>=1:
            x,y=L[N-1][0]+w/2,L[N-1][1]+h/2+13
            while all_to_work==False:
                #We check the color of the bottom work icon
                (R,G,B)=cs.pixelRGB(x,y)
                #Wecheck the color of the bottom rest icon
                xr,yr=x+40,y
                (Rr,Gr,Br)=cs.pixelRGB(xr,yr)
                if G<=200 :
                    if Gr<=180:
                        cs.move(x,y)
                        cs.clic_gauche()
                        cs.random_sleep(0.8)
                    else:
                        all_to_work=True
                else:
                    all_to_work=True

#WORK OFF (115, 147, 94)
#WORK ON  (177, 130, 22)
#REST OFF (177, 130, 22)
#REST ON  (253, 186, 32)

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