import pyautogui
import time
import sys

pyautogui.FAILSAFE = False
sleepSeconds = None

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    sleepSeconds = 2 * 60
else:
    sleepSeconds = int(sys.argv[1]) * 60
while(True):
    pyautogui.moveRel(10,0)
    pyautogui.press("shift")
    time.sleep(0.5)
    pyautogui.moveRel(-10,0)
    pyautogui.press("shift")
    time.sleep(sleepSeconds)
