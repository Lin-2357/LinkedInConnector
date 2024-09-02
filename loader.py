import pyautogui
import time
import csv

link = 'https://www.linkedin.com/in/annie-king-37913a10b'
subject = 'UC Berkeley student looking for possible career positions'
text = """I hope this message finds you well. My name is Jiayin Lin, and I am a Computer Science and Mathematics student at UC Berkeley, set to graduate next summer. With a solid background in software development, data analysis, and full-stack engineering, I have gained experience in building scalable web applications and working with technologies like Python, HTML, and Java. I have technical internship experience in various fields including healthcare and education, where I worked on software development and data analysis.
Due to unforeseen family circumstances, my partner and I are facing significant challenges with our immigration status as our financial support has been abruptly withdrawn. We are urgently seeking employment opportunities that can offer visa sponsorship. I am open to any role that leverages my technical skills, and I do not require a high salary. 
My primary concern is finding a position that can support our basic needs and secure our ability to remain in the U.S.
If there are any opportunities available or if you could offer any advice, I would be immensely grateful. Thank you for your time and consideration."""
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
        name = x[2]
        for i in "Dear "+name+":\n":
            pyautogui.hotkey(i)
        for i in text:
            pyautogui.hotkey(i)

        send = pyautogui.locateOnScreen("send.png")
        pyautogui.click(send.left+10, send.top+10)
        time.sleep(1)
        close = pyautogui.locateOnScreen("close.png")
        pyautogui.click(close.left+10, close.top+10)
        time.sleep(1)