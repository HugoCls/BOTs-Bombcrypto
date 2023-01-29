import clavier_souris as cs

def yellow(x,y):
    R,G,B=cs.pixelRGB(x,y)
    if 220<=R and 100<=G<=150 and B<=50 :
        return(True)
    else :
        return(False)

def gray(x,y):
    R,G,B=cs.pixelRGB(x,y)
    if 100<=R<=150 and 100<=G<=150 and 100<=B<=150 :
        return(True)
    else :
        return(False)
    
def dark_gray(x,y):
    R,G,B=cs.pixelRGB(x,y)
    if 100<=R<=170 and 100<=G<=170 and 100<=B<=170 :
        return(True)
    else :
        return(False)