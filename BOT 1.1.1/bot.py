from time import sleep
import time
import detects as dt
import anticheat_numbers
import refresh as fresh
import heroes
import historic
import errors
import music

def infinite_loop(j,N):
    errors.RESET()
    t0=time.time()
    t1=time.time()
    trefresh=time.time()
    t_errors=time.time()
    i=0
    ERROR=False
    last_count=int(errors.COUNT())
    while True:
        if dt.find('new map'):
            i+=1
            historic.printt("Map | "+str(i))
        if fresh.refresh():
            sleep(0.5)
        if fresh.connect():
            sleep(0.5)
        if dt.find('close'):
            sleep(0.5)
        if dt.find('treasure hunt'):
            sleep(0.5)
        if dt.check('robot_numbers'):
            anticheat_numbers.all_captcha()
            sleep(0.5)
        while dt.find('treasure hunt'):
            sleep(0.5)
        if j==0:
            t0-=1000
            t1-=1000
            j+=1
        if time.time()-trefresh>=300:
            for i in range(N):
                dt.find_the_one('arrow',i)
            sleep(0.5)
            for i in range(N):
                dt.find_the_one('treasure hunt',i)
            trefresh=time.time()
        if time.time()-t0>=1000:
            while dt.find('treasure hunt'):
                sleep(0.5)
            working_heroes=heroes.loop(0)
            historic.printt("Heroes | 0 | "+str(working_heroes)+" working")
            t0=time.time()
            
        if time.time()-t1>=1000 and N>=2:
            while dt.find('treasure hunt'):
                sleep(0.5)
            working_heroes=heroes.loop(1)
            historic.printt("Heroes | 1 | "+str(working_heroes)+" working")
            t1=time.time()
        if historic.error():
            historic.printt("<@150673899963678720>. Historic :/")
        
        err_count=int(errors.COUNT())
        if err_count!=last_count:
            last_count=err_count
            if err_count>=8:
                historic.printt('Errors | Critical | '+str(err_count))
        
        if err_count>=15:
            historic.printt("<@150673899963678720>. Errors :/")
            ERROR=True
            break
        if time.time()-t_errors>=300:
            historic.printt("Errors | 300s | "+errors.COUNT())
            errors.RESET()
            t_errors=time.time()
            sleep(0.5)
    if ERROR:
        music.play()