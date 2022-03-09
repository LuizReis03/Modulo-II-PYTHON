# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:11:02 2022

@author: DISRCT
"""

import cv2
import numpy as np

def draw_circle(event, x,y, flags,param):
    if event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img,(x,y),40,(191,0,191), -1)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.ellipse(img, (x, y), (60, 20), 0, 0, 360, (500, 150, 150), -1)
        
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()