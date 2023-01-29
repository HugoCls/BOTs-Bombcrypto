import detects as dt
import clavier_souris as cs
import time
import heroes as h
import refresh as fresh
import matchtemplate as templ

def unpause_all(N):
    for i in range(N):
        unpause_loop(i)

def pause_all(N):
    for i in range(N):
        debug()
        pause_loop(i)

def unpause_loop(i):
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
        h.all_to_work()
    else:
        fresh.connect()
        cs.random_sleep(0.5)

    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)

def pause_loop(i):
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
        h.all_to_sleep()
    else:
        fresh.connect()
        cs.random_sleep(0.5)

    if dt.find('close'):
        cs.random_sleep(0.5)
    if dt.find('close'):
        cs.random_sleep(0.5)

def debug(N):
    L,w,h=templ.matchtemplate('arrow')
    while len(L)<N:
        L,w,h=templ.matchtemplate('arrow')
        if fresh.refresh():
            cs.random_sleep(0.5)
        if fresh.connect():
            cs.random_sleep(0.5)
        if dt.find('treasure hunt'):
            cs.random_sleep(0.5)
        if dt.find('new map'):
           cs.random_sleep(0.5)
        if dt.find('new map'):
           cs.random_sleep(0.5)
        if fresh.connect():
            cs.random_sleep(0.5)
    while dt.find('new map'):
       cs.random_sleep(0.5)