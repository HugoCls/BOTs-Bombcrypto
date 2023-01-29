import random as rd
import clavier_souris as cs
import colors
import time
import pyautogui
from time import sleep

class Hero():
    def __init__(self):
        # Initialize the state of the hero to False for work, rest, and home
        self.work_state=False
        self.rest_state=False
        self.home_state=False
        # Initialize the hero's health percentage to 0
        self.hp_percentage=0
        # Initialize the top left coordinates of the hero's work location
        self.work_topleft=(100,150)

    def infos(self):
        # Return a string with the current state of the hero
        return(str(self.work_state)+' | '+str(self.rest_state)+' | '+str(self.home_state)+' | '+str(self.hp_percentage))

    def set_work(self,state):
        # Set the work state of the hero to the given state
        self.work_state=state

    def set_rest(self,state):
        # Set the rest state of the hero to the given state
        self.rest_state=state

    def set_home(self,state):
        # Set the home state of the hero to the given state
        self.home_state=state

    def set_hp_percentage(self,percentage):
        # Set the health percentage of the hero to the given percentage
        self.hp_percentage=percentage

    def send_to_work(self,trueorfalse):
        if trueorfalse:
            # Set the width and height of the work location
            w,h=37,23
            # Get the top left coordinates of the work location
            (x,y)=self.work_topleft
            # Generate random x and y coordinates within the work location
            dx=rd.randint(5,w-5)
            dy=rd.randint(5,h-5)
            # Move the cursor to the random coordinates and click
            cs.move(x+dx,y+dy)
            cs.clic_gauche()
            """
            t=time.time()
            while cs.pixelRGB(x+dx,y+dy)==(237, 215, 186) or time.time()-t>=2:
                cs.random_sleep(0.05)
            """
        # Set the work state of the hero to the given state
        self.set_work(trueorfalse)

    def send_to_rest(self,trueorfalse):
        if trueorfalse:
            # Set the width and height of the rest location
            w,h=37,23
            # Get the top left coordinates of the work location
            (x,y)=self.work_topleft
            # Add 40 to the x coordinate to get the top left coordinates of the rest location
            x+=40
            # Generate random x and y coordinates within the rest location
            dx=rd.randint(5,w-5)
            dy=rd.randint(5,h-5)
            # Move the cursor to the random coordinates and click
            cs.move(x+dx,y+dy)
            cs.clic_gauche()
        self.set_rest(trueorfalse)

    def send_to_home(self,trueorfalse):
        # Check if the input is True
        if trueorfalse:
            w,h=37,23
            (x,y)=self.work_topleft
            x+=80
            # Check if the color at the specified coordinates is gray
            if not colors.gray(x+w/2,y+4*(h/5)):
                dx=rd.randint(5,w-5)
                dy=rd.randint(5,h-5)
                cs.move(x+dx,y+dy)
                cs.clic_gauche()
                self.set_home(trueorfalse)
            # If the color is gray, call the send_to_rest function and set home to false
            else:
                self.send_to_rest(True)
                self.set_home(False)
                
class Browser():
    def __init__(self,win,t_heroes,init_topleft,init_size,i):
        # Initialize instance variables
        self.win=win
        self.t_heroes=t_heroes
        self.init_size=init_size
        self.init_topleft=init_topleft
        self.i=i

    def infos(self):
        # Returns a string with the window and t_heroes information
        return(str(self.win)+' | '+str(self.t_heroes))

    def get_win(self):
       # Returns the window
       return(self.win)
   
    def get_t_heroes(self):
        # Returns t_heroes
        return(self.t_heroes)
    
    def change_t_heroes(self,t):
        # Changes the value of t_heroes
        self.t_heroes=t
        
    def maximize(self):
        # Move the window to the top left corner of the screen
        self.win.moveTo(0,0)

        # Resize the window to full screen
        self.win.resizeTo(1920,1080)

        # Move the mouse to the center of the screen
        pyautogui.moveTo(800,800)
        pyautogui.click(button='left')

        sleep(0.1)
        # Use the ctrl + key to zoom in 4 times
        for i in range(4):
            cs.ctrl(cs.PLUS)
            sleep(0.05)

        sleep(0.1)
            
    def minimize(self):
        # Get the initial top left coordinates and size
        (x,y)=self.init_topleft
        (w,h)=self.init_size
        self.win.moveTo(x,y)

        # Resize the window to its initial size
        self.win.resizeTo(w,h)

        # Move the mouse to the center of the window
        pyautogui.moveTo(int(x+w/2),int(y+h/2))
        pyautogui.click(button='left')

        sleep(0.1)
        for i in range(4):
            cs.ctrl(cs.MINUS)
            sleep(0.05)

        sleep(0.1)