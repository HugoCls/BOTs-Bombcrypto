import ocr
import matchtemplate as templ
import cv2
import os

def one_count(br):
    (x,y)=br.init_topleft
    (w,h)=br.init_size
    ocr.screenGrab(x,y,x+w,y+h)
    Lzzz,w,h=templ.matchtemplate_without_screen('zzz zzz 100%')
    return(len(Lzzz))

def count(br):
    M=0
    for j in range(15):
        p=one_count(br)
        if p>=M:
            M=p
    print('ZZZ | Screen ',br.i+1,' | ',M)
    return(M)