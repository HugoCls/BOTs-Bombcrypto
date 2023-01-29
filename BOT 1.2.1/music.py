import vlc
from time import sleep
import time

def play():
    t_alarm=time.time()
    alarm=vlc.MediaPlayer('error_alarm.m4a')
    while time.time()-t_alarm<=300:
        if (time.time()-t_alarm)%25<=2:
            alarm=vlc.MediaPlayer('error_alarm.m4a')
        sleep(1)
        if alarm.is_playing()==0:
            sleep(0.5)
            alarm.play()
        sleep(0.5)
    alarm.stop()