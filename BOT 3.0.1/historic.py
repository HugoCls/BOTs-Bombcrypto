import datetime
import os
from PIL import ImageGrab
import json
from urllib import request

def printt(content):
    now = datetime.datetime.now()
    mins=str(now.minute)
    if len(mins)==1:
        mins='0'+mins
    hour=str(now.hour)+':'+mins
    content=hour+' | '+content
    payload = {'content': content}

    headers = {'Content-Type': 'application/json','user-agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}

    WEBHOOK_URL = 'https://discord.com/api/webhooks/934463119298818109/-x2WPUflxowADyHuAsulCYu_oSGoZnuGvp3_MjnNN00ZW6Kykf3M3zeA3DS7U31uvaKG'

    req = request.Request(url=WEBHOOK_URL,data=json.dumps(payload).encode('utf-8'),headers=headers,method='POST')

    request.urlopen(req)

def screen():
    box = (0,0,2559,1439)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\Discord BOT\\screenshot.png', 'PNG')