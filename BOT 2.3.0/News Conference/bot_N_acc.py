from time import sleep
import time
import detects as dt
import heroes as h
import refresh as fresh
import zzz
import anticheat_reveal
import clavier_souris as cs
##WHOLE BOT:



def loop_with_zzz(N):
    j=0
    zzz_numbers=[4,4,3,3]
    t=time.time()
    while j!=-1:
        if fresh.refresh():
            cs.random_sleep(0.5)
        if fresh.connect():
            cs.random_sleep(0.5)
        if dt.check('Reveal Number'):
            anticheat_reveal.all_captcha()
            cs.random_sleep(0.5)
        if dt.find('treasure hunt'):
            cs.random_sleep(0.5)
        if dt.check('Reveal Number'):
            anticheat_reveal.all_captcha()
            cs.random_sleep(0.5)
        if dt.find('new map'):
           cs.random_sleep(0.5)
        if dt.check('Reveal Number'):
            anticheat_reveal.all_captcha()
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
                        if dt.check('Reveal Number'):
                            anticheat_reveal.all_captcha()
                            cs.random_sleep(0.5)
                    loop(i)
        else:
            for i in [2,3]:
                if zzz.count(i)>=zzz_numbers[i]:
                    while dt.find('new map'):
                        cs.random_sleep(0.5)
                        if dt.check('Reveal Number'):
                            anticheat_reveal.all_captcha()
                            cs.random_sleep(0.5)
                    loop(i)
        j+=1

def loop(i):
    j=0
    while dt.find('new map'):
        cs.random_sleep(0.5)
    if dt.find_the_one('arrow',i):
        cs.random_sleep(0.5)
    if dt.find('heroes'):
        cs.random_sleep(0.5)
    if dt.check('Reveal Number'):
        anticheat_reveal.all_captcha()
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
    if dt.check('Reveal Number'):
        anticheat_reveal.all_captcha()
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)
    if dt.check('Reveal Number'):
        anticheat_reveal.all_captcha()
        cs.random_sleep(0.5)
