from time import sleep
import time
import detects as dt
import heroes as h
import refresh as fresh
import zzz
import anticheat_numbers
import clavier_souris as cs
import errors
import historic
##WHOLE BOT:

def loop_with_zzz(N):
    j=0
    #Errors
    errors.RESET()
    t_errors=time.time()
    ERROR=False
    last_count=int(errors.COUNT())
    
    zzz_numbers=[4,4,3,3]
    t=time.time()
    while j!=-1:
        if fresh.refresh():
            cs.random_sleep(0.5)
        if fresh.connect():
            cs.random_sleep(0.5)
        if dt.check('robot_numbers'):
            anticheat_numbers.all_captcha()
            cs.random_sleep(0.5)
        if dt.find('treasure hunt'):
            cs.random_sleep(0.5)
        if dt.check('robot_numbers'):
            anticheat_numbers.all_captcha()
            cs.random_sleep(0.5)
        if dt.find('new map'):
           cs.random_sleep(0.5)
        if dt.check('robot_numbers'):
            anticheat_numbers.all_captcha()
            cs.random_sleep(0.5)
        if dt.find('close'):
            cs.random_sleep(0.5)
        if fresh.connect():
            cs.random_sleep(0.5)
            
        if time.time()-t>=180:
            fresh.auto_refresh()
            t=time.time()

        if j%2==0:
            for i in [0,1]:
                if zzz.count(i)>=zzz_numbers[i]:
                    while dt.find('new map'):
                        cs.random_sleep(0.5)
                        if dt.check('robot_numbers'):
                            anticheat_numbers.all_captcha()
                            cs.random_sleep(0.5)
                    loop(i)
        else:
            for i in [2,3]:
                if zzz.count(i)>=zzz_numbers[i]:
                    while dt.find('new map'):
                        cs.random_sleep(0.5)
                        if dt.check('robot_numbers'):
                            anticheat_numbers.all_captcha()
                            cs.random_sleep(0.5)
                    loop(i)
        j+=1
        err_count=int(errors.COUNT())
        if err_count!=last_count:
            last_count=err_count
            if err_count>=5:
                historic.printt('Errors | Critical | '+str(err_count))
        
        if err_count>=8:
            historic.printt("<@397738036592508931>. Errors :/")
            ERROR=True
            break
        
        if time.time()-t_errors>=300:
            historic.printt("Errors | 300s | "+errors.COUNT())
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
    if dt.check('robot_numbers'):
        anticheat_numbers.all_captcha()
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
    if dt.check('robot_numbers'):
        anticheat_numbers.all_captcha()
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)
    if dt.check('robot_numbers'):
        anticheat_numbers.all_captcha()
        cs.random_sleep(0.5)
