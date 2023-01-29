import bot
import security
import pyautogui

if security.password_correct('Vypz26'):
    N=int(pyautogui.prompt(text='', title='Accounts number:' , default='1'))
    bot.infinite_loop(0,N)