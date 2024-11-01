import pyautogui
import time
import keyboard 
import pygame
import os

time.sleep(1)
image= "C:\Users\prati\OneDrive\Documents\Clicker BOT INTERN\image.png"
def recognition():
   try:
    pos1 = pyautogui.locateOnScreen(image) 
    if pos1 is not None:
      print('moving to 1st case') 
      pyautogui.click(x=930, y=1075)
      time.sleep(0.1)
      pyautogui.click(x=815 ,y=392)
      time.sleep(0.1)
      keyboard.write('Let me solve your doubt')
      keyboard.press('enter')

   except Exception as e:
        time.sleep(1.5)
        recognition()
        
        
recognition()