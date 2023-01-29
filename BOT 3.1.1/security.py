import pyautogui
import requests

def get_key(user):
    r=requests.get('http://140.82.55.213/'+str(user))
    r=r.text
    #print(r)
    key = r[2:len(r)-2]
    return(key) 

def password_correct(user):
    key=get_key(user)
    password=pyautogui.password(text='enter your password', title=str(user), default='', mask='*')
    if password==key:
        return(True)
    else:
        return(False)