import clavier_souris as cs
import matchtemplate as templ
from time import sleep
import time
import detects as dt
import anticheat

def infinite_loop(j):
    t0=time.time()
    t1=time.time()
    i=0
    while True:
        if (dt.find('new map')==True):
            i+=1
            print("Map "+str(i)+" Ended.")
        refresh()
        sleep(0.5)
        connect()
        sleep(0.5)
        dt.find('close')
        sleep(0.5)
        dt.find('treasure hunt')
        sleep(0.5)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(0.5)
        if j==0:
            heroes()
            print("Heroes back to work.")
            j+=1
        sleep(1)
        if time.time()-t1>=300:
            dt.find('arrow')
            sleep(0.5)
            dt.find('treasure hunt')
            t1=time.time()
        if time.time()-t0>=3600:
            heroes()
            print("Heroes back to work.")
            t0=time.time()

def skip_maintenance(waiting_time):
    t0=time.time()
    while time.time()-t0<=waiting_time:
        sleep(1)
    if waiting_time>0:
        cs.appuyer(cs.F5)
        sleep(5)
    while dt.check('arrow')==False:
        connect()
        if dt.check('arrow')==False:
            cs.appuyer(cs.F5)
        sleep(12)
    infinite_loop(0)

def heroes():
    dt.find('new map')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
        sleep(2)
    sleep(0.5)
    dt.find('arrow')
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

def refresh():
    result=dt.check('ok')
    if result==True:
        cs.appuyer(cs.F5)
        sleep(6)
        dt.find('connect')
        sleep(2)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(3)
        dt.find('sign')
        sleep(2)
        dt.find('connect')
        return(True)
    return(False)

def connect():
    if dt.check('connect')==True:
        t0=time.time()
        cs.appuyer(cs.F5)
        sleep(10)
        dt.find('connect')
        sleep(2)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(1)
        while dt.check('sign')==False and time.time()-t0<=100:
            sleep(0.5)
        sleep(1)
        dt.find('sign')
        sleep(3)
        while dt.check('treasure hunt')==False:
            sleep(0.5)
            if dt.find('connect')==True or dt.find('ok')==True or time.time()-t0>=200:
                break
        sleep(2)
        dt.find('treasure hunt')
        sleep(2)
        print('Tryed to connect for '+str(int(time.time()-t0))+'seconds.')
        
    
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