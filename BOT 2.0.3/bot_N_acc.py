from time import sleep
import time
import detects as dt
import heroes as h
import refresh as fresh
import zzz
import anticheat

##WHOLE BOT:

def loop_with_zzz(N):
    j=0
    zzz_numbers=[4,3,3,3]
    t=time.time()
    while j==0:
        fresh.refresh()
        sleep(0.5)
        fresh.connect()
        sleep(0.5)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(0.5)
        dt.find('treasure hunt')
        sleep(0.5)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(0.5)
        dt.find('new map')
        sleep(0.5)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(0.5)
        dt.find('close')
        sleep(0.5)
        fresh.connect()
        sleep(0.5)
        if time.time()-t>=180:
            fresh.auto_refresh()
            t=time.time()

        for i in range(N):
            if zzz.count(i)>=zzz_numbers[i]:
                while dt.find('new map')==True:
                    sleep(0.5)
                loop(i)

def loop(i):
    j=0
    while dt.find('new map')==True:
        sleep(1)
    dt.find_the_one('arrow',i)
    sleep(0.5)
    dt.find('heroes')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
    sleep(0.5)
    while dt.check('upgrade')==False:
        sleep(0.1)
        if dt.check_the_one('new map')[1]==i:
            j=1
            break
    if j==1:
        return(None)
    if dt.check('connect')==False:
        h.heroes_entirely()
    else:
        fresh.connect()
        sleep(0.5)
    dt.find('treasure hunt')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
    sleep(0.5)
    dt.find('treasure hunt')
    sleep(0.5)
    if dt.check('robot')==True:
        anticheat.detect_puzzle(0)
    sleep(0.5)
