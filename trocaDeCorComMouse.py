# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:32:24 2022

@author: DISRCT
"""

import cv2
import numpy as np
import random

a = 0
b = 0
c = 0

def funcao(event,x,y,flags,param):
    global a,b,c
    if event == cv2.EVENT_MOUSEWHEEL:
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)

cv2.namedWindow('janela')
cv2.setMouseCallback('janela', funcao)
while True:
    img = np.full((512,512,3), (a,b,c), np.uint8)
    cv2.imshow('janela', img)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()