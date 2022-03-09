# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:21:02 2022

@author: DISRCT
"""

import cv2
import numpy as np

mode = True
r = 0
b = 0
g = 0
font = cv2.FONT_HERSHEY_SIMPLEX
    
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img(x,y), 20,(b,r,g), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    cv2.putText(img, 'Red=' +str(r), (10,30), font, 1.0, (255,255,255), 4, cv2.LINE_AA)
    cv2.putText(img, 'Blue=' +str(b), (10,80), font, 1.0, (255,255,255), 4, cv2.LINE_AA)
    cv2.putText(img, 'Green=' +str(g), (10,130), font, 1.0, (255,255,255), 4, cv2.LINE_AA)
    k = cv2.waitKey(20) & 0xFF
    if k == ord('r'):
        r+=10
        cv2.circle(img,(140,30),50,(0,0,0), -1)
        if r > 255:
            r = 0;
    if k == ord('b'):
        b+=10
        cv2.circle(img,(140,80),50,(0,0,0), -1)
        if b > 255:
            b = 0;
    if k == ord('g'):
        g+=10
        cv2.circle(img,(140,130),50,(0,0,0), -1)
        if g > 255:
            g = 0;
            
    if k == ord('x'):
        break
cv2.destroyAllWindows()


'''
    elif cv2.waitKey(20) & 0xFF == 114:
        valorVermelho = cores['Red']+10
        cv2.putText(img, valorVermelho, (120,100), font, 1.0, (191,0,191), 4, cv2.LINE_AA)
    elif cv2.waitKey(20) & 0xFF == 98:
        valorBlue = cores['Blue'] = cores['Blue']+10
        cv2.putText(img, valorBlue, (120,100), font, 1.0, (191,0,191), 4, cv2.LINE_AA)
    elif cv2.waitKey(20) & 0xFF == 103:
        valorVerde = cores['Green'] + 10
        cv2.putText(img, valorVerde, (120,100), font, 1.0, (191,0,191), 4, cv2.LINE_AA)
'''