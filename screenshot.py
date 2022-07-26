
# Author: José Victor Moreno
# Github: https://github.com/josevictormoreno

import pyautogui
import os
from PIL import ImageGrab

lista = os.listdir('./screenshots')
image = pyautogui.screenshot()
filename = './screenshots/image' + str(len(lista)+1) + '.png'
image.save(filename)