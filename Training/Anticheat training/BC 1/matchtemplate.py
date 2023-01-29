# Python program to illustrate
# template matching
import cv2
import numpy as np
import pyautogui
import os
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


def screen():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.getcwd()+'\\images\\screenshot.png', image)
   
def show_matchtemplate(img_modele):
    screen()
    img_rgb = cv2.imread(os.getcwd()+'\\images\\screenshot.png')
     
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
     
    # Read the template
    template = cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png',0)
     
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
     
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
     
    # Specify a threshold
    threshold = 0.8
     
    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
     
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        print(pt[0],pt[1])
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
     
    # Show the final image with the matched area.
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    
def matchtemplate(img_modele):
    screen()
    img_rgb = cv2.imread(os.getcwd()+'\\images\\screenshot.png')
     
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
     
    # Read the template
    template = cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png',0)
     
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
     
    # Specify a threshold
    threshold = 0.8
     
    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    L=[]
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        L.append((pt[0],pt[1]))
    return(L,w,h)

##PERSONALIZED FUNCTIONS

def show_matchtemplate_personalized(img_modele,precision):
    screen()
    img_rgb = cv2.imread(os.getcwd()+'\\images\\screenshot.png')
     
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
     
    # Read the template
    template = cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png',0)
     
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
     
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
     
    # Specify a threshold
    threshold = precision
     
    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    L=[]
    for pt in zip(*loc[::-1]):
        L.append((pt[0],pt[1]))
    L=points(L)
    for i in range(len(L)):
        cv2.rectangle(img_rgb, L[i], (L[i][0] + w, L[i][1] + h), (0,255,255), 2)
    print(L)
    # Show the final image with the matched area.
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    
def matchtemplate_personalized(img_modele,precision):
    screen()
    img_rgb = cv2.imread(os.getcwd()+'\\images\\screenshot.png')
     
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
     
    # Read the template
    template = cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png',0)
     
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
     
    # Specify a threshold
    threshold = precision
     
    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    L=[]
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        L.append((pt[0],pt[1]))
    return(L,w,h)

##CIBLED FUNCTIONS

def show_matchtemplate_cibled(img_modele,img_cible,precision):
    img_rgb = cv2.imread(os.getcwd()+'\\images\\'+img_cible+'.png')
     
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
     
    # Read the template
    template = cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png',0)
     
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
     
    # Specify a threshold
    threshold = precision
     
    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    L=[]
    for pt in zip(*loc[::-1]):
        L.append((pt[0],pt[1]))
    L=points(L)
    for i in range(len(L)):
        cv2.rectangle(img_rgb, L[i], (L[i][0] + w, L[i][1] + h), (0,255,255), 2)
     
    # Show the final image with the matched area.
    print(L)
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)

def matchtemplate_cibled(img_modele,img_cible,precision):
    img_rgb = cv2.imread(os.getcwd()+'\\images\\'+img_cible+'.png')
     
    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
     
    # Read the template
    template = cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png',0)
     
    # Store width and height of template in w and h
    w, h = template.shape[::-1]
    # Perform match operations.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
     
    # Specify a threshold
    threshold = precision
     
    # Store the coordinates of matched area in a numpy array
    loc = np.where( res >= threshold)
    L=[]
    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        L.append((pt[0],pt[1]))
    L=points(L)
    return(L,w,h)

##TOOLS FUNCTIONS

def distance(x1,y1,x2,y2):
    return(np.sqrt((x2-x1)**2+(y2-y1)**2))

def points(L):
    if len(L)==1 or len(L)==0:
        return(L)
    else:
        for i in range(len(L)-1):
            xi,yi=L[i][0],L[i][1]
            for j in range(i+1,len(L)):
                xj,yj=L[j][0],L[j][1]
                d=distance(xi,yi,xj,yj)
                if d<=20:
                    del(L[j])
                    return(points(L))
        return(L)

def closer(x,y,L):
    m=distance(x,y,L[0][0],L[0][1])
    j=0
    for i in range(len(L)):
        if distance(x,y,L[0][0],L[0][1])<=m:
            m=distance(x,y,L[0][0],L[0][1])
            j=i
    return(L[j][0],L[j][1])

def width(img_name):
    img = cv2.imread(os.getcwd()+'\\images\\'+img_name+'.png')
    return(img.shape[::-1])

def all_images():
    files=os.listdir('./images')
    images=[]
    for file in files:
        if '.png' in file:
            images.append(file[:-4])
    return(images)
        
def get_images(key_word):
    images=all_images()
    cibled_images=[]
    for image in images:
        if key_word in image:
            cibled_images.append(image)
    return(cibled_images)

def test(img_modele):
    import cv2
    import numpy
    img=cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png')
    image=img[200:400,300:800]
    avg_color_per_row = numpy.average(image, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    cv2.imshow('Detected',image)
    cv2.waitKey(0)
    print(avg_color)
    
def averageRGB(img_modele):
    import cv2
    import numpy
    image=cv2.imread(os.getcwd()+'\\images\\'+img_modele+'.png')
    avg_color_per_row = numpy.average(image, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    for i in range(3):
        avg_color[i]=int(avg_color[i])
    L=(list(avg_color))
    return(L[0],L[1],L[2])