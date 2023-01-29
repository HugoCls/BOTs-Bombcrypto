import matchtemplate as templ
import clavier_souris as cs

def find(img_modele):
    L,w,h=templ.matchtemplate(img_modele)
    if len(L)>=1:
        x,y=L[0][0]+w/2,L[0][1]+h/2
        cs.move(x,y)
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
        if i==0 or i==2:
            for j in range(len(L)):
                if 0<=L[j][0]<=1271:
                    if i==0:
                        if  L[j][1]<=752:
                            x,y=L[j][0]+w/2,L[j][1]+h/2
                    else:
                        if  L[j][1]>=752:
                            x,y=L[j][0]+w/2,L[j][1]+h/2
        elif i==1 or i==3:
            for j in range(len(L)):
                if 1271<=L[j][0]<=2559:
                    if i==2:
                        if  L[j][1]<=752:
                            x,y=L[j][0]+w/2,L[j][1]+h/2
                    else:
                        if  L[j][1]>=752:
                            x,y=L[j][0]+w/2,L[j][1]+h/2
        cs.move(x,y)
        cs.clic_gauche()
        return(True)
    else:
        return(False)
    
def check_precisely(img_modele,precision):
    L,w,h=templ.matchtemplate_personalized(img_modele,precision)
    if len(L)>=1:
        return(True)
    else:
        return(False)