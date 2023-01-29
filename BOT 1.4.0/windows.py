import win32gui
import pygetwindow
import pywinauto
from time import sleep
import clavier_souris as cs
import os

def get_window_titles():
    ret = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            txt = win32gui.GetWindowText(hwnd)
            if txt:
                ret.append((hwnd,txt))

    win32gui.EnumWindows(winEnumHandler, None)
    fenetres=[]
    for i in range(len(ret)):
        fenetres.append(ret[i][1])
    return(fenetres)

def dimensions(fenetre):
    win=pygetwindow.getWindowsWithTitle(fenetre)[0]
    return(win.size)

def repositionner(fenetre,x,y):
    win = pygetwindow.getWindowsWithTitle(fenetre)[0]
    x,y=int(x),int(y)
    win.moveTo(x,y)


def redimensionner(fenetre,x,y):
    windows=pygetwindow.getWindowsWithTitle(fenetre)
    for win in windows:
        win.resizeTo(x,y)

def positionner_bombcrypto():
    windows=pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')
    redimensionner('Bombcrypto - Google Chrome',1061,765)
    for i in range(len(windows)):
        #print(windows[i])
        win=windows[i]
        #print(win.topleft, win.size)
        x,y=-5,-47
        if i==1:
            x,y=1074,-47
        elif i==2:
            x,y=-5,672
        elif i==3:
            x,y=1074,672
        win.moveTo(x,y)
        
def premier_plan_bombcrypto():
    windows=pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')
    for i in range(len(windows)):
        win=windows[i]
        (x,y)=win.topleft
        (w,h)=win.size        
        if y<=100:
            cs.move(x+w/2,y+10)
            cs.clic_gauche()
            sleep(0.05)

def mettre_premier_plan(fenetre):
    (x,y)=cs.curseur()
    window = pygetwindow.getWindowsWithTitle(fenetre)[0]
    if window.isActive == False:
        pywinauto.application.Application().connect(handle=window._hWnd).top_window().set_focus()
    cs.move(x,y)

def mettre_arriere_plan(fenetre):
    window = pygetwindow.getWindowsWithTitle(fenetre)[0]
    if window.isActive == False:
        pywinauto.application.Application().connect(handle=window._hWnd).top_window().minimize()

def fenetre_premier_plan():
    window = win32gui.GetForegroundWindow()
    active_window_name = win32gui.GetWindowText(window)
    return(active_window_name)

def position(fenetre):
    win=pygetwindow.getWindowsWithTitle(fenetre)[0]
    return(win.topleft)
