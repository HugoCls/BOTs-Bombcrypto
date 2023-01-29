import matchtemplate as templ
import clavier_souris as cs
import random as rd

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
            di,dj=i%2,i//2
            if di*643<=xj<=(di+1)*643 and dj*470<=yj<=(dj+1)*470:
                x,y=xj+w/2,yj+h/2
        cs.move(x,y)
        cs.clic_gauche()
        return(True)
    else:
        return(False)

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