import ocr
import matchtemplate as templ

def one_count(i):
    if i==0:
        ocr.screenGrab(10,228,964,888)
    elif i==1:
        ocr.screenGrab(974,228,1919,888)
    elif i==2:
        ocr.screenGrab(1929,228,2880,888)
    elif i==3:
        ocr.screenGrab(2890,228,3839,888)
    Lzzz,w,h=templ.matchtemplate_without_screen('zzz zzz')
    return(len(Lzzz))

def count(i):
    M=0
    for j in range(15):
        p=one_count(i)
        if p>=M:
            M=p
    print('ZZZ | Screen ',i+1,' | ',M)
    return(M)