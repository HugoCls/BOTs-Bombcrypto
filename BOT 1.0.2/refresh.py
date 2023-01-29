import clavier_souris as cs
import detects as dt
import matchtemplate as templ
from time import sleep
import time
import anticheat
import historic

def auto_refresh():
    for i in range(3):
        found=dt.find('new map')
        if found==True:
            sleep(0.5)
    L,w,h=templ.matchtemplate('arrow')
    for i in range(len(L)):
        (x,y)=L[i][0]+w/2,L[i][1]+h/2
        cs.move(x,y)
        cs.clic_gauche()
        sleep(1)
    L,w,h=templ.matchtemplate('treasure hunt')
    for i in range(len(L)):
        (x,y)=L[i][0]+w/2,L[i][1]+h/2
        cs.move(x,y)
        cs.clic_gauche()

def refresh():
    result=dt.find('ok')
    if result==True:
        cs.appuyer(cs.F5)
        sleep(6)
        dt.find('connect')
        sleep(1)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(3)
        if dt.check('busy_fox')==True and dt.check('sign')==False:
            dt.find('busy_fox')
            sleep(1.5)
        dt.find('sign')
        sleep(2)
        dt.find('connect')
        return(True)
    return(False)

def connect():
    tconnexion=time.time()
    while dt.find('bombcrypto connexion')==True and dt.check('connect')==False:
        if dt.check('busy_fox')==True:
            dt.find('busy_fox')
            sleep(2)
            dt.find('sign')
            sleep(0.5)
            cs.ctrl(cs.F5)
            sleep(0.5)
        if time.time()-tconnexion>=40:
            historic.printt('Connect | Expired')
            cs.ctrl(cs.F5)
    while dt.find('bombcrypto mainscreen')==True:
        if dt.check('busy_fox')==True:
            dt.find('busy_fox')
            sleep(2)
            dt.find('sign')
            sleep(0.5)
            cs.ctrl(cs.F5)
            sleep(0.5)
        t0=time.time()
        result=dt.find('connect')
        sleep(1)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
            sleep(1.5)
        dt.find('sign')
        historic.printt('Connect | '+str(int(time.time()-t0))+'s')