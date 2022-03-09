# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:51:20 2022

@author: DISRCT
"""

import cv2

cap = cv2.VideoCapture('pixar_inv.mp4')
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
output = cv2.VideoWriter("novo_video.avi", fourcc, 30.0, (720,1280))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,(0,30))
        output.write(frame)
        
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()
output.release()
cv2.destroyAllWindows()