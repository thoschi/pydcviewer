#!/usr/bin/env python

import cv2
import os
import pyperclip


os.system('clear') 
imgstr = cv2.imencode('.png', cv2.imread('m_inactive.png', -1))[1].tobytes()
print(imgstr)
pyperclip.copy(str(imgstr))
input("inactive UI image string copied to clipboard (and printed above)... Continue?")

os.system('clear') 
imgstr = cv2.imencode('.png', cv2.imread('m_disabled.png', -1))[1].tobytes()
print(imgstr)
pyperclip.copy(str(imgstr))
input("disabled UI image string copied to clipboard (and printed above)... Continue?")


os.system('clear') 
imgstr = cv2.imencode('.png', cv2.imread('m_placeholder.png', -1))[1].tobytes()
print(imgstr)
pyperclip.copy(str(imgstr))
input("placeholder for UI image string copied to clipboard (and printed above)... Continue?")

#os.system('clear') 
#imgstr = cv2.imencode('.png', cv2.imread('ui_active.png', -1))[1].tobytes()
#print(imgstr)
#pyperclip.copy(str(imgstr))
#input("active UI image string copied to clipboard (and printed above)... Finished!")
