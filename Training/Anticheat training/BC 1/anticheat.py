import cv2
import os
import numpy as np
import matchtemplate as templ
import clavier_souris as cs
import pyautogui
from PIL import ImageGrab
from time import sleep
import detects as dt

def anticheat_grey(x,y):
    R,G,B=cs.pixelRGB(x,y)
    return(R==G==B)

def detect_puzzle(e):
    if dt.find('connect')==True:
        sleep(1)
    L,w,h=templ.matchtemplate('robot')
    if len(L)>=1:
        Xmin=L[0][0]-68
        Xmax=Xmin+346
        x0,y0=L[0][0]+20,L[0][1]+140
        image = ImageGrab.grab()
        count=0
        sames=0
        (Rs,Gs,Bs) = image.getpixel((x0, y0))
        y=get_ystart()
        for i in range(100):
            x=x0+2*i
            cs.move(x,y)
            (R,G,B) = image.getpixel((x, y))
            if count>=5:
                xpuz,ypuz=x,y
                xmoy,xmax=middle_x_grey(image,xpuz,ypuz)
                ymoy=middle_y_grey(image,xmoy,ypuz)
                cs.move(xmoy,ymoy)
                bar_percentage=(xmoy-Xmin)/346
                print(bar_percentage)
                Lmc,wc,hc=templ.matchtemplate('yellow')
                LMc,wc,hc=templ.matchtemplate('brown1')
                if len(LMc)==0:
                    LMc,wc,hc=templ.matchtemplate('brown2')
                xmcurseur,ycurseur=Lmc[0][0]+wc/2,Lmc[0][1]+hc/2
                xMcurseur=LMc[0][0]+wc/2
                
                xbar=int(xmcurseur+bar_percentage*(xMcurseur-xmcurseur))
                #return(xmax,ymoy,ycurseur)
                
                cs.move(xmcurseur,ycurseur)
                cs.mouse.press(cs.Button.left)
                sleep(0.5)
                cs.pyautogui.moveTo(xbar,ycurseur,0.1)
                if bar_percentage<=0.40:
                    cs.mouse.release(cs.Button.left)
                    
                else:
                    image = ImageGrab.grab()
                    k=1
                    while still_grey(image,xmax-1,ymoy+15) and k<=200:
                        image=ImageGrab.grab()
                        cs.pyautogui.moveTo(xbar+k,ycurseur,0.01)
                        k+=1
                    cs.mouse.release(cs.Button.left)
                sleep(0.5)
                if dt.check('robot')==False:
                    sleep(1.5)
                    dt.find('sign')
                    return(True)
                else:
                    if e<3:
                        return(detect_puzzle(e+1))
                    else:
                        cs.ctrl(cs.F5)
                        return(False)
            
            elif R==G==B:
                count+=1
                if (Rs,Gs,Bs)==(R,G,B):
                    sames+=1
                else:
                    sames=0
                if sames>=3:
                    count=0
                Rs,Gs,Bs=R,G,B
                    
            else:
                count=0
                sames=0
    return(False)

def test():
    for i in range(50):
        print(dt.check('connecting'))
        sleep(0.2)

def get_ystart():
    L,w,h=templ.matchtemplate('robot')
    x,y=L[0][0],L[0][1]
    x0,y0=x-50,y+70
    j=1
    while True:
        cs.move(x0,y0+8*j)
        R,G,B=cs.pixelRGB(x0,y0+8*j)
        if (R,G,B)==(181,112,82):
            j+=1
        else:
            break
    return(y0+8*j+10)

def middle_x_grey(image,xpuz,ypuz):
    xmin=xpuz
    xmax=xpuz
    start=False
    end=False
    for i in range(0,40):
        (Rm,Gm,Bm) = image.getpixel((xpuz-i, ypuz))
        if Rm==Gm==Bm and start==False:
            xmin=xpuz-i
        else:
            start==True

        (RM,GM,BM) = image.getpixel((xpuz+i, ypuz))
        if RM==GM==BM and end==False:
            xmax=xpuz+i
        else:
            end==True
    return(int((xmax+xmin)/2),xmax)

def middle_y_grey(image,xmoy,ypuz):
    ymin=ypuz
    ymax=ypuz
    start=False
    end=False
    for i in range(0,40):
        (Rm,Gm,Bm) = image.getpixel((xmoy, ypuz-i))
        if Rm==Gm==Bm and start==False:
            ymin=ypuz-i
        else:
            start==True

        (RM,GM,BM) = image.getpixel((xmoy, ypuz+i))
        if RM==GM==BM and end==False:
            ymax=ypuz+i
        else:
            end==True
    return(int((ymax+ymin)/2))


def still_grey(image,xmax,ymoy):
    j=0
    for x in range(xmax-10,xmax):
        (R,G,B) = image.getpixel((x, ymoy))
        #print(R,G,B)
        if R==G==B and R!=0:
            j+=1
    return(j>=1)