import time
import detects as dt
import refresh as fresh
import heroes as h
import historic
import errors
import music
import clavier_souris as cs
import random as rd
import windows as wd
import pause

def infinite_loop(j,N):
    wd.positionner_bombcrypto()
    windows=wd.pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')
    heroes_t=[]
    for i in range(N):
        heroes_t.append(time.time())
    trefresh_left=time.time()
    trefresh_right=time.time()
    #ERROR THINGS
    errors.RESET()
    t_errors=time.time()
    ERROR=False
    last_count=int(errors.COUNT())
    #COUNTS
    map_count=0
    loop_count=0
    #PAUSE THINGS
    PAUSE=False
    t_pause=time.time()
    mins_until_next_pause=rd.randint(4*60,5*60)
    while True:
        if PAUSE==False:
            loop_count+=1
            if dt.find('new map'):
                map_count+=1
                historic.printt("Map | "+str(map_count))
            if dt.find('close'):
                cs.random_sleep(0.5)
            while dt.find('treasure hunt'):
                cs.random_sleep(0.5)
                
            fresh.connect()
            
            if j==0:
                for i in range(N):
                    heroes_t[i]-=1000
                j+=1
            
            if time.time()-trefresh_left>=rd.randint(180,220):
                for i in range(N):
                    dt.find_the_one('arrow',i)
                cs.random_sleep(0.5)
                for i in range(N):
                    dt.find_the_one('treasure hunt',i)
                trefresh_left=time.time()

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
                    historic.printt('Errors | Critical | '+str(err_count))
            
            if err_count>=15 and time.time()-t_pause>=180:
                historic.printt("BOT STOPPED <@150673899963678720> BOT STOPPED")
                ERROR=True
                break
            
            if time.time()-t_errors>=300:
                historic.screen()
                historic.printt("Errors | 300s | "+errors.COUNT())
                errors.RESET()
                t_errors=time.time()
                cs.random_sleep(0.5)
            
            if time.time()-t_pause>=(60*mins_until_next_pause):
                PAUSE=True

        else:
            pause.pause_all(N)
            historic.printt('PAUSED')
            historic.screen()
            cs.random_sleep(rd.uniform(15*60,20*60)) #time in seconds
            fresh.F5_all(N)
            historic.printt('UNPAUSED')
            t_pause=time.time()
            PAUSE=False
            mins_until_next_pause=rd.randint(4*60,5*60) #time in minutes
    if ERROR:
        music.play()
        
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