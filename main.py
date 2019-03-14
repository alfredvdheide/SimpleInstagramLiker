import pyautogui
from random import *
import time
# failsafe = drag mouse top right.
# ensure that the picture 'hearticon.png' is visible on the screen to start.
pyautogui.PAUSE = 5 # 5 seconds till start
pyautogui.FAILSAFE = True # drag mouse top left to stop
likeCounter = 0
y = input("enable sleep?")
t = input("how many likes?")


while (int(likeCounter) <= int(t)):

    if((randrange(101) < 4) and (y == "yes")):
        x = randrange(1000)
        print("sleeping for: "+ str(x)+" seconds...")
        print("total likes botted: "+ str(likeCounter))
        time.sleep(x)
    else:
        try:
            x, y = pyautogui.locateCenterOnScreen('hearticon.png', grayscale=True, confidence=0.99)
            #print(x, y)
            x = (x / 2) - 42
            y = y / 2
            if((x or y) != None):
                pyautogui.click(x,y)
                likeCounter+=1
                print("Likes placed: " + str(likeCounter))
        except Exception:
            pass
            randomScrollAmount = uniform(1.0,20.0)
            #print("scrolling: "+str(randomScrollAmount))
            pyautogui.vscroll((randomScrollAmount*-1))


