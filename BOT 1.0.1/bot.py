import clavier_souris as cs
from time import sleep
import time
import detects as dt
import anticheat
import refresh as fresh
import heroes

def infinite_loop(j,N):
    t0=time.time()
    t1=time.time()
    trefresh=time.time()
    i=0
    while True:
        if (dt.find('new map')==True):
            i+=1
            print("Map | "+str(i))
        fresh.refresh()
        sleep(0.5)
        fresh.connect()
        sleep(0.5)
        dt.find('close')
        sleep(0.5)
        dt.find('treasure hunt')
        sleep(0.5)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(0.5)
        if j==0:
            heroes.loop(0)
            print("Heroes | 0 | Work")
            heroes.loop(1)
            print("Heroes | 1 | Work")
            j+=1
        sleep(1)
        if time.time()-trefresh>=300:
            for i in range(N):
                dt.find_the_one('arrow',i)
            sleep(0.5)
            for i in range(N):
                dt.find_the_one('treasure hunt',i)
            trefresh=time.time()
        if time.time()-t0>=2400:
            heroes.loop(0)
            print("Heroes | 0 | Work")
            t0=time.time()
            
        if time.time()-t1>=2400 and N>=2:
            heroes.loop(1)
            print("Heroes | 1 | Work")
            t1=time.time()