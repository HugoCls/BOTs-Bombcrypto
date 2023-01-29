import clavier_souris as cs
import matchtemplate as templ
from time import sleep
import detects as dt
import anticheat

def loop(i):
    dt.find('new map')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
        sleep(2)
    sleep(0.5)
    dt.find_the_one('arrow',i)
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
        sleep(2)
    dt.find('heroes')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
        sleep(2)
    #Vérifie si le serveur a crash
    if dt.check('connect')==False and dt.check('ok')==False:
        work_heroes()
    sleep(0.5)
    dt.find('close')
    sleep(0.5)
    dt.find('treasure hunt')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
        sleep(2)

def work_heroes():
    L,w,h=templ.matchtemplate('swords')
    if len(L)>=1:
        (x,y)=L[0][0]+w/2,L[0][1]+h/2+100
        cs.move(x,y)
        cs.clic_gauche()
        for i in range(70):
            cs.scroll(-1)
            sleep(0.01)
        sleep(0.5)
        L,w,h=templ.matchtemplate('work_off')
        N=len(L)
        if N>=1:
            for i in range(15):
                x,y=L[N-1][0]+w/2,L[N-1][1]+h/2
                cs.move(x,y)
                cs.clic_gauche()
                sleep(0.5)