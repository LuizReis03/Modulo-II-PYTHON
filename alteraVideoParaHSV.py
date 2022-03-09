# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:43:42 2022

@author: DISRCT
"""

import cv2

cap = cv2.VideoCapture('video_car.mp4') #video puxado da maquina

fourcc = cv2.VideoWriter_fourcc(*"DIVX") 
output = cv2.VideoWriter("video_hsv.mp4", fourcc, 30.0, (300,300)) #informa como está salvando o video

while (cap.isOpened()):
    ret, frame = cap.read() #ret é para verificar se tem frame no video, enquanto tiver ele roda 
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #altera cor do video
        frame2 = cv2.resize(frame,(300,300)) #altera tamanho do video
        output.write(frame2)
        cv2.imshow('frame', frame2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #ao pressionar "q" o video para
            break
    else:
        break
        
cap.release() #reinicia a variavel
output.release() #reinicia a variavel
cv2.destroyAllWindows()