# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:26:26 2022

@author: DISRCT
"""

import cv2

cap = cv2.VideoCapture('video_car.mp4')

fourcc = cv2.VideoWriter_fourcc(*"MJPG")
output = cv2.VideoWriter("novo_video.avi", fourcc, 20.0, (640,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        output.write(frame)
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
output.release()
cv2.destroyAllWindows()