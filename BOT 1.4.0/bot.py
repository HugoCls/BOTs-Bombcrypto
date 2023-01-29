import time
import detects as dt
import anticheat_reveal as anticheat
import refresh as fresh
import heroes
import historic
import errors
import music
import clavier_souris as cs
import random as rd
import windows as wd

def test():
    while True:
        if dt.find('new map'):
            cs.random_sleep(0.5)

def infinite_loop(j,N):
    #from time import sleep
    #sleep(3600)
    wd.positionner_bombcrypto()
    t0=time.time()
    t1=time.time()
    t2=time.time()
    t3=time.time()
    trefresh=time.time()
    #Errors
    errors.RESET()
    t_errors=time.time()
    ERROR=False
    last_count=int(errors.COUNT())
    map_count=0
    loop_count=0
    while True:
        loop_count+=1
        """if loop_count%5==1:
            wd.premier_plan_bombcrypto()"""
        if dt.find('new map'):
            map_count+=1
            historic.printt("Map | "+str(map_count))
        if fresh.refresh():
            cs.random_sleep(0.5)
        if fresh.connect():
            cs.random_sleep(0.5)
        if dt.find('close'):
            cs.random_sleep(0.5)
        if dt.find('treasure hunt'):
            cs.random_sleep(0.5)
        if dt.check('robot_numbers'):
            anticheat.all_captcha()
            cs.random_sleep(0.5)
        while dt.find('treasure hunt'):
            cs.random_sleep(0.5)
        if j==0:
            t0-=1000
            t1-=1000
            t2-=1000
            t3-=1000
            j+=1
        if time.time()-trefresh>=rd.randint(180,220):
            for i in range(N):
                dt.find_the_one('arrow',i)
            cs.random_sleep(0.5)
            for i in range(N):
                dt.find_the_one('treasure hunt',i)
            trefresh=time.time()
        if time.time()-t0>=1000:
            while dt.find('treasure hunt'):
                cs.random_sleep(0.5)
            working_heroes=heroes.loop(0)
            historic.printt("Heroes | 0 | "+str(working_heroes)+" working")
            t0=time.time()
            
        if time.time()-t1>=1000 and N>=2:
            while dt.find('treasure hunt'):
                cs.random_sleep(0.5)
            working_heroes=heroes.loop(1)
            historic.printt("Heroes | 1 | "+str(working_heroes)+" working")
            t1=time.time()
            
        if time.time()-t2>=1000 and N>=3:
            while dt.find('treasure hunt'):
                cs.random_sleep(0.5)
            working_heroes=heroes.loop(2)
            historic.printt("Heroes | 2 | "+str(working_heroes)+" working")
            t2=time.time()

        if time.time()-t3>=1000 and N>=4:
            while dt.find('treasure hunt'):
                cs.random_sleep(0.5)
            working_heroes=heroes.loop(3)
            historic.printt("Heroes | 3 | "+str(working_heroes)+" working")
            t3=time.time()
        
        err_count=int(errors.COUNT())
        if err_count!=last_count:
            last_count=err_count
            if err_count>=6:
                historic.printt('Errors | Critical | '+str(err_count))
        
        if err_count>=15:
            historic.printt("BOT STOPPED <@150673899963678720> BOT STOPPED")
            ERROR=True
            break
        if time.time()-t_errors>=300:
            historic.screen()
            """
            if loop_count%10==0:
                for i in range(N):
                    dt.find('chest')
                    cs.random_sleep(0.2)
                cs.random_sleep(1)
                historic.coins()
                
                for i in range(N):
                    dt.find('close')
                    cs.random_sleep(0.2)
            """
            
            historic.printt("Errors | 300s | "+errors.COUNT())
            errors.RESET()
            t_errors=time.time()
            cs.random_sleep(0.5)
    if ERROR:
        music.play()