import pyautogui, time, threading, subprocess, os, psutil,cv2
from pathlib import Path
os.startfile("C:/Users/HP/AppData/Roaming/Zoom/bin/Zoom.exe")
time.sleep(1)
button_location = pyautogui.locateOnScreen(str(Path("images\join1.png")),confidence = 0.7)
pyautogui.click(button_location)

time.sleep(1)

#entering the meeting
pyautogui.write('--------------YOUR MEETING ID HERE--------------')  #meeting id
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.hotkey('CTRL', 'a')
pyautogui.write('--------------YOUR MEETING NAME HERE--------------') #Your name in meeting
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
# join the meeting

time.sleep(3)
pyautogui.write('--------------MEETING PASSWORD  HERE--------------')    #Meeting Password
time.sleep(1)
#pyautogui.press('tab')
#pyautogui.press('enter')
join = pyautogui.locateOnScreen(str(Path("images\join3.png")),confidence = 0.5)
pyautogui.click(join)
time.sleep(10)
joinj = pyautogui.locateOnScreen(str(Path("images\join6.PNG")),confidence = 0.4)
pyautogui.click(joinj)
time.sleep(5)   
#joining breakout room

pyautogui.moveTo(766,272)
pyautogui.click()
pyautogui.press('tab')
for i in range(10):
    pyautogui.press("down")
    pyautogui.press("left")
pyautogui.press("down")
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(10)
#joined breakout room
#chat
#chat = pyautogui.locateOnScreen(str(Path("images\chat1.PNG")),confidence = 0.5)
#pyautogui.click(chat)
pyautogui.hotkey('alt', 'h')
time.sleep(1)
pyautogui.write('---------------ATTENDANCE MESSAGE HERE----------------------------') 
pyautogui.press('enter')
time.sleep(10)
#leave room
#lr = pyautogui.locateOnScreen(str(Path("images\lr.PNG")),confidence = 0.5)
#pyautogui.click(lr)
pyautogui.hotkey('alt', 'F4')
time.sleep(1)

#leave meeting
lm = pyautogui.locateOnScreen(str(Path("images\leave meeting.png")),confidence = 0.5)
pyautogui.click(lm)  









