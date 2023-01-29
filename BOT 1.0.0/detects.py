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