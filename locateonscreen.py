import pyautogui
import time

time.sleep(5)
location = pyautogui.locateOnScreen('image2.png')
print(location) 