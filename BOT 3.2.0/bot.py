import time
import detects as dt
import refresh as fresh
import heroes as h
import historic
import errors
import windows as wd
import classes as C
from time import sleep

def infinite_loop(j):
    # create an empty list to store browsers
    browsers=[]
    # get all windows with the title 'Bombcrypto'
    windows=wd.pygetwindow.getWindowsWithTitle('Bombcrypto')
    # get the number of windows
    N=len(windows)
    # get the sizes and positions of the windows
    (sizes,positions)=wd.positionner_bombcrypto(windows)
    # iterate through the windows and create a browser object for each one
    for i in range(N):
        size=sizes[i]
        topleft=positions[i]
        browsers.append(C.Browser(windows[i],time.time(),topleft,size,i))

    # set the time when the refresh function was last called
    trefresh=time.time()
    # reset the error count
    errors.RESET()
    # set the time when the error count was last checked
    t_errors=time.time()
    # store the last error count
    last_count=int(errors.COUNT())
    # initialize counters for maps and loops
    map_count=0
    loop_count=0
    while True:
        # increment the loop counter
        loop_count+=1
        # check for the 'actualiser' button
        dt.find('actualiser')
        
        # check for the 'ok_tw' button and sleep for 0.5 seconds if found
        if dt.find('ok_tw'):
            sleep(0.5)
        
        # check for the 'new map' button and increment the map counter if found
        if dt.find('new map'):
            map_count+=1
            #historic.printt("Map | "+str(map_count))
        # check for the 'close' button and sleep for 0.5 seconds if found
        if dt.find('close'):
            sleep(0.5)
        # check for the 'treasure hunt' button and sleep for 0.5 seconds if found
        while dt.find('treasure hunt'):
            sleep(0.5)
            
        # call the connect function
        fresh.connect()
        
        # if j is 0, set the time of the heroes check for all browsers to 1000 seconds ago
        if j==0:
            for i in range(N):
                browsers[i].t_heroes-=1000
            j+=1
        
        # if 6 minutes have passed since the last refresh, call the refresh function
        if time.time()-trefresh>=6*60:
            dt.find_all('arrow')
            sleep(0.1)
            dt.find_all('treasure hunt')
            trefresh=time.time()

        # iterate through the browsers
        for i in range(N):
           br=browsers[i]
           # if 1000 seconds have passed since the last heroes check, check the heroes for that browser
           if time.time()-br.t_heroes>=1000:
                # Check if the time since the last check for heroes is greater than or equal to 1000
                br.maximize()
                # Maximize the browser window
                loop()
                # Execute the loop function
                br.minimize()
                # Minimize the browser window
                wd.positionner_bombcrypto(windows)
                # Position the browser window
                br.t_heroes=time.time()
                # Update the time of the last check for heroes
                sleep(0.5)
                break
                # Exit the loop

        err_count=int(errors.COUNT())
        # Get the number of errors
        if err_count!=last_count:
            # Check if the number of errors is not equal to the last count
            last_count=err_count
            # Update the last count
            if err_count>=6:
                # Check if the number of errors is greater than or equal to 6
                historic.printt('Errors | Critical | '+str(err_count))
                # Print the number of errors
        
        if err_count>=30:
            # Check if the number of errors is greater than or equal to 30
            historic.printt("BOT STOPPED <@user_discord_id> BOT STOPPED")
            # Print that the bot has stopped using 
            break
            # Exit the loop

        
def loop():
    # Define the loop function
    j=0
    # Initialize variable j
    while dt.find('new map 100%'):
        # Check if the picture "new map 100%"  is into the screen
        sleep(0.5)
        
    if dt.find('arrow 100%'):
        # Check if the picture arrow is into the screen
        sleep(0.5)
        
    if dt.find('heroes 100%'):
        # Check if the image "heroes 100%" is found
        sleep(0.5)
        
    t_upgrade=time.time()
    # Initialize variable t_upgrade
    while dt.check('upgrade 100%')==False and time.time()-t_upgrade<=20:
        # Check if the image "upgrade 100%" is not found and the time since t_upgrade is less than or equal to 20
        sleep(0.1)
        # Wait for 0.1 seconds
        if dt.check('new map 100%'):
            # Check if the picture "new map 100%"  is into the screen
            j=1
            # Update the value of j