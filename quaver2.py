from mss import mss
from PIL import Image
import time
import numpy as np
import pydirectinput as pdi
import pyautogui as pg
import cv2

region = {'left': 734, 'top': 1084, 'width': 10, 'height': 181}
sct = mss()
press = False

while True:
    img = sct.grab(region)
    img = Image.frombytes('RGB', (img.width, img.height), img.rgb).convert('L')
    if (img.getpixel((5,121))!= 0) and (img.getpixel((5,54))== 0):
        pdi.press('e')   
    elif (img.getpixel((5,121))!= 0) and (img.getpixel((5,54))!= 0):
        while (img.getpixel((5,121))!= 0) and (img.getpixel((5,54))!= 0):
            pdi.keyDown('e')
        print('out')
