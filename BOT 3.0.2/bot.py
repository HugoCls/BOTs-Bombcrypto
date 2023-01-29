import time
import detects as dt
import refresh as fresh
import heroes as h
import historic
import errors
import clavier_souris as cs
import random as rd
import windows as wd
from time import sleep

workers=['construction','factory','health','man_construction','man_factory','man_health','man_office','office','woman_construction','woman_factory','woman_health','woman_office']
work_smiles=[]
for i in range(len(workers)):
    work_smiles.append(':'+workers[i]+'_worker:')

def infinite_loop(j,N):
    wd.positionner_bombcrypto()
    windows=wd.pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')
    heroes_t=[]
    F5_t=[]
    for i in range(N):
        heroes_t.append(time.time())
        F5_t.append(time.time()+4*60-5*i*60)
    trefresh=time.time()
    #ERROR THINGS
    errors.RESET()
    t_errors=time.time()
    ERROR=False
    last_count=int(errors.COUNT())
    #COUNTS
    map_count=0
    loop_count=0
    while True:
        loop_count+=1
        dt.find('actualiser')
            
        if dt.find_all('new map'):
            map_count+=1
            ##◘historic.printt("Map | "+str(map_count))
        if dt.find_all('close'):
            cs.random_sleep(0.5)
        if dt.find_all('treasure hunt'):
            cs.random_sleep(0.5)
            
        fresh.connect()
        
        if j==0:
            for i in range(N):
                heroes_t[i]-=1000
            j+=1
        
        if time.time()-trefresh>=rd.randint(5*60,6*60):
            dt.find_all('arrow')
            cs.random_sleep(0.5)
            dt.find_all('treasure hunt')
            trefresh=time.time()
        """
        for i in range(N):
            if time.time()-F5_t[i]>=N*5*60:
                dt.find_the_one('chrome_refresh',i)
                #◘historic.logs(str(i)+' | :x:')
                F5_t[i]=time.time()
                sleep(3)
                fresh.connect()
                break
        """
        for i in range(N):
            if time.time()-heroes_t[i]>=1000 and i in dt.check_all('arrow'):
                while dt.find('treasure hunt'):
                    cs.random_sleep(0.5)
                loop(i)
                heroes_t[i]=time.time()
                break
            
        err_count=int(errors.COUNT())
        if err_count!=last_count:
            last_count=err_count
            if err_count>=10:
                None
                #◘historic.printt('Errors | '+str(err_count)+' | :no_entry_sign:')
        
        if err_count>=30:
            None
            #◘historic.printt("BOT STOPPED <@150673899963678720> BOT STOPPED")
            break
        
        if time.time()-t_errors>=500:
            nbr=dt.accounts_number()
            if N-1<=nbr<N:
                None
                #◘historic.printt('Accounts | '+str(nbr)+' | :warning:')
            elif nbr<N-1:
                None
                #◘historic.printt('Accounts | '+str(nbr)+' | :no_entry: | <@150673899963678720>')
            else:
                None
                #◘historic.printt('Accounts | '+str(nbr)+' | :low_brightness:')
            if err_count<=10:
                None
                #◘historic.printt("Errors | "+errors.COUNT()+' | :white_check_mark:')
            
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
    t_upgrade=time.time()
    while dt.check('upgrade')==False and time.time()-t_upgrade<=20:
        cs.random_sleep(0.1)
        if dt.check_the_one('new map')[1]==i:
            j=1
            break
    if j==1:
        return(None)
    result,p=dt.check_the_one('upgrade')
    rd.shuffle(work_smiles)
    #◘historic.heroes(str(p)+' | '+work_smiles[0])
    h.heroes_entirely()

    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)
    if dt.find('treasure hunt'):
        cs.random_sleep(0.5)