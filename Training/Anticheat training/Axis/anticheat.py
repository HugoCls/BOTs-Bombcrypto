import cv2
import os
import numpy as np
import matchtemplate as templ

def rotateImage(image,angle):
    img = cv2.imread(os.getcwd()+'\\images\\'+image+'.png')
    img_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(img_center, angle, 1.0)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    I,J,k=result.shape
    for i in range(I):
        for j in range(J):
            x,y,z=result[i][j]
            if x==y==z==0:
                result[i][j]=[ 53,  68, 124]
    cv2.imshow('Detected',result)
    cv2.waitKey(0)

def numbers_positions():
    img = cv2.imread(os.getcwd()+'//images//number_patern.png')
    print(img.shape)
    for i in range(10):
        print(img[i][i])
     
def detecting_number(x,y):
    p,w,h=templ.width('number_patern')
    img_bg=cv2.imread(os.getcwd()+'//images//copy.png')
    img=img_bg[x:x+w,y:y+h]
    cv2.imshow('Detected',img)
    cv2.waitKey(0)
    

def test():
    L,w,h=templ.matchtemplate_cibled('number_patern','copy',0.7)
    numbers=L
    x,y=numbers[0][0],numbers[0][1]
    detecting_number(x,y)