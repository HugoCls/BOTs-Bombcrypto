import clavier_souris as cs
import detects as dt
import matchtemplate as templ
from time import sleep
import time
import anticheat_reveal
import errors

def auto_refresh():
    while dt.find('new map'):
        cs.random_sleep(0.5)
    while dt.find('arrow'):
        cs.random_sleep(0.5)
    while dt.find('treasure hunt'):
        cs.random_sleep(0.5)

def refresh():
    result=dt.find('ok')
    if result==True:
        errors.ADD(2)
        cs.appuyer(cs.F5)
        cs.random_sleep(6)
        dt.find('connect')
        cs.random_sleep(1)
        if dt.check('robot_numbers')==True:
            anticheat_reveal.all_captcha()
        cs.random_sleep(3)
        if dt.check('busy_fox')==True and dt.check('sign')==False:
            dt.find('busy_fox')
            cs.random_sleep(1.5)
        dt.find('sign')
        cs.random_sleep(2)
        dt.find('connect')
        return(True)
    return(False)

def connect():
    tconnexion=time.time()
    while dt.find('bombcrypto connexion')==True and dt.check('connect')==False:
        if time.time()-tconnexion>=40:
            print('Connect | Expired')
            cs.ctrl(cs.F5)
    while dt.find('bombcrypto mainscreen')==True:
        t0=time.time()
        if dt.find('connect'):
            errors.ADD(2)
            cs.random_sleep(1)
        if dt.check('robot_numbers')==True:
            anticheat_reveal.all_captcha()
            cs.random_sleep(1.5)
        dt.find('sign')
        print('Connect | '+str(int(time.time()-t0))+'s')