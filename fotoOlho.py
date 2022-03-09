# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:49:08 2022

@author: DISRCT
"""

import cv2

image = cv2.imread('imagem.jpg')
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

txt = 'Olho psicodelico'

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(image2, txt, (30,250), font, 0.8, (255,255,255), 4, cv2.LINE_AA)

cv2.imshow("Olho psicodelico", image2)
inverter = cv2.flip(image2, 1)
cv2.imshow("Olho psicodelico Invertido", inverter)



cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()