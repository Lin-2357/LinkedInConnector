import pyautogui
import time
import csv

link = 'https://www.linkedin.com/in/annie-king-37913a10b'
subject = 'shskdjfhskjdfhk'
text = 'jkhfhfdshfd'
with open('links.csv') as f:
    fr = csv.reader(f)
    for x in fr:
        link = x[0]
        print(link)
        fire = pyautogui.locateOnScreen("firefox.png")
        pyautogui.click(fire.left+10, fire.top+10)
        time.sleep(1)
        for i in link:
            pyautogui.hotkey(i)
        pyautogui.hotkey('enter')
        time.sleep(5)
        mes = pyautogui.locateOnScreen("message.png")
        pyautogui.click(mes.left+15, mes.top+15)
        time.sleep(2)
        sub = pyautogui.locateOnScreen("sub.png")
        pyautogui.click(sub.left+10, sub.top+10)
        for i in subject:
            pyautogui.hotkey(i)
        pyautogui.hotkey('tab')
        for i in text:
            pyautogui.hotkey(i)

        close = pyautogui.locateOnScreen("close.png")
        pyautogui.click(close.left+10, close.top+10)
        time.sleep(1)