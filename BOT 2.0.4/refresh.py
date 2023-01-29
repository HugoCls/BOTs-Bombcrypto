import clavier_souris as cs
import detects as dt
import matchtemplate as templ
from time import sleep
import time
import anticheat

def auto_refresh():
    while dt.find('new map'):
        sleep(0.5)
    while dt.find('arrow'):
        sleep(0.5)
    while dt.find('treasure hunt'):
        sleep(0.5)

def refresh():
    result=dt.find('ok')
    if result==True:
        cs.appuyer(cs.F5)
        sleep(6)
        dt.find('connect')
        sleep(1)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
        sleep(3)
        if dt.check('busy_fox')==True and dt.check('sign')==False:
            dt.find('busy_fox')
            sleep(1.5)
        dt.find('sign')
        sleep(2)
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
        result=dt.find('connect')
        sleep(1)
        if dt.check('robot')==True:
            anticheat.detect_puzzle(0)
            sleep(1.5)
        dt.find('sign')
        print('Connect | '+str(int(time.time()-t0))+'s')