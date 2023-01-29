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
        image = ImageGrab.grab()
        xpuz,ypuz,Xmin=get_xypuz()
        xmoy,xmax=middle_x_grey(image,xpuz,ypuz)
        ymoy=middle_y_grey(image,xmoy,ypuz)
        cs.move(xmoy,ymoy)
        ymax=max_y_grey(image,xmoy,ymoy)
        bar_percentage=(xmoy-Xmin)/346
        print(bar_percentage)
        Lmc,wc,hc=templ.matchtemplate('yellow')
        LMc,wc,hc=templ.matchtemplate('brown1')
        if len(LMc)==0:
            LMc,wc,hc=templ.matchtemplate('brown2')
        xmcurseur,ycurseur=Lmc[0][0]+wc/2,Lmc[0][1]+hc/2
        xMcurseur,ynone=templ.closer(xmcurseur,ycurseur,LMc)
        xMcurseur+=wc/2
        xbar=int(xmcurseur+bar_percentage*(xMcurseur-xmcurseur))
        cs.move(xmcurseur,ycurseur)
        cs.mouse.press(cs.Button.left)
        sleep(0.5)
        cs.pyautogui.moveTo(xbar,ycurseur,0.1)
        if bar_percentage<=0.40:
            cs.mouse.release(cs.Button.left)
            
        else:
            image = ImageGrab.grab()
            k=1
            while still_grey(image,xmax-1,ymax+5) and k<=100:
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
    return(False)
    

def get_xypuz():
    L,w,h=templ.matchtemplate('robot')
    xf=0
    j=0
    if len(L)>=1:
        xstart,ystart=L[0][0],get_ystart()
        templ.screen()
        img=cv2.imread(os.getcwd()+'//images//screenshot.png')
        for i in range(100):
            image=img[ystart:ystart+20,xstart+i*5:xstart+20+i*5]
            cv2.imwrite(os.getcwd()+'//images//cropped_img.png',image)
            #cv2.imshow('Detected',image)
            #cv2.waitKey(0)
            (R,G,B)=templ.averageRGB('cropped_img')
            if R==G==B:
                #cs.move(xstart+i*5+10,ystart+10)
                xf+=xstart+i*5+10
                j+=1
        xpuz,ypuz=xf/j,ystart+10
        return(xpuz,ypuz,xstart-68)

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
    if abs(xmax-xmin)<=40:
        return(middle_x_grey(image,xpuz,ypuz-1))
    return(int((xmax+xmin)/2),int(xmax))

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

def max_y_grey(image,xmoy,ymoy):
    j=0
    for i in range(0,40):
        (Rm,Gm,Bm) = image.getpixel((xmoy, ymoy-i))
        if Rm==Gm==Bm:
            None
        else:
            if j==0:
                j=i
    if j<=20:
        return(max_y_grey(image,xmoy-2,ymoy))
    else:
        return(ymoy-j)

def xy_grey(image,xmoy,ypuz):
    return(middle_x_grey(image,xmoy,ypuz),middle_y_grey(image,xmoy,ypuz))

def still_grey(image,xmax,ymax):
    j=0
    for x in range(xmax-10,xmax):
        (R,G,B) = image.getpixel((x, ymax-1))
        #print(R,G,B)
        if R==G==B and R!=0:
            j+=1
    return(j>=1)