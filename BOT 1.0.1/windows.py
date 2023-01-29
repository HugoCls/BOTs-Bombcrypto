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
    print(ret)
    for i in range(len(ret)):
        fenetres.append(ret[i][1])
    return(fenetres)

def dimensions(fenetre):
    win=pygetwindow.getWindowsWithTitle(fenetre)[0]
    return(win.size)

def repositionner(fenetre,x,y,i):
    windows=pygetwindow.getWindowsWithTitle(fenetre)
    if len(windows)>=i+1:
        win = pygetwindow.getWindowsWithTitle(fenetre)[i]
        x,y=int(x),int(y)
        win.moveTo(x,y)

def redimensionner(fenetre,x,y):
    win=pygetwindow.getWindowsWithTitle(fenetre)[0]
    win.resizeTo(x,y)

def mettre_premier_plan(fenetre):
    window = pygetwindow.getWindowsWithTitle(fenetre)[0]
    if window.isActive == False:
        pywinauto.application.Application().connect(handle=window._hWnd).top_window().set_focus()

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

def show_chromes():
    windows=pygetwindow.getWindowsWithTitle('Bombcrypto - Google Chrome')
    for win in windows:
        print(str(win)+'\n\n')