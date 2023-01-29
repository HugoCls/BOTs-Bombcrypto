import matchtemplate as templ
import clavier_souris as cs
import random as rd
from time import sleep

def find(img_modele):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        x,y=L[0][0],L[0][1]
        if w>25 and h>25:
            dx=rd.randint(10,w-10)
            dy=rd.randint(10,h-10)
            cs.move(x+dx,y+dy)
        else:
            cs.move(x+w/2,y+h/2)
        cs.clic_gauche()
        return(True)
    else:
        return(False) 

def find_which(img_modele):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        x,y=L[0][0],L[0][1]
        if w>25 and h>25:
            dx=rd.randint(10,w-10)
            dy=rd.randint(10,h-10)
            cs.move(x+dx,y+dy)
        else:
            cs.move(x+w/2,y+h/2)
        cs.clic_gauche()
        di,dj=int(x//645),int(y//470)
        p=4*dj+di
        return(True,p)
    else:
        return(False,-1) 

def find_all(img_modele,j=0):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        N=len(L)
        for i in range(N):
            if j==0:
                x,y=L[i][0],L[i][1]
            else:
                x,y=L[N-1-i][0],L[N-1-i][1]
            cs.move(x+w/2,y+h/2)
            cs.clic_gauche()
        return(True)
    else:
        return(False)

def check(img_modele):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        return(True)
    else:
        return(False)
    
def find_the_one(img_modele,i):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        x,y=L[0][0]+w/2,L[0][1]+h/2
        for j in range(len(L)):
            xj,yj=L[j][0],L[j][1]
            di,dj=i%4,i//4
            if di*645<=xj<=(di+1)*645 and dj*470<=yj<=(dj+1)*470:
                x,y=xj+w/2,yj+h/2
        cs.move(x,y)
        cs.clic_gauche()
        return(True)
    else:
        return(False)

def check_all(img_modele):
    found=[]
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        for j in range(len(L)):
            xj,yj=L[j][0],L[j][1]
            di,dj=int(xj//645),int(yj//470)
            p=4*dj+di
            found.append(p)
    return(found)    
    
def check_the_one(img_modele):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        for j in range(len(L)):
            xj,yj=L[j][0],L[j][1]
            di,dj=int(xj//645),int(yj//470)
            p=4*dj+di
            if p<=12:
                return(True,p)
    return(False,-1)

def check_precisely(img_modele,precision):
    L,w,h=templ.matchtemplate_personalized(img_modele,precision)
    if len(L)>=1:
        return(True)
    else:
        return(False)
    
def accounts_number():
    L,w,h=templ.matchtemplate('arrow')
    Lu,w,h=templ.matchtemplate('upgrade')
    return(len(L)+len(Lu))