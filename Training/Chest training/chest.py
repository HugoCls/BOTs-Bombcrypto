import matchtemplate as templ
import os
import time

def count(chest):
    templ.screen()
    names=templ.get_images(chest)
    positions=[]
    t=time.time()
    for name in names:
        t1=time.time()
        L,w,h=templ.matchtemplate_personalized(name, 0.6)
        print(time.time()-t1)
        for coordonate in L:
            positions.append(coordonate)
    print(time.time()-t)
    t0=time.time()
    positions=templ.points(positions)
    print(time.time()-t0)
    return(len(positions))