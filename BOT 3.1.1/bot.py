import time
import detects as dt
import refresh as fresh
import heroes as h
import errors
import clavier_souris as cs
import random as rd
import windows as wd
from time import sleep

def infinite_loop(j,N):
    wd.positionner_bombcrypto()
    windows=wd.pygetwindow.getWindowsWithTitle('Bombcrypto')
    """
    N=len(windows)
    if N==0:
        print('Bombcrypto not oppened')
        sleep(5)
    """
    heroes_t=[]
    for i in range(N):
        heroes_t.append(time.time())
    trefresh=time.time()
    #ERROR THINGS
    errors.RESET()
    t_errors=time.time()
    last_count=int(errors.COUNT())
    #COUNTS
    map_count=0
    loop_count=0
    while True:
        loop_count+=1
        if dt.find('new map'):
            map_count+=1
            #printt("Map | "+str(map_count))
        if dt.find('close'):
            cs.random_sleep(0.5)
        while dt.find('treasure hunt'):
            cs.random_sleep(0.5)
            
        fresh.connect()
        
        if j==0:
            for i in range(N):
                heroes_t[i]-=1000
            j+=1
        
        if time.time()-trefresh>=rd.randint(5*60,6*60):
            for i in range(N):
                dt.find_the_one('arrow',i)
            cs.random_sleep(0.5)
            for i in range(N):
                dt.find_the_one('treasure hunt',i)
            trefresh=time.time()

        for i in range(N):
            if time.time()-heroes_t[i]>=1000:
                while dt.find('treasure hunt'):
                    cs.random_sleep(0.5)
                loop(i)
                heroes_t[i]=time.time()
                break

        err_count=int(errors.COUNT())
        if err_count!=last_count:
            last_count=err_count
            if err_count>=6:
                print('Errors | Critical | '+str(err_count))
        
        if err_count>=30:
            print("BOT STOPPED")
            break
        
        if time.time()-t_errors>=500:
            errors.RESET()
            t_errors=time.time()
            cs.random_sleep(0.5)
        
def loop(i):
    j=0
    while dt.find('new map'):
        cs.random_sleep(0.5)
    if dt.find_the_one('arrow',i):
        cs.random_sleep(0.5)
    if dt.find('heroes'):
        cs.random_sleep(0.5)
    t_upgrade=time.time()
    while dt.check('upgrade')==False and time.time()-t_upgrade<=20:
        cs.random_sleep(0.1)
        if dt.check_the_one('new map')[1]==i:
            j=1
            break
    if j==1:
        return(None)
    h.heroes_entirely()

    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)