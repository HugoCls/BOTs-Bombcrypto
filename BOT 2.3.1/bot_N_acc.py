import time
import detects as dt
import heroes as h
import refresh as fresh
import zzz
import clavier_souris as cs
import errors
import historic
import random as rd
import pause
##WHOLE BOT:
def loop_with_zzz(N):
    loop_count=0
    zzz_numbers=[4,4,3,3]
    t=time.time()
    #ERRORS SETUP
    errors.RESET()
    t_errors=time.time()
    ERROR=False
    last_count=int(errors.COUNT())
    PAUSE=False
    t_pause=time.time()
    mins_until_next_pause=rd.randint(180,240)
    while loop_count!=-1:
        if PAUSE==False:
            #CHECKING THINGS
            if fresh.refresh():
                cs.random_sleep(0.5)
            if fresh.connect():
                cs.random_sleep(0.5)
            if dt.find('treasure hunt'):
                cs.random_sleep(0.5)
            if dt.find('new map'):
               cs.random_sleep(0.5)
            if fresh.connect():
                cs.random_sleep(0.5)

            if time.time()-t>=rd.randint(120,180):
                fresh.auto_refresh()
                t=time.time()
            #ZZZ THINGS
            if loop_count%2==0:
                for i in [0,1]:
                    if zzz.count(i)>=zzz_numbers[i]:
                        while dt.find('new map'):
                            cs.random_sleep(0.5)
                        loop(i)
            else:
                for i in [2,3]:
                    if zzz.count(i)>=zzz_numbers[i]:
                        while dt.find('new map'):
                            cs.random_sleep(0.5)
                        loop(i)
            loop_count+=1
            #ERRORS THINGS
            err_count=int(errors.COUNT())
            if err_count!=last_count:
                last_count=err_count
                if err_count>=8:
                    historic.printt('Errors | Critical | '+str(err_count))

            if err_count>=15:
                historic.printt("BOT STOPPED <@397738036592508931> BOT STOPPED")
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
        else:   #PAUSE THINGS
            None
            """
            pause.pause_all(N)
            cs.random_sleep(rd.uniform(15*60,30*60))
            pause.unpause_all(N)
            t_pause=time.time()
            PAUSE=False
            """

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
    if dt.check('connect')==False:
        h.heroes_entirely()
    else:
        fresh.connect()
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)
