import random as rd
import clavier_souris as cs
import colors
import time

class Hero():
    def __init__(self):
        self.work_state=False
        self.rest_state=False
        self.home_state=False
        self.hp_percentage=0
        self.work_topleft=(100,150)

    def infos(self):
        return(str(self.work_state)+' | '+str(self.rest_state)+' | '+str(self.home_state)+' | '+str(self.hp_percentage))

    def set_work(self,state):
        self.work_state=state
        #print('New work_state is:'+str(state))

    def set_rest(self,state):
        self.rest_state=state
        #print('New rest_state is:'+str(state))

    def set_home(self,state):
        self.home_state=state
        #print('New house_state is:'+str(state))

    def set_hp_percentage(self,percentage):
        self.hp_percentage=percentage
        #print('New hp_percentage is:'+str(percentage))

    def send_to_work(self,trueorfalse):
        if trueorfalse:
            w,h=37,23
            (x,y)=self.work_topleft
            dx=rd.randint(5,w-5)
            dy=rd.randint(5,h-5)
            cs.move(x+dx,y+dy)
            cs.clic_gauche()
            """
            t=time.time()
            while cs.pixelRGB(x+dx,y+dy)==(237, 215, 186) or time.time()-t>=2:
                cs.random_sleep(0.05)
            """
        self.set_work(trueorfalse)

    def send_to_rest(self,trueorfalse):
        if trueorfalse:
            w,h=37,23
            (x,y)=self.work_topleft
            x+=40
            dx=rd.randint(5,w-5)
            dy=rd.randint(5,h-5)
            cs.move(x+dx,y+dy)
            cs.clic_gauche()
        self.set_rest(trueorfalse)

    def send_to_home(self,trueorfalse):
        if trueorfalse:
            w,h=37,23
            (x,y)=self.work_topleft
            x+=80
            if not colors.gray(x+w/2,y+4*(h/5)):
                dx=rd.randint(5,w-5)
                dy=rd.randint(5,h-5)
                cs.move(x+dx,y+dy)
                cs.clic_gauche()
                self.set_home(trueorfalse)
            else:
                self.send_to_rest(True)
                self.set_home(False)